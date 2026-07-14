#!/usr/bin/python

import argparse
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import glob
import shutil
import json

def begin_conversion(filen):
   with open(filen,"r") as fd:
      lines = fd.readlines()
      for line in lines:
         url,filename = line.split(";",2)
         print("url is:",url)
         yt = YouTube(url, on_progress_callback=on_progress)
         # Get audio stream
         audio_stream = yt.streams.filter(only_audio=True,file_extension="mp4").first()
         new_file = audio_stream.download()
         base, ext = os.path.splitext(new_file)
         outfile = base + 'm4a'
         shutil.move(outfile,"output/")

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
