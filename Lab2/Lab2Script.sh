#!/bin/bash

fname=0
for x in $(sort "p_list.txt")
do 
	echo "$x"
	echo "$x" > "Level$fname.txt"
	((fname++))	
done
