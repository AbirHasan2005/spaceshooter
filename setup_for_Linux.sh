#!/bin/bash

printf "\n\e[1;92mRunning Setup for Linux ...\n\n"
sleep 2
sudo apt install python3
pip3 install -r requirements.txt
printf "\n\n\e[1;92mLinux Setup Done ...\n"
