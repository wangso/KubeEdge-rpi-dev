#!/bin/bash

# This script acquires token for connecting edge core to Cloud core node and should be run on the Cloud core
# Developed by Songjie Wang at the University of Missouri
# March 03, 2021

# This script requires two arguments - public IP of the Cloud core, and the token obtained from Cloud cloud core earlier
# $1: IP of Cloud node
# $2: Token 

#check to make sure argument edgeNode IP provided
if [ "$#" -lt 2 ]
then
    echo -e "\n${RED}Not enough arguments supplied, please provide the public IP of the Cloud node, and the token for joining the cluster. Exiting...${NC}"
    exit
fi

#Color declarations
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
LIGHTBLUE='\033[1;34m'
LIGHTGREEN='\033[1;32m'
NC='\033[0m' # No Color

function checkErr() {
    echo -e "${RED}$1 failed. Exiting.${NC}" >&2; exit;
}

#Check to see if the script is run as root/sudo. If not, warn the user and exit.
if [[ $EUID -ne 0 ]] ; then
    echo -e "${RED}This script needs to be run as root. Please run this script again as root. Exiting.${NC}"
    exit
fi


# start Keadm and connect to Cloud core node
keadm join --cloudcore-ipport="$1":10000 --token="$2" --edgenode-name=test1 --kubeedge-version=1.6.0 || checkErr "Joining edge core to cluster"