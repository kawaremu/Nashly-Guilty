label Chapter1Start:
  scene black with dissolve

  play music "audio/coffee_bgm.mp3" volume 0.3 loop
  #Get a black screen while ambient sound is playing 
  show text "Chapitre 1\n L'équilibre qui réside en vous" with Pause(3)

  scene black with dissolve

  "{i}C'est maintenant que les choses commencent.{/i}"

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
  s @ clueless "[name_character]... Je suis policière."
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
  show friend mad with dissolve
  y "..."
  s @ mad "NON!" with hpunch
  s @ mad "Je n'accepte pas ça." with dissolve
  y "Mais Sabrina..."
  s "Non. Je pense qu'on devrait trouver une solution." with dissolve
  y "Comment ça ?"
  show friend worried with dissolve
  s "Tu as oublié une chose importante, [name_character]... Tu as des problèmes de santé." with dissolve
  "{i}Sabrina avait raison... J'étais de constitution faible, et je n'avais en aucun cas intérêt à jouer avec ma vie dans l'unique but de 
  recevoir de l'affection d'un être humain...{/i}"
  "{i}Mon médecin me l'avait dit la dernière fois. Que si la dépression s'en prenait à moi, je réduirai mon espérance de vie...{/i}"
  "{i}Nash me rend si triste ces deux dernières années, il ne fait que prendre mon argent et m'humilier...{/i}"
  "{i}Les larmes me montent juste à la pensée de la semaine dernière. 
  Il m'a acheté une glace en guise de remerciement... 
  Après une giffle publique...{/i}"
  show friend sad with dissolve
  s "[name_character]...{p}Tu ne mérites pas ce traitement...{p=1.0}Laisse moi t'aider..." with dissolve
  y "... Mais comment ?"
  s @ smiling "Je suis contente que tu ne te sois pas laissée abattre!" with dissolve
  y "Je ne sais pas exactement quoi faire, mais une chose est sûre; cette relation me fait souffrir."
  s @ disappointed "Essayons d'être des joueurs rationnels... Nash est comme ton adversaire." with dissolve
  menu:
    "C'est vrai... Nash ne m'a jamais aimé. Il n'est là que pour ses propres intérêts...":
      s @ happy "Oh, je n'aurais jamais pu pensé entendre ça de ta part!" with dissolve
    "Non... Je l'aime vraiment. Je ne pense pas pouvoir le laisser tomber.":
      s @ disappointed "C'est ton opinion,mais je n'ai jamais aimé cet homme..." with dissolve
  

  s @ smiling "Tu peux compter sur mon aide en tout cas. Je suis policière, et je promets de t'assister dans toutes les procédures." with dissolve

  "{i}Sabrina me propose de l'aide. Je pense que ça sera un tournant dans ma vie.{/i}" with dissolve

  show friend clueless with dissolve
  menu strategieR_C:
    "{i}Faîtes un choix. Cette stratégie vous sera soit bénéfique, soit destructrice.{/i}"
    "{size=+20}Dénoncer à la police{/size}{vspace=20}{size=-10}{color=#4287f5}{i}(espérance de vie +10){/i}{/color}{/size}":
      jump ReportPolice
    "{size=+20}Essayer de discuter avec Nash{/size} {vspace=20}{size=-10}{color=#d1492e}{i}(espérance de vie +5){/i}{/color}{/size}":
      jump ConversationLover
  return

label ReportPolice:
  show friend smiling with dissolve
  s  "Très bon choix et sage décision."
  y "Merci... Qu'est-ce que je dois faire maintenant ?"
  s @ happy "Haha, tu dois d'abord finir ton café et tes petits gâteaux, et ensuite, tu rentreras à la maison." with dissolve
  y "Qu'est-ce que je ferais sans toi Sabrina !"
  s @ happy "Beaucoup de choses quand tu es courageuse! Prends ta décision ce soir encore une fois et confirme moi par téléphone." with dissolve
  "{i}Sabrina et moi prenons nos gâteaux dans le plus grand des calmes.{/i}"
  "{i}C'était le calme avant la tempête; une tempête qui allait semer le chaos dans l'équilibre de la vie que je menais.{/i}"
  "{i}Un équilibre auprès de Nash...{/i}"
  stop music fadeout 0.5


  scene black with dissolve
  #Get a black screen while ambient sound is playing 
  show text "Le déjeuner continue entre les deux amies..." with Pause(3)
  scene black with dissolve

  "{i}Vous rentrez à la maison, la tête pleine de stratégies pour un meilleur avenir et une plus longue vie pleine de prospérité.{/i}"


  scene bg house with dissolve
  play music "audio/house_bgm.mp3" volume 0.3 loop
  y "Maman ? Papa ?"
  "{i}Aucune réponse...{/i}"
  y "Ce n'est pas grave. Je vais monter et rejoindre ma chambre. Je pourrai mieux réflechir une fois là-bas."

  scene bg character room with dissolve
  y "Quelles semaines fatiguantes... Je suis crevée."

  play sound "audio/door open.mp3" volume 0.7
  "La porte de ma chambre s'ouvre et c'est une figure douce qui vient m'embrasser chaleureusement."
  $wait(5)
  m "[name_character]! Je te cherchais!"
  y "Maman! Tu m'as manquée!"
  "Je saute dans ses bras." with vpunch
  m "Toi aussi ma belle... J'étais dans la cuisine. Comment te sens-tu ? "
  y "Je suis fatiguée... très fatiguée, même."
  m "Ta santé passe avant tout. Je t'aime mon coeur. Si tu as besoin d'aide, sache que nous serons toujours là pour toi, ton père et moi."
  y "Merci maman... "
  m "Maintenant va dormir, et repose toi bien. Je t'ai laissé ta tisane préférée sur le bahut. Bonne nuit."
  y "Bonne nuit..."
  "{i}Ma mère quitte ma chambre, sans faire de bruit.{/i}"
  "{i}Maintenant que je suis seule avec mes pensées, je devrais prendre une décision... Cela fait presque 2 ans que je souffre...{/i}"
  "{i}A cela s'ajoute les menaces avec lesquelles je vis... Nash me torture...{/i}"
  "{i}Je cache même à mes parents que je prends des somnifères afin de pouvoir dormir...{/i}"
  "{i}Rompre un équilibre n'est pas chose facile...{/i}"

  menu:
    "{i}Faîtes un choix. Cette stratégie vous sera soit bénéfique, soit destructrice.{/i}"
    "{size=+20}Dénoncer à la police pour de bon.{/size}  {vspace=20}{size=-10}{color=#4287f5}{i}(espérance de vie +10){/i}{/color}{/size}":
      $ NashEquilibrium = True
      stop music fadeout 1.0
      jump ReportToJustice
    "{size=+20}Ne pas dénoncer à la police.{/size} {vspace=20}{size=-10}{color=#d1492e}{i}(espérance de vie -20){/i}{/color}{/size}":
      stop music fadeout 1.0
      jump EternalSuffering

  return


