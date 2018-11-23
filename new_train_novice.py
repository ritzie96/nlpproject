import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import json
import os
import re
import sys
from os import walk
import multiprocessing
from newWikiExceptions import exceptionList
import logging
import multiprocessing
from gensim.models import Word2Vec
from time import time
from gensim.test.utils import common_corpus, common_texts, get_tmpfile
from gensim.models.callbacks import CallbackAny2Vec


class EpochSaver(CallbackAny2Vec):

    def __init__(self, path_prefix):
        self.path_prefix = path_prefix
        self.epoch = 0

    def on_epoch_end(self, model):
        output_path = get_tmpfile('{}_epoch{}.model'.format(self.path_prefix, self.epoch))
        model.save(output_path)
        #model.wv.save_word2vec_format('wiki.en.very_novice_text.vector', binary=False)
        model.wv.save_word2vec_format(output_path+'.bin', binary=True)
        self.epoch += 1

#generates list of list of words.
class MySentences(object):
    def __init__(self, path):
        self.path = path
 
    def __iter__(self):
        neg_titles = exceptionList
        for (dirpath, dirnames,filenames) in walk(self.path):
            for fi in filenames:
                for line in open(os.path.join(dirpath,fi), mode="r",encoding="utf-8"):
                    a = json.loads(line).get("title")
                    if a not in neg_titles:
                        li = []
                        li = json.loads(line).get("text") 
                        z = re.sub(r'[™!®#\'()*+,-./:;<=>?@\&[\]^_`{|}~"’”“′‘\\\\%0123456789£'',\n()]'," ",li)       
                        w = [w.lower() for w in str(z).split()]                  
                        yield w 
                    else:
                        with open('used_exception_list.txt','a') as f:
                            f.write('"'+str(a)+'"'+',\n')
                        
#train word2vec
begin = time()
if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
 
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    saver = EpochSaver("very_novice_w2v")
    sentences = MySentences('extracted')       
    model = Word2Vec(sentences, size=400, window=5, min_count=5, workers=multiprocessing.cpu_count(), callbacks=[saver])
	
end = time()
print("Total procesing time: %d seconds" % (end - begin))
