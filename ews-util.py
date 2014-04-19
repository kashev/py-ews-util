#!/usr/bin/env python 

# py-ews-util
# Kashev Dalmia
# kashev.dalmia@gmail.com

# ews-util.py

# Support both Python 2 and 3
from __future__ import print_function
from __future__ import division

# IMPORTS
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

# EWS API VARIABLES
# if the EWS API changes, these too might need to change.
ews_url      = 'https://my.engr.illinois.edu/labtrack/util_data_json.asp'
data_string  = 'data'
use_string   = 'inusecount'
total_string = 'machinecount'
lab_string   = 'strlabname'

def getJsonFromEWS(url):
    """
    given a URL to the EWS JSON API, gets the JSON object containing lab data.
    """
    resp = urlopen(ews_url)
    html = resp.read().decode('utf-8')

    json_response = json.loads(html)
    data = json_response[data_string] # specific to the EWS API
    return data

def getBarString(fraction, width=40):
    fill = ['=' if i / width < fraction else ' ' for i in range(width)]
    bar  = '[' + ''.join(fill) + ']';
    return bar

def pprintLabData(data):
    """
    Given the JSON object to lab data, pretty prints it with nice bar graph utilization.
    """
    # Print Constants
    bar_width = 40
    
    # Pretty Printing
    maxlen_lab = max([len(lab[lab_string]) for lab in data])
    maxlen_use = max([len(str(lab[use_string])) for lab in data])
    maxlen_tot = max([len(str(lab[total_string])) for lab in data])

    for lab in data:
        print ( lab[lab_string].ljust(maxlen_lab, ' '),
                ' : ',
                getBarString(lab[use_string] / lab[total_string], bar_width),
                ' ',
                str(lab[use_string]).rjust(maxlen_use, ' '),
                '/',
                str(lab[total_string]).ljust(maxlen_tot, ' '),
                sep='')

def main():
    data = getJsonFromEWS(ews_url)
    pprintLabData(data)

if __name__ == '__main__':
    main()
