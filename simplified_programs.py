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

    number_io = []
    checksum = []
    collatz_numbers = []
    compare_string_lengths = []
    count_odds = []
    digits = []
    double_letters = []
    even_squares = []
    for_loop_index = []
    grade = []
    last_index_of_zero = []
    median = []
    mirror_image = []
    negative_to_zero = []
    pig_latin = []
    replace_space_with_newline = []
    scrabble_score = []
    small_or_large = []
    smallest = []
    string_differences = []
    string_lengths_backwards = []
    sum_of_squares = []
    super_anagrams = []
    syllables = []
    vector_average = []
    vectors_summed = []
    wallis_pi = []
    word_stats = []
    x_word_lines = []
    

    problems = [number_io, checksum, collatz_numbers, compare_string_lengths, count_odds, digits, double_letters, even_squares, for_loop_index, grade, last_index_of_zero, median, mirror_image, negative_to_zero, pig_latin, replace_space_with_newline, scrabble_score, small_or_large, smallest, string_differences, string_lengths_backwards, sum_of_squares, super_anagrams, syllables, vector_average, vectors_summed, wallis_pi, word_stats, x_word_lines]

    for inputfile in inputfiles:    
        f = open(inputfile)

        tags = []

        for line in f:
            #print line

            if line[1] == "[":
                prob = line[2:-3]   #change this
                #print line

            if line.startswith("Simplified:"):

                #print line

                program = line[:-1].split(",")[1:]
                all_programs.append(program)
                #print_prog(program)

                if prob == "number-io":
                    number_io.append(program)

                if prob == "checksum":
                    checksum.append(program)

                if prob == "collatz-numbers":
                    collatz_numbers.append(program)

                if prob == "compare-string-lengths":
                    compare_string_lengths.append(program)

                if prob = "count-odds":
                    count_odds.append(prob)

                if prob = "digits":
                    digits.append(prob)

                if prob = "double-letters":
                    double_letters.append(prob)

                if prob = "even-squares":
                    even_squares.append(prob)

                if prob = "for-loop-index":
                    for_loop_index.append(prob)

                if prob = "grade":
                    grade.append(prob)

                if prob = "last-index-of-zero":
                    last_index_of_zero.append(prob)

                if prob = "median":
                    median.append(prob)

                if prob = "mirror-image":
                    mirror_image.append(prob)

                if prob = "negative-to-zero":
                    negative_to_zero.append(prob)

                if prob = "pig-latin":
                    pig_latin.append(prob)

                if prob = "replace-space-with-newline":
                    replace_space_with_newline.append(prob)

                if prob = "scrabble-score":
                    scrabble_score.append(prob)

                if prob = "small-or-large":
                    small_or_large.append(prob)

                if prob = "smallest":
                    smallest.append(prob)

                if prob == "string-differences":
                    string_differences.append(prob)

                if prob == "string-lengths-backwards":
                    string_lengths_backwards.append(prob)

                if prob == "sum-of-squares":
                    sum_of_squares.append(prob)

                if prob == "super-anagrams":
                    super_anagrams.append(prob)

                if prob == "syllables":
                    syllables.append(prob)

                if prob == "vector-average":
                    vector_average.append(prob)

                if prob == "vectors-summed":
                    vectors_summed.append(prob)

                if prob == "wallis-pi":
                    wallis_pi.append(prob)

                if prob == "word-stats":
                    word_stats.append(prob)

                if prob == "x-word-lines":
                    x_word_lines.append(prob)


                """
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
                        file.append(program)"""

    return final

def main():

    categorized_programs = success_only()


if __name__ == '__main__':
    main()