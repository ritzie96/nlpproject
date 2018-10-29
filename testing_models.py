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
            if b.has_key(i):  
                b[i] += 1  
            else:  
                b[i] = 1 
    return b
    
model = KeyedVectors.load_word2vec_format("E:/projectnlp/models_bin/wiki.en.novice_text.vector.bin", binary=True) 
word = "dance"
define_words = ["hustle","social","turn","skip","music","exercise","move","choreo","express","energy","sweat","therapy","disco","hop","jump","tango","salsa","culture","theatre","ballet"]
cosine = cos_sim(word,define_words,model)
print(cosine)
similar_words = sim_words(define_words,model)
print(similar_words)
overlappers = unique_count(similar_words)
print(overlappers)