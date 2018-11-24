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
    
model = KeyedVectors.load_word2vec_format("wiki.en.expert.vector.bin", binary=True)

word = "psychotherapy"
define_words =["exposure",
"reinforcement",
"stimulus",
"response",
"ruminating",
"ruminate",
"ruminates",
"ruminated",
"brooding",
"conditioning",
"medication",
"ocd",
"ect",
"cbt",
"serotonin",
"inhibitor",
"antidepressants",
"placebo",
"ssri",
"psychosurgery",
"addiction",
"sleep",
"freud",
"trichotillomania"]


cosine1 = cos_sim(word,define_words,model)
print(cosine1)
with open('new_mental_expert.txt','w') as f:
    for k, v in cosine1.items():
        f.write(str(k) + ':'+ str(v) + '\n')
similar_words1 = sim_words(define_words,model)
print(similar_words1)
with open('new_mental_expert.txt','a') as f1:
    for k, v in similar_words1.items():
        f1.write(str(k) + ':'+ str(v) + '\n')