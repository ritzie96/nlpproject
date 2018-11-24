import requests
import json

#catName is the name of the category
def wikiCatReq(catName):
	S = requests.Session()
	URL = "https://en.wikipedia.org/w/api.php"
	PARAMS = {
		'action': "query",
		'list': "categorymembers",
		'cmtitle': "Category:" + catName,
		'cmlimit': 500,
		'format': "json"
	}

	R = S.get(url=URL, params=PARAMS)
	DATA = R.json()
	return DATA

#TODO: fix very bad code duplication, but it just works
#the the names of the articles if more exists
def wikiCatReqCont(catName, cont):
	S = requests.Session()
	URL = "https://en.wikipedia.org/w/api.php"
	PARAMS = {
		'action': "query",
		'list': "categorymembers",
		'cmtitle': "Category:" + catName,
		'cmcontinue': cont,
		'cmlimit': 100,
		'format': "json"
	}

	R = S.get(url=URL, params=PARAMS)
	DATA = R.json()
	return DATA

#prints the article names
def printTitles(data):
	#print(type(data))
	#print(data['query']['categorymembers'])
	listOfArticles = (data['query']['categorymembers'])
	for article in listOfArticles:
		print('"' + article['title'] + '",')
	
		

#SET YOUR DESIRED CATEGORY
category = "First-person shooters"

DATA = wikiCatReq(category)
printTitles(DATA)

#get the continue parameter if one available
hasMoreArticles = True
cont = (DATA['continue']['cmcontinue'])

#get all articles
while hasMoreArticles:
	DATA = wikiCatReqCont(category, cont)
	printTitles(DATA)
	if "continue" in DATA:
		cont = (DATA['continue']['cmcontinue'])
	else:
		hasMoreArticles = False
	
#for key, value in DATA.items():
#	print(key, value)

#print(DATA)
