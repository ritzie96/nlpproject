from gensim.models import KeyedVectors

def sim_words(words,model_novice):
    # a = dict()
    b = dict()
    for i in words:
        # a[i] = model_expert.most_similar(i,topn = 100)
        b[i] = model_novice.most_similar(i, topn = 20)
    return b 
    
model_novice = KeyedVectors.load_word2vec_format("wiki.en.very_novice_text.bin", binary=True) 
# model_expert = KeyedVectors.load_word2vec_format("wiki.en.expert.vector.bin", binary=True)

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


words1 = ["dance",
"salsa",
"breakdance",
"folkdance",
"bellydance",
"natyam",
"kathak",
"lavani",
"dabke",
"ballet",
"sweat",
"exercise",
"therapy",
"choreo",
"choreographer",
"choreography",
"sneakers",
"rhythm",
"acrobatic",
"disco",
"culture",
"hop",
"tap",
"music",
"tango",
"dancefloor",
"steps",
"stepup",
"footloose",
"streetdance"]


words2 = ["fps",
"shooter",
"bomb",
"bots",
"chief",
"computer",
"deathmatch",
"display",
"doom",
"enemies",
"engine",
"features",
"first",
"gameplay",
"games",
"gun",
"halo",
"levels",
"looking",
"map",
"military",
"mission",
"mode",
"movement",
"multiplayer",
"person",
"player",
"players",
"playstation",
"point",
"power",
"precise",
"quake",
"reaction",
"rifle",
"space",
"strike",
"team",
"terrorist",
"tournament",
"twitch",
"unreal",
"weapons",
"xbox"]


words3 = ["mental",
"health",
"psychotherapy",
"exposure",
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

b = sim_words(words,model_novice)

with open('new_20_badminton_newnovice.txt','w') as f1:
    for k1, v1 in b.items():
        f1.write(str(k1) + ':'+ str(v1) + '\n')
        
b1 = sim_words(words1,model_novice)

with open('new_20_dance_newnovice.txt','w') as f2:
    for k1, v1 in b1.items():
        f2.write(str(k1) + ':'+ str(v1) + '\n')

b2 = sim_words(words2,model_novice)

with open('new_20_shooter_newnovice.txt','w') as f3:
    for k1, v1 in b2.items():
        f3.write(str(k1) + ':'+ str(v1) + '\n')
        
        
b3 = sim_words(words3,model_novice)

with open('new_20_psychotherapy_newnovice.txt','w') as f4:
    for k1, v1 in b3.items():
        f4.write(str(k1) + ':'+ str(v1) + '\n')        