# Personnages du jeu
define y = Character('[name_character]', color="#8a335f")
define maitre_avocat = Character('Lloyd Shapley', color="#3d933d")
define client = Character('Inconnu', color="#213f5b")
define a = Character('Assistante', color="#213f5b")
define l = Character('John Nash', color="#bbc46b",image="lover")
define s = Character('Sabrina Duopoli', color="#308285",image="friend")


# Déclarez sous cette ligne les images, avec l'instruction 'image'





# ex: image eileen heureuse = "eileen_heureuse.png"

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


image friend scolding:
      subpixel True pos (0.5, 1.21) zoom 0.98
      "characters/friend scolding.png"

image friend surprised:
      subpixel True pos (0.5, 1.21) zoom 0.98
      "characters/friend surprised.png"

image friend worried:
      subpixel True pos (0.5, 1.21) zoom 0.98
      "characters/friend worried.png"




# ================================  BACKGROUNDS =======================
image bg outside = im.Scale("backgrounds/bg outside.jpg",1920,1080)
image bg atm = im.Scale("backgrounds/bg atm.png",1920,1080)
image bg_beach:
      zoom 2
      "backgrounds/bg beach.jpg"


image bg office door:
      zoom 2
      "backgrounds/bg office door.jpg"

