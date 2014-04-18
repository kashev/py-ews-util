#!/usr/bin/env python 

# py-ews-util
# Kashev Dalmia
# kashev.dalmia@gmail.com

# ews-util.py

# IMPORTS
import urllib2
import json
import os

# EWS API VARIALBLES
# if the EWS API changes, these too might need to change.
ews_url      = 'https://my.engr.illinois.edu/labtrack/util_data_json.asp'
data_string  = 'data'
use_string   = 'inusecount'
total_string = 'machinecount'
lab_string   = 'strlabname'

resp = urllib2.urlopen(ews_url)
html = resp.read()

json_response = json.loads(html)
data = json_response[data_string]

# Pretty Printing
maxlen_lab = max([len(lab[lab_string]) for lab in data])
maxlen_use = max([len(str(lab[use_string])) for lab in data])
maxlen_tot = max([len(str(lab[total_string])) for lab in data])

for lab in data:
    print lab[lab_string].ljust(maxlen_lab, ' '), \
          ':', \
          str(lab[use_string]).ljust(maxlen_use, ' '), \
          '/', \
          str(lab[total_string]).ljust(maxlen_tot, ' ')

