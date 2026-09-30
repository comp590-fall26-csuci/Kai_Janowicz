#!/bin/bash
sout=$(./../Lab3/main)


if [[ "$sout" == *"55"* && "$sout" == *"1.618034"* ]]; then 
	echo string found
else 
	echo missing string 
	exit 1
fi
