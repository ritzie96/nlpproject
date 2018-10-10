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
import os
import re
from os import walk
#for a single file
def json_readr(file):
    neg_titles=["Chromosome", "Charles Martel", "Celestines"]
    l = []    
    for line in open(file, mode="r",encoding="utf-8"):
        li = []
        a = json.loads(line).get("title")
        if a not in neg_titles:
            li = []
            li = json.loads(line).get("text") 
            # lit = re.sub('\][-*&^%$#@!?><,.',' ',li)
            # lite = [w.lower() for w in lit.spilt()]
            z = re.sub(r'[™!®#\'()*+,-./:;<=>?@\&[\]^_`{|}~"’”“′‘\\\\%0123456789£'',\n()]'," ",li)       
            w = [w.lower() for w in str(z).split()]    
            l.append(w)              
    yield l 

#for all files    
path = "E:\extracted"
lis = []
for (dirpath, dirnames,filenames) in walk(path):
    for fi in filenames: 
        lst = json_readr(os.path.join(dirpath,fi))
        print(lst)
        lis.extend(lst)
    
with open('sent_to_train.txt', 'w') as f:
    for item in lis:
        f.write("%s\n" % item)