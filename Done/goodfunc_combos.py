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

	if abs(freqs[f1] - freqs[f2]) < 50:

		if freqs[f1] <= freqs[f2]:
			if pairs[(f1, f2)] >= (.9 * freqs[f1]):
				significant = True

		else:
			if pairs[(f1, f2)] >= (.9 * freqs[f2]):
				significant = True

	return significant




def calculate_distances(all_progs):

	dists = {}
	counts = {}

	for program in all_progs:

		program = fix_strings(program)

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
						
						#comment this line out for ordered	
						#elif (other, func) in dists:
						#	dists[(other, func)] += [distance]
						#	counts[(other, func)] += 1

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

	#a list of lists; a master list containing lists of programs broken down by problem they solve
	#just change this line for unsimplified 
	organized_programs = simp_success_only()

	all_progs = organized_programs[0]

	pairs = {}
	freqs = {}

	(dists, counts) = calculate_distances(all_progs)

	for oprogram in all_progs:

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
						#elif (other, func) in pairs:
						#	pairs[(other, func)] += 1

						else:
							pairs[(func, other)] = 1

			if i == len(program) - 2:
				if not check_if_constant(program[i+1]):
					add_freqs(program[i+1], freqs)

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
				distlst = dists[(f1, f2)]
				#distlst.sort()
				print distlst
				minimum = min(dists[(f1, f2)])
				maximum = max(dists[(f1, f2)])
			else:
				avgdist = sum(dists[(f2, f1)]) / float(counts[(f2, f1)])
				distlst = dists[(f2, f1)]
				#distlst.sort()
				print distlst
				minimum = min(dists[(f2, f1)])
				maximum = max(dists[(f2, f1)])
			print avgdist
			print

			all_pairs.append((f1, f2))
			all_freqs.append(pairs[(f1, f2)])
			total_freqs.append((freqs[f1], freqs[f2]))
			total_dists.append(avgdist)
			minmax_dists.append((minimum, maximum))


	destwriter.writerow(all_pairs)
	destwriter.writerow(all_freqs)
	destwriter.writerow(total_freqs)
	destwriter.writerow(total_dists)
	destwriter.writerow(minmax_dists)

def main():
	simplified_pairs()

if __name__ == '__main__':
	main()