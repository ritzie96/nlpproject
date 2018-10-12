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

#generates list of list of words.
def json_readr(path):
    neg_titles=["Dance", "History_of_dance", "List_of_dance_style_categories", "List_of_national_dances", "List_of_ethnic,_regional,_and_folk_dances_by_origin", "List_of_dance_occupations","Choreography","Outline_of_dance","Dance_move","Dance_technology","List_of_dance_companies","List_of_dancers","Group_dance","Dance_and_health","Dancing_mania"
               ,"Modern_dance","Dance_education","Dance_in_mythology_and_religion","Dance_therapy","Dance_music", "First-person_shooter", "Category:First-person_shooters", "Doom_(1993_video_game)", "Counter-Strike_(video_game)", "Wolfenstein_3D", "Call_of_Duty", "Quake_(video_game)", "Battlefield_(video_game_series)", "First-person_shooter_engine", "Multiplayer_video_game", "Action_game", "Shooter_game", "Esports", "Arrow_keys#WASD_keys", "Computer_mouse", "Computer_keyboard", "Reticle", "Level_(video_gaming)", "Weapon", "Hitscan"]
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
    
