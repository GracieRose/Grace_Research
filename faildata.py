import sys
import csv
import os


# Make a verison of this that will run on HPC
#directories = ["/home/gwoolson/research/gwoolson/Grace_Research/csvdata/checksum"]

directories = ["C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/checksum/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/count-odds/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/double-letters/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/negative-to-zero/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/replace-space-with-newline/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/scrabble-score/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/string-lengths-backwards/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/syllables/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/vector-average/"]

#directories = ["C:/Users/livel/Documents/Research2019/Grace_Research/csvdata/count-odds/"]

outputFilePrefix = "run"
outputFileSuffix = ".csv"


"""if len(sys.argv) > 1:
    destination = sys.argv[1]
else:
    print("please provide a destination file in the format <filename>.csv")
    exit(1)

destfile = open(destination, mode="w")
destwriter = csv.writer(destfile)"""

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

max_val = max(avg_freqs)

#destwriter.writerow(all_funcs)
#destwriter.writerow(avg_freqs)

for x in range(0, len(all_funcs)):
	this_func = all_funcs[x]
	this_freq = avg_freqs[x]

	if this_freq >= 0.6:
		print "%s: %f" % (this_func, this_freq)