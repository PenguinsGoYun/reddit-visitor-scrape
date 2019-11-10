#!/usr/bin/env python3

import os
import sys

import requests
import re

import time

# accounts active
# currently viewing count

# Globals
URL = "https://www.reddit.com/"
SUBREDDIT = "r/showerthoughts"

headers = {'user-agent': 'reddit-{}'.format(os.environ.get('USER'))}

# Functions
def usage(status=0):
    ''' Display usage information and exit with specified status '''
    print('''Usage: {} [options] SUBREDDIT

    -s          Shorten URLs using the is.gd web service (default: False)
    '''.format(os.path.basename(sys.argv[0])))
    sys.exit(status)



if __name__ == "__main__":
    response = requests.get(URL+SUBREDDIT, headers=headers)
    
    # Grab current time for logging
    local_time = time.asctime(time.localtime(time.time()))

    # Use RegEx to scrape online visitor count from HTML of specified subreddit
    currently_viewing = re.search(r'(?<=\"currentlyViewingCount\":)\d+', response.text)
    currently_viewing = int(currently_viewing.group(0))

    # Store information in external file based on 
    f = open(SUBREDDIT[2:] + ".txt", "a")
    f.write(local_time + "\n")
    f.write(str(currently_viewing) + "\n")
    f.close()
