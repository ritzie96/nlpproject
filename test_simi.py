
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format("wiki.en.novice_text.vector.bin", binary=True) 
#model.save_word2vec_format("wiki.en.novice_text.vector.bin", binary=True)  
print("LESS KNOWN MODEL")
print(model.most_similar("dance"))
print(model.most_similar("shooter"))
print(model.most_similar("badminton"))
print(model.most_similar("health"))

model1 = KeyedVectors.load_word2vec_format("wiki.en.bin.vector", binary=True)
print("FULL MODEL")
print(model1.most_similar("dance"))
print(model1.most_similar("shooter"))
print(model1.most_similar("badminton"))
print(model1.most_similar("health"))