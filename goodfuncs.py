import sys
import csv
from success_by_problem import success_only
#from simplified_programs import success_only


def print_prog(program):
    for element in program:
        print element


def check_if_constant(instruction):

	is_constant = False
	numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

	#booleans
	if instruction == "true" or instruction == "false":
		is_constant = True

	#integers/floats
	if instruction[0] in numbers:
		is_constant = True

	if instruction[0] == "-":
		is_constant = True

	#tags
	if instruction[:3] == "tag":
		is_constant = True

	#characters
	if instruction[0] == "\\":
		is_constant = True

	#strings
	if instruction[0] == '\"':
		is_constant = True

	#vectors
	if instruction[0] == "[":
		is_constant = True


	return is_constant


def get_funcs_list(organized_programs):
	problems = ["all_programs", "number-io", "checksum", "collatz-numbers", "compare-string-lengths", "count-odds", "digits", "double-letters", "even-squares", "for-loop-index", "grade", "last-index-of-zero", "median", "mirror-image", "negative-to-zero", "pig-latin", "replace-space-with-newline", "scrabble-score", "small-or-large", "smallest", "string-differences", "string-lengths-backwards", "sum-of-squares", "super-anagrams", "syllables", "vector-average", "vectors-summed", "wallis-pi", "word-stats", "x-word-lines"]

	all_funcs = []

	for prob in problems:

		if prob == "all_programs":
			programs = organized_programs[0]

		if prob == "number-io":
			programs = organized_programs[1]

		if prob == "checksum":
			programs = organized_programs[2]

		if prob == "collatz-numbers":
			programs = organized_programs[3]

		if prob == "compare-string-lengths":
			programs = organized_programs[4]

		if prob == "count-odds":
			programs = organized_programs[5]

		if prob == "digits":
			programs = organized_programs[6]

		if prob == "double-letters":
			programs = organized_programs[7]

		if prob == "even-squares":
			programs = organized_programs[8]

		if prob == "for-loop-index":
			programs = organized_programs[9]

		if prob == "grade":
			programs = organized_programs[10]

		if prob == "last-index-of-zero":
			programs = organized_programs[11]

		if prob == "median":
			programs = organized_programs[12]

		if prob == "mirror-image":
			programs = organized_programs[13]

		if prob == "negative-to-zero":
			programs = organized_programs[14]

		if prob == "pig-latin":
			programs = organized_programs[15]

		if prob == "replace-space-with-newline":
			programs = organized_programs[16]

		if prob == "scrabble-score":
			programs = organized_programs[17]

		if prob == "small-or-large":
			programs = organized_programs[18]

		if prob == "smallest":
			programs = organized_programs[19]

		if prob == "string-differences":
			programs = organized_programs[20]

		if prob == "string-lengths-backwards":
			programs = organized_programs[21]

		if prob == "sum-of-squares":
			programs = organized_programs[22]

		if prob == "super-anagrams":
			programs = organized_programs[23]

		if prob == "syllables":
			programs = organized_programs[24]

		if prob == "vector-average":
			programs = organized_programs[25]

		if prob == "vectors-summed":
			programs = organized_programs[26]

		if prob == "wallis-pi":
			programs = organized_programs[27]

		if prob == "word-stats":
			programs = organized_programs[28]

		if prob == "x-word-lines":
			programs = organized_programs[29]

		max_frequency = len(programs)
		freqs = {}

		for program in programs:
			this_run = []
			#print_prog(program)
			for func in program:
				#ACCOUNTS FOR CONSTANTS
				is_constant = check_if_constant(func)
				if (not is_constant) and not (func in this_run):
					this_run.append(func)
					if func in freqs:
						freqs[func] += 1
					else:
						freqs[func] = 1


		max_threshold = round(max_frequency * .6)
		if max_threshold > 0:

			interesting = {}

			for key in freqs:
				if (freqs[key] >= max_threshold):
					if not key in all_funcs:
						all_funcs.append(key)

	return all_funcs


def goodfuncs1():

	tags = {"I/O" : ["number-io", "checksum", "digits", "double-letters", "even-squares", "for-loop-index", "grade", "median", "negative-to-zero", "pig-latin", "replace-space-with-newline", "small-or-large", "smallest", "string-differences", "string-lengths-backwards", "syllables", "word-stats", "x-word-lines"],
			"arithmetic" : ["number-io", "checksum", "collatz-numbers", "count-odds", "digits", "even-squares", "for-loop-index", "replace-space-with-newline", "scrabble-score", "sum-of-squares", "syllables", "vector-average", "vectors-summed", "wallis-pi", "word-stats"],
			"comparison" : ["collatz-numbers", "compare-string-lengths", "double-letters", "grade", "last-index-of-zero", "median", "mirror-image", "negative-to-zero", "small-or-large", "smallest","string-differences", "super-anagrams"],
			"boolean" : ["compare-string-lengths", "mirror-image", "super-anagrams"],
			"string_handling" : ["checksum", "compare-string-lengths", "digits", "double-letters", "pig-latin", "replace-space-with-newline", "scrabble-score", "string-differences", "string-lengths-backwards", "super-anagrams", "syllables", "word-stats", "x-word-lines"],
			"vectors" : ["count-odds", "last-index-of-zero", "mirror-image", "negative-to-zero", "string-lengths-backwards", "vector-average", "vectors-summed"]}

	IO = []
	arithmetic = []
	comparison = []
	boolean = []
	string_handling = []
	vectors = []
	all_programs = []

	iocount = 0
	arithcount = 0
	compcount = 0
	boolcount = 0
	strcount = 0
	vectorcount = 0

	if len(sys.argv) > 1:
	    destination = sys.argv[1]
	else:
	    print("please provide a destination file in the format <filename>.csv")
	    exit(1)


	destfile = open(destination, mode="w")
	destwriter = csv.writer(destfile)

	organized_programs = success_only()


	#I removed file from this list because no program with that tag has succeeded, providing no data
	problems = ["all_programs", "number-io", "checksum", "collatz-numbers", "compare-string-lengths", "count-odds", "digits", "double-letters", "even-squares", "for-loop-index", "grade", "last-index-of-zero", "median", "mirror-image", "negative-to-zero", "pig-latin", "replace-space-with-newline", "scrabble-score", "small-or-large", "smallest", "string-differences", "string-lengths-backwards", "sum-of-squares", "super-anagrams", "syllables", "vector-average", "vectors-summed", "wallis-pi", "word-stats", "x-word-lines"]

	all_funcs = get_funcs_list(organized_programs)

	for prob in problems:

		print prob

		if prob == "all_programs":
			programs = organized_programs[0]

		if prob == "number-io":
			programs = organized_programs[1]

		if prob == "checksum":
			programs = organized_programs[2]

		if prob == "collatz-numbers":
			programs = organized_programs[3]

		if prob == "compare-string-lengths":
			programs = organized_programs[4]

		if prob == "count-odds":
			programs = organized_programs[5]

		if prob == "digits":
			programs = organized_programs[6]

		if prob == "double-letters":
			programs = organized_programs[7]

		if prob == "even-squares":
			programs = organized_programs[8]

		if prob == "for-loop-index":
			programs = organized_programs[9]

		if prob == "grade":
			programs = organized_programs[10]

		if prob == "last-index-of-zero":
			programs = organized_programs[11]

		if prob == "median":
			programs = organized_programs[12]

		if prob == "mirror-image":
			programs = organized_programs[13]

		if prob == "negative-to-zero":
			programs = organized_programs[14]

		if prob == "pig-latin":
			programs = organized_programs[15]

		if prob == "replace-space-with-newline":
			programs = organized_programs[16]

		if prob == "scrabble-score":
			programs = organized_programs[17]

		if prob == "small-or-large":
			programs = organized_programs[18]

		if prob == "smallest":
			programs = organized_programs[19]

		if prob == "string-differences":
			programs = organized_programs[20]

		if prob == "string-lengths-backwards":
			programs = organized_programs[21]

		if prob == "sum-of-squares":
			programs = organized_programs[22]

		if prob == "super-anagrams":
			programs = organized_programs[23]

		if prob == "syllables":
			programs = organized_programs[24]

		if prob == "vector-average":
			programs = organized_programs[25]

		if prob == "vectors-summed":
			programs = organized_programs[26]

		if prob == "wallis-pi":
			programs = organized_programs[27]

		if prob == "word-stats":
			programs = organized_programs[28]

		if prob == "x-word-lines":
			programs = organized_programs[29]

		max_frequency = len(programs)
		freqs = {}

		for program in programs:
			this_run = []
			#print_prog(program)
			for func in program:
				#ACCOUNTS FOR CONSTANTS
				is_constant = check_if_constant(func)
				if (not is_constant) and not (func in this_run):
					this_run.append(func)
					if func in freqs:
						freqs[func] += 1
					else:
						freqs[func] = 1


		max_threshold = round(max_frequency * .6)
		if max_threshold > 0:

			print "Max possible occurances: %i" % max_frequency
			print "Max Threshold is: %i" % max_threshold
			print


			for i in range(0, len(all_funcs)):
				function = all_funcs[i]
				if function in freqs:
					frequency = round((freqs[function] / float(max_frequency)), 2)
				else:
					frequency = 0.0

				if prob == "all_programs":
					all_programs.append(frequency)

				if prob in tags["I/O"]:
					#print i
					if len(IO) - 1 < i:
						IO.append(frequency)
					else:
						IO[i] = IO[i] + frequency

					if i == len(all_funcs) - 1:
						iocount += 1

				if prob in tags["arithmetic"]:
					if len(arithmetic) - 1 < i:
						arithmetic.append(frequency)
					else:
						arithmetic[i] = arithmetic[i] + frequency

					if i == len(all_funcs) - 1:
						arithcount += 1

				if prob in tags["comparison"]:
					if len(comparison) - 1 < i:
						comparison.append(frequency)
					else:
						comparison[i] = comparison[i] + frequency

					if i == len(all_funcs) - 1:
						compcount += 1

				if prob in tags["boolean"]:
					if len(boolean) - 1 < i:
						boolean.append(frequency)
					else:
						boolean[i] = boolean[i] + frequency

					if i == len(all_funcs) - 1:
						boolcount += 1

				if prob in tags["string_handling"]:
					if len(string_handling) - 1 < i:
						string_handling.append(frequency)
					else:
						string_handling[i] = string_handling[i] + frequency

					if i == len(all_funcs) - 1:
						strcount += 1

				if prob in tags["vectors"]:
					if len(vectors) - 1 < i:
						vectors.append(frequency)
					else:
						vectors[i] = vectors[i] + frequency

					if i == len(all_funcs) - 1:
						vectorcount += 1


	for a in range(0, len(all_funcs)):
		element = IO[a]
		IO[a] = element / iocount

	for b in range(0, len(all_funcs)):
		element = arithmetic[b]
		arithmetic[b] = element / arithcount

	for c in range(0, len(all_funcs)):
		element = comparison[c]
		comparison[c] = element / compcount

	for d in range(0, len(all_funcs)):
		element = boolean[d]
		boolean[d] = element / boolcount

	for e in range(0, len(all_funcs)):
		element = string_handling[e]
		string_handling[e] = element / strcount

	for f in range(0, len(all_funcs)):
		element = vectors[f]
		vectors[f] = element / vectorcount

	destwriter.writerow(["Problem"] + all_funcs)
	destwriter.writerow(["IO"] + IO)
	destwriter.writerow(["Arithmetic"] + arithmetic)
	destwriter.writerow(["Comparison"] + comparison)
	destwriter.writerow(["Boolean"] + boolean)
	destwriter.writerow(["String Handling"] + string_handling)
	destwriter.writerow(["Vectors"] + vectors)
	destwriter.writerow(["All Programs"] + all_programs)



def goodfuncs2():

	tags = {"I/O" : ["number-io", "checksum", "digits", "double-letters", "even-squares", "for-loop-index", "grade", "median", "negative-to-zero", "pig-latin", "replace-space-with-newline", "small-or-large", "smallest", "string-differences", "string-lengths-backwards", "syllables", "word-stats", "x-word-lines"],
			"arithmetic" : ["number-io", "checksum", "collatz-numbers", "count-odds", "digits", "even-squares", "for-loop-index", "replace-space-with-newline", "scrabble-score", "sum-of-squares", "syllables", "vector-average", "vectors-summed", "wallis-pi", "word-stats"],
			"comparison" : ["collatz-numbers", "compare-string-lengths", "double-letters", "grade", "last-index-of-zero", "median", "mirror-image", "negative-to-zero", "small-or-large", "smallest","string-differences", "super-anagrams"],
			"boolean" : ["compare-string-lengths", "mirror-image", "super-anagrams"],
			"string_handling" : ["checksum", "compare-string-lengths", "digits", "double-letters", "pig-latin", "replace-space-with-newline", "scrabble-score", "string-differences", "string-lengths-backwards", "super-anagrams", "syllables", "word-stats", "x-word-lines"],
			"vectors" : ["count-odds", "last-index-of-zero", "mirror-image", "negative-to-zero", "string-lengths-backwards", "vector-average", "vectors-summed"]}

	IO = []
	arithmetic = []
	comparison = []
	boolean = []
	string_handling = []
	vectors = []
	all_programs = []

	iocount = 0
	arithcount = 0
	compcount = 0
	boolcount = 0
	strcount = 0
	vectorcount = 0

	if len(sys.argv) > 1:
	    destination = sys.argv[1]
	else:
	    print("please provide a destination file in the format <filename>.csv")
	    exit(1)


	destfile = open(destination, mode="w")
	destwriter = csv.writer(destfile)

	organized_programs = success_only()


	#I removed file from this list because no program with that tag has succeeded, providing no data
	problems = ["all_programs", "number-io", "checksum", "collatz-numbers", "compare-string-lengths", "count-odds", "digits", "double-letters", "even-squares", "for-loop-index", "grade", "last-index-of-zero", "median", "mirror-image", "negative-to-zero", "pig-latin", "replace-space-with-newline", "scrabble-score", "small-or-large", "smallest", "string-differences", "string-lengths-backwards", "sum-of-squares", "super-anagrams", "syllables", "vector-average", "vectors-summed", "wallis-pi", "word-stats", "x-word-lines"]

	all_funcs = get_funcs_list(organized_programs)

	for prob in problems:

		print prob

		if prob == "all_programs":
			programs = organized_programs[0]

		if prob == "number-io":
			programs = organized_programs[1]

		if prob == "checksum":
			programs = organized_programs[2]

		if prob == "collatz-numbers":
			programs = organized_programs[3]

		if prob == "compare-string-lengths":
			programs = organized_programs[4]

		if prob == "count-odds":
			programs = organized_programs[5]

		if prob == "digits":
			programs = organized_programs[6]

		if prob == "double-letters":
			programs = organized_programs[7]

		if prob == "even-squares":
			programs = organized_programs[8]

		if prob == "for-loop-index":
			programs = organized_programs[9]

		if prob == "grade":
			programs = organized_programs[10]

		if prob == "last-index-of-zero":
			programs = organized_programs[11]

		if prob == "median":
			programs = organized_programs[12]

		if prob == "mirror-image":
			programs = organized_programs[13]

		if prob == "negative-to-zero":
			programs = organized_programs[14]

		if prob == "pig-latin":
			programs = organized_programs[15]

		if prob == "replace-space-with-newline":
			programs = organized_programs[16]

		if prob == "scrabble-score":
			programs = organized_programs[17]

		if prob == "small-or-large":
			programs = organized_programs[18]

		if prob == "smallest":
			programs = organized_programs[19]

		if prob == "string-differences":
			programs = organized_programs[20]

		if prob == "string-lengths-backwards":
			programs = organized_programs[21]

		if prob == "sum-of-squares":
			programs = organized_programs[22]

		if prob == "super-anagrams":
			programs = organized_programs[23]

		if prob == "syllables":
			programs = organized_programs[24]

		if prob == "vector-average":
			programs = organized_programs[25]

		if prob == "vectors-summed":
			programs = organized_programs[26]

		if prob == "wallis-pi":
			programs = organized_programs[27]

		if prob == "word-stats":
			programs = organized_programs[28]

		if prob == "x-word-lines":
			programs = organized_programs[29]

		max_frequency = len(programs)
		freqs = {}

		for program in programs:
			this_run = []
			#print_prog(program)
			for func in program:
				#ACCOUNTS FOR CONSTANTS
				is_constant = check_if_constant(func)
				if (not is_constant) and not (func in this_run):
					this_run.append(func)
					if func in freqs:
						freqs[func] += 1
					else:
						freqs[func] = 1


		max_threshold = round(max_frequency * .6)
		if max_threshold > 0:

			print "Max possible occurances: %i" % max_frequency
			print "Max Threshold is: %i" % max_threshold
			print


			for i in range(0, len(all_funcs)):
				function = all_funcs[i]
				if function in freqs:
					frequency = round((freqs[function] / float(max_frequency)), 2)
				else:
					frequency = 0.0

				if prob == "all_programs":
					all_programs.append(frequency)

				if prob in tags["I/O"]:
					#print i
					if len(IO) - 1 < i:
						IO.append(frequency)
					else:
						IO[i] = IO[i] + frequency

					if i == len(all_funcs) - 1:
						iocount += 1

				if prob in tags["arithmetic"]:
					if len(arithmetic) - 1 < i:
						arithmetic.append(frequency)
					else:
						arithmetic[i] = arithmetic[i] + frequency

					if i == len(all_funcs) - 1:
						arithcount += 1

				if prob in tags["comparison"]:
					if len(comparison) - 1 < i:
						comparison.append(frequency)
					else:
						comparison[i] = comparison[i] + frequency

					if i == len(all_funcs) - 1:
						compcount += 1

				if prob in tags["boolean"]:
					if len(boolean) - 1 < i:
						boolean.append(frequency)
					else:
						boolean[i] = boolean[i] + frequency

					if i == len(all_funcs) - 1:
						boolcount += 1

				if prob in tags["string_handling"]:
					if len(string_handling) - 1 < i:
						string_handling.append(frequency)
					else:
						string_handling[i] = string_handling[i] + frequency

					if i == len(all_funcs) - 1:
						strcount += 1

				if prob in tags["vectors"]:
					if len(vectors) - 1 < i:
						vectors.append(frequency)
					else:
						vectors[i] = vectors[i] + frequency

					if i == len(all_funcs) - 1:
						vectorcount += 1


	for a in range(0, len(all_funcs)):
		element = IO[a]
		IO[a] = element / iocount

	for b in range(0, len(all_funcs)):
		element = arithmetic[b]
		arithmetic[b] = element / arithcount

	for c in range(0, len(all_funcs)):
		element = comparison[c]
		comparison[c] = element / compcount

	for d in range(0, len(all_funcs)):
		element = boolean[d]
		boolean[d] = element / boolcount

	for e in range(0, len(all_funcs)):
		element = string_handling[e]
		string_handling[e] = element / strcount

	for f in range(0, len(all_funcs)):
		element = vectors[f]
		vectors[f] = element / vectorcount

	destwriter.writerow(["Problem"] + all_funcs)
	destwriter.writerow(["IO"] + IO)

	destwriter.writerow(["Problem"] + all_funcs)
	destwriter.writerow(["Arithmetic"] + arithmetic)

	destwriter.writerow(["Problem"] + all_funcs)
	destwriter.writerow(["Comparison"] + comparison)

	destwriter.writerow(["Problem"] + all_funcs)
	destwriter.writerow(["Boolean"] + boolean)
	
	destwriter.writerow(["Problem"] + all_funcs)
	destwriter.writerow(["String Handling"] + string_handling)

	destwriter.writerow(["Problem"] + all_funcs)
	destwriter.writerow(["Vectors"] + vectors)

	destwriter.writerow(["Problem"] + all_funcs)
	destwriter.writerow(["All Programs"] + all_programs)

def main():

	goodfuncs2()

if __name__ == '__main__':
	main()
