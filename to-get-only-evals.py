import os
import sys
import fileinput
import re
import linecache
j=1
while j<=1169:
  fileToSearch  = "/home/bitseat/Desktop/new-experiment/concentrate/ugh/test/preprocessed/replaceResult"+str(j)+".scm"
  someFile = open( fileToSearch, 'r+' )
  newfile = open ("/home/bitseat/Desktop/new-experiment/concentrate/ugh/test/preprocessed/only-eval/replaceResulteval"+str(j)+".scm", 'w')
  inEval= False
  inPredicate = False
  inListLink = False
  inPredicate2 = False
  for line in someFile:
    if line.startswith('"'):
      newfile.write(";"+line)
    #count +=1
    if "EvaluationLink" in line:
      inEval= True
      first = line
    if (inEval and "sumti" in line):
      inPredicate = True
      second = line
    if inPredicate and "ListLink" in line:
      #print "removing"
      inListLink = True
      third = line
    if (inListLink and "PredicateNode" in line and not "ConceptNode" in line) and "SimpleTV" not in line:
      inPredicate2 = True
      fourth = line
    if (inEval and "Link" in line and not "List" in line and not "Evaluation" in line):  
      #print "removing"  
      inEval = False
      inPredicate = False
      inListLink = False
      inPredicate2 = False
    if (inPredicate2 and "ConceptNode" in line) and "SimpleTV" not in line:
      fifth = line
      newfile.write(first)
      #newfile.write('\n')
      newfile.write(second)
      #newfile.write('\n')
      newfile.write(third)
      #newfile.write('\n')
      newfile.write(fourth)
      #newfile.write('\n')
      newfile.write(fifth)
      #newfile.write('\n')
      newfile.write('              )')
      newfile.write('\n')
      newfile.write('            )')
      newfile.write('\n')
      newfile.write('\n')
  j+=1