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






label EternalSuffering:
  pass