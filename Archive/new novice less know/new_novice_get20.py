from gensim.models import KeyedVectors

def sim_words(words,model_novice,model_expert):
    a = dict()
    b = dict()
    for i in words:
        a[i] = model_expert.most_similar(i,topn = 200)
        b[i] = model_novice.most_similar(i, topn = 200)
    return a,b 
    
model_novice = KeyedVectors.load_word2vec_format("very_novice_epoch4.bin", binary=True) 
model_expert = KeyedVectors.load_word2vec_format("expert_epoch4.bin", binary=True)

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

a, b = sim_words(words,model_novice,model_expert)

with open('badminton_novice.txt','w') as f1:
    for k1, v1 in b.items():
        f1.write(str(k1) + ':'+ str(v1) + '\n')
        
with open('badminton_expert.txt','w') as f5:
    for k1, v1 in a.items():
        f5.write(str(k1) + ':'+ str(v1) + '\n')
        
a1, b1 = sim_words(words1,model_novice,model_expert)

with open('dance_novice.txt','w') as f2:
    for k1, v1 in b1.items():
        f2.write(str(k1) + ':'+ str(v1) + '\n')

with open('dance_expert.txt','w') as f6:
    for k1, v1 in a1.items():
        f6.write(str(k1) + ':'+ str(v1) + '\n')
        
a2, b2 = sim_words(words2,model_novice,model_expert)

with open('shooter_novice.txt','w') as f3:
    for k1, v1 in b2.items():
        f3.write(str(k1) + ':'+ str(v1) + '\n')
        
with open('shooter_expert.txt','w') as f7:
    for k1, v1 in a2.items():
        f7.write(str(k1) + ':'+ str(v1) + '\n')
        
        
a3, b3 = sim_words(words3,model_novice,model_expert)

with open('psychotherapy_novice.txt','w') as f4:
    for k1, v1 in b3.items():
        f4.write(str(k1) + ':'+ str(v1) + '\n')

with open('psychotherapy_expert.txt','w') as f8:
    for k1, v1 in a3.items():
        f8.write(str(k1) + ':'+ str(v1) + '\n')        