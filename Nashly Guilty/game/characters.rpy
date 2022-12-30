# Personnages du jeu
define you = Character('[name_character]', color="#460a28")
define maitre_avocat = Character('Lloyd Shapley', color="#3d933d")
define client = Character('Inconnu', color="#213f5b")
define a = Character('Assistante', color="#213f5b")
define lover = Character('John Nash', color="#bbc46b")


# Déclarez sous cette ligne les images, avec l'instruction 'image'



# ex: image eileen heureuse = "eileen_heureuse.png"
image lover happy = im.Scale("characters/nash_smile.png", 300, 1080)
image lover angry = "characters/nash_angry.png"
image lover neutral = "characters/nash_neutral.png"
image lover glad = "characters/nash_glad.png"
image lover suspicious = "characters/nash_suspicious.png"


# BACKGROUNDS 
image bg_beach:
      zoom 2
      "backgrounds/bg beach.jpg"


image bg office door:
      zoom 2
      "backgrounds/bg office door.jpg"

