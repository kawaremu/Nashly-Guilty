# Personnages du jeu
define y = Character('[name_character]', color="#8a335f")
define maitre_avocat = Character('Lloyd Shapley', color="#3d933d")
define client = Character('Inconnu', color="#213f5b")
define a = Character('Assistante', color="#213f5b")
define l = Character('John Nash', color="#bbc46b",image="lover")
define s = Character('Sabrina Duopoli', color="#308285",image="friend")
define m = Character('Maman', color="#9773ac")
define j = Character('Juge Suprême' ,color="#612525",image="judge")
define na = Character("", kind=nvl, what_italic=True, what_color="#6c6bc4")
# Déclarez sous cette ligne les images, avec l'instruction 'image'


# ========================  NASH ==========================
image lover happy:
      subpixel True xzoom 1 pos (0.53, 1.6) zoom 1.05
      "characters/nash_smile.png"
      
image lover angry:
      subpixel True xzoom 1 pos (0.53, 1.6) zoom 1.05
      "characters/nash_angry.png"


image lover neutral:
      subpixel True xzoom 1 pos (0.53, 1.6) zoom 1.05
      "characters/nash_neutral.png"


image lover glad:
      subpixel True xzoom 1 pos (0.53, 1.6) zoom 1.05
      "characters/nash_glad.png"


image lover suspicious:
      subpixel True xzoom 1 pos (0.53, 1.6) zoom 1.05
      "characters/nash_suspicious.png"


# ==================  BEST FRIEND ===================
image friend happy:
      subpixel True pos (0.5, 1.21) zoom 0.98
      "characters/friend happy.png"

image friend smiling:
      subpixel True pos (0.5, 1.21) zoom 0.98 
      "characters/friend smile.png"
      
image friend angry:
      subpixel True pos (0.5, 1.21) zoom 0.98
      "characters/friend angry.png"


image friend clueless:
      subpixel True pos (0.5, 1.21) zoom 0.98
      "characters/friend clueless.png"


image friend mad slightly:
      subpixel True pos (0.5, 1.21) zoom 0.98
      "characters/friend mad slightly.png"

image friend mad:
      subpixel True pos (0.5, 1.21) zoom 0.98
      "characters/friend mad slightly.png"

image friend scolding:
      subpixel True pos (0.5, 1.21) zoom 0.98
      "characters/friend scolding.png"

image friend surprised:
      subpixel True pos (0.5, 1.21) zoom 0.98
      "characters/friend surprised.png"

image friend worried:
      subpixel True pos (0.5, 1.21) zoom 0.98
      "characters/friend worried.png"

image friend sad:
      subpixel True pos (0.5, 1.21) zoom 0.98
      "characters/friend sad.png"

image friend disappointed:
      subpixel True pos (0.5, 1.21) zoom 0.98
      "characters/friend disappointed.png"

# ========================  JUDGE ==========================
image judge neutral:
      subpixel True xzoom 1.0 pos (0.5, 1.01) zoom 1.38 
      "characters/judge_neutral.png"
      
image judge angry:
      subpixel True xzoom 1.0 pos (0.5, 1.01) zoom 1.38
      "characters/judge_angry.png"

image judge annoyed:
      subpixel True xzoom 1.0 pos (0.5, 1.01) zoom 1.38
      "characters/judge_annoyed.png"

image judge disgusted:
      subpixel True xzoom 1.0 pos (0.5, 1.01) zoom 1.38
      "characters/judge_disgust.png"

image judge happy:
      subpixel True xzoom 1.0 pos (0.5, 1.01) zoom 1.38
      "characters/judge_happy.png"

image judge sight:
      subpixel True xzoom 1.0 pos (0.5, 1.01) zoom 1.38
      "characters/judge_sight.png"


# ================================  BACKGROUNDS =======================
image bg outside = im.Scale("backgrounds/bg outside.jpg",1920,1080)
image bg atm = im.Scale("backgrounds/bg atm.png",1920,1080)
image bg house = im.Scale("backgrounds/bg house.jpg",1920,1080)
image bg character room = im.Scale("backgrounds/bg character room.jpg",1920,1080)
image bg supreme court = im.Scale("backgrounds/bg supreme court.jpg",1920,1080)
image bg lover room = im.Scale("backgrounds/bg boyfriend room.jpg",1920,1080)
image bg beach = im.Scale("backgrounds/bg beach.jpg",1920,1080)
image bg living room = im.Scale("backgrounds/bg living room.png",1920,1080)

image halfblack = Solid("#000000cb") #hope this is half transparent (haven't tested)

image bg office door:
      zoom 2
      "backgrounds/bg office door.jpg"

