# 1.Le téléphone sonne dans l'office. Vous répondez. On vous demande votre nom, et on vérifie que vous êtes bel et bien l'assistante de l'avocat
# 2.C'est bon, vous êtes dans le jeu. Vous appelez votre supérieur et vous continuez à prendre des appels et revenez à votre pile de papiers.
# 3.Quelqu'un toque à la porte, vous allez ouvrir la porte. C'est votre petit ami

init python:
    def wait_phone_ringing():
        if renpy.music.is_playing('sound'):
            renpy.pause((10-renpy.music.get_pos('sound')),hard=True)

# Le jeu commence ici
label start:
    default name_character = "default"

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
    "Oui et non. Je suis son assistante."

    if name_character == "default":
        $ name_character = renpy.input("Je suis ",exclude="0123456789",length=32)
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
    "{i}Vous indiquez avec votre doigt le combiné du téléphone. Mr Shapley se presse de le saisir et vous suggère du mouvement de main que vous
    pouvez disposez."
    "Quelle arrogance ce Shapley."
    "{i} Vou"

    return










label variables:
    pass
