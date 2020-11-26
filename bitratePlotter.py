#!/usr/bin/python
import sys
import getopt
import subprocess
import json
import matplotlib.pyplot as plt

## get command-line arguments
args = sys.argv[1:]
## list of available options
opts = "hc:s:go:"
## from the arguments, find any recognised options
optionValuePairs, otherArgs = getopt.getopt(args, opts, ["help"])
## list of options to be passed to ffmpeg_bitrate_stats
fbsArgs = []

showGrid = False
saveImg = False
outFile = ""

def plot(filename,fbsArgs,ax):
    command = ["ffmpeg_bitrate_stats",filename]
    command.extend(fbsArgs) ## add arguments onto command
    ## Execute the actual command doing the work
    stdout,stderr = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
    d=json.loads(stdout)["bitrate_per_chunk"]

    x = []
    for i in range(len(d)):
        x.append(i/60) # x is the x axis, in minutes here. TODO: x is variable depending on timescale of input

    ax.plot(x, d)
    ax.set_xlabel("time (min)")
    ax.set_ylabel("bitrate (kB/s)")
    ax.set_title(filename)
    if showGrid:
        ax.grid()


def help():
    print("Help: see README.md#Usage")
    print("usage: bitratePlotter [-h] [-s {video,audio}] [-c CHUNK_SIZE] [-g] [-o OUTPUT_FILE] file\n\t\noptional arguments:\n\t-s\tStream type to analyze (default: video)\n\t-c\tCustom aggregation window size in seconds (default: 1.0)\n\t\n\t-g\tShow gridlines on the graph(s)\n\t-o\tSave graphs as OUTPUT_FILE, if not present graphs are displayed\n\t\n\t-h\tShow this help\n\t\npositional arguments:\n\tfile\tinput file(s)")

for o,v in optionValuePairs:
    if o in ("-h", "--help"):
        help()
        sys.exit()
    elif o in ("-c","-s"):
        fbsArgs.extend([o,v])
    elif o == "-g":
        showGrid = True
    elif o == "-o":
        saveImg = True
        outFile = v

print("FBS args: ",fbsArgs)

if len(otherArgs) < 1:
    ## if no filename specified (as the final argument, with no option), ask for the input file
    filename = input("file name: ")
    fig, ax = plt.subplots(1,1)
    plot(filename,fbsArgs,ax)
elif len(otherArgs) == 1:
    fig, ax = plt.subplots(1,1)
    plot(otherArgs[0],fbsArgs,ax)
else:
    ## otherwise, analyse the multiple files given
    fig, ax = plt.subplots(len(otherArgs),1)
    plt.tight_layout()
    for f in range(len(otherArgs)):
        plot(otherArgs[f],fbsArgs,ax[f])

## make the subplots sit together more nicely so you can see all the writing
plt.subplots_adjust(left = 0.125, right = 0.9, bottom = 0.1, top = 0.9, wspace = 0.2, hspace = 0.5)
if saveImg:
    plt.savefig(outFile)
else:
    plt.show()
