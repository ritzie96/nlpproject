from gensim.models import KeyedVectors

def sim_words(words,model_expert,model_novice):
    a = dict()
    b = dict()
    for i in words:
        a[i] = model_expert.most_similar(i,topn = 100)
        b[i] = model_novice.most_similar(i, topn = 20)
    return a,b 
    
model_novice = KeyedVectors.load_word2vec_format("wiki.en.novice_text.vector.bin", binary=True) 
model_expert = KeyedVectors.load_word2vec_format("wiki.en.expert.vector.bin", binary=True) 

words = ["badminton",
"baddy",
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

a,b = sim_words(words,model_expert,model_novice)

with open('new_100_badminton_expert.txt','w') as f:
    for k, v in a.items():
        f.write(str(k) + ':'+ str(v) + '\n')
with open('new_20_badminton_novice.txt','w') as f1:
    for k1, v1 in b.items():
        f1.write(str(k1) + ':'+ str(v1) + '\n')
    
   