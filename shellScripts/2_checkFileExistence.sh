#!/bin/bash 

echo "Enter file name for existence-check: "
read fileName

if [ -e $fileName ];then 

echo "file ${fileName} exists."
else
echo "file ${fileName} does not exist."
	   

fi 



