import os
import sys
import fileinput
import re
import linecache
import collections



def positions(varArray):
	unique_entries = set(varArray)
	#i = 1
	indices = { value : [ i for i, v in enumerate(varArray) if v == value ] for value in unique_entries }
	#print indices
	firstarr = []
	secondarr = []
	for x in indices:
		bit = indices[x]
		firstarr.append(bit)
	#print firstarr
	return firstarr

def secpositions(secvarArray):
	secunique_entries = set(secvarArray)
	#i = 1
	secindices = { value : [ i for i, v in enumerate(secvarArray) if v == value ] for value in secunique_entries }
	#print secindices
	secfirstarr = []
	secsecondarr = []
	for x in secindices:
		secbit = secindices[x]
		secfirstarr.append(secbit)
	#print secfirstarr
	return secfirstarr




j = 716
while j == 716:
	i = 0
	countsec = 0
	countfirst = 0
	newFile = open ("/home/bitseat/Desktop/new-experiment/concentrate/ugh/matched/replaceresult"+str(j), 'w')
	firstFile = open ("/home/bitseat/Desktop/new-experiment/concentrate/ugh/the-sentences/file"+str(j)+".scm", 'r')
	l = firstFile.readlines()
	secondFile = open ("/home/bitseat/Desktop/new-experiment/concentrate/ugh/original-sents/unreplacedResult"+str(j)+".scm", 'r+')
	for line in secondFile:
		countsec +=1
		print "file two line  " + str(countsec)
		val = re.findall(r'LinkGrammarRelationshipNode "(\w+)', line)
		#length = len(val) * 
		#print length
		print val
		varArray = ['"$var_1")']
		myArray = ['no']
		#print varArray
		#varArray += []
		list_of_words = line.split()
		if not val:
			continue
		else:
			for val[i] in val:
				myArray[i] = list_of_words[list_of_words.index("\""+val[i]+"\")") + 3]
				varArray.append(myArray[i])
				#print varArray
				myArray[i] = list_of_words[list_of_words.index("\""+val[i]+"\")") + 5]
				varArray.append(myArray[i])
				#print varArray
			varArray.pop(0)
			#print varArray
			the_dictionary = positions(varArray)
			#print the_dictionary
			if not the_dictionary:
				continue
			else:
				for line1 in l:
					print "am here"
					countfirst += 1
					secval = re.findall(r'LinkGrammarRelationshipNode "(\w+)', line1)
					print secval
					secvarArray = ['"$var_1")']
					secmyArray = ['no']
					list_of_words = line1.split()
					if not secval:
						continue
					else:
						for secval[i] in secval:
							try:
								secmyArray[i] = list_of_words[list_of_words.index("\""+secval[i]+"\")") + 3]
								secvarArray.append(secmyArray[i])
								#print varArray
								secmyArray[i] = list_of_words[list_of_words.index("\""+secval[i]+"\")") + 5]
								secvarArray.append(secmyArray[i])
								#print varArray
							except IndexError:
								continue
						secvarArray.pop(0)
						sec_dictionary = secpositions(secvarArray)
						if sorted(the_dictionary) == sorted(sec_dictionary):
							newFile.write(line)
							del secval[:]
							#print line
							del varArray[:]
							del myArray[:]
							print "file one line  "+ str(countfirst)
							print "found\n"
						else:
							del secvarArray[:]
							del secmyArray[:]
							del varArray[:]
							del myArray[:]
	j +=1
						


	
