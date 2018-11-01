import json
import os
import re
import sys
from os import walk
import multiprocessing
from wikiExceptions import exceptionList
import logging
import multiprocessing
from gensim.models import Word2Vec
from time import time


path = 'extracted'  

neg_titles = exceptionList
for (dirpath, dirnames,filenames) in walk(path):
	for fi in filenames:
		for line in open(os.path.join(dirpath,fi), mode="r",encoding="utf-8"):
			a = json.loads(line).get("title")
			if a in neg_titles:
				li = []
				li = json.loads(line).get("text") 
				z = re.sub(r'[™!®#\'()*+,-./:;<=>?@\&[\]^_`{|}~"’”“′‘\\\\%0123456789£'',()]'," ",li)       
				#w = [w.lower() for w in str(z).split()]                  
					    	#print w to file
				w = z
				with open("removedNoviceArticles.txt", "w") as text_file:
					print(w, file=text_file) 
					
