#!/bin/sh
while read line
do 
	if ! [ -z  "$(echo $line | cut -d ':' -f 4 )" ]  #using '[' to test if string is zero or not
			then a=$(echo $line | cut -d ':' -f 1 )
				for c in $(echo $line |cut -d ':' -f 4 | tr "," " ")
				do
				echo $c $a
				done
				fi
				done | cut -d " " -f1 | sort | uniq -c | sort -nr