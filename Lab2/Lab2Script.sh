#!/bin/bash

fname=0
for x in $(sort "p_list.txt")
do 
	echo "$x"
	echo "$x" > "PW$fname.txt"
	((fname++))	
done
