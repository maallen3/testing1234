import os
import argparse
import configparser
import sys

def run():
	parser = argparse.ArgumentParser(description='This is the test package')
	parser.add_argument('--display', help='prints a statement', default="no display message")
	parser.add_argument('--config', help="config file goes here", default=False)
	if len(sys.argv)==1:
		parser.print_help()
		sys.exit(1)
	arg = parser.parse_args().display
	print "Hello World!"
        os.system("echo hello worlds in bash!")
	print arg
	configfile = parser.parse_args().config
	if configfile!=False:
		config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
		config.read(configfile)
		print config
		for key in config:
			for item in config[key]:
				print key, item, config[key][item]
	to_print = config['PRINT STATEMENTS']["to_print"]
	print to_print
