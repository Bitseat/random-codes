import os
import sys
import fileinput
import re
import linecache
j=1
while j<=1169:

        fileToSearch  = "newfile"+str(j)+".scm"

        someFile = open( fileToSearch, 'r+' )
        tempFile = open ("bit1.txt", 'w')
        newFile = open ("replaceResult"+str(j)+".scm", 'w')


        pattern = r'"([A-Za-z0-9_\./\\-]*)"'
         
        tempFile.writelines([l for l in open("newfile"+str(j)+".scm").readlines()])     
        print "made bit"
        tempFile.close()

        tempFile = open ("bit1.txt", 'r+')

        def findReplacment1 (org_string):
            #find a subsetLink that has a conceptNode with org_string, go lower into its EvaluationLink and find the predicateNode
            inSubset = False
            inSatisfyingScope = False
            inEvalListLink = False
            isEqual = False
            tempFile = open ("bit1.txt", 'r+')
                
            for line in tempFile:
                 if "SubsetLink" or "IntensionalInheritanceLink" in line:
                      inSubset = True
                 if inSubset and "ConceptNode" in line:
                      val = re.search(pattern, line)  
                      if(val is not None):
                          val = str(val.group())
                          print "checking org_string and val\n"
                          print val
                          print org_string
                          if (val == org_string): 
                              isEqual = True
                          else:    
                              inSubset = False
                              continue
                 if inSubset and isEqual and "SatisfyingSetScopeLink" in line:
                            inSatisfyingScope = True            
                 if inSatisfyingScope and "ListLink" in line:
                      inEvalListLink = True
                 if "Link" in line and not "SatisfyingSetScope" in line and not "Evaluation" in line and not "List" in line and not inSubset:
                      # we have gone outside of the SubsetLink parameters
                      inSubset = False
                      inSatisfyingScope = False
                      inEvalListLink = False      
                 if inEvalListLink and "PredicateNode" in line:
                      val = re.search(pattern, line)  
                      if(val is not None):
                          print "\n"+val.group()+"\n"
                          val = str(val.group())
                          print "replacment word is"+val
                          tempFile.close()
                          return val
            tempFile.close()
            return ""                        
                   
        def findReplacment (valset, val):
            #find a subsetLink that has a conceptNode with org_string, go lower into its EvaluationLink and find the predicateNode
            inSubset = False
            inSatisfyingScope = False
            inEvalListLink = False
            isEqual = False
            tempFile = open ("bit1.txt", 'r+')
            print valset + "  and  " + val
                
            for line in tempFile:
                 if "SubsetLink" or "IntensionalInheritanceLink" in line:
                      inSubset = True
                 if inSubset and "ConceptNode" in line:
                      val = re.search(pattern, line)  
                      if(val is not None):
                          val = str(val.group())
                          print "checking org_string and val\n"
                          print val
                          print valset
                          if (val == valset): 
                              isEqual = True
                          else:    
                              inSubset = False
                              continue
                 if inSubset and isEqual and "SatisfyingSetScopeLink" in line:
                            inSatisfyingScope = True            
                 if inSatisfyingScope and "ListLink" in line:
                      inEvalListLink = True
                 if "Link" in line and not "SatisfyingSetScope" in line and not "Evaluation" in line and not "List" in line and not inSubset:
                      # we have gone outside of the SubsetLink parameters
                      inSubset = False
                      inSatisfyingScope = False
                      inEvalListLink = False      
                 if inEvalListLink and "PredicateNode" in line:
                      val = re.search(pattern, line)  
                      if(val is not None):
                          print "\n"+val.group()+"\n"
                          val = str(val.group())
                          print "replacment word is"+val
                          tempFile.close()
                          return val
            tempFile.close()
            return ""                        

        def findSetVal(val):
          inSetTypeLink = False
          inFirstConcept = False
          for line in tempFile:
            if "SetTypeLink" in line:
              inSetTypeLink = True
            if inSetTypeLink and val in line:
              inFirstConcept = True
            if inFirstConcept and "___" in line:
              print "got here"
              valset = re.search(pattern, line)
              if(valset is not None):
                print "\n"+valset.group()+"\n"
                valset = str(valset.group())
                print valset
                if(valset.endswith('___"')):
                  textToReplace = findReplacment(valset, val)
                  return textToReplace
          return ""

        inEval = False
        inPredicate = False
        inListLink = False
        inPredicate2 = False
        count = 0
        for line in someFile:
              count +=1
              if "EvaluationLink" in line : 
                  inEval= True 
                  #print "inEval!"
              if (inEval and "sumti" in line):           
                  inPredicate = True
                  #print "inEvalLink"
              if inPredicate and "ListLink" in line:  
                   #print "removing"  
                  inListLink = True
              if (inListLink and "PredicateNode" in line):
                  inPredicate2 = True
              if (inEval and "Link" in line and not "List" in line and not "Evaluation" in line):  
                   #print "removing"  
                   inEval = False
                   inPredicate = False
                   inListLink = False
                   inPredicate2 = False


              if (inPredicate2 and "ConceptNode" in line):
                  val = re.search(pattern, line)
                  if(val is not None):
                     print "\n"+val.group()+"\n"
                     val = str(val.group())
                     print val
                     if(val.endswith('___"')):
                         print val + "ends with __"
                         textToReplace = findReplacment1(val)
                         if textToReplace == "":
                             print "unreplaced at line" + str(count)
                         elif val in line and not textToReplace == "":
                            print"found val"
                            print line
                            print line.replace (val,textToReplace)
                            newFile.write(line.replace(val, textToReplace))
                            continue;
                     if "___" not in val:
                      print "___ not in val"
                      thevalinsetval = findSetVal(val)
                      if thevalinsetval == "":
                             print "unreplaced at line" + str(count)
                      elif val in line and not thevalinsetval == "":
                        print"found val"
                        print line
                        print line.replace (val,thevalinsetval)
                        newFile.write(line.replace(val, thevalinsetval))
                        continue;
              newFile.write(line)
                       
            
              
        someFile.close()          
        newFile.close()  
        os.remove('bit1.txt')
        j+=1
