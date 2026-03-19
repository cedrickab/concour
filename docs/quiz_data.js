// Quiz Data - 493 questions

const THEME_1 = [
  {
    "question": "Quel est le synonyme du mot « fugace » ?",
    "options": [
      "A) Permanent",
      "B) Éphémère",
      "C) Rapide",
      "D) Durable"
    ],
    "answer": "B",
    "explanation": "« Fugace » signifie éphémère, qui dure peu de temps."
  },
  {
    "question": "Quel mot est l'antonyme de « prospère » ?",
    "options": [
      "A) Florissant",
      "B) Misérable",
      "C) Riche",
      "D) Opulent"
    ],
    "answer": "B",
    "explanation": "« Misérable » est le contraire de « prospère » (qui réussit bien)."
  },
  {
    "question": "Complétez : « Il est arrivé …… faute ! »",
    "options": [
      "A) sans",
      "B) sang",
      "C) cent",
      "D) sens"
    ],
    "answer": "A",
    "explanation": "« Sans » (sans faute) est la préposition correcte dans ce contexte."
  },
  {
    "question": "Quel est le genre du mot « armistice » ?",
    "options": [
      "A) Féminin",
      "B) Masculin",
      "C) Les deux"
    ],
    "answer": "B",
    "explanation": "« Armistice » est un nom masculin : un armistice."
  },
  {
    "question": "Quelle expression est correcte ?",
    "options": [
      "A) Je vous saurai gré",
      "B) Je vous saurais gré",
      "C) Je vous serais gré"
    ],
    "answer": "A",
    "explanation": "L'expression correcte est « Je vous saurai gré » (futur simple)."
  },
  {
    "question": "Quel mot n'appartient pas à la même famille ?",
    "options": [
      "A) Terroir",
      "B) Territoire",
      "C) Terreur",
      "D) Terrain"
    ],
    "answer": "C",
    "explanation": "« Terreur » vient du latin « terror » tandis que les autres viennent de « terra » (terre)."
  },
  {
    "question": "Trouvez le mot mal orthographié :",
    "options": [
      "A) Aréopage",
      "B) Anathème",
      "C) Apotheose",
      "D) Acrobate"
    ],
    "answer": "C",
    "explanation": "L'orthographe correcte est « apothéose » avec un accent aigu."
  },
  {
    "question": "Quel mot est l'antonyme de « prolixe » ?",
    "options": [
      "A) Concis",
      "B) Verbeux",
      "C) Bavard",
      "D) Éloquent"
    ],
    "answer": "A",
    "explanation": "« Prolixe » signifie bavard, son antonyme est « concis » (bref)."
  },
  {
    "question": "Quel pluriel est correct ?",
    "options": [
      "A) des cache-nez",
      "B) des cache-nezs",
      "C) des caches-nez"
    ],
    "answer": "A",
    "explanation": "Les noms composés avec « cache » restent invariables : des cache-nez."
  },
  {
    "question": "Quelle phrase ne contient pas de pléonasme ?",
    "options": [
      "A) Monter en haut",
      "B) Prévoir à l'avance",
      "C) Répéter encore",
      "D) Examiner attentivement"
    ],
    "answer": "D",
    "explanation": "« Examiner attentivement » n'est pas redondant, contrairement aux autres."
  },
  {
    "question": "Trouvez l'orthographe correcte :",
    "options": [
      "A) Dilemme",
      "B) Dilème",
      "C) Dilemne",
      "D) Dilenne"
    ],
    "answer": "A",
    "explanation": "Le mot s'écrit « dilemme » avec deux m."
  },
  {
    "question": "Quel verbe se construit avec « de » ?",
    "options": [
      "A) Pallier",
      "B) Remédier",
      "C) Suppléer",
      "D) Obvier"
    ],
    "answer": "B",
    "explanation": "On dit « remédier à » et non « remédier de ». « Pallier » se construit sans préposition."
  },
  {
    "question": "Quelle est la nature du mot « Épuisé » dans : « Épuisé, l'athlète abandonne » ?",
    "options": [
      "A) Adjectif qualificatif",
      "B) Participe passé épithète",
      "C) Participe passé en apposition"
    ],
    "answer": "C",
    "explanation": "« Épuisé » est un participe passé mis en apposition (détaché par une virgule)."
  },
  {
    "question": "Quelle est la définition de « l'emphase » ?",
    "options": [
      "A) Un style exagéré",
      "B) La discrétion",
      "C) La clarté",
      "D) La concision"
    ],
    "answer": "A",
    "explanation": "L'emphase est un ton, un style emphatique, exagéré et pompeux."
  },
  {
    "question": "Quel mot désigne une personne qui mange de tout ?",
    "options": [
      "A) Herbivore",
      "B) Carnivore",
      "C) Omnivore",
      "D) Frugivore"
    ],
    "answer": "C",
    "explanation": "« Omnivore » désigne un être qui se nourrit de tout (végétaux et animaux)."
  },
  {
    "question": "Que signifie le sigle « ONU » ?",
    "options": [
      "A) Organisation des Nations Unies",
      "B) Office des Nations Unies",
      "C) Ordre des Nations Unies",
      "D) Organe des Nations Unies"
    ],
    "answer": "A",
    "explanation": "ONU signifie Organisation des Nations Unies."
  },
  {
    "question": "Quel est l'antonyme de « appareiller » ?",
    "options": [
      "A) Accoster",
      "B) Fusionner",
      "C) Apprêter",
      "D) Partir"
    ],
    "answer": "A",
    "explanation": "« Appareiller » signifie partir (pour un navire), son antonyme est « accoster » (arriver)."
  },
  {
    "question": "Une personne « dégingandée » est une personne :",
    "options": [
      "A) Élégante",
      "B) Ayant une démarche disloquée",
      "C) Timide",
      "D) Intelligente"
    ],
    "answer": "B",
    "explanation": "« Dégingandée » qualifie une personne ayant des mouvements maladroits et une démarche disloquée."
  },
  {
    "question": "Quel dessert tire son nom d'une femme célèbre ?",
    "options": [
      "A) Tiramisu",
      "B) Pavlova",
      "C) Macaron",
      "D) Éclair"
    ],
    "answer": "B",
    "explanation": "La Pavlova est nommée d'après la ballerine russe Anna Pavlova."
  },
  {
    "question": "Quel est le genre du mot « haltère » ?",
    "options": [
      "A) Féminin",
      "B) Masculin",
      "C) Les deux"
    ],
    "answer": "B",
    "explanation": "« Haltère » est masculin : un haltère."
  },
  {
    "question": "Quel mot n'appartient pas à la même famille que les autres ?",
    "options": [
      "A) Fable",
      "B) Fabuleux",
      "C) Affable",
      "D) Fabulation"
    ],
    "answer": "C",
    "explanation": "« Affable » vient du latin « affabilis » (courtois), tandis que les autres viennent de « fabula » (récit)."
  },
  {
    "question": "Quelle relation n'existe pas (nature-adjectif) ?",
    "options": [
      "A) Eau-aquatique",
      "B) Église-ecclésiastique",
      "C) Humilité-modestie"
    ],
    "answer": "C",
    "explanation": "« Humilité » et « modestie » sont deux noms, pas une relation nature-adjectif."
  },
  {
    "question": "Quel est l'antonyme du mot « truculent » ?",
    "options": [
      "A) Succulent",
      "B) Original",
      "C) Commun",
      "D) Savoureux"
    ],
    "answer": "C",
    "explanation": "« Truculent » signifie haut en couleur, pittoresque ; son antonyme est « commun » (banal)."
  },
  {
    "question": "Trouvez l'intrus :",
    "options": [
      "A) Le Souverain Pontife",
      "B) Le Saint-Père",
      "C) La Bible",
      "D) Le Pape"
    ],
    "answer": "C",
    "explanation": "Les trois autres désignent le Pape, la Bible est un livre sacré."
  },
  {
    "question": "Quel est l'antonyme du mot « pingre » ?",
    "options": [
      "A) Robuste",
      "B) Radin",
      "C) Généreux",
      "D) Avare"
    ],
    "answer": "C",
    "explanation": "« Pingre » signifie avare, son antonyme est « généreux »."
  },
  {
    "question": "Quel pluriel est correct ?",
    "options": [
      "A) Des arcs-en-ciels",
      "B) Des passes-partout",
      "C) Des avant-premières",
      "D) Tous sont corrects"
    ],
    "answer": "C",
    "explanation": "« Des avant-premières » est correct. « Arcs-en-ciel » et « passe-partout » restent invariables."
  },
  {
    "question": "Dans quelle phrase n'y a-t-il pas de pléonasme ?",
    "options": [
      "A) Le jeune lavandier travaille dans la laverie",
      "B) Pour la police, c'est un petit détail",
      "C) Ils vont tous se rencontrer ensemble"
    ],
    "answer": "B",
    "explanation": "Cette phrase n'a pas de redondance, contrairement aux autres."
  },
  {
    "question": "Trouvez l'orthographe correcte :",
    "options": [
      "A) Pérégrination",
      "B) Pirégrination",
      "C) Perigrination",
      "D) Pérégrinassion"
    ],
    "answer": "A",
    "explanation": "Le mot correct est « pérégrination » (voyage lointain)."
  },
  {
    "question": "Quel complément convient au verbe « luter » ?",
    "options": [
      "A) Une fissure",
      "B) Un vase",
      "C) Un trou",
      "D) Une fenêtre"
    ],
    "answer": "B",
    "explanation": "« Luter » signifie boucher hermétiquement avec du lut (mastic). On lute un vase."
  },
  {
    "question": "Quel mot n'appartient pas à la même famille ?",
    "options": [
      "A) Ingénieur",
      "B) Géniteur",
      "C) Genèse",
      "D) Génération"
    ],
    "answer": "A",
    "explanation": "« Ingénieur » vient de « ingenium » (talent), les autres de « genesis » (naissance)."
  },
  {
    "question": "Quelle est la définition de la « rhétorique » ?",
    "options": [
      "A) L'analyse de textes",
      "B) L'étude de la religion",
      "C) L'art du discours",
      "D) La grammaire"
    ],
    "answer": "C",
    "explanation": "La rhétorique est l'art du discours et de l'éloquence."
  },
  {
    "question": "Quel mot désigne un amour excessif de soi-même ?",
    "options": [
      "A) Égoïsme",
      "B) Narcissisme",
      "C) Orgueil",
      "D) Vanité"
    ],
    "answer": "B",
    "explanation": "Le narcissisme désigne un amour excessif de sa propre personne."
  },
  {
    "question": "Quel est le féminin de « empereur » ?",
    "options": [
      "A) Empereure",
      "B) Impératrice",
      "C) Empératrice",
      "D) Emperesse"
    ],
    "answer": "B",
    "explanation": "Le féminin d'empereur est impératrice."
  },
  {
    "question": "Que signifie « ubiquité » ?",
    "options": [
      "A) Rapidité",
      "B) Capacité d'être partout",
      "C) Solitude",
      "D) Clarté"
    ],
    "answer": "B",
    "explanation": "L'ubiquité est la capacité d'être présent partout à la fois."
  },
  {
    "question": "Quel mot désigne la peur des espaces clos ?",
    "options": [
      "A) Agoraphobie",
      "B) Claustrophobie",
      "C) Acrophobie",
      "D) Hydrophobie"
    ],
    "answer": "B",
    "explanation": "La claustrophobie est la peur des espaces fermés."
  },
  {
    "question": "Complétez : « Il a fait cela de son propre …… »",
    "options": [
      "A) chef",
      "B) chèque",
      "C) chaire",
      "D) cher"
    ],
    "answer": "A",
    "explanation": "L'expression est « de son propre chef » (de sa propre initiative)."
  },
  {
    "question": "Quel mot désigne l'art de bien manger ?",
    "options": [
      "A) Gastrologie",
      "B) Gastronomie",
      "C) Gastrosophie",
      "D) Gastromancie"
    ],
    "answer": "B",
    "explanation": "La gastronomie est l'art de bien manger et de bien cuisiner."
  },
  {
    "question": "Quelle est l'origine du mot « bibliothèque » ?",
    "options": [
      "A) Latin",
      "B) Grec",
      "C) Arabe",
      "D) Sanskrit"
    ],
    "answer": "B",
    "explanation": "« Bibliothèque » vient du grec « biblion » (livre) et « thêkê » (lieu de rangement)."
  },
  {
    "question": "Quel adjectif qualifie quelqu'un qui parle plusieurs langues ?",
    "options": [
      "A) Multilingue",
      "B) Polyglotte",
      "C) Bilingue",
      "D) Tous sont corrects"
    ],
    "answer": "B",
    "explanation": "« Polyglotte » qualifie spécifiquement quelqu'un qui parle plusieurs langues."
  },
  {
    "question": "Que signifie le sigle « HLM » ?",
    "options": [
      "A) Habitation de longueur moyenne",
      "B) Habitation à loyer modéré",
      "C) Habitation de location moderne",
      "D) Hôtel de luxe moderne"
    ],
    "answer": "B",
    "explanation": "HLM signifie Habitation à Loyer Modéré."
  },
  {
    "question": "Quel est le genre du mot « alvéole » ?",
    "options": [
      "A) Féminin",
      "B) Masculin",
      "C) Les deux sont acceptés"
    ],
    "answer": "C",
    "explanation": "« Alvéole » est traditionnellement féminin mais le masculin est aussi admis par l'Académie française."
  },
  {
    "question": "Quelle figure de style consiste à dire le contraire de ce que l'on pense ?",
    "options": [
      "A) Litote",
      "B) Antiphrase",
      "C) Euphémisme",
      "D) Oxymore"
    ],
    "answer": "B",
    "explanation": "L'antiphrase consiste à dire le contraire de ce que l'on veut faire comprendre, souvent avec ironie."
  },
  {
    "question": "Quelle figure de style associe deux termes contradictoires ?",
    "options": [
      "A) Métaphore",
      "B) Oxymore",
      "C) Antithèse",
      "D) Chiasme"
    ],
    "answer": "B",
    "explanation": "L'oxymore unit deux termes de sens opposé. Ex : « un silence assourdissant »."
  },
  {
    "question": "Comment appelle-t-on un mot qui a une forme identique au masculin et au féminin ?",
    "options": [
      "A) Homonyme",
      "B) Épicène",
      "C) Polymorphe",
      "D) Androgyne"
    ],
    "answer": "B",
    "explanation": "Un mot épicène a la même forme pour les deux genres. Ex : « un/une artiste »."
  },
  {
    "question": "Quel est l'adjectif verbal du verbe « naviguer » ?",
    "options": [
      "A) Naviguant",
      "B) Navigant",
      "C) Naviguent"
    ],
    "answer": "B",
    "explanation": "L'adjectif verbal est « navigant » (variable) ; le participe présent est « naviguant » (invariable)."
  },
  {
    "question": "Quelle est l'orthographe correcte ?",
    "options": [
      "A) Echappatoire",
      "B) Échapattoire",
      "C) Échappatoire",
      "D) Échapatoire"
    ],
    "answer": "C",
    "explanation": "Le mot s'écrit « échappatoire » avec deux p."
  },
  {
    "question": "Quel mode utilise-t-on après la conjonction « Bien que » ?",
    "options": [
      "A) L'indicatif",
      "B) Le subjonctif",
      "C) Le conditionnel",
      "D) L'impératif"
    ],
    "answer": "B",
    "explanation": "« Bien que » est toujours suivi du subjonctif."
  },
  {
    "question": "Laquelle de ces phrases est correcte ?",
    "options": [
      "A) Après qu'il soit venu",
      "B) Après qu'il est venu",
      "C) Après qu'il ait venu"
    ],
    "answer": "B",
    "explanation": "« Après que » est suivi de l'indicatif (contrairement à « avant que » qui prend le subjonctif)."
  },
  {
    "question": "Comment s'accorde l'adjectif de couleur « orange » ?",
    "options": [
      "A) Il s'accorde normalement",
      "B) Il reste invariable",
      "C) Il ne s'accorde qu'au pluriel"
    ],
    "answer": "B",
    "explanation": "Les adjectifs de couleur issus de noms (orange, marron, crème…) sont invariables."
  },
  {
    "question": "Que signifie le sigle « PIB » ?",
    "options": [
      "A) Produit Intérieur Budgétaire",
      "B) Produit Intérieur Brut",
      "C) Plan d'Investissement Bancaire",
      "D) Programme d'Intervention Budgétaire"
    ],
    "answer": "B",
    "explanation": "PIB signifie Produit Intérieur Brut, indicateur de la richesse d'un pays."
  },
  {
    "question": "Quelle est la bonne orthographe ?",
    "options": [
      "A) Aceuillir",
      "B) Accueillir",
      "C) Acceuillir",
      "D) Accueuillir"
    ],
    "answer": "B",
    "explanation": "Le mot s'écrit « accueillir » (c-c-u-e-i-l-l-i-r)."
  },
  {
    "question": "Quelle figure de style consiste à remplacer un terme par une expression plus douce ?",
    "options": [
      "A) Hyperbole",
      "B) Litote",
      "C) Euphémisme",
      "D) Antiphrase"
    ],
    "answer": "C",
    "explanation": "L'euphémisme adoucit une réalité. Ex : « il nous a quittés » pour « il est mort »."
  },
  {
    "question": "Quelle figure de style consiste à désigner un tout par une de ses parties ?",
    "options": [
      "A) Métonymie",
      "B) Synecdoque",
      "C) Périphrase",
      "D) Allégorie"
    ],
    "answer": "B",
    "explanation": "La synecdoque prend la partie pour le tout. Ex : « les voiles » pour désigner les bateaux."
  },
  {
    "question": "Quelle est la définition d'une « périphrase » ?",
    "options": [
      "A) Dire le contraire de ce qu'on pense",
      "B) Utiliser plusieurs mots pour un seul",
      "C) Exagérer volontairement",
      "D) Comparer deux éléments"
    ],
    "answer": "B",
    "explanation": "La périphrase remplace un mot par une expression. Ex : « l'astre du jour » pour « le soleil »."
  },
  {
    "question": "Quel est le genre du mot « tentacule » ?",
    "options": [
      "A) Féminin",
      "B) Masculin",
      "C) Les deux"
    ],
    "answer": "B",
    "explanation": "« Tentacule » est masculin : un tentacule."
  },
  {
    "question": "Quel est le genre du mot « obélisque » ?",
    "options": [
      "A) Féminin",
      "B) Masculin",
      "C) Les deux"
    ],
    "answer": "B",
    "explanation": "« Obélisque » est masculin : un obélisque."
  },
  {
    "question": "Que signifie l'expression « faire long feu » ?",
    "options": [
      "A) Durer longtemps",
      "B) Échouer, ne pas aboutir",
      "C) Provoquer un grand incendie"
    ],
    "answer": "B",
    "explanation": "« Faire long feu » signifie ne pas aboutir, échouer (et non durer longtemps)."
  },
  {
    "question": "Quel mot désigne la peur du nombre 13 ?",
    "options": [
      "A) Arachnophobie",
      "B) Triskaïdékaphobie",
      "C) Nyctophobie",
      "D) Agoraphobie"
    ],
    "answer": "B",
    "explanation": "La triskaïdékaphobie est la phobie du nombre 13."
  },
  {
    "question": "Comment s'écrit 80 en lettres ?",
    "options": [
      "A) Quatre-vingt",
      "B) Quatre-vingts",
      "C) Quatres-vingts",
      "D) Quatres-vingt"
    ],
    "answer": "B",
    "explanation": "On écrit « quatre-vingts » avec un s quand il n'est pas suivi d'un autre nombre."
  },
  {
    "question": "« Il n'est pas mécontent » pour dire qu'il est ravi est une :",
    "options": [
      "A) Hyperbole",
      "B) Litote",
      "C) Antiphrase",
      "D) Métonymie"
    ],
    "answer": "B",
    "explanation": "La litote dit moins pour suggérer plus (double négation atténuante)."
  },
  {
    "question": "« La diplomatie est le bras armé de la politique » est une :",
    "options": [
      "A) Métaphore",
      "B) Comparaison",
      "C) Métonymie",
      "D) Synecdoque"
    ],
    "answer": "A",
    "explanation": "C'est une métaphore car il y a identification directe sans mot de comparaison."
  },
  {
    "question": "Quel mot désigne l'étude des noms propres ?",
    "options": [
      "A) Onomastique",
      "B) Toponymie",
      "C) Lexicologie",
      "D) Philologie"
    ],
    "answer": "A",
    "explanation": "L'onomastique est l'étude des noms propres (personnes et lieux)."
  },
  {
    "question": "Quel est le contraire de « véhément » ?",
    "options": [
      "A) Violent",
      "B) Calme",
      "C) Passionné",
      "D) Fougueux"
    ],
    "answer": "B",
    "explanation": "« Véhément » signifie ardent, impétueux ; son contraire est « calme »."
  },
  {
    "question": "Conjuguez : « Il faut que je …… ce travail avant demain. »",
    "options": [
      "A) finis",
      "B) finisse",
      "C) finirai",
      "D) finirais"
    ],
    "answer": "B",
    "explanation": "Après « il faut que », on utilise le subjonctif présent : « que je finisse »."
  },
  {
    "question": "Quel est le genre du mot « pétale » ?",
    "options": [
      "A) Féminin",
      "B) Masculin",
      "C) Les deux"
    ],
    "answer": "B",
    "explanation": "« Pétale » est masculin : un pétale."
  },
  {
    "question": "Quel est le genre du mot « apostrophe » ?",
    "options": [
      "A) Féminin",
      "B) Masculin",
      "C) Les deux"
    ],
    "answer": "A",
    "explanation": "« Apostrophe » est féminin : une apostrophe."
  },
  {
    "question": "Que signifie l'expression « avoir maille à partir » ?",
    "options": [
      "A) Avoir beaucoup d'argent",
      "B) Avoir un différend avec quelqu'un",
      "C) Devoir partager",
      "D) Être pressé"
    ],
    "answer": "B",
    "explanation": "« Avoir maille à partir » signifie avoir un conflit, un désaccord avec quelqu'un."
  },
  {
    "question": "Quel mot désigne un discours prononcé en l'honneur d'un défunt ?",
    "options": [
      "A) Panégyrique",
      "B) Oraison funèbre",
      "C) Réquisitoire",
      "D) Plaidoyer"
    ],
    "answer": "B",
    "explanation": "L'oraison funèbre est un discours d'hommage prononcé lors des funérailles."
  },
  {
    "question": "Que signifie le sigle « BEPC » ?",
    "options": [
      "A) Brevet d'Études du Premier Cycle",
      "B) Bureau d'Études des Programmes Communs",
      "C) Bilan d'Évaluation Professionnelle Continu"
    ],
    "answer": "A",
    "explanation": "BEPC signifie Brevet d'Études du Premier Cycle."
  },
  {
    "question": "Complétez : « Ces fleurs, je les ai …… »",
    "options": [
      "A) cueilli",
      "B) cueillie",
      "C) cueillies",
      "D) cueillis"
    ],
    "answer": "C",
    "explanation": "Le participe passé s'accorde avec le COD « les » (= fleurs, féminin pluriel) placé avant."
  },
  {
    "question": "Quel verbe est correctement conjugué au passé simple ?",
    "options": [
      "A) Il prena",
      "B) Il prit",
      "C) Il prenna",
      "D) Il prendit"
    ],
    "answer": "B",
    "explanation": "Le passé simple de « prendre » à la 3e personne est « il prit »."
  },
  {
    "question": "Quel mot désigne la science du droit ?",
    "options": [
      "A) Jurisprudence",
      "B) Juridiction",
      "C) Droit",
      "D) Jurisconsulte"
    ],
    "answer": "A",
    "explanation": "La jurisprudence est l'ensemble des décisions de justice et la science du droit."
  },
  {
    "question": "Que signifie « apocryphe » ?",
    "options": [
      "A) Authentique",
      "B) D'authenticité douteuse",
      "C) Ancien",
      "D) Sacré"
    ],
    "answer": "B",
    "explanation": "Un texte apocryphe est un écrit dont l'authenticité est contestée."
  },
  {
    "question": "Quel est le genre du mot « effluve » ?",
    "options": [
      "A) Féminin",
      "B) Masculin",
      "C) Les deux"
    ],
    "answer": "B",
    "explanation": "« Effluve » est masculin : un effluve."
  },
  {
    "question": "Que signifie « inique » ?",
    "options": [
      "A) Juste",
      "B) Injuste",
      "C) Unique",
      "D) Inutile"
    ],
    "answer": "B",
    "explanation": "« Inique » signifie injuste, contraire à l'équité."
  },
  {
    "question": "Quel proverbe signifie qu'il faut être discret sur ses projets ?",
    "options": [
      "A) Pierre qui roule n'amasse pas mousse",
      "B) Pour vivre heureux, vivons cachés",
      "C) Qui sème le vent récolte la tempête"
    ],
    "answer": "B",
    "explanation": "« Pour vivre heureux, vivons cachés » signifie qu'il faut rester discret."
  },
  {
    "question": "Que signifie « obtempérer » ?",
    "options": [
      "A) Refuser",
      "B) Obéir",
      "C) Hésiter",
      "D) Demander"
    ],
    "answer": "B",
    "explanation": "« Obtempérer » signifie obéir, se soumettre à un ordre."
  },
  {
    "question": "Quel est le genre du mot « encaustique » ?",
    "options": [
      "A) Féminin",
      "B) Masculin",
      "C) Les deux"
    ],
    "answer": "A",
    "explanation": "« Encaustique » est féminin : une encaustique."
  },
  {
    "question": "Quelle est la bonne orthographe ?",
    "options": [
      "A) Imbécilité",
      "B) Imbécillité",
      "C) Imbésilité",
      "D) Imbescilité"
    ],
    "answer": "A",
    "explanation": "Depuis la réforme de 1990, « imbécilité » s'écrit avec un seul l (anciennement deux)."
  },
  {
    "question": "Quelle est la bonne orthographe ?",
    "options": [
      "A) Acolade",
      "B) Accollade",
      "C) Accolade",
      "D) Acollade"
    ],
    "answer": "C",
    "explanation": "Le mot s'écrit « accolade » avec deux c et un seul l."
  },
  {
    "question": "Que signifie « promulguer une loi » ?",
    "options": [
      "A) Proposer une loi",
      "B) Rendre une loi officielle et applicable",
      "C) Abroger une loi",
      "D) Modifier une loi"
    ],
    "answer": "B",
    "explanation": "Promulguer une loi, c'est la rendre officiellement applicable par décret du président."
  },
  {
    "question": "Quel mot désigne un gouvernement dirigé par un petit nombre de personnes ?",
    "options": [
      "A) Démocratie",
      "B) Oligarchie",
      "C) Monarchie",
      "D) Théocratie"
    ],
    "answer": "B",
    "explanation": "L'oligarchie est un régime où le pouvoir est entre les mains d'un petit groupe."
  },
  {
    "question": "Quel est le sens de « philantrope » ?",
    "options": [
      "A) Qui déteste l'humanité",
      "B) Qui aime l'humanité",
      "C) Qui collectionne les timbres",
      "D) Qui étudie les plantes"
    ],
    "answer": "B",
    "explanation": "Un philanthrope (du grec philos = ami + anthropos = homme) aime l'humanité et agit pour son bien."
  },
  {
    "question": "Complétez : « Quoiqu'il …… riche, il reste modeste. »",
    "options": [
      "A) est",
      "B) soit",
      "C) serait",
      "D) sera"
    ],
    "answer": "B",
    "explanation": "« Quoique » (= bien que) est suivi du subjonctif : « quoiqu'il soit »."
  },
  {
    "question": "Que signifie « abroger » ?",
    "options": [
      "A) Annuler une loi",
      "B) Publier une loi",
      "C) Modifier une loi",
      "D) Appliquer une loi"
    ],
    "answer": "A",
    "explanation": "Abroger signifie supprimer, annuler une loi ou un décret."
  },
  {
    "question": "Quel est le contraire de « pléthorique » ?",
    "options": [
      "A) Abondant",
      "B) Insuffisant",
      "C) Excessif",
      "D) Immense"
    ],
    "answer": "B",
    "explanation": "« Pléthorique » signifie en excès, surabondant ; son contraire est « insuffisant »."
  },
  {
    "question": "Que signifie « un arrêté » en droit administratif ?",
    "options": [
      "A) Une décision de justice",
      "B) Un acte administratif d'une autorité",
      "C) Un projet de loi",
      "D) Un discours officiel"
    ],
    "answer": "B",
    "explanation": "Un arrêté est un acte administratif pris par un ministre, un préfet ou un maire."
  }
];

