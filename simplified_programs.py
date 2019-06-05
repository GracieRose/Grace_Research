import math
import os
import sys


def print_prog(program):
    for element in program:
        print element


#maybe change this to make each list a file
def success_only():
    inputfiles = ["C:/Users/livel/Desktop/Research/cat_best_programs.csv", "C:/Users/livel/Desktop/Research/fly_best_programs.csv"]

    verbose = True
    if(len(sys.argv) > 1):
        verbose = False


    all_programs = []
    IO = []
    arithmetic = []
    comparison = []
    boolean = []
    string_handling = []
    vectors = []
    file = []


    final = [all_programs, IO, arithmetic, comparison, boolean, string_handling, vectors, file]

    for inputfile in inputfiles:    
        f = open(inputfile)

        tags = []

        for line in f:
            #print line

            if line[1] == "[":
                tags = line[3:-4].split("', '")
                #print line

            if line.startswith("Simplified:"):

                #print line

                program = line[:-1].split(",")[1:]
                all_programs.append(program)
                #print_prog(program)

                for tag in tags:
                    #print tag
                    if tag == "I/O":
                        IO.append(program)
                    elif tag == "arithmetic":
                        arithmetic.append(program)
                    elif tag == "comparison":
                        comparison.append(program)
                    elif tag == "boolean":
                        boolean.append(program)
                    elif tag == "string_handling":
                        string_handling.append(program)
                    elif tag == "vectors":
                        vectors.append(program)
                    elif tag == "file":
                        file.append(program)

    return final

def main():

    categorized_programs = success_only()


if __name__ == '__main__':
    main()