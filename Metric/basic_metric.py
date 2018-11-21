import gensim.downloader as api
import numpy as np

#get similarity between concept and each relations
#and return the average score
def metric_avg_dist(model, concept, relations):
	score = np.float(0.0)
	for rel in relations:
		print("concept : " + concept)
		print("Relations : " + rel)
		print("similarity : " + str(model.similarity(concept,rel)))
		print("")
		score = np.add(score,model.similarity(concept,rel))
	metric_score = np.divide(score,len(relations))
	return metric_score

	






#load model
model = api.load("glove-twitter-25")
concept = "car"
relations = ["wheel", "window", "speed", "mercedes", "motorcycle", "flower", "dancing"]

print("metric get score:")
print(metric_avg_dist(model,concept, relations))


