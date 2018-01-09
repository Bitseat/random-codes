import os
import sys
import fileinput
import re
import linecache
import collections

j = 1
while j <= 1169:
	newFile = open ("/home/bitseat/Desktop/new-experiment/concentrate/ugh/dup-removed-line-numbers2/line-numbers-for-newfile"+str(j)+".scm", 'w')
	try:
		with open('/home/bitseat/Desktop/new-experiment/concentrate/ugh/duplicates-removed/newfile'+str(j)+'.scm') as f:
			for line in f:
				line_cont = line
				i=1
				with open('/home/bitseat/Desktop/new-experiment/concentrate/ugh/tools/replaceresult2.scm') as file:
					for line in file:
						if line == line_cont:
							newFile.write(str(i))
							newFile.write('\n')
						i+=1
	except IOError:
		print "file not found"
	j +=1

