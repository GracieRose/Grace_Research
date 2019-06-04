from g_success_programs import success_only


def check_if_constant(instruction):

	is_constant = False
	numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

	#booleans
	if instruction == "true" or instruction == "false":
		is_constant = True

	#integers/floats
	if instruction[0] in numbers:
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



organized_programs = success_only()
#["all_programs", "IO", "arithmetic", "comparison", "boolean", "string_handling", "vectors", "file"]

tag = "all_programs"

if tag == "all_programs":
	programs = organized_programs[0]
elif tag == "IO":
	programs = organized_programs[1]
elif tag == "arithmetic":
	programs = organized_programs[2]
elif tag == "comparison":
	programs = organized_programs[3]
elif tag = "boolean":
	programs = organized_programs[4]
elif tag == "string_handling":
	programs = organized_programs[5]
elif tag == "vectors":
	programs = organized_programs[6]
elif tag == "file":
	programs = organized_programs[7]


freqs = {}

for program in programs:
	this_run = []
	for func in program:
		#ACCOUNT FOR CONSTANTS
		is_constant = check_if_constant(func)
		#if not is_constant:


