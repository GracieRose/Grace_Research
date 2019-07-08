import sys
import csv
import os


# Make a verison of this that will run on HPC
#directories = ["/home/gwoolson/research/gwoolson/Grace_Research/csvdata/checksum"]

directories = ["C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/checksum/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/collatz-numbers/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/compare_string_lengths/", #MAY HAVE TO CHANGE THIS ONE
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

outputFilePrefix = "run"
outputFileSuffix = ".csv"

# Don't have to change anything below!

if len(sys.argv) > 1:
    destination = sys.argv[1]
else:
    print("please provide a destination file in the format <filename>.csv")
    exit(1)


destfile = open(destination, mode="w")
destwriter = csv.writer(destfile)

all_funcs = []
all_freqs = []

for outputDirectory in directories:

    print outputDirectory

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)


    z = 0
    while (outputFilePrefix + str(z) + outputFileSuffix) in dirList:

        fileName = (outputFilePrefix + str(z) + outputFileSuffix)
        f = open(outputDirectory + fileName)
        z += 1


        for linenum, line in enumerate(f):
        	if linenum == 0:
        		#unfortunately all functions have commas at the end, and are encompassed by quotes
        		funcs = line[1:-3].split(",\",\"")

        	if linenum == 1:
        		freqs = line[:-1].split(",")

        if funcs != ['']:
	    	for i in range(0, len(funcs)):
	    		function = funcs[i]
	    		frequency = float(freqs[i])

	    		"""print function
	    		print frequency
	    		print"""

	    		if function not in all_funcs:
	    			all_funcs.append(function)
	    			all_freqs.append([frequency])

	    		else:
	    			loc = all_funcs.index(function)
	    			all_freqs[loc].append(frequency)

avg_freqs = []
for subset in all_freqs:
	avg = sum(subset) / len(subset)
	avg_freqs.append(avg)


destwriter.writerow(all_funcs)
destwriter.writerow(avg_freqs)