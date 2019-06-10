import os, stat

##########################################################################
# Settings
number_runs = 100
"""
clojush_directory = "/home/thelmuth/Clojush/"
output_directory = "/home/thelmuth/Results/odd/"

example_file = "clojush.problems.demos.odd"

title_string = "Test of cluster runs with odd problem"
"""


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


#command = "/share/apps/bin/lein with-profiles production trampoline run " + example_file

service_tag = "tom"

##########################################################################
output_directory = "/home/gwoolson/csvdata_count-odds"

# Check to make sure directory doesn't exist; if not, create it
if output_directory[-1] != "/":
    output_directory += "/"
if os.path.isdir(output_directory):
    raise RuntimeError("Output directory already exists")

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
    intro_command = "echo Starting run; export PYTHONHOME=usr/bin; cd /home/gwoolson/Grace_Research/;%s%i%s;" % (zip_start1, run, zip_end1)
    command = "python fly_export.py run%i.csv /home/gwoolson/Grace_Research;" % (run)
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
