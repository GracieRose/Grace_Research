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
zip_start4 = "tar -xvzf /home/thelmuth/Results/clustering-bench/last-indexls-of-zero/baseline-uniform/csv/data"
zip_start5 = "tar -xvzf /home/thelmuth/Results/clustering-bench/median/baseline-uniform/csv/data"
zip_start6 = "tar -xvzf /home/thelmuth/Results/clustering-bench/mirror-image/baseline-uniform/csv/data"
zip_start7 = "tar -xvzf /home/thelmuth/Results/clustering-bench/negative-to-zero/lexicase/csv/data"
zip_start8 = "tar -xvzf /home/thelmuth/Results/clustering-bench/number-io/baseline-uniform/csv/data"
zip_start9 = "tar -xvzf /home/thelmuth/Results/clustering-bench/pig-latin/baseline-uniform/csv/data"
zip_start10 = "tar -xvzf /home/thelmuth/Results/clustering-bench/replace-space-with-newline/lexicase/csv/data"
zip_start11 = "tar -xvzf /home/thelmuth/Results/clustering-bench/scrabble-score/lexicase/csv/data" #*******************
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
zip_start23 = "tar -xvzf /home/thelmuth/Results/clustering-bench/x-word-lines/baseline-uniform/csv/data" #*****************************
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
output_directory = "/home/gwoolson/Grace_Research/csvdata"
runfile = "/home/gwoolson/Grace_Research/fly_failedall.py"

# Check to make sure directory doesn't exist; if not, create it
if output_directory[-1] != "/":
    output_directory += "/"
"""if os.path.isdir(output_directory):
    raise RuntimeError("Output directory already exists")"""

copyfile(runfile, output_directory + "checksum/fly_failedall.py")

copyfile(runfile, output_directory + "count-odds/fly_failedall.py")

copyfile(runfile, output_directory + "double-letters/fly_failedall.py")

copyfile(runfile, output_directory + "negative-to-zero/fly_failedall.py")

copyfile(runfile, output_directory + "replace-space-with-newline/fly_failedall.py")

copyfile(runfile, output_directory + "scrabble-score/fly_failedall.py")

copyfile(runfile, output_directory + "string-lengths-backwards/fly_failedall.py")

copyfile(runfile, output_directory + "syllables/fly_failedall.py")

copyfile(runfile, output_directory + "vector-average/fly_failedall.py")

# Make alf file
#alf_file_string = output_directory + "clojush_runs.alf"
alf_file_string = output_directory + "clojush_scraping.alf"
alf_f = open(alf_file_string, "w")

alfcode = """##AlfredToDo 3.0
Job -title {%s} -subtasks {
""" % (title_string)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %schecksum/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; \
    %s%i%s;" % (output_directory, zip_start24, run, zip_end)
    command = "python fly_failedall.py run%i.csv %schecksum/data%i.csv;" % (run, output_directory, run)
    outro_command = "cd /state/partition1/; rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s} -tags {max20}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %scount-odds/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; \
    %s%i%s;" % (output_directory, zip_start27, run, zip_end)
    command = "python fly_failedall.py run%i.csv %scount-odds/data%i.csv;" % (run, output_directory, run)
    outro_command = "cd /state/partition1/; rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s} -tags {max20}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sdouble-letters/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; \
    %s%i%s;" % (output_directory, zip_start29, run, zip_end)
    command = "python fly_failedall.py run%i.csv %sdouble-letters/data%i.csv;" % (run, output_directory, run)
    outro_command = "cd /state/partition1/; rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s} -tags {max20}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %snegative-to-zero/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; \
    %s%i%s;" % (output_directory, zip_start7, run, zip_end)
    command = "python fly_failedall.py run%i.csv %snegative-to-zero/data%i.csv;" % (run, output_directory, run)
    outro_command = "cd /state/partition1/; rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s} -tags {max20}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sreplace-space-with-newline/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; \
    %s%i%s;" % (output_directory, zip_start10, run, zip_end)
    command = "python fly_failedall.py run%i.csv %sreplace-space-with-newline/data%i.csv;" % (run, output_directory, run)
    outro_command = "cd /state/partition1/; rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s} -tags {max20}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sscrabble-score/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; \
    %s%i%s;" % (output_directory, zip_start11, run, zip_end)
    command = "python fly_failedall.py run%i.csv %sscrabble-score/data%i.csv;" % (run, output_directory, run)
    outro_command = "cd /state/partition1/; rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s} -tags {max20}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sstring-lengths-backwards/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; \
    %s%i%s;" % (output_directory, zip_start15, run, zip_end)
    command = "python fly_failedall.py run%i.csv %sstring-lengths-backwards/data%i.csv;" % (run, output_directory, run)
    outro_command = "cd /state/partition1/; rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s} -tags {max20}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %ssyllables/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; \
    %s%i%s;" % (output_directory, zip_start18, run, zip_end)
    command = "python fly_failedall.py run%i.csv %ssyllables/data%i.csv;" % (run, output_directory, run)
    outro_command = "cd /state/partition1/; rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s} -tags {max20}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %svector-average/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; \
    %s%i%s%i%s;" % (output_directory, zip_start19, run, vecavg_zend, run, vecavg_zend2)
    command = "python fly_failedall.py run%i.csv %svector-average/data%i.csv;" % (run, output_directory, run)
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
