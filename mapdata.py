import os
import sys
import csv


def convert_float(num):

	pass


# Make a verison of this that will run on HPC
#directories = ["/home/gwoolson/research/gwoolson/Grace_Research/mapdata/checksum"]

directories = ["C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/checksum/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/collatz-numbers/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/compare-string-lengths/", #MAY HAVE TO CHANGE THIS ONE
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/count-odds/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/digits/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/double-letters/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/even-squares/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/for-loop-index/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/grade/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/last-index-of-zero/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/median/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/mirror-image/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/negative-to-zero/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/number-io/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/pig-latin/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/replace-space-with-newline/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/scrabble-score/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/smallest/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/small-or-large/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/string-differences/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/string-lengths-backwards/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/sum-of-squares/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/super-anagrams/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/syllables/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/vector-average/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/vectors-summed/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/wallis-pi/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/word-stats/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/x-word-lines/"]


outputFilePrefix = "mapdata"
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

for outputDirectory in directories:

    #print outputDirectory

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)


    z = 0
    while (outputFilePrefix + str(z) + outputFileSuffix) in dirList:
    	#Try rewriting this section to ENSURE that the functions are chosen in the same order
        fileName = (outputFilePrefix + str(z) + outputFileSuffix)
        f = open(outputDirectory + fileName)
        z += 1


        funcs = []
        freqs = []

        for line in f:

        	if line.startswith("Gen "):
        		gen = int(line[4:])

        		if len(all_funcs) <= gen:
        			all_funcs.append({})

        	elif line.startswith("0"):
        		freqs = line[:-1].split(",")
        		#print "freqs: ", freqs
        		#print

        	else:
        		funcs = line[:-1].split(",")
        		#print "funcs: ", funcs

        	if freqs == line[:-1].split(","):

        		for i in range(0, len(funcs)):

        			func = funcs[i]
        			frequency = round(float(freqs[i]), 4)
        			if frequency > 1.0:
        				print "%s%s" % (outputDirectory, fileName)
        				print frequency
        				print

        			if func in all_funcs[gen]:
        				all_funcs[gen][func].append(frequency)
        			else:
        				all_funcs[gen][func] = [frequency]


gencount = 0
for generation_map in all_funcs:

	funcslist = []
	freqslist = []
	
	for function in generation_map:
		frequencies = generation_map[function]

		avg_freq = sum(frequencies) / len(frequencies)
		#print frequencies
		
		funcslist.append(function)
		freqslist.append(avg_freq)
		#print avg_freq
		#print

		genprint = "Gen %i" % gencount

	if gencount == 0:
		destwriter.writerow(funcslist)


	destwriter.writerow(freqslist)
	gencount += 1

#print all_funcs