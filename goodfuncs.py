import sys
import csv
from g_success_programs import success_only


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
		is_constant == True

	#strings
	if instruction[0] == '\"':
		is_constant = True

	#vectors
	if instruction[0] == "[":
		is_constant = True

	return is_constant

def goodfuncs1():

	if len(sys.argv) > 1:
	    destination = sys.argv[1]
	else:
	    print("please provide a destination file in the format <filename>.csv")
	    exit(1)


	destfile = open(destination, mode="w")
	destwriter = csv.writer(destfile)

	organized_programs = success_only()
	#I removed file from this list because no program with that tag has succeeded, providing no data
	possible_tags = ["all_programs", "IO", "arithmetic", "comparison", "boolean", "string_handling", "vectors", "all_programs"]

	all_funcs = []

	destwriter.writerow(all_funcs)

	for tag in possible_tags:
		print tag

		if tag == "all_programs":
			programs = organized_programs[0]
		elif tag == "IO":
			programs = organized_programs[1]
		elif tag == "arithmetic":
			programs = organized_programs[2]
		elif tag == "comparison":
			programs = organized_programs[3]
		elif tag == "boolean":
			programs = organized_programs[4]
		elif tag == "string_handling":
			programs = organized_programs[5]
		elif tag == "vectors":
			programs = organized_programs[6]
		

		max_frequency = len(programs)
		freqs = {}

		for program in programs:
			this_run = []
			#print_prog(program)
			for func in program:
				#ACCOUNT FOR CONSTANTS
				is_constant = check_if_constant(func)
				if (not is_constant) and not (func in this_run):
					this_run.append(func)
					if func in freqs:
						freqs[func] += 1
					else:
						freqs[func] = 1


		max_threshold = round(max_frequency * .6)
		print "Max Threshold is: %i" % max_threshold
		#max_threshold = sorted(freqs.values())[-(len_freqs // 3)]
		#min_threshold = sorted(freqs.values())[20] #This ends up being 1

		interesting = {}

		for key in freqs:
			if (freqs[key] >= max_threshold):
				if not key in all_funcs:
					all_funcs.append(key)

				frequency = round((freqs[key] / float(max_frequency)), 2)
				interesting[key] = frequency
				print key, frequency

		print "Max possible occurances: %i" % max_frequency 
		print

		output = [tag]
		for instruction in all_funcs:
			if instruction in interesting:
				output.append(interesting[instruction])
			elif tag == "all_programs":
				frequency = round((freqs[key] / float(max_frequency)), 2)
				output.append(frequency)
			else:
				output.append(0.0)

		destwriter.writerow(output)

	destwriter.writerow(["Tag"] + all_funcs)

def goodfuncs2():

	if len(sys.argv) > 1:
	    destination = sys.argv[1]
	else:
	    print("please provide a destination file in the format <filename>.csv")
	    exit(1)


	destfile = open(destination, mode="w")
	destwriter = csv.writer(destfile)

	organized_programs = success_only()
	#I removed file from this list because no program with that tag has succeeded, providing no data
	possible_tags = ["all_programs", "IO", "arithmetic", "comparison", "boolean", "string_handling", "vectors"]

	for tag in possible_tags:
		#print tag
		all_funcs = []

		if tag == "all_programs":
			programs = organized_programs[0]
		elif tag == "IO":
			programs = organized_programs[1]
		elif tag == "arithmetic":
			programs = organized_programs[2]
		elif tag == "comparison":
			programs = organized_programs[3]
		elif tag == "boolean":
			programs = organized_programs[4]
		elif tag == "string_handling":
			programs = organized_programs[5]
		elif tag == "vectors":
			programs = organized_programs[6]
		

		max_frequency = len(programs)
		freqs = {}

		for program in programs:
			this_run = []
			#print_prog(program)
			for func in program:
				#ACCOUNT FOR CONSTANTS
				is_constant = check_if_constant(func)
				if (not is_constant) and not (func in this_run):
					this_run.append(func)
					if func in freqs:
						freqs[func] += 1
					else:
						freqs[func] = 1


		max_threshold = round(max_frequency * .6)
		#print "Max Threshold is: %i" % max_threshold
		#max_threshold = sorted(freqs.values())[-(len_freqs // 3)]
		#min_threshold = sorted(freqs.values())[20] #This ends up being 1

		interesting = {}

		for key in freqs:
			if (freqs[key] >= max_threshold):
				if not key in all_funcs:
					all_funcs.append(key)

				frequency = round((freqs[key] / float(max_frequency)), 2)
				interesting[key] = frequency
				print key, frequency

		#print "Max possible occurances: %i" % max_frequency 
		print

		output = [tag]
		for instruction in all_funcs:
			if instruction in interesting:
				output.append(interesting[instruction])
			elif tag == "all_programs":
				frequency = round((freqs[key] / float(max_frequency)), 2)
				output.append(frequency)
			else:
				output.append(0.0)
		destwriter.writerow(["Tag"] + all_funcs)
		destwriter.writerow(output)

def main():

	goodfuncs2()

if __name__ == '__main__':
	main()