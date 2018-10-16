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

import json
import os
import re
import sys
from os import walk
import multiprocessing
from gensim.models import word2vec
from wikiExceptions import exceptionList

#generates list of list of words.
def json_readr(path):
    neg_titles = exceptionList
    l = []
    for (dirpath, dirnames,filenames) in walk(path):
        for fi in filenames:
            for line in open(os.path.join(dirpath,fi), mode="r",encoding="utf-8"):
                li = []
                a = json.loads(line).get("title")
                if a not in neg_titles:
                    li = []
                    li = json.loads(line).get("text") 
                    z = re.sub(r'[™!®#\'()*+,-./:;<=>?@\&[\]^_`{|}~"’”“′‘\\\\%0123456789£'',\n()]'," ",li)       
                    w = [w.lower() for w in str(z).split()]    
                    l.append(w)              
    yield l 

#train word2vec
if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
 
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
  
    path = "E:\extracted"    
    model = Word2Vec(json_readr(path), size=400, 
        window=5, min_count=5, workers=multiprocessing.cpu_count())
    # trim unneeded model memory = use (much) less RAM
    model.init_sims(replace=True)
    model.save("novice_word_vec_wiki.model")

# with open('sent_to_train.txt', 'w') as f:
    # for item in lis:
        # f.write("%s\n" % item)
    
