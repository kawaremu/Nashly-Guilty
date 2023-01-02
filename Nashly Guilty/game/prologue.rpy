# 1.Le téléphone sonne dans l'office. Vous répondez. On vous demande votre nom, et on vérifie que vous êtes bel et bien l'assistante de l'avocat
# 2.C'est bon, vous êtes dans le jeu. Vous appelez votre supérieur et vous continuez à prendre des appels et revenez à votre pile de papiers.
# 3.Quelqu'un toque à la porte, vous allez ouvrir la porte. C'est votre petit ami

init python:
    def wait():
        if renpy.music.is_playing('sound'):
            renpy.pause((5-renpy.music.get_pos('sound')),hard=True)

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
    default name_character = "Vous"

    play music "audio/office ambience.mp3" volume 0.3 loop
    #Get a black screen while ambient sound is playing 
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
    you "Oui et non. Je suis son assistante."

    if name_character == "Vous":
        $ name_character = renpy.input("Je suis (Veuillez insérer votre nom)",exclude="0123456789",length=32)
        $ name_character = name_character.strip()
    you "Je suis [name_character]. Je viens tout juste de reprendre le travail."

    client "D'accord, Mlle [name_character]. Je souhaiterai parler à Mr Lloyd Shapley. Est-ce qu'il est là ?"
    you "Oui, bien sûr. Je vais vous le passer tout de suite."

    "{i}Vous déposez le combiné sur la table, histoire que le client ne puisse pas écouter vos conversations privées."

    you "Mr Shapley ?"
    you "MR SHAPLEY !" with vpunch
    maitre_avocat "Oui, oui! J'arrive! Tu peux bien attendre [name_character], non? Tu vois bien que je suis occupé!"
    you "Pardon Monsieur Shapley, mais il y a quelqu'un à l'autre bout du fil qui vous attend."
    maitre_avocat "D'accord, d'accord. Passe le moi."
    "{i}Vous indiquez avec votre doigt le combiné du téléphone. Mr Shapley se presse de le saisir et vous suggère du mouvement de sa main que vous
    pouvez disposez."
    "Quelle arrogance ce Shapley."
    "{i}Vous décidez d'aller vous débarbouiller le visage, sentant la chaleur vous montez à la tête."

    scene bg bathroom with dissolve
    "{i}Vous ouvrez le robinet. Votre reflet dans le miroir affiche des cernes."
    play sound "audio/running water.mp3" volume 0.7

    "{i}L'eau est fraîche. Elle est revigorisante et vous fait oublier tous vos problèmes."
    you "Ces derniers jours ont été particulièrement fort en émotion."

    play sound "<from 4 to 6>audio/door knock.mp3" volume 0.7
    a "[name_character] ? Tu es là ?"
    $ wait()
    you "Oui, oui? Qu'est-ce qu'il y a ?"
    a "Il y a quelqu'un qui te cherche, il t'attend devant la porte."
    you "D'accord, j'arrive."

    scene bg office door with dissolve
    stop music fadeout 0.5
    show lover happy with moveinleft 
    lover "Hey."



    return










label variables:
    pass