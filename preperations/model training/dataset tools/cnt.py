import os
import sys


#this code counts all the files in a directory

"""
excpects:
cnt.py all.txt folder_photos
"""
print(len(os.listdir(sys.argv[1])))