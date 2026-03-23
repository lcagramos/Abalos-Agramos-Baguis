import random

#PAST CODE FOR REFERENCE


characters = {
   "onBanner5" : {"Xiao" : 0.0025},
   "offBanner5" : {"Jean" : 0.0025, "Diluc" : 0.0025, "Keqing" : 0.0025, "Qiqi" : 0.0025, "Mona" : 0.0025},
   "onBanner4" : {"Kaveh" : 0.0025, "Faruzan" : 0.0025, "Bennett" : 0.0025},
   "offBanner4" : {"Xingqiu" : 0.0025, "Xiangling" : 0.0025, "Freminet" : 0.0025, "Ningguang" : 0.0025, "Kuki Shinobu" : 0.0025,"Yao Yao" : 0.0025, "Heizou" : 0.0025}
}
weapons = {
   "3*" : {"Slingshot (3* Bow)" : 0.8, "Debate Club (3* Claymore)" : 0.8, "Harbinger of Dawn (3* Sword)" : 0.8, "Thrilling Tales of Dragon Slayer (3* Catalyst)" : 0.8, "White Tassel (3* Polearm)" : 0.8},
   "4*" : {"Rust (4* Bow)" : 0.4, "Favonius Greatsword (4* Claymore)" : 0.4, "Lion's Roar (4* Sword)" : 0.4, "Favonius Codex (4* Catalyst)" : 0.4, "Dragon's Bane (4* Polearm)" : 0.4}
}


pull = 10


for i in range(pull, 0, -1):
   if i == 10:
       guaranteed = list(characters["onBanner4"].keys()) + list(characters["offBanner4"].keys()) + list(weapons["4*"].keys()) # equal chances
       choice = random.choice(guaranteed)
       print(f"You got {choice}")


