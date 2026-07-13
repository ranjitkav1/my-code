#!/usr/bin/python

import argparse
from pytubefix import YouTube
import os
import glob
import shutil

def begin_conversion(filen):
   with open(filen,"r") as fd:
      lines = fd.readlines()
      for line in lines:
         url,filename = line.split(";",2)
         print("url is:",url)
         #print("filename is:", filename)
         # input url
         yt = YouTube(url)
         # Get audio stream with highest bit rate
         audio = yt.streams.get_audio_only()
         new_file = audio.download()
         filee = glob.glob("*m4a")
         m4afile = str(filee).replace("[","").replace("]","").replace("'","")
         #os.rename(m4afile,filename)
         print("m4a file is:",m4afile)
         shutil.move(m4afile,"output/")

# main function
if __name__ == '__main__':
   parser = argparse.ArgumentParser(description="Command Line arguments")
   parser.add_argument('--f', type=str, required=True)
   args = parser.parse_args()
   if not args.f:
      print("no input file")
      exit()
   print("input file is:", args.f)
   begin_conversion(args.f)
