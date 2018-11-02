from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format("wiki.en.novice_text.vector.bin", binary=True)
 
#model.save_word2vec_format("wiki.en.novice_text.vector.bin", binary=True)  

model1 = KeyedVectors.load_word2vec_format("wiki.en.bin.vector", binary=True)

with open('sim_dance_novice.txt','w') as f:
    f.write(model.most_similar("dance",topn = 100))
                
with open('sim_dance_expert.txt','w') as f1:
    f1.write(model1.most_similar("dance",topn = 100))
        
with open('sim_badminton_novice.txt','w') as f2:
    f2.write(model.most_similar("badminton",topn = 100))
        
with open('sim_badminton_expert.txt','w') as f3:
    f3.write(model1.most_similar("badminton",topn = 100))
        
with open('sim_shooter_novice.txt','w') as f4:
    f4.write(model.most_similar("shooter",topn = 100))

with open('sim_shooter_expert.txt','w') as f5:
    f5.write(model1.most_similar("shooter",topn = 100))        
        
with open('sim_fps_novice.txt','w') as f6:
    f6.write(model.most_similar("fps",topn = 100))        
        
with open('sim_fps_expert.txt','w') as f7:
    f7.write(model1.most_similar("fps",topn = 100))        
        