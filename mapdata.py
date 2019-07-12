import os
import sys
import csv

def find_funcs(directories):

	all_funcs = []

	outputFilePrefix = "mapdata"
	outputFileSuffix = ".csv"

	for outputDirectory in directories:

	    if outputDirectory[-1] != '/':
	        outputDirectory += '/'
	    dirList = os.listdir(outputDirectory)

	    z = 0
	    while (outputFilePrefix + str(z) + outputFileSuffix) in dirList:

	        fileName = (outputFilePrefix + str(z) + outputFileSuffix)
	        f = open(outputDirectory + fileName)
	        z += 1

	        funcs = []

	        for line in f:

	        	if (not line.startswith("Gen ")) and (not (line.startswith("0") or line.startswith("1.0"))):
	        		funcs = line[:-1].split(",")

	        		for item in funcs:
	        			if not item in all_funcs:
	        				all_funcs.append(item)

	return all_funcs


# Make a verison of this that will run on HPC
#directories = ["/home/gwoolson/research/gwoolson/Grace_Research/mapdata/checksum"]

directories = ["C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/checksum/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/count-odds/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/double-letters/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/negative-to-zero/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/replace-space-with-newline/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/scrabble-score/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/string-lengths-backwards/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/syllables/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/vector-average/"]

outputFilePrefix = "mapdata"
outputFileSuffix = ".csv"


if len(sys.argv) > 1:
    destination = sys.argv[1]
else:
    print("please provide a destination file in the format <filename>.csv")
    exit(1)


destfile = open(destination, mode="wb")
destwriter = csv.writer(destfile)

all_funcs = find_funcs(directories)
all_gens = []

for outputDirectory in directories:

    #print outputDirectory

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)

    z = 0
    while (outputFilePrefix + str(z) + outputFileSuffix) in dirList:

        fileName = (outputFilePrefix + str(z) + outputFileSuffix)
        f = open(outputDirectory + fileName)
        z += 1

        funcs = []
        freqs = []

        for line in f:

        	if line.startswith("Gen "):
        		gen = int(line[4:])

        		if len(all_gens) <= gen:
        			all_gens.append({})

        	elif line.startswith("0") or line.startswith("1.0"):
        		freqs = line[:-1].split(",")

        	else:
        		funcs = line[:-1].split(",")

        	if freqs == line[:-1].split(","):

        		for i in range(0, len(all_funcs)):

        			func = all_funcs[i]

        			if func in funcs:
        				funcindex = funcs.index(func)
	        			frequency = float(freqs[funcindex])
	        		else:
	        			frequency = 0.0

        			if func in all_gens[gen]:
        				all_gens[gen][func].append(frequency)
        			else:
        				all_gens[gen][func] = [frequency]


header = True
funcs_printed = []
to_print = []
for generation_map in all_gens:

	#use all_funcs instead
	#funcslist = []
	freqslist = [] 
	
	for function in all_funcs:

		#debugging
		#print all_funcs[counter]
		#print all_gens[0][all_funcs[0]]
		#print sum(all_gens[0][all_funcs[counter]]) / len(all_gens[0][all_funcs[counter]])

		frequencies = generation_map[function]

		avg_freq = sum(frequencies) / len(frequencies)

		freqslist.append(avg_freq)

	if header:
		destwriter.writerow(all_funcs)
		header = False

	destwriter.writerow(freqslist)

#print all_gens