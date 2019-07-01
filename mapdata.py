import math
import sys
import csv


# Make a verison of this that will run on HPC
#directories = ["/home/gwoolson/research/gwoolson/Grace_Research/mapdata/checksum"]

directories = ["C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/checksum/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/collatz-numbers/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/compare-string-lengths/", #MAY HAVE TO CHANGE THIS ONE
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/count-odds/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/digits/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/double-letters/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/even-squares/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/for-loop-index/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/grade/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/last-index-of-zero/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/median/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/mirror-image/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/negative-to-zero/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/number-io/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/pig-latin/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/replace-space-with-newline/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/scrabble-score/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/smallest/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/small-or-large/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/string-differences/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/string-lengths-backwards/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/sum-of-squares/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/super-anagrams/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/syllables/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/vector-average/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/vectors-summed/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/wallis-pi/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/word-stats/",
				"C:/Users/livel/Documents/Research2019/Grace_Research/mapdata/x-word-lines/"]


