label CompromiseTogether:
  #Transition vers la scène de Justice
  scene black with dissolve
  "{i}Après avoir pris cette décision, vous n'appelez pas votre meilleure amie Sabrina.{/i}"
  "{i}C'est maintenant que les {b}vraies{/b} choses commencent.{/i}"

  centered "Epilogue \n {p=4.0} Compromis."
  hide text with dissolve
  $ renpy.pause(4, hard=True)

  play music "audio/compromise theme.mp3" volume 0.3 loop fadein 0.4
  
  "{i}Vous vous rendez chez Nash afin d'essayer de le raisonner.{/i}"
  play sound "<from 4 to 6>audio/door knock.mp3" volume 0.7
  play sound "audio/door open.mp3" volume 0.7
  "La porte s'ouvre et c'est Nash qui apparaît."
  $wait(5)
  scene bg lover room
  with dissolve

  show lover glad with moveinleft 
  l "Woah! [name_character], quelle belle suprise!"

  y "{i}(Sa maison était délabrée, des journals et de la nourriture étaient éparpillés un peu partout.){/i}"
  y "{i}(Il avait les yeux rouges... Comme s'il venait de prendre des médicaments..){/i}"
  y "{i}(Sa maison était délabrée, des journals et de la nourriture étaient éparpillés un peu partout.){/i}"


  y "Hey Nash, je suis venue pour te parler."
  l @ happy "Oh, ça me fait plaisir ça! De quoi est-ce que tu veux parler ? Je peux te servir du thé, donne moi un instant!" with dissolve
  y "{i}(Oh, il est bizarrement attentionné aujourd'hui...){/i}"
  y "Avec plaisir, cette conversation va être longue..."
  l @ suspicious "Vraiment ? Et pourquoi ?" with dissolve
  menu :
    "Ne l'énervez pas... Choisissez sagement, ou non."
    "C'est à propos de notre relation.":
      show lover angry with dissolve
      l "Y a un problème dans notre relation ?" with vpunch
      y "Ne t'énerve pas s'il te plaît, mais je veux qu'on discute comme les adultes que nous sommes."
    "Le thé est à la menthe ou au citron ?":
      show lover happy with dissolve
      l  "A la menthe et au citron, comme tu l'aimes." with dissolve
      y "Merci bien...Mais faudrait qu'on parle de notre relation..."
    
  "{i}Un silence s'installe dans la chambre, et on peut entendre l'eau du thé bouillir déjà.{/i}"
  "{i}Nash s'empare de deux tasses de thé sales, les rince rapidement et les remplit de thé, puis les pose sur la table qui servait comme bureau.{/i}"

  show lover neutral with dissolve
  l "Alors, de quoi tu voulais parler ...?" 
  y "Nash... Je sais tout. Je suis ta moitié, et je ne pense pas que ça puisse marcher entre nous si tu continues à me traiter comme ça."
  l "Qu'est-ce que j'ai encore fait ?"
  y "COMMENT CA ? Tu as oublié l'épisode de la banque? De l'argent ? Des coups ?" with vpunch
  l @ suspicious "Je ne sais pas de quoi tu parles..." with dissolve
  y "Nash..."
  l "Quoi ?" 
  y "Et les coups du mois passé ? La giffle ? Les menaces d'argent ?"
  l @ angry "Comment ça ? Ce n'est rien du tout! Et puis, tu m'appartiens, pourquoi y a un problème avec l'argent ? On se marriera bientôt, donc..." with dissolve
  y "Nash, je ne peux pas continuer avec toi. Je vais en parler à mes parents et à Sabrina."
  $ renpy.pause(2, hard=True)

  "{i}Un silence, mais cette fois-ci différent, vient engouffrer la chambre dans une ambiance plus que tendu.{/i}"

  y "Nash, je sais que tu prends des drogues. Je le sais, j'ai vu tes yeux à plusieurs  reprises... J'ai essayé de penser que ce n'était pas vrai..."
  show lover angry with dissolve
  y "Que c'était sûrement de la fatigue... Mais j'ai fini par comprendre que c'était une réalité."

  "{i}Nash paraissait perdu. Il était pris d'une panique soudaine à la mention de Sabrina.{/i}"
  "{i}Il savait qu'elle était policière, et que cela pouvait lui causer de gros problèmes.{/i}"
  "{i}Il commence ensuite à me fixer et observer les blessures sur mon visage qu'il m'avait laissés. Elles paraissaient même derrière mon fond de teint.{/i}"
  "{i}Des regrets, de la panique et des remords se sont vite dessinés sur son visage.{/i}"

  
  y "Nash, s'il te plaît... Donne moi des raisons de rester avec toi...Je ne peux plus vivre comme ça. 
  Je suis fatigué de souffrir à cause de tes problèmes avec les drogues. "
  $ renpy.pause(2, hard=True)
  l @ neutral "Je sais...Je veux arrêter de prendre ces drogues, mais c'est plus facile à dire qu'à faire." with dissolve
  y "Je suis là pour toi, mais tu dois être prêt à faire les changements nécessaires pour être en bonne santé."
  l "Je sais, mais j'ai peur. J'ai peur de ne pas réussir et de te décevoir."
  y "Je ne serais jamais déçu de toi. Tu es assez fort pour surmonter cela. Je te soutiendrai à chaque étape du chemin."
  show lover happy with dissolve
  l "Mais comment puis-je être sûr que tu seras toujours là ?"
  y "Je suis ici, avec toi, en ce moment même. Je serai toujours là pour toi, peu importe ce qui se passe."
  l "D'accord, je vais faire un effort pour changer pour le mieux."
  y "Je sais que tu peux le faire. Je suis là pour t'aider."


  scene bg beach with dissolve
  show halfblack with dissolve
  centered "C'est ainsi que leur amour s'est renforcé au fil des années. {p=4.0} \n\n
  Ils ont surmonté les obstacles ensemble et ont construit une vie heureuse basée sur le respect de l'autre et l'amour.  {p=4.0} \n\n
  Chaque jour, ils se réveillaient avec un sourire sur leurs visages, sachant qu'ils étaient là l'un pour l'autre, à travers les bons 
  et les mauvais moments. {p=4.0} \n"
  
  centered "Ils étaient fiers de leur choix d'avoir trouvé un compromis et de s'être soutenus mutuellement pour 
  devenir de meilleures personnes.{p=4.0} \n\n
  Leur amour était la source de leur force et leur bonheur était contagieux pour tous ceux qui les entouraient. {p=4.0} \n\n
  Ils ont vécu heureux pour le restant de leur vie.\n\n"
  hide text with dissolve
  scene black with dissolve
  centered "{font=fonts/JMH Typewriter.ttf}{size=+50}{color=#d1492e}Vous avez trouvé un second équilibre de Nash !  
  {/color}{/size}{/font} {vspace=20}Votre espérance de vie et celle de Nash sont rallongées de 20 ans.\n" 
  with Pause(10.0)
  hide text with fade
  return