const THEME_2 = [
  {
    "question": "Les mots « saut », « seau » et « sot » sont des :",
    "options": [
      "A) Paronymes",
      "B) Homographes",
      "C) Homophones",
      "D) Antonymes"
    ],
    "answer": "C",
    "explanation": "Ces mots se prononcent de la même façon mais s'écrivent différemment : ce sont des homophones."
  },
  {
    "question": "La relation entre « rose » et « fleur » est une :",
    "options": [
      "A) Synonymie",
      "B) Hyponymie",
      "C) Antonymie",
      "D) Méronymie"
    ],
    "answer": "B",
    "explanation": "« Rose » est un hyponyme de « fleur » (terme plus général, l'hyperonyme)."
  },
  {
    "question": "Le mot « Ressasser » est un exemple de :",
    "options": [
      "A) Anagramme",
      "B) Palindrome",
      "C) Homonyme",
      "D) Paronyme"
    ],
    "answer": "B",
    "explanation": "« Ressasser » se lit dans les deux sens, c'est un palindrome."
  },
  {
    "question": "Les mots « éminent » et « imminent » sont des :",
    "options": [
      "A) Synonymes",
      "B) Homographes",
      "C) Paronymes",
      "D) Antonymes"
    ],
    "answer": "C",
    "explanation": "Ces mots se ressemblent fortement mais ont des sens différents : ce sont des paronymes."
  },
  {
    "question": "Dans les expressions « avoir du cœur » et « le cœur bat », « cœur » illustre :",
    "options": [
      "A) Homonymie",
      "B) Polysémie",
      "C) Méronymie",
      "D) Synonymie"
    ],
    "answer": "B",
    "explanation": "Un même mot avec plusieurs sens liés illustre la polysémie."
  },
  {
    "question": "« Marie » et « aimer » sont des :",
    "options": [
      "A) Palindromes",
      "B) Homophones",
      "C) Anagrammes",
      "D) Synonymes"
    ],
    "answer": "C",
    "explanation": "Les mêmes lettres réorganisées forment des anagrammes."
  },
  {
    "question": "« Grand » et « petit » sont des :",
    "options": [
      "A) Antonymes",
      "B) Homonymes",
      "C) Hyponymes",
      "D) Paronymes"
    ],
    "answer": "A",
    "explanation": "Ces mots ont des sens opposés : ce sont des antonymes."
  },
  {
    "question": "« Touche » est le méronyme de « clavier ». La méronymie décrit :",
    "options": [
      "A) Relation de sens proche",
      "B) Relation d'inclusion (partie/tout)",
      "C) Relation de ressemblance"
    ],
    "answer": "B",
    "explanation": "La méronymie exprime une relation partie/tout."
  },
  {
    "question": "« Date » (jour) et « datte » (fruit) sont des :",
    "options": [
      "A) Mots polysémiques",
      "B) Homonymes",
      "C) Paronymes",
      "D) Synonymes"
    ],
    "answer": "B",
    "explanation": "Ces mots se prononcent pareil mais n'ont aucun lien de sens : homonymes."
  },
  {
    "question": "Quel terme désigne des mots interchangeables avec un sens très proche ?",
    "options": [
      "A) Antonymes",
      "B) Synonymes",
      "C) Paronymes",
      "D) Homonymes"
    ],
    "answer": "B",
    "explanation": "Les synonymes ont un sens identique ou très proche."
  },
  {
    "question": "L'expression « J'ai mille choses à faire » est un :",
    "options": [
      "A) Euphémisme",
      "B) Litote",
      "C) Hyperbole",
      "D) Métonymie"
    ],
    "answer": "C",
    "explanation": "L'exagération volontaire est une hyperbole."
  },
  {
    "question": "Quel est l'hyperonyme de « voiture », « camion », « bus » ?",
    "options": [
      "A) Véhicule",
      "B) Transport",
      "C) Route",
      "D) Moteur"
    ],
    "answer": "A",
    "explanation": "« Véhicule » est le terme général qui englobe ces mots."
  },
  {
    "question": "La répétition d'un mot en début de vers s'appelle :",
    "options": [
      "A) Anaphore",
      "B) Allitération",
      "C) Assonance",
      "D) Métaphore"
    ],
    "answer": "A",
    "explanation": "L'anaphore est la répétition d'un mot ou groupe de mots en début de phrase."
  },
  {
    "question": "Les mots « poisson » et « poison » sont des :",
    "options": [
      "A) Homographes",
      "B) Paronymes",
      "C) Homophones",
      "D) Synonymes"
    ],
    "answer": "B",
    "explanation": "Ils se ressemblent beaucoup mais ont des sens différents : paronymes."
  },
  {
    "question": "Quel terme désigne les mots cohyponymes de « animal » ?",
    "options": [
      "A) Arbre, plante",
      "B) Chat, chien, oiseau",
      "C) Maison, jardin",
      "D) Mammifère, reptile"
    ],
    "answer": "B",
    "explanation": "Les cohyponymes sont des hyponymes d'un même hyperonyme (ici « animal »)."
  },
  {
    "question": "Les mots « ver », « verre » et « vert » sont des :",
    "options": [
      "A) Paronymes",
      "B) Homographes",
      "C) Homophones",
      "D) Synonymes"
    ],
    "answer": "C",
    "explanation": "Ces mots se prononcent identiquement mais s'écrivent différemment : homophones."
  },
  {
    "question": "La relation entre « chien » et « animal » est une :",
    "options": [
      "A) Synonymie",
      "B) Hyponymie",
      "C) Antonymie",
      "D) Homonymie"
    ],
    "answer": "B",
    "explanation": "« Chien » est un hyponyme (terme spécifique) de « animal » (terme général)."
  },
  {
    "question": "Le mot « Radar » est un exemple de :",
    "options": [
      "A) Anagramme",
      "B) Palindrome",
      "C) Homonyme",
      "D) Paronyme"
    ],
    "answer": "B",
    "explanation": "« Radar » se lit identiquement dans les deux sens : c'est un palindrome."
  },
  {
    "question": "Quelle figure de style est une courte phrase qui se termine par une pointe satirique ?",
    "options": [
      "A) Métaphore",
      "B) Épigramme",
      "C) Hyperbole",
      "D) Allégorie"
    ],
    "answer": "B",
    "explanation": "L'épigramme est une courte pièce satirique ou spirituelle."
  },
  {
    "question": "Les mots « cession » et « session » sont des :",
    "options": [
      "A) Synonymes",
      "B) Homographes",
      "C) Paronymes",
      "D) Homophones"
    ],
    "answer": "C",
    "explanation": "Ces mots se ressemblent fortement mais ont des sens différents : paronymes."
  },
  {
    "question": "Dans « pied de la jambe » et « pied d'une montagne », « pied » illustre :",
    "options": [
      "A) Homonymie",
      "B) Polysémie",
      "C) Méronymie",
      "D) Paronymie"
    ],
    "answer": "B",
    "explanation": "Un même mot avec plusieurs sens liés par l'origine : polysémie."
  },
  {
    "question": "« Imaginer » et « migraine » sont des :",
    "options": [
      "A) Palindromes",
      "B) Homophones",
      "C) Anagrammes",
      "D) Paronymes"
    ],
    "answer": "C",
    "explanation": "Les lettres des deux mots peuvent être réorganisées : anagrammes."
  },
  {
    "question": "Dans « Sa bouche est une rose », quelle figure de style est utilisée ?",
    "options": [
      "A) Comparaison",
      "B) Métaphore",
      "C) Métonymie",
      "D) Hyperbole"
    ],
    "answer": "B",
    "explanation": "Une métaphore établit une comparaison implicite sans utiliser « comme »."
  },
  {
    "question": "« Chaud » et « froid » sont des :",
    "options": [
      "A) Antonymes",
      "B) Homonymes",
      "C) Hyponymes",
      "D) Synonymes"
    ],
    "answer": "A",
    "explanation": "Ces mots ont des sens opposés : ce sont des antonymes."
  },
  {
    "question": "« Roue » est le méronyme de « voiture ». La méronymie décrit :",
    "options": [
      "A) Relation de sens proche",
      "B) Relation d'inclusion (partie/tout)",
      "C) Relation de ressemblance"
    ],
    "answer": "B",
    "explanation": "Un méronyme désigne une partie d'un tout (holonyme)."
  },
  {
    "question": "« Avocat » (fruit) et « avocat » (profession) sont des :",
    "options": [
      "A) Mots polysémiques",
      "B) Homonymes",
      "C) Paronymes",
      "D) Synonymes"
    ],
    "answer": "B",
    "explanation": "Ces mots n'ont aucun lien de sens malgré leur forme identique : homonymes."
  },
  {
    "question": "Quel terme désigne des mots au sens identique ou très proche ?",
    "options": [
      "A) Antonymes",
      "B) Synonymes",
      "C) Paronymes",
      "D) Homophones"
    ],
    "answer": "B",
    "explanation": "Les synonymes sont interchangeables dans un contexte donné."
  },
  {
    "question": "L'expression « Je meurs de faim » est un :",
    "options": [
      "A) Euphémisme",
      "B) Litote",
      "C) Hyperbole",
      "D) Oxymore"
    ],
    "answer": "C",
    "explanation": "L'hyperbole est une exagération volontaire pour renforcer l'expression."
  },
  {
    "question": "Quel est l'hyperonyme de « chaise », « fauteuil », « tabouret » ?",
    "options": [
      "A) Meuble",
      "B) Bois",
      "C) Assise",
      "D) Salon"
    ],
    "answer": "A",
    "explanation": "« Meuble » est le terme général qui englobe ces sièges."
  },
  {
    "question": "Comment appelle-t-on la répétition d'un mot en début de phrase ?",
    "options": [
      "A) Anaphore",
      "B) Allitération",
      "C) Assonance",
      "D) Épiphore"
    ],
    "answer": "A",
    "explanation": "L'anaphore est la répétition d'un mot ou groupe en début de vers ou phrase."
  },
  {
    "question": "Les mots « pêcheur » et « pécheur » sont des :",
    "options": [
      "A) Homographes",
      "B) Homophones",
      "C) Synonymes",
      "D) Antonymes"
    ],
    "answer": "B",
    "explanation": "Prononciation identique mais orthographe différente : homophones."
  },
  {
    "question": "Quel phénomène décrit des mots très ressemblants mais de sens différents ?",
    "options": [
      "A) Homonymie",
      "B) Synonymie",
      "C) Paronymie",
      "D) Polysémie"
    ],
    "answer": "C",
    "explanation": "Les paronymes se ressemblent phonétiquement et graphiquement."
  },
  {
    "question": "« Engage le jeu que je le gagne » est un :",
    "options": [
      "A) Anagramme",
      "B) Palindrome",
      "C) Épigramme",
      "D) Calembour"
    ],
    "answer": "B",
    "explanation": "Cette phrase se lit dans les deux sens : palindrome."
  },
  {
    "question": "L'hétéronymie concerne des mots de sens liés mais de radicaux différents ?",
    "options": [
      "A) Vrai",
      "B) Faux",
      "C) Partiellement vrai"
    ],
    "answer": "A",
    "explanation": "Ex : « oncle/tante », « cheval/jument » - sens liés, radicaux différents."
  },
  {
    "question": "Quels mots sont cohyponymes de « fleur » ?",
    "options": [
      "A) Arbre, arbuste",
      "B) Rose, tulipe",
      "C) Bouquet, jardin",
      "D) Pétale, tige"
    ],
    "answer": "B",
    "explanation": "Les cohyponymes partagent le même hyperonyme (ici « fleur »)."
  },
  {
    "question": "« Conte », « comte » et « compte » sont des :",
    "options": [
      "A) Paronymes",
      "B) Homophones",
      "C) Homographes",
      "D) Synonymes"
    ],
    "answer": "B",
    "explanation": "Même prononciation, orthographes différentes : homophones."
  },
  {
    "question": "Dans « Il est mort de rire », quelle figure est utilisée ?",
    "options": [
      "A) Hyperbole",
      "B) Litote",
      "C) Euphémisme",
      "D) Antiphrase"
    ],
    "answer": "A",
    "explanation": "Exagération volontaire pour renforcer l'expression : hyperbole."
  },
  {
    "question": "« Oncle » et « tante » illustrent :",
    "options": [
      "A) Synonymie",
      "B) Antonymie",
      "C) Hétéronymie",
      "D) Paronymie"
    ],
    "answer": "C",
    "explanation": "Sens liés (famille) mais radicaux complètement différents : hétéronymie."
  },
  {
    "question": "L'allitération est la répétition de :",
    "options": [
      "A) Voyelles",
      "B) Consonnes",
      "C) Mots",
      "D) Syllabes"
    ],
    "answer": "B",
    "explanation": "L'allitération répète des consonnes. L'assonance répète des voyelles."
  },
  {
    "question": "« Père » est l'holonyme de « main ». Vrai ou faux ?",
    "options": [
      "A) Vrai",
      "B) Faux"
    ],
    "answer": "B",
    "explanation": "Faux. « Corps » serait l'holonyme de « main » (tout dont fait partie la main)."
  },
  {
    "question": "« Ce n'est pas mauvais » pour dire « c'est excellent » est une :",
    "options": [
      "A) Hyperbole",
      "B) Litote",
      "C) Métaphore",
      "D) Métonymie"
    ],
    "answer": "B",
    "explanation": "La litote dit moins pour suggérer plus."
  },
  {
    "question": "« Nager » et « narguer » sont des :",
    "options": [
      "A) Synonymes",
      "B) Paronymes",
      "C) Homonymes",
      "D) Antonymes"
    ],
    "answer": "B",
    "explanation": "Ressemblance phonétique et graphique forte : paronymes."
  },
  {
    "question": "Dans « Il pleut des cordes », quelle figure est utilisée ?",
    "options": [
      "A) Métaphore",
      "B) Comparaison",
      "C) Hyperbole",
      "D) Personnification"
    ],
    "answer": "C",
    "explanation": "Exagération pour décrire une pluie forte : hyperbole."
  },
  {
    "question": "« Tête » (partie du corps) et « tête » (chef) illustrent :",
    "options": [
      "A) Homonymie",
      "B) Polysémie",
      "C) Paronymie",
      "D) Synonymie"
    ],
    "answer": "B",
    "explanation": "Même mot, sens différents mais liés par l'origine : polysémie."
  },
  {
    "question": "L'assonance est la répétition de :",
    "options": [
      "A) Consonnes",
      "B) Voyelles",
      "C) Mots entiers",
      "D) Phrases"
    ],
    "answer": "B",
    "explanation": "L'assonance est la répétition de voyelles. L'allitération répète des consonnes."
  },
  {
    "question": "« Boire un verre » est un exemple de :",
    "options": [
      "A) Métaphore",
      "B) Métonymie",
      "C) Synecdoque",
      "D) Litote"
    ],
    "answer": "B",
    "explanation": "La métonymie remplace un mot par un autre lié logiquement. Ici le contenant (verre) pour le contenu (boisson)."
  },
  {
    "question": "Quel terme désigne un mot créé récemment dans une langue ?",
    "options": [
      "A) Archaïsme",
      "B) Néologisme",
      "C) Barbarisme",
      "D) Solécisme"
    ],
    "answer": "B",
    "explanation": "Un néologisme est un mot nouveau ou récemment entré dans la langue."
  },
  {
    "question": "Quel terme désigne un mot tombé en désuétude, n'étant plus employé ?",
    "options": [
      "A) Néologisme",
      "B) Archaïsme",
      "C) Barbarisme",
      "D) Pléonasme"
    ],
    "answer": "B",
    "explanation": "Un archaïsme est un mot ou une expression ancienne qui n'est plus en usage courant."
  },
  {
    "question": "Qu'est-ce qu'un barbarisme ?",
    "options": [
      "A) Un mot étranger",
      "B) Une faute de vocabulaire (mot déformé)",
      "C) Un mot ancien",
      "D) Un mot technique"
    ],
    "answer": "B",
    "explanation": "Un barbarisme est l'emploi d'un mot inexistant ou déformé. Ex : « aéropage » au lieu d'« aréopage »."
  },
  {
    "question": "Qu'est-ce qu'un solécisme ?",
    "options": [
      "A) Une faute d'orthographe",
      "B) Une faute de syntaxe",
      "C) Un mot inventé",
      "D) Un mot étranger"
    ],
    "answer": "B",
    "explanation": "Un solécisme est une faute de grammaire/syntaxe. Ex : « c'est à moi que je parle » au lieu de « c'est à moi qu'on parle »."
  },
  {
    "question": "« Le Roi Soleil » pour désigner Louis XIV est une :",
    "options": [
      "A) Métaphore",
      "B) Périphrase",
      "C) Antonomase",
      "D) Comparaison"
    ],
    "answer": "C",
    "explanation": "L'antonomase utilise un nom propre comme nom commun ou inversement."
  },
  {
    "question": "L'épiphore est la répétition d'un mot ou groupe de mots :",
    "options": [
      "A) En début de phrase",
      "B) En fin de phrase",
      "C) Au milieu de phrase",
      "D) Partout dans la phrase"
    ],
    "answer": "B",
    "explanation": "L'épiphore est le contraire de l'anaphore : elle répète un élément en fin de vers ou de phrase."
  },
  {
    "question": "« Blanc bonnet et bonnet blanc » est un exemple de :",
    "options": [
      "A) Chiasme",
      "B) Anaphore",
      "C) Palindrome",
      "D) Métonymie"
    ],
    "answer": "A",
    "explanation": "Le chiasme est un croisement de termes selon le schéma AB-BA."
  },
  {
    "question": "« Courriel » est un néologisme français pour remplacer :",
    "options": [
      "A) Internet",
      "B) E-mail",
      "C) SMS",
      "D) Chat"
    ],
    "answer": "B",
    "explanation": "« Courriel » est le néologisme officiel pour remplacer l'anglicisme « e-mail »."
  },
  {
    "question": "La catachrèse est :",
    "options": [
      "A) Une métaphore devenue si courante qu'on ne la remarque plus",
      "B) Un pléonasme",
      "C) Une exagération",
      "D) Une ironie"
    ],
    "answer": "A",
    "explanation": "La catachrèse est une métaphore passée dans l'usage courant. Ex : « les pieds d'une table »."
  },
  {
    "question": "« Cheval » et « équestre » illustrent :",
    "options": [
      "A) Synonymie",
      "B) Un doublet étymologique",
      "C) Paronymie",
      "D) Homonymie"
    ],
    "answer": "B",
    "explanation": "Le nom vient du latin populaire (caballus) et l'adjectif du latin savant (equester) : doublet étymologique."
  },
  {
    "question": "Quel est l'antonyme de « loquace » ?",
    "options": [
      "A) Bavard",
      "B) Taciturne",
      "C) Verbeux",
      "D) Prolixe"
    ],
    "answer": "B",
    "explanation": "« Loquace » signifie bavard ; « taciturne » signifie silencieux, peu enclin à parler."
  },
  {
    "question": "Quel phénomène lexical lie « hôte » (celui qui reçoit) et « hôte » (celui qui est reçu) ?",
    "options": [
      "A) Polysémie",
      "B) Homonymie",
      "C) Énantiosémie",
      "D) Paronymie"
    ],
    "answer": "C",
    "explanation": "L'énantiosémie (ou auto-antonymie) désigne un mot qui a deux sens opposés."
  },
  {
    "question": "« Clair-obscur » est un exemple de :",
    "options": [
      "A) Pléonasme",
      "B) Oxymore",
      "C) Antithèse",
      "D) Chiasme"
    ],
    "answer": "B",
    "explanation": "L'oxymore associe deux termes contradictoires dans un même syntagme."
  },
  {
    "question": "Qu'est-ce qu'une antithèse ?",
    "options": [
      "A) Deux termes contradictoires accolés",
      "B) Opposition de deux idées dans une phrase",
      "C) Exagération volontaire",
      "D) Comparaison implicite"
    ],
    "answer": "B",
    "explanation": "L'antithèse oppose deux idées dans une phrase ou un paragraphe, contrairement à l'oxymore qui accole les contraires."
  },
  {
    "question": "Quel procédé consiste à atténuer une vérité désagréable ?",
    "options": [
      "A) Hyperbole",
      "B) Litote",
      "C) Euphémisme",
      "D) Antiphrase"
    ],
    "answer": "C",
    "explanation": "L'euphémisme adoucit une réalité brutale. Ex : « il s'est éteint » pour « il est mort »."
  },
  {
    "question": "« Frère » et « sœur » illustrent :",
    "options": [
      "A) Synonymie",
      "B) Antonymie",
      "C) Hétéronymie",
      "D) Paronymie"
    ],
    "answer": "C",
    "explanation": "Sens liés (famille) mais radicaux totalement différents : c'est l'hétéronymie."
  },
  {
    "question": "Le mot « chrysanthème » est :",
    "options": [
      "A) Féminin",
      "B) Masculin",
      "C) Les deux"
    ],
    "answer": "B",
    "explanation": "« Chrysanthème » est masculin : un chrysanthème."
  },
  {
    "question": "Qu'est-ce qu'une personnification ?",
    "options": [
      "A) Comparer deux éléments",
      "B) Attribuer des traits humains à un objet ou animal",
      "C) Exagérer un propos",
      "D) Dire le contraire de ce qu'on pense"
    ],
    "answer": "B",
    "explanation": "La personnification donne des caractéristiques humaines à ce qui n'est pas humain. Ex : « le vent hurle »."
  },
  {
    "question": "Qu'est-ce qu'une gradation ?",
    "options": [
      "A) Répétition d'un mot",
      "B) Énumération de termes d'intensité croissante ou décroissante",
      "C) Opposition de deux idées",
      "D) Comparaison implicite"
    ],
    "answer": "B",
    "explanation": "La gradation est une suite de mots d'intensité progressive. Ex : « je le vis, je rougis, je pâlis » (Racine)."
  },
  {
    "question": "Dans « La fourmi travaille sans relâche », quelle figure est utilisée ?",
    "options": [
      "A) Métaphore",
      "B) Personnification",
      "C) Comparaison",
      "D) Allégorie"
    ],
    "answer": "B",
    "explanation": "Attribuer le travail (action humaine consciente) à un animal est une personnification."
  },
  {
    "question": "« Il prit son chapeau et la porte » est un exemple de :",
    "options": [
      "A) Pléonasme",
      "B) Zeugme",
      "C) Chiasme",
      "D) Oxymore"
    ],
    "answer": "B",
    "explanation": "Le zeugme associe sur le même verbe des compléments de nature très différente (sens concret et figuré)."
  },
  {
    "question": "Qu'est-ce qu'un champ lexical ?",
    "options": [
      "A) L'ensemble des sens d'un mot",
      "B) L'ensemble des mots liés à un même thème",
      "C) Les mots de même famille",
      "D) Les mots de même racine"
    ],
    "answer": "B",
    "explanation": "Le champ lexical regroupe les mots se rapportant à un même thème. Ex : école → élève, cours, tableau."
  },
  {
    "question": "Qu'est-ce qu'un champ sémantique ?",
    "options": [
      "A) Les mots d'un même thème",
      "B) L'ensemble des sens d'un seul mot",
      "C) Les mots de même sonorité",
      "D) Les synonymes d'un mot"
    ],
    "answer": "B",
    "explanation": "Le champ sémantique est l'ensemble des significations d'un mot. Ex : « feuille » → papier, arbre, métal."
  },
  {
    "question": "Qu'est-ce qu'une prosopopée ?",
    "options": [
      "A) Faire parler un absent, un mort ou un objet",
      "B) Exagérer ses propos",
      "C) Répéter un mot pour insister",
      "D) Utiliser un mot pour un autre"
    ],
    "answer": "A",
    "explanation": "La prosopopée fait parler un absent, un mort, un animal ou une abstraction."
  },
  {
    "question": "« Je suis venu, j'ai vu, j'ai vaincu » est un exemple de :",
    "options": [
      "A) Gradation",
      "B) Anaphore",
      "C) Les deux à la fois",
      "D) Allitération"
    ],
    "answer": "C",
    "explanation": "C'est à la fois une anaphore (répétition de « je ») et une gradation (intensité croissante)."
  },
  {
    "question": "Quel est l'hyperonyme de « pomme », « banane », « mangue » ?",
    "options": [
      "A) Aliment",
      "B) Fruit",
      "C) Arbre",
      "D) Récolte"
    ],
    "answer": "B",
    "explanation": "« Fruit » est le terme général englobant pomme, banane et mangue."
  },
  {
    "question": "« Prêt » et « près » sont des :",
    "options": [
      "A) Synonymes",
      "B) Homophones",
      "C) Paronymes",
      "D) Antonymes"
    ],
    "answer": "B",
    "explanation": "Même prononciation mais sens et orthographe différents : homophones."
  },
  {
    "question": "« Éruption » et « irruption » sont des :",
    "options": [
      "A) Synonymes",
      "B) Homophones",
      "C) Paronymes",
      "D) Antonymes"
    ],
    "answer": "C",
    "explanation": "Formes proches mais sens différents : éruption (sortie violente) vs irruption (entrée brusque)."
  },
  {
    "question": "« Page » (de livre) et « page » (jeune serviteur) sont des :",
    "options": [
      "A) Mots polysémiques",
      "B) Homonymes",
      "C) Paronymes",
      "D) Synonymes"
    ],
    "answer": "B",
    "explanation": "Même forme mais origines et sens totalement différents : homonymes."
  },
  {
    "question": "Qu'est-ce qu'une allégorie ?",
    "options": [
      "A) Une comparaison abrégée",
      "B) Une métaphore filée représentant une idée abstraite",
      "C) Un pléonasme",
      "D) Une exagération"
    ],
    "answer": "B",
    "explanation": "L'allégorie représente une idée abstraite par une image concrète prolongée. Ex : la Justice avec une balance."
  },
  {
    "question": "« Doigt » est le méronyme de :",
    "options": [
      "A) Ongle",
      "B) Main",
      "C) Bras",
      "D) Pied"
    ],
    "answer": "B",
    "explanation": "Le doigt est une partie de la main : « doigt » (méronyme) → « main » (holonyme)."
  },
  {
    "question": "Qu'est-ce qu'une prétérition ?",
    "options": [
      "A) Parler d'une chose en disant qu'on n'en parlera pas",
      "B) Exagérer ses propos",
      "C) Dire le contraire",
      "D) Atténuer la réalité"
    ],
    "answer": "A",
    "explanation": "La prétérition consiste à dire qu'on ne va pas parler de quelque chose tout en en parlant."
  },
  {
    "question": "« Été » et « hiver » sont des :",
    "options": [
      "A) Synonymes",
      "B) Antonymes",
      "C) Cohyponymes",
      "D) Homonymes"
    ],
    "answer": "C",
    "explanation": "Ce sont des cohyponymes de l'hyperonyme « saison »."
  },
  {
    "question": "« Kayak » est un exemple de :",
    "options": [
      "A) Anagramme",
      "B) Palindrome",
      "C) Néologisme",
      "D) Emprunt"
    ],
    "answer": "B",
    "explanation": "« Kayak » se lit dans les deux sens : c'est un palindrome."
  },
  {
    "question": "Dans « boire la tasse » (avaler de l'eau en nageant), quelle figure est utilisée ?",
    "options": [
      "A) Métaphore",
      "B) Métonymie",
      "C) Catachrèse",
      "D) Litote"
    ],
    "answer": "C",
    "explanation": "C'est une catachrèse : une métaphore figée dans l'usage courant."
  }
];

const THEME_3 = [
  {
    "question": "Quelle est la capitale du Togo ?",
    "options": [
      "A) Porto-Novo",
      "B) Lomé",
      "C) Cotonou",
      "D) Ouagadougou"
    ],
    "answer": "B",
    "explanation": "Lomé est la capitale du Togo."
  },
  {
    "question": "Quelle est la capitale du Burkina Faso ?",
    "options": [
      "A) Bamako",
      "B) Niamey",
      "C) Ouagadougou",
      "D) Dakar"
    ],
    "answer": "C",
    "explanation": "Ouagadougou est la capitale du Burkina Faso."
  },
  {
    "question": "Dans quelle partie du corps se trouve le fémur ?",
    "options": [
      "A) Le bras",
      "B) La jambe",
      "C) Le dos",
      "D) Le pied"
    ],
    "answer": "B",
    "explanation": "Le fémur est l'os de la cuisse, dans la jambe."
  },
  {
    "question": "Si je suis le gendre de Paul, qui est Paul pour moi ?",
    "options": [
      "A) Mon père",
      "B) Mon frère",
      "C) Mon beau-père",
      "D) Mon oncle"
    ],
    "answer": "C",
    "explanation": "Le gendre est le mari de la fille, donc Paul est mon beau-père."
  },
  {
    "question": "Sur quoi portent principalement les recherches de Louis Pasteur ?",
    "options": [
      "A) L'électricité",
      "B) Les microbes et vaccins",
      "C) La mécanique",
      "D) L'astronomie"
    ],
    "answer": "B",
    "explanation": "Louis Pasteur est célèbre pour ses travaux sur les microbes et la vaccination."
  },
  {
    "question": "Dans quel océan navigue-t-on au large de Tokyo ?",
    "options": [
      "A) Océan Atlantique",
      "B) Océan Pacifique",
      "C) Océan Indien",
      "D) Océan Arctique"
    ],
    "answer": "B",
    "explanation": "Tokyo se situe sur la côte de l'océan Pacifique."
  },
  {
    "question": "Quel est le plus petit pays du monde ?",
    "options": [
      "A) Monaco",
      "B) Le Vatican",
      "C) Saint-Marin",
      "D) Le Liechtenstein"
    ],
    "answer": "B",
    "explanation": "Le Vatican est le plus petit pays du monde avec 0,44 km²."
  },
  {
    "question": "Quel pays a pour monnaie le Cedi ?",
    "options": [
      "A) Le Ghana",
      "B) Le Nigeria",
      "C) Le Sénégal",
      "D) Le Togo"
    ],
    "answer": "A",
    "explanation": "Le Cedi est la monnaie du Ghana."
  },
  {
    "question": "De quelle région Abengourou est-il le chef-lieu ?",
    "options": [
      "A) Le Moronou",
      "B) L'Indénié-Djuablin",
      "C) Le N'Zi",
      "D) Le Bounkani"
    ],
    "answer": "B",
    "explanation": "Abengourou est le chef-lieu de la région de l'Indénié-Djuablin."
  },
  {
    "question": "De quel pays Nairobi est-il la capitale ?",
    "options": [
      "A) Tanzanie",
      "B) Kenya",
      "C) Ouganda",
      "D) Rwanda"
    ],
    "answer": "B",
    "explanation": "Nairobi est la capitale du Kenya."
  },
  {
    "question": "Laquelle de ces inventions est la plus récente ?",
    "options": [
      "A) Le téléphone",
      "B) L'ampoule électrique",
      "C) Internet",
      "D) La radio"
    ],
    "answer": "C",
    "explanation": "Internet a été développé dans les années 1960-1990, bien après les autres."
  },
  {
    "question": "Qui est l'auteur de l'œuvre « Le Petit Prince » ?",
    "options": [
      "A) Victor Hugo",
      "B) Antoine de Saint-Exupéry",
      "C) Albert Camus",
      "D) Jules Verne"
    ],
    "answer": "B",
    "explanation": "Antoine de Saint-Exupéry a écrit « Le Petit Prince » en 1943."
  },
  {
    "question": "Quel est le cri du corbeau ?",
    "options": [
      "A) Croasse",
      "B) Coasse",
      "C) Siffle",
      "D) Piaule"
    ],
    "answer": "A",
    "explanation": "Le corbeau croasse."
  },
  {
    "question": "Comment écrit-on 200 en lettres ?",
    "options": [
      "A) Deux-cent",
      "B) Deux-cents",
      "C) Deux cent",
      "D) Deux cents"
    ],
    "answer": "D",
    "explanation": "« Deux cents » s'écrit avec « cents » au pluriel car suivi de rien."
  },
  {
    "question": "Quel mode suit la conjonction « Avant que » ?",
    "options": [
      "A) L'indicatif",
      "B) Le subjonctif",
      "C) Le conditionnel",
      "D) L'impératif"
    ],
    "answer": "B",
    "explanation": "« Avant que » est toujours suivi du subjonctif."
  },
  {
    "question": "Quelle est la capitale du Cameroun ?",
    "options": [
      "A) Douala",
      "B) Yaoundé",
      "C) Libreville",
      "D) Bangui"
    ],
    "answer": "B",
    "explanation": "Yaoundé est la capitale politique du Cameroun."
  },
  {
    "question": "Quelle est la capitale de la République démocratique du Congo ?",
    "options": [
      "A) Brazzaville",
      "B) Kinshasa",
      "C) Lubumbashi",
      "D) Goma"
    ],
    "answer": "B",
    "explanation": "Kinshasa est la capitale de la RDC."
  },
  {
    "question": "Quelle est la capitale du Gabon ?",
    "options": [
      "A) Libreville",
      "B) Port-Gentil",
      "C) Franceville",
      "D) Oyem"
    ],
    "answer": "A",
    "explanation": "Libreville est la capitale du Gabon."
  },
  {
    "question": "Quelle est la capitale du Tchad ?",
    "options": [
      "A) Abéché",
      "B) Moundou",
      "C) N'Djamena",
      "D) Sarh"
    ],
    "answer": "C",
    "explanation": "N'Djamena est la capitale du Tchad."
  },
  {
    "question": "Quelle est la capitale du Ghana ?",
    "options": [
      "A) Kumasi",
      "B) Tamale",
      "C) Accra",
      "D) Tema"
    ],
    "answer": "C",
    "explanation": "Accra est la capitale du Ghana."
  },
  {
    "question": "Quelle est la capitale du Bénin ?",
    "options": [
      "A) Cotonou",
      "B) Porto-Novo",
      "C) Parakou",
      "D) Abomey"
    ],
    "answer": "B",
    "explanation": "Porto-Novo est la capitale administrative du Bénin, bien que Cotonou soit la capitale économique."
  },
  {
    "question": "Quelle est la capitale du Niger ?",
    "options": [
      "A) Niamey",
      "B) Zinder",
      "C) Maradi",
      "D) Agadez"
    ],
    "answer": "A",
    "explanation": "Niamey est la capitale du Niger."
  },
  {
    "question": "Quelle est la capitale du Sénégal ?",
    "options": [
      "A) Saint-Louis",
      "B) Thiès",
      "C) Dakar",
      "D) Ziguinchor"
    ],
    "answer": "C",
    "explanation": "Dakar est la capitale du Sénégal."
  },
  {
    "question": "Quelle est la capitale du Mali ?",
    "options": [
      "A) Bamako",
      "B) Tombouctou",
      "C) Sikasso",
      "D) Kayes"
    ],
    "answer": "A",
    "explanation": "Bamako est la capitale du Mali."
  },
  {
    "question": "Quel est le plus long fleuve d'Afrique ?",
    "options": [
      "A) Congo",
      "B) Niger",
      "C) Nil",
      "D) Zambèze"
    ],
    "answer": "C",
    "explanation": "Le Nil est le plus long fleuve d'Afrique (6 650 km)."
  },
  {
    "question": "Quel est le plus haut sommet d'Afrique ?",
    "options": [
      "A) Mont Kenya",
      "B) Kilimandjaro",
      "C) Mont Stanley",
      "D) Ras Dashan"
    ],
    "answer": "B",
    "explanation": "Le Kilimandjaro en Tanzanie culmine à 5 895 m."
  },
  {
    "question": "Combien de pays partagent le bassin du fleuve Niger ?",
    "options": [
      "A) 5",
      "B) 7",
      "C) 10",
      "D) 12"
    ],
    "answer": "C",
    "explanation": "Le fleuve Niger traverse ou borde 10 pays africains."
  },
  {
    "question": "Quel désert est le plus grand du monde ?",
    "options": [
      "A) Sahara",
      "B) Gobi",
      "C) Antarctique",
      "D) Kalahari"
    ],
    "answer": "C",
    "explanation": "L'Antarctique est techniquement le plus grand désert (désert froid)."
  },
  {
    "question": "Quel est le plus grand désert chaud du monde ?",
    "options": [
      "A) Kalahari",
      "B) Sahara",
      "C) Gobi",
      "D) Arabie"
    ],
    "answer": "B",
    "explanation": "Le Sahara est le plus grand désert chaud avec environ 9 millions de km²."
  },
  {
    "question": "Comment appelle-t-on le gendre pour les parents de l'épouse ?",
    "options": [
      "A) Beau-fils",
      "B) Beau-frère",
      "C) Neveu",
      "D) Cousin"
    ],
    "answer": "A",
    "explanation": "Le gendre est le beau-fils pour les parents de l'épouse."
  },
  {
    "question": "Comment appelle-t-on la belle-fille pour les parents du mari ?",
    "options": [
      "A) Nièce",
      "B) Bru",
      "C) Belle-sœur",
      "D) Cousine"
    ],
    "answer": "B",
    "explanation": "La bru est l'épouse du fils (belle-fille)."
  },
  {
    "question": "Quel est le nom scientifique de la rotule ?",
    "options": [
      "A) Tibia",
      "B) Fémur",
      "C) Patella",
      "D) Humérus"
    ],
    "answer": "C",
    "explanation": "La rotule est appelée 'patella' en nomenclature anatomique."
  },
  {
    "question": "Quel est le nom scientifique du péroné ?",
    "options": [
      "A) Fibula",
      "B) Tibia",
      "C) Fémur",
      "D) Malléole"
    ],
    "answer": "A",
    "explanation": "Le péroné est appelé 'fibula' en nomenclature anatomique."
  },
  {
    "question": "Quel est l'os le plus long du corps humain ?",
    "options": [
      "A) Humérus",
      "B) Tibia",
      "C) Fémur",
      "D) Radius"
    ],
    "answer": "C",
    "explanation": "Le fémur (os de la cuisse) est l'os le plus long."
  },
  {
    "question": "Combien d'os compte le squelette humain adulte ?",
    "options": [
      "A) 186",
      "B) 206",
      "C) 226",
      "D) 246"
    ],
    "answer": "B",
    "explanation": "Le squelette adulte compte 206 os."
  },
  {
    "question": "Qui a découvert la loi de la gravitation universelle ?",
    "options": [
      "A) Galilée",
      "B) Newton",
      "C) Einstein",
      "D) Kepler"
    ],
    "answer": "B",
    "explanation": "Isaac Newton a formulé la loi de la gravitation en 1687."
  },
  {
    "question": "Qui a découvert les rayons X ?",
    "options": [
      "A) Marie Curie",
      "B) Wilhelm Röntgen",
      "C) Henri Becquerel",
      "D) Pierre Curie"
    ],
    "answer": "B",
    "explanation": "Wilhelm Röntgen a découvert les rayons X en 1895."
  },
  {
    "question": "Qui a découvert la radioactivité ?",
    "options": [
      "A) Marie Curie",
      "B) Pierre Curie",
      "C) Henri Becquerel",
      "D) Ernest Rutherford"
    ],
    "answer": "C",
    "explanation": "Henri Becquerel a découvert la radioactivité en 1896."
  },
  {
    "question": "Qui a développé la théorie de la relativité ?",
    "options": [
      "A) Newton",
      "B) Bohr",
      "C) Einstein",
      "D) Planck"
    ],
    "answer": "C",
    "explanation": "Albert Einstein a publié la relativité restreinte en 1905 et générale en 1915."
  },
  {
    "question": "Quel scientifique a créé le premier vaccin contre la rage ?",
    "options": [
      "A) Edward Jenner",
      "B) Louis Pasteur",
      "C) Robert Koch",
      "D) Jonas Salk"
    ],
    "answer": "B",
    "explanation": "Louis Pasteur a développé le vaccin contre la rage en 1885."
  },
  {
    "question": "Qui a inventé la première vaccination contre la variole ?",
    "options": [
      "A) Louis Pasteur",
      "B) Edward Jenner",
      "C) Robert Koch",
      "D) Alexander Fleming"
    ],
    "answer": "B",
    "explanation": "Edward Jenner a développé le vaccin contre la variole en 1796."
  },
  {
    "question": "Quel est le cri du lion ?",
    "options": [
      "A) Rugit",
      "B) Brame",
      "C) Hurle",
      "D) Gronde"
    ],
    "answer": "A",
    "explanation": "Le lion rugit."
  },
  {
    "question": "Quel est le cri de l'âne ?",
    "options": [
      "A) Hennit",
      "B) Brait",
      "C) Mugit",
      "D) Bêle"
    ],
    "answer": "B",
    "explanation": "L'âne brait."
  },
  {
    "question": "Quel est le cri du cerf ?",
    "options": [
      "A) Brame",
      "B) Rugit",
      "C) Hurle",
      "D) Aboie"
    ],
    "answer": "A",
    "explanation": "Le cerf brame."
  },
  {
    "question": "Quel est le cri de la grenouille ?",
    "options": [
      "A) Croasse",
      "B) Coasse",
      "C) Siffle",
      "D) Piaule"
    ],
    "answer": "B",
    "explanation": "La grenouille coasse."
  },
  {
    "question": "En quelle année a eu lieu la chute du mur de Berlin ?",
    "options": [
      "A) 1987",
      "B) 1989",
      "C) 1991",
      "D) 1993"
    ],
    "answer": "B",
    "explanation": "Le mur de Berlin est tombé le 9 novembre 1989."
  },
  {
    "question": "En quelle année a eu lieu la Révolution française ?",
    "options": [
      "A) 1789",
      "B) 1799",
      "C) 1804",
      "D) 1815"
    ],
    "answer": "A",
    "explanation": "La Révolution française a commencé en 1789."
  },
  {
    "question": "Qui était le premier président des États-Unis ?",
    "options": [
      "A) Thomas Jefferson",
      "B) John Adams",
      "C) George Washington",
      "D) Benjamin Franklin"
    ],
    "answer": "C",
    "explanation": "George Washington a été le premier président (1789-1797)."
  },
  {
    "question": "En quelle année Christophe Colomb a-t-il découvert l'Amérique ?",
    "options": [
      "A) 1482",
      "B) 1492",
      "C) 1502",
      "D) 1512"
    ],
    "answer": "B",
    "explanation": "Christophe Colomb a découvert l'Amérique en 1492."
  },
  {
    "question": "Quelle est la capitale de l'Australie ?",
    "options": [
      "A) Sydney",
      "B) Melbourne",
      "C) Canberra",
      "D) Brisbane"
    ],
    "answer": "C",
    "explanation": "Canberra est la capitale de l'Australie."
  },
  {
    "question": "Quelle est la capitale du Canada ?",
    "options": [
      "A) Toronto",
      "B) Montréal",
      "C) Vancouver",
      "D) Ottawa"
    ],
    "answer": "D",
    "explanation": "Ottawa est la capitale du Canada."
  },
  {
    "question": "Quelle est la capitale du Brésil ?",
    "options": [
      "A) Rio de Janeiro",
      "B) São Paulo",
      "C) Brasília",
      "D) Salvador"
    ],
    "answer": "C",
    "explanation": "Brasília est la capitale du Brésil depuis 1960."
  },
  {
    "question": "Quelle est la devise de l'Union européenne ?",
    "options": [
      "A) Dollar",
      "B) Livre",
      "C) Euro",
      "D) Franc"
    ],
    "answer": "C",
    "explanation": "L'euro est la monnaie officielle de l'Union européenne."
  },
  {
    "question": "Quelle est la devise du Royaume-Uni ?",
    "options": [
      "A) Euro",
      "B) Livre sterling",
      "C) Dollar",
      "D) Couronne"
    ],
    "answer": "B",
    "explanation": "La livre sterling (GBP) est la devise du Royaume-Uni."
  },
  {
    "question": "Quelle est la planète la plus proche du Soleil ?",
    "options": [
      "A) Vénus",
      "B) Mars",
      "C) Mercure",
      "D) Terre"
    ],
    "answer": "C",
    "explanation": "Mercure est la planète la plus proche du Soleil."
  },
  {
    "question": "Combien de continents existe-t-il ?",
    "options": [
      "A) 5",
      "B) 6",
      "C) 7",
      "D) 8"
    ],
    "answer": "C",
    "explanation": "Il y a 7 continents : Afrique, Amérique du Nord, Amérique du Sud, Antarctique, Asie, Europe, Océanie."
  },
  {
    "question": "Quel pays a remporté la première Coupe du monde de football ?",
    "options": [
      "A) Brésil",
      "B) Argentine",
      "C) Uruguay",
      "D) Italie"
    ],
    "answer": "C",
    "explanation": "L'Uruguay a remporté la première Coupe du monde en 1930."
  },
  {
    "question": "Qui a peint la Joconde ?",
    "options": [
      "A) Michel-Ange",
      "B) Léonard de Vinci",
      "C) Raphaël",
      "D) Donatello"
    ],
    "answer": "B",
    "explanation": "Léonard de Vinci a peint la Joconde vers 1503-1506."
  },
  {
    "question": "Dans quel pays se trouve la tour Eiffel ?",
    "options": [
      "A) Italie",
      "B) Espagne",
      "C) France",
      "D) Belgique"
    ],
    "answer": "C",
    "explanation": "La tour Eiffel se trouve à Paris, en France."
  },
  {
    "question": "Quel est le symbole chimique de l'or ?",
    "options": [
      "A) Or",
      "B) Au",
      "C) Ag",
      "D) Go"
    ],
    "answer": "B",
    "explanation": "Le symbole de l'or est Au (du latin 'aurum')."
  },
  {
    "question": "Quel est le symbole chimique de l'argent ?",
    "options": [
      "A) Ar",
      "B) Ag",
      "C) Si",
      "D) Al"
    ],
    "answer": "B",
    "explanation": "Le symbole de l'argent est Ag (du latin 'argentum')."
  },
  {
    "question": "Combien y a-t-il de secondes dans une heure ?",
    "options": [
      "A) 3 000",
      "B) 3 600",
      "C) 6 000",
      "D) 7 200"
    ],
    "answer": "B",
    "explanation": "1 heure = 60 minutes × 60 secondes = 3 600 secondes."
  },
  {
    "question": "Quelle est la capitale de l'Éthiopie ?",
    "options": [
      "A) Nairobi",
      "B) Khartoum",
      "C) Addis-Abeba",
      "D) Kampala"
    ],
    "answer": "C",
    "explanation": "Addis-Abeba est la capitale de l'Éthiopie."
  },
  {
    "question": "Quel océan borde l'ouest de l'Afrique ?",
    "options": [
      "A) Océan Indien",
      "B) Océan Atlantique",
      "C) Océan Pacifique",
      "D) Océan Arctique"
    ],
    "answer": "B",
    "explanation": "L'océan Atlantique borde la côte ouest de l'Afrique."
  },
  {
    "question": "Combien de planètes compte le système solaire ?",
    "options": [
      "A) 7",
      "B) 8",
      "C) 9",
      "D) 10"
    ],
    "answer": "B",
    "explanation": "Le système solaire compte 8 planètes depuis le déclassement de Pluton en 2006."
  },
  {
    "question": "Quel pays est surnommé le 'pays du Soleil Levant' ?",
    "options": [
      "A) Chine",
      "B) Corée du Sud",
      "C) Japon",
      "D) Thaïlande"
    ],
    "answer": "C",
    "explanation": "Le Japon est traditionnellement appelé le 'pays du Soleil Levant'."
  },
  {
    "question": "Quelle est la langue officielle du Brésil ?",
    "options": [
      "A) Espagnol",
      "B) Portugais",
      "C) Français",
      "D) Anglais"
    ],
    "answer": "B",
    "explanation": "Le portugais est la langue officielle du Brésil."
  },
  {
    "question": "Quel est le chef-lieu du District des Lacs en Côte d'Ivoire ?",
    "options": [
      "A) Yamoussoukro",
      "B) Dimbokro",
      "C) Bouaflé",
      "D) Toumodi"
    ],
    "answer": "B",
    "explanation": "Dimbokro est le chef-lieu du District des Lacs."
  },
  {
    "question": "De quelle région Bouna est-il le chef-lieu ?",
    "options": [
      "A) Le Zanzan",
      "B) Le Bounkani",
      "C) Le Gontougo",
      "D) Le Tchologo"
    ],
    "answer": "B",
    "explanation": "Bouna est le chef-lieu de la région du Bounkani."
  },
  {
    "question": "De quel pays Lilongwe est-il la capitale ?",
    "options": [
      "A) Zambie",
      "B) Zimbabwe",
      "C) Malawi",
      "D) Mozambique"
    ],
    "answer": "C",
    "explanation": "Lilongwe est la capitale du Malawi."
  },
  {
    "question": "Quel nom d'oiseau utilise-t-on pour désigner un auteur de lettres anonymes ?",
    "options": [
      "A) Un aigle",
      "B) Un vautour",
      "C) Un corbeau",
      "D) Un faucon"
    ],
    "answer": "C",
    "explanation": "On appelle « corbeau » la personne qui envoie des lettres anonymes malveillantes."
  },
  {
    "question": "Quelle traversée Louis Blériot a-t-il réussie en avion le 25 juillet 1909 ?",
    "options": [
      "A) L'Atlantique",
      "B) La Méditerranée",
      "C) La Manche",
      "D) Le Pacifique"
    ],
    "answer": "C",
    "explanation": "Louis Blériot a été le premier à traverser la Manche en avion."
  },
  {
    "question": "Quel est le nom de la maladie qui entraîne un battement trop rapide du cœur ?",
    "options": [
      "A) Tachycardie",
      "B) Bradycardie",
      "C) Arythmie",
      "D) Angine"
    ],
    "answer": "A",
    "explanation": "La tachycardie est l'accélération anormale du rythme cardiaque."
  },
  {
    "question": "Qui est l'auteur de l'œuvre « Le Malade imaginaire » ?",
    "options": [
      "A) Molière",
      "B) Racine",
      "C) Corneille",
      "D) Voltaire"
    ],
    "answer": "A",
    "explanation": "Molière (Jean-Baptiste Poquelin) a écrit « Le Malade imaginaire » en 1673."
  },
  {
    "question": "Dans quelle ville siège l'Organisation des pays exportateurs de pétrole (OPEP) ?",
    "options": [
      "A) Genève",
      "B) New York",
      "C) Vienne",
      "D) Riyad"
    ],
    "answer": "C",
    "explanation": "L'OPEP a son siège à Vienne, en Autriche."
  },
  {
    "question": "Lequel de ces personnages n'est PAS issu du roman « Les Misérables » ?",
    "options": [
      "A) Fleur de lys",
      "B) Jean Valjean",
      "C) Cosette",
      "D) Gavroche"
    ],
    "answer": "A",
    "explanation": "Fleur de lys est un personnage de « Notre-Dame de Paris », pas des « Misérables »."
  },
  {
    "question": "En quelle année la Côte d'Ivoire a-t-elle accédé à l'indépendance ?",
    "options": [
      "A) 1958",
      "B) 1960",
      "C) 1962",
      "D) 1963"
    ],
    "answer": "B",
    "explanation": "La Côte d'Ivoire a proclamé son indépendance le 7 août 1960."
  },
  {
    "question": "Qui est le premier président de la Côte d'Ivoire ?",
    "options": [
      "A) Henri Konan Bédié",
      "B) Laurent Gbagbo",
      "C) Félix Houphouët-Boigny",
      "D) Robert Guéï"
    ],
    "answer": "C",
    "explanation": "Félix Houphouët-Boigny est le père fondateur et premier président (1960-1993)."
  },
  {
    "question": "Quelle est la capitale administrative de la Côte d'Ivoire ?",
    "options": [
      "A) Abidjan",
      "B) Bouaké",
      "C) Yamoussoukro",
      "D) San-Pédro"
    ],
    "answer": "C",
    "explanation": "Yamoussoukro est la capitale politique et administrative depuis 1983."
  },
  {
    "question": "Qui a écrit « L'enfant noir » ?",
    "options": [
      "A) Léopold Sédar Senghor",
      "B) Camara Laye",
      "C) Ahmadou Kourouma",
      "D) Mongo Béti"
    ],
    "answer": "B",
    "explanation": "Camara Laye, écrivain guinéen, a écrit « L'enfant noir » en 1953."
  },
  {
    "question": "Qui a écrit « Les Soleils des Indépendances » ?",
    "options": [
      "A) Bernard Dadié",
      "B) Ahmadou Kourouma",
      "C) Félix Tchicaya",
      "D) Birago Diop"
    ],
    "answer": "B",
    "explanation": "Ahmadou Kourouma, écrivain ivoirien, a publié ce roman en 1968."
  },
  {
    "question": "Quel poète et homme politique sénégalais a cofondé le mouvement de la Négritude ?",
    "options": [
      "A) Aimé Césaire",
      "B) Léopold Sédar Senghor",
      "C) Léon-Gontran Damas",
      "D) Les trois ensemble"
    ],
    "answer": "D",
    "explanation": "La Négritude a été fondée par Senghor, Césaire et Damas dans les années 1930."
  },
  {
    "question": "Quel pays africain est le plus grand producteur mondial de cacao ?",
    "options": [
      "A) Ghana",
      "B) Nigeria",
      "C) Côte d'Ivoire",
      "D) Cameroun"
    ],
    "answer": "C",
    "explanation": "La Côte d'Ivoire est le premier producteur mondial de cacao."
  },
  {
    "question": "Quel pays a pour monnaie le Naira ?",
    "options": [
      "A) Ghana",
      "B) Nigeria",
      "C) Liberia",
      "D) Sierra Leone"
    ],
    "answer": "B",
    "explanation": "Le Naira est la monnaie officielle du Nigeria."
  },
  {
    "question": "Quel pays a pour monnaie le Rand ?",
    "options": [
      "A) Kenya",
      "B) Éthiopie",
      "C) Afrique du Sud",
      "D) Tanzanie"
    ],
    "answer": "C",
    "explanation": "Le Rand est la monnaie de l'Afrique du Sud."
  },
  {
    "question": "Quelle est la capitale du Rwanda ?",
    "options": [
      "A) Bujumbura",
      "B) Kigali",
      "C) Kampala",
      "D) Gitega"
    ],
    "answer": "B",
    "explanation": "Kigali est la capitale du Rwanda."
  },
  {
    "question": "Quelle est la capitale de la Guinée-Bissau ?",
    "options": [
      "A) Conakry",
      "B) Bissau",
      "C) Freetown",
      "D) Banjul"
    ],
    "answer": "B",
    "explanation": "Bissau est la capitale de la Guinée-Bissau."
  },
  {
    "question": "Quelle est la capitale de la Gambie ?",
    "options": [
      "A) Banjul",
      "B) Dakar",
      "C) Freetown",
      "D) Bissau"
    ],
    "answer": "A",
    "explanation": "Banjul est la capitale de la Gambie."
  },
  {
    "question": "Quelle est la capitale du Liberia ?",
    "options": [
      "A) Freetown",
      "B) Accra",
      "C) Monrovia",
      "D) Abidjan"
    ],
    "answer": "C",
    "explanation": "Monrovia est la capitale du Liberia."
  },
  {
    "question": "Quelle est la capitale de la Sierra Leone ?",
    "options": [
      "A) Monrovia",
      "B) Freetown",
      "C) Conakry",
      "D) Banjul"
    ],
    "answer": "B",
    "explanation": "Freetown est la capitale de la Sierra Leone."
  },
  {
    "question": "Quelle est la capitale de la République Centrafricaine ?",
    "options": [
      "A) Bangui",
      "B) Yaoundé",
      "C) Libreville",
      "D) Malabo"
    ],
    "answer": "A",
    "explanation": "Bangui est la capitale de la République Centrafricaine."
  },
  {
    "question": "Quel lac est le plus grand d'Afrique ?",
    "options": [
      "A) Lac Tanganyika",
      "B) Lac Tchad",
      "C) Lac Victoria",
      "D) Lac Malawi"
    ],
    "answer": "C",
    "explanation": "Le lac Victoria est le plus grand lac d'Afrique (environ 68 000 km²)."
  },
  {
    "question": "Qui a écrit « Les Fleurs du Mal » ?",
    "options": [
      "A) Arthur Rimbaud",
      "B) Charles Baudelaire",
      "C) Paul Verlaine",
      "D) Stéphane Mallarmé"
    ],
    "answer": "B",
    "explanation": "Charles Baudelaire a publié « Les Fleurs du Mal » en 1857."
  },
  {
    "question": "Qui a écrit « Candide » ?",
    "options": [
      "A) Montesquieu",
      "B) Rousseau",
      "C) Voltaire",
      "D) Diderot"
    ],
    "answer": "C",
    "explanation": "Voltaire a écrit « Candide ou l'Optimisme » en 1759."
  },
  {
    "question": "Quel fleuve est le plus long d'Europe ?",
    "options": [
      "A) Danube",
      "B) Rhin",
      "C) Volga",
      "D) Loire"
    ],
    "answer": "C",
    "explanation": "La Volga est le plus long fleuve d'Europe (environ 3 530 km)."
  },
  {
    "question": "En quelle année le Sénégal a-t-il accédé à l'indépendance ?",
    "options": [
      "A) 1958",
      "B) 1960",
      "C) 1962",
      "D) 1963"
    ],
    "answer": "B",
    "explanation": "Le Sénégal a proclamé son indépendance le 4 avril 1960."
  },
  {
    "question": "Quelle est la principale base de lancement d'engins spatiaux aux États-Unis ?",
    "options": [
      "A) Houston",
      "B) Cap Canaveral",
      "C) Los Angeles",
      "D) Washington"
    ],
    "answer": "B",
    "explanation": "Cap Canaveral (Kennedy Space Center) est la principale base spatiale américaine."
  },
  {
    "question": "Depuis 2020, quel territoire pourrait devenir le 51ème État des États-Unis ?",
    "options": [
      "A) Porto Rico",
      "B) Guam",
      "C) Washington D.C.",
      "D) Samoa américaines"
    ],
    "answer": "A",
    "explanation": "Porto Rico a voté en 2020 en faveur de son intégration comme 51ème État."
  },
  {
    "question": "Combien de districts administratifs compte la Côte d'Ivoire ?",
    "options": [
      "A) 10",
      "B) 12",
      "C) 14",
      "D) 31"
    ],
    "answer": "C",
    "explanation": "La Côte d'Ivoire compte 14 districts, dont 2 districts autonomes (Abidjan et Yamoussoukro)."
  },
  {
    "question": "Quel est le symbole chimique du fer ?",
    "options": [
      "A) Fr",
      "B) Fe",
      "C) Fa",
      "D) Fi"
    ],
    "answer": "B",
    "explanation": "Le symbole du fer est Fe (du latin 'ferrum')."
  },
  {
    "question": "Quel est le cri de l'éléphant ?",
    "options": [
      "A) Barrit",
      "B) Rugit",
      "C) Mugit",
      "D) Brame"
    ],
    "answer": "A",
    "explanation": "L'éléphant barrit."
  },
  {
    "question": "Quel est le cri du cheval ?",
    "options": [
      "A) Brait",
      "B) Mugit",
      "C) Hennit",
      "D) Bêle"
    ],
    "answer": "C",
    "explanation": "Le cheval hennit."
  },
  {
    "question": "Quel est le plus grand fleuve de Côte d'Ivoire ?",
    "options": [
      "A) Le Sassandra",
      "B) Le Bandama",
      "C) Le Comoé",
      "D) Le Cavally"
    ],
    "answer": "B",
    "explanation": "Le Bandama est le plus grand fleuve de Côte d'Ivoire (environ 1 050 km)."
  },
  {
    "question": "Quel organe détient le pouvoir législatif en Côte d'Ivoire ?",
    "options": [
      "A) Le gouvernement",
      "B) Le Sénat seul",
      "C) L'Assemblée nationale et le Sénat",
      "D) La Cour suprême"
    ],
    "answer": "C",
    "explanation": "Le Parlement ivoirien est bicaméral : Assemblée nationale et Sénat."
  },
  {
    "question": "Quelle est la religion la plus pratiquée dans le monde ?",
    "options": [
      "A) L'islam",
      "B) Le christianisme",
      "C) L'hindouisme",
      "D) Le bouddhisme"
    ],
    "answer": "B",
    "explanation": "Le christianisme est la religion la plus pratiquée avec environ 2,4 milliards de fidèles."
  },
  {
    "question": "Quel pays africain a accueilli la CAN 2023 ?",
    "options": [
      "A) Cameroun",
      "B) Côte d'Ivoire",
      "C) Sénégal",
      "D) Nigeria"
    ],
    "answer": "B",
    "explanation": "La Côte d'Ivoire a accueilli la CAN 2023 (jouée en janvier-février 2024)."
  },
  {
    "question": "Qui a remporté la CAN 2023 ?",
    "options": [
      "A) Le Nigeria",
      "B) Le Sénégal",
      "C) La Côte d'Ivoire",
      "D) La RDC"
    ],
    "answer": "C",
    "explanation": "La Côte d'Ivoire a remporté la CAN 2023 en battant le Nigeria en finale."
  },
  {
    "question": "Quel est le symbole chimique du cuivre ?",
    "options": [
      "A) Cr",
      "B) Cu",
      "C) Co",
      "D) Ci"
    ],
    "answer": "B",
    "explanation": "Le symbole du cuivre est Cu (du latin 'cuprum')."
  },
  {
    "question": "Quel organe du corps humain produit l'insuline ?",
    "options": [
      "A) Le foie",
      "B) Le rein",
      "C) Le pancréas",
      "D) La rate"
    ],
    "answer": "C",
    "explanation": "Le pancréas produit l'insuline qui régule le taux de glucose dans le sang."
  },
  {
    "question": "Quel est le plus grand pays d'Afrique en superficie ?",
    "options": [
      "A) RDC",
      "B) Soudan",
      "C) Algérie",
      "D) Libye"
    ],
    "answer": "C",
    "explanation": "L'Algérie est le plus grand pays d'Afrique avec environ 2,38 millions de km²."
  },
  {
    "question": "Qui a écrit « Une vie de boy » ?",
    "options": [
      "A) Mongo Béti",
      "B) Ferdinand Oyono",
      "C) Camara Laye",
      "D) Cheikh Hamidou Kane"
    ],
    "answer": "B",
    "explanation": "Ferdinand Oyono, écrivain camerounais, a publié « Une vie de boy » en 1956."
  },
  {
    "question": "Qui a écrit « L'aventure ambiguë » ?",
    "options": [
      "A) Birago Diop",
      "B) Cheikh Hamidou Kane",
      "C) Ousmane Sembène",
      "D) Léopold Sédar Senghor"
    ],
    "answer": "B",
    "explanation": "Cheikh Hamidou Kane, écrivain sénégalais, a publié ce roman en 1961."
  },
  {
    "question": "Quelle est la capitale de la Guinée équatoriale ?",
    "options": [
      "A) Bata",
      "B) Malabo",
      "C) Libreville",
      "D) Douala"
    ],
    "answer": "B",
    "explanation": "Malabo est la capitale de la Guinée équatoriale."
  },
  {
    "question": "Quelle est la capitale du Soudan ?",
    "options": [
      "A) Khartoum",
      "B) Djouba",
      "C) Le Caire",
      "D) Asmara"
    ],
    "answer": "A",
    "explanation": "Khartoum est la capitale du Soudan."
  },
  {
    "question": "Quelle est la capitale du Soudan du Sud ?",
    "options": [
      "A) Khartoum",
      "B) Djouba",
      "C) Kampala",
      "D) Nairobi"
    ],
    "answer": "B",
    "explanation": "Djouba (Juba) est la capitale du Soudan du Sud."
  },
  {
    "question": "Quel pays a pour monnaie le Yen ?",
    "options": [
      "A) Chine",
      "B) Corée du Sud",
      "C) Japon",
      "D) Thaïlande"
    ],
    "answer": "C",
    "explanation": "Le Yen est la monnaie du Japon."
  },
  {
    "question": "Quel est le plus petit continent ?",
    "options": [
      "A) Antarctique",
      "B) Europe",
      "C) Océanie",
      "D) Amérique du Sud"
    ],
    "answer": "C",
    "explanation": "L'Océanie est le plus petit continent."
  },
  {
    "question": "Combien d'arrondissements compte la ville d'Abidjan ?",
    "options": [
      "A) 10",
      "B) 13",
      "C) 15",
      "D) 20"
    ],
    "answer": "A",
    "explanation": "La ville d'Abidjan compte 10 communes (arrondissements)."
  },
  {
    "question": "Quel est le sigle de la monnaie utilisée en Côte d'Ivoire ?",
    "options": [
      "A) CDF",
      "B) XOF",
      "C) EUR",
      "D) GHS"
    ],
    "answer": "B",
    "explanation": "XOF est le code ISO du franc CFA de l'Afrique de l'Ouest (BCEAO)."
  },
  {
    "question": "Quel savant grec est considéré comme le père de la médecine ?",
    "options": [
      "A) Aristote",
      "B) Hippocrate",
      "C) Galien",
      "D) Archimède"
    ],
    "answer": "B",
    "explanation": "Hippocrate (460-370 av. J.-C.) est considéré comme le père de la médecine."
  },
  {
    "question": "Quel pays africain n'a jamais été colonisé ?",
    "options": [
      "A) Ghana",
      "B) Liberia",
      "C) Éthiopie",
      "D) Liberia et Éthiopie"
    ],
    "answer": "D",
    "explanation": "L'Éthiopie et le Liberia sont les deux seuls pays africains n'ayant jamais été colonisés."
  },
  {
    "question": "Qui a découvert la pénicilline ?",
    "options": [
      "A) Louis Pasteur",
      "B) Alexander Fleming",
      "C) Robert Koch",
      "D) Jonas Salk"
    ],
    "answer": "B",
    "explanation": "Alexander Fleming a découvert la pénicilline (antibiotique) en 1928."
  },
  {
    "question": "Quel est le fleuve le plus long du monde ?",
    "options": [
      "A) Amazone",
      "B) Nil",
      "C) Mississippi",
      "D) Yangzi Jiang"
    ],
    "answer": "B",
    "explanation": "Le Nil est le fleuve le plus long du monde avec environ 6 650 km."
  },
  {
    "question": "En quelle année les attentats du 11 septembre ont-ils eu lieu ?",
    "options": [
      "A) 2000",
      "B) 2001",
      "C) 2002",
      "D) 2003"
    ],
    "answer": "B",
    "explanation": "Les attentats du World Trade Center ont eu lieu le 11 septembre 2001."
  },
  {
    "question": "Quel philosophe grec est l'auteur de « La République » ?",
    "options": [
      "A) Aristote",
      "B) Socrate",
      "C) Platon",
      "D) Épicure"
    ],
    "answer": "C",
    "explanation": "Platon a écrit « La République » où il développe sa vision de la cité idéale."
  },
  {
    "question": "Quelle est la capitale de Madagascar ?",
    "options": [
      "A) Moroni",
      "B) Antananarivo",
      "C) Maputo",
      "D) Victoria"
    ],
    "answer": "B",
    "explanation": "Antananarivo est la capitale de Madagascar."
  },
  {
    "question": "Quel organe du corps humain filtre le sang ?",
    "options": [
      "A) Le cœur",
      "B) Le foie",
      "C) Le rein",
      "D) Le poumon"
    ],
    "answer": "C",
    "explanation": "Les reins filtrent le sang pour éliminer les déchets sous forme d'urine."
  }
];

