from gensim.models import KeyedVectors

def cos_sim(word,define_words,model_novice):
    c_n = {}
    #c_e = {}
    for i in define_words:
        c_n[i] = model_novice.wv.similarity(word, i)
        #c_e[i] = model_expert.wv.similarity(word, i)
        #print(word + "(" + model.wv.similarity(word, i)+ ")"+ i)
    return c_n
    
    
model_novice = KeyedVectors.load_word2vec_format("wiki.en.very_novice_text.bin", binary=True) 

word = "badminton"
word1 = "dance"
word2 = "shooter"
word3 = "psychotherapy"

define_words = ["baddy",
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


define_words1 = ["salsa",
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


define_words2 = ["fps",
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


define_words3 = ["mental",
"health",
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


c_n = cos_sim(word,define_words,model_novice)

with open('avg_badminton_newnovice.txt','w') as f:
    for k, v in c_n.items():
        f.write(str(k) + ':'+ str(v) + '\n')
        
c_n1 = cos_sim(word1,define_words1,model_novice)

with open('avg_dance_newnovice.txt','w') as f1:
    for k, v in c_n1.items():
        f1.write(str(k) + ':'+ str(v) + '\n')

c_n2 = cos_sim(word2,define_words2,model_novice)

with open('avg_shooter_newnovice.txt','w') as f2:
    for k, v in c_n2.items():
        f2.write(str(k) + ':'+ str(v) + '\n')

c_n3 = cos_sim(word3,define_words3,model_novice)

with open('avg_psychotherapy_newnovice.txt','w') as f3:
    for k, v in c_n3.items():
        f3.write(str(k) + ':'+ str(v) + '\n')        
        
        
        
        
        
        
        
        