import os
import nltk
import json
import gensim


def getSentences(directory):
		data = []
		ll = ""
		print("hello")
		for subdir, dirs, files in os.walk(self.filename):
			for fil in files:
				print(os.path.join(subdir,fil))
				f = open(os.path.join(subdir,fil),'r')
				for line in f:
					data = json.loads(line)
					print(data)
					ll = ll + [i for i in unicode(data, 'utf-8').lower().split()]
			
			print (ll)
		yield ll


#get = getSentences("extracted")
#get.next()


#input- single json file and titles not required
#output - list of list of documents excluding not required titles

import json
from os import walk
#for a single file
def json_readr(file):
    neg_titles=["Chromosome", "Charles Martel", "Celestines"]
    l = []    
    for line in open(file, mode="r",encoding="utf-8"):
        li = []
        a = json.loads(line).get("title")
        if a not in neg_titles:
            li = json.loads(line).get("text")        
            l.append(li)
    return l 

#for all files    
path = "E:\extracted"
lis = []
for (dirpath, dirnames,filenames) in walk(path):
    for fi in filenames: 
        lst = json_readr(os.path.join(dirpath,fi))
        lis.extend(lst)

#write the extracted sentences to file        
with open('sent_to_train.txt', 'w') as f:
    for item in lis:
        f.write("%s\n" % item)