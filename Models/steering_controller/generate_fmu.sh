#!/bin/bash

echo Argument must be 'source' or 'tool'

wget http://overture.au.dk/into-cps/vdm-tool-wrapper/development/latest/fmu-import-export.jar -O overture-fmu.jar

java -jar overture-fmu.jar -name steering_controller -output ../../FMUs/ -root . -export $1
