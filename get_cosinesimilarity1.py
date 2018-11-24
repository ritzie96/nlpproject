from gensim.models import KeyedVectors

def cos_sim(word,define_words,model_novice,model_expert):
    c_n = {}
    c_e = {}
    for i in define_words:
        c_n[i] = model_novice.wv.similarity(word, i)
        c_e[i] = model_expert.wv.similarity(word, i)
        #print(word + "(" + model.wv.similarity(word, i)+ ")"+ i)
    return c_e,c_n
    
model_novice = KeyedVectors.load_word2vec_format("very_novice_epoch1.bin", binary=True) 
model_expert = KeyedVectors.load_word2vec_format("expert_epoch1.bin", binary=True)

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
"xbox",
"rpg",
"puzzle",
"fighting",
"fortnite",
"third",
"respawn",
"frag",
"gib"]


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
"trichotillomania",
"hospital"]



c_e, c_n = cos_sim(word,define_words,model_novice,model_expert):

with open('cos_badminton_novice1.txt','w') as f:
    for k, v in c_n.items():
        f.write(str(k) + ':'+ str(v) + '\n')
        
with open('cos_badminton_expert1.txt','w') as f4:
    for k, v in c_e.items():
        f4.write(str(k) + ':'+ str(v) + '\n')
        
c_e1,c_n1 = cos_sim(word1,define_words1,model_novice,model_expert)

with open('cos_dance_novice1.txt','w') as f1:
    for k, v in c_n1.items():
        f1.write(str(k) + ':'+ str(v) + '\n')
        
with open('cos_dance_expert1.txt','w') as f5:
    for k, v in c_e1.items():
        f5.write(str(k) + ':'+ str(v) + '\n')

c_e2,c_n2 = cos_sim(word2,define_words2,model_novice,model_expert)

with open('cos_shooter_novice1.txt','w') as f2:
    for k, v in c_n2.items():
        f2.write(str(k) + ':'+ str(v) + '\n')

with open('cos_shooter_expert1.txt','w') as f6:
    for k, v in c_e2.items():
        f6.write(str(k) + ':'+ str(v) + '\n')        

c_e3,c_n3 = cos_sim(word3,define_words3,model_novice,model_expert)

with open('cos_psychotherapy_novice1.txt','w') as f3:
    for k, v in c_n3.items():
        f3.write(str(k) + ':'+ str(v) + '\n')        
        
with open('cos_psychotherapy_expert1.txt','w') as f7:
    for k, v in c_e3.items():
        f7.write(str(k) + ':'+ str(v) + '\n')        
 