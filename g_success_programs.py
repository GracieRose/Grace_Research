import math
import os
import sys

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
outputDirectory = "/home/gwoolson/research/thelmuth/Results/parent-selection-v2/tournament/number-io"

outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Don't have to change anything below!

verbose = True
if(len(sys.argv) > 1):
    verbose = False

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

i = 0
while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:

    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    success = False
    simpl = False

    if verbose:
        print
        print "-------------------------------------------------"
        print "------------------ Run %i ------------------------" % i
        print

    testForBest = 5

    for line in f:
        if line.startswith("Successful program: "):
            if verbose:
                print line
                print
            else:
                if sys.argv[1] != "test" or testForBest == 0:
                    print line[len("Successful program: "):-1]
            success = True

        if simpl == True and verbose:
            print "Simplification after 1000 steps:"
            print line
            break

        if success and line.startswith("step: 1000"):
            simpl = True

        if line.startswith("Test total error for best:"):
            testForBest = int(line.split()[-1].strip("Nn"))

    i += 1
