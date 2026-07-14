#!/bin/bash

sudo apt update
sudo apt install python3 python3-pip dos2unix
sudo pip3 install argparse 
sudo pip3 install -U pytubefix
sudo apt update
sudo chmod -R 777 /usr/local/lib/python3.12/dist-packages/pytubefix/
