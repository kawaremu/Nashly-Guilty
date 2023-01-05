label Chapter1Start:
  scene black with dissolve

  play music "audio/coffee_bgm.mp3" volume 0.3 loop
  #Get a black screen while ambient sound is playing 
  show text "Chapitre 1\n L'équilibre qui réside en vous" with Pause(3)

  scene black with dissolve

  "{i}C'est maintenant que les choses commencent."

  pause 3.0
 
  scene bg coffee with dissolve
  show friend smiling with moveinleft 
  s "Hello copine!"
  y "Oh! Coucou Sabrina! Je viens juste d'arriver. Désolée je suis en retard à notre rendez-vous!"
  s @ happy "Mais non, ce n'est rien. Assis-toi!" with dissolve
  y "Alors, comment ça va? Tu racontes quoi de beau ?"
  show friend mad slightly with dissolve
  s  "Quoi de beau ?" with dissolve
  s  "Ce n'est pas la peine de le cacher [name_character]! Je sais ce qui s'est passé la semaine dernière."
  show friend clueless with dissolve
  y "Hein ? De quoi tu parles ?"
  s @ clueless "[name_character]... Je suis policière." with dissolve
  y "Et alors ?" with vpunch
  s @ scolding "Tu es avocate! Et je suis policière." with dissolve
  y "Je ne le suis pas à 100%."

  # Ici, son amie va :
    # 1. l'aider 
    # 2. la faire revenir à la raison
    # 3. la consoler 


  return


  
  