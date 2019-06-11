import sys
import csv
from success_by_problem import success_only
#from simplified_programs import success_only

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


#this includes doubles in the program, should fix
x = len(all_progs)
print x

for program in all_progs:

	print program[0]

	this_run = []

	for i in range(0, len(program) - 1):

		func = program[i]
		rest = program[i+1:]
		is_constant = check_if_constant(func)

		if not is_constant:
			freqs = add_freqs(func, freqs)

			for other in rest:

				if not func in this_run:

					if not check_if_constant(other):
						if (func, other) in pairs:
							pairs[(func, other)] += 1
							this_run.append(func)
							
						elif (other, func) in pairs:
							pairs[(other, func)] += 1
							this_run.append(func)

						else:
							pairs[(func, other)] = 1
							this_run.append(func)

						#print "Not a constant!"

			if i == len(program) - 2:
				if not check_if_constant(program[i+1]):
					add_freqs(program[i+1], freqs)

all_pairs = []
all_freqs = []
total_freqs = []

for (f1, f2) in pairs:
	"""all_pairs.append((f1, f2))
	all_freqs.append(pairs[(f1, f2)])
	total_freqs.append((freqs[f1], freqs[f2]))"""

	print "%s, %s: %i" % (f1, f2, pairs[(f1, f2)])
	print "%s: %i" % (f1, freqs[f1])
	print "%s: %i" % (f2, freqs[f2])
	print