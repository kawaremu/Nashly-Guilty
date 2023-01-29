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
  y  "Je ne le suis pas vraiment..."
  s @ surprised "Ahbon ? Pourquoi ?"
  y "Bah... Je travaille en tant qu'assistante d'un avocat, tu penses vraiment que ..."
  show friend angry with dissolve
  s  "Ecoute [name_character]... Je suis ta meilleure amie, et tu n'as pas à me cacher quoi que ce soit. "
  s "Je suis là pour t'aider."
  y "Sabrina... La semaine passée, Nash est venue à mon bureau et m'a humilié... Il m'a giflé dehors et m'a pris de l'argent..."
  s @ worried "Je sais... J'espère que c'est la première fois, sinon je risque de m'énerver."
  y "..."
  s @ surprised "Quoi ?"
  y "..."
  s @ mad "NON!" with hpunch
  s @ mad "Je n'accepte pas ça."
  y "Mais Sabrina..."
  s "Non. Je pense qu'on devrait trouver une solution."


  # Ici, son amie va :
    # 1. la consoler et l'aider 
    # 2. la faire revenir à la raison


  return


  
  