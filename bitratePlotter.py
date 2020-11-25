#!/usr/bin/python
import sys
import getopt
import subprocess
import json
import matplotlib.pyplot as plt

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

if len(sys.argv) < 2:
    filename = input("file name: ")
    plot(filename)
else:
    for f in sys.argv[1:]:
        plot(f)
