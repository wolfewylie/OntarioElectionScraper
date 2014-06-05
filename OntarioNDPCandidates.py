#!/usr/bin/env python

import re
import csv
import urllib
import time

topcolumns = ['Riding', 'Name', 'Image', 'Link', 'email']

MacFile = csv.writer(file('OntNDPCandidates.csv','a'),dialect='excel')
MacFile.writerow(topcolumns)

baseurl = "http://ourteam.ontariondp.ca/page/"
basehtml = urllib.urlopen(baseurl).read()
pagecount = 1

def candidatescraper(urlhtml):
	for every_candidate in re.finditer("<div class='candi-single'>(.+?)'>View Candidate", urlhtml, re.S|re.DOTALL):
		candidate = every_candidate.group(0)
		riding = re.search("class='candi-riding'>(.+?)<\/div>", candidate)
		riding = riding.group(1)
		name = re.search("class='candi-name'>(.+?)<\/div>", candidate)
		name = name.group(1)
		image = re.search("<img src='(.+?)'", candidate)
		image = image.group(1)
		link = re.search("class='candi-pic'><a href='(.+?)' title", candidate)
		link = link.group(1)
		email = re.sub(' ', '', name)
		email = email + "@ontariondp.ca"
		row_data = [riding, name, image, link, email]
		MacFile.writerow(row_data)
		print row_data

while pagecount < 7:
	newurl = baseurl + str(pagecount)
	urlhtml = urllib.urlopen(newurl).read()
	urlhtml = re.search("<div id='candidates-area'>(.+?)<div id='pagination-area'>", urlhtml, re.S|re.DOTALL)
	urlhtml = urlhtml.group(1)
	candidatescraper(urlhtml)
	pagecount = pagecount + 1



