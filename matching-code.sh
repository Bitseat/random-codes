#!/bin/bash
ans="matching_lines"

for file1 in *
do 
    for file2 in *
        do 
            if  [ "$file1" != "$ans" ] && [ "$file2" != "$ans" ] && [ "$file1" != "$file2" ] ; then
                echo "Comparing: $file1 $file2 ..." >> $ans
                perl -ne 'print if ($seen{$_} .= @ARGV) =~ /10$/' $file1 $file2 >> $ans
            fi
         done 
done
