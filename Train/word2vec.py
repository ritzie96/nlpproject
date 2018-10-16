import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import logging
import multiprocessing
import os
import re
import sys

from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from time import time

begin = time()
if __name__ == '__main__':
    
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    fdir = 'C:\\Users\\Suhas\\Gensim Trainer\\'
    inp = fdir + 'wiki.en.text.txt'
    outp1 = fdir + 'wiki.en.text.model'
    outp2 = fdir + 'wiki.en.text.vector'
	
    model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5,
                     workers=multiprocessing.cpu_count())
					 
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)
	
end = time()

print("Total procesing time: %d seconds" % (end - begin))

#python word2vec.py wiki.en.text.txt wiki.en.text.model wiki.en.text.vector