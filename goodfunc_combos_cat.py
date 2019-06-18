import sys
import csv
from success_by_problem import success_only
from simplified_programs import simp_success_only

def check_if_constant(instruction):

	is_constant = True

	instr_types = ["in", "autoconstructive", "boolean", "char", "code", "environment", "exec", "float", "genome", "gtm", "integer", "noop", "print", "return", "string", "vector", "zip"]

	for category in instr_types:
		if instruction.startswith(category):
			is_constant = False
			break

	return is_constant



def add_freqs(func, freqs):

	if func in freqs:
		freqs[func] += 1
	else:
		freqs[func] = 1

	return freqs




def simplify(program):

	new_prog = []

	for i in range(0, len(program)-1):
		current = program[i]
		rest = program[i+1:]
		if not (current in rest):
			new_prog.append(current)

	return new_prog



def significance(f1, f2, freqs, pairs):
	significant = False

	#if abs(freqs[f1] - freqs[f2]) < 30:

	if freqs[f1] <= freqs[f2]:
		if pairs[(f1, f2)] >= (.8 * freqs[f1]):
			significant = True

	else:
		if pairs[(f1, f2)] >= (.8 * freqs[f2]):
			significant = True

	if f1 == "in1" or f2 == "in1":
		significant = False

	if f1 == "in2" or f2 == "in2":
		significant = False

	return True




def calculate_distances(all_progs):

	dists = {}
	counts = {}

	for program in all_progs:

		for i in range(0, len(program) - 1):

			func = program[i]
			rest = program[i+1:]
			is_constant = check_if_constant(func)

			if not is_constant:

				for x in range(0, len(rest)):
					other = rest[x]

					#because x is zero when other is one away from func
					distance = x + 1

					if not check_if_constant(other):
						if (func, other) in dists:
							dists[(func, other)] += [distance]
							counts[(func, other)] += 1
							
						elif (other, func) in dists:
							dists[(other, func)] += [distance]
							counts[(other, func)] += 1

						else:
							dists[(func, other)] = [distance]
							counts[(func, other)] = 1

	return (dists, counts)


def simplified_pairs():
	if len(sys.argv) > 1:
	    destination = sys.argv[1]
	else:
	    print("please provide a destination file in the format <filename>.csv")
	    exit(1)

	destfile = open(destination, mode="w")
	destwriter = csv.writer(destfile)
    #final = [all_programs, number_io, checksum, collatz_numbers, compare_string_lengths, count_odds, digits, double_letters, even_squares, for_loop_index, grade, last_index_of_zero, median, mirror_image, negative_to_zero, pig_latin, replace_space_with_newline, scrabble_score, small_or_large, smallest, string_differences, string_lengths_backwards, sum_of_squares, super_anagrams, syllables, vector_average, vectors_summed, wallis_pi, word_stats, x_word_lines]

	#a list of lists; a master list containing lists of programs broken down by problem they solve
	#just change this line for unsimplified 
	organized_programs = simp_success_only()

	#all_progs = organized_programs[0]
	for prob in range (0, len(organized_programs)):

		if prob == 0:
			destwriter.writerow(["all_programs"])

		if prob == 1:
			destwriter.writerow(["number_io"])

		if prob == 2:
			destwriter.writerow(["checksum"])

		if prob == 3:
			destwriter.writerow(["collatz_numbers"])

		if prob == 4:
			destwriter.writerow(["compare_string_lengths"])

		if prob == 5:
			destwriter.writerow(["count_odds"])

		if prob == 6:
			destwriter.writerow(["digits"])

		if prob == 7:
			destwriter.writerow(["double_letters"])

		if prob == 8:
			destwriter.writerow(["even_squares"])

		if prob == 9:
			destwriter.writerow(["for_loop_index"])

		if prob == 10:
			destwriter.writerow(["grade"])

		if prob == 11:
			destwriter.writerow(["last_index_of_zero"])

		if prob == 12:
			destwriter.writerow(["median"])

		if prob == 13:
			destwriter.writerow(["mirror_image"])

		if prob == 14:
			destwriter.writerow(["negative_to_zero"])

		if prob == 15:
			destwriter.writerow(["pig_latin"])

		if prob == 16:
			destwriter.writerow(["replace_space_with_newline"])

		if prob == 17:
			destwriter.writerow(["scrabble_score"])

		if prob == 18:
			destwriter.writerow(["small_or_large"])

		if prob == 19:
			destwriter.writerow(["smallest"])

		if prob == 20:
			destwriter.writerow(["string_differences"])

		if prob == 21:
			destwriter.writerow(["string_lengths_backwards"])

		if prob == 22:
			destwriter.writerow(["sum_of_squares"])

		if prob == 23:
			destwriter.writerow(["super_anagrams"])

		if prob == 24:
			destwriter.writerow(["syllables"])

		if prob == 25:
			destwriter.writerow(["vector_average"])

		if prob == 26:
			destwriter.writerow(["vectors_summed"])

		if prob == 27:
			destwriter.writerow(["wallis_pi"])

		if prob == 28:
			destwriter.writerow(["word_stats"])

		if prob == 29:
			destwriter.writerow(["x_word_lines"])

		problem = organized_programs[prob]

		(dists, counts) = calculate_distances(problem)

		freqs = {}
		pairs = {}

		for oprogram in problem:

			program = simplify(oprogram)

			for i in range(0, len(program) - 1):

				func = program[i]
				rest = program[i+1:]
				is_constant = check_if_constant(func)

				if not is_constant:
					freqs = add_freqs(func, freqs)

					for other in rest:

						if not check_if_constant(other):

							if (func, other) in pairs:
								pairs[(func, other)] += 1
								
							#comment this line for ordered pairs, uncomment for unordered pairs
							elif (other, func) in pairs:
								pairs[(other, func)] += 1

							else:
								pairs[(func, other)] = 1

				if i == len(program) - 2:
					if not check_if_constant(program[i+1]):
						freqs = add_freqs(program[i+1], freqs)

		all_pairs = []
		all_freqs = []
		total_freqs = []
		total_dists = []
		minmax_dists = []

		for (f1, f2) in pairs:
			significant = significance(f1, f2, freqs, pairs)

			if significant:
				print f1, f2

				if (f1, f2) in dists:
					avgdist = sum(dists[(f1, f2)]) / float(counts[(f1, f2)])
					minimum = min(dists[(f1, f2)])
					maximum = max(dists[(f1, f2)])
				else:
					avgdist = sum(dists[(f2, f1)]) / float(counts[(f2, f1)])
					minimum = min(dists[(f2, f1)])
					maximum = max(dists[(f2, f1)])
				#print avgdist
				print

				all_pairs.append((f1, f2))
				all_freqs.append(pairs[(f1, f2)])
				total_freqs.append((freqs[f1], freqs[f2]))
				total_dists.append(avgdist)
				minmax_dists.append((minimum, maximum))

			pairs[(f1, f2)] = 0

		for elem in freqs:
			freqs[elem] = 0


		destwriter.writerow(all_pairs)
		destwriter.writerow(all_freqs)
		destwriter.writerow(total_freqs)
		destwriter.writerow(total_dists)
		destwriter.writerow(minmax_dists)


def main():
	simplified_pairs()

if __name__ == '__main__':
	main()