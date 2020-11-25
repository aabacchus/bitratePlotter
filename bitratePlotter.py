#!/usr/bin/python
import sys
import getopt
import subprocess
import json
import matplotlib.pyplot as plt

## get command-line arguments
args = sys.argv[1:]
## list of available options
opts = "c:g:o:"

## from the arguments, find any recognised options
optionValuePairs, otherArgs = getopt.getopt(args, opts)

def plot(filename):
    stdout,stderr = subprocess.Popen(["ffmpeg_bitrate_stats",filename],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
    d=json.loads(stdout)["bitrate_per_chunk"]
    #with open(filename) as f:
    #    d= json.load(f)["bitrate_per_chunk"]

    x = []
    for i in range(len(d)):
        x.append(i/60)

    plt.figure()
    plt.plot(x,d)
    plt.xlabel("time (min)")
    plt.ylabel("bitrate (kB/s)")
    plt.title(filename)
    plt.grid()
    plt.show()

if len(otherArgs) < 1:
    ## if no filename specified (as the final argument, with no option), ask for the input file
    filename = input("file name: ")
    plot(filename)
else:
    ## otherwise analyse the files given
    for f in otherArgs:
        plot(f)