label ArgumentAndJustice:
#Transition vers la scène de Justice
  scene black with dissolve
  "{i}Après avoir pris cette décision, vous n'appelez pas votre meilleure amie Sabrina.{/i}"
  "{i}C'est maintenant que les {b}vraies{/b} choses commencent.{/i}"

  centered "Epilogue \n {p=4.0} Regret et Justice."
  hide text with dissolve
  $ renpy.pause(4, hard=True)

  play music "audio/fatal argument theme.mp3" volume 0.3 loop fadein 0.4

  "{i}Vous vous rendez chez Nash afin d'essayer de le confronter.{/i}"
  play sound "<from 4 to 6>audio/door knock.mp3" volume 0.7
  play sound "audio/door open.mp3" volume 0.7
  "La porte s'ouvre et c'est Nash qui apparaît."
  scene bg lover room
  with dissolve

  show lover glad with moveinleft 
  l "Woah! [name_character], quelle belle suprise!"

  y "{i}(Sa maison était délabrée, des journals et de la nourriture étaient éparpillés un peu partout.){/i}"
  y "{i}(Il avait les yeux rouges... Comme s'il venait de prendre des médicaments..){/i}"
  y "{i}(Sa maison était délabrée, des journals et de la nourriture étaient éparpillés un peu partout.){/i}"


  y "Hey Nash, je suis venue pour te parler."
  l @ happy "Oh, ça me fait plaisir ça! De quoi est-ce que tu veux parler ? Je peux te servir du thé, donne moi un instant!" with dissolve
  y "{i}(Oh, il est bizarrement attentionné aujourd'hui...){/i}"
  y "Avec plaisir, cette conversation va être longue..."
  l @ suspicious "Vraiment ? Et pourquoi ?" with dissolve
  menu :
    "Ne l'énervez pas... Choisissez sagement, ou non."
    "C'est à propos de notre relation.":
      show lover angry with dissolve
      l "Y a un problème dans notre relation ?" with vpunch
      y "Ne t'énerve pas s'il te plaît, mais je veux qu'on discute comme les adultes que nous sommes."
    "Le thé est à la menthe ou au citron ?":
      show lover happy with dissolve
      l  "A la menthe et au citron, comme tu l'aimes." with dissolve
      y "Merci bien...Mais faudrait qu'on parle de notre relation..."

  show lover angry with dissolve
  l "Comment ça discuter comme des adultes? De quoi tu veux discuter, dis-moi ?" with vpunch
  y "Et bien, je ne suis pas d'accord avec la façon avec laquelle tu me traites."
  y"Tu me prends tous mon argent, tu me frappes... \n
  Et tu me promets bonheur et mariage, mais je n'ai reçu que violences et tristesse."
  l @ suspicious "Toujours aussi sensible, [name_character]!" with dissolve
  y "Comment !" with vpunch
  l @ glad "Oui! Tu fais toujours ta victime, alors que je n'ai fait que t'emprunter de l'argent!" with dissolve
  y "...{i}(Ce garçon est fou...){/i}"
  y "Nash, si tu n'es pas en mesure d'avoir une conversation normale, je serai obligée de partir..."
  l @ happy "Et alors ? Tu finiras toujours par revenir vers moi, parce que tu m'aimes." with dissolve
  y "NON! J'EN AI VRAIMENT MARRE DE TOI!" with hpunch

  show lover angry with vpunch
  play sound "audio/face punch.mp3" volume 0.7
  "{i}Nash me giffle encore, et cette fois-ci, c'est la dernière fois qu'il le fait.{/i}"

  y "NASH! C'est la dernière fois que tu me vois, tu vas me le payer cher!" with vpunch

  
  scene black with dissolve
  "{i}Je sors en courant de chez lui, ne me sentant plus en sécurité, il essaye de me prendre par le bras, mais je me débats et je fuis.{/i}"
  "{i}Sabrina avait raison... Cet homme était loin d'être un vrai homme...{/i}"
  "{i}Je le lui ferai payer. La Justice le lui fera payer.{/i}"
  hide text with dissolve
  $ renpy.pause(4, hard=True)

  scene bg supreme court 
  with dissolve
  show halfblack with dissolve
  centered "Sabrina finit par vous aider. {p=4.0} \n\n
  Nash est convoqué au commissariat après avoir été sorti de force de sa maison avec l'aide de Sabrina. {p=4.0}
  Elle,qui avait participé à l'arrêt de Nash, avait retrouvé des documents falsifiés ayant pour but de détourner de 
  l'argent de mon compte bancaire.{p=4.0} \n\n
  Après une procédure judiciaire approfondie, l'accusé a été déclaré coupable par le jury en raison de la preuve solide présentée contre lui..{p=4.0} \n\n
  Les avocats ont fait un travail remarquable dans la gestion de l'affaire et ont aidé à faire respecter la justice.{p=4.0}"  

  centered "Vous aviez quand même pris un coup, et votre coeur sera blessé à jamais.{p=4.0} \n\n"
  
  hide text with dissolve
  scene black with dissolve
  centered "{font=fonts/JMH Typewriter.ttf}{size=+50}{color=#d1492e}Vous avez rompu l'équilibre de Nash !  
  {/color}{/size}{/font} {vspace=20}Votre espérance de vie est réduite de 5 ans et celle de Nash de 10 ans qu'il passera en prison.\n" 
  with Pause(10.0)
  hide text with fade
  return




