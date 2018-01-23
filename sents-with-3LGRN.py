import os
import sys
import fileinput
import re
import linecache

#teststring = "This is a test of number, number: 525, number: 585, number2: 559"

#fileToSearch  = "/home/bitseat/Documents/learning-python/1.scm"
newFile = open ("replaceResult.scm", 'w')

def do_replacement(count, line, val, first_next_word1, first_next_word2, second_next_word1, second_next_word2, third_next_word1, third_next_word2):
    list_of_words2 = line.split()
    print list_of_words2
    one = list_of_words2[list_of_words2.index("\""+val[0]+"\")") + 3]
    two = list_of_words2[list_of_words2.index("\""+val[0]+"\")") + 5]
    three = list_of_words2[list_of_words2.index("\""+val[1]+"\")") + 3]
    four = list_of_words2[list_of_words2.index("\""+val[1]+"\")") + 5]
    five = list_of_words2[list_of_words2.index("\""+val[2]+"\")") + 3]
    six = list_of_words2[list_of_words2.index("\""+val[2]+"\")") + 5]
    print one
    print two
    print three
    print four
    print five
    #print see
    line = line.replace(one, first_next_word1)
    line = line.replace(two, first_next_word2)
    line = line.replace(three, second_next_word1)
    line = line.replace(four, second_next_word2)
    line = line.replace(five, third_next_word1)
    line = line.replace(six, first_next_word2)
    newFile.write(line + str(count) + "\n")
    return "replaced"

def searchline(val,first_next_word1, first_next_word2, second_next_word1, second_next_word2, third_next_word1, third_next_word2):
    first = False
    second = False
    third = False
    f  = open ("/home/bitseat/Desktop/xpwd/dec1/match/big-tat/3gram/tat-replaced.scm", 'r+')
    count = 0
    for line in f:
        count +=1
        if "\""+val[0]+"\"" in line:
            first = True
            if first and "\""+val[1]+"\"" in line:
                second = True
                if second and "\""+val[2]+"\"" in line:
                    print count
                    found = do_replacement(count, line, val, first_next_word1, first_next_word2, second_next_word1, second_next_word2, third_next_word1, third_next_word2)
		continue
		return "not found"
						#newFile.write(line)
                        #newFile.write("\n")
                   

		    	
   
#three gram
fileToSearch = open ("/home/bitseat/Desktop/xpwd/dec1/match/big-tat/3gram/matching_lines.scm", 'r+')

for line in fileToSearch:
    val = re.findall(r'LinkGrammarRelationshipNode "(\w+)', line)
    
    if val:
    	print val
    	list_of_words = line.split()
    	print list_of_words
    	first_next_word1 = list_of_words[list_of_words.index("\""+val[0]+"\"") + 6]
        first_next_word2 = list_of_words[list_of_words.index("\""+val[0]+"\"") + 8]
        second_next_word1 = list_of_words[list_of_words.index("\""+val[1]+"\"") + 6]
        second_next_word2 = list_of_words[list_of_words.index("\""+val[1]+"\"") + 8]
        third_next_word1 = list_of_words[list_of_words.index("\""+val[2]+"\"") + 6]
        third_next_word2 = list_of_words[list_of_words.index("\""+val[2]+"\"") + 8]
        print first_next_word1
        print first_next_word2
        print second_next_word1
        print second_next_word2
        print third_next_word1
        print third_next_word2
    	result = searchline(val,first_next_word1, first_next_word2, second_next_word1, second_next_word2, third_next_word1, third_next_word2)
    	#if result is not "not found":
            #print result
            #newFile.write(result)




newFile.close()





