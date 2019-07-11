import os, stat
from shutil import copyfile

##########################################################################
# Settings
number_runs = 100

title_string = "Data collection of function frequencies in programs throughout a GP run"

description = """A collection of compact csv data files representing program
counts of all individuals in evolutionary runs """

##########################################################################
# Uncomment the following if you want to print timings in the logs
#example_file += " :print-timings true"

##########################################################################
# Probably don't change these
#output_prefix = "log"
#output_postfix = ".txt"
output_prefix = "run"
output_postfix = ".csv"


zip_start1 = "tar -xvzf /home/thelmuth/Results/clustering-bench/even-squares/baseline-uniform/csv/data"
zip_start2 = "tar -xvzf /home/thelmuth/Results/clustering-bench/for-loop-index/baseline-uniform/csv/data"
zip_start3 = "tar -xvzf /home/thelmuth/Results/clustering-bench/grade/baseline-uniform/csv/data"
zip_start4 = "tar -xvzf /home/thelmuth/Results/clustering-bench/last-index-of-zero/baseline-uniform/csv/data"
zip_start5 = "tar -xvzf /home/thelmuth/Results/clustering-bench/median/baseline-uniform/csv/data"
zip_start6 = "tar -xvzf /home/thelmuth/Results/clustering-bench/mirror-image/baseline-uniform/csv/data"
zip_start7 = "tar -xvzf /home/thelmuth/Results/clustering-bench/negative-to-zero/lexicase/csv/data"
zip_start8 = "tar -xvzf /home/thelmuth/Results/clustering-bench/number-io/baseline-uniform/csv/data"
zip_start9 = "tar -xvzf /home/thelmuth/Results/clustering-bench/pig-latin/baseline-uniform/csv/data"
zip_start10 = "tar -xvzf /home/thelmuth/Results/clustering-bench/replace-space-with-newline/lexicase/csv/data"
zip_start11 = "tar -xvzf /home/thelmuth/Results/clustering-bench/scrabble-score/lexicase/csv/data"
zip_start12 = "tar -xvzf /home/thelmuth/Results/clustering-bench/smallest/baseline-uniform/csv/data"
zip_start13 = "tar -xvzf /home/thelmuth/Results/clustering-bench/small-or-large/baseline-uniform/csv/data"
zip_start14 = "tar -xvzf /home/thelmuth/Results/clustering-bench/string-differences/baseline-uniform/csv/data"
zip_start15 = "tar -xvzf /home/thelmuth/Results/clustering-bench/string-lengths-backwards/lexicase/csv/data"
zip_start16 = "tar -xvzf /home/thelmuth/Results/clustering-bench/sum-of-squares/baseline-uniform/csv/data"
zip_start17 = "tar -xvzf /home/thelmuth/Results/clustering-bench/super-anagrams/baseline-uniform/csv/data"
zip_start18 = "tar -xvzf /home/thelmuth/Results/clustering-bench/syllables/lexicase/csv/data"
zip_start19 = "gunzip -c /home/thelmuth/Results/clustering-bench/vector-average/lexicase/csv/data"
zip_start20 = "tar -xvzf /home/thelmuth/Results/clustering-bench/vectors-summed/baseline-uniform/csv/data"
zip_start21 = "tar -xvzf /home/thelmuth/Results/clustering-bench/wallis-pi/baseline-uniform/csv/data"
zip_start22 = "tar -xvzf /home/thelmuth/Results/clustering-bench/word-stats/baseline-uniform/csv/data"
zip_start23 = "tar -xvzf /home/thelmuth/Results/clustering-bench/x-word-lines/baseline-uniform/csv/data"
zip_start24 = "tar -xvzf /home/thelmuth/Results/clustering-bench/checksum/lexicase/csv/data"
zip_start25 = "tar -xvzf /home/thelmuth/Results/clustering-bench/collatz-numbers/baseline-uniform/csv/data"
zip_start26 = "tar -xvzf /home/thelmuth/Results/clustering-bench/compare-string-lengths/baseline-uniform/csv/data"
zip_start27 = "tar -xvzf /home/thelmuth/Results/clustering-bench/count-odds/lexicase/csv/data"
zip_start28 = "tar -xvzf /home/thelmuth/Results/clustering-bench/digits/baseline-uniform/csv/data"
zip_start29 = "tar -xvzf /home/thelmuth/Results/clustering-bench/double-letters/lexicase/csv/data"

zip_end = ".csv.tar.gz -C /state/partition1/"
vecavg_zend = ".csv.gz > /state/partition1/data"
vecavg_zend2 = ".csv"

service_tag = "tom"

##########################################################################
output_directory = "/home/gwoolson/Grace_Research/mapdata"
runfile = "/home/gwoolson/Grace_Research/map.py"

# Check to make sure directory doesn't exist; if not, create it
if output_directory[-1] != "/":
    output_directory += "/"
"""if os.path.isdir(output_directory):
    raise RuntimeError("Output directory already exists")"""

"""os.mkdir(output_directory)

os.mkdir(output_directory + "checksum/")
os.mkdir(output_directory + "checksum/donetest")
copyfile(runfile, output_directory + "checksum/map.py")

os.mkdir(output_directory + "collatz-numbers/")
os.mkdir(output_directory + "collatz-numbers/donetest")
copyfile(runfile, output_directory + "collatz-numbers/map.py")

os.mkdir(output_directory + "compare-string-lengths")
os.mkdir(output_directory + "compare-string-lengths/donetest")
copyfile(runfile, output_directory + "compare-string-lengths/map.py")

os.mkdir(output_directory + "count-odds")
os.mkdir(output_directory + "count-odds/donetest")
copyfile(runfile, output_directory + "count-odds/map.py")

os.mkdir(output_directory + "digits/")
os.mkdir(output_directory + "digits/donetest")
copyfile(runfile, output_directory + "digits/map.py")

os.mkdir(output_directory + "double-letters/")
os.mkdir(output_directory + "double-letters/donetest")
copyfile(runfile, output_directory + "double-letters/map.py")

os.mkdir(output_directory + "even-squares/")
os.mkdir(output_directory + "even-squares/donetest")
copyfile(runfile, output_directory + "even-squares/map.py")

os.mkdir(output_directory + "for-loop-index/")
os.mkdir(output_directory + "for-loop-index/donetest")
copyfile(runfile, output_directory + "for-loop-index/map.py")

os.mkdir(output_directory + "grade/")
os.mkdir(output_directory + "grade/donetest")
copyfile(runfile, output_directory + "grade/map.py")

os.mkdir(output_directory + "last-index-of-zero/")
os.mkdir(output_directory + "last-index-of-zero/donetest")
copyfile(runfile, output_directory + "last-index-of-zero/map.py")

os.mkdir(output_directory + "median/")
os.mkdir(output_directory + "median/donetest")
copyfile(runfile, output_directory + "median/map.py")

os.mkdir(output_directory + "mirror-image/")
os.mkdir(output_directory + "mirror-image/donetest")
copyfile(runfile, output_directory + "mirror-image/map.py")

os.mkdir(output_directory + "negative-to-zero/")
os.mkdir(output_directory + "negative-to-zero/donetest")
copyfile(runfile, output_directory + "negative-to-zero/map.py")

os.mkdir(output_directory + "number-io/")
os.mkdir(output_directory + "number-io/donetest")
copyfile(runfile, output_directory + "number-io/map.py")

os.mkdir(output_directory + "pig-latin/")
os.mkdir(output_directory + "pig-latin/donetest")
copyfile(runfile, output_directory + "pig-latin/map.py")

os.mkdir(output_directory + "replace-space-with-newline/")
os.mkdir(output_directory + "replace-space-with-newline/donetest")
copyfile(runfile, output_directory + "replace-space-with-newline/map.py")

os.mkdir(output_directory + "scrabble-score/")
os.mkdir(output_directory + "scrabble-score/donetest")
copyfile(runfile, output_directory + "scrabble-score/map.py")

os.mkdir(output_directory + "smallest/")
os.mkdir(output_directory + "smallest/donetest")
copyfile(runfile, output_directory + "smallest/map.py")

os.mkdir(output_directory + "small-or-large/")
os.mkdir(output_directory + "small-or-large/donetest")
copyfile(runfile, output_directory + "small-or-large/map.py")

os.mkdir(output_directory + "string-differences/")
os.mkdir(output_directory + "string-differences/donetest")
copyfile(runfile, output_directory + "string-differences/map.py")

os.mkdir(output_directory + "string-lengths-backwards/")
os.mkdir(output_directory + "string-lengths-backwards/donetest")
copyfile(runfile, output_directory + "string-lengths-backwards/map.py")

os.mkdir(output_directory + "sum-of-squares/")
os.mkdir(output_directory + "sum-of-squares/donetest")
copyfile(runfile, output_directory + "sum-of-squares/map.py")

os.mkdir(output_directory + "super-anagrams/")
os.mkdir(output_directory + "super-anagrams/donetest")
copyfile(runfile, output_directory + "super-anagrams/map.py")

os.mkdir(output_directory + "syllables/")
os.mkdir(output_directory + "syllables/donetest")
copyfile(runfile, output_directory + "syllables/map.py")

os.mkdir(output_directory + "vector-average/")
os.mkdir(output_directory + "vector-average/donetest")
copyfile(runfile, output_directory + "vector-average/map.py")

os.mkdir(output_directory + "vectors-summed/")
os.mkdir(output_directory + "vectors-summed/donetest")
copyfile(runfile, output_directory + "vectors-summed/map.py")

os.mkdir(output_directory + "wallis-pi/")
os.mkdir(output_directory + "wallis-pi/donetest")
copyfile(runfile, output_directory + "wallis-pi/map.py")

os.mkdir(output_directory + "word-stats/")
os.mkdir(output_directory + "word-stats/donetest")
copyfile(runfile, output_directory + "word-stats/map.py")

os.mkdir(output_directory + "x-word-lines/")
os.mkdir(output_directory + "x-word-lines/donetest")
copyfile(runfile, output_directory + "x-word-lines/map.py")"""


copyfile(runfile, output_directory + "checksum/map.py")

#copyfile(runfile, output_directory + "collatz-numbers/map.py")

#copyfile(runfile, output_directory + "compare-string-lengths/map.py")

copyfile(runfile, output_directory + "count-odds/map.py")

#copyfile(runfile, output_directory + "digits/map.py")

copyfile(runfile, output_directory + "double-letters/map.py")

#copyfile(runfile, output_directory + "even-squares/map.py")

#copyfile(runfile, output_directory + "for-loop-index/map.py")

#copyfile(runfile, output_directory + "grade/map.py")

#copyfile(runfile, output_directory + "last-index-of-zero/map.py")

#copyfile(runfile, output_directory + "median/map.py")

#copyfile(runfile, output_directory + "mirror-image/map.py")

copyfile(runfile, output_directory + "negative-to-zero/map.py")

#copyfile(runfile, output_directory + "number-io/map.py")

#copyfile(runfile, output_directory + "pig-latin/map.py")

#copyfile(runfile, output_directory + "replace-space-with-newline/map.py")

copyfile(runfile, output_directory + "scrabble-score/map.py")

#copyfile(runfile, output_directory + "smallest/map.py")

#copyfile(runfile, output_directory + "small-or-large/map.py")

#copyfile(runfile, output_directory + "string-differences/map.py")

copyfile(runfile, output_directory + "string-lengths-backwards/map.py")

#copyfile(runfile, output_directory + "sum-of-squares/map.py")

#copyfile(runfile, output_directory + "super-anagrams/map.py")

copyfile(runfile, output_directory + "syllables/map.py")

copyfile(runfile, output_directory + "vector-average/map.py")

#copyfile(runfile, output_directory + "vectors-summed/map.py")

#copyfile(runfile, output_directory + "wallis-pi/map.py")

#copyfile(runfile, output_directory + "word-stats/map.py")

#copyfile(runfile, output_directory + "x-word-lines/map.py")


# Make alf file
#alf_file_string = output_directory + "clojush_runs.alf"
alf_file_string = output_directory + "clojush_scraping.alf"
alf_f = open(alf_file_string, "w")

alfcode = """##AlfredToDo 3.0
Job -title {%s} -subtasks {
""" % (title_string)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sreplace-space-with-newline/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; \
    %s%i%s;" % (output_directory, zip_start10, run, zip_end)
    command = "python map.py %sreplace-space-with-newline/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "cd /state/partition1/; rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s} -tags {max20}
    }
""" % (title_string, run, full_command, service_tag)



alfcode += "}\n"

alf_f.writelines(alfcode)
alf_f.close()

# Don't touch this Woolson
# Run tractor command
source_string = "source /etc/sysconfig/pixar"
pixar_string = "/opt/pixar/tractor-blade-1.7.2/python/bin/python2.6 /opt/pixar/tractor-blade-1.7.2/tractor-spool.py --engine=fly:8000"

os.system("%s;%s %s" % (source_string, pixar_string, alf_file_string))
