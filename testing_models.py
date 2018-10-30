from gensim.models import KeyedVectors

def cos_sim(word,define_words,model):
    c = {}
    for i in define_words:
        c[i] = model.wv.similarity(word, i)
        #print(word + "(" + model.wv.similarity(word, i)+ ")"+ i)
    return c

def sim_words(define_words,model):
    a = {}
    for i in define_words:
        a[i] = model.most_similar(i)
    print(a)
    return a 
    
def unique_count(similar_words):
    b = {}
    for key, value in similar_words.items():
        for i in value:            
            if i in b:  
                b[i] += 1  
            else:  
                b[i] = 1 
    return b
    
model = KeyedVectors.load_word2vec_format("wiki.en.novice_text.vector.bin", binary=True) 
#model = KeyedVectors.load_word2vec_format("wiki.en.bin.vector", binary=True) 
#word = "dance"
#word = "fps"
word = "badminton"
#define_words = ["hustle","social","turn","skip","music","exercise","move","choreo","express","energy","sweat","therapy","disco","hop","jump","tango","salsa","culture","theatre","ballet"]
#define_words = ["shoot","kill","respawn","aim","run","walk","videogame","action","game","jump","bunny","frag","crosshair","strafe","reload","sensitivity","quake","battlefield","health"]
define_words = ["racquet","net","shuttlecock","serve","smash","drop","dribble","spin","rally","stroke","court","string","grip","feather","yonex","referee","li","singles","doubles","battledore"]
cosine = cos_sim(word,define_words,model)
print(cosine)
with open('badminton_novice.txt','w') as f:
    for k, v in cosine.items():
        f.write(str(k) + ':'+ str(v) + '\n')
similar_words = sim_words(define_words,model)
print(similar_words)
with open('badminton_novice.txt','a') as f1:
    for k, v in similar_words.items():
        f1.write(str(k) + ':'+ str(v) + '\n')	
#overlappers = unique_count(similar_words)
#print(overlappers)