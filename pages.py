import sys
import subprocess
import re

# Calls the R system specifying that commands come from file commands.R
# The commands.R provided with this assignment will read the file named
# data and will output a histogram of that data to the file pageshist.pdf
def runR( ):
    res = subprocess.call(['R', '-f', 'commands.R'])

# log2hist analyzes a log file to calculate the total number of pages
# printed by each user during the period represented by this log file,
# and uses R to produce a pdf file pageshist.pdf showing a histogram
# of these totals.  logfilename is a string which is the name of the
# log file to analyze.
def log2hist(logfilename):
    inFile = open(logfilename, 'r')
    outFile = open("data", 'w')
    users = {}

    for line in inFile:
    	data = re.search(r'(user:[\s]+)([\w]+)(.*)(pages:[\s]+)([\d]+)',line)
    	if data:
    		if not data.group(2) in users:
    			users[data.group(2)] = int(data.group(5))
    		else:
    			users[data.group(2)] += int(data.group(5))

    for user in users:
    	outFile.write(str(users[user]) + '\n')

    inFile.close()
    outFile.close()
    runR()

if __name__ == '__main__':
    log2hist(sys.argv[1])  # edit this line to change log file name.
