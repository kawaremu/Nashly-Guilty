label ReportToJustice:
  play music "audio/report justice bgm.mp3" volume 0.3 loop
  y "Je pense que je devrais faire appel à la justice une fois pour toute."
  na"{i}Soudain, des pensées viennent traverser mon esprit.{/i}"
  na"{i}Est-ce que je devrais aller aussi loin pour une simple histoire d'amour ?{/i}"
  na"{i}Est-ce que la justice me soulagera de toutes mes peines ?{/i}"
  na"{i}Je me rappelle alors de toutes mes peines...{p}Des blackmails... Des coups... Des tonnes de fond de teint utilisées pour cacher
  mes blessures à mes parents...{p=1.0}{/i}"
  na"{i}Je suis fatiguée de cette façade. Ce soir, je pleurerai toutes les larmes de mon corps pour rompre l'équilibre de Nash.{/i}"
  na"{i}Je m'enfous de l'équilibre, je veux juste survivre... Et trouver {b}la stratégie gagnante{/b}{/i}."
  #Transition vers la scène de Justice
  scene black with dissolve
  "{i}Après avoir pris cette décision, vous appelez directement votre meilleure amie Sabrina.{/i}"
  y "Sabrina, je suis prête."
  s "Oh, [name_character], je vois que tu as finalement accepté la réalité..."
  y "Oui."
  "{i}C'est maintenant que les {b}vraies{/b} choses commencent.{/i}"
  "{i}Sabrina travaillait dans la police, et moi, qui avais fait des études en droit connaissais déjà à peu près toutes les procédures à entreprendre.{/i}"
  

  scene black with dissolve

  centered "Vous êtes d'abord convoquée au commissariat pour témoigner des harcélemnts subis par votre persécuteur.{p=4.0} \n\n
  Vous racontez tout. Vous pleurez en racontant mais sentez une force grandir en vous.{p=4.0} \n\n
  Nash est convoqué au commissariat après avoir été sorti de force de sa maison avec l'aide de Sabrina."
  hide text with dissolve

  centered "D'après Sabrina qui avait assisté à son témoignage, il n'avait pas nié les violences perpertuées.{p=4.0} \n\n
  Cela vous rappelle à quel point vous avez été douce et naive à son sujet.{p=4.0} \n\n
  Nash est convoqué au commissariat après avoir été sorti de force de sa maison avec l'aide de Sabrina."
  hide text with dissolve

  centered "Mais ce n'est pas grave...Vous vous apprêter à avoir un tournant dans votre vie....{p=4.0} \n\n
  Vous allez rompre l'équilibre de votre vie pour en trouver un autre....{p=4.0}"
  hide text with dissolve
  stop music fadeout 0.7
  centered "Epilogue \n {p=4.0} Que Justice soit faite !"
  hide text with dissolve
  $ renpy.pause(4, hard=True)

  scene bg supreme court 
  with dissolve
  play music "audio/justice court theme.mp3" volume 0.3 loop fadein 0.4
  y "{i}(Aujourd'hui est un grand jour.){/i}"
  y "{i}(C'est le jour qui va changer ma vie...){/i}"
  y "{i}(Nash va être jugé...){/i}"

  play sound "audio/crowd noise court.mp3" volume 0.6
  show judge angry with moveinright
  j "SILENCE!" with hpunch
  stop sound fadeout 1
  $wait(2)  
  j @ annoyed "Très bien.Nous pouvons commencer." with dissolve
  j @angry "Vous pouvez faire entrer l'accusé." with dissolve

  show judge neutral at left 
  with move
  pause(1.5)

  # Faire entrer l'accusé
  show lover angry at left:
    subpixel True xzoom 1 pos (0.53, 1.6) zoom 0.93
  with moveinright

  l "..." 
  y "{i}(Oh... Il a l'air furieux.){/i}"
  j @ happy "Bonjour et bienvenue dans ce tribunal. Vous êtes ici pour répondre d'harcélements répétés, menaces et violences sur la victime ici 
  présente ; [name_character]. Pouvez-vous vous identifier pour la cour ?" with dissolve
  l @ neutral "Oui, Je m'appelle John Nash." with dissolve
  j "Très bien, John Nash. La victime ici présente, [name_character] accuse que vous lui avez pris une grande somme d'argent à une banque en utilisant 
  la violence. Est-ce vrai ?" with dissolve 
  l @ angry "Je nie ces accusations, Votre Honneur." with dissolve
  j @ angry "C'est à la cour de déterminer la vérité. Le procès débute maintenant, et nous entendrons les témoignages et les preuves pour 
  arriver à une décision équitable." with dissolve

  play sound "audio/crowd noise court.mp3" volume 0.6
  show judge angry with dissolve 
  j "SILENCE!" with hpunch
  stop sound fadeout 1

  scene black with dissolve

  centered "Les avocats dans l'affaire ont travaillé dur pour rassembler des preuves et des témoignages pour soutenir leur argumentation.{p=4.0} \n\n
  Ils ont fait des plaidoyers convaincants devant le juge et le jury, présentant les faits de l'affaire de manière claire et concise. {p=4.0} \n\n"
  hide text with dissolve

  centered "Sabrina, qui avait participé à l'arrêt de Nash, avait retrouvé des documents falsifiés ayant pour but de détourner de 
  l'argent de mon compte bancaire.{p=4.0} \n\n
  Après une procédure judiciaire approfondie, l'accusé a été déclaré coupable par le jury en raison de la preuve solide présentée contre lui..{p=4.0} \n\n
  Les avocats ont fait un travail remarquable dans la gestion de l'affaire et ont aidé à faire respecter la justice."
  hide text with dissolve

  centered "{font=fonts/JMH Typewriter.ttf}{size=+50}{color=#d1492e}Equilibre de Nash retrouvé! (+20,-10){/color}{/size}{/font}
  {vspace=20}Votre espérance de vie est rallongée de 20 ans et celle de Nash réduite de 10 ans qu'il passe en prison.\n\n"
  hide text with dissolve
  return

  #Here the game ends with the first ending. (With a nash equilibrium)

