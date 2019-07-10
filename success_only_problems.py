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
    

    final = [all_programs, number_io, checksum, collatz_numbers, compare_string_lengths, count_odds, digits, double_letters, even_squares, for_loop_index, grade, last_index_of_zero, median, mirror_image, negative_to_zero, pig_latin, replace_space_with_newline, scrabble_score, small_or_large, smallest, string_differences, string_lengths_backwards, sum_of_squares, super_anagrams, syllables, vector_average, vectors_summed, wallis_pi, word_stats, x_word_lines]
    prob = ""

    for inputfile in inputfiles:    
        f = open(inputfile)

        tags = []

        for line in f:
            #print line

            if line[0] == "[":
                prob = line[2:-3]   #change this
                #print prob

            if line.startswith("Successful"):

                #print line
                print prob

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

                if prob == "count-odds":
                    count_odds.append(program)

                if prob == "digits":
                    digits.append(program)

                if prob == "double-letters":
                    double_letters.append(program)

                if prob == "even-squares":
                    even_squares.append(program)

                if prob == "for-loop-index":
                    for_loop_index.append(program)

                if prob == "grade":
                    grade.append(program)

                if prob == "last-index-of-zero":
                    last_index_of_zero.append(program)

                if prob == "median":
                    median.append(program)

                if prob == "mirror-image":
                    mirror_image.append(program)

                if prob == "negative-to-zero":
                    negative_to_zero.append(program)

                if prob == "pig-latin":
                    pig_latin.append(program)

                if prob == "replace-space-with-newline":
                    replace_space_with_newline.append(program)

                if prob == "scrabble-score":
                    scrabble_score.append(program)

                if prob == "small-or-large":
                    small_or_large.append(program)

                if prob == "smallest":
                    smallest.append(program)

                if prob == "string-differences":
                    string_differences.append(program)

                if prob == "string-lengths-backwards":
                    string_lengths_backwards.append(program)

                if prob == "sum-of-squares":
                    sum_of_squares.append(program)

                if prob == "super-anagrams":
                    super_anagrams.append(program)

                if prob == "syllables":
                    syllables.append(program)

                if prob == "vector-average":
                    vector_average.append(program)

                if prob == "vectors-summed":
                    vectors_summed.append(program)

                if prob == "wallis-pi":
                    wallis_pi.append(program)

                if prob == "word-stats":
                    word_stats.append(program)

                if prob == "x-word-lines":
                    x_word_lines.append(program)

    return final

def main():

    categorized_programs = success_only()


if __name__ == '__main__':
    main()