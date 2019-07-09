import os
import sys
import csv


def convert_float(num):

	pass


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


destfile = open(destination, mode="w")
destwriter = csv.writer(destfile)

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
        			frequency = float(freqs[i])

        			if func == "exec_do*whi":
        				print outputDirectory+fileName
        				print frequency

        			if func in all_gens[gen]:
        				all_gens[gen][func].append(frequency)
        			else:
        				all_gens[gen][func] = [frequency]

gencount = 0
funcs_printed = []
to_print = []
for generation_map in all_gens:

	funcslist = []
	freqslist = []
	
	for function in generation_map:
		frequencies = generation_map[function]

		avg_freq = sum(frequencies) / len(frequencies)
		#print frequencies
		
		funcslist.append(function)
		freqslist.append(avg_freq)
		
		"""if function == "exec_do*whi":
			print frequencies, len(frequencies)
			print avg_freq
			print"""

		genprint = "Gen %i" % gencount

	#if gencount == 0:
	destwriter.writerow(funcslist)
	#funcs_printed = funcslist


	destwriter.writerow(freqslist)
	gencount += 1

#print all_gens