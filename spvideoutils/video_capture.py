"""
Captures the video from the camera to a file.
"""

import argparse
import sys


def create_parser():
	"""Create command line parser for arguments."""
	parser = argparse.ArgumentParser(description="Capture video from camera to mp4 file.")
	parser.add_argument('--index', '-i', default=0, type=int, help="Camera index on this mc.")
	parser.add_argument('--time', '-t', default=4, type=int, help='Seconds to capture the video')
	parser.add_argument('outfile', type=str, help="Output mp4 file to store the video.")
	return parser 

def parse_args(parser, args):
	"""Parse all the arguments."""
	opt = parser.parse_args(args)

	if len(args) == 1:
		parser.print_help(sys.stderr)
		sys.exit(-1)
		
	return opt

def main():
	""" Main program. """
	opt = parse_args(create_parser(), sys.argv)

if __name__ == "__main__":
	main()