import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import json
import os
import re
import sys
from os import walk
import multiprocessing
from gensim.models import word2vec
from wikiExceptions import exceptionList
import logging
import multiprocessing
#from gensim.corpora import WikiCorpus
#from gensim.models import Word2Vec
#from gensim.models.word2vec import LineSentence
from time import time

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
 
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
  
    path = "E:\\extracted"    
    model = Word2Vec(json_readr(path), size=400, 
        window=5, min_count=5, workers=multiprocessing.cpu_count())
 
    model.save('wiki.en.novice_text.model')
    model.wv.save_word2vec_format('wiki.en.novice_text.vector', binary=False)
	
end = time()

print("Total procesing time: %d seconds" % (end - begin))
