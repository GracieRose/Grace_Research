# Grace Woolson, Summer 2019
import math
import os
import sys
import csv



def check_if_constant(instruction):

    is_constant = False
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    #booleans
    if instruction == "true" or instruction == "false":
        is_constant = True

    #integers/floats
    if instruction[0] in numbers:
        is_constant = True

    if instruction[0] == "-":
        is_constant = True

    #tags
    if instruction[:3] == "tag":
        is_constant = True

    #characters
    if instruction[0] == "\\":
        is_constant = True

    #strings
    if instruction[0] == '\"':
        is_constant = True

    #vectors
    if instruction[0] == "[":
        is_constant = True


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




def stats(all_genomes, funcs):

    freqs = {}
    count = 0

    for (genome, errors) in all_genomes:
        count += 1

        #only collects data for programs that completely fail*************************
        if not "0" in errors:

            for i in range(0, len(genome) - 1):
                word = genome[i]

                if word == ":instruction":
                    func = genome[i+1]
                    is_constant = check_if_constant(func)
                    if not is_constant:
                        if func in freqs:
                            freqs[func] += 1
                        else:
                            freqs[func] = 1
                        

    for key in freqs:
        freqs[key] = round((freqs[key] / float(count)), 2)


    return freqs





def collect():

    problems = ["number-io", "checksum", "collatz-numbers", "compare-string-lengths", "count-odds", "digits", "double-letters", "even-squares", "for-loop-index", "grade", "last-index-of-zero", "median", "mirror-image", "negative-to-zero", "pig-latin", "replace-space-with-newline", "scrabble-score", "small-or-large", "smallest", "string-differences", "string-lengths-backwards", "sum-of-squares", "super-anagrams", "syllables", "vector-average", "vectors-summed", "wallis-pi", "word-stats", "x-word-lines"]

    outputFilePrefix = "data"
    outputFileSuffix = ".csv"


    verbose = False
    if len(sys.argv) >= 3:
        #outputDirectory = "C:/Users/livel/Desktop/Research"
        outputDirectory = sys.argv[2]
    else:
        print "Please provide an directory"
        exit(1)

    if len(sys.argv) > 1:
        destination = sys.argv[1]
        i = int(destination[3])
    else:
        print("please provide a destination file in the format <filename>.csv")
        exit(1)


    destfile = open(destination, mode="w")
    destwriter = csv.writer(destfile)

    #I want to use the problem, not the tags
    #category = directories[outputDirectory] ##UPDATE********************************************************8

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    #dirList = os.listdir(outputDirectory)

    problem = ""
    for topic in problems:
        if topic in outputDirectory:
                problem = topic


    header = [problem]
    destwriter.writerow(header)

    all_funcs = []
    all_genomes = []

    #CHANGE THIS
    #while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:

    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    success = False
    simpl = False
    running_error = sys.maxint


    for line in f:

        if not line.startswith("uuid"):
            #the first line always starts with uuid I THINK************************
            
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
                    if not func in all_funcs:
                        all_funcs.append(func)


            all_genomes.append((genes_line, end))


    freqs = stats(all_genomes, all_funcs)

    funcslist = []
    freqslist = []

    for key in freqs:

        funcslist.append(key)  
        freqslist.append(freqs[key])


    destwriter.writerow(funcslist)
    destwriter.writerow(freqslist)


def main():
    collect()

if __name__ == '__main__':
    main()