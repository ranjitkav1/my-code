#!/usr/bin/python

import argparse
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import glob
import shutil
import json

def my_token_verifier():
   visitor_data = "CgtNQktNTHpfd3BJTSi88NnSBjIKCgJVUxIEGgAgTGLfAgrcAjE5LllUPWgzTVRMclNhYlBPOGxzcTVfa0ZwVHNLUFAwMnhjSE1VMHI2b2Zhb3Mwd0pvWmVPRjZXTDFnZXF0bjdsN0UtanVjbVlBeS1mTExvbWpMdGpXMXpPZDhMWVlYRmZTTHRCenphRExyc1RKcU9aOVJGal9vaGVsSHp5ZFZWY1FmeGtKeUFQZHVSNldiZWFmMThyM0c0U1VwN2VjZlRzakh5b0FsMUVObU1FdVlKNnBVTlNzSDJPdmlOemZOd3FLZmJoemhPbWgxdkUxazhRZnhSek9IbWZ5SG9SWFhNN2psY2hOU2t1WS11ZGE2R0R4c21mUllFSTNWTDBXU2tlWnk5WHR1YUI4VTJ0dWdaMlBnY04yYVBJM3B0VmtGYlA1bl95YWJZanNfN2JxdU9pV3UtamdhOTB0ZEUzSEI3TFFOMXdWNVBXaXFFUE1LNUZGVy1kVGRBUnBnZw%3D%3D",
   po_token = "MlOIreO-u_vHd4iRdu1uEfqtodru_5zCX1shVsLfagVE-urVrW1F14n3fMVDR2tbdhpWcIvXhPyz6GXBj3SkZBZZwZ3Rk95DjJd1Y4D3UuK2w0LuMw=="
   return visitor_data, po_token

def begin_conversion(filen):
   with open(filen,"r") as fd:
      lines = fd.readlines()
      for line in lines:
         print("url is:",line)
         #yt = YouTube(url, use_po_token=True)
         yt = YouTube(line, use_oauth=True, allow_oauth_cache=True,on_progress_callback=on_progress, use_po_token=True, po_token_verifier=my_token_verifier)
         # Get audio stream with highest bit rate
         audio_stream = yt.streams.filter(only_audio=True,file_extension="mp4").first()
         new_file = audio_stream.download()
         filee = glob.glob("*mp4")
         #os.rename(m4afile,filename)
         print("mp4 file is:",new_file)
         shutil.move(new_file,"output/")

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
