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


zip_start1 = "tar -xvzf /home/thelmuth/Results/clustering-bench/even-squares/baseline-uniform/csv/data"
zip_end = ".csv.tar.gz"

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
zip_start19 = "tar -xvzf /home/thelmuth/Results/clustering-bench/vector-average/lexicase/csv/data"
zip_start20 = "tar -xvzf /home/thelmuth/Results/clustering-bench/vectors-summed/baseline-uniform/csv/data"
zip_start21 = "tar -xvzf /home/thelmuth/Results/clustering-bench/wallis-pi/baseline-uniform/csv/data"
zip_start22 = "tar -xvzf /home/thelmuth/Results/clustering-bench/word-stats/baseline-uniform/csv/data"
zip_start23 = "tar -xvzf /home/thelmuth/Results/clustering-bench/x-word-lines/baseline-uniform/csv/data"


service_tag = "tom"

##########################################################################
output_directory = "/home/gwoolson/Grace_Research/csvdata"

# Check to make sure directory doesn't exist; if not, create it
if output_directory[-1] != "/":
    output_directory += "/"
"""if os.path.isdir(output_directory):
    raise RuntimeError("Output directory already exists")"""

# Make alf file
#alf_file_string = output_directory + "clojush_runs.alf"
alf_file_string = output_directory + "clojush_scraping.alf"
alf_f = open(alf_file_string, "w")

alfcode = """##AlfredToDo 3.0
Job -title {%s} -subtasks {
""" % (title_string)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sscrabble-score/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start11, run, zip_end)
    command = "python fly_failedall.py run%i.csv %sscrabble-score/data%i.csv;" % (run, output_directory, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

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
