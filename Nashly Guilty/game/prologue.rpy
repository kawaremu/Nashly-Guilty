# 1.Le téléphone sonne dans l'office. Vous répondez. On vous demande votre nom, et on vérifie que vous êtes bel et bien l'assistante de l'avocat
# 2.C'est bon, vous êtes dans le jeu. Vous appelez votre supérieur et vous continuez à prendre des appels et revenez à votre pile de papiers.
# 3.Quelqu'un toque à la porte, vous allez ouvrir la porte. C'est votre petit ami

init python:
    def wait(input_sec):
        if renpy.music.is_playing('sound'):
            renpy.pause((input_sec-renpy.music.get_pos('sound')),hard=True)

# Presenting
label splashscreen:
    scene black with dissolve
    with Pause(1)

    show text "MIV Interactive présente..." with dissolve
    with Pause(1)

    show text "MIV Interactive présente..." with dissolve
    with Pause(1)

    hide text with dissolve
    with Pause(1)

    show text "Nashement Coupable" with dissolve
    with Pause(1)

    show text "Toute ressemblance avec une personne existant ou ayant existé n'est qu'une pure coïncidence." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    return


# Le jeu commence ici
label start:
    $name_character = "Vous"

    play music "audio/office ambience.mp3" volume 0.3 loop
    #Get a black screen while ambient sound is playing 

    show text "{i}Prologue : L’autre n’est pas votre problème" with Pause(3)
    

    scene black with dissolve
    pause 3.0
 
    scene bg law office with dissolve
    "08:24."
    "{i}C'est une journée calme et presque monotone au bureau."
    "{i}Il y a quelques femmes qui attendent dans la salle d'attente."
    "{i}On entend les piles de papier craquer au son des doigts des employés."

    play sound "audio/phone ringing.mp3" volume 0.7
    "Le téléphone sonne déjà ! C'est sûrement du travail en plus."

    play sound "<from 7.8 to 8.5>audio/phone pick up.mp3" volume 0.8

    "Bonjour. Cabinet Nash d'Avocats, j'écoute ?"
    client "Bonjour. Je suis bien avec Mr Lloyd Shapley ?"
    y "Oui et non. Je suis son assistante."

    if name_character == "Vous":
        $ name_character = renpy.input("Je suis (Veuillez insérer votre nom)",exclude="0123456789",length=32)
        $ name_character = name_character.strip()
    y "Je suis [name_character]. Je viens tout juste de reprendre le travail."

    client "D'accord, Mlle [name_character]. Je souhaiterai parler à Mr Lloyd Shapley. Est-ce qu'il est là ?"
    y "Oui, bien sûr. Je vais vous le passer tout de suite."

    "{i}Vous déposez le combiné sur la table, histoire que le client ne puisse pas écouter vos conversations privées."

    y "Mr Shapley ?"
    y "MR SHAPLEY !" with vpunch
    maitre_avocat "Oui, oui! J'arrive! Tu peux bien attendre [name_character], non? Tu vois bien que je suis occupé!"
    y "Pardon Monsieur Shapley, mais il y a quelqu'un à l'autre bout du fil qui vous attend."
    maitre_avocat "D'accord, d'accord. Passe le moi."
    "{i}Vous indiquez avec votre doigt le combiné du téléphone. Mr Shapley se presse de le saisir et vous suggère du mouvement de sa main que vous
    pouvez disposez."
    "Quelle arrogance ce Shapley."
    "{i}Vous décidez d'aller vous débarbouiller le visage, sentant la chaleur vous montez à la tête."

    scene bg bathroom with dissolve
    "{i}Vous ouvrez le robinet. Votre reflet dans le miroir affiche des cernes."
    play sound "audio/running water.mp3" volume 0.7

    "{i}L'eau est fraîche. Elle est revigorisante et vous fait oublier tous vos problèmes."
    $wait(5)
    y "Ces derniers jours ont été particulièrement fort en émotion."

    play sound "<from 4 to 6>audio/door knock.mp3" volume 0.7
    a "[name_character] ? Tu es là ?"
    $ wait()
    y "Oui, oui? Qu'est-ce qu'il y a ?"
    a "Il y a quelqu'un qui te cherche, il t'attend devant la porte."
    y "D'accord, j'arrive."

    scene bg office door with dissolve
    stop music fadeout 0.5

    # L'apparition du joueur Nash
    show lover happy with moveinleft 
    l  "Hey."
    y "Oh! John! Qu'est-ce que tu fais là ?"

    # Ici, le narrateur parle, mais c'est la voix du personnage principal
    "{i}Ca, c'est John Nash. Mon âme-soeur."
    "{i}Je l'aime vraiment beaucoup, et je ne sais pas si je peux vivre sans lui."
    "{i}On compte se marrier bientôt. J'essaye de l'aider comme je peux."
 
    l @ glad "Je me suis dit que ça serait cool de venir te voir au boulot. Comment ça se passe au cabinet ?" with dissolve
    y "Ca pourrait aller mieux. Mon supérieur vient juste de me crier dessus..."
    l @ suspicious "Arrête de faire ta nunuche! T'es trop sensible!" with dissolve
    y "C'est pas gentil ça! Je pense juste que ça ne se fait pas... En tout cas, qu'est-ce que tu fais là ?"
    l @ glad "J'ai besoin d'argent en fait..."
    y "QUOI ?" with vpunch
    l @ suspicious "Attends..." with dissolve
    show lover neutral with dissolve
    y "Quoi encore! C'est la 3e fois de la semaine que tu me demandes de l'argent, je ne suis pas une banque..."
    l @ glad "Ce n'est pas la fin du monde... J'en ai vraiment besoin, mon amour..." with dissolve
    y "Hmm... T'as besoin de combien d'argent ?"
    l @ glad "J'ai besoin de 25000DA, maintenant. En liquide." with dissolve
    y "Je ne pense pas que ça sera possible, désolée."
    show lover angry with dissolve
    l  "Comment ça pas possible?" with hpunch
    y "Je n'ai pas cette somme."
    l  "Je m'en fous. J'en ai besoin." 
    l "ET MAINTENANT !" with vpunch
    l "Donne moi cet argent! Tout de suite!" with hpunch
    y "Mon amour, ça ne sera pas possible..."
    l "Si. Montre moi ton sac, tout de suite!"
    y "Non.. Mon sac est dans mon bureau, je ne peux pas te laisser rentrer..."
    l "POUSSE-TOI! Laisse moi passer!" with vpunch
    # Camera flash - quickly fades to white, then back to the scene.
    define flash = Fade(0.1, 0.0, 1, color="#000000")
    y "No-" with flash
    play sound "<from 0 to 2>audio/body_fall.mp3" volume 0.7

    scene bg law office with dissolve
    "{i}Nash court vers le bureau où se trouve mon sac."
    "{i}Il me pousse assez fort pour me faire trébucher derrière lui et ne m'aide même pas à redresser..."
    y "Nash! Attends!" with vpunch

    show lover angry with moveinright
    play music "audio/office ambience.mp3" volume 0.2 loop
    l "NON! Où est ton sac ?"

    "{i}Les assistantes qui travaillent avec moi semblent observer la scène..."
    "{i}C'est très honteux pour moi, et j'ai de la chance que Mr Shapley se soit enfermé dans son bureau après avoir fini l'appel."
    l @ glad "Oh! Le voici!" with dissolve
    y "Nash, mon amour s'il te plaît... Je n'ai pas cet argent!"
    l "Je m'enfous. Tu me le donneras tout de suite!"
    y "Nash..."
    hide lover with dissolve
    "{i}Il commence à fouiller violamment mon sac."
    "{i}Lorsqu'il retrouve mon porte-monnaie, il commence à compter l'argent qu'il y avait à l'intérieur."
    show lover suspicious with moveinright
    l "Alors, combien tu as..." with dissolve
    l "1000..."
    l "3000..."
    l "5000..."
    l "6000..."
    l @ glad "C'est pas mal 6000 DA! " with dissolve
    y "Nash! Arrête, tu me fous la honte!"
    l @ happy "Pourquoi tu dis ça? Tu es ma bien aimée, donc je prends l'argent que je veux!" with dissolve
    y "Ce n'est pas une raison!"
    l @ angry "Tais-toi! Donne moi la suite. Je sais que tu la caches dans les tiroirs.." with dissolve
    y "Non, c'est tout ce que j'ai. Tu m'as tout pris."
    l @ glad "Alors, on va à la poste retirer de l'argent, n'est-ce pas ?"
    y "Comment ça?" with vpunch
    l @ happy "Oui, tout de suite. On va à la banque la plus proche, retirer de l'argent." with dissolve
    y "Non, je ne peux pas je travaille." 
    show lover angry with vpunch

    play sound "audio/face punch.mp3" volume 0.7
    "{i}Nash m'a giflé devant tout le monde."
    y "... Pourquoi..."
    l @ angry "Je t'ai dit que j'avais besoin d'argent. C'est une urgence."
    y "... Ce n'est pas une raison pour me frapper devant tout le monde..."
    "{i}Je pleurais à chaudes larmes, et c'était plus que honteux de me faire gifflée dans mon bureau."
    y "D'accord.. Si tu veux cet argent.. Allons-y..."
    "{i}Les assistantes me regardaient avec un regard plein de pitié. Incapables de me venir en aide tant mon amoureux paraissait agressif."
    show lover glad with dissolve
    l "Super, allons-y. Pardon pour la giffle mon amour!" 

    "{i}Il m'a forcé à quitter mon bureau pour me diriger vers la banque la plus proche."
    "{i}J'étais plus blessée qu'autre chose... Mais je m'étais habituée à sa violence..."
    "{i}Même si l'on s'était pas encore mariés, tolérer ce genre de comportement était devenu une seconde nature pour moi."
    stop music fadeout 0.5
    scene black with dissolve
    pause 1.5

    scene bg outside with dissolve
    play music "audio/outside vfx.mp3" fadein 0.5 volume 0.2  loop
    show lover suspicious with moveinleft 
    
    l "Alors! Vas-y, sors le reste de la somme." 
    l @ angry "Qu'est-ce que tu attends ?" with dissolve
    y "... Okay."
    hide lover

    scene bg atm with dissolve
    "{i}Je sors alors ma carte de crédit et l'insère dans le distributeur pour sortir la somme d'argent demandée."
    play sound "audio/atm vfx.mp3" volume 0.7
    "{i}Le bruit des billets semble réconforter Nash dans sa violence..."
    $ wait(30)
    scene black with dissolve
    stop music fadeout 0.5
    pause 3
    jump Chapter1Start
    return

# FIN PROLOGUE
