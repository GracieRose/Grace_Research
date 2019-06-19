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
