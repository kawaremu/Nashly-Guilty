label CompromiseTogether:
  #Transition vers la scène de Justice
  scene black with dissolve
  "{i}Après avoir pris cette décision, vous n'appelez pas votre meilleure amie Sabrina.{/i}"
  "{i}C'est maintenant que les {b}vraies{/b} choses commencent.{/i}"

  play music "audio/compromise theme.mp3" volume 0.3 loop fadein 0.4
  
  "{i}Vous vous rendez chez Nash afin d'essayer de le raisonner.{/i}"
  play sound "<from 4 to 6>audio/door knock.mp3" volume 0.7
  play sound "audio/door open.mp3" volume 0.7
  "La porte s'ouvre et c'est Nash qui m'ouvre la porte."
  $wait(5)
  scene bg lover room
  with dissolve

  show lover glad with moveinleft 
  l "Woah! [name_character], quelle belle suprise!"
  # TODO : Finir la conversation et trouver un compromis




  show halfblack with dissolve
  centered "C'est ainsi que leur amour s'est renforcé au fil des années. {p=4.0} \n\n
  Ils ont surmonté les obstacles ensemble et ont construit une vie heureuse basée sur le respect de l'autre et l'amour.  {p=4.0} \n\n
  Chaque jour, ils se réveillaient avec un sourire sur leurs visages, sachant qu'ils étaient là l'un pour l'autre, à travers les bons 
  et les mauvais moments. {p=4.0} \n
  Ils étaient fiers de leur choix d'avoir trouvé un compromis et de s'être soutenus mutuellement pour devenir de meilleures personnes.{p=4.0} \n\n
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
  # TODO : Grosse dispute
  return




