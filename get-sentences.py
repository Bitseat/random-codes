import os
import sys
import fileinput
import re
import linecache

j = 1
while j <= 1169:
	newFile = open ("/home/bitseat/Desktop/new-experiment/concentrate/ugh/parsed-org-sents/parsed-org-sent-for-newfile"+str(j)+".scm", 'w')
	with open('/home/bitseat/Desktop/new-experiment/concentrate/ugh/dup-removed-line-numbers2/line-numbers-for-newfile'+str(j)+'.scm') as f:
		for line in f:
			line_cont = line
			with open('/home/bitseat/Desktop/new-experiment/concentrate/ugh/tools/merged.scm') as file:
				for i, line in enumerate(file):
					if i == int(line_cont):
						newFile.write(line)
	j +=1