#!/usr/bin/env python

import re
import csv
import urllib
import time

topcolumns = ['Riding', 'Name', 'Image', 'Link', 'email']

MacFile = csv.writer(file('OntPCCandidates.csv','a'),dialect='excel')
MacFile.writerow(topcolumns)

baseurl = "http://www.ontariopc.com/team"
basehtml = urllib.urlopen(baseurl).read()

for every_candidate in re.finditer('<div class="w-col w-col-4 candidate-list-col">(.+?)<\/a>', basehtml, re.S|re.DOTALL):
	candidate = every_candidate.group(0)
	riding = re.search('<a class="candidate-list-link" href="(.+?)" target="_blank">(.+?)<\/a', candidate)
	riding = riding.group(2)
	name = re.search('<div class="candidate-list-name">(.+?)<\/div>', candidate)
	name = name.group(1)
	image = re.search('<img class="candidate-list-photo" src="(.+)">', candidate)
	image = image.group(1)
	link = re.search('<a class="candidate-list-link" href="(.+?)" target="_blank">(.+?)<\/a', candidate)
	link = link.group(1)
	email = "none available"
	row_data = [riding, name, image, link, email]
	MacFile.writerow(row_data)
	print row_data




