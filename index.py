import json
import sys
import time
from elasticsearch import Elasticsearch
import pathlib

def get_dataset_filename():
   currentDirectory = pathlib.Path('dataset')
   currentPattern = "*.json"
   currentFiles = []
   for currentFile in currentDirectory.glob(currentPattern):  
      currentFiles.append(str(currentFile))
   return currentFiles