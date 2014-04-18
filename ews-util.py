#!/usr/bin/env python 

# py-ews-util
# Kashev Dalmia
# kashev.dalmia@gmail.com

# ews-util.py

# IMPORTS
import urllib2
import json

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
# print json.dumps(data, sort_keys=True, indent=2, separators=(',', ': '))

for lab in data:
    print lab[lab_string], ' : ', lab[use_string], '/', lab[total_string]

