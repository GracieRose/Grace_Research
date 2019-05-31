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
"""

outputFilePrefix = "log"
outputFileSuffix = ".txt"


#directories = ["C:/Users/livel/Desktop/tournament/number-io", "C:/Users/livel/Desktop/double-letters"]
#directories = ["C:/Users/livel/Desktop/scrabble-score"]


verbose = False
if (len(sys.argv) >= 3 and sys.argv[2] == "print"):
    verbose = True


def debracket(lst):
    newlist = []

    for word in lst:

        newword = word

        if word[0] == "{":
            newword = newword[1:]

        if word[-1] == "}":
            newword = newword[:-1]

        newlist.append(newword)

        #print newword

    return newlist



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

    #category = directories[outputDirectory]

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)

    #header = [outputDirectory, category]
    header = [outputDirectory]

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
        #print runcount

        fileName = (outputFilePrefix + str(i) + outputFileSuffix)
        f = open(outputDirectory + fileName)

        success = False
        simpl = False
        running_error = sys.maxint

        prev_line = ""
        for line in f:

            if line.startswith("Test total error for best:"):
                #print gen
                #print prev_line
                #print line
                try:
                    running_error = int(line.split()[-1].strip("Nn"))
                except ValueError, e:
                    running_error = float(line.split()[-1].strip("Nn"))

                if running_error == 0:
                    success = True

                gen += 1

            if line.startswith("Best genome: "):

                genes_lst = line.split("} ")
                first = genes_lst[0][14:]
                last = genes_lst[-1][:-2]
                mid_lst = genes_lst[1:-1]

                genes_lst = [first] + mid_lst + [last]

                genes_lst = debracket(genes_lst)

                if success:
                    final = ["Successful"] + genes_lst
                else:
                    final = ["Failed"] + genes_lst

                destwriter.writerow(final)

                if verbose:
                    print final
                    print

                    if success:
                        print "Success!"

            prev_line = line

        i += 1
