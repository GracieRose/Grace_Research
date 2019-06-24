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
zip_start19 = "tar -xvzf /home/thelmuth/Results/clustering-bench/vector-average/lexicase/csv/data"
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



zip_end = ".csv.tar.gz"

service_tag = "tom"

##########################################################################
output_directory = "/home/gwoolson/mapdata"
runfile = "/home/gwoolson/Grace_Research/map.py"

# Check to make sure directory doesn't exist; if not, create it
if output_directory[-1] != "/":
    output_directory += "/"
"""if os.path.isdir(output_directory):
    raise RuntimeError("Output directory already exists")"""

os.mkdir(output_directory)

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
os.mkdir(output_directory + "x-word-lines/donetest")


# Make alf file
#alf_file_string = output_directory + "clojush_runs.alf"
alf_file_string = output_directory + "clojush_scraping.alf"
alf_f = open(alf_file_string, "w")

alfcode = """##AlfredToDo 3.0
Job -title {%s} -subtasks {
""" % (title_string)

#change this! Enter bash commands on the command line to do whatever you want, then enter those commands here, separated by ;
for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %seven-squares/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start1, run, zip_end)
    command = "python map.py %seven-squares/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sfor-loop-index/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start2, run, zip_end)
    command = "python map.py %sfor-loop-index/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sgrade/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start3, run, zip_end)
    command = "python map.py %sgrade/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %slast-index-of-zero/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start4, run, zip_end)
    command = "python map.py %slast-index-of-zero/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %smedian/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start5, run, zip_end)
    command = "python map.py %smedian/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %smirror-image/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start6, run, zip_end)
    command = "python map.py %smirror-image/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %snegative-to-zero/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start7, run, zip_end)
    command = "python map.py %snegative-to-zero/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %snumber-io/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start8, run, zip_end)
    command = "python map.py %snumber-io/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %spig-latin/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start9, run, zip_end)
    command = "python map.py %spig-latin/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sreplace-space-with-newline/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start10, run, zip_end)
    command = "python map.py %sreplace-space-with-newline/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sscrabble-score/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start11, run, zip_end)
    command = "python map.py %sscrabble-score/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %ssmallest/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start12, run, zip_end)
    command = "python map.py %ssmallest/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %ssmall-or-large/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start13, run, zip_end)
    command = "python map.py %ssmall-or-large/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sstring-differences/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start14, run, zip_end)
    command = "python map.py %sstring-differences/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sstring-lengths-backwards/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start15, run, zip_end)
    command = "python map.py %sstring-lengths-backwards/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %ssum-of-squares/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start16, run, zip_end)
    command = "python map.py %ssum-of-squares/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %ssuper-anagrams/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start17, run, zip_end)
    command = "python map.py %ssuper-anagrams/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %ssyllables/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start18, run, zip_end)
    command = "python map.py %ssyllables/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %svector-average/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start19, run, zip_end)
    command = "python map.py %svector-average/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %svectors-summed/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start20, run, zip_end)
    command = "python map.py %svectors-summed/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)

for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %swallis-pi/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start21, run, zip_end)
    command = "python map.py %swallis-pi/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sword-stats/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start22, run, zip_end)
    command = "python map.py %sword-stats/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sx-word-lines/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start23, run, zip_end)
    command = "python map.py %sx-word-lines/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)




for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %schecksum/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start24, run, zip_end)
    command = "python map.py %schecksum/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %scollatz-numbers/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start25, run, zip_end)
    command = "python map.py %scollatz-numbers/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %scompare-string-lengths/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start26, run, zip_end)
    command = "python map.py %scompare-string-lengths/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %scount-odds/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start27, run, zip_end)
    command = "python map.py %scount-odds/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sdigits/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start28, run, zip_end)
    command = "python map.py %sdigits/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
    outro_command = "rm data%i.csv; echo Finished Run" % (run)

    full_command = intro_command + command + outro_command

    alfcode += """    Task -title {%s - run %i} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, run, full_command, service_tag)


for run in range(0, number_runs):
    intro_command = "echo Starting run; cd %sdouble-letters/; export PYTHONHOME=/usr; export PYTHONPATH=$PYTHONPATH:/opt/sdsc/lib:/opt/sdsc/lib/python2.6/site-packages:/usr/lib64/python26.zip:/usr/lib64/python2.6/plat-linux2:/usr/lib64/python2.6/lib-tk:/usr/lib64/python2.6/lib-old:/usr/lib64/python2.6/lib-dynload:/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info:/usr/lib64/python2.6:/usr/lib64/python2.6/site-packages:/usr/lib/python2.6/site-packages; %s%i%s;" % (output_directory, zip_start29, run, zip_end)
    command = "python map.py %sdouble-letters/data%i.csv mapdata%i.csv;" % (output_directory, run, run)
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
