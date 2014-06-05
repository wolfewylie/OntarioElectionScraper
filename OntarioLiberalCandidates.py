#!/usr/bin/env python

import re
import csv
import urllib
import time

topcolumns = ['Riding', 'Name', 'Image', 'Link', 'email']

MacFile = csv.writer(file('OntLibCandidates.csv','a'),dialect='excel')
MacFile.writerow(topcolumns)

baseurl = "http://www.ontarioliberal.ca/ourteam/whoweare/candidates.aspx"
basehtml = urllib.urlopen(baseurl).read()

for every_candidate in re.finditer('<img src="http:\/\/pantone201.ca(.+?)<\/div', basehtml, re.S|re.DOTALL):
	candidate = every_candidate.group(0)
	riding = re.search('<h4(.+?)>(.+?)<\/h4>', candidate)
	riding = riding.group(2)
	name = re.search('<h3(.+?)>(.+?)<\/h3>', candidate)
	name = name.group(2)
	image = re.search('<img src="(.+?)"', candidate)
	image = image.group(1)
	link = re.search('<p><a href="(.+)"', candidate)
	link = link.group(1)
	link = re.sub('" target="_blank', '', link)
	email = re.sub('http:\/\/', '', link)
	email = "info@" + email
	row_data = [riding, name, image, link, email]
	MacFile.writerow(row_data)
	print row_data