label EternalSuffering:
  play music "audio/eternal suffering theme.mp3" volume 0.3 loop fadein 0.4
  y "Je ne pas pense que je devrais faire appel à la justice pour ce problème, ça n'en vaut pas du tout la peine..."
  na"{i}Soudain, des pensées viennent traverser mon esprit.{/i}"
  na"{i}Est-ce que je devrais aller aussi loin pour une simple histoire d'amour ?{/i}"
  na"{i}Est-ce que la justice me soulagera de toutes mes peines ?{/i}"
  na"{i}Je me rappelle alors de toutes mes peines...{p}Des blackmails... Des coups... Des tonnes de fond de teint utilisées pour cacher
  mes blessures à mes parents...{p=1.0}{/i}"
  na"{i}Je suis fatiguée de cette façade. Ce soir, je pleurerai toutes les larmes de mon corps pour rompre l'équilibre de Nash.{/i}"
  na"{i}Mais Nash vit seul.. Ses deux parents sont morts. Il n a pas d'argent...{/i}"
  na"{i}Je ne devrais pas le laisser tomber...{/i}"
  na"{i}Je veux garder cette harmonie et cet équilibre qui existe entre lui et moi...
  Je veux juste rester à ses côtés...{/i}."

  #Transition vers la scène finale de regret
  scene black with dissolve
  "{i}Après avoir pris cette décision, vous n'appelez pas votre meilleure amie.{/i}"
  centered "Epilogue \n {p=4.0} Souffrance éternelle."
  hide text with dissolve
  $ renpy.pause(4, hard=True)
  scene bg living room
  with dissolve
  centered "Des années se sont écoulées et le temps a laissé son empreinte sur le visage de [name_character]. 
  Elle est seule dans sa chambre, se rappelant les jours où elle était amoureuse de l'homme parfait à ses yeux. {p=4.0} \n\n
  Elle avait tout donné pour lui, lui offrant tout ce qu'il désirait, faisant confiance aveuglement à un homme qui s'est révélé être toxique et manipulateur. {p=4.0} \n
  Elle a enduré des années de souffrance et de regrets, se demandant pourquoi elle n'a jamais rassemblé le courage de le quitter ou de le dénoncer à la police.\n\n
  Maintenant, à l'aube de la trentaine, elle se sent seule même aux côtés de Nash, malade, et avec une espérance de vie réduite.Ayant pour seuls compagnons ses pensées et ses regrets. 
  Elle se demande souvent ce qui aurait pu être si elle avait pris une autre décision."
  hide text with dissolve
  scene black with dissolve
  centered "{font=fonts/JMH Typewriter.ttf}{size=+50}{color=#d1492e}Vous pensiez vraiment avoir trouvé l'équilibre de Nash ? 
  {/color}{/size}{/font} {vspace=20}Votre espérance de vie est réduite de 20 ans,Nash échappe à la Justice et vit 10 ans de plus que vous.\n" 
  with Pause(10.0)
  hide text with fade
  return