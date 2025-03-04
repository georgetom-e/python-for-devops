#!/bin/bash 


echo "Enter you target word: "
read word 
echo "Enter your target file: "
read file 

count=$(grep -o -w ${word} ${file} | wc -l) 

echo "${word} found in ${file} in ${count} places" 

