# Grace Woolson, Summer 2019
import os
import sys
import csv



def check_if_constant(instruction):

    is_constant = True

    instr_types = ["in", "autoconstructive", "boolean", "char", "code", "environment", "exec", "float", "genome", "gtm", "integer", "noop", "print", "return", "string", "vector", "zip"]

    for category in instr_types:
        if instruction.startswith(category):
            is_constant = False
            break


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




def stats(all_genomes):

    freqs = {}
    count = 0

    "Calculating stats"

    for (genome, errors) in all_genomes:

        #only collects data for programs that completely fail*************************
        if not "0" in errors:
            this_run = []
            count += 1

            for i in range(0, len(genome) - 1):
                word = genome[i]

                if word == ":instruction":
                    func = genome[i+1]
                    is_constant = check_if_constant(func)

                    if (not is_constant) and (not func in this_run):
                        this_run.append(func)
                        if func in freqs:
                            freqs[func] += 1
                        else:
                            freqs[func] = 1
                        

    for key in freqs:
        print key, freqs[key]
        freqs[key] = round((freqs[key] / float(count)), 2)
        print freqs[key]
        print

    print "Total number of programs: ", count

    return freqs

def find_path(directory):
    #ex: takes /home/gwoolson/csvdata/collatz-numbers/data2.csv -> /home/gwoolson/csvdata/collatz-numbers/

    if directory[-10] == "/":
        path = directory[:-9]
    else:
        path = directory[:-10]

    print path
    return path


def collect():

    #problems = ["number-io", "checksum", "collatz-numbers", "compare-string-lengths", "count-odds", "digits", "double-letters", "even-squares", "for-loop-index", "grade", "last-index-of-zero", "median", "mirror-image", "negative-to-zero", "pig-latin", "replace-space-with-newline", "scrabble-score", "small-or-large", "smallest", "string-differences", "string-lengths-backwards", "sum-of-squares", "super-anagrams", "syllables", "vector-average", "vectors-summed", "wallis-pi", "word-stats", "x-word-lines"]

    #outputFilePrefix = "data"
    #outputFileSuffix = ".csv"


    verbose = False
    if len(sys.argv) > 2:
        #outputDirectory = "C:/Users/livel/Desktop/Research"
        outputDirectory = sys.argv[2]
        isdonepath = find_path(outputDirectory)
    else:
        print "Please provide a file to open"
        exit(1)

    if len(sys.argv) > 1:
        destination = sys.argv[1]

        donenum = destination[3:]
        donenum = int(donenum[:-4])
    else:
        print("please provide a destination file in the format <filename>.csv")
        exit(1)

    isdonefile = isdonepath + "donetest/done%i.txt" % donenum 


    destfile = open(destination, mode="w")
    destwriter = csv.writer(destfile)

    all_funcs = []
    all_genomes = []


    #fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory)

    #success = False
    #simpl = False

    for line in f:

        if not line.startswith("uuid"):
            #the first line always starts with uuid************************
            
            #removes  d1355282-86ad-4964-aa74-d040ff2385f3,0,0,[],:random,98,86, i think
            genes_line = line.split(",")[7:]
            genes_line = ",".join(genes_line)[1:].split()
            end = genes_line[-1]

            genes_line = genes_line[:-1]
            end_instr = end.split(",")[0][:-1]

            end = end.split(",")[1:]

            genes_line.append(end_instr)

            genes_line = debracket(deparenthasize(genes_line))

            for i in range(0, len(genes_line) - 1):
                if genes_line[i] == ":instruction":
                    func = genes_line[i + 1]
                    #print func
                    """if not func in all_funcs:
                        all_funcs.append(func)"""


            all_genomes.append((genes_line, end))

    #freqs = stats(all_genomes, all_funcs)
    freqs = stats(all_genomes)

    funcslist = []
    freqslist = []

    for key in freqs:

        funcslist.append(key)  
        freqslist.append(freqs[key])


    destwriter.writerow(funcslist)
    destwriter.writerow(freqslist)

    is_finished = open(isdonefile, mode="w")

def main():
    collect()

if __name__ == '__main__':
    main()