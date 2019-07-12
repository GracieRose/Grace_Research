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

	return significant




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

	IO = [{}, {}]
	arithmetic = [{}, {}]
	comparison = [{}, {}]
	boolean = [{}, {}]
	string_handling = [{}, {}]
	vectors = [{}, {}]

	#a list of lists; a master list containing lists of programs broken down by problem they solve
	#just change this line for unsimplified 
	organized_programs = simp_success_only()

	#all_progs = organized_programs[0]
	for prob in range (1, len(organized_programs)):

		if prob == 1: #*************************************************************
			tags = [IO, arithmetic]

		if prob == 2:
			tags = [string_handling, arithmetic, IO]

		if prob == 3:
			tags = [arithmetic, comparison]

		if prob == 4: #*************************************************************
			tags = [boolean, comparison, string_handling]

		if prob == 5:
			tags = [vectors, arithmetic]

		if prob == 6:
			tags = [IO, arithmetic, string_handling]

		if prob == 7: #*************************************************************
			tags = [string_handling, IO, comparison]

		if prob == 8:
			tags = [IO, arithmetic]

		if prob == 9:
			tags = [IO, arithmetic]

		if prob == 10:
			tags = [IO, comparison]

		if prob == 11: #*************************************************************
			tags = [vectors, comparison]

		if prob == 12: #*************************************************************
			tags = [IO, comparison]

		if prob == 13: #*************************************************************
			tags = [vectors, boolean, comparison]

		if prob == 14: #*************************************************************
			tags = [vectors, comparison]

		if prob == 15:
			tags = [string_handling, IO]

		if prob == 16: #*************************************************************
			tags = [string_handling, IO, arithmetic]

		if prob == 17: #*************************************************************
			tags = [string_handling, arithmetic]

		if prob == 18:
			tags = [IO, comparison]

		if prob == 19:
			tags = [IO, comparison]

		if prob == 20:
			tags = [string_handling, comparison, IO]

		if prob == 21:
			tags = [IO, string_handling, vectors]

		if prob == 22:
			tags = [arithmetic]

		if prob == 23:
			tags = [boolean, string_handling, comparison]

		if prob == 24: #*************************************************************
			tags = [IO, string_handling, arithmetic]

		if prob == 25: #*************************************************************
			tags = [vectors, arithmetic]

		if prob == 26:
			tags = [vectors, arithmetic]

		if prob == 27:
			tags = [arithmetic]

		if prob == 28:
			tags = [IO, string_handling, arithmetic]

		if prob == 29: #*************************************************************
			tags = [string_handling, IO]


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

		for (f1, f2) in pairs:

			pair = (f1, f2)

			if pair in dists:
				avgdist = sum(dists[(f1, f2)]) / float(counts[(f1, f2)])
			else:
				avgdist = sum(dists[(f2, f1)]) / float(counts[(f2, f1)])

			frequency = float(pairs[pair]) / len(problem)

			for tag in tags: 

				#each tag is TAG = [pairs, dists], where pairs and dists are dictionaries containing lists
				if (f1, f2) in tag[0]:
					tag[0][(f1, f2)].append(frequency)
					tag[1][(f1, f2)].append(avgdist)

				elif (f2, f1) in tag[0]:
					tag[0][(f2, f1)].append(frequency)
					tag[1][(f2, f1)].append(avgdist)

				else:
					tag[0][(f1, f2)] = [frequency]
					tag[1][(f1, f2)] = [avgdist]


			"""
			significant = significance(f1, f2, freqs, pairs)
			if significant:
				print f1, f2

				if (f1, f2) in dists:
					avgdist = sum(dists[(f1, f2)]) / float(counts[(f1, f2)])
				else:
					avgdist = sum(dists[(f2, f1)]) / float(counts[(f2, f1)])
				#print avgdist
				print

				
				all_pairs.append((f1, f2))
				all_freqs.append(pairs[(f1, f2)])
				total_freqs.append((freqs[f1], freqs[f2]))
				total_dists.append(avgdist)"""

			pairs[(f1, f2)] = 0

		for elem in freqs:
			freqs[elem] = 0


		"""destwriter.writerow(all_pairs)
		destwriter.writerow(all_freqs)
		destwriter.writerow(total_freqs)
		destwriter.writerow(total_dists)"""

	all_pairs = []
	all_freqs = []
	total_dists = []

	destwriter.writerow(["IO"])
	for combo in IO[0]:
		#IO[0][combo] = list of frequencies
		avg_frequency = sum(IO[0][combo]) / 5

		#IO[1][combo] = list of average distances
		avg_distance = sum(IO[1][combo]) / len(IO[1][combo])
		#print avg_distance

		if avg_frequency >= .3:
			all_pairs.append(combo)
			print combo
			print IO[0][combo]
			#print len(IO)
			print avg_frequency
			all_freqs.append(avg_frequency)
			total_dists.append(avg_distance)
			#print avg_distance
			print

	destwriter.writerow(all_pairs)
	destwriter.writerow(all_freqs)
	destwriter.writerow(total_dists)


	all_pairs = []
	all_freqs = []
	total_dists = []

	destwriter.writerow(["arithmetic"])
	for combo in arithmetic[0]:
		#arithmetic[0][combo] = list of frequencies
		avg_frequency = sum(arithmetic[0][combo]) / 5

		#arithmetic[1][combo] = list of average distances
		avg_distance = sum(arithmetic[1][combo]) / len(arithmetic[1][combo])
		#print avg_distance

		if avg_frequency >= .3:
			all_pairs.append(combo)
			#print combo
			#print avg_frequency
			all_freqs.append(avg_frequency)
			total_dists.append(avg_distance)
			#print avg_distance
			#print

	destwriter.writerow(all_pairs)
	destwriter.writerow(all_freqs)
	destwriter.writerow(total_dists)



	all_pairs = []
	all_freqs = []
	total_dists = []

	destwriter.writerow(["comparison"])
	for combo in comparison[0]:
		#comparison[0][combo] = list of frequencies
		avg_frequency = sum(comparison[0][combo]) / 6

		#comparison[1][combo] = list of average distances
		avg_distance = sum(comparison[1][combo]) / len(comparison[1][combo])
		#print avg_distance

		if avg_frequency >= .3:
			all_pairs.append(combo)
			#print combo
			#print avg_frequency
			all_freqs.append(avg_frequency)
			total_dists.append(avg_distance)
			#print avg_distance
			#print

	destwriter.writerow(all_pairs)
	destwriter.writerow(all_freqs)
	destwriter.writerow(total_dists)



	all_pairs = []
	all_freqs = []
	total_dists = []

	destwriter.writerow(["boolean"])
	for combo in boolean[0]:
		#boolean[0][combo] = list of frequencies
		avg_frequency = sum(boolean[0][combo]) / 2

		#boolean[1][combo] = list of average distances
		avg_distance = sum(boolean[1][combo]) / len(boolean[1][combo])
		#print avg_distance

		if avg_frequency >= .3:
			all_pairs.append(combo)
			#print combo
			#print avg_frequency
			all_freqs.append(avg_frequency)
			total_dists.append(avg_distance)
			#print avg_distance
			#print

	destwriter.writerow(all_pairs)
	destwriter.writerow(all_freqs)
	destwriter.writerow(total_dists)



	all_pairs = []
	all_freqs = []
	total_dists = []

	destwriter.writerow(["string_handling"])
	for combo in string_handling[0]:
		#string_handling[0][combo] = list of frequencies
		avg_frequency = sum(string_handling[0][combo]) / 6

		#string_handling[1][combo] = list of average distances
		avg_distance = sum(string_handling[1][combo]) / len(string_handling[1][combo])
		#print avg_distance

		if avg_frequency >= .3:
			all_pairs.append(combo)
			#print combo
			#print avg_frequency
			all_freqs.append(avg_frequency)
			total_dists.append(avg_distance)
			#print avg_distance
			#print

	destwriter.writerow(all_pairs)
	destwriter.writerow(all_freqs)
	destwriter.writerow(total_dists)



	all_pairs = []
	all_freqs = []
	total_dists = []

	destwriter.writerow(["vectors"])
	for combo in vectors[0]:
		#vectors[0][combo] = list of frequencies
		avg_frequency = sum(vectors[0][combo]) / 4

		#vectors[1][combo] = list of average distances
		avg_distance = sum(vectors[1][combo]) / len(vectors[1][combo])
		#print avg_distance

		if avg_frequency >= .3:
			all_pairs.append(combo)
			#print combo
			#print avg_frequency
			all_freqs.append(avg_frequency)
			total_dists.append(avg_distance)
			#print avg_distance
			#print

	destwriter.writerow(all_pairs)
	destwriter.writerow(all_freqs)
	destwriter.writerow(total_dists)


def main():
	simplified_pairs()

if __name__ == '__main__':
	main()