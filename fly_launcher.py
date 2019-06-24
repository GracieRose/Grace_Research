import os, stat

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


zip_start1 = "tar -xvzf /home/thelmuth/Results/clustering-bench/count-odds/lexicase/csv/data"
zip_end1 = ".csv.tar.gz"

service_tag = "tom"

##########################################################################
output_directory = "/home/gwoolson/csvdata"

# Check to make sure directory doesn't exist; if not, create it
if output_directory[-1] != "/":
    output_directory += "/"
if os.path.isdir(output_directory):
    raise RuntimeError("Output directory already exists")

"""os.mkdir(output_directory)
os.mkdir(output_directory + "checksum/")
os.mkdir(output_directory + "collatz-numbers/")

os.mkdir(output_directory + "digits/")
os.mkdir(output_directory + "digits/donetest")

os.mkdir(output_directory + "double-letters/")
os.mkdir(output_directory + "double-letters/donetest")

os.mkdir(output_directory + "even-squares/")
os.mkdir(output_directory + "even-squares/donetest")

os.mkdir(output_directory + "for-loop-index/")
os.mkdir(output_directory + "for-loop-index/donetest")

os.mkdir(output_directory + "grade/")
os.mkdir(output_directory + "grade/donetest")

os.mkdir(output_directory + "last-index-of-zero/")
os.mkdir(output_directory + "last-index-of-zero/donetest")

os.mkdir(output_directory + "median/")
os.mkdir(output_directory + "median/donetest")

os.mkdir(output_directory + "mirror-image/")
os.mkdir(output_directory + "mirror-image/donetest")

os.mkdir(output_directory + "negative-to-zero/")
os.mkdir(output_directory + "negative-to-zero/donetest")

os.mkdir(output_directory + "number-io/")
os.mkdir(output_directory + "number-io/donetest")

os.mkdir(output_directory + "pig-latin/")
os.mkdir(output_directory + "pig-latin/donetest")

os.mkdir(output_directory + "replace-space-with-newline/")
os.mkdir(output_directory + "replace-space-with-newline/donetest")

os.mkdir(output_directory + "scrabble-score/")
os.mkdir(output_directory + "scrabble-score/donetest")

os.mkdir(output_directory + "smallest/")
os.mkdir(output_directory + "smallest/donetest")

os.mkdir(output_directory + "small-or-large/")
os.mkdir(output_directory + "small-or-large/donetest")

os.mkdir(output_directory + "string-differences/")
os.mkdir(output_directory + "string-differences/donetest")

os.mkdir(output_directory + "string-lengths-backwards/")
os.mkdir(output_directory + "string-lengths-backwards/donetest")

os.mkdir(output_directory + "sum-of-squares/")
os.mkdir(output_directory + "sum-of-squares/donetest")

os.mkdir(output_directory + "super-anagrams/")
os.mkdir(output_directory + "super-anagrams/donetest")

os.mkdir(output_directory + "syllables/")
os.mkdir(output_directory + "syllables/donetest")

os.mkdir(output_directory + "vector-average/")
os.mkdir(output_directory + "vector-average/donetest")

os.mkdir(output_directory + "vectors-summed/")
os.mkdir(output_directory + "vectors-summed/donetest")

os.mkdir(output_directory + "wallis-pi/")
os.mkdir(output_directory + "wallis-pi/donetest")

os.mkdir(output_directory + "word-stats/")
os.mkdir(output_directory + "word-stats/donetest")

os.mkdir(output_directory + "x-word-lines/")
os.mkdir(output_directory + "x-word-lines/donetest")"""


os.mkdir(output_directory)

# Make alf file
#alf_file_string = output_directory + "clojush_runs.alf"
alf_file_string = output_directory + "clojush_scraping.alf"
alf_f = open(alf_file_string, "w")

alfcode = """##AlfredToDo 3.0
Job -title {%s} -subtasks {
""" % (title_string)

#change this! Enter bash commands on the command line to do whatever you want, then enter those commands here, separated by ;
for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %scount-odds/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (outputDirectory, zip_start1, run, zip_end1)
    command = "python fly_failedall.py run%i.csv %scount-odds/data%i.csv;" % (outputDirectory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
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
