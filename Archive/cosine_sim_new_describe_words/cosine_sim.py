from gensim.models import KeyedVectors

def cos_sim(word,define_words,model_novice,model_expert):
    c_n = {}
    c_e = {}
    for i in define_words:
        c_n[i] = model_novice.wv.similarity(word, i)
        c_e[i] = model_expert.wv.similarity(word, i)
        #print(word + "(" + model.wv.similarity(word, i)+ ")"+ i)
    return c_n,c_e

model_novice = KeyedVectors.load_word2vec_format("wiki.en.novice_text.vector.bin", binary=True) 
model_expert = KeyedVectors.load_word2vec_format("wiki.en.expert.vector.bin", binary=True) 

word = "badminton"
define_words =["baddy",
"ace",
"alley",
"backcourt",
"baseline",
"carry",
"court",
"deception",
"doubles",
"dribble",
"drive",
"drop",
"fault",
"feather",
"feathers",
"flick",
"grip",
"hidayat",
"let",
"lets",
"net",
"racquet",
"rally",
"referee",
"saina",
"serve",
"service",
"short",
"shot",
"shuttlecock",
"singles",
"smash",
"spin",
"string",
"stroke",
"thomas",
"tumbling",
"uber",
"yonex"]
        
c_n, c_e = cos_sim(word,define_words,model_novice,model_expert)

with open('avg_badminton_novice.txt','w') as f:
    for k, v in c_n.items():
        f.write(str(k) + ':'+ str(v) + '\n')

with open('avg_badminton_expert.txt','w') as f1:
    for k, v in c_e.items():
        f1.write(str(k) + ':'+ str(v) + '\n')	
