import sys
import csv
from simplified_programs import simp_success_only


def check_if_constant(instruction):

	is_constant = True

	instr_types = ["in", "autoconstructive", "boolean", "char", "code", "environment", "exec", "float", "genome", "gtm", "integer", "noop", "print", "return", "string", "vector", "zip"]

	for category in instr_types:
		if instruction.startswith(category):
			is_constant = False
			break

	return is_constant


def fix_strings(program):
	
	print program

	newprog = []
	stringy = False

	for item in program:
		if stringy:
			if item.endswith('"""'):
				stringy = False
			newprog[-1] = newprog[-1] + item

		elif item.startswith('"""'):
			stringy = True
			newprog.append(item)

		else:
			newprog.append(item)

	print
	print newprog

	return newprog



if len(sys.argv) > 1:
    destination = sys.argv[1]
else:
    print("please provide a destination file in the format <filename>.csv")
    exit(1)

destfile = open(destination, mode="w")
destwriter = csv.writer(destfile)


organized_programs = simp_success_only()

all_programs = organized_programs[0]
number_io = organized_programs[1]
checksum = organized_programs[2]
collatz_numbers = organized_programs[3]
compare_string_lengths = organized_programs[4]
count_odds = organized_programs[5]
digits = organized_programs[6]
double_letters = organized_programs[7]
even_squares = organized_programs[8]
for_loop_index = organized_programs[9]
grade = organized_programs[10]
last_index_of_zero = organized_programs[11]
median = organized_programs[12]
mirror_image = organized_programs[13]
negative_to_zero = organized_programs[14]
pig_latin = organized_programs[15]
replace_space_with_newline = organized_programs[16]
scrabble_score = organized_programs[17]
small_or_large = organized_programs[18]
smallest = organized_programs[19]
string_differences = organized_programs[20]
string_lengths_backwards = organized_programs[21]
sum_of_squares = organized_programs[22]
super_anagrams = organized_programs[23]
syllables = organized_programs[24]
vector_average = organized_programs[25]
vectors_summed = organized_programs[26]
wallis_pi = organized_programs[27]
word_stats = organized_programs[28]
x_word_lines = organized_programs[29]


print_problems = [double_letters, median, number_io, replace_space_with_newline, string_lengths_backwards, syllables, vector_average, x_word_lines]
return_problems = [compare_string_lengths, count_odds, last_index_of_zero, mirror_image, negative_to_zero, replace_space_with_newline, scrabble_score, vector_average]
#these include the word "count" and "number of"
count_problems = [count_odds, syllables, replace_space_with_newline, syllables]



freqs = {}
total_programs = 0

#change this for each keyword
for lst in count_problems:

	for solution in lst:
		total_programs += 1
		this_run = []

		for term in solution:
			is_constant = check_if_constant(term)

			if (not is_constant) and not (term in this_run):

				if term in freqs:
					freqs[term] += 1
				else:
					freqs[term] = 1
				this_run.append(term)


funcslist = []
freqslist = []
for func in freqs:
	funcslist.append(func)

	frequency = freqs[func] / float(total_programs)
	freqslist.append(frequency)

destwriter.writerow(["Count/Number Of"])
destwriter.writerow(funcslist)
destwriter.writerow(freqslist)




freqs = {}
total_programs = 0

#change this for each keyword
for lst in print_problems:

	for solution in lst:
		total_programs += 1
		this_run = []

		for term in solution:
			is_constant = check_if_constant(term)

			if (not is_constant) and (not term in this_run):

				if term in freqs:
					freqs[term] += 1
				else:
					freqs[term] = 1
				this_run.append(term)


funcslist = []
freqslist = []
for func in freqs:
	funcslist.append(func)

	frequency = freqs[func] / float(total_programs)
	freqslist.append(frequency)


destwriter.writerow(["Print"])
destwriter.writerow(funcslist)
destwriter.writerow(freqslist)



freqs = {}
total_programs = 0

#change this for each keyword
for lst in return_problems:

	for solution in lst:
		total_programs += 1
		this_run = []

		for term in solution:
			is_constant = check_if_constant(term)

			if (not is_constant) and (not term in this_run):

				if term in freqs:
					freqs[term] += 1
				else:
					freqs[term] = 1
				this_run.append(term)


funcslist = []
freqslist = []
for func in freqs:
	funcslist.append(func)

	frequency = freqs[func] / float(total_programs)
	freqslist.append(frequency)


destwriter.writerow(["Return"])
destwriter.writerow(funcslist)
destwriter.writerow(freqslist)