import sys
import csv

def check_if_constant(instruction):

    is_constant = True

    instr_types = ["in", "autoconstructive", "boolean", "char", "code", "environment", "exec", "float", "genome", "gtm", "integer", "noop", "print", "return", "string", "vector", "zip"]

    for category in instr_types:
        if instruction.startswith(category):
            is_constant = False
            break

    #print instruction, is_constant
    return is_constant


def deparenthasize(lst):

    newlst = []
        
    for i in range(0, len(lst)):

        word = lst[i]
        #print "Before: %s" % word
        done = False

        while not done:
            if word == "(":
                word = "" 
            elif len(word) > 0 and word[0] == "(":
                word = word[1:]
            if len(word) > 0 and word[-1] == ")":
                word = word[:-1]

            if len(word) > 0:
                if word[0] == "(" or word[-1] == ")":
                    done = False
                else:
                    done = True
            else:
                done = True

        if not word == "":
            newlst.append(word)

        #print "After: %s" % word

    return newlst



def debracket(lst):
    newlist = []

    for word in lst:

        newword = word

        if word[0] == "{":
            newword = newword[1:]

        if word[-1] == "}":
            newword = newword[:-1]

        newlist.append(newword)

    return newlist


def find_funcs_and_simplify(genome, freqs):

    funcslist = []

    for i in range(0, len(genome) - 1):

        if genome[i] == ":instruction":
            func = genome[i+1][:-1]

            is_constant = check_if_constant(func)
            if (not is_constant) and (not func in funcslist):
                
                if func in freqs:
                    freqs[func] += 1
                else:
                    freqs[func] = 1
                funcslist.append(func)


    return freqs



def find_path(directory):
    #ex: takes /home/gwoolson/csvdata/collatz-numbers/data2.csv -> /home/gwoolson/csvdata/collatz-numbers/

    if directory[-10] == "/":
        path = directory[:-9]
    else:
        path = directory[:-10]

    return path



def map():

    if len(sys.argv) > 1:
        outputFile = sys.argv[1]
        isdonepath = find_path(outputFile)

    else:
        print "Please provide a file to read"
        exit(1)

    if len(sys.argv) > 2:
        destination = sys.argv[2]

        donenum = destination[7:]
        donenum = int(donenum[:-4])

    else:
        print("please provide a destination file in the format <filename>.csv")
        exit(1)

    isdonefile = isdonepath + "donetest/done%i.csv" % donenum
    print isdonefile

    destfile = open(destination, mode="w")
    destwriter = csv.writer(destfile)

    f = open("/state/partition1/data%i.csv" % donenum)

    gen = 0
    gencount = 0
    freqs = {}
    destwriter.writerow(["Gen 0"])

    for line in f:
        if not line.startswith("uuid"):
            
            line = line.split(",")
            this_gen = int(line[1])

            if this_gen != gen:

                funcslist = []
                freqslist = []
                for key in freqs:
                    funcslist.append(key)
                    #turns the frequency into a percentage
                    freqslist.append(freqs[key]/float(gencount))

                    #this ensures that the lists will always be in the same order
                    freqs[key] = 0

                if gen = 0:
                    destwriter.writerow(funcslist)

                destwriter.writerow(freqslist)

                destwriter.writerow(["Gen %i" % this_gen])
                gen = this_gen
                gencount = 0  #7/8

            gencount += 1   #7/8

            line = ",".join(line[7:-201])

            line = debracket(deparenthasize(line[1:-1].split()))
            
            freqs = find_funcs_and_simplify(line, freqs)

    funcslist = []
    freqslist = []
    for key in freqs:
        funcslist.append(key)
        freqslist.append(freqs[key])

    #destwriter.writerow(funcslist)
    destwriter.writerow(freqslist)

    is_finished = open(isdonefile, mode="w")

def main():
    map()

if __name__ == '__main__':
    main()