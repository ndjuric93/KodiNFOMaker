#!/bin/bash/python

import os
import sys

# Ovu skriptu koristiti pokretati iskljucivo sa dva parametra
# Prvi parametar predstavlja tip video fajlova (movie, tvshow itd.)
# Drugi parametar predstavlja apsolutnu putanju do direktorijuma gde se nalaze video fajlovi
# Treci parametar je obavezan ukoliko se koristi tvshow tag, predstavlja ime serije.

tags = ['movie', 'tvshow','musicvideo']

if sys.argv[1] == tags[1] and len(sys.argv) != 4:
	print 'Ukoliko se koristi TV Show potreban je treci argument koji predstavlja ime serije!'
	exit()

if sys.argv[1] not in tags:
	print 'Netacan tag, ili nije dozvoljen, ukoliko tag ne postoji, dodati u tags listu!'
	exit()

if not os.path.isdir(sys.argv[2]) : 
	print 'Drugi argument skripte mora biti direktorijum koji postoji!'
	exit()

if sys.argv[1] != tags[1]:
	for file in os.listdir(sys.argv[2]):
		file_name = file.split('.')[0]
		f = open(os.path.join(sys.argv[2], file_name + '.nfo'), "w")
		f.write('<?xml version="1.0" encoding="utf-8"?>' + '\n' + 
				'<'+ sys.argv[1] + '>' + '\n' +
				'<title>' + sys.argv[3] + '</title>' + '\n' + 
				'</' + sys.argv[1] + '>')
else:
	for file in os.listdir(sys.argv[2]):
		print file
		file_name = file.split('.')[0]
		f = open(os.path.join(sys.argv[2], file_name + '.nfo'), "w")
		f.write('<?xml version="1.0" encoding="utf-8"?>' + '\n' + 
				'<episodedetails>' + '\n' +
				'<title>' + file_name + '</title>' + '\n' + 
				'</episodedetails>')
		f = open(os.path.join(sys.argv[2], 'tvshow.nfo'), "w")
		f.write('<?xml version="1.0" encoding="utf-8"?>' + '\n' + 
				'<tvshow>' + '\n' +
				'<title>' + sys.argv[3] + '</title>' + '\n' + 
				'</tvshow>')



print 'NFO Fajlovi generisani!'
