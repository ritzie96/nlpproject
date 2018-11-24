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
    
#model = KeyedVectors.load_word2vec_format("wiki.en.novice_text.vector.bin", binary=True) 
model = KeyedVectors.load_word2vec_format("wiki.en.expert.vector.bin", binary=True) 

#word = "fps"
#word = "badminton"

#define_words = ["hustle","social","turn","skip","music","exercise","move","choreo","express","energy","sweat","therapy","disco","hop","jump","tango","salsa","culture","theatre","ballet"]
#define_words = ["shoot","kill","respawn","aim","run","walk","videogame","action","game","jump","bunny","frag","crosshair","strafe","reload","sensitivity","quake","battlefield","health"]
#define_words = ["racquet","net","shuttlecock","serve","smash","drop","dribble","spin","rally","stroke","court","string","grip","feather","yonex","referee","li","singles","doubles","battledore"]

word = "dance"
define_words = ["salsa","breakdance","folkdance","bellydance","natyam","kathak","lavani","dabke","ballet","sweat","exercise","therapy","choreo","choreographer","count","tap","sneakers","rhythm","round","beatboxing","singing","song","pop","drumming","chorus"]


word2 = "fps"
define_words2 = ["twitch","reaction","point","military","precise","deathmatch","rifle","gun","chief","bomb","terrorist","bots","map","looking","display","quake","power","tournament","halo","unreal","strike","player","first","players","person","games","team","multiplayer","weapons","xbox","features","mode","levels","gameplay","playstation","computer","engine","movement","enemies","mission","doom","space"]

word3 = "shooter"
define_words3 = ["twitch","reaction","point","military","precise","deathmatch","rifle","gun","chief","bomb","terrorist","bots","map","looking","display","quake","power","tournament","halo","unreal","strike","player","first","players","person","games","team","multiplayer","weapons","xbox","features","mode","levels","gameplay","playstation","computer","engine","movement","enemies","mission","doom","space"]

word1 = "badminton"
define_words1 = ["ace","carry","court","doubles","dribble","drive","drop","feather","grip","net","racquet","rally","referee","serve","service","short","shot","shuttlecock","singles","smash","spin","string","stroke","yonex","let","lets","feather","feathers","saina","nehwal","hidayat"]


#for novice
# cosine = cos_sim(word,define_words,model)
# print(cosine)
# with open('new_dance_novice.txt','w') as f:
    # for k, v in cosine.items():
        # f.write(str(k) + ':'+ str(v) + '\n')
# similar_words = sim_words(define_words,model)
# print(similar_words)
# with open('new_dance_novice.txt','a') as f1:
    # for k, v in similar_words.items():
        # f1.write(str(k) + ':'+ str(v) + '\n')	


#for expert
cosine1 = cos_sim(word,define_words,model)
print(cosine1)
with open('new_dance_expert.txt','w') as f:
    for k, v in cosine1.items():
        f.write(str(k) + ':'+ str(v) + '\n')
similar_words1 = sim_words(define_words,model)
print(similar_words1)
with open('new_dance_expert.txt','a') as f1:
    for k, v in similar_words1.items():
        f1.write(str(k) + ':'+ str(v) + '\n')
        
        
        
#for novice
# cosine2 = cos_sim(word1,define_words1,model)
# print(cosine2)
# with open('new_badminton_novice.txt','w') as f:
    # for k, v in cosine2.items():
        # f.write(str(k) + ':'+ str(v) + '\n')
# similar_words2 = sim_words(define_words1,model)
# print(similar_words2)
# with open('new_badminton_novice.txt','a') as f1:
    # for k, v in similar_words2.items():
        # f1.write(str(k) + ':'+ str(v) + '\n')	


#for expert
cosine3 = cos_sim(word1,define_words1,model)
print(cosine3)
with open('new_badminton_expert.txt','w') as f:
    for k, v in cosine3.items():
        f.write(str(k) + ':'+ str(v) + '\n')
similar_words3 = sim_words(define_words1,model)
print(similar_words3)
with open('new_badminton_expert.txt','a') as f1:
    for k, v in similar_words3.items():
        f1.write(str(k) + ':'+ str(v) + '\n')
        
        
#for novice
# cosine4 = cos_sim(word2,define_words2,model)
# print(cosine4)
# with open('new_fps_novice.txt','w') as f:
    # for k, v in cosine4.items():
        # f.write(str(k) + ':'+ str(v) + '\n')
# similar_words4 = sim_words(define_words2,model)
# print(similar_words4)
# with open('new_fps_novice.txt','a') as f1:
    # for k, v in similar_words4.items():
        # f1.write(str(k) + ':'+ str(v) + '\n')	


#for expert
cosine5 = cos_sim(word2,define_words2,model)
print(cosine5)
with open('new_fps_expert.txt','w') as f:
    for k, v in cosine5.items():
        f.write(str(k) + ':'+ str(v) + '\n')
similar_words5 = sim_words(define_words2,model)
print(similar_words5)
with open('new_fps_expert.txt','a') as f1:
    for k, v in similar_words5.items():
        f1.write(str(k) + ':'+ str(v) + '\n')
        
        
#for novice
# cosine6 = cos_sim(word3,define_words3,model)
# print(cosine6)
# with open('new_shooter_novice.txt','w') as f:
    # for k, v in cosine6.items():
        # f.write(str(k) + ':'+ str(v) + '\n')
# similar_words6 = sim_words(define_words3,model)
# print(similar_words6)
# with open('new_shooter_novice.txt','a') as f1:
    # for k, v in similar_words6.items():
        # f1.write(str(k) + ':'+ str(v) + '\n')	


#for expert
cosine7 = cos_sim(word3,define_words3,model)
print(cosine7)
with open('new_shooter_expert.txt','w') as f:
    for k, v in cosine7.items():
        f.write(str(k) + ':'+ str(v) + '\n')
similar_words7 = sim_words(define_words3,model)
print(similar_words7)
with open('new_shooter_expert.txt','a') as f1:
    for k, v in similar_words7.items():
        f1.write(str(k) + ':'+ str(v) + '\n')