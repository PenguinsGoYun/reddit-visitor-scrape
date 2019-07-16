#!/usr/bin/env python3

import collections
import os
import sys
import pprint as pp

import requests

# Globals
URL_MAIN = 'https://www.reddit.com/'
SUB = None
headers = {'user-agent': 'reddit-{}'.format(os.environ.get('USER', 'reddit-cse'))}

# Functions
def usage(status=0):
    ''' Display usage information and exit with specified status '''
    print('''Usage: {} [options] SUBREDDIT_NAME (r/all i.e.)

    -d          Duration of data collection (default: 30 minutes)
    '''.format(os.path.basename(sys.argv[0])))
    sys.exit(status)

def load_sub_data(sub=SUB):
    URL_FULL = URL_MAIN + sub + "/.json"
    print(URL_FULL)
    response = requests.get(URL_FULL, headers=headers)

    print(response)
    type(response)

    rawdata = response.json()

    print(type(rawdata))

    return rawdata

sub_data = load_sub_data("r/mildlyinteresting")

pp.pprint(sub_data)