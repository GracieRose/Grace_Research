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

	#if abs(freqs[f1] - freqs[f2]) < 50:

	if freqs[f1] <= freqs[f2]:
		if pairs[(f1, f2)] >= (.6 * freqs[f1]):
			significant = True

	else:
		if pairs[(f1, f2)] >= (.6 * freqs[f2]):
			significant = True

	if f1 == "in1" or f2 == "in1":
		significant = False

	if f1 == "in2" or f2 == "in2":
		significant = False

	return significant




def all_pairs():
	if len(sys.argv) > 1:
	    destination = sys.argv[1]
	else:
	    print("please provide a destination file in the format <filename>.csv")
	    exit(1)

	destfile = open(destination, mode="w")
	destwriter = csv.writer(destfile)

	#a list of lists; a master list containing lists of programs broken down by problem they solve
	organized_programs = success_only()

	all_progs = organized_programs[0]

	pairs = {}
	freqs = {}


	for program in all_progs:

		program = simplify(program)

		for i in range(0, len(program) - 1):

			func = program[i]
			other = program[i+1]
			is_constant = check_if_constant(func)

			if not is_constant:
				freqs = add_freqs(func, freqs)

				if not check_if_constant(other):
					if (func, other) in pairs:
						pairs[(func, other)] += 1
						
					elif (other, func) in pairs:
						pairs[(other, func)] += 1

					else:
						pairs[(func, other)] = 1

			if i == len(program) - 2:
				if not check_if_constant(program[i+1]):
					add_freqs(other, freqs)

	all_pairs = []
	all_freqs = []
	total_freqs = []

	for (f1, f2) in pairs:
		significant = significance(f1, f2, freqs, pairs)

		if significant:
			all_pairs.append((f1, f2))
			all_freqs.append(pairs[(f1, f2)])
			total_freqs.append((freqs[f1], freqs[f2]))

		print "%s, %s: %i" % (f1, f2, pairs[(f1, f2)])
		print "%s: %i" % (f1, freqs[f1])
		print "%s: %i" % (f2, freqs[f2])
		print


	destwriter.writerow(all_pairs)
	destwriter.writerow(all_freqs)
	destwriter.writerow(total_freqs)



def simplified_pairs_ordered():
	if len(sys.argv) > 1:
	    destination = sys.argv[1]
	else:
	    print("please provide a destination file in the format <filename>.csv")
	    exit(1)

	destfile = open(destination, mode="w")
	destwriter = csv.writer(destfile)

	#a list of lists; a master list containing lists of programs broken down by problem they solve
	organized_programs = simp_success_only()

	all_progs = organized_programs[0]

	pairs = {}
	freqs = {}


	#this includes doubles in the program, should fix
	for program in all_progs:

		program = simplify(program)

		for i in range(0, len(program) - 1):

			func = program[i]
			other = program[i+1]
			is_constant = check_if_constant(func)

			if not is_constant:
				freqs = add_freqs(func, freqs)

				if not check_if_constant(other):
					if (func, other) in pairs:
						pairs[(func, other)] += 1

					else:
						pairs[(func, other)] = 1

			if i == len(program) - 2:
				if not check_if_constant(program[i+1]):
					add_freqs(other, freqs)


	all_pairs = []
	all_freqs = []
	total_freqs = []

	for (f1, f2) in pairs:
		significant = significance(f1, f2, freqs, pairs)

		if significant:
			all_pairs.append((f1, f2))
			all_freqs.append(pairs[(f1, f2)])
			total_freqs.append((freqs[f1], freqs[f2]))

		print "%s, %s: %i" % (f1, f2, pairs[(f1, f2)])
		print "%s: %i" % (f1, freqs[f1])
		print "%s: %i" % (f2, freqs[f2])
		print


	destwriter.writerow(all_pairs)
	destwriter.writerow(all_freqs)
	destwriter.writerow(total_freqs)


def simplified_pairs_unordered():
	if len(sys.argv) > 1:
	    destination = sys.argv[1]
	else:
	    print("please provide a destination file in the format <filename>.csv")
	    exit(1)

	destfile = open(destination, mode="w")
	destwriter = csv.writer(destfile)

	#a list of lists; a master list containing lists of programs broken down by problem they solve
	organized_programs = simp_success_only()

	all_progs = organized_programs[0]

	pairs = {}
	freqs = {}


	#this includes doubles in the program, should fix
	for program in all_progs:

		program = simplify(program)

		for i in range(0, len(program) - 1):

			func = program[i]
			other = program[i+1]
			is_constant = check_if_constant(func)

			if not is_constant:
				freqs = add_freqs(func, freqs)

				if not check_if_constant(other):
					if (func, other) in pairs:
						pairs[(func, other)] += 1
						
					elif (other, func) in pairs:
						pairs[(other, func)] += 1

					else:
						pairs[(func, other)] = 1

			if i == len(program) - 2:
				if not check_if_constant(program[i+1]):
					add_freqs(other, freqs)

	all_pairs = []
	all_freqs = []
	total_freqs = []

	for (f1, f2) in pairs:
		significant = significance(f1, f2, freqs, pairs)

		if significant:
			all_pairs.append((f1, f2))
			all_freqs.append(pairs[(f1, f2)])
			total_freqs.append((freqs[f1], freqs[f2]))

		print "%s, %s: %i" % (f1, f2, pairs[(f1, f2)])
		print "%s: %i" % (f1, freqs[f1])
		print "%s: %i" % (f2, freqs[f2])
		print


	destwriter.writerow(all_pairs)
	destwriter.writerow(all_freqs)
	destwriter.writerow(total_freqs)


def main():
	#all_pairs()
	simplified_pairs_ordered()

if __name__ == '__main__':
	main()