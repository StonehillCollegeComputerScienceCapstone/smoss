#!/bin/bash

function main
{
	# Array of assignment names and empty URL array
	assignments=( "Warmup" "TwentyOne" "SquareRoot" "Insipid" "Rodentia" )
	
	# cd to data directory
	cd data
	
	# For each assignment in the array, run MOSS and store the results
	for assignment in "${assignments[@]}"
	do
		echo "Retrieving $assignment..."
		mossResults=$(perl ../moss.pl -l java *"$assignment".java)
		url=$(echo $mossResults | grep -o 'http:\/\/moss\.stanford\.edu\/results\/[0-9][0-9]*') # Search the results for the regular expression
		echo "$url"
		urls+=($url)
	done


	#URLs for testing
	#echo "Retrieving url for test_processTableStrings1"
	#test1 = $(perl ../moss.pl -l java jbaxter5_Warmup.java)
	#echo "$test1"
	#urls += test1
	#echo "Retrieving url for test_processTableStrings2"
	#test2 = $(perl ../moss.pl -l java jbaxter5_Warmup.java jbaxter5_Insipid.java stentacles_Warmup.java stentacles_Insipid.java)
	#urls += test2
	#cd back to smoss directory


	cd ..
	
	# Write all URLs to mossUrls.txt
	for url in "${urls[@]}"
	do 
		echo -e "$url"
	done > mossUrls.txt
	
	# Copy mossUrls.txt to the test directory
	cp mossUrls.txt test/mossUrls.txt
}

main
