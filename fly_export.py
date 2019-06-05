# Grace Woolson, Summer 2019
import math
import os
import sys
import csv

problems = {"number-io" : ["I/O", "arithmetic"],
            "checksum" : ["string_handling", "arithmetic", "I/O"], 
            "collatz-numbers" : ["arithmetic", "comparison"], 
            "compare-string-lengths" : ["boolean", "comparison", "string_handling"], 
            "count-odds" : ["vectors", "arithmetic"], 
            "digits" : ["I/O", "arithmetic", "string_handling"],
            "double-letters" : ["string_handling", "I/O", "comparison"],
            "even-squares" : ["I/O", "arithmetic"]
            "for-loop-index" : ["I/O", "arithmetic"],
            "grade" : ["I/O", "comparison"], 
            "last-index-of-zero" : ["vectors", "comparison"],
            "median" : ["I/O", "comparison"],
            "mirror-image" : ["vectors", "boolean", "comparison"],
            "negative-to-zero" : ["vectors", "comparison"],
            "pig-latin" : ["string_handling", "I/O"],
            "replace-space-with-newline" : ["string_handling", "I/O", "arithmetic"],
            "scrabble-score" : ["string_handling", "arithmetic"], 
            "small-or-large" : ["I/O", "comparison"],
            "smallest" : ["I/O", "comparison"],
            "string-differences" : ["string_handling", "comparison", "I/O"],
            "string-lengths-backwards" : ["I/O", "string_handling", "vectors"], 
            "sum-of-squares" : ["arithmetic"],
            "super-anagrams" : ["boolean", "string_handling", "comparison"],
            "syllables" : ["I/O", "arithmetic", "string_handling"],
            "vector-average" : ["vectors", "arithmetic"],
            "vectors-summed" : ["vectors", "arithmetic"],
            "wallis-pi" : ["arithmetic"],
            "word-stats" : ["file", "I/O", "string_handling", "arithmetic"],
            "x-word-lines" : ["string_handling", "I/O"]}

outputFilePrefix = "log"
outputFileSuffix = ".txt"


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



if len(sys.argv) > 1:
    destination = sys.argv[1]
else:
    print("please provide a destination file in the format <filename>.csv")
    exit(1)


destfile = open(destination, mode="w")
destwriter = csv.writer(destfile)


category = directories[outputDirectory] ##UPDATE******************

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

header = [category]


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

        if not line.startswith("uuid"):
            #the first line always starts with uuid I THINK************************
            
            #removes  d1355282-86ad-4964-aa74-d040ff2385f3,0,0,[],:random,98,86, i think
            genes_line = line.split(",")[7:]
            genes_line = ",".join(genes_line)

    i += 1