label ConversationLover:
  show friend mad with dissolve
  s "[name_character]! Pourquoi tu es si têtue.."
  y "Sabrina, ce n'est pas grave. Je vais essayer de le raisonner..."
  s @ disappointed "... J'espère que tu feras le bon choix après ça. Je n'approuverai jamais cet homme." with dissolve
  y "Il est merveilleux, même avec ses défauts..."
  s @ clueless "Prends ta décision ce soir encore une fois et confirme moi par téléphone." with dissolve
  "{i}Sabrina et moi prenons nos gâteaux dans le plus grand des calmes.{/i}"
  "{i}C'était le calme avant la tempête; une tempête qui allait semer le chaos dans l'équilibre de la vie que je menais.{/i}"
  "{i}Un équilibre auprès de Nash...{/i}"
  stop music fadeout 0.5

  scene black with dissolve
  #Get a black screen while ambient sound is playing 
  show text "Le déjeuner continue entre les deux amies..." with Pause(3)
  scene black with dissolve

  "{i}Vous rentrez à la maison, la tête pleine de stratégies pour un meilleur avenir et une plus longue vie pleine de prospérité.{/i}"
  scene bg house with dissolve
  play music "audio/house_bgm.mp3" volume 0.3 loop
  y "Maman ? Papa ?"
  "{i}Aucune réponse...{/i}"
  y "Ce n'est pas grave. Je vais monter et rejoindre ma chambre. Je pourrai mieux réflechir une fois là-bas."

  scene bg character room with dissolve
  y "Quelles semaines fatiguantes... Je suis crevée."

  play sound "audio/door open.mp3" volume 0.7
  "La porte de ma chambre s'ouvre et c'est une figure douce qui vient m'embrasser chaleureusement."
  $wait(5)
  m "[name_character]! Je te cherchais!"
  y "Maman! Tu m'as manquée!"
  "Je saute dans ses bras." with vpunch
  m "Toi aussi ma belle... J'étais dans la cuisine. Comment te sens-tu ? "
  y "Je suis fatiguée... très fatiguée, même."
  m "Ta santé passe avant tout. Si tu as besoin d'aide, sache que nous serons toujours là pour toi, ton père et moi."
  y "Merci maman... "
  m "Maintenant va dormir, et repose toi bien. Je t'ai laissé ta tisane préférée sur le bahut.Bonne nuit.Je t'aime mon coeur."
  y "Bonne nuit..."
  "{i}Ma mère quitte ma chambre, sans faire de bruit.{/i}"
  "{i}Maintenant que je suis seule avec mes pensées, je devrais prendre une décision... Cela fait presque 2 ans que je souffre...{/i}"
  "{i}A cela s'ajoute les menaces avec lesquelles je vis... Nash me torture...{/i}"
  "{i}Je cache même à mes parents que je prends des somnifères afin de pouvoir dormir...{/i}"
  "{i}Rompre un équilibre n'est pas chose facile...{/i}"

  menu:
    "{i}Faîtes un choix. Cette stratégie vous sera soit bénéfique, soit destructrice.{/i}"
    "{size=+20}Avoir une conversation mâture avec Nash{/size} {vspace=20}{size=-10}{color=#4287f5}{i}(espérance de vie +10){/i}{/color}{/size}":
      $ NashEquilibrium = True
      stop music fadeout 1.0
      jump CompromiseTogether
    "{size=+20}Confronter Nash avec rage{/size} {vspace=20}{size=-10}{color=#d1492e}{i}(espérance de vie -20){/i}{/color}{/size}":
      stop music fadeout 1.0
      jump ArgumentAndJustice
  return
  