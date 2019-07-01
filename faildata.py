import math
import sys
import csv


# Make a verison of this that will run on HPC
#directories = ["/home/gwoolson/research/gwoolson/Grace_Research/csvdata/checksum"]

directories = ["C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/checksum/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/collatz-numbers/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/compare-string-lengths/", #MAY HAVE TO CHANGE THIS ONE
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/count-odds/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/digits/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/double-letters/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/even-squares/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/for-loop-index/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/grade/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/last-index-of-zero/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/median/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/mirror-image/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/negative-to-zero/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/number-io/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/pig-latin/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/replace-space-with-newline/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/scrabble-score/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/smallest/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/small-or-large/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/string-differences/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/string-lengths-backwards/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/sum-of-squares/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/super-anagrams/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/syllables/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/vector-average/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/vectors-summed/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/wallis-pi/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/word-stats/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/x-word-lines/"]


#directories = ["C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/count-odds/"]

outputFilePrefix = "data"
outputFileSuffix = ".csv"

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

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)


    i = 0
    while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:

       
       
        i += 1
