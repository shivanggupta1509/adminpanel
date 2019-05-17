#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from Classes import MainClass
from colorama import Fore, Back, Style
import sys

okadminfinder = MainClass.okadminfinder()
okadminfinder.getCredits()

parser = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=30, width=90))
parser.add_argument("-u", "--url", default=False,
					help="Target URL (e.g. 'www.example.com' or 'example.com')")
parser.add_argument("-t", "--tor", action='store_true', default=False,
					help="Use Tor anonymity network")
parser.add_argument("-p", "--proxy", default=False,
					help="Use an HTTP proxy (e.g '127.0.0.1:8080')")
parser.add_argument("-rp", "--random-proxy", action="store_true", default=False,
					dest="random_proxy", help="Use randomly selected proxy server")
parser.add_argument("-r", "--random-agent", action='store_true', default=False,
					dest='rand', help="Use randomly selected User-Agent")
parser.add_argument("-f", "--fast", action='store_true', default=False,
					dest='fast', help="Fast work")
parser.add_argument("-v", "--verbose", action='store_true', default=False,
					help="Display more informations")
parser.add_argument("-U", "--update", action='store_true', default=False,
					help="Update OKadminFinder")
parser.add_argument("-i", "--interactive", action='store_true', default=False,
					help="Interactive interface" + Fore.RED+Style.BRIGHT + " [other arguments not required]")
if len(sys.argv) <= 1:
	parser.print_usage()
	sys.exit(1)
else:
	args = parser.parse_args()

# site = 'panjiachen.github.io'
# okadminfinder.url(site)
proxies = ""


if __name__ == '__main__':
	# Updater

	# interactive

	# random user-agent

	# random proxy

	# tor

	# proxy
	if args.proxy:
		if args.url is False:
			parser.print_usage()
			quit(0)
		else:
			prox=str(args.proxy)
			okadminfinder.proxy(prox)
			proxies = okadminfinder.proxy(prox)

	# verbose

	# fast
	if args.fast:
		if args.fast is False:
			fast = ""
		else:
			fast = args.fast

	# url
	if args.url:
		site = args.url
		if args.fast is False:
			fast = False
		else:
			fast = args.fast
		# proxies=""
		okadminfinder.url(site, proxies, fast)
