import math
import os
import sys
import csv

# Could include more?
#Grace Woolson
##########################################################################################
#################################### Novelty Lexicase ####################################
##########################################################################################
"""

"/home/thelmuth/Results/clustering-bench/checksum/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/collatz-numbers/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/compare-string-lengths/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/count-odds/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/digits/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/double-letters/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/even-squares/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/for-loop-index/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/grade/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/last-index-of-zero/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/median/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/mirror-image/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/negative-to-zero/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/number-io/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/pig-latin/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/replace-space-with-newline/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/scrabble-score/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/smallest/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/small-or-large/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/string-differences/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/string-lengths-backwards/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/sum-of-squares/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/super-anagrams/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/syllables/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/vector-average/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/vectors-summed/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/wallis-pi/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/word-stats/lexicase/logs/"
"/home/thelmuth/Results/clustering-bench/x-word-lines/lexicase/logs/"

"""
directories = {"/home/thelmuth/Results/clustering-bench/checksum/lexicase/logs/" : ["string_handling", "arithmetic", "I/O"],
                "/home/thelmuth/Results/clustering-bench/checksum/baseline-uniform/logs/" : ["string_handling", "arithmetic", "I/O"],
                "/home/thelmuth/Results/clustering-bench/collatz-numbers/baseline-uniform/logs/" : ["arithmetic", "comparison"],
                "/home/thelmuth/Results/clustering-bench/compare-string-lengths/baseline-uniform/logs/" : ["boolean", "comparison", "string_handling"],
                "/home/thelmuth/Results/clustering-bench/count-odds/baseline-uniform/logs/" : ["vectors", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/count-odds/lexicase/logs/" : ["vectors", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/digits/baseline-uniform/logs/" : ["I/O", "arithmetic", "string_handling"],
                "/home/thelmuth/Results/clustering-bench/double-letters/baseline-uniform/logs/" : ["I/O", "string_handling", "comparison"],
                "/home/thelmuth/Results/clustering-bench/double-letters/lexicase/logs/" : ["I/O", "string_handling", "comparison"],
                "/home/thelmuth/Results/clustering-bench/even-squares/baseline-uniform/logs/" : ["I/O", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/for-loop-index/baseline-uniform/logs/" : ["I/O", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/grade/baseline-uniform/logs/" : ["I/O", "comparison"],
                "/home/thelmuth/Results/clustering-bench/last-index-of-zero/baseline-uniform/logs/" : ["comparison", "vectors"],
                "/home/thelmuth/Results/clustering-bench/median/baseline-uniform/logs/" : ["I/O", "comparison"],
                "/home/thelmuth/Results/clustering-bench/mirror-image/baseline-uniform/logs/" : ["vectors", "boolean", "comparison"],
                "/home/thelmuth/Results/clustering-bench/negative-to-zero/lexicase/logs/" : ["vectors", "comparison"],
                "/home/thelmuth/Results/clustering-bench/negative-to-zero/baseline-uniform/logs/" : ["vectors", "comparison"],
                "/home/thelmuth/Results/clustering-bench/number-io/baseline-uniform/logs/" : ["I/O", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/pig-latin/baseline-uniform/logs/" : ["I/O", "string_handling"],
                "/home/thelmuth/Results/clustering-bench/replace-space-with-newline/lexicase/logs/" : ["string_handling", "I/O", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/replace-space-with-newline/baseline-uniform/logs/" : ["string_handling", "I/O", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/scrabble-score/lexicase/logs/" : ["string_handling", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/scrabble-score/baseline-uniform/logs/" : ["string_handling", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/smallest/baseline-uniform/logs/" : ["I/O", "comparison"],
                "/home/thelmuth/Results/clustering-bench/small-or-large/baseline-uniform/logs/" : ["I/O", "comparison"],
                "/home/thelmuth/Results/clustering-bench/string-differences/baseline-uniform/logs/" : ["string_handling", "comparison", "I/O"],
                "/home/thelmuth/Results/clustering-bench/string-lengths-backwards/lexicase/logs/" : ["I/O", "string_handling", "vectors"],
                "/home/thelmuth/Results/clustering-bench/string-lengths-backwards/baseline-uniform/logs/" : ["I/O", "string_handling", "vectors"],
                "/home/thelmuth/Results/clustering-bench/sum-of-squares/baseline-uniform/logs/" : ["arithmetic"],
                "/home/thelmuth/Results/clustering-bench/super-anagrams/baseline-uniform/logs/" : ["boolean", "string_handling", "comparison"],
                "/home/thelmuth/Results/clustering-bench/syllables/lexicase/logs/" : ["I/O", "string_handling", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/syllables/baseline-uniform/logs/" : ["I/O", "string_handling", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/vector-average/lexicase/logs/" : ["vectors", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/vector-average/baseline-uniform/logs/" : ["vectors", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/vectors-summed/baseline-uniform/logs/" : ["vectors", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/wallis-pi/baseline-uniform/logs/" : ["arithmetic"],
                "/home/thelmuth/Results/clustering-bench/word-stats/baseline-uniform/logs/" : ["file", "I/O", "string_handling", "arithmetic"],
                "/home/thelmuth/Results/clustering-bench/x-word-lines/baseline-uniform/logs/" : ["I/O", "string_handling"]}


outputFilePrefix = "log"
outputFileSuffix = ".txt"


#directories = ["C:/Users/livel/Desktop/tournament/number-io", "C:/Users/livel/Desktop/double-letters"]
#directories = {"C:/Users/livel/Desktop/tournament/number-io" : ["I/O", "arithmetic"]}
#directories = {"C:/Users/livel/Desktop/syllables" : ["I/O", "string_handling", "arithmetic"]}


verbose = False
if (len(sys.argv) >= 3 and sys.argv[2] == "print"):
    verbose = True


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



# Don't have to change anything below!

if len(sys.argv) > 1:
    destination = sys.argv[1]
else:
    print("please provide a destination file in the format <filename>.csv")
    exit(1)


destfile = open(destination, mode="w")
destwriter = csv.writer(destfile)


for outputDirectory in directories:

    print outputDirectory

    category = directories[outputDirectory]

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)

    header = [category]
    #header = [outputDirectory, category]

    destwriter.writerow(header)

    i = 0
    while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
        gen = 0

        if verbose:
            print
            print "--------------------------------------------------"
            print "------------------ Run %i ------------------------" % i
            print "--------------------------------------------------"
            print

        runcount = "Run %i" % i
        destwriter.writerow([runcount])

        fileName = (outputFilePrefix + str(i) + outputFileSuffix)
        f = open(outputDirectory + fileName)

        #success = False
        #simpl = False
        funcs_list = []

        for line in f:
            if line.startswith("Lexicase best program: "):
                if funcs_list != []:
                    destwriter.writerow(funcs_list)

                #print line
                # removes "best program"
                funcs_list = line.split()[3:]
                #removes parentheses
                funcs_list[0] = funcs_list[0][1:]
                funcs_list[-1] = funcs_list[-1][:-1]
                #indicates this program was not a solution
                funcs_list = ["Failed"] + deparenthasize(funcs_list)

                if verbose:
                    print "Gen %i" % gen
                    print funcs_list
                    print

                gen += 1

            elif line.startswith("Best program: "):
                if funcs_list != []:
                    destwriter.writerow(funcs_list)

                #print line
                # removes "best program"
                funcs_list = line.split()[2:]
                #removes parentheses
                funcs_list[0] = funcs_list[0][1:]
                funcs_list[-1] = funcs_list[-1][:-1]
                #indicates this program was not a solution
                funcs_list = ["Failed"] + deparenthasize(funcs_list)

                if verbose:
                    print "Gen %i" % gen
                    print funcs_list
                    print

                gen += 1

            if line.startswith("Successful program: "):
                #removes "Successful Program"
                funcs_list[0] = "Successful"
                funcs_list = deparenthasize(funcs_list)
                destwriter.writerow(funcs_list)   
                #success = True

                if verbose:
                    print "Gen %i" % gen
                    print funcs_list
                    print
            """
            if simpl == True:

                if verbose:
                    print "Simplification after 1000 steps:"
                    print line

                # removes "program"
                funcs_list = line.split()[1:]
                #removes parentheses
                funcs_list[0] = funcs_list[0][1:]
                funcs_list[-1] = funcs_list[-1][:-1]
                #indicates this program was not a solution
                funcs_list = ["Simplified:"] + deparenthasize(funcs_list)
                destwriter.writerow(funcs_list)
                break

            if success and line.startswith("step: 1000"):
                simpl = True
            """

        i += 1
