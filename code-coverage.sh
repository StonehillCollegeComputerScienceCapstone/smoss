#!/usr/bin/env bash

#
#   FILE:       code-coverage.sh
#   AUTHOR:     mmiddleton
#   DATE:       19 MAR. 2018
#
#   DESCRIPTION:
#   This file is used by the build-machine to load the code coverage app provided by Code Climate to generate
#   a report that we will be able to 
#
curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > ./coverage-app
chmod +x ./coverage-app
./coverage-app before-build
echo "INFO:   code-coverage script DONE!"