# Bitrate Plotter
a tool for graph creation using [ffmpeg_bitrate_stats](https://github.com/slhck/ffmpeg-bitrate-stats), written in Python

----------------
## Requirements

+ [ffmpeg_bitrate_stats](https://github.com/slhck/ffmpeg-bitrate-stats) and its dependencies (Python>=3.6, FFmpeg, pandas, numpy)
+ matplotlib

Both of these can be installed by running pip on Requirements.txt:
	pip3 install -r Requirements.txt

----------------
## Usage

	bitratePlotter [-h] [-s {video,audio}] [-c CHUNK_SIZE] [-g] [-o OUTPUT_FILE] file

	-s	Stream type to analyze (default: video)
	-c	Custom aggregation window size in seconds (default: 1.0)

	-g	Show gridlines on the graph(s)
	-o	Save graphs as OUTPUT_FILE, if not present graphs are displayed

	-h	Show help

	file	input file

The first two options are passed directly to ffmpeg_bitrate_stats.

---------------
## Output

Either displays or saves graphs of bitrate in kB/s over the duration of `file`, depending on the `-o` option (see [Usage](#Usage))
