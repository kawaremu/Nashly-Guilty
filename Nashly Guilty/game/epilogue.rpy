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
  stop music fadeout 0.7


  # Transition vers la scène de Justice
  # TODO : - ajouter des détails sur la transition, ce qu'a fait Sabrina etc...
  scene black with dissolve
  with Pause(1)
  show text "Vous vous apprêter à avoir un tournant dans votre vie..." with dissolve
  with Pause(2)
  show text "Vous allez rompre l'équilibre de votre vie pour en trouver un autre..." with dissolve
  with Pause(2)
  hide text with dissolve
  with Pause(5)

  

  scene bg supreme court with dissolve
  play music "audio/justice court theme.mp3" volume 0.3 loop
  "Aujourd'hui est un grand jour."

 









label EternalSuffering:
  pass