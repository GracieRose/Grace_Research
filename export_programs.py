import math
import os
import sys
import csv

# Set these before running:
#Grace Woolson
##########################################################################################
#################################### Novelty Lexicase ####################################
##########################################################################################

## genops UMAD
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/compare-string-lengths"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/double-letters"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/last-index-of-zero"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/mirror-image"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/negative-to-zero"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/replace-space-with-newline"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/scrabble-score"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/syllables"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/vector-average"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/x-word-lines"


## genops standard
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-standard/replace-space-with-newline"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-standard/syllables"


## gens-1000/genops-UMAD
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-UMAD/replace-space-with-newline"


## gens-1000/genops-original
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/compare-string-lengths"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/double-letters"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/last-index-of-zero"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/median"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/mirror-image"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/negative-to-zero"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/pig-latin"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/replace-space-with-newline"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/scrabble-score"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/syllables"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/vector-average"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/x-word-lines"


## gens-1000/no-novelty-genops-original
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/compare-string-lengths"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/double-letters"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/last-index-of-zero"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/median"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/mirror-image"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/negative-to-zero"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/pig-latin"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/replace-space-with-newline"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/scrabble-score"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/syllables"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/vector-average"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/x-word-lines"


##########################################################################################
################################## Parent Selection v2 ###################################
##########################################################################################

## novelty-search
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/novelty-search/double-letters"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/novelty-search/scrabble-score"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/novelty-search/syllables"
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/novelty-search/x-word-lines"


## tournament
#outputDirectory = "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/tournament/number-io"


#outputDirectory = "C:/Users/livel/Desktop/tournament/number-io"
#outputDirectory = "C:/Users/livel/Desktop/double-letters"
"""
directories = ["/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/compare-string-lengths",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/double-letters",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/last-index-of-zero",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/mirror-image",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/negative-to-zero",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/replace-space-with-newline",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/scrabble-score",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/syllables",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/vector-average",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/x-word-lines",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-standard/replace-space-with-newline",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-standard/syllables",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-UMAD/replace-space-with-newline",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/compare-string-lengths",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/double-letters",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/last-index-of-zero",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/median",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/mirror-image",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/negative-to-zero",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/pig-latin",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/replace-space-with-newline",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/scrabble-score",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/syllables",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/vector-average",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/x-word-lines",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/compare-string-lengths",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/double-letters",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/last-index-of-zero",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/median",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/mirror-image",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/negative-to-zero",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/pig-latin",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/replace-space-with-newline",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/scrabble-score",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/syllables",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/vector-average",
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/x-word-lines",
                "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/novelty-search/double-letters",
                "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/novelty-search/scrabble-score",
                "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/novelty-search/syllables",
                "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/novelty-search/x-word-lines",
                "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/tournament/number-io"]
"""


directories = {"/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/compare-string-lengths" : ["boolean", "comparison", "string-handling"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/double-letters" : ["I/O", "string-handling", "comparison"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/last-index-of-zero" : ["comparison", "vectors"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/mirror-image" : ["vectors", "boolean", "comparison"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/negative-to-zero" : ["vectors", "comparison"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/replace-space-with-newline" : ["string-handling", "I/O", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/scrabble-score" : ["string-handling", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/syllables" : ["I/O", "string-handling", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/vector-average" : ["vectors", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-UMAD/x-word-lines" : ["I/O", "string-handling"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-standard/replace-space-with-newline" : ["string-handling", "I/O", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/genops-standard/syllables" : ["I/O", "string-handling", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-UMAD/replace-space-with-newline" : ["string-handling", "I/O", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/compare-string-lengths" : ["boolean", "comparison", "string-handling"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/double-letters" : ["I/O", "string-handling", "comparison"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/last-index-of-zero" : ["comparison", "vectors"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/median" : ["I/O", "comparison"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/mirror-image" : ["vectors", "boolean", "comparison"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/negative-to-zero" : ["vectors", "comparison"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/pig-latin" : ["I/O", "string-handling"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/replace-space-with-newline" : ["string-handling", "I/O", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/scrabble-score" : ["string-handling", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/syllables" : ["I/O", "string-handling", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/vector-average" : ["vectors", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/x-word-lines" : ["I/O", "string-handling"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/compare-string-lengths" : ["boolean", "comparison", "string-handling"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/double-letters" : ["I/O", "string-handling", "comparison"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/last-index-of-zero" : ["comparison", "vectors"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/median" : ["I/O", "comparison"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/mirror-image" : ["vectors", "boolean", "comparison"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/negative-to-zero" : ["vectors", "comparison"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/pig-latin" : ["I/O", "string-handling"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/replace-space-with-newline" : ["string-handling", "I/O", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/scrabble-score" : ["string-handling", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/syllables" : ["I/O", "string-handling", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/vector-average" : ["vectors", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/x-word-lines" : ["I/O", "string-handling"],
                "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/novelty-search/double-letters" : ["I/O", "string-handling", "comparison"],
                "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/novelty-search/scrabble-score" : ["string-handling", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/novelty-search/syllables" : ["I/O", "string-handling", "arithmetic"],
                "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/novelty-search/x-word-lines" : ["I/O", "string-handling"],
                "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/tournament/number-io" : ["I/O", "arithmetic"]}


outputFilePrefix = "log"
outputFileSuffix = ".txt"


#directories = ["C:/Users/livel/Desktop/tournament/number-io", "C:/Users/livel/Desktop/double-letters"]
#directories = {"C:/Users/livel/Desktop/tournament/number-io" : ["I/O", "arithmetic"]}
#directories = {"C:/Users/livel/Desktop/syllables" : ["I/O", "string-handling", "arithmetic"]}


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
            elif word[0] == "(":
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

        success = False
        simpl = False
        funcs_list = []

        for line in f:
            if line.startswith("Best program: "):
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
                success = True

                if verbose:
                    print "Gen %i" % gen
                    print funcs_list
                    print

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

        i += 1