const THEME_4 = [
  {
    "question": "En quelle année l'ONU a-t-elle été officiellement créée ?",
    "options": [
      "A) 1945",
      "B) 1946",
      "C) 1944",
      "D) 1950"
    ],
    "answer": "A",
    "explanation": "L'ONU a été créée le 24 octobre 1945."
  },
  {
    "question": "Combien de membres permanents compte le Conseil de Sécurité de l'ONU ?",
    "options": [
      "A) 3",
      "B) 5",
      "C) 7",
      "D) 10"
    ],
    "answer": "B",
    "explanation": "Il y a 5 membres permanents : USA, Russie, Chine, France, Royaume-Uni."
  },
  {
    "question": "Où siège la Cour internationale de Justice ?",
    "options": [
      "A) New York",
      "B) La Haye",
      "C) Genève",
      "D) Paris"
    ],
    "answer": "B",
    "explanation": "La CIJ siège à La Haye aux Pays-Bas."
  },
  {
    "question": "Quel Secrétaire Général de l'ONU a obtenu le prix Nobel de la paix en 2001 ?",
    "options": [
      "A) Ban Ki-moon",
      "B) Kofi Annan",
      "C) Boutros Boutros-Ghali",
      "D) António Guterres"
    ],
    "answer": "B",
    "explanation": "Kofi Annan, Secrétaire Général ghanéen, a reçu le prix Nobel en 2001."
  },
  {
    "question": "En quelle année a été créée l'OTAN ?",
    "options": [
      "A) 1949",
      "B) 1945",
      "C) 1955",
      "D) 1960"
    ],
    "answer": "A",
    "explanation": "L'OTAN a été créée le 4 avril 1949."
  },
  {
    "question": "Où siège le Parlement européen ?",
    "options": [
      "A) Bruxelles",
      "B) Luxembourg",
      "C) Strasbourg",
      "D) Paris"
    ],
    "answer": "C",
    "explanation": "Le Parlement européen siège principalement à Strasbourg."
  },
  {
    "question": "Combien d'États membres compte l'Union Européenne actuellement ?",
    "options": [
      "A) 25",
      "B) 27",
      "C) 28",
      "D) 30"
    ],
    "answer": "B",
    "explanation": "L'UE compte 27 États membres depuis le Brexit."
  },
  {
    "question": "Le Mercosur est une organisation de quel continent ?",
    "options": [
      "A) Afrique",
      "B) Asie",
      "C) Amérique du Sud",
      "D) Europe"
    ],
    "answer": "C",
    "explanation": "Le Mercosur est une organisation sud-américaine."
  },
  {
    "question": "Où se trouve le siège de l'Union africaine ?",
    "options": [
      "A) Accra",
      "B) Addis-Abeba",
      "C) Abidjan",
      "D) Le Caire"
    ],
    "answer": "B",
    "explanation": "Le siège de l'UA est à Addis-Abeba en Éthiopie."
  },
  {
    "question": "L'Union africaine a succédé à quelle organisation ?",
    "options": [
      "A) ONU",
      "B) OUA",
      "C) CEDEAO",
      "D) UEMOA"
    ],
    "answer": "B",
    "explanation": "L'UA a remplacé l'Organisation de l'Unité Africaine (OUA) en 2002."
  },
  {
    "question": "En quelle année a été créée la CEDEAO ?",
    "options": [
      "A) 1970",
      "B) 1975",
      "C) 1980",
      "D) 1985"
    ],
    "answer": "B",
    "explanation": "La CEDEAO a été créée en 1975."
  },
  {
    "question": "Combien d'États membres compte actuellement l'UEMOA ?",
    "options": [
      "A) 6",
      "B) 8",
      "C) 10",
      "D) 12"
    ],
    "answer": "B",
    "explanation": "L'UEMOA compte 8 États membres."
  },
  {
    "question": "Où se trouve le siège de l'UEMOA ?",
    "options": [
      "A) Dakar",
      "B) Ouagadougou",
      "C) Abidjan",
      "D) Lomé"
    ],
    "answer": "B",
    "explanation": "Le siège de l'UEMOA est à Ouagadougou au Burkina Faso."
  },
  {
    "question": "Où se trouve le siège de la Banque africaine de développement ?",
    "options": [
      "A) Abidjan",
      "B) Lagos",
      "C) Accra",
      "D) Dakar"
    ],
    "answer": "A",
    "explanation": "La BAD a son siège à Abidjan en Côte d'Ivoire."
  },
  {
    "question": "Quel organisme a reçu le prix Nobel de la Paix en 2012 ?",
    "options": [
      "A) L'ONU",
      "B) L'Union Européenne",
      "C) La CEDEAO",
      "D) L'UA"
    ],
    "answer": "B",
    "explanation": "L'Union Européenne a reçu le prix Nobel de la Paix en 2012."
  },
  {
    "question": "Combien de membres compte l'Assemblée générale de l'ONU ?",
    "options": [
      "A) 173",
      "B) 183",
      "C) 193",
      "D) 203"
    ],
    "answer": "C",
    "explanation": "L'Assemblée générale compte 193 États membres."
  },
  {
    "question": "Où se trouve le siège principal de l'ONU ?",
    "options": [
      "A) Washington",
      "B) Genève",
      "C) New York",
      "D) Paris"
    ],
    "answer": "C",
    "explanation": "Le siège principal de l'ONU est à New York."
  },
  {
    "question": "Qui est le Secrétaire Général actuel de l'ONU ?",
    "options": [
      "A) Ban Ki-moon",
      "B) Kofi Annan",
      "C) António Guterres",
      "D) Boutros Boutros-Ghali"
    ],
    "answer": "C",
    "explanation": "António Guterres est Secrétaire Général depuis 2017."
  },
  {
    "question": "Quel organe de l'ONU peut imposer des sanctions ?",
    "options": [
      "A) L'Assemblée générale",
      "B) Le Conseil de Sécurité",
      "C) La CIJ",
      "D) Le Secrétariat"
    ],
    "answer": "B",
    "explanation": "Le Conseil de Sécurité a le pouvoir d'imposer des sanctions."
  },
  {
    "question": "Combien de membres non permanents siègent au Conseil de Sécurité ?",
    "options": [
      "A) 5",
      "B) 8",
      "C) 10",
      "D) 15"
    ],
    "answer": "C",
    "explanation": "Il y a 10 membres non permanents élus pour 2 ans."
  },
  {
    "question": "Quelle est la durée du mandat des membres non permanents du Conseil de Sécurité ?",
    "options": [
      "A) 1 an",
      "B) 2 ans",
      "C) 3 ans",
      "D) 4 ans"
    ],
    "answer": "B",
    "explanation": "Les membres non permanents sont élus pour un mandat de 2 ans."
  },
  {
    "question": "Quel est le siège de l'Organisation mondiale de la Santé (OMS) ?",
    "options": [
      "A) Paris",
      "B) Genève",
      "C) New York",
      "D) Londres"
    ],
    "answer": "B",
    "explanation": "L'OMS a son siège à Genève en Suisse."
  },
  {
    "question": "En quelle année a été créée l'OUA (Organisation de l'Unité Africaine) ?",
    "options": [
      "A) 1960",
      "B) 1963",
      "C) 1965",
      "D) 1970"
    ],
    "answer": "B",
    "explanation": "L'OUA a été créée le 25 mai 1963 à Addis-Abeba."
  },
  {
    "question": "En quelle année l'UA a-t-elle remplacé l'OUA ?",
    "options": [
      "A) 1999",
      "B) 2000",
      "C) 2001",
      "D) 2002"
    ],
    "answer": "D",
    "explanation": "L'Union africaine a été créée en 2002."
  },
  {
    "question": "Combien d'États membres compte l'Union africaine ?",
    "options": [
      "A) 50",
      "B) 53",
      "C) 54",
      "D) 55"
    ],
    "answer": "D",
    "explanation": "L'UA compte 55 États membres africains."
  },
  {
    "question": "Quel pays africain n'est pas membre de l'Union africaine ?",
    "options": [
      "A) Somalie",
      "B) Soudan du Sud",
      "C) Maroc (suspendu)",
      "D) Aucun, tous sont membres"
    ],
    "answer": "D",
    "explanation": "Tous les 55 pays africains sont membres de l'UA."
  },
  {
    "question": "Où se trouve le siège de l'OTAN ?",
    "options": [
      "A) Washington",
      "B) Bruxelles",
      "C) Paris",
      "D) Londres"
    ],
    "answer": "B",
    "explanation": "Le siège de l'OTAN est à Bruxelles en Belgique."
  },
  {
    "question": "Combien de pays sont membres de l'OTAN actuellement ?",
    "options": [
      "A) 28",
      "B) 30",
      "C) 31",
      "D) 32"
    ],
    "answer": "C",
    "explanation": "L'OTAN compte 31 pays membres (avec la Finlande rejointe en 2023)."
  },
  {
    "question": "Quel article du traité de l'OTAN définit la défense collective ?",
    "options": [
      "A) Article 3",
      "B) Article 5",
      "C) Article 7",
      "D) Article 10"
    ],
    "answer": "B",
    "explanation": "L'article 5 stipule qu'une attaque contre un membre est une attaque contre tous."
  },
  {
    "question": "Où se trouve le siège de la Commission européenne ?",
    "options": [
      "A) Strasbourg",
      "B) Luxembourg",
      "C) Bruxelles",
      "D) Paris"
    ],
    "answer": "C",
    "explanation": "La Commission européenne siège à Bruxelles."
  },
  {
    "question": "Quelle monnaie est utilisée par l'UEMOA ?",
    "options": [
      "A) Le dollar",
      "B) L'euro",
      "C) Le franc CFA",
      "D) Le cedi"
    ],
    "answer": "C",
    "explanation": "Les pays de l'UEMOA utilisent le franc CFA."
  },
  {
    "question": "Combien d'États membres compte la CEDEAO ?",
    "options": [
      "A) 12",
      "B) 13",
      "C) 14",
      "D) 15"
    ],
    "answer": "D",
    "explanation": "La CEDEAO compte 15 États membres."
  },
  {
    "question": "Où se trouve le siège de la CEDEAO ?",
    "options": [
      "A) Dakar",
      "B) Abuja",
      "C) Accra",
      "D) Abidjan"
    ],
    "answer": "B",
    "explanation": "Le siège de la CEDEAO est à Abuja au Nigeria."
  },
  {
    "question": "Quelle organisation africaine est dédiée à l'intégration économique et monétaire ?",
    "options": [
      "A) L'UA",
      "B) La CEDEAO",
      "C) L'UEMOA",
      "D) La BAD"
    ],
    "answer": "C",
    "explanation": "L'UEMOA vise l'intégration économique et monétaire de ses membres."
  },
  {
    "question": "En quelle année a été créée l'Organisation mondiale du Commerce (OMC) ?",
    "options": [
      "A) 1985",
      "B) 1990",
      "C) 1995",
      "D) 2000"
    ],
    "answer": "C",
    "explanation": "L'OMC a été créée en 1995, succédant au GATT."
  },
  {
    "question": "Où se trouve le siège de l'OMC ?",
    "options": [
      "A) New York",
      "B) Genève",
      "C) Bruxelles",
      "D) Paris"
    ],
    "answer": "B",
    "explanation": "L'OMC a son siège à Genève en Suisse."
  },
  {
    "question": "Quel organe de l'ONU s'occupe de l'éducation, la science et la culture ?",
    "options": [
      "A) UNICEF",
      "B) UNESCO",
      "C) OMS",
      "D) FAO"
    ],
    "answer": "B",
    "explanation": "L'UNESCO est dédiée à l'éducation, la science et la culture."
  },
  {
    "question": "Où se trouve le siège de l'UNESCO ?",
    "options": [
      "A) Londres",
      "B) Rome",
      "C) Paris",
      "D) Genève"
    ],
    "answer": "C",
    "explanation": "L'UNESCO a son siège à Paris en France."
  },
  {
    "question": "Quel organe de l'ONU s'occupe des réfugiés ?",
    "options": [
      "A) UNICEF",
      "B) HCR",
      "C) OIM",
      "D) PNUD"
    ],
    "answer": "B",
    "explanation": "Le HCR (Haut-Commissariat aux Réfugiés) protège les réfugiés."
  },
  {
    "question": "Quel organe de l'ONU s'occupe des enfants ?",
    "options": [
      "A) UNICEF",
      "B) UNESCO",
      "C) OMS",
      "D) PAM"
    ],
    "answer": "A",
    "explanation": "L'UNICEF (Fonds des Nations Unies pour l'Enfance) protège les enfants."
  },
  {
    "question": "En quelle année a été créé le FMI (Fonds Monétaire International) ?",
    "options": [
      "A) 1944",
      "B) 1945",
      "C) 1946",
      "D) 1950"
    ],
    "answer": "A",
    "explanation": "Le FMI a été créé en 1944 lors de la conférence de Bretton Woods."
  },
  {
    "question": "Où se trouve le siège du FMI ?",
    "options": [
      "A) New York",
      "B) Washington",
      "C) Genève",
      "D) Londres"
    ],
    "answer": "B",
    "explanation": "Le FMI a son siège à Washington D.C. aux États-Unis."
  },
  {
    "question": "Où se trouve le siège de la Banque mondiale ?",
    "options": [
      "A) New York",
      "B) Washington",
      "C) Londres",
      "D) Genève"
    ],
    "answer": "B",
    "explanation": "La Banque mondiale a son siège à Washington D.C."
  },
  {
    "question": "Quel traité a créé l'Union européenne ?",
    "options": [
      "A) Traité de Rome",
      "B) Traité de Maastricht",
      "C) Traité de Lisbonne",
      "D) Traité de Paris"
    ],
    "answer": "B",
    "explanation": "Le traité de Maastricht (1992) a créé l'Union européenne."
  },
  {
    "question": "En quelle année le traité de Maastricht a-t-il été signé ?",
    "options": [
      "A) 1990",
      "B) 1992",
      "C) 1995",
      "D) 2000"
    ],
    "answer": "B",
    "explanation": "Le traité de Maastricht a été signé le 7 février 1992."
  },
  {
    "question": "Quelle organisation régionale réunit les pays d'Asie du Sud-Est ?",
    "options": [
      "A) APEC",
      "B) ASEAN",
      "C) SAARC",
      "D) BRICS"
    ],
    "answer": "B",
    "explanation": "L'ASEAN (Association des Nations de l'Asie du Sud-Est) réunit 10 pays."
  },
  {
    "question": "Combien de pays composent le G7 ?",
    "options": [
      "A) 5",
      "B) 7",
      "C) 8",
      "D) 10"
    ],
    "answer": "B",
    "explanation": "Le G7 comprend 7 pays industrialisés : USA, Canada, Japon, Allemagne, France, Royaume-Uni, Italie."
  },
  {
    "question": "Quel pays a été exclu du G8 en 2014 ?",
    "options": [
      "A) La Chine",
      "B) La Russie",
      "C) L'Inde",
      "D) Le Brésil"
    ],
    "answer": "B",
    "explanation": "La Russie a été exclue du G8 en 2014 suite à l'annexion de la Crimée."
  },
  {
    "question": "Que signifie BRICS ?",
    "options": [
      "A) Brésil, Russie, Inde, Chine, Suisse",
      "B) Brésil, Russie, Inde, Chine, Afrique du Sud",
      "C) Belgique, Russie, Iran, Chine, Sénégal",
      "D) Brésil, Roumanie, Inde, Canada, Suède"
    ],
    "answer": "B",
    "explanation": "BRICS = Brésil, Russie, Inde, Chine, South Africa (Afrique du Sud)."
  },
  {
    "question": "Quelle charte, proclamée en 1941 par Roosevelt et Churchill, annonça la création de l'ONU ?",
    "options": [
      "A) La Charte de San Francisco",
      "B) La Charte de l'Atlantique",
      "C) La Charte de Genève",
      "D) La Charte de Yalta"
    ],
    "answer": "B",
    "explanation": "La Charte de l'Atlantique, signée en août 1941, posa les bases de l'ONU."
  },
  {
    "question": "Lors de la conférence de Yalta (1945), quel dirigeant tenait le plus à la création de l'ONU ?",
    "options": [
      "A) Roosevelt",
      "B) Churchill",
      "C) Staline",
      "D) De Gaulle"
    ],
    "answer": "A",
    "explanation": "Le président américain Roosevelt fut le plus grand défenseur de la création de l'ONU."
  },
  {
    "question": "Quel est le dernier pays à avoir intégré l'ONU ?",
    "options": [
      "A) Le Monténégro",
      "B) Le Soudan du Sud",
      "C) Le Kosovo",
      "D) Le Timor oriental"
    ],
    "answer": "B",
    "explanation": "Le Soudan du Sud a rejoint l'ONU en 2011."
  },
  {
    "question": "Quelles sont les langues de travail au Secrétariat Général de l'ONU ?",
    "options": [
      "A) Français et Anglais",
      "B) Anglais et Espagnol",
      "C) Anglais et Chinois",
      "D) Français et Espagnol"
    ],
    "answer": "B",
    "explanation": "Les deux langues de travail au Secrétariat sont l'anglais et l'espagnol."
  },
  {
    "question": "Que représente la sculpture « Non-violence » devant le siège de l'ONU ?",
    "options": [
      "A) Une colombe",
      "B) Un revolver noué",
      "C) Un globe terrestre",
      "D) Des mains jointes"
    ],
    "answer": "B",
    "explanation": "La sculpture de Carl Fredrik Reuterswärd représente un revolver au canon noué."
  },
  {
    "question": "Quel est le statut de la Palestine à l'ONU ?",
    "options": [
      "A) Membre à part entière",
      "B) Membre associé",
      "C) Observateur",
      "D) Aucun statut"
    ],
    "answer": "C",
    "explanation": "La Palestine a un statut d'État observateur non membre à l'ONU."
  },
  {
    "question": "L'ONU dispose-t-elle d'une armée propre ?",
    "options": [
      "A) Oui, avec des soldats permanents",
      "B) Non, elle utilise les forces des États membres",
      "C) Oui, basée à Genève"
    ],
    "answer": "B",
    "explanation": "L'ONU n'a pas d'armée propre. Les casques bleus sont fournis par les États membres."
  },
  {
    "question": "Qui est l'actuel Secrétaire Général de l'OTAN ?",
    "options": [
      "A) Jens Stoltenberg",
      "B) Anders Rasmussen",
      "C) Mark Rutte",
      "D) Ursula von der Leyen"
    ],
    "answer": "C",
    "explanation": "Mark Rutte est devenu Secrétaire Général de l'OTAN en 2024."
  },
  {
    "question": "Quel est le dernier pays à avoir rejoint l'OTAN ?",
    "options": [
      "A) La Finlande",
      "B) L'Ukraine",
      "C) La Suède",
      "D) La Géorgie"
    ],
    "answer": "C",
    "explanation": "La Suède a rejoint l'OTAN le 7 mars 2024."
  },
  {
    "question": "Qui est le président en exercice de l'Union africaine ?",
    "options": [
      "A) Macky Sall",
      "B) Évariste N'dayishimiye",
      "C) Félix Tshisekedi",
      "D) William Ruto"
    ],
    "answer": "B",
    "explanation": "Évariste N'dayishimiye, président du Burundi, est président en exercice de l'UA."
  },
  {
    "question": "Combien de membres élus composent le Conseil de Paix et de Sécurité (CPS) de l'UA ?",
    "options": [
      "A) 10",
      "B) 15",
      "C) 20",
      "D) 25"
    ],
    "answer": "B",
    "explanation": "Le CPS de l'UA est composé de 15 membres élus."
  },
  {
    "question": "Combien de pays compte actuellement la CEDEAO ?",
    "options": [
      "A) 10",
      "B) 12",
      "C) 15",
      "D) 16"
    ],
    "answer": "B",
    "explanation": "La CEDEAO compte actuellement 12 pays après le retrait du Mali, du Burkina Faso et du Niger."
  },
  {
    "question": "Quel pays a été réintégré à la CEDEAO après sa suspension en 2021 ?",
    "options": [
      "A) Le Mali",
      "B) La Guinée",
      "C) Le Niger",
      "D) Le Burkina Faso"
    ],
    "answer": "B",
    "explanation": "La Guinée a été réintégrée à la CEDEAO après sa suspension suite au coup d'État de 2021."
  },
  {
    "question": "Quel est le statut juridique de l'AES (Alliance des États du Sahel) ?",
    "options": [
      "A) Une fédération d'États",
      "B) Une confédération d'États",
      "C) Une organisation régionale",
      "D) Une union économique"
    ],
    "answer": "B",
    "explanation": "L'AES (Mali, Burkina Faso, Niger) est une confédération d'États."
  },
  {
    "question": "La ZLECAF (Zone de Libre-Échange Continentale Africaine) relève de :",
    "options": [
      "A) La CEDEAO",
      "B) Un accord sous l'égide de l'UA",
      "C) L'ONU",
      "D) L'OMC"
    ],
    "answer": "B",
    "explanation": "La ZLECAF est un accord commercial continental sous l'égide de l'Union africaine."
  },
  {
    "question": "Où se trouve le siège de la SADC (Communauté de développement de l'Afrique australe) ?",
    "options": [
      "A) Gaborone",
      "B) Pretoria",
      "C) Lusaka",
      "D) Harare"
    ],
    "answer": "A",
    "explanation": "Le siège de la SADC est à Gaborone au Botswana."
  },
  {
    "question": "Quels sont les cinq pays ayant fait passer les BRICS aux BRICS+ ?",
    "options": [
      "A) Turquie, Argentine, Mexique, Thaïlande, Nigeria",
      "B) Indonésie, Éthiopie, Iran, Arabie Saoudite, Égypte",
      "C) Algérie, Vietnam, Bangladesh, Pakistan, Colombie",
      "D) Philippines, Malaisie, Kenya, Pérou, Pologne"
    ],
    "answer": "B",
    "explanation": "Les BRICS+ incluent l'Indonésie, l'Éthiopie, l'Iran, l'Arabie Saoudite et l'Égypte."
  },
  {
    "question": "Quel pays a été suspendu du Mercosur ?",
    "options": [
      "A) L'Argentine",
      "B) Le Venezuela",
      "C) Le Paraguay",
      "D) L'Uruguay"
    ],
    "answer": "B",
    "explanation": "Le Venezuela a été suspendu du Mercosur pour rupture de l'ordre démocratique."
  },
  {
    "question": "L'accord UE-MERCOSUR a-t-il été finalisé ?",
    "options": [
      "A) Oui",
      "B) Non",
      "C) Il est en cours de négociation"
    ],
    "answer": "A",
    "explanation": "L'accord de libre-échange UE-MERCOSUR a été signé."
  },
  {
    "question": "En quelle année la Côte d'Ivoire a-t-elle pris la présidence de la CEDEAO ?",
    "options": [
      "A) 2012",
      "B) 2015",
      "C) 2018",
      "D) 2020"
    ],
    "answer": "A",
    "explanation": "La Côte d'Ivoire a présidé la CEDEAO en 2012."
  },
  {
    "question": "Qui est le président actuel de la BAD (Banque africaine de développement) ?",
    "options": [
      "A) Sidi Ould Tah",
      "B) Akinwumi Adesina",
      "C) Donald Kaberuka",
      "D) Cristina Duarte"
    ],
    "answer": "A",
    "explanation": "Sidi Ould Tah est le président actuel de la BAD."
  },
  {
    "question": "Où a été signée en 1992 la Convention-cadre de l'ONU sur les changements climatiques ?",
    "options": [
      "A) Sommet de Kyoto",
      "B) Sommet de Paris",
      "C) Sommet de la Terre à Rio de Janeiro",
      "D) Sommet de Copenhague"
    ],
    "answer": "C",
    "explanation": "La Convention-cadre a été signée au Sommet de la Terre à Rio de Janeiro en 1992."
  },
  {
    "question": "Le mécanisme africain d'évaluation par les pairs relève de :",
    "options": [
      "A) La CEDEAO",
      "B) L'Union africaine",
      "C) L'ONU",
      "D) La BAD"
    ],
    "answer": "B",
    "explanation": "Le MAEP est un instrument de l'Union africaine pour promouvoir la bonne gouvernance."
  },
  {
    "question": "La Banque mondiale et le FMI sont-ils associés à l'ONU ?",
    "options": [
      "A) Oui, ce sont des institutions spécialisées",
      "B) Non, ils sont totalement indépendants",
      "C) Seulement la Banque mondiale"
    ],
    "answer": "A",
    "explanation": "La Banque mondiale et le FMI sont des institutions spécialisées du système des Nations Unies."
  },
  {
    "question": "Quelle est la deuxième puissance économique mondiale ?",
    "options": [
      "A) Le Japon",
      "B) L'Union européenne",
      "C) La Chine",
      "D) L'Inde"
    ],
    "answer": "C",
    "explanation": "La Chine est la deuxième puissance économique mondiale derrière les États-Unis."
  },
  {
    "question": "Qui est l'actuel président de la Commission de la CEDEAO ?",
    "options": [
      "A) Omar Touray",
      "B) Jean-Claude Brou",
      "C) Julius Maada Bio",
      "D) Nana Akufo-Addo"
    ],
    "answer": "C",
    "explanation": "Julius Maada Bio est le président actuel de la Commission de la CEDEAO."
  },
  {
    "question": "Qui est le président actuel de la Commission de l'UEMOA ?",
    "options": [
      "A) Abdoulaye Diop",
      "B) Cheickna Seydi Ahamadi Diawara",
      "C) Boureima Badini",
      "D) Soumaïla Cissé"
    ],
    "answer": "A",
    "explanation": "Abdoulaye Diop est le président actuel de la Commission de l'UEMOA."
  },
  {
    "question": "Où se trouve le siège de l'Organisation internationale de la Francophonie (OIF) ?",
    "options": [
      "A) Genève",
      "B) Bruxelles",
      "C) Paris",
      "D) Montréal"
    ],
    "answer": "C",
    "explanation": "Le siège de l'OIF est à Paris."
  },
  {
    "question": "Combien de pays membres compte l'Organisation internationale de la Francophonie ?",
    "options": [
      "A) 54",
      "B) 68",
      "C) 88",
      "D) 93"
    ],
    "answer": "C",
    "explanation": "L'OIF compte 88 États et gouvernements membres, observateurs et associés."
  },
  {
    "question": "Où se trouve le siège de la Cour pénale internationale (CPI) ?",
    "options": [
      "A) New York",
      "B) La Haye",
      "C) Genève",
      "D) Bruxelles"
    ],
    "answer": "B",
    "explanation": "La CPI siège à La Haye, aux Pays-Bas."
  },
  {
    "question": "En quelle année la CPI a-t-elle été créée par le Statut de Rome ?",
    "options": [
      "A) 1998",
      "B) 2000",
      "C) 2002",
      "D) 2005"
    ],
    "answer": "C",
    "explanation": "La CPI est entrée en vigueur le 1er juillet 2002, le Statut de Rome ayant été adopté en 1998."
  },
  {
    "question": "Qu'est-ce que la CEMAC ?",
    "options": [
      "A) Communauté Économique des États de l'Afrique de l'Ouest",
      "B) Communauté Économique et Monétaire de l'Afrique Centrale",
      "C) Commission Européenne des Marchés de Capitaux",
      "D) Comité Économique des Marchés Africains"
    ],
    "answer": "B",
    "explanation": "La CEMAC est la Communauté Économique et Monétaire de l'Afrique Centrale."
  },
  {
    "question": "Combien de pays composent la CEMAC ?",
    "options": [
      "A) 4",
      "B) 6",
      "C) 8",
      "D) 10"
    ],
    "answer": "B",
    "explanation": "La CEMAC compte 6 pays : Cameroun, Centrafrique, Congo, Gabon, Guinée équatoriale et Tchad."
  },
  {
    "question": "Où se trouve le siège de la Ligue arabe ?",
    "options": [
      "A) Riyad",
      "B) Le Caire",
      "C) Beyrouth",
      "D) Tunis"
    ],
    "answer": "B",
    "explanation": "Le siège de la Ligue arabe est au Caire, en Égypte."
  },
  {
    "question": "Combien de pays composent le G20 ?",
    "options": [
      "A) 19 pays + l'UE",
      "B) 20 pays exactement",
      "C) 18 pays + 2 organisations",
      "D) 20 pays + l'ONU"
    ],
    "answer": "A",
    "explanation": "Le G20 comprend 19 pays + l'Union européenne."
  },
  {
    "question": "Quelle est la différence entre le Conseil de l'Europe et le Conseil européen ?",
    "options": [
      "A) Aucune, c'est la même chose",
      "B) Le Conseil de l'Europe est une organisation distincte de l'UE",
      "C) Le Conseil européen est plus ancien",
      "D) Le Conseil de l'Europe fait partie de l'ONU"
    ],
    "answer": "B",
    "explanation": "Le Conseil de l'Europe (46 membres, siège à Strasbourg) est indépendant de l'UE. Le Conseil européen est un organe de l'UE."
  },
  {
    "question": "En quelle année ont été signés les Accords de Paris sur le climat ?",
    "options": [
      "A) 2012",
      "B) 2015",
      "C) 2018",
      "D) 2020"
    ],
    "answer": "B",
    "explanation": "L'Accord de Paris sur le climat a été adopté le 12 décembre 2015 lors de la COP21."
  },
  {
    "question": "Combien de langues officielles compte l'ONU ?",
    "options": [
      "A) 4",
      "B) 5",
      "C) 6",
      "D) 7"
    ],
    "answer": "C",
    "explanation": "L'ONU a 6 langues officielles : anglais, arabe, chinois, espagnol, français et russe."
  },
  {
    "question": "Quel organe de l'ONU s'occupe de l'alimentation et l'agriculture ?",
    "options": [
      "A) PAM",
      "B) FAO",
      "C) FIDA",
      "D) UNICEF"
    ],
    "answer": "B",
    "explanation": "La FAO (Organisation des Nations Unies pour l'Alimentation et l'Agriculture) a son siège à Rome."
  },
  {
    "question": "Où se trouve le siège de la FAO ?",
    "options": [
      "A) Paris",
      "B) Rome",
      "C) Genève",
      "D) New York"
    ],
    "answer": "B",
    "explanation": "Le siège de la FAO est à Rome, en Italie."
  },
  {
    "question": "Quel est le rôle principal du PAM (Programme Alimentaire Mondial) ?",
    "options": [
      "A) Financer les pays pauvres",
      "B) Lutter contre la faim dans le monde",
      "C) Protéger les réfugiés",
      "D) Promouvoir l'éducation"
    ],
    "answer": "B",
    "explanation": "Le PAM est l'organisme d'aide alimentaire de l'ONU, luttant contre la faim."
  },
  {
    "question": "Quel pays membre fondateur a quitté l'Union européenne ?",
    "options": [
      "A) La Suisse",
      "B) La Norvège",
      "C) Le Royaume-Uni",
      "D) L'Islande"
    ],
    "answer": "C",
    "explanation": "Le Royaume-Uni a quitté l'UE le 31 janvier 2020 (Brexit)."
  },
  {
    "question": "En quelle année le Brexit a-t-il été effectif ?",
    "options": [
      "A) 2016",
      "B) 2018",
      "C) 2020",
      "D) 2021"
    ],
    "answer": "C",
    "explanation": "Le Brexit est devenu effectif le 31 janvier 2020 (le référendum avait eu lieu en 2016)."
  },
  {
    "question": "Combien de pays membres l'OPEP compte-t-elle actuellement ?",
    "options": [
      "A) 10",
      "B) 12",
      "C) 13",
      "D) 15"
    ],
    "answer": "C",
    "explanation": "L'OPEP compte 13 pays membres producteurs de pétrole."
  },
  {
    "question": "Quel organisme de l'ONU est chargé du maintien de la paix ?",
    "options": [
      "A) L'Assemblée générale",
      "B) Le Conseil de Sécurité",
      "C) La CIJ",
      "D) Le Conseil économique et social"
    ],
    "answer": "B",
    "explanation": "Le Conseil de Sécurité est l'organe principal chargé du maintien de la paix et de la sécurité internationales."
  },
  {
    "question": "Quel est le nombre total de membres du Conseil de Sécurité (permanents + non permanents) ?",
    "options": [
      "A) 10",
      "B) 12",
      "C) 15",
      "D) 20"
    ],
    "answer": "C",
    "explanation": "Le Conseil de Sécurité compte 15 membres : 5 permanents + 10 non permanents."
  },
  {
    "question": "Quelle convention internationale protège les droits de l'Homme ?",
    "options": [
      "A) Convention de Genève",
      "B) Déclaration universelle des droits de l'homme",
      "C) Traité de Versailles",
      "D) Charte de l'Atlantique"
    ],
    "answer": "B",
    "explanation": "La DUDH a été adoptée le 10 décembre 1948 par l'Assemblée générale de l'ONU."
  },
  {
    "question": "En quelle année la Déclaration universelle des droits de l'homme a-t-elle été adoptée ?",
    "options": [
      "A) 1945",
      "B) 1948",
      "C) 1950",
      "D) 1955"
    ],
    "answer": "B",
    "explanation": "La DUDH a été adoptée le 10 décembre 1948 à Paris."
  },
  {
    "question": "Où se trouve le siège de l'Organisation Internationale du Travail (OIT) ?",
    "options": [
      "A) New York",
      "B) Genève",
      "C) Paris",
      "D) Bruxelles"
    ],
    "answer": "B",
    "explanation": "L'OIT a son siège à Genève, en Suisse."
  },
  {
    "question": "Quel accord de libre-échange lie les États-Unis, le Mexique et le Canada ?",
    "options": [
      "A) ALENA",
      "B) ACEUM (USMCA)",
      "C) MERCOSUR",
      "D) APEC"
    ],
    "answer": "B",
    "explanation": "L'ACEUM (ou USMCA en anglais) a remplacé l'ALENA en 2020."
  }
];

