#!/bin/bash

function main
{
	# Array of assignment names and empty URL array
	assignments=( "magicsquare" "palindrome" "twentyone")
	
	# cd to data directory
	cd newData
	
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


	echo "Retrieving url for test_processTableStrings1"
	test1=$(perl ../moss.pl -l java abhatia_magicsquare.java)
	url=$(echo $test1 | grep -o 'http:\/\/moss\.stanford\.edu\/results\/[0-9][0-9]*')
	echo "$url"
	#echo "\n"
	testurls+=($url)

	echo "Retrieving url for test_processTableStrings2"
	test2=$(perl ../moss.pl -l java abhatia_magicsquare.java abhatia_magicsquare.java )
	url=$(echo $test2 | grep -o 'http:\/\/moss\.stanford\.edu\/results\/[0-9][0-9]*')
	echo "$url"
	#echo "\n"
	testurls+=($url)

	echo "Retrieving url for test_processTableStrings3"
	test3=$(perl ../moss.pl -l java dtargaryen_twentyone.java jdalbey_twentyone.java ssnape_twentyone.java)
	url=$(echo $test3 | grep -o 'http:\/\/moss\.stanford\.edu\/results\/[0-9][0-9]*')
	echo "$url"
	testurls+=($url)

    #echo "Retrieving url for test_processTableStrings3"
    #test3=$(perl ../moss.pl -l java jbaxter5_Warmup.java jbaxter5_Warmup.java)
    #url=$(echo $test3 | grep -o 'http:\/\/moss\.stanford\.edu\/results\/[0-9][0-9]*')
    #echo $url
    #echo "\n"
    #testurls+=($url)

    #echo "Retrieving url for test_processTableStrings4"
    #test4=$(perl ../moss.pl -l java jbaxter5_Warmup.java stentacles_Warmup.java jbaxter5_Insipid.java stentacles_Insipid.java )
    #url=$(echo $test4 | grep -o 'http:\/\/moss\.stanford\.edu\/results\/[0-9][0-9]*')
    #echo $url
    #echo "\n"
    #testurls+=($url)

    #echo "Retrieving url for test_processTableStrings5"
    #test5=$(perl ../moss.pl -l java jbaxter5_Warmup.java jbaxter5_Warmup.java)
    #url=$(echo $test5 | grep -o 'http:\/\/moss\.stanford\.edu\/results\/[0-9][0-9]*')
    #echo $url
    #echo "\n"
    #testurls+=($url)


	#cd back to smoss directory
	cd ..
	
	# Write all URLs to mossUrls.txt
	for url in "${urls[@]}"
	do
		echo "$url"
	done > mossUrls.txt

	# Write test urls to testurls.txt
	for url in "${testurls[@]}"
	do
	    echo "$url"
	done > testurls.txt
	
	# Copy mossUrls.txt to the test directory
	cp mossUrls.txt test/mossUrls.txt
    rm mossUrls.txt
	#Move testurls to test directory
	cp testurls.txt test/testurls.txt
	rm testUrls.txt
}

main