const THEME_5 = [
  {
    "question": "Complete: 'If I ___ you, I would apologize.'",
    "options": [
      "A) am",
      "B) was",
      "C) were",
      "D) be"
    ],
    "answer": "C",
    "explanation": "Type 2 conditional uses 'were' for all persons with the verb 'to be'."
  },
  {
    "question": "Which sentence is correct?",
    "options": [
      "A) If it will rain, I stay home",
      "B) If it rains, I will stay home",
      "C) If it rains, I would stay home"
    ],
    "answer": "B",
    "explanation": "Type 1 conditional: never use 'will' immediately after 'if'. Structure: If + Present, will + verb."
  },
  {
    "question": "'You ___ park here. It's forbidden.'",
    "options": [
      "A) mustn't",
      "B) needn't",
      "C) shouldn't",
      "D) can't"
    ],
    "answer": "A",
    "explanation": "'Mustn't' expresses prohibition (interdiction). 'Needn't' means no obligation."
  },
  {
    "question": "Choose the correct article: 'She is ___ honest woman.'",
    "options": [
      "A) a",
      "B) an",
      "C) the",
      "D) Ø"
    ],
    "answer": "B",
    "explanation": "Use 'an' before words starting with a vowel SOUND. 'Honest' starts with a silent 'h'."
  },
  {
    "question": "'I travel ___ bus every day.'",
    "options": [
      "A) by",
      "B) on the",
      "C) in a",
      "D) with"
    ],
    "answer": "A",
    "explanation": "'By' + means of transport (without article) is used for general transport."
  },
  {
    "question": "'If I had known, I ___ differently.'",
    "options": [
      "A) would act",
      "B) would have acted",
      "C) will act",
      "D) acted"
    ],
    "answer": "B",
    "explanation": "Type 3 conditional (past regret): If + Past Perfect → Would have + Past Participle."
  },
  {
    "question": "'You ___ come if you don't want to.'",
    "options": [
      "A) mustn't",
      "B) don't have to",
      "C) can't",
      "D) shouldn't"
    ],
    "answer": "B",
    "explanation": "'Don't have to' expresses absence of obligation. 'Mustn't' is prohibition."
  },
  {
    "question": "Which preposition? 'The meeting is ___ Monday.'",
    "options": [
      "A) at",
      "B) in",
      "C) on",
      "D) by"
    ],
    "answer": "C",
    "explanation": "Use 'on' for specific days: on Monday, on Tuesday, on my birthday."
  },
  {
    "question": "'She ___ speak three languages.' (Present ability)",
    "options": [
      "A) can",
      "B) could",
      "C) may",
      "D) might"
    ],
    "answer": "A",
    "explanation": "'Can' expresses ability in the present. 'Could' is past or politeness."
  },
  {
    "question": "'___ water boils at 100°C.'",
    "options": [
      "A) A",
      "B) The",
      "C) Ø (no article)",
      "D) An"
    ],
    "answer": "C",
    "explanation": "No article for general truths with uncountable nouns like 'water'."
  },
  {
    "question": "'If water reaches 0°C, it ___.'",
    "options": [
      "A) freezes",
      "B) will freeze",
      "C) would freeze",
      "D) freeze"
    ],
    "answer": "A",
    "explanation": "Type Zero conditional (general truth): If + Present → Present."
  },
  {
    "question": "'He ___ be at home. His car is in the driveway.' (Deduction)",
    "options": [
      "A) might",
      "B) must",
      "C) should",
      "D) can"
    ],
    "answer": "B",
    "explanation": "'Must' expresses strong deduction/logical certainty (quasi-certitude)."
  },
  {
    "question": "'I was sitting ___ the train when I saw him.'",
    "options": [
      "A) by",
      "B) in",
      "C) on",
      "D) at"
    ],
    "answer": "C",
    "explanation": "'On' is used for public transport: on the bus, on the train, on the plane."
  },
  {
    "question": "'You ___ to see a doctor. You look ill.' (Advice)",
    "options": [
      "A) ought",
      "B) must",
      "C) might",
      "D) need"
    ],
    "answer": "A",
    "explanation": "'Ought to' expresses advice/recommendation (conseil)."
  },
  {
    "question": "'___ dogs are loyal animals.'",
    "options": [
      "A) A",
      "B) The",
      "C) Ø (no article)",
      "D) An"
    ],
    "answer": "C",
    "explanation": "No article for general statements with plural nouns."
  },
  {
    "question": "'The concert is ___ 8 PM.'",
    "options": [
      "A) at",
      "B) in",
      "C) on",
      "D) by"
    ],
    "answer": "A",
    "explanation": "Use 'at' for precise times: at 8 PM, at noon, at midnight."
  },
  {
    "question": "'If she ___ harder, she would pass the exam.'",
    "options": [
      "A) studies",
      "B) studied",
      "C) will study",
      "D) study"
    ],
    "answer": "B",
    "explanation": "Type 2 conditional (imaginary present): If + Past Simple → Would + verb."
  },
  {
    "question": "'He travels to work ___ car.'",
    "options": [
      "A) by",
      "B) in",
      "C) on",
      "D) with"
    ],
    "answer": "A",
    "explanation": "'By car' (no article) for general transport method. 'In a car' for specific vehicle."
  },
  {
    "question": "'It ___ rain later. Take an umbrella.' (Possibility ~50%)",
    "options": [
      "A) must",
      "B) may",
      "C) should",
      "D) will"
    ],
    "answer": "B",
    "explanation": "'May' expresses possibility (~50% probability)."
  },
  {
    "question": "'My birthday is ___ July 15th.'",
    "options": [
      "A) at",
      "B) in",
      "C) on",
      "D) by"
    ],
    "answer": "C",
    "explanation": "Use 'on' for specific dates: on July 15th, on December 25th."
  },
  {
    "question": "'She has lived here ___ 2010.'",
    "options": [
      "A) since",
      "B) for",
      "C) during",
      "D) from"
    ],
    "answer": "A",
    "explanation": "'Since' is used with a specific point in time (depuis 2010)."
  },
  {
    "question": "'I have studied English ___ five years.'",
    "options": [
      "A) since",
      "B) for",
      "C) during",
      "D) ago"
    ],
    "answer": "B",
    "explanation": "'For' is used with a duration (pendant 5 ans)."
  },
  {
    "question": "'I visited Paris three years ___.'",
    "options": [
      "A) since",
      "B) for",
      "C) ago",
      "D) before"
    ],
    "answer": "C",
    "explanation": "'Ago' is used with past simple for a point in the past (il y a 3 ans)."
  },
  {
    "question": "'He ___ finished his homework yet.'",
    "options": [
      "A) hasn't",
      "B) didn't",
      "C) doesn't",
      "D) wasn't"
    ],
    "answer": "A",
    "explanation": "'Yet' with present perfect negative: hasn't/haven't + past participle."
  },
  {
    "question": "'Have you ___ been to Japan?'",
    "options": [
      "A) yet",
      "B) ever",
      "C) already",
      "D) never"
    ],
    "answer": "B",
    "explanation": "'Ever' is used in questions with present perfect (déjà dans ta vie)."
  },
  {
    "question": "'I have ___ finished my work.'",
    "options": [
      "A) yet",
      "B) ever",
      "C) already",
      "D) ago"
    ],
    "answer": "C",
    "explanation": "'Already' with present perfect affirmative: have already + past participle."
  },
  {
    "question": "'Neither John ___ Mary came to the party.'",
    "options": [
      "A) or",
      "B) nor",
      "C) and",
      "D) but"
    ],
    "answer": "B",
    "explanation": "'Neither...nor' is the correct correlative conjunction."
  },
  {
    "question": "'Either you apologize, ___ I will leave.'",
    "options": [
      "A) and",
      "B) but",
      "C) or",
      "D) nor"
    ],
    "answer": "C",
    "explanation": "'Either...or' expresses a choice/alternative."
  },
  {
    "question": "'She is not only intelligent ___ also kind.'",
    "options": [
      "A) and",
      "B) but",
      "C) or",
      "D) yet"
    ],
    "answer": "B",
    "explanation": "'Not only...but also' is the correct correlative conjunction."
  },
  {
    "question": "'I would rather ___ at home today.'",
    "options": [
      "A) stay",
      "B) to stay",
      "C) staying",
      "D) stayed"
    ],
    "answer": "A",
    "explanation": "'Would rather' is followed by base form (infinitive without 'to')."
  },
  {
    "question": "'She made me ___ my homework.'",
    "options": [
      "A) do",
      "B) to do",
      "C) doing",
      "D) did"
    ],
    "answer": "A",
    "explanation": "'Make' is followed by object + base form (without 'to')."
  },
  {
    "question": "'He let me ___ his car.'",
    "options": [
      "A) use",
      "B) to use",
      "C) using",
      "D) used"
    ],
    "answer": "A",
    "explanation": "'Let' is followed by object + base form (without 'to')."
  },
  {
    "question": "'She wants me ___ her.'",
    "options": [
      "A) help",
      "B) to help",
      "C) helping",
      "D) helped"
    ],
    "answer": "B",
    "explanation": "'Want' is followed by object + to-infinitive."
  },
  {
    "question": "'I'm looking forward ___ you.'",
    "options": [
      "A) see",
      "B) to see",
      "C) to seeing",
      "D) seeing"
    ],
    "answer": "C",
    "explanation": "'Look forward to' is followed by gerund (verb + -ing)."
  },
  {
    "question": "'He is used ___ early.'",
    "options": [
      "A) wake up",
      "B) to wake up",
      "C) to waking up",
      "D) waking up"
    ],
    "answer": "C",
    "explanation": "'Be used to' (être habitué à) is followed by gerund."
  },
  {
    "question": "'He used ___ in London.'",
    "options": [
      "A) live",
      "B) to live",
      "C) living",
      "D) lived"
    ],
    "answer": "B",
    "explanation": "'Used to' (habitude passée) is followed by base form."
  },
  {
    "question": "'The book ___ by millions of people.'",
    "options": [
      "A) was read",
      "B) read",
      "C) is reading",
      "D) reads"
    ],
    "answer": "A",
    "explanation": "Passive voice (past): was/were + past participle."
  },
  {
    "question": "'The house ___ built in 1990.'",
    "options": [
      "A) is",
      "B) was",
      "C) has",
      "D) had"
    ],
    "answer": "B",
    "explanation": "Passive voice with specific past date uses 'was/were'."
  },
  {
    "question": "'English ___ all over the world.'",
    "options": [
      "A) speaks",
      "B) is spoken",
      "C) is speaking",
      "D) has spoken"
    ],
    "answer": "B",
    "explanation": "Passive voice (present): is/are + past participle."
  },
  {
    "question": "'I wish I ___ rich.'",
    "options": [
      "A) am",
      "B) was",
      "C) were",
      "D) be"
    ],
    "answer": "C",
    "explanation": "'I wish' + past tense for present unreal situation. Use 'were' for 'to be'."
  },
  {
    "question": "'I wish I ___ studied harder.' (Past regret)",
    "options": [
      "A) have",
      "B) had",
      "C) would",
      "D) could"
    ],
    "answer": "B",
    "explanation": "'I wish' + past perfect for past regret."
  },
  {
    "question": "'If only I ___ more time!'",
    "options": [
      "A) have",
      "B) had",
      "C) will have",
      "D) would have"
    ],
    "answer": "B",
    "explanation": "'If only' + past tense for present wish/regret."
  },
  {
    "question": "'He asked me where I ___.'",
    "options": [
      "A) live",
      "B) lived",
      "C) am living",
      "D) lives"
    ],
    "answer": "B",
    "explanation": "Reported speech: present → past (backshift)."
  },
  {
    "question": "'She said she ___ come tomorrow.'",
    "options": [
      "A) will",
      "B) would",
      "C) can",
      "D) may"
    ],
    "answer": "B",
    "explanation": "Reported speech: 'will' becomes 'would'."
  },
  {
    "question": "'There ___ many people at the party yesterday.'",
    "options": [
      "A) was",
      "B) were",
      "C) is",
      "D) are"
    ],
    "answer": "B",
    "explanation": "'There were' for plural subjects in the past."
  },
  {
    "question": "'There ___ a problem with the system.'",
    "options": [
      "A) is",
      "B) are",
      "C) was",
      "D) were"
    ],
    "answer": "A",
    "explanation": "'There is' for singular subjects in the present."
  },
  {
    "question": "'Few people ___ the answer.'",
    "options": [
      "A) knows",
      "B) know",
      "C) knowing",
      "D) knew"
    ],
    "answer": "B",
    "explanation": "'Few people' is plural, so use 'know' (no -s)."
  },
  {
    "question": "'Each student ___ a book.'",
    "options": [
      "A) have",
      "B) has",
      "C) having",
      "D) are having"
    ],
    "answer": "B",
    "explanation": "'Each' is singular, so use 'has'."
  },
  {
    "question": "'Neither of the answers ___ correct.'",
    "options": [
      "A) is",
      "B) are",
      "C) were",
      "D) being"
    ],
    "answer": "A",
    "explanation": "'Neither' is singular, so use 'is'."
  },
  {
    "question": "'The team ___ playing well.' (as a unit)",
    "options": [
      "A) is",
      "B) are",
      "C) was",
      "D) were"
    ],
    "answer": "A",
    "explanation": "Collective nouns can be singular (unit) or plural (individuals). Here, 'is' for unit."
  },
  {
    "question": "'She is ___ than her sister.' (intelligent)",
    "options": [
      "A) more intelligent",
      "B) most intelligent",
      "C) intelligenter",
      "D) more intelligenter"
    ],
    "answer": "A",
    "explanation": "Long adjectives use 'more' for comparatives: more intelligent."
  },
  {
    "question": "'He is the ___ student in the class.'",
    "options": [
      "A) most tallest",
      "B) tallest",
      "C) more tall",
      "D) taller"
    ],
    "answer": "B",
    "explanation": "Short adjectives use '-est' for superlatives: the tallest."
  },
  {
    "question": "'You like coffee, ___?'",
    "options": [
      "A) don't you",
      "B) do you",
      "C) isn't it",
      "D) aren't you"
    ],
    "answer": "A",
    "explanation": "Question tags: positive statement → negative tag. 'You like' → 'don't you?'"
  },
  {
    "question": "'She can't swim, ___?'",
    "options": [
      "A) can't she",
      "B) can she",
      "C) could she",
      "D) does she"
    ],
    "answer": "B",
    "explanation": "Question tags: negative statement → positive tag. 'Can't swim' → 'can she?'"
  },
  {
    "question": "'The man ___ lives next door is a doctor.'",
    "options": [
      "A) which",
      "B) who",
      "C) whom",
      "D) whose"
    ],
    "answer": "B",
    "explanation": "'Who' is used for people as subject in relative clauses."
  },
  {
    "question": "'The book ___ I read was fascinating.'",
    "options": [
      "A) who",
      "B) which",
      "C) whose",
      "D) whom"
    ],
    "answer": "B",
    "explanation": "'Which' (or 'that') is used for things in relative clauses."
  },
  {
    "question": "'The girl ___ father is a pilot studies here.'",
    "options": [
      "A) who",
      "B) which",
      "C) whose",
      "D) whom"
    ],
    "answer": "C",
    "explanation": "'Whose' indicates possession in relative clauses."
  },
  {
    "question": "'If I ___ about the meeting, I would have attended.'",
    "options": [
      "A) know",
      "B) knew",
      "C) had known",
      "D) have known"
    ],
    "answer": "C",
    "explanation": "Type 3 conditional: If + Past Perfect → Would have + Past Participle."
  },
  {
    "question": "'She asked me ___ I was going.'",
    "options": [
      "A) where",
      "B) that",
      "C) what",
      "D) if"
    ],
    "answer": "A",
    "explanation": "Reported questions with 'wh-' words keep the question word: 'Where are you going?' → 'where I was going.'"
  },
  {
    "question": "'He told me ___ he would come.'",
    "options": [
      "A) what",
      "B) that",
      "C) if",
      "D) where"
    ],
    "answer": "B",
    "explanation": "Reported statements use 'that' (optional): He said, 'I will come' → He told me that he would come."
  },
  {
    "question": "Choose the correct sentence:",
    "options": [
      "A) He suggested to go out",
      "B) He suggested going out",
      "C) He suggested go out",
      "D) He suggested that going out"
    ],
    "answer": "B",
    "explanation": "'Suggest' is followed by gerund (verb + -ing) or 'that + subject + base form'."
  },
  {
    "question": "'I ___ up at 6 AM every day.' (habitual action)",
    "options": [
      "A) wake",
      "B) woke",
      "C) waken",
      "D) waking"
    ],
    "answer": "A",
    "explanation": "Present simple for habitual actions: I wake up every day."
  },
  {
    "question": "'By next year, I ___ here for ten years.'",
    "options": [
      "A) will work",
      "B) will have worked",
      "C) will be working",
      "D) work"
    ],
    "answer": "B",
    "explanation": "Future perfect: 'will have + past participle' for actions completed before a future point."
  },
  {
    "question": "'She enjoys ___ books in her free time.'",
    "options": [
      "A) read",
      "B) to read",
      "C) reading",
      "D) reads"
    ],
    "answer": "C",
    "explanation": "'Enjoy' is always followed by gerund (verb + -ing)."
  },
  {
    "question": "'He avoided ___ the question.'",
    "options": [
      "A) answer",
      "B) to answer",
      "C) answering",
      "D) answered"
    ],
    "answer": "C",
    "explanation": "'Avoid' is followed by gerund. Some verbs require -ing form."
  },
  {
    "question": "'Despite ___ hard, he failed the exam.'",
    "options": [
      "A) study",
      "B) to study",
      "C) studying",
      "D) studied"
    ],
    "answer": "C",
    "explanation": "'Despite' is followed by a noun or gerund: despite studying hard."
  },
  {
    "question": "'I'm not ___ tall ___ my brother.'",
    "options": [
      "A) so...than",
      "B) as...as",
      "C) more...than",
      "D) so...so"
    ],
    "answer": "B",
    "explanation": "'As...as' is used for comparisons of equality (or inequality with 'not')."
  },
  {
    "question": "'The more you study, the ___ you learn.'",
    "options": [
      "A) much",
      "B) more",
      "C) most",
      "D) many"
    ],
    "answer": "B",
    "explanation": "'The more...the more' is a correlative comparative structure."
  },
  {
    "question": "'He ___ to the gym three times a week.' (regular habit)",
    "options": [
      "A) is going",
      "B) goes",
      "C) go",
      "D) going"
    ],
    "answer": "B",
    "explanation": "Present simple for regular habits: He goes (third person -s)."
  },
  {
    "question": "'We arrived ___ the airport ___ time.'",
    "options": [
      "A) at / on",
      "B) in / on",
      "C) at / in",
      "D) to / at"
    ],
    "answer": "A",
    "explanation": "'Arrive at' + specific place, 'on time' = à l'heure."
  },
  {
    "question": "'I have been living here ___ January.'",
    "options": [
      "A) for",
      "B) since",
      "C) during",
      "D) from"
    ],
    "answer": "B",
    "explanation": "'Since' + specific point in time (since January). 'For' + duration."
  },
  {
    "question": "Choose the correct article: '___ university is a place of learning.'",
    "options": [
      "A) An",
      "B) A",
      "C) The",
      "D) Ø"
    ],
    "answer": "B",
    "explanation": "'A' before 'university' because the first sound is /juː/ (consonant sound), not a vowel sound."
  },
  {
    "question": "'He ___ be tired. He has been working all day.' (logical deduction)",
    "options": [
      "A) can",
      "B) may",
      "C) must",
      "D) should"
    ],
    "answer": "C",
    "explanation": "'Must' for strong logical deduction based on evidence."
  },
  {
    "question": "'They ___ have left already. The lights are off.' (deduction about past)",
    "options": [
      "A) can",
      "B) must",
      "C) should",
      "D) would"
    ],
    "answer": "B",
    "explanation": "'Must have + past participle' for deductions about the past."
  },
  {
    "question": "'I ___ dinner when the phone rang.'",
    "options": [
      "A) cooked",
      "B) was cooking",
      "C) have cooked",
      "D) cook"
    ],
    "answer": "B",
    "explanation": "Past continuous for an ongoing action interrupted by another event."
  },
  {
    "question": "'She ___ for two hours when he arrived.'",
    "options": [
      "A) waited",
      "B) was waiting",
      "C) had been waiting",
      "D) has waited"
    ],
    "answer": "C",
    "explanation": "Past perfect continuous for a duration before a past event: had been + -ing."
  },
  {
    "question": "'How ___ sugar do you need?'",
    "options": [
      "A) many",
      "B) much",
      "C) few",
      "D) several"
    ],
    "answer": "B",
    "explanation": "'Much' for uncountable nouns. 'Many' for countable nouns."
  },
  {
    "question": "'There are ___ apples in the basket.'",
    "options": [
      "A) much",
      "B) a few",
      "C) a little",
      "D) less"
    ],
    "answer": "B",
    "explanation": "'A few' for countable nouns (positive sense). 'A little' for uncountable."
  },
  {
    "question": "Which noun is uncountable?",
    "options": [
      "A) Book",
      "B) Chair",
      "C) Information",
      "D) Apple"
    ],
    "answer": "C",
    "explanation": "'Information' is uncountable: 'some information' (never 'informations' in English)."
  },
  {
    "question": "Which noun is uncountable?",
    "options": [
      "A) Advice",
      "B) Student",
      "C) Table",
      "D) Question"
    ],
    "answer": "A",
    "explanation": "'Advice' is uncountable: 'a piece of advice' (never 'an advice')."
  },
  {
    "question": "'She ___ here for three years.' (and still works here)",
    "options": [
      "A) worked",
      "B) works",
      "C) has been working",
      "D) was working"
    ],
    "answer": "C",
    "explanation": "Present perfect continuous for an action that started in the past and continues."
  },
  {
    "question": "'He ___ while I ___ .' (read / study)",
    "options": [
      "A) was reading / was studying",
      "B) read / studied",
      "C) was reading / studied",
      "D) read / was studying"
    ],
    "answer": "A",
    "explanation": "Two simultaneous ongoing past actions: both in past continuous."
  },
  {
    "question": "'Although it was raining, ___'",
    "options": [
      "A) but they went out",
      "B) they went out",
      "C) so they stayed",
      "D) however they left"
    ],
    "answer": "B",
    "explanation": "'Although' introduces a concession — no need for 'but'. Avoid double conjunction."
  },
  {
    "question": "'___ the rain, they went out.'",
    "options": [
      "A) Although",
      "B) Despite",
      "C) However",
      "D) Because of"
    ],
    "answer": "B",
    "explanation": "'Despite' + noun/gerund for concession. 'Although' needs a clause."
  },
  {
    "question": "'He is good ___ mathematics.'",
    "options": [
      "A) in",
      "B) at",
      "C) on",
      "D) for"
    ],
    "answer": "B",
    "explanation": "'Good at' is the correct preposition for skills/subjects."
  },
  {
    "question": "'She is interested ___ history.'",
    "options": [
      "A) about",
      "B) at",
      "C) in",
      "D) for"
    ],
    "answer": "C",
    "explanation": "'Interested in' is the correct preposition."
  },
  {
    "question": "'He depends ___ his parents financially.'",
    "options": [
      "A) of",
      "B) on",
      "C) from",
      "D) in"
    ],
    "answer": "B",
    "explanation": "'Depend on' is the correct preposition (not 'depend of')."
  },
  {
    "question": "'Could you look ___ my cat while I'm away?' (take care of)",
    "options": [
      "A) at",
      "B) for",
      "C) after",
      "D) up"
    ],
    "answer": "C",
    "explanation": "'Look after' means to take care of someone/something."
  },
  {
    "question": "'I need to look ___ a word in the dictionary.' (search for)",
    "options": [
      "A) at",
      "B) for",
      "C) up",
      "D) after"
    ],
    "answer": "C",
    "explanation": "'Look up' means to search for information in a reference."
  },
  {
    "question": "'He ___ up smoking last year.' (stop)",
    "options": [
      "A) gave",
      "B) put",
      "C) took",
      "D) got"
    ],
    "answer": "A",
    "explanation": "'Give up' means to stop/quit a habit."
  },
  {
    "question": "'___ you study hard, you won't pass the exam.'",
    "options": [
      "A) If",
      "B) Unless",
      "C) Although",
      "D) Despite"
    ],
    "answer": "B",
    "explanation": "'Unless' = 'if not'. Unless you study hard = if you don't study hard."
  },
  {
    "question": "'He ran fast ___ he could catch the bus.'",
    "options": [
      "A) so that",
      "B) because",
      "C) although",
      "D) unless"
    ],
    "answer": "A",
    "explanation": "'So that' expresses purpose (pour que/afin que)."
  },
  {
    "question": "'___ I finish this report, I will call you.'",
    "options": [
      "A) While",
      "B) During",
      "C) As soon as",
      "D) Until"
    ],
    "answer": "C",
    "explanation": "'As soon as' = dès que. Followed by present tense for future meaning."
  },
  {
    "question": "'This is the city ___ I was born.'",
    "options": [
      "A) which",
      "B) who",
      "C) where",
      "D) that"
    ],
    "answer": "C",
    "explanation": "'Where' for places in relative clauses."
  },
  {
    "question": "'I don't know ___ he is coming or not.'",
    "options": [
      "A) if",
      "B) whether",
      "C) that",
      "D) Both A and B"
    ],
    "answer": "D",
    "explanation": "Both 'if' and 'whether' can introduce indirect yes/no questions. 'Whether' is more formal."
  },
  {
    "question": "'He speaks English ___ fluently ___ French.' (comparison of equality)",
    "options": [
      "A) so / than",
      "B) as / as",
      "C) more / than",
      "D) less / as"
    ],
    "answer": "B",
    "explanation": "'As...as' for comparisons of equality: He speaks English as fluently as French."
  },
  {
    "question": "'___ having a headache, she went to work.'",
    "options": [
      "A) Although",
      "B) In spite of",
      "C) Because",
      "D) Due to"
    ],
    "answer": "B",
    "explanation": "'In spite of' + gerund/noun for concession (synonym of 'despite')."
  },
  {
    "question": "'He ___ to London twice this year.' (experience up to now)",
    "options": [
      "A) went",
      "B) has been",
      "C) was going",
      "D) goes"
    ],
    "answer": "B",
    "explanation": "Present perfect for experiences within an unfinished time period ('this year')."
  },
  {
    "question": "'The exam was ___ than I expected.'",
    "options": [
      "A) more easier",
      "B) easier",
      "C) most easy",
      "D) easy"
    ],
    "answer": "B",
    "explanation": "Short adjectives: comparative = adjective + '-er'. Never 'more + -er'."
  }
];
