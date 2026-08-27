const QUIZ_QUESTIONS = [
  {
    "question": "Quel est le synonyme du mot « fugace » ?",
    "options": ["A) Permanent", "B) Éphémère", "C) Rapide", "D) Durable"],
    "answer": "B",
    "explanation": "« Fugace » signifie éphémère, qui dure peu de temps.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot est l'antonyme de « prospère » ?",
    "options": ["A) Florissant", "B) Misérable", "C) Riche", "D) Opulent"],
    "answer": "B",
    "explanation": "« Misérable » est le contraire de « prospère » (qui réussit bien).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : « Il est arrivé …… faute ! »",
    "options": ["A) sans", "B) sang", "C) cent", "D) sens"],
    "answer": "A",
    "explanation": "« Sans » (sans faute) est la préposition correcte dans ce contexte.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le genre du mot « armistice » ?",
    "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
    "answer": "B",
    "explanation": "« Armistice » est un nom masculin : un armistice.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle expression est correcte ?",
    "options": ["A) Je vous saurai gré", "B) Je vous saurais gré", "C) Je vous serais gré"],
    "answer": "A",
    "explanation": "L'expression correcte est « Je vous saurai gré » (futur simple).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot n'appartient pas à la même famille ?",
    "options": ["A) Terroir", "B) Territoire", "C) Terreur", "D) Terrain"],
    "answer": "C",
    "explanation": "« Terreur » vient du latin « terror » tandis que les autres viennent de « terra » (terre).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Trouvez le mot mal orthographié :",
    "options": ["A) Aréopage", "B) Anathème", "C) Apotheose", "D) Acrobate"],
    "answer": "C",
    "explanation": "L'orthographe correcte est « apothéose » avec un accent aigu.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot est l'antonyme de « prolixe » ?",
    "options": ["A) Concis", "B) Verbeux", "C) Bavard", "D) Éloquent"],
    "answer": "A",
    "explanation": "« Prolixe » signifie bavard, son antonyme est « concis » (bref).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel pluriel est correct ?",
    "options": ["A) des cache-nez", "B) des cache-nezs", "C) des caches-nez"],
    "answer": "A",
    "explanation": "Les noms composés avec « cache » restent invariables : des cache-nez.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle phrase ne contient pas de pléonasme ?",
    "options": ["A) Monter en haut", "B) Prévoir à l'avance", "C) Répéter encore", "D) Examiner attentivement"],
    "answer": "D",
    "explanation": "« Examiner attentivement » n'est pas redondant, contrairement aux autres.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Trouvez l'orthographe correcte :",
    "options": ["A) Dilemme", "B) Dilème", "C) Dilemne", "D) Dilenne"],
    "answer": "A",
    "explanation": "Le mot s'écrit « dilemme » avec deux m.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel verbe se construit avec « de » ?",
    "options": ["A) Pallier", "B) Remédier", "C) Suppléer", "D) Obvier"],
    "answer": "B",
    "explanation": "On dit « remédier à » et non « remédier de ». « Pallier » se construit sans préposition.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la nature du mot « Épuisé » dans : « Épuisé, l'athlète abandonne » ?",
    "options": ["A) Adjectif qualificatif", "B) Participe passé épithète", "C) Participe passé en apposition"],
    "answer": "C",
    "explanation": "« Épuisé » est un participe passé mis en apposition (détaché par une virgule).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la définition de « l'emphase » ?",
    "options": ["A) Un style exagéré", "B) La discrétion", "C) La clarté", "D) La concision"],
    "answer": "A",
    "explanation": "L'emphase est un ton, un style emphatique, exagéré et pompeux.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot désigne une personne qui mange de tout ?",
    "options": ["A) Herbivore", "B) Carnivore", "C) Omnivore", "D) Frugivore"],
    "answer": "C",
    "explanation": "« Omnivore » désigne un être qui se nourrit de tout (végétaux et animaux).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie le sigle « ONU » ?",
    "options": ["A) Organisation des Nations Unies", "B) Office des Nations Unies", "C) Ordre des Nations Unies", "D) Organe des Nations Unies"],
    "answer": "A",
    "explanation": "ONU signifie Organisation des Nations Unies.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est l'antonyme de « appareiller » ?",
    "options": ["A) Accoster", "B) Fusionner", "C) Apprêter", "D) Partir"],
    "answer": "A",
    "explanation": "« Appareiller » signifie partir (pour un navire), son antonyme est « accoster » (arriver).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Une personne « dégingandée » est une personne :",
    "options": ["A) Élégante", "B) Ayant une démarche disloquée", "C) Timide", "D) Intelligente"],
    "answer": "B",
    "explanation": "« Dégingandée » qualifie une personne ayant des mouvements maladroits et une démarche disloquée.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel dessert tire son nom d'une femme célèbre ?",
    "options": ["A) Tiramisu", "B) Pavlova", "C) Macaron", "D) Éclair"],
    "answer": "B",
    "explanation": "La Pavlova est nommée d'après la ballerine russe Anna Pavlova.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le genre du mot « haltère » ?",
    "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
    "answer": "B",
    "explanation": "« Haltère » est masculin : un haltère.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot n'appartient pas à la même famille que les autres ?",
    "options": ["A) Fable", "B) Fabuleux", "C) Affable", "D) Fabulation"],
    "answer": "C",
    "explanation": "« Affable » vient du latin « affabilis » (courtois), tandis que les autres viennent de « fabula » (récit).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle relation n'existe pas (nature-adjectif) ?",
    "options": ["A) Eau-aquatique", "B) Église-ecclésiastique", "C) Humilité-modestie"],
    "answer": "C",
    "explanation": "« Humilité » et « modestie » sont deux noms, pas une relation nature-adjectif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est l'antonyme du mot « truculent » ?",
    "options": ["A) Succulent", "B) Original", "C) Commun", "D) Savoureux"],
    "answer": "C",
    "explanation": "« Truculent » signifie haut en couleur, pittoresque ; son antonyme est « commun » (banal).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Trouvez l'intrus :",
    "options": ["A) Le Souverain Pontife", "B) Le Saint-Père", "C) La Bible", "D) Le Pape"],
    "answer": "C",
    "explanation": "Les trois autres désignent le Pape, la Bible est un livre sacré.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est l'antonyme du mot « pingre » ?",
    "options": ["A) Robuste", "B) Radin", "C) Généreux", "D) Avare"],
    "answer": "C",
    "explanation": "« Pingre » signifie avare, son antonyme est « généreux ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Dans quelle phrase n'y a-t-il pas de pléonasme ?",
    "options": ["A) Le jeune lavandier travaille dans la laverie", "B) Pour la police, c'est un petit détail", "C) Ils vont tous se rencontrer ensemble"],
    "answer": "B",
    "explanation": "Cette phrase n'a pas de redondance, contrairement aux autres.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel complément convient au verbe « luter » ?",
    "options": ["A) Une fissure", "B) Un vase", "C) Un trou", "D) Une fenêtre"],
    "answer": "B",
    "explanation": "« Luter » signifie boucher hermétiquement avec du lut (mastic). On lute un vase.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la définition de la « rhétorique » ?",
    "options": ["A) L'analyse de textes", "B) L'étude de la religion", "C) L'art du discours", "D) La grammaire"],
    "answer": "C",
    "explanation": "La rhétorique est l'art du discours et de l'éloquence.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot désigne un amour excessif de soi-même ?",
    "options": ["A) Égoïsme", "B) Narcissisme", "C) Orgueil", "D) Vanité"],
    "answer": "B",
    "explanation": "Le narcissisme désigne un amour excessif de sa propre personne.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le féminin de « empereur » ?",
    "options": ["A) Empereure", "B) Impératrice", "C) Empératrice", "D) Emperesse"],
    "answer": "B",
    "explanation": "Le féminin d'empereur est impératrice.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie « ubiquité » ?",
    "options": ["A) Rapidité", "B) Capacité d'être partout", "C) Solitude", "D) Clarté"],
    "answer": "B",
    "explanation": "L'ubiquité est la capacité d'être présent partout à la fois.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot désigne la peur des espaces clos ?",
    "options": ["A) Agoraphobie", "B) Claustrophobie", "C) Acrophobie", "D) Hydrophobie"],
    "answer": "B",
    "explanation": "La claustrophobie est la peur des espaces fermés.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : « Il a fait cela de son propre …… »",
    "options": ["A) chef", "B) chèque", "C) chaire", "D) cher"],
    "answer": "A",
    "explanation": "L'expression est « de son propre chef » (de sa propre initiative).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot désigne l'art de bien manger ?",
    "options": ["A) Gastrologie", "B) Gastronomie", "C) Gastrosophie", "D) Gastromancie"],
    "answer": "B",
    "explanation": "La gastronomie est l'art de bien manger et de bien cuisiner.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est l'origine du mot « bibliothèque » ?",
    "options": ["A) Latin", "B) Grec", "C) Arabe", "D) Sanskrit"],
    "answer": "B",
    "explanation": "« Bibliothèque » vient du grec « biblion » (livre) et « thêkê » (lieu de rangement).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel adjectif qualifie quelqu'un qui parle plusieurs langues ?",
    "options": ["A) Multilingue", "B) Polyglotte", "C) Bilingue", "D) Tous sont corrects"],
    "answer": "B",
    "explanation": "« Polyglotte » qualifie spécifiquement quelqu'un qui parle plusieurs langues.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie le sigle « HLM » ?",
    "options": ["A) Habitation de longueur moyenne", "B) Habitation à loyer modéré", "C) Habitation de location moderne", "D) Hôtel de luxe moderne"],
    "answer": "B",
    "explanation": "HLM signifie Habitation à Loyer Modéré.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le genre du mot « alvéole » ?",
    "options": ["A) Féminin", "B) Masculin", "C) Les deux sont acceptés"],
    "answer": "C",
    "explanation": "« Alvéole » est traditionnellement féminin mais le masculin est aussi admis par l'Académie française.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle figure de style consiste à dire le contraire de ce que l'on pense ?",
    "options": ["A) Litote", "B) Antiphrase", "C) Euphémisme", "D) Oxymore"],
    "answer": "B",
    "explanation": "L'antiphrase consiste à dire le contraire de ce que l'on veut faire comprendre, souvent avec ironie.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle figure de style associe deux termes contradictoires ?",
    "options": ["A) Métaphore", "B) Oxymore", "C) Antithèse", "D) Chiasme"],
    "answer": "B",
    "explanation": "L'oxymore unit deux termes de sens opposé. Ex : « un silence assourdissant ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Comment appelle-t-on un mot qui a une forme identique au masculin et au féminin ?",
    "options": ["A) Homonyme", "B) Épicène", "C) Polymorphe", "D) Androgyne"],
    "answer": "B",
    "explanation": "Un mot épicène a la même forme pour les deux genres. Ex : « un/une artiste ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est l'adjectif verbal du verbe « naviguer » ?",
    "options": ["A) Naviguant", "B) Navigant", "C) Naviguent"],
    "answer": "B",
    "explanation": "L'adjectif verbal est « navigant » (variable) ; le participe présent est « naviguant » (invariable).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est l'orthographe correcte ?",
    "options": ["A) Echappatoire", "B) Échapattoire", "C) Échappatoire", "D) Échapatoire"],
    "answer": "C",
    "explanation": "Le mot s'écrit « échappatoire » avec deux p.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mode utilise-t-on après la conjonction « Bien que » ?",
    "options": ["A) L'indicatif", "B) Le subjonctif", "C) Le conditionnel", "D) L'impératif"],
    "answer": "B",
    "explanation": "« Bien que » est toujours suivi du subjonctif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Laquelle de ces phrases est correcte ?",
    "options": ["A) Après qu'il soit venu", "B) Après qu'il est venu", "C) Après qu'il ait venu"],
    "answer": "B",
    "explanation": "« Après que » est suivi de l'indicatif (contrairement à « avant que » qui prend le subjonctif).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Comment s'accorde l'adjectif de couleur « orange » ?",
    "options": ["A) Il s'accorde normalement", "B) Il reste invariable", "C) Il ne s'accorde qu'au pluriel"],
    "answer": "B",
    "explanation": "Les adjectifs de couleur issus de noms (orange, marron, crème…) sont invariables.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie le sigle « PIB » ?",
    "options": ["A) Produit Intérieur Budgétaire", "B) Produit Intérieur Brut", "C) Plan d'Investissement Bancaire", "D) Programme d'Intervention Budgétaire"],
    "answer": "B",
    "explanation": "PIB signifie Produit Intérieur Brut, indicateur de la richesse d'un pays.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la bonne orthographe ?",
    "options": ["A) Aceuillir", "B) Accueillir", "C) Acceuillir", "D) Accueuillir"],
    "answer": "B",
    "explanation": "Le mot s'écrit « accueillir » (c-c-u-e-i-l-l-i-r).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle figure de style consiste à remplacer un terme par une expression plus douce ?",
    "options": ["A) Hyperbole", "B) Litote", "C) Euphémisme", "D) Antiphrase"],
    "answer": "C",
    "explanation": "L'euphémisme adoucit une réalité. Ex : « il nous a quittés » pour « il est mort ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle figure de style consiste à désigner un tout par une de ses parties ?",
    "options": ["A) Métonymie", "B) Synecdoque", "C) Périphrase", "D) Allégorie"],
    "answer": "B",
    "explanation": "La synecdoque prend la partie pour le tout. Ex : « les voiles » pour désigner les bateaux.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la définition d'une « périphrase » ?",
    "options": ["A) Dire le contraire de ce qu'on pense", "B) Utiliser plusieurs mots pour un seul", "C) Exagérer volontairement", "D) Comparer deux éléments"],
    "answer": "B",
    "explanation": "La périphrase remplace un mot par une expression. Ex : « l'astre du jour » pour « le soleil ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le genre du mot « tentacule » ?",
    "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
    "answer": "B",
    "explanation": "« Tentacule » est masculin : un tentacule.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le genre du mot « obélisque » ?",
    "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
    "answer": "B",
    "explanation": "« Obélisque » est masculin : un obélisque.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie l'expression « faire long feu » ?",
    "options": ["A) Durer longtemps", "B) Échouer, ne pas aboutir", "C) Provoquer un grand incendie"],
    "answer": "B",
    "explanation": "« Faire long feu » signifie ne pas aboutir, échouer (et non durer longtemps).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot désigne la peur du nombre 13 ?",
    "options": ["A) Arachnophobie", "B) Triskaïdékaphobie", "C) Nyctophobie", "D) Agoraphobie"],
    "answer": "B",
    "explanation": "La triskaïdékaphobie est la phobie du nombre 13.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Comment s'écrit 80 en lettres ?",
    "options": ["A) Quatre-vingt", "B) Quatre-vingts", "C) Quatres-vingts", "D) Quatres-vingt"],
    "answer": "B",
    "explanation": "On écrit « quatre-vingts » avec un s quand il n'est pas suivi d'un autre nombre.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "« Il n'est pas mécontent » pour dire qu'il est ravi est une :",
    "options": ["A) Hyperbole", "B) Litote", "C) Antiphrase", "D) Métonymie"],
    "answer": "B",
    "explanation": "La litote dit moins pour suggérer plus (double négation atténuante).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "« La diplomatie est le bras armé de la politique » est une :",
    "options": ["A) Métaphore", "B) Comparaison", "C) Métonymie", "D) Synecdoque"],
    "answer": "A",
    "explanation": "C'est une métaphore car il y a identification directe sans mot de comparaison.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot désigne l'étude des noms propres ?",
    "options": ["A) Onomastique", "B) Toponymie", "C) Lexicologie", "D) Philologie"],
    "answer": "A",
    "explanation": "L'onomastique est l'étude des noms propres (personnes et lieux).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le contraire de « véhément » ?",
    "options": ["A) Violent", "B) Calme", "C) Passionné", "D) Fougueux"],
    "answer": "B",
    "explanation": "« Véhément » signifie ardent, impétueux ; son contraire est « calme ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Conjuguez : « Il faut que je …… ce travail avant demain. »",
    "options": ["A) finis", "B) finisse", "C) finirai", "D) finirais"],
    "answer": "B",
    "explanation": "Après « il faut que », on utilise le subjonctif présent : « que je finisse ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le genre du mot « pétale » ?",
    "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
    "answer": "B",
    "explanation": "« Pétale » est masculin : un pétale.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le genre du mot « apostrophe » ?",
    "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
    "answer": "A",
    "explanation": "« Apostrophe » est féminin : une apostrophe.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie l'expression « avoir maille à partir » ?",
    "options": ["A) Avoir beaucoup d'argent", "B) Avoir un différend avec quelqu'un", "C) Devoir partager", "D) Être pressé"],
    "answer": "B",
    "explanation": "« Avoir maille à partir » signifie avoir un conflit, un désaccord avec quelqu'un.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot désigne un discours prononcé en l'honneur d'un défunt ?",
    "options": ["A) Panégyrique", "B) Oraison funèbre", "C) Réquisitoire", "D) Plaidoyer"],
    "answer": "B",
    "explanation": "L'oraison funèbre est un discours d'hommage prononcé lors des funérailles.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie le sigle « BEPC » ?",
    "options": ["A) Brevet d'Études du Premier Cycle", "B) Bureau d'Études des Programmes Communs", "C) Bilan d'Évaluation Professionnelle Continu"],
    "answer": "A",
    "explanation": "BEPC signifie Brevet d'Études du Premier Cycle.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : « Ces fleurs, je les ai …… »",
    "options": ["A) cueilli", "B) cueillie", "C) cueillies", "D) cueillis"],
    "answer": "C",
    "explanation": "Le participe passé s'accorde avec le COD « les » (= fleurs, féminin pluriel) placé avant.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel verbe est correctement conjugué au passé simple ?",
    "options": ["A) Il prena", "B) Il prit", "C) Il prenna", "D) Il prendit"],
    "answer": "B",
    "explanation": "Le passé simple de « prendre » à la 3e personne est « il prit ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot désigne la science du droit ?",
    "options": ["A) Jurisprudence", "B) Juridiction", "C) Droit", "D) Jurisconsulte"],
    "answer": "A",
    "explanation": "La jurisprudence est l'ensemble des décisions de justice et la science du droit.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie « apocryphe » ?",
    "options": ["A) Authentique", "B) D'authenticité douteuse", "C) Ancien", "D) Sacré"],
    "answer": "B",
    "explanation": "Un texte apocryphe est un écrit dont l'authenticité est contestée.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le genre du mot « effluve » ?",
    "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
    "answer": "B",
    "explanation": "« Effluve » est masculin : un effluve.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie « inique » ?",
    "options": ["A) Juste", "B) Injuste", "C) Unique", "D) Inutile"],
    "answer": "B",
    "explanation": "« Inique » signifie injuste, contraire à l'équité.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel proverbe signifie qu'il faut être discret sur ses projets ?",
    "options": ["A) Pierre qui roule n'amasse pas mousse", "B) Pour vivre heureux, vivons cachés", "C) Qui sème le vent récolte la tempête"],
    "answer": "B",
    "explanation": "« Pour vivre heureux, vivons cachés » signifie qu'il faut rester discret.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie « obtempérer » ?",
    "options": ["A) Refuser", "B) Obéir", "C) Hésiter", "D) Demander"],
    "answer": "B",
    "explanation": "« Obtempérer » signifie obéir, se soumettre à un ordre.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le genre du mot « encaustique » ?",
    "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
    "answer": "A",
    "explanation": "« Encaustique » est féminin : une encaustique.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie « promulguer une loi » ?",
    "options": ["A) Proposer une loi", "B) Rendre une loi officielle et applicable", "C) Abroger une loi", "D) Modifier une loi"],
    "answer": "B",
    "explanation": "Promulguer une loi, c'est la rendre officiellement applicable par décret du président.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot désigne un gouvernement dirigé par un petit nombre de personnes ?",
    "options": ["A) Démocratie", "B) Oligarchie", "C) Monarchie", "D) Théocratie"],
    "answer": "B",
    "explanation": "L'oligarchie est un régime où le pouvoir est entre les mains d'un petit groupe.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le sens de « philantrope » ?",
    "options": ["A) Qui déteste l'humanité", "B) Qui aime l'humanité", "C) Qui collectionne les timbres", "D) Qui étudie les plantes"],
    "answer": "B",
    "explanation": "Un philanthrope (du grec philos = ami + anthropos = homme) aime l'humanité et agit pour son bien.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : « Quoiqu'il …… riche, il reste modeste. »",
    "options": ["A) est", "B) soit", "C) serait", "D) sera"],
    "answer": "B",
    "explanation": "« Quoique » (= bien que) est suivi du subjonctif : « quoiqu'il soit ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie « abroger » ?",
    "options": ["A) Annuler une loi", "B) Publier une loi", "C) Modifier une loi", "D) Appliquer une loi"],
    "answer": "A",
    "explanation": "Abroger signifie supprimer, annuler une loi ou un décret.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le contraire de « pléthorique » ?",
    "options": ["A) Abondant", "B) Insuffisant", "C) Excessif", "D) Immense"],
    "answer": "B",
    "explanation": "« Pléthorique » signifie en excès, surabondant ; son contraire est « insuffisant ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie « un arrêté » en droit administratif ?",
    "options": ["A) Une décision de justice", "B) Un acte administratif d'une autorité", "C) Un projet de loi", "D) Un discours officiel"],
    "answer": "B",
    "explanation": "Un arrêté est un acte administratif pris par un ministre, un préfet ou un maire.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la definition de la rhetorique ?",
    "options": ["A) L'etude d'une langue fondee sur l'analyse des textes", "B) L'etude de la religion", "C) L'art du discours et de l'eloquence", "D) La science des sons"],
    "answer": "C",
    "explanation": "La rhetorique est l'art du discours, de l'eloquence.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot est mal orthographie ?",
    "options": ["A) echapattoire", "B) alveole", "C) anagramme", "D) peregrination"],
    "answer": "A",
    "explanation": "La bonne orthographe est ecchappatoire avec deux p.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la nature de Fatiguees dans : Fatiguees, les femmes se reposent ?",
    "options": ["A) Participe passe epithete", "B) Adjectif qualificatif epithete", "C) Participe passe mis en apposition", "D) Adjectif attribut"],
    "answer": "C",
    "explanation": "Fatiguees est un participe passe mis en apposition, detache par une virgule.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot n'appartient pas a la meme famille que les autres ?",
    "options": ["A) ingenieur", "B) geniteur", "C) genese", "D) generation"],
    "answer": "A",
    "explanation": "Ingenieur vient du latin ingenium, tandis que les autres viennent de gignere (engendrer).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Choisissez le complement correct pour le verbe Luter :",
    "options": ["A) une fissure", "B) un vase", "C) un trou", "D) une bouteille"],
    "answer": "B",
    "explanation": "Luter signifie fermer hermetiquement avec du lut. On lute un vase, un creuset.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel terme designe un nom identique pour les deux genres ?",
    "options": ["A) Invariable", "B) Epicene", "C) Commun", "D) Neutre"],
    "answer": "B",
    "explanation": "Un nom epicene a la meme forme au masculin et au feminin (ex : enfant, artiste).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Comment ecrit-on correctement 80 en lettres ?",
    "options": ["A) Quatre-vingt", "B) Quatre-vingts", "C) Quatre vingt", "D) Quatre-vingts-s"],
    "answer": "B",
    "explanation": "Quatre-vingts s'ecrit avec un s final quand il n'est pas suivi d'un autre nombre.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle phrase est correcte apres la conjonction bien que ?",
    "options": ["A) Bien qu'il a termine son travail.", "B) Bien qu'il ait termine son travail.", "C) Bien qu'il termina son travail.", "D) Bien qu'il terminera son travail."],
    "answer": "B",
    "explanation": "Bien que impose le subjonctif : bien qu'il ait termine.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle phrase est correcte apres la conjonction apres que ?",
    "options": ["A) Apres qu'il soit venu", "B) Apres qu'il ait ete la", "C) Apres qu'il est venu", "D) Apres qu'il viendrait"],
    "answer": "C",
    "explanation": "Contrairement a avant que, apres que se construit avec l'indicatif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "L'expression Il n'est pas mecontent pour dire qu'il est ravi est une :",
    "options": ["A) Hyperbole", "B) Litote", "C) Metaphore", "D) Euphemisme"],
    "answer": "B",
    "explanation": "La litote dit moins pour exprimer davantage : il n'est pas mecontent = il est tres content.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "La diplomatie est le bras arme de la politique est une :",
    "options": ["A) Metaphore", "B) Comparaison", "C) Metonymie", "D) Synecdoque"],
    "answer": "A",
    "explanation": "C'est une metaphore : assimilation directe sans terme comparatif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Comment s'accorde l'adjectif de couleur dans elle a achete des jupes orange ?",
    "options": ["A) orange (invariable)", "B) oranges", "C) orangee", "D) orangees"],
    "answer": "A",
    "explanation": "Les adjectifs de couleur issus d'un nom (orange, marron, kaki) sont invariables.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Le mot navigant est l'adjectif verbal de naviguer. Il est :",
    "options": ["A) Variable", "B) Invariable", "C) Uniquement masculin", "D) Uniquement feminin"],
    "answer": "A",
    "explanation": "L'adjectif verbal navigant est variable : des personnels navigants.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot est mal orthographié ?",
    "options": ["A) Chrysanthème", "B) Philantropie", "C) Rhythme", "D) Ephémère"],
    "answer": "B",
    "explanation": "Le mot correct est « philanthropie » avec un « h » après le « p ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le synonyme de « acrimonieux » ?",
    "options": ["A) Doux", "B) Acide", "C) Haineux", "D) Jovial"],
    "answer": "C",
    "explanation": "« Acrimonieux » signifie aigre, hargneux, plein d'animosité.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie le mot « adage » ?",
    "options": ["A) Un instrument de musique", "B) Un proverbe", "C) Un texte de loi", "D) Une formule mathématique"],
    "answer": "B",
    "explanation": "Un adage est un proverbe ou une maxime populaire transmettant une vérité pratique.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot est l'antonyme de « loquace » ?",
    "options": ["A) Bavard", "B) Silencieux", "C) Éloquent", "D) Verbeux"],
    "answer": "B",
    "explanation": "« Loquace » signifie bavard ; son antonyme est « silencieux » ou « taciturne ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Dans quelle phrase le subjonctif est-il obligatoire ?",
    "options": ["A) Je pense qu'il viendra.", "B) Il faut qu'il vienne.", "C) Je sais qu'il est là.", "D) Je crois qu'il a raison."],
    "answer": "B",
    "explanation": "Après « il faut que », le subjonctif est obligatoire.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la forme correcte du conditionnel passé ?",
    "options": ["A) Il aurait mangé", "B) Il aura mangé", "C) Il avait mangé", "D) Il eut mangé"],
    "answer": "A",
    "explanation": "Le conditionnel passé se forme avec l'auxiliaire au conditionnel présent + participe passé.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Le mot « péremptoire » signifie :",
    "options": ["A) Hésitant", "B) Définitif et sans appel", "C) Bienveillant", "D) Ambigu"],
    "answer": "B",
    "explanation": "Un ton péremptoire est absolu, tranchant, qui n'admet pas de réplique.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le pluriel correct de « bal » ?",
    "options": ["A) bals", "B) baux", "C) bales", "D) bles"],
    "answer": "A",
    "explanation": "Le pluriel de « bal » est « bals » (exception aux mots en -al qui font -aux).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle figure de style consiste à atténuer une réalité pour en diminuer l'effet ?",
    "options": ["A) Hyperbole", "B) Euphémisme", "C) Métonymie", "D) Personnification"],
    "answer": "B",
    "explanation": "L'euphémisme adoucit une réalité dure (ex. : « il a disparu » pour « il est mort »).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la nature grammaticale de « vite » dans « il court vite » ?",
    "options": ["A) Adjectif", "B) Nom", "C) Adverbe", "D) Préposition"],
    "answer": "C",
    "explanation": "« Vite » est un adverbe qui modifie le verbe « court ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le sens du préfixe « bene- » ?",
    "options": ["A) Mauvais", "B) Deux", "C) Bien", "D) Avant"],
    "answer": "C",
    "explanation": "Le préfixe latin « bene- » signifie bien (bénéfice, bénévole).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la différence entre « davantage » et « d'avantage » ?",
    "options": ["A) Aucune différence", "B) Davantage = plus ; d'avantage = d'un avantage", "C) Davantage s'écrit sans accent", "D) D'avantage est toujours incorrect"],
    "answer": "B",
    "explanation": "« Davantage » = plus ; « d'avantage » = d'un avantage (bénéfice).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel verbe est défectif (n'existe qu'à certaines formes) ?",
    "options": ["A) Manger", "B) Partir", "C) Clore", "D) Faire"],
    "answer": "C",
    "explanation": "« Clore » est un verbe défectif : il manque de nombreuses formes conjuguées.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle phrase utilise le passé simple correctement ?",
    "options": ["A) Il mangea une pomme.", "B) Il a mangea une pomme.", "C) Il mangeait une pomme.", "D) Il mangera une pomme."],
    "answer": "A",
    "explanation": "Le passé simple d'un verbe en -er se forme en ajoutant -a (3e personne singulier).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est l'homonyme de « cent » ?",
    "options": ["A) Saint", "B) Sont", "C) Sans", "D) Sang"],
    "answer": "D",
    "explanation": "« Cent », « sans », « sang », « s'en » et « sent » sont des homophones.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie « à bon escient » ?",
    "options": ["A) Par hasard", "B) Avec mauvaise intention", "C) À propos et judicieusement", "D) Avec hésitation"],
    "answer": "C",
    "explanation": "Agir à bon escient, c'est agir de manière pertinente, avec une bonne connaissance de la situation.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le terme grammatical désignant « le » dans « le chien aboie » ?",
    "options": ["A) Adjectif démonstratif", "B) Pronom personnel", "C) Article défini", "D) Article indéfini"],
    "answer": "C",
    "explanation": "« Le » est un article défini qui détermine le nom « chien ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la forme correcte ?",
    "options": ["A) Quoiqu'il fasse beau.", "B) Quoique il fasse beau.", "C) Quoi qu'il fasse beau.", "D) Quoi que il fasse beau."],
    "answer": "A",
    "explanation": "Devant « il », « quoique » subit l'élision : « quoiqu'il ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Le mot « épistémologie » désigne :",
    "options": ["A) L'étude des épistaxis", "B) La théorie de la connaissance", "C) L'étude des épidémies", "D) La science des lettres"],
    "answer": "B",
    "explanation": "L'épistémologie est la branche philosophique qui étudie la nature et les limites de la connaissance.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Dans « cette robe est verte », le mot « verte » est :",
    "options": ["A) Un adjectif épithète", "B) Un adjectif attribut", "C) Un nom", "D) Un adverbe"],
    "answer": "B",
    "explanation": "« Verte » est attribut du sujet « robe » via le verbe d'état « est ».",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est l'antonyme de « turpitude » ?",
    "options": ["A) Probité", "B) Honte", "C) Bassesse", "D) Indignité"],
    "answer": "A",
    "explanation": "La turpitude désigne la bassesse morale ; son antonyme est la probité (honnêteté).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la règle d'accord du participe passé employé avec « avoir » ?",
    "options": ["A) Il s'accorde toujours avec le sujet", "B) Il s'accorde avec le COD placé avant", "C) Il reste invariable", "D) Il s'accorde avec le COI"],
    "answer": "B",
    "explanation": "Le participe passé avec « avoir » s'accorde avec le COD si celui-ci précède le verbe.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le sens de « hégémonie » ?",
    "options": ["A) Domination prépondérante", "B) Égalité des nations", "C) Faiblesse politique", "D) Alliance militaire"],
    "answer": "A",
    "explanation": "L'hégémonie désigne la domination, la suprématie d'un État ou groupe sur d'autres.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la figure de style dans « ses yeux sont deux étoiles » ?",
    "options": ["A) Comparaison", "B) Métaphore", "C) Allitération", "D) Antithèse"],
    "answer": "B",
    "explanation": "La métaphore exprime une ressemblance sans outil comparatif (sans « comme »).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le genre du mot « amalgame » ?",
    "options": ["A) Féminin", "B) Masculin", "C) Les deux selon le contexte", "D) Neutre"],
    "answer": "B",
    "explanation": "« Amalgame » est un nom masculin : un amalgame.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie « circonstancié » ?",
    "options": ["A) Vague et imprécis", "B) Détaillé et accompagné de précisions", "C) Rapide et bref", "D) Oral et non écrit"],
    "answer": "B",
    "explanation": "Un rapport circonstancié contient tous les détails et précisions nécessaires.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot est un paronyme de « éruption » ?",
    "options": ["A) Irruption", "B) Corruption", "C) Absorption", "D) Interruption"],
    "answer": "A",
    "explanation": "« Éruption » (volcanique) et « irruption » (entrée brusque) sont des paronymes souvent confondus.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la règle d'accord dans « les fenêtres que j'ai ouvertes » ?",
    "options": ["A) Pas d'accord car COD après le verbe", "B) Accord avec 'fenêtres' car COD placé avant", "C) Accord avec le sujet 'je'", "D) Pas d'accord avec 'avoir'"],
    "answer": "B",
    "explanation": "« Que » reprend « fenêtres » (COD) placé avant le verbe avoir → accord au féminin pluriel.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le sens de l'expression « au pied levé » ?",
    "options": ["A) Avec beaucoup de préparation", "B) Sans préparation, immédiatement", "C) En marchant", "D) Avec prudence"],
    "answer": "B",
    "explanation": "Agir au pied levé, c'est agir sans préparation préalable, dans l'urgence.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Laquelle de ces formes verbales est au plus-que-parfait ?",
    "options": ["A) Il avait mangé", "B) Il a mangé", "C) Il mangea", "D) Il mangerait"],
    "answer": "A",
    "explanation": "Le plus-que-parfait se forme avec l'imparfait de l'auxiliaire + participe passé.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le sens du suffixe « -phile » ?",
    "options": ["A) Qui craint", "B) Qui aime", "C) Qui mange", "D) Qui gouverne"],
    "answer": "B",
    "explanation": "Le suffixe « -phile » signifie qui aime (bibliophile = qui aime les livres).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la phrase correcte ?",
    "options": ["A) Malgré que j'aie faim, je ne mange pas.", "B) Bien que j'aie faim, je ne mange pas.", "C) Malgré j'ai faim, je ne mange pas.", "D) Encore que j'ai faim, je ne mange pas."],
    "answer": "B",
    "explanation": "« Bien que » est correct et se construit avec le subjonctif. « Malgré que » est critiqué par les puristes.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le mot générique pour désigner les figures rhétoriques liées au son ?",
    "options": ["A) Tropes", "B) Figures sonores", "C) Métaplasmes", "D) Syntaxèmes"],
    "answer": "C",
    "explanation": "Les métaplasmes (allitération, assonance...) sont les figures qui jouent sur les sons.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que désigne le terme « polémique » dans son sens originel ?",
    "options": ["A) Une guerre verbale, un débat houleux", "B) Une démonstration mathématique", "C) Un traité diplomatique", "D) Une cérémonie officielle"],
    "answer": "A",
    "explanation": "Du grec « polemikos » (guerre), une polémique est un débat vif et souvent agressif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Dans quelle phrase le pronom « on » peut-il remplacer « nous » ?",
    "options": ["A) On a fini le travail (= nous avons fini).", "B) On a du pain (= il y a du pain).", "C) Que dit-on de lui ?", "D) On frappe à la porte."],
    "answer": "A",
    "explanation": "En français courant, « on » peut remplacer « nous » comme sujet de la phrase.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le mode verbal utilisé pour donner un ordre direct ?",
    "options": ["A) Indicatif", "B) Subjonctif", "C) Impératif", "D) Infinitif"],
    "answer": "C",
    "explanation": "L'impératif exprime un ordre, une demande ou un conseil direct.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le sens de « nonobstant » ?",
    "options": ["A) Cependant, malgré", "B) De plus, en outre", "C) Autrement dit", "D) C'est pourquoi"],
    "answer": "A",
    "explanation": "« Nonobstant » signifie malgré, en dépit de (terme juridique fréquent).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie « exergue » ?",
    "options": ["A) Un exercice d'écriture", "B) Une courte citation placée en tête d'un ouvrage", "C) Un résumé de texte", "D) Une annexe juridique"],
    "answer": "B",
    "explanation": "Mettre en exergue = mettre en évidence ; une citation en exergue introduit un texte.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la différence entre « apporter » et « amener » ?",
    "options": ["A) Aucune différence", "B) Apporter concerne les choses ; amener concerne les personnes ou animaux", "C) Amener s'utilise pour aller vers ; apporter pour venir vers", "D) Amener est plus formel"],
    "answer": "B",
    "explanation": "On apporte un objet, on amène une personne ou un animal.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le sens littéral de « laconique » ?",
    "options": ["A) Venant de Laconie (Sparte) : bref et concis", "B) Ennuyeux et long", "C) Émouvant", "D) Obscur et ambigu"],
    "answer": "A",
    "explanation": "Les Laconiens (Spartiates) étaient réputés pour leur discours bref ; laconique = bref et concis.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la fonction grammaticale de « demain » dans « il viendra demain » ?",
    "options": ["A) Sujet", "B) COD", "C) Complément circonstanciel de temps", "D) Attribut"],
    "answer": "C",
    "explanation": "« Demain » indique quand aura lieu l'action : c'est un CC de temps.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie le verbe « circonscrire » ?",
    "options": ["A) Développer, étendre", "B) Limiter, délimiter avec précision", "C) Critiquer sévèrement", "D) Résumer"],
    "answer": "B",
    "explanation": "Circonscrire un incendie = limiter sa propagation ; circonscrire un sujet = en définir les limites.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle figure de style consiste à répéter un mot ou groupe en début de plusieurs propositions ?",
    "options": ["A) Épiphore", "B) Anaphore", "C) Chiasme", "D) Syllepse"],
    "answer": "B",
    "explanation": "L'anaphore est la répétition d'un mot ou groupe en tête de propositions successives.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que désigne « l'ellipse » en stylistique ?",
    "options": ["A) Une figure géométrique", "B) Une omission volontaire d'éléments grammaticaux sans ambiguïté", "C) Une répétition de sons", "D) Une exagération"],
    "answer": "B",
    "explanation": "L'ellipse est l'omission d'un ou plusieurs mots logiquement attendus mais sous-entendus.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le sens du mot « acuité » ?",
    "options": ["A) Manque de clarté", "B) Finesse, précision d'un sens ou d'une faculté", "C) Lenteur de réaction", "D) Générosité"],
    "answer": "B",
    "explanation": "L'acuité visuelle, l'acuité intellectuelle désignent la finesse et la précision d'une faculté.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Dans « il se souvient de son enfance », le pronom « se » est :",
    "options": ["A) Pronom COD", "B) Pronom COI", "C) Pronom réfléchi sans fonction propre", "D) Pronom sujet"],
    "answer": "C",
    "explanation": "Dans les verbes essentiellement pronominaux, le « se » fait partie du verbe sans fonction propre.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Identifiez la phrase correcte :",
    "options": ["A) Les pommes que j'ai acheté sont bonnes.", "B) Les pommes que j'ai achetées sont bonnes.", "C) Les pommes que j'ai achetés sont bonnes.", "D) Les pommes que j'ai acheter sont bonnes."],
    "answer": "B",
    "explanation": "Le participe passé conjugué avec avoir s'accorde avec le COD s'il est placé avant le verbe.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Quels que ___ vos problèmes, vous devez avancer.'",
    "options": ["A) soit", "B) sois", "C) soient", "D) soyent"],
    "answer": "C",
    "explanation": "'Soient' s'accorde avec le sujet 'vos problèmes'.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Laquelle de ces phrases contient une faute ?",
    "options": ["A) Elle s'est lavé les mains.", "B) Elle s'est lavée.", "C) Ils se sont parlés.", "D) Elles se sont souri."],
    "answer": "C",
    "explanation": "'Parler' est transitif indirect (parler à). Il n'y a pas d'accord du participe passé.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Je ne pense pas qu'il ___ venir demain.'",
    "options": ["A) peut", "B) puisse", "C) pourras", "D) pourra"],
    "answer": "B",
    "explanation": "La forme négative de 'penser que' entraîne généralement le subjonctif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le pluriel de 'un arc-en-ciel' ?",
    "options": ["A) des arcs-en-ciels", "B) des arc-en-ciel", "C) des arcs-en-ciel", "D) des arc-en-ciels"],
    "answer": "C",
    "explanation": "Seul le premier nom s'accorde, 'en ciel' est invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Elles se sont ___ compte de leur erreur.'",
    "options": ["A) rendu", "B) rendue", "C) rendus", "D) rendues"],
    "answer": "A",
    "explanation": "L'expression 'se rendre compte' est invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Parmi ces phrases, laquelle emploie correctement le verbe 'pallier' ?",
    "options": ["A) Il faut pallier à ce manque.", "B) Il faut pallier ce manque.", "C) Il faut y pallier à.", "D) Il faut pallier contre ce manque."],
    "answer": "B",
    "explanation": "'Pallier' est un verbe transitif direct, on pallie quelque chose, pas 'à' quelque chose.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Même s'il ___ raison, je ne l'écouterais pas.'",
    "options": ["A) a", "B) ait", "C) avait", "D) aurait"],
    "answer": "C",
    "explanation": "Après 'même si', on emploie l'indicatif. L'imparfait ('avait') s'accorde avec le conditionnel ('écouterais').",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la conjugaison correcte au passé simple (3e personne du singulier) du verbe 'coudre' ?",
    "options": ["A) il cousit", "B) il cousa", "C) il coudit", "D) il couda"],
    "answer": "A",
    "explanation": "Le verbe coudre fait 'il cousit' au passé simple.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Il faut que nous ___ prêts à 8h.'",
    "options": ["A) sommes", "B) soyons", "C) serions", "D) soions"],
    "answer": "B",
    "explanation": "'Il faut que' est suivi du subjonctif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Identifiez la faute d'accord :",
    "options": ["A) Des demi-heures", "B) Une heure et demi", "C) Une demi-heure", "D) Deux heures et demie"],
    "answer": "B",
    "explanation": "On écrit 'une heure et demie' (demie s'accorde en genre avec heure).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le pluriel de 'un laissez-passer' ?",
    "options": ["A) des laissez-passers", "B) des laissez-passer", "C) des laissés-passer", "D) des laisses-passers"],
    "answer": "B",
    "explanation": "'Laissez-passer' est invariable car composé d'un verbe à l'impératif et d'un infinitif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Je préfère qu'elle le ___ demain.'",
    "options": ["A) fait", "B) fera", "C) fasse", "D) fait"],
    "answer": "C",
    "explanation": "'Préférer que' appelle le subjonctif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Laquelle de ces formes verbales est correcte ?",
    "options": ["A) Je résou", "B) Je résouds", "C) Je résous", "D) Je résout"],
    "answer": "C",
    "explanation": "Au présent de l'indicatif, le verbe résoudre fait 'je résous'.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Elle a l'air ___.'",
    "options": ["A) sérieux", "B) sérieuse", "C) sérieusement", "D) sérieuxement"],
    "answer": "B",
    "explanation": "Avec un sujet animé féminin, l'adjectif s'accorde avec le sujet (Elle a l'air sérieuse = elle semble sérieuse).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Il m'a dit qu'il ___ là demain.'",
    "options": ["A) sera", "B) serait", "C) est", "D) soit"],
    "answer": "B",
    "explanation": "Concordance des temps : verbe de la principale au passé (a dit), l'action future dans la subordonnée se met au conditionnel (futur dans le passé).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le participe présent du verbe 'savoir' ?",
    "options": ["A) savant", "B) sachant", "C) saveur", "D) savantement"],
    "answer": "B",
    "explanation": "Le participe présent de 'savoir' est 'sachant'.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Des personnes ___ intentionnées.'",
    "options": ["A) mal", "B) mals", "C) male", "D) males"],
    "answer": "A",
    "explanation": "L'adverbe 'mal' est invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : '___ intelligents qu'ils soient.'",
    "options": ["A) Tout", "B) Tous", "C) Toute", "D) Toutes"],
    "answer": "A",
    "explanation": "'Tout' devant un adjectif masculin pluriel commençant par une voyelle est adverbe et invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Les enfants se sont ___ lavés.'",
    "options": ["A) tout", "B) tous", "C) toute", "D) toutes"],
    "answer": "B",
    "explanation": "Ici 'tous' est un pronom mis en apposition ou adverbe d'accord, 'tous' prend un 's' car c'est le pronom (tous les enfants).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle phrase est mal ponctuée ?",
    "options": ["A) Marie, viens ici !", "B) Je crois, qu'il va pleuvoir.", "C) Cependant, il reste silencieux.", "D) Il est fatigué, car il a beaucoup travaillé."],
    "answer": "B",
    "explanation": "On ne met pas de virgule entre le verbe et la complétive introduite par 'que'.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Conjugaison : 'Il ___ fallu que je m'en aille.'",
    "options": ["A) eu", "B) eut", "C) a eu", "D) eût"],
    "answer": "D",
    "explanation": "Subjonctif plus-que-parfait (souvent précédé du conditionnel ou imparfait, mais ici 'Il eût fallu' est le conditionnel passé 2e forme).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Elle s'est ___ coupée au doigt.'",
    "options": ["A) fait", "B) faite", "C) faites", "D) fais"],
    "answer": "A",
    "explanation": "Le participe passé 'fait' suivi d'un infinitif est toujours invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot est invariable ?",
    "options": ["A) Pourpre", "B) Rose", "C) Orange", "D) Mauve"],
    "answer": "C",
    "explanation": "Les adjectifs de couleur dérivés de noms (fruit, fleur) sont invariables, comme 'orange' et 'marron'.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'C'est l'un des meilleurs livres que j'___ lu.'",
    "options": ["A) ai", "B) aie", "C) ait", "D) a"],
    "answer": "B",
    "explanation": "Le superlatif ('le meilleur') entraîne souvent l'utilisation du subjonctif dans la subordonnée relative ('aie').",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Trouvez l'erreur dans cette phrase :",
    "options": ["A) Je vais au bureau.", "B) Je vais en vélo.", "C) Je vais à bicyclette.", "D) Je vais à cheval."],
    "answer": "B",
    "explanation": "La règle traditionnelle exige la préposition 'à' pour les moyens de transport que l'on enfourche ('à vélo', 'à moto'). 'En' est pour ceux dans lesquels on entre.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Les jours se sont ___.'",
    "options": ["A) succédé", "B) succédés", "C) succédées", "D) succéder"],
    "answer": "A",
    "explanation": "Succéder est transitif indirect (succéder à). Le participe passé ne s'accorde pas.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Elle a chanté de ___ chansons.'",
    "options": ["A) belle", "B) belles", "C) beau", "D) beaux"],
    "answer": "B",
    "explanation": "'De' remplace 'des' devant un adjectif pluriel antéposé ('de belles chansons').",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Identifiez le mot correctement écrit :",
    "options": ["A) cauchemard", "B) cauchemar", "C) cauchemmard", "D) cochemar"],
    "answer": "B",
    "explanation": "'Cauchemar' ne prend pas de 'd' à la fin.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'C'est la ville ___ j'ai grandi.'",
    "options": ["A) qui", "B) que", "C) où", "D) dont"],
    "answer": "C",
    "explanation": "Le pronom relatif 'où' indique le lieu.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le participe passé de 'moudre' ?",
    "options": ["A) moudit", "B) moulé", "C) moulu", "D) moudé"],
    "answer": "C",
    "explanation": "Le verbe moudre fait 'moulu' au participe passé.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Il faut s'attendre à ce qu'il ___ demain.'",
    "options": ["A) vient", "B) viendra", "C) vienne", "D) viendrait"],
    "answer": "C",
    "explanation": "'À ce que' est suivi du subjonctif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Accord : 'Elles se sont ___ des lettres.'",
    "options": ["A) envoyé", "B) envoyés", "C) envoyée", "D) envoyées"],
    "answer": "A",
    "explanation": "Elles ont envoyé quoi ? 'des lettres' (COD placé après le verbe). À qui ? 'se' (COI). Donc pas d'accord.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : '___ les efforts qu'il a fournis, il a échoué.'",
    "options": ["A) Malgré de", "B) En dépit", "C) Malgré", "D) Quoique"],
    "answer": "C",
    "explanation": "'Malgré' s'emploie sans préposition.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la bonne conjugaison du verbe 'bouillir' au présent ?",
    "options": ["A) je bouille", "B) je bous", "C) je bouillis", "D) je bouil"],
    "answer": "B",
    "explanation": "Au présent de l'indicatif : je bous, tu bous, il bout.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Laquelle de ces phrases contient un pléonasme ?",
    "options": ["A) Il monte en haut.", "B) Il est parti loin.", "C) Il parle fort.", "D) Il marche vite."],
    "answer": "A",
    "explanation": "'Monter en haut' est un pléonasme, car monter implique déjà une élévation.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Je doute qu'il ___ la vérité.'",
    "options": ["A) sait", "B) saura", "C) sache", "D) savais"],
    "answer": "C",
    "explanation": "Le verbe douter demande le subjonctif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Il lui a donné les livres qu'il avait ___.'",
    "options": ["A) acheté", "B) achetés", "C) achetée", "D) achetées"],
    "answer": "B",
    "explanation": "Accord du participe avec 'qu'' (mis pour 'livres', masculin pluriel).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Ces femmes se sont ___ compte de la situation.'",
    "options": ["A) rendues", "B) rendu", "C) rendus", "D) rendue"],
    "answer": "B",
    "explanation": "L'expression 'se rendre compte' est toujours invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le pluriel de 'un chef-d'œuvre' ?",
    "options": ["A) des chefs-d'œuvre", "B) des chef-d'œuvres", "C) des chefs-d'œuvres", "D) des chef-d'œuvre"],
    "answer": "A",
    "explanation": "Seul 'chef' prend le pluriel, 'd'œuvre' étant un complément du nom.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Il faut qu'ils ___ leurs devoirs.'",
    "options": ["A) font", "B) feront", "C) fasse", "D) fassent"],
    "answer": "D",
    "explanation": "Subjonctif présent, 3e personne du pluriel du verbe faire.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Je ne crois pas qu'elle ___ venir.'",
    "options": ["A) puisse", "B) peut", "C) pourra", "D) pût"],
    "answer": "A",
    "explanation": "'Croire' à la forme négative est suivi du subjonctif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Identifiez le mot invariable :",
    "options": ["A) demi", "B) demi-heure", "C) debout", "D) grand-mère"],
    "answer": "C",
    "explanation": "L'adverbe 'debout' est invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Accord : 'Elles se sont ___ les mains.'",
    "options": ["A) lavé", "B) lavées", "C) lavés", "D) lavée"],
    "answer": "A",
    "explanation": "Le COD 'les mains' est placé après le verbe pronominal, donc pas d'accord.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Elles se sont ___ les mains.",
    "options": ["A) lavé", "B) lavés", "C) lavées", "D) lavée"],
    "answer": "A",
    "explanation": "COD (les mains) postposé, donc invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Les musiciens que j'ai ___ jouer.",
    "options": ["A) entendu", "B) entendus", "C) entendue", "D) entendues"],
    "answer": "B",
    "explanation": "Le COD fait l'action de jouer, accord.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Les chansons que j'ai ___ chanter.",
    "options": ["A) entendu", "B) entendus", "C) entendue", "D) entendues"],
    "answer": "A",
    "explanation": "Le COD subit l'action, invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Ils se sont ___.",
    "options": ["A) succédés", "B) succédé", "C) succédées", "D) succédée"],
    "answer": "B",
    "explanation": "Transitif indirect (succéder à), invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Des robes ___.",
    "options": ["A) bleu clair", "B) bleues claires", "C) bleues clair", "D) bleu claires"],
    "answer": "A",
    "explanation": "Adjectifs de couleur composés invariables.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Des chaussures ___.",
    "options": ["A) marrons", "B) marrons foncé", "C) marron", "D) marronnes"],
    "answer": "C",
    "explanation": "Nom employé comme adjectif, invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "___ que soient ses excuses.",
    "options": ["A) Quel", "B) Quelles", "C) Quelque", "D) Quelques"],
    "answer": "B",
    "explanation": "Quel que s'accorde avec le sujet postposé.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Des efforts, ___ intenses qu'ils soient.",
    "options": ["A) quelque", "B) quelques", "C) quel que", "D) quels que"],
    "answer": "A",
    "explanation": "Quelque adverbe devant adjectif = invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Des ___.",
    "options": ["A) chou-fleur", "B) chous-fleurs", "C) choux-fleur", "D) choux-fleurs"],
    "answer": "D",
    "explanation": "Nom + Nom = pluriel pour les deux.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "___ ses remarques.",
    "options": ["A) Nonobstant", "B) Non obstant", "C) Non-obstant", "D) N'obstant"],
    "answer": "A",
    "explanation": "Préposition invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Les années se sont ___.",
    "options": ["A) écoulées", "B) écoulé", "C) écoulés", "D) écoulée"],
    "answer": "A",
    "explanation": "Verbe essentiellement pronominal, accord sujet.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Ils se sont ___ compte de l'erreur.",
    "options": ["A) rendus", "B) rendues", "C) rendu", "D) rendue"],
    "answer": "C",
    "explanation": "COD (compte) postposé.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "La robe qu'elle s'est ___.",
    "options": ["A) acheté", "B) achetée", "C) achetés", "D) achetées"],
    "answer": "B",
    "explanation": "COD (que = la robe) antéposé.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "La chaleur qu'il a ___.",
    "options": ["A) fait", "B) faite", "C) faits", "D) faites"],
    "answer": "A",
    "explanation": "Faire impersonnel toujours invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Les efforts qu'il a ___.",
    "options": ["A) fallu", "B) fallus", "C) fallue", "D) fallues"],
    "answer": "A",
    "explanation": "Falloir impersonnel invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Elles sont ___ surprises.",
    "options": ["A) tout", "B) toute", "C) toutes", "D) tous"],
    "answer": "C",
    "explanation": "Tout s'accorde devant adj féminin commençant par consonne.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Elle était ___ étonnée.",
    "options": ["A) tout", "B) toute", "C) toutes", "D) tous"],
    "answer": "A",
    "explanation": "Tout devant adj féminin commençant par voyelle = invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Des enfants ___ à partir.",
    "options": ["A) près", "B) prêts", "C) prêt", "D) prêtent"],
    "answer": "B",
    "explanation": "Prêt à s'accorde avec le sujet.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Il habite ___ de l'école.",
    "options": ["A) prêts", "B) près", "C) prêt", "D) prête"],
    "answer": "B",
    "explanation": "Près de = invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Il a agi ___.",
    "options": ["A) sciemment", "B) siemment", "C) csiemment", "D) sciement"],
    "answer": "A",
    "explanation": "Dérivé de scient, deux m.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Il l'a demandé ___.",
    "options": ["A) instamment", "B) instament", "C) instantamment", "D) instamant"],
    "answer": "A",
    "explanation": "Adverbe de instant (faux, de instamment) -amment.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Il faut qu'il ___.",
    "options": ["A) conclu", "B) conclue", "C) conclus", "D) conclut"],
    "answer": "B",
    "explanation": "Subjonctif de conclure.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Bien qu'il ___ malade.",
    "options": ["A) est", "B) était", "C) soit", "D) fut"],
    "answer": "C",
    "explanation": "Bien que + subjonctif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Après qu'il ___ parti.",
    "options": ["A) soit", "B) est", "C) fût", "D) serait"],
    "answer": "B",
    "explanation": "Après que + indicatif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Le document ___ je parlais.",
    "options": ["A) que", "B) dont", "C) qui", "D) auquel"],
    "answer": "B",
    "explanation": "Parler de -> dont.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Le collègue ___ je me suis adressé.",
    "options": ["A) au quel", "B) à qui", "C) de qui", "D) dont"],
    "answer": "B",
    "explanation": "S'adresser à une personne -> à qui.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Il a ___ faim.",
    "options": ["A) grand", "B) grande", "C) grands", "D) grandement"],
    "answer": "A",
    "explanation": "Expression figée, invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Une chaleur ___.",
    "options": ["A) fatigante", "B) fatiguante", "C) fatigantes", "D) fatiguantes"],
    "answer": "A",
    "explanation": "Adjectif verbal sans u.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Des arguments ___.",
    "options": ["A) convainquants", "B) convaincants", "C) convainquant", "D) convaincant"],
    "answer": "B",
    "explanation": "Adjectif verbal avec c.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Il s'est coupé les cheveux ___.",
    "options": ["A) court", "B) courts", "C) cour", "D) courre"],
    "answer": "A",
    "explanation": "Adverbe invariable dans cette locution.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "C'est la ___ fois.",
    "options": ["A) vingt-et-unième", "B) vingt et unième", "C) vingtième et un", "D) vingt-unième"],
    "answer": "A",
    "explanation": "Traits d'union pour numéraux composés.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Elles se sont ___ des fleurs.",
    "options": ["A) lancées", "B) lancés", "C) lancé", "D) lancée"],
    "answer": "C",
    "explanation": "COD (fleurs) postposé.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Les pompiers, ___ preuve de courage.",
    "options": ["A) faisant", "B) faisants", "C) faisantes", "D) fait"],
    "answer": "A",
    "explanation": "Participe présent invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quoi que tu ___.",
    "options": ["A) fait", "B) fais", "C) fasse", "D) fasses"],
    "answer": "D",
    "explanation": "Quoi que + subjonctif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Il l'a fait ___.",
    "options": ["A) exprès", "B) express", "C) expresse", "D) expressément"],
    "answer": "A",
    "explanation": "Adverbe invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Les documents ci-___.",
    "options": ["A) joint", "B) joints", "C) jointe", "D) jointes"],
    "answer": "B",
    "explanation": "Placé après le nom, s'accorde.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Ci-___, les documents.",
    "options": ["A) joint", "B) joints", "C) jointe", "D) jointes"],
    "answer": "A",
    "explanation": "En tête de phrase, invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "De ___ en mieux.",
    "options": ["A) mieu", "B) mieux", "C) meilleur", "D) meilleurs"],
    "answer": "B",
    "explanation": "Invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Il a fui ___.",
    "options": ["A) nuitamment", "B) nuitement", "C) nuitament", "D) nuitemment"],
    "answer": "A",
    "explanation": "De nuit, 2 m.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Des enfants ___-nés.",
    "options": ["A) nouveau", "B) nouveaux", "C) nouvelle", "D) nouvelles"],
    "answer": "B",
    "explanation": "Nouveau s'accorde avec nés.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Des fleurs ___-écloses.",
    "options": ["A) fraiches", "B) fraîche", "C) fraîches", "D) fraichement"],
    "answer": "C",
    "explanation": "Fraîches s'accorde en genre et nombre avec écloses.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "La femme que j'ai ___ chanter.",
    "options": ["A) entendu", "B) entendue", "C) entendus", "D) entendues"],
    "answer": "B",
    "explanation": "La femme fait l'action de chanter, s'accorde.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Ils ont acheté de ___ beaux fruits.",
    "options": ["A) très", "B) de", "C) de très", "D) bien"],
    "answer": "C",
    "explanation": "Des devient de devant un adjectif pluriel.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "C'est l'une des filles qui ___ venues.",
    "options": ["A) est", "B) sont", "C) ont", "D) a"],
    "answer": "B",
    "explanation": "L'antécédent de qui est filles, donc pluriel.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Il y a un grand nombre d'élèves qui ___.",
    "options": ["A) participe", "B) participent", "C) participés", "D) participé"],
    "answer": "B",
    "explanation": "L'accord se fait avec le complément du collectif (élèves).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Une foule de curieux ___.",
    "options": ["A) approchait", "B) approchaient", "C) Les deux", "D) Aucun"],
    "answer": "C",
    "explanation": "Accord possible avec le collectif ou le complément.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "La plupart ___ d'accord.",
    "options": ["A) est", "B) sont", "C) était", "D) sera"],
    "answer": "B",
    "explanation": "La plupart impose l'accord au pluriel.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Choisissez la forme correcte :",
    "options": ["A) Ils se sont dit la vérité.", "B) Ils se sont dits la vérité.", "C) Ils se sont dite la vérité.", "D) Ils se sont dis la vérité."],
    "answer": "A",
    "explanation": "'Se' est COI (ils ont dit la vérité à eux-mêmes). 'la vérité', COD, est placé après, donc invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Trouvez la phrase correcte :",
    "options": ["A) Quoiqu'il soit riche, il est avare.", "B) Quoi qu'il soit riche, il est avare.", "C) Quoi qu'il est riche, il est avare.", "D) Quoiqu'il est riche, il est avare."],
    "answer": "A",
    "explanation": "'Quoique' en un seul mot signifie 'bien que' et appelle le subjonctif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Laquelle de ces phrases contient une erreur d'accord ?",
    "options": ["A) Les lettres qu'ils se sont envoyées.", "B) Elles se sont rendu compte de leur erreur.", "C) Les années se sont succédées rapidement.", "D) Ils se sont plu immédiatement."],
    "answer": "C",
    "explanation": "Le verbe 'se succéder' n'a jamais de COD (succéder à), le participe passé est donc toujours invariable : se sont succédé.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Accord des adjectifs de couleur. Lequel est correct ?",
    "options": ["A) Des robes bleues claires", "B) Des robes bleu clair", "C) Des robes bleues clair", "D) Des robes bleu claires"],
    "answer": "B",
    "explanation": "Les adjectifs de couleur composés sont invariables.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Comment écrit-on le nombre 300 en toutes lettres lorsqu'il n'est suivi d'aucun autre chiffre ?",
    "options": ["A) Trois cent", "B) Trois-cent", "C) Trois cents", "D) Trois-cents"],
    "answer": "C",
    "explanation": "Vingt et cent prennent la marque du pluriel quand ils sont multipliés par un nombre et qu'ils terminent l'adjectif numéral.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Comment écrit-on 80 en toutes lettres ?",
    "options": ["A) Quatre-vingt", "B) Quatre-vingts", "C) Quatre vingts", "D) Quatre vingt"],
    "answer": "B",
    "explanation": "'Vingts' prend un 's' car il est multiplié par quatre et n'est suivi d'aucun autre nombre.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le pluriel du mot composé 'un compte-gouttes' ?",
    "options": ["A) Des comptes-gouttes", "B) Des compte-gouttes", "C) Des comptes-goutte", "D) Des compte-goutte"],
    "answer": "B",
    "explanation": "'compte' est un verbe (invariable), 'gouttes' prend le pluriel (qui est d'ailleurs déjà présent au singulier).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le pluriel de 'chef-d'œuvre' ?",
    "options": ["A) Chefs-d'œuvre", "B) Chefs-d'œuvres", "C) Chef-d'œuvres", "D) Chef-d'œuvre"],
    "answer": "A",
    "explanation": "Seul le premier nom prend la marque du pluriel dans un nom composé d'un nom et de son complément prépositionnel.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Identifiez la phrase sans erreur :",
    "options": ["A) Elles se sont arrogées des droits.", "B) Elles se sont arrogé des droits.", "C) Elles se sont arrogé de droits.", "D) Elles se sont arrogées de droits."],
    "answer": "B",
    "explanation": "Le verbe s'arroger (arroger à soi). 'des droits' est COD placé après, donc invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Laquelle de ces formes est correcte ?",
    "options": ["A) Des arc-en-ciels", "B) Des arcs-en-ciels", "C) Des arcs-en-ciel", "D) Des arc-en-ciel"],
    "answer": "B",
    "explanation": "Nom + préposition + nom : seul le premier nom varie. Les arcs qui sont dans le ciel.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Choisissez la bonne graphie :",
    "options": ["A) Il faut qu'il résoud le problème.", "B) Il faut qu'il résolve le problème.", "C) Il faut qu'il résout le problème.", "D) Il faut qu'il résolusse le problème."],
    "answer": "B",
    "explanation": "Subjonctif présent du verbe résoudre.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le participe passé de 's'enfuir' à la 3ème personne du pluriel au féminin ?",
    "options": ["A) se sont enfuies", "B) se sont enfui", "C) se sont enfuit", "D) se sont enfuis"],
    "answer": "A",
    "explanation": "Verbe essentiellement pronominal, s'accorde avec le sujet.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Sélectionnez l'orthographe correcte pour 300 000 :",
    "options": ["A) Trois cents mille", "B) Trois-cents mille", "C) Trois cent mille", "D) Trois-cent mille"],
    "answer": "C",
    "explanation": "Cent est invariable s'il est suivi d'un autre nombre (ici, mille, qui est un adjectif numéral invariable).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est l'accord correct ?",
    "options": ["A) Les pommes que j'ai vu tomber.", "B) Les pommes que j'ai vues tomber.", "C) Les pommes que j'ai vue tomber.", "D) Les pommes que j'ai vus tomber."],
    "answer": "B",
    "explanation": "Le COD 'que' (mis pour pommes) précède, et les pommes font l'action de tomber (sujet de l'infinitif), l'accord se fait.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Accord avec laisser :",
    "options": ["A) Les arbres que j'ai laissé abattre.", "B) Les arbres que j'ai laissés abattre.", "C) Les arbres que j'ai laissées abattre.", "D) Les arbres que j'ai laissé abattus."],
    "answer": "A",
    "explanation": "Depuis la réforme de 1990, 'fait' et 'laissé' suivis d'un infinitif sont invariables.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Laquelle de ces propositions est juste ?",
    "options": ["A) Ils se sont parler pendant des heures.", "B) Ils se sont parlés pendant des heures.", "C) Ils se sont parlé pendant des heures.", "D) Ils se sont parlées pendant des heures."],
    "answer": "C",
    "explanation": "Se parler à soi-même ou à l'un l'autre (COI). Donc invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Pluriel des mots composés : 'nouveau-né'.",
    "options": ["A) nouveaux-né", "B) nouveau-nés", "C) nouveaux-nés", "D) nouveau-nées"],
    "answer": "C",
    "explanation": "Les deux éléments (adjectif + participe passé/adjectif) s'accordent au pluriel.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Laquelle de ces orthographes est correcte concernant le verbe asseoir ?",
    "options": ["A) Je m'assoies", "B) Je m'assied", "C) Je m'assois", "D) Je m'assié"],
    "answer": "C",
    "explanation": "Les deux formes 'je m'assois' et 'je m'assieds' sont valables, mais 'je m'assied' sans 's' est fautif.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Identifiez l'erreur :",
    "options": ["A) Elle a l'air bête.", "B) Elle a l'air bêtes.", "C) Elle a l'air gentille.", "D) Ils ont l'air fatigués."],
    "answer": "B",
    "explanation": "L'adjectif s'accorde avec le sujet (Elle) ou avec 'air', mais ne prend pas de 's' si le sujet est singulier.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez la phrase : Il travaille d'arrache-...",
    "options": ["A) pieds", "B) pied", "C) pié", "D) piéd"],
    "answer": "A",
    "explanation": "La locution est 'd'arrache-pied' (invariable).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Trouvez la phrase correcte avec 'quelque' :",
    "options": ["A) Quelque soient vos raisons.", "B) Quelles que soient vos raisons.", "C) Quelques que soient vos raisons.", "D) Quels que soient vos raisons."],
    "answer": "B",
    "explanation": "'Quel que' s'écrit en deux mots devant le verbe être et s'accorde avec le sujet 'raisons' (féminin pluriel).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Orthographe des couleurs :",
    "options": ["A) Des yeux marrons", "B) Des yeux marron", "C) Des yeux marront", "D) Des yeux marrones"],
    "answer": "A",
    "explanation": "Marron vient d'un nom de fruit et est donc invariable en tant qu'adjectif de couleur.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Accord avec 'avoir' :",
    "options": ["A) La chanson que j'ai entendu chanter.", "B) La chanson que j'ai entendue chanter.", "C) La chanson que j'ai entendue chantée.", "D) La chanson que j'ai entendu chantée."],
    "answer": "A",
    "explanation": "Le sujet de l'infinitif n'est pas la chanson (la chanson ne chante pas), donc le participe 'entendu' reste invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Sélectionnez la phrase contenant une erreur :",
    "options": ["A) Même les plus forts tombent.", "B) Ils sont arrivés eux-même.", "C) Nous l'avons fait nous-mêmes.", "D) Mêmes ses amis l'ont abandonné."],
    "answer": "D",
    "explanation": "'Même' placé avant un nom/pronom et signifiant 'y compris' est un adverbe invariable. On écrit 'Même ses amis'.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Accord de 'tout' :",
    "options": ["A) Elle est tout étonnée.", "B) Elle est toute étonnée.", "C) Elle est toutes étonnée.", "D) Elle est touts étonnée."],
    "answer": "A",
    "explanation": "'Tout' adverbe ne s'accorde devant un adjectif féminin que si celui-ci commence par une consonne ou un h aspiré. 'étonnée' commence par une voyelle.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Cochez la bonne forme :",
    "options": ["A) Des fleurs fraîches écloses", "B) Des fleurs fraîchement écloses", "C) Des fleurs fraîches éclose", "D) Des fleurs fraîche écloses"],
    "answer": "A",
    "explanation": "'Frais' employé adverbialement s'accorde exceptionnellement avec l'adjectif qui suit.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle phrase est correcte ?",
    "options": ["A) C'est nous qui avons décidé.", "B) C'est nous qui ont décidé.", "C) C'est nous qui a décidé.", "D) C'est nous qui avez décidé."],
    "answer": "A",
    "explanation": "Le verbe s'accorde avec l'antécédent du pronom relatif 'qui', soit 'nous' (1ère personne du pluriel).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel verbe est au conditionnel passé ?",
    "options": ["A) J'aurai fini", "B) J'avais fini", "C) J'aurais fini", "D) J'eus fini"],
    "answer": "C",
    "explanation": "Le conditionnel passé se forme avec l'auxiliaire au conditionnel présent (j'aurais) et le participe passé.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Accord des participes passés :",
    "options": ["A) Les efforts qu'il a fallus", "B) Les efforts qu'il a fallu", "C) Les efforts qu'ils a fallu", "D) Les efforts qu'il as fallu"],
    "answer": "A",
    "explanation": "Le participe passé des verbes impersonnels (il a fallu, il a plu) est toujours invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Identifiez l'orthographe correcte du pluriel :",
    "options": ["A) Des gratte-ciels", "B) Des grattes-ciels", "C) Des gratte-ciel", "D) Des grattes-ciel"],
    "answer": "A",
    "explanation": "'Gratte' (verbe invariable) + 'ciel' (invariable car il n'y a qu'un ciel qu'on gratte).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Lequel de ces mots est féminin ?",
    "options": ["A) un tentacule", "B) un tubercule", "C) une scolopendre", "D) un termite"],
    "answer": "C",
    "explanation": "Scolopendre est de genre féminin, contrairement aux autres qui sont souvent confondus.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel mot peut être masculin OU féminin (double genre) selon son sens ou nombre ?",
    "options": ["A) Orgue", "B) Termite", "C) Augure", "D) Aucun des trois"],
    "answer": "A",
    "explanation": "Orgue (comme amour et délice) est masculin au singulier et généralement féminin au pluriel (de belles orgues).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Complétez : 'Ces femmes se sont...'",
    "options": ["A) souri", "B) souris", "C) souries", "D) sourire"],
    "answer": "A",
    "explanation": "Se sourire à soi ou à un autre (COI), le participe passé reste invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle phrase contient un verbe transitif direct ?",
    "options": ["A) Il parle à son frère.", "B) Elle mange une pomme.", "C) Nous allons à Paris.", "D) Ils obéissent aux règles."],
    "answer": "B",
    "explanation": "Manger quelque chose (ici une pomme, COD) -> verbe transitif direct.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Que signifie la locution 'a priori' ?",
    "options": ["A) Au premier abord, avant toute expérience.", "A posteriori, après réflexion.", "C) Une priorité absolue.", "D) Une excuse non fondée."],
    "answer": "A",
    "explanation": "'a priori' (du latin) signifie au premier abord, en se fondant sur des données antérieures à l'expérience.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Choisissez la proposition exacte :",
    "options": ["A) Il l'a convaincu.", "B) Il l'a convaincue.", "C) Il l'a convaincues.", "D) Cela dépend du contexte."],
    "answer": "D",
    "explanation": "Le participe s'accorde avec le pronom 'l'', il s'écrira 'convaincue' si 'l'' remplace une femme, et 'convaincu' si c'est un homme.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle est la bonne orthographe pour 92 ?",
    "options": ["A) Quatre-vingts-deux", "B) Quatre-vingt-deux", "C) Quatre-vingt deux", "D) Quatre-vingts deux"],
    "answer": "B",
    "explanation": "Le 's' de vingts tombe lorsqu'il est suivi d'un autre adjectif numéral (deux).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Parmi ces phrases, laquelle est correcte ?",
    "options": ["A) Les enfants dont je t'ai parlé sont ici.", "B) Les enfants dont je t'ai parlés sont ici.", "C) Les enfants dont je t'ai parlées sont ici.", "D) Les enfants que je t'ai parlé sont ici."],
    "answer": "A",
    "explanation": "Parler de quelqu'un (COI), donc pas d'accord. Le pronom relatif 'dont' remplace un COI.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Comment conjuguer au conditionnel présent (1ère pers. singulier) : 'courir' ?",
    "options": ["A) Je courrais", "B) Je courais", "C) Je courrai", "D) Je courai"],
    "answer": "A",
    "explanation": "Le conditionnel présent de courir prend deux 'r' : je courrais (radical du futur + terminaisons de l'imparfait).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Indiquez l'accord correct :",
    "options": ["A) Des fleurs rouge sang", "B) Des fleurs rouges sang", "C) Des fleurs rouge sangs", "D) Des fleurs rouges sangs"],
    "answer": "A",
    "explanation": "Les adjectifs de couleur composés (rouge sang) sont toujours invariables.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle phrase présente un pléonasme ?",
    "options": ["A) Monter en haut.", "B) Sortir dehors.", "C) Descendre en bas.", "D) Toutes les réponses."],
    "answer": "D",
    "explanation": "Monter implique d'aller en haut, sortir implique d'aller dehors, descendre d'aller en bas. Ce sont tous des pléonasmes.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Identifiez la proposition correcte pour le subjonctif imparfait :",
    "options": ["A) Que je fisse", "B) Que je fis", "C) Que je faisait", "D) Que je fasse"],
    "answer": "A",
    "explanation": "'Fisse' est la 1ère personne du singulier de l'imparfait du subjonctif du verbe faire.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quel est le pluriel de 'passe-partout' ?",
    "options": ["A) passe-partouts", "B) passes-partouts", "C) passe-partout", "D) passes-partout"],
    "answer": "A",
    "explanation": "Mot composé d'un verbe (passe) et d'un adverbe (partout). Le nom entier est donc invariable.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Quelle locution est correcte pour dire 'à condition que' (avec subjonctif) ?",
    "options": ["A condition que tu viens.", "A condition que tu viennes.", "A condition que tu viendras.", "A condition que tu vienne."],
    "answer": "A",
    "explanation": "'A condition que' exige le subjonctif (tu viennes).",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Orthographe correcte du pluriel de 'coffre-fort' ?",
    "options": ["A) coffre-forts", "B) coffres-fort", "C) coffres-forts", "D) coffre-fort"],
    "answer": "C",
    "explanation": "Nom + adjectif : les deux s'accordent au pluriel.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Laquelle de ces phrases contient une faute d'orthographe ?",
    "options": ["A) Ils se sont rendu compte de l'erreur.", "B) Elle s'est lavé les mains.", "C) Elles se sont permises de répondre.", "D) Ils se sont écrit des lettres."],
    "answer": "C",
    "explanation": "Permettre à soi (COI) de faire quelque chose. Le participe passé doit être invariable : se sont permis.",
    "theme": "Culture Générale — Langue française"
  },
  {
    "question": "Les mots « saut », « seau » et « sot » sont des :",
    "options": ["A) Paronymes", "B) Homographes", "C) Homophones", "D) Antonymes"],
    "answer": "C",
    "explanation": "Ces mots se prononcent de la même façon mais s'écrivent différemment : ce sont des homophones.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "La relation entre « rose » et « fleur » est une :",
    "options": ["A) Synonymie", "B) Hyponymie", "C) Antonymie", "D) Méronymie"],
    "answer": "B",
    "explanation": "« Rose » est un hyponyme de « fleur » (terme plus général, l'hyperonyme).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Le mot « Ressasser » est un exemple de :",
    "options": ["A) Anagramme", "B) Palindrome", "C) Homonyme", "D) Paronyme"],
    "answer": "B",
    "explanation": "« Ressasser » se lit dans les deux sens, c'est un palindrome.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Les mots « éminent » et « imminent » sont des :",
    "options": ["A) Synonymes", "B) Homographes", "C) Paronymes", "D) Antonymes"],
    "answer": "C",
    "explanation": "Ces mots se ressemblent fortement mais ont des sens différents : ce sont des paronymes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans les expressions « avoir du cœur » et « le cœur bat », « cœur » illustre :",
    "options": ["A) Homonymie", "B) Polysémie", "C) Méronymie", "D) Synonymie"],
    "answer": "B",
    "explanation": "Un même mot avec plusieurs sens liés illustre la polysémie.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Marie » et « aimer » sont des :",
    "options": ["A) Palindromes", "B) Homophones", "C) Anagrammes", "D) Synonymes"],
    "answer": "C",
    "explanation": "Les mêmes lettres réorganisées forment des anagrammes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Grand » et « petit » sont des :",
    "options": ["A) Antonymes", "B) Homonymes", "C) Hyponymes", "D) Paronymes"],
    "answer": "A",
    "explanation": "Ces mots ont des sens opposés : ce sont des antonymes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Touche » est le méronyme de « clavier ». La méronymie décrit :",
    "options": ["A) Relation de sens proche", "B) Relation d'inclusion (partie/tout)", "C) Relation de ressemblance"],
    "answer": "B",
    "explanation": "La méronymie exprime une relation partie/tout.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Date » (jour) et « datte » (fruit) sont des :",
    "options": ["A) Mots polysémiques", "B) Homonymes", "C) Paronymes", "D) Synonymes"],
    "answer": "B",
    "explanation": "Ces mots se prononcent pareil mais n'ont aucun lien de sens : homonymes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel terme désigne des mots interchangeables avec un sens très proche ?",
    "options": ["A) Antonymes", "B) Synonymes", "C) Paronymes", "D) Homonymes"],
    "answer": "B",
    "explanation": "Les synonymes ont un sens identique ou très proche.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "L'expression « J'ai mille choses à faire » est un :",
    "options": ["A) Euphémisme", "B) Litote", "C) Hyperbole", "D) Métonymie"],
    "answer": "C",
    "explanation": "L'exagération volontaire est une hyperbole.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'hyperonyme de « voiture », « camion », « bus » ?",
    "options": ["A) Véhicule", "B) Transport", "C) Route", "D) Moteur"],
    "answer": "A",
    "explanation": "« Véhicule » est le terme général qui englobe ces mots.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "La répétition d'un mot en début de vers s'appelle :",
    "options": ["A) Anaphore", "B) Allitération", "C) Assonance", "D) Métaphore"],
    "answer": "A",
    "explanation": "L'anaphore est la répétition d'un mot ou groupe de mots en début de phrase.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Les mots « poisson » et « poison » sont des :",
    "options": ["A) Homographes", "B) Paronymes", "C) Homophones", "D) Synonymes"],
    "answer": "B",
    "explanation": "Ils se ressemblent beaucoup mais ont des sens différents : paronymes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel terme désigne les mots cohyponymes de « animal » ?",
    "options": ["A) Arbre, plante", "B) Chat, chien, oiseau", "C) Maison, jardin", "D) Mammifère, reptile"],
    "answer": "B",
    "explanation": "Les cohyponymes sont des hyponymes d'un même hyperonyme (ici « animal »).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Les mots « ver », « verre » et « vert » sont des :",
    "options": ["A) Paronymes", "B) Homographes", "C) Homophones", "D) Synonymes"],
    "answer": "C",
    "explanation": "Ces mots se prononcent identiquement mais s'écrivent différemment : homophones.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "La relation entre « chien » et « animal » est une :",
    "options": ["A) Synonymie", "B) Hyponymie", "C) Antonymie", "D) Homonymie"],
    "answer": "B",
    "explanation": "« Chien » est un hyponyme (terme spécifique) de « animal » (terme général).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Le mot « Radar » est un exemple de :",
    "options": ["A) Anagramme", "B) Palindrome", "C) Homonyme", "D) Paronyme"],
    "answer": "B",
    "explanation": "« Radar » se lit identiquement dans les deux sens : c'est un palindrome.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle figure de style est une courte phrase qui se termine par une pointe satirique ?",
    "options": ["A) Métaphore", "B) Épigramme", "C) Hyperbole", "D) Allégorie"],
    "answer": "B",
    "explanation": "L'épigramme est une courte pièce satirique ou spirituelle.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Les mots « cession » et « session » sont des :",
    "options": ["A) Synonymes", "B) Homographes", "C) Paronymes", "D) Homophones"],
    "answer": "C",
    "explanation": "Ces mots se ressemblent fortement mais ont des sens différents : paronymes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans « pied de la jambe » et « pied d'une montagne », « pied » illustre :",
    "options": ["A) Homonymie", "B) Polysémie", "C) Méronymie", "D) Paronymie"],
    "answer": "B",
    "explanation": "Un même mot avec plusieurs sens liés par l'origine : polysémie.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Imaginer » et « migraine » sont des :",
    "options": ["A) Palindromes", "B) Homophones", "C) Anagrammes", "D) Paronymes"],
    "answer": "C",
    "explanation": "Les lettres des deux mots peuvent être réorganisées : anagrammes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans « Sa bouche est une rose », quelle figure de style est utilisée ?",
    "options": ["A) Comparaison", "B) Métaphore", "C) Métonymie", "D) Hyperbole"],
    "answer": "B",
    "explanation": "Une métaphore établit une comparaison implicite sans utiliser « comme ».",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Chaud » et « froid » sont des :",
    "options": ["A) Antonymes", "B) Homonymes", "C) Hyponymes", "D) Synonymes"],
    "answer": "A",
    "explanation": "Ces mots ont des sens opposés : ce sont des antonymes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Roue » est le méronyme de « voiture ». La méronymie décrit :",
    "options": ["A) Relation de sens proche", "B) Relation d'inclusion (partie/tout)", "C) Relation de ressemblance"],
    "answer": "B",
    "explanation": "Un méronyme désigne une partie d'un tout (holonyme).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Avocat » (fruit) et « avocat » (profession) sont des :",
    "options": ["A) Mots polysémiques", "B) Homonymes", "C) Paronymes", "D) Synonymes"],
    "answer": "B",
    "explanation": "Ces mots n'ont aucun lien de sens malgré leur forme identique : homonymes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel terme désigne des mots au sens identique ou très proche ?",
    "options": ["A) Antonymes", "B) Synonymes", "C) Paronymes", "D) Homophones"],
    "answer": "B",
    "explanation": "Les synonymes sont interchangeables dans un contexte donné.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "L'expression « Je meurs de faim » est un :",
    "options": ["A) Euphémisme", "B) Litote", "C) Hyperbole", "D) Oxymore"],
    "answer": "C",
    "explanation": "L'hyperbole est une exagération volontaire pour renforcer l'expression.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'hyperonyme de « chaise », « fauteuil », « tabouret » ?",
    "options": ["A) Meuble", "B) Bois", "C) Assise", "D) Salon"],
    "answer": "A",
    "explanation": "« Meuble » est le terme général qui englobe ces sièges.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Comment appelle-t-on la répétition d'un mot en début de phrase ?",
    "options": ["A) Anaphore", "B) Allitération", "C) Assonance", "D) Épiphore"],
    "answer": "A",
    "explanation": "L'anaphore est la répétition d'un mot ou groupe en début de vers ou phrase.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Les mots « pêcheur » et « pécheur » sont des :",
    "options": ["A) Homographes", "B) Homophones", "C) Synonymes", "D) Antonymes"],
    "answer": "B",
    "explanation": "Prononciation identique mais orthographe différente : homophones.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel phénomène décrit des mots très ressemblants mais de sens différents ?",
    "options": ["A) Homonymie", "B) Synonymie", "C) Paronymie", "D) Polysémie"],
    "answer": "C",
    "explanation": "Les paronymes se ressemblent phonétiquement et graphiquement.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Engage le jeu que je le gagne » est un :",
    "options": ["A) Anagramme", "B) Palindrome", "C) Épigramme", "D) Calembour"],
    "answer": "B",
    "explanation": "Cette phrase se lit dans les deux sens : palindrome.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "L'hétéronymie concerne des mots de sens liés mais de radicaux différents ?",
    "options": ["A) Vrai", "B) Faux", "C) Partiellement vrai"],
    "answer": "A",
    "explanation": "Ex : « oncle/tante », « cheval/jument » - sens liés, radicaux différents.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quels mots sont cohyponymes de « fleur » ?",
    "options": ["A) Arbre, arbuste", "B) Rose, tulipe", "C) Bouquet, jardin", "D) Pétale, tige"],
    "answer": "B",
    "explanation": "Les cohyponymes partagent le même hyperonyme (ici « fleur »).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Conte », « comte » et « compte » sont des :",
    "options": ["A) Paronymes", "B) Homophones", "C) Homographes", "D) Synonymes"],
    "answer": "B",
    "explanation": "Même prononciation, orthographes différentes : homophones.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans « Il est mort de rire », quelle figure est utilisée ?",
    "options": ["A) Hyperbole", "B) Litote", "C) Euphémisme", "D) Antiphrase"],
    "answer": "A",
    "explanation": "Exagération volontaire pour renforcer l'expression : hyperbole.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Oncle » et « tante » illustrent :",
    "options": ["A) Synonymie", "B) Antonymie", "C) Hétéronymie", "D) Paronymie"],
    "answer": "C",
    "explanation": "Sens liés (famille) mais radicaux complètement différents : hétéronymie.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "L'allitération est la répétition de :",
    "options": ["A) Voyelles", "B) Consonnes", "C) Mots", "D) Syllabes"],
    "answer": "B",
    "explanation": "L'allitération répète des consonnes. L'assonance répète des voyelles.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Père » est l'holonyme de « main ». Vrai ou faux ?",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Faux. « Corps » serait l'holonyme de « main » (tout dont fait partie la main).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Ce n'est pas mauvais » pour dire « c'est excellent » est une :",
    "options": ["A) Hyperbole", "B) Litote", "C) Métaphore", "D) Métonymie"],
    "answer": "B",
    "explanation": "La litote dit moins pour suggérer plus.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Nager » et « narguer » sont des :",
    "options": ["A) Synonymes", "B) Paronymes", "C) Homonymes", "D) Antonymes"],
    "answer": "B",
    "explanation": "Ressemblance phonétique et graphique forte : paronymes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans « Il pleut des cordes », quelle figure est utilisée ?",
    "options": ["A) Métaphore", "B) Comparaison", "C) Hyperbole", "D) Personnification"],
    "answer": "C",
    "explanation": "Exagération pour décrire une pluie forte : hyperbole.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Tête » (partie du corps) et « tête » (chef) illustrent :",
    "options": ["A) Homonymie", "B) Polysémie", "C) Paronymie", "D) Synonymie"],
    "answer": "B",
    "explanation": "Même mot, sens différents mais liés par l'origine : polysémie.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "L'assonance est la répétition de :",
    "options": ["A) Consonnes", "B) Voyelles", "C) Mots entiers", "D) Phrases"],
    "answer": "B",
    "explanation": "L'assonance est la répétition de voyelles. L'allitération répète des consonnes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Boire un verre » est un exemple de :",
    "options": ["A) Métaphore", "B) Métonymie", "C) Synecdoque", "D) Litote"],
    "answer": "B",
    "explanation": "La métonymie remplace un mot par un autre lié logiquement. Ici le contenant (verre) pour le contenu (boisson).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel terme désigne un mot créé récemment dans une langue ?",
    "options": ["A) Archaïsme", "B) Néologisme", "C) Barbarisme", "D) Solécisme"],
    "answer": "B",
    "explanation": "Un néologisme est un mot nouveau ou récemment entré dans la langue.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel terme désigne un mot tombé en désuétude, n'étant plus employé ?",
    "options": ["A) Néologisme", "B) Archaïsme", "C) Barbarisme", "D) Pléonasme"],
    "answer": "B",
    "explanation": "Un archaïsme est un mot ou une expression ancienne qui n'est plus en usage courant.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qu'est-ce qu'un barbarisme ?",
    "options": ["A) Un mot étranger", "B) Une faute de vocabulaire (mot déformé)", "C) Un mot ancien", "D) Un mot technique"],
    "answer": "B",
    "explanation": "Un barbarisme est l'emploi d'un mot inexistant ou déformé. Ex : « aéropage » au lieu d'« aréopage ».",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qu'est-ce qu'un solécisme ?",
    "options": ["A) Une faute d'orthographe", "B) Une faute de syntaxe", "C) Un mot inventé", "D) Un mot étranger"],
    "answer": "B",
    "explanation": "Un solécisme est une faute de grammaire/syntaxe. Ex : « c'est à moi que je parle » au lieu de « c'est à moi qu'on parle ».",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Le Roi Soleil » pour désigner Louis XIV est une :",
    "options": ["A) Métaphore", "B) Périphrase", "C) Antonomase", "D) Comparaison"],
    "answer": "C",
    "explanation": "L'antonomase utilise un nom propre comme nom commun ou inversement.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "L'épiphore est la répétition d'un mot ou groupe de mots :",
    "options": ["A) En début de phrase", "B) En fin de phrase", "C) Au milieu de phrase", "D) Partout dans la phrase"],
    "answer": "B",
    "explanation": "L'épiphore est le contraire de l'anaphore : elle répète un élément en fin de vers ou de phrase.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Blanc bonnet et bonnet blanc » est un exemple de :",
    "options": ["A) Chiasme", "B) Anaphore", "C) Palindrome", "D) Métonymie"],
    "answer": "A",
    "explanation": "Le chiasme est un croisement de termes selon le schéma AB-BA.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Courriel » est un néologisme français pour remplacer :",
    "options": ["A) Internet", "B) E-mail", "C) SMS", "D) Chat"],
    "answer": "B",
    "explanation": "« Courriel » est le néologisme officiel pour remplacer l'anglicisme « e-mail ».",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "La catachrèse est :",
    "options": ["A) Une métaphore devenue si courante qu'on ne la remarque plus", "B) Un pléonasme", "C) Une exagération", "D) Une ironie"],
    "answer": "A",
    "explanation": "La catachrèse est une métaphore passée dans l'usage courant. Ex : « les pieds d'une table ».",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Cheval » et « équestre » illustrent :",
    "options": ["A) Synonymie", "B) Un doublet étymologique", "C) Paronymie", "D) Homonymie"],
    "answer": "B",
    "explanation": "Le nom vient du latin populaire (caballus) et l'adjectif du latin savant (equester) : doublet étymologique.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de « loquace » ?",
    "options": ["A) Bavard", "B) Taciturne", "C) Verbeux", "D) Prolixe"],
    "answer": "B",
    "explanation": "« Loquace » signifie bavard ; « taciturne » signifie silencieux, peu enclin à parler.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel phénomène lexical lie « hôte » (celui qui reçoit) et « hôte » (celui qui est reçu) ?",
    "options": ["A) Polysémie", "B) Homonymie", "C) Énantiosémie", "D) Paronymie"],
    "answer": "C",
    "explanation": "L'énantiosémie (ou auto-antonymie) désigne un mot qui a deux sens opposés.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Clair-obscur » est un exemple de :",
    "options": ["A) Pléonasme", "B) Oxymore", "C) Antithèse", "D) Chiasme"],
    "answer": "B",
    "explanation": "L'oxymore associe deux termes contradictoires dans un même syntagme.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qu'est-ce qu'une antithèse ?",
    "options": ["A) Deux termes contradictoires accolés", "B) Opposition de deux idées dans une phrase", "C) Exagération volontaire", "D) Comparaison implicite"],
    "answer": "B",
    "explanation": "L'antithèse oppose deux idées dans une phrase ou un paragraphe, contrairement à l'oxymore qui accole les contraires.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel procédé consiste à atténuer une vérité désagréable ?",
    "options": ["A) Hyperbole", "B) Litote", "C) Euphémisme", "D) Antiphrase"],
    "answer": "C",
    "explanation": "L'euphémisme adoucit une réalité brutale. Ex : « il s'est éteint » pour « il est mort ».",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Frère » et « sœur » illustrent :",
    "options": ["A) Synonymie", "B) Antonymie", "C) Hétéronymie", "D) Paronymie"],
    "answer": "C",
    "explanation": "Sens liés (famille) mais radicaux totalement différents : c'est l'hétéronymie.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Le mot « chrysanthème » est :",
    "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
    "answer": "B",
    "explanation": "« Chrysanthème » est masculin : un chrysanthème.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qu'est-ce qu'une personnification ?",
    "options": ["A) Comparer deux éléments", "B) Attribuer des traits humains à un objet ou animal", "C) Exagérer un propos", "D) Dire le contraire de ce qu'on pense"],
    "answer": "B",
    "explanation": "La personnification donne des caractéristiques humaines à ce qui n'est pas humain. Ex : « le vent hurle ».",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qu'est-ce qu'une gradation ?",
    "options": ["A) Répétition d'un mot", "B) Énumération de termes d'intensité croissante ou décroissante", "C) Opposition de deux idées", "D) Comparaison implicite"],
    "answer": "B",
    "explanation": "La gradation est une suite de mots d'intensité progressive. Ex : « je le vis, je rougis, je pâlis » (Racine).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans « La fourmi travaille sans relâche », quelle figure est utilisée ?",
    "options": ["A) Métaphore", "B) Personnification", "C) Comparaison", "D) Allégorie"],
    "answer": "B",
    "explanation": "Attribuer le travail (action humaine consciente) à un animal est une personnification.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Il prit son chapeau et la porte » est un exemple de :",
    "options": ["A) Pléonasme", "B) Zeugme", "C) Chiasme", "D) Oxymore"],
    "answer": "B",
    "explanation": "Le zeugme associe sur le même verbe des compléments de nature très différente (sens concret et figuré).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qu'est-ce qu'un champ lexical ?",
    "options": ["A) L'ensemble des sens d'un mot", "B) L'ensemble des mots liés à un même thème", "C) Les mots de même famille", "D) Les mots de même racine"],
    "answer": "B",
    "explanation": "Le champ lexical regroupe les mots se rapportant à un même thème. Ex : école → élève, cours, tableau.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qu'est-ce qu'un champ sémantique ?",
    "options": ["A) Les mots d'un même thème", "B) L'ensemble des sens d'un seul mot", "C) Les mots de même sonorité", "D) Les synonymes d'un mot"],
    "answer": "B",
    "explanation": "Le champ sémantique est l'ensemble des significations d'un mot. Ex : « feuille » → papier, arbre, métal.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qu'est-ce qu'une prosopopée ?",
    "options": ["A) Faire parler un absent, un mort ou un objet", "B) Exagérer ses propos", "C) Répéter un mot pour insister", "D) Utiliser un mot pour un autre"],
    "answer": "A",
    "explanation": "La prosopopée fait parler un absent, un mort, un animal ou une abstraction.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Je suis venu, j'ai vu, j'ai vaincu » est un exemple de :",
    "options": ["A) Gradation", "B) Anaphore", "C) Les deux à la fois", "D) Allitération"],
    "answer": "C",
    "explanation": "C'est à la fois une anaphore (répétition de « je ») et une gradation (intensité croissante).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'hyperonyme de « pomme », « banane », « mangue » ?",
    "options": ["A) Aliment", "B) Fruit", "C) Arbre", "D) Récolte"],
    "answer": "B",
    "explanation": "« Fruit » est le terme général englobant pomme, banane et mangue.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Prêt » et « près » sont des :",
    "options": ["A) Synonymes", "B) Homophones", "C) Paronymes", "D) Antonymes"],
    "answer": "B",
    "explanation": "Même prononciation mais sens et orthographe différents : homophones.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Éruption » et « irruption » sont des :",
    "options": ["A) Synonymes", "B) Homophones", "C) Paronymes", "D) Antonymes"],
    "answer": "C",
    "explanation": "Formes proches mais sens différents : éruption (sortie violente) vs irruption (entrée brusque).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Page » (de livre) et « page » (jeune serviteur) sont des :",
    "options": ["A) Mots polysémiques", "B) Homonymes", "C) Paronymes", "D) Synonymes"],
    "answer": "B",
    "explanation": "Même forme mais origines et sens totalement différents : homonymes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qu'est-ce qu'une allégorie ?",
    "options": ["A) Une comparaison abrégée", "B) Une métaphore filée représentant une idée abstraite", "C) Un pléonasme", "D) Une exagération"],
    "answer": "B",
    "explanation": "L'allégorie représente une idée abstraite par une image concrète prolongée. Ex : la Justice avec une balance.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Doigt » est le méronyme de :",
    "options": ["A) Ongle", "B) Main", "C) Bras", "D) Pied"],
    "answer": "B",
    "explanation": "Le doigt est une partie de la main : « doigt » (méronyme) → « main » (holonyme).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qu'est-ce qu'une prétérition ?",
    "options": ["A) Parler d'une chose en disant qu'on n'en parlera pas", "B) Exagérer ses propos", "C) Dire le contraire", "D) Atténuer la réalité"],
    "answer": "A",
    "explanation": "La prétérition consiste à dire qu'on ne va pas parler de quelque chose tout en en parlant.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Été » et « hiver » sont des :",
    "options": ["A) Synonymes", "B) Antonymes", "C) Cohyponymes", "D) Homonymes"],
    "answer": "C",
    "explanation": "Ce sont des cohyponymes de l'hyperonyme « saison ».",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Kayak » est un exemple de :",
    "options": ["A) Anagramme", "B) Palindrome", "C) Néologisme", "D) Emprunt"],
    "answer": "B",
    "explanation": "« Kayak » se lit dans les deux sens : c'est un palindrome.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans « boire la tasse » (avaler de l'eau en nageant), quelle figure est utilisée ?",
    "options": ["A) Métaphore", "B) Métonymie", "C) Catachrèse", "D) Litote"],
    "answer": "C",
    "explanation": "C'est une catachrèse : une métaphore figée dans l'usage courant.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans la phrase Sa bouche est une rose, quelle figure de style est utilisee ?",
    "options": ["A) Comparaison", "B) Metaphore", "C) Metonymie", "D) Synecdoque"],
    "answer": "B",
    "explanation": "C'est une metaphore : assimilation directe sans terme comparatif.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle figure de style se termine par une pointe satirique ?",
    "options": ["A) Metaphore", "B) Epigramme", "C) Hyperbole", "D) Anaphore"],
    "answer": "B",
    "explanation": "L'epigramme est une courte composition poetique a caractere satirique.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans pied de la jambe et pied d'une montagne, le mot pied illustre :",
    "options": ["A) Homonymie", "B) Polysemie", "C) Meronymie", "D) Antonymie"],
    "answer": "B",
    "explanation": "C'est de la polysemie : meme mot, sens differents mais lies par l'origine.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "L'expression Je meurs de faim est :",
    "options": ["A) Un euphemisme", "B) Une litote", "C) Une hyperbole", "D) Une metaphore"],
    "answer": "C",
    "explanation": "C'est une hyperbole : exageration deliberee pour produire un effet d'intensite.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Les mots imaginer et migraine sont des :",
    "options": ["A) Palindromes", "B) Homophones", "C) Anagrammes", "D) Paronymes"],
    "answer": "C",
    "explanation": "On peut former migraine en reordonnant les lettres d'imaginer : ce sont des anagrammes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle paire illustre l'heteronymie ?",
    "options": ["A) chaud / froid", "B) oncle / tante", "C) voiture / automobile", "D) fleur / rose"],
    "answer": "B",
    "explanation": "L'heteronymie concerne des mots a sens lies mais de radicaux differents : oncle/tante, cheval/jument.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle est la bonne definition de la meronymie ?",
    "options": ["A) Relation de sens proche", "B) Relation partie/tout", "C) Relation de ressemblance formelle", "D) Relation d'opposition"],
    "answer": "B",
    "explanation": "La meronymie decrit la relation d'inclusion partie/tout : roue est le meronyme de voiture.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel terme designe les cohyponymes de animal ?",
    "options": ["A) Plante, arbre", "B) Chien, chat", "C) Jambe, bras", "D) Table, chaise"],
    "answer": "B",
    "explanation": "Chien et chat partagent le meme hyperonyme animal : ce sont des cohyponymes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel terme designe la relation entre main et doigt d un point de vue meronymique ?",
    "options": ["A) Doigt est l holonyme de main", "B) Main est l holonyme de doigt", "C) Main et doigt sont des cohyponymes", "D) Main est le meronyme de doigt"],
    "answer": "B",
    "explanation": "La main est le tout (holonyme) dont le doigt est une partie (meronyme).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Pi?ge : eminent et imminent sont-ils synonymes ?",
    "options": ["A) Oui ils signifient remarquable", "B) Non : eminent=remarquable imminent=qui va arriver tres bientot", "C) Oui ils expriment l urgence", "D) Non : eminent=lieu imminent=personne"],
    "answer": "B",
    "explanation": "Pi?ge de paronymie : eminent = qui se distingue ; imminent = sur le point de se produire.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel phenomene illustre verre ver vers vert ?",
    "options": ["A) Paronymie", "B) Synonymie", "C) Homophonie", "D) Polysemie"],
    "answer": "C",
    "explanation": "Meme prononciation orthographes differentes : homophones.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle figure remplace une expression brusque par une formulation douce ?",
    "options": ["A) Litote", "B) Euphemisme", "C) Hyperbole", "D) Antiphrase"],
    "answer": "B",
    "explanation": "L euphemisme attenue la brutalite. Ex : il a quitte ce monde pour dire il est mort.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans la phrase Il ne travaille pas mal quelle figure est utilisee ?",
    "options": ["A) Hyperbole", "B) Euphemisme", "C) Litote", "D) Metaphore"],
    "answer": "C",
    "explanation": "Litote : dire moins pour faire comprendre plus. Il ne travaille pas mal = il travaille bien.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel terme designe la relation rose fleur en semantique ?",
    "options": ["A) Holonymie", "B) Hyponymie", "C) Synonymie", "D) Meronymie"],
    "answer": "B",
    "explanation": "Rose est un hyponyme de fleur : terme special inclus dans le terme general.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Conjecture et conjoncture sont-ils des paronymes ?",
    "options": ["A) Non homonymes", "B) Oui : conjecture=supposition conjoncture=situation ?conomique", "C) Non antonymes", "D) Non synonymes"],
    "answer": "B",
    "explanation": "Conjecture/conjoncture : paronymes tres proches mais de sens tres differents.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle est la difference entre holonyme et hyperonyme ?",
    "options": ["A) Ce sont des synonymes", "B) Holonyme=tout dont le meronyme est une partie ; hyperonyme=terme general dont depend un hyponyme", "C) Hyperonyme=partie holonyme=ensemble", "D) Ces termes n existent pas"],
    "answer": "B",
    "explanation": "Holonyme/meronyme = relation partie-tout. Hyperonyme/hyponyme = inclusion semantique.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Polysemie et homonymie sont-elles la meme chose ?",
    "options": ["A) Oui", "B) Non : polysemie=sens differents mais lies par etymologie ; homonymie=mots de formes identiques mais d origines differentes", "C) Oui dans les deux cas les sens sont totalement differents", "D) Non polysemie concerne verbes uniquement"],
    "answer": "B",
    "explanation": "Polysemie : tete corps/liste meme origine. Homonymie : avocat fruit/juriste origines distinctes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "avocat fruit et avocat juriste illustrent quel phenomene ?",
    "options": ["A) Polysemie", "B) Homonymie car etymologies completement differentes", "C) Synonymie", "D) Paronymie"],
    "answer": "B",
    "explanation": "Avocat fruit vient du nahuatl ; avocat juriste du latin advocatus : homonymie.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle relation sémantique lie « voiture » et « roue » ?",
    "options": ["A) Synonymie", "B) Holonymie / méronymie", "C) Antonymie", "D) Hyperonymie"],
    "answer": "B",
    "explanation": "Voiture est l'holonyme (le tout) ; roue en est le méronyme (une partie).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle figure consiste à employer un mot concret pour désigner une réalité abstraite ?",
    "options": ["A) Synecdoque", "B) Métonymie", "C) Catachrèse", "D) Allégorie"],
    "answer": "D",
    "explanation": "L'allégorie représente une idée abstraite par une image concrète et symbolique.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel phénomène illustre « couler » (aller au fond) et « couler » (du robinet) ?",
    "options": ["A) Homonymie", "B) Polysémie", "C) Paronymie", "D) Hétéronymie"],
    "answer": "B",
    "explanation": "Même mot, même origine étymologique, sens différents liés : polysémie.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle est la différence entre « injure » et « injure » verbale ?",
    "options": ["A) Ce sont des homonymes", "B) Ce sont des polysèmes (injustice / propos offensant)", "C) Ce sont des paronymes", "D) Ce sont des synonymes"],
    "answer": "B",
    "explanation": "« Injure » = polysémie : une injustice (sens juridique) ou une parole blessante (sens courant).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "La phrase « Il fait un temps de chien » contient quelle figure ?",
    "options": ["A) Comparaison", "B) Métaphore figée (locution)", "C) Allégorie", "D) Synecdoque"],
    "answer": "B",
    "explanation": "C'est une métaphore lexicalisée (figée dans la langue) : « temps de chien » = très mauvais temps.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel terme désigne un mot crée par abrègement comme « ciné » pour « cinéma » ?",
    "options": ["A) Acronyme", "B) Apocope", "C) Aphérèse", "D) Troncation"],
    "answer": "D",
    "explanation": "La troncation supprime une partie du mot. « Ciné » est une apocope (troncation finale).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle relation existe entre « rapide » et « lent » ?",
    "options": ["A) Synonymie", "B) Antonymie graduable", "C) Méronymie", "D) Hyponymie"],
    "answer": "B",
    "explanation": "Rapide et lent sont des antonymes graduables : il existe des degrés entre les deux.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Le mot « bœuf » au sens de « grand effort musical collectif » illustre quel phénomène ?",
    "options": ["A) Néologisme sémantique", "B) Métaphore lexicalisée", "C) Homonymie", "D) Paronymie"],
    "answer": "A",
    "explanation": "C'est un néologisme sémantique : un sens nouveau attribué à un mot existant.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle figure attribue à un objet les caractéristiques d'un être humain ?",
    "options": ["A) Allégorie", "B) Personnification", "C) Métonymie", "D) Antithèse"],
    "answer": "B",
    "explanation": "La personnification donne des traits humains à ce qui n'en a pas (ex. : « la mer rugit »).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel terme désigne la relation entre « tibia » et « jambe » ?",
    "options": ["A) Tibia est l'hyperonyme de jambe", "B) Tibia est le méronyme de jambe", "C) Tibia et jambe sont des cohyponymes", "D) Tibia est le synonyme de jambe"],
    "answer": "B",
    "explanation": "Le tibia est une partie (méronyme) de la jambe (holonyme).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que désigne le phénomène de « dénotation » ?",
    "options": ["A) Le sens subjectif et émotionnel d'un mot", "B) Le sens objectif et littéral d'un mot", "C) Le sens figuré d'un mot", "D) L'ensemble des synonymes d'un mot"],
    "answer": "B",
    "explanation": "La dénotation est le sens premier, neutre et objectif d'un mot. La connotation est le sens subjectif.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "« Aimer » (affecter) et « aimer » (comme dans « j'aimerais ») illustrent quelle nuance ?",
    "options": ["A) Homonymie", "B) Polysémie avec registres différents", "C) Synonymie contextuelle", "D) Antonymie graduelle"],
    "answer": "B",
    "explanation": "Le même verbe « aimer » couvre plusieurs sens selon le contexte : polysémie.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle figure consiste à dire le contraire de ce qu'on pense avec une intention satirique ?",
    "options": ["A) Litote", "B) Euphémisme", "C) Antiphrase (ironie)", "D) Prétérition"],
    "answer": "C",
    "explanation": "L'antiphrase est la figure de l'ironie : on dit le contraire pour se moquer.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Le mot « clé » dans « argument clé » est employé comme :",
    "options": ["A) Nom apposé", "B) Adjectif épithète par métaphore", "C) Adverbe", "D) Complément de nom"],
    "answer": "B",
    "explanation": "« Clé » est employé métaphoriquement comme un adjectif : l'argument essentiel.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle relation existe entre « voiture de sport » et « voiture » ?",
    "options": ["A) Holonymie", "B) Hyponymie", "C) Méronymie", "D) Synonymie"],
    "answer": "B",
    "explanation": "« Voiture de sport » est un hyponyme de « voiture » : terme spécifique inclus dans le terme général.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme complémentaire (non graduable) de « vivant » ?",
    "options": ["A) Faible", "B) Mort", "C) Silencieux", "D) Immobile"],
    "answer": "B",
    "explanation": "Vivant/mort est une antonymie complémentaire : pas de degré intermédiaire.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans « il avale les kilomètres », quelle figure est utilisée ?",
    "options": ["A) Comparaison", "B) Métaphore", "C) Synecdoque", "D) Métonymie"],
    "answer": "B",
    "explanation": "C'est une métaphore : avaler des kilomètres = parcourir une grande distance facilement.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel phénomène lexical explique que « souris » désigne à la fois un animal et un dispositif informatique ?",
    "options": ["A) Homonymie", "B) Néologisme sémantique", "C) Métaphore lexicalisée", "D) Emprunt"],
    "answer": "C",
    "explanation": "Le dispositif informatique a été appelé « souris » par métaphore avec le rongeur (forme et câble = queue).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle est la particularité d'un mot épicène ?",
    "options": ["A) Il est invariable", "B) Il désigne indifféremment les deux sexes", "C) Il n'a pas de pluriel", "D) Il est toujours masculin"],
    "answer": "B",
    "explanation": "Un mot épicène a la même forme au masculin et au féminin (ex. : enfant, élève, artiste).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'hypéronyme commun de « colère », « joie », « tristesse » ?",
    "options": ["A) Sentiment", "B) Pensée", "C) Action", "D) Sensation"],
    "answer": "A",
    "explanation": "Colère, joie et tristesse sont des hyponymes de « sentiment ».",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans « brûler les étapes », quelle figure de style est employée ?",
    "options": ["A) Synecdoque", "B) Catachrèse", "C) Métaphore lexicalisée", "D) Métonymie"],
    "answer": "C",
    "explanation": "C'est une métaphore figée dans l'usage : aller trop vite, sauter des étapes.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel phénomène linguistique désigne l'apparition d'un nouveau mot dans la langue ?",
    "options": ["A) Archaïsme", "B) Néologisme", "C) Pléonasme", "D) Barbarisme"],
    "answer": "B",
    "explanation": "Un néologisme est un mot nouveau ou un sens nouveau donné à un mot existant.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "La relation entre « oiseau » et « aigle » est une relation de :",
    "options": ["A) Synonymie", "B) Méronymie", "C) Hyperonymie/hyponymie", "D) Antonymie"],
    "answer": "C",
    "explanation": "Oiseau est l'hyperonyme (terme général) ; aigle est l'hyponyme (terme spécifique).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans « la salle applaudit », quelle figure de style voit-on ?",
    "options": ["A) Métaphore", "B) Métonymie", "C) Synecdoque", "D) Antonomase"],
    "answer": "B",
    "explanation": "C'est une métonymie : la salle (le lieu) désigne les personnes qui s'y trouvent.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel outil stylistique consiste à utiliser le nom d'une personne célèbre pour désigner une catégorie ?",
    "options": ["A) Métonymie", "B) Synecdoque", "C) Antonomase", "D) Allégorie"],
    "answer": "C",
    "explanation": "L'antonomase utilise un nom propre comme nom commun (ex. : un Harpagon = un avare).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le rapport sémantique entre « maison » et « toit » ?",
    "options": ["A) Holonymie/méronymie", "B) Hyperonymie/hyponymie", "C) Synonymie", "D) Antonymie"],
    "answer": "A",
    "explanation": "Maison est l'holonyme (le tout) ; toit en est le méronyme (une partie).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle figure de style dit moins pour faire comprendre plus ?",
    "options": ["A) Hyperbole", "B) Euphémisme", "C) Litote", "D) Amplification"],
    "answer": "C",
    "explanation": "La litote atténue volontairement pour que le lecteur comprenne le contraire (ex. : Ce n'est pas mal = c'est bien).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qu'est-ce qu'un archaïsme ?",
    "options": ["A) Un mot étranger intégré dans la langue", "B) Un mot vieilli qui n'est plus en usage courant", "C) Un mot récemment créé", "D) Un mot au sens contraire de son sens original"],
    "answer": "B",
    "explanation": "Un archaïsme est un mot ou une forme démodée, sortie de l'usage courant (ex. : « icelui »).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle différence y a-t-il entre un synonyme total et un synonyme partiel ?",
    "options": ["A) Aucune différence", "B) Synonyme total = mêmes sens dans tous les contextes ; synonyme partiel = interchangeable seulement dans certains contextes", "C) Un synonyme total est toujours de même registre", "D) Les synonymes totaux n'existent pas"],
    "answer": "B",
    "explanation": "Les synonymes totaux (parfaits) sont rares. La plupart des synonymes sont partiels.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans « les murs ont des oreilles », quelle figure de style est utilisée ?",
    "options": ["A) Métaphore", "B) Personnification", "C) Métonymie", "D) Hyperbole"],
    "answer": "B",
    "explanation": "On attribue aux murs un organe humain (oreilles) : personnification.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel phénomène explique que « souris » (animal) et « souris » (sourire, 3e pers.) soient distincts ?",
    "options": ["A) Polysémie", "B) Homographie", "C) Synonymie", "D) Méronymie"],
    "answer": "B",
    "explanation": "Même graphie, prononciation identique, sens sans lien étymologique : homographie.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel terme désigne la liste de termes généraux à spécifiques (animal → mammifère → chien → labrador) ?",
    "options": ["A) Taxinomie", "B) Synonymie", "C) Champ lexical", "D) Isotopie"],
    "answer": "A",
    "explanation": "Une taxinomie est une classification hiérarchique des termes du général au spécifique.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans « il pleut des cordes », quelle figure est employée ?",
    "options": ["A) Comparaison", "B) Métaphore", "C) Hyperbole métaphorique", "D) Personnification"],
    "answer": "C",
    "explanation": "C'est une métaphore hyperbole : il pleut très fort (les cordes exagèrent l'image).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle relation lie « mari » et « femme » sur le plan lexical ?",
    "options": ["A) Hétéronymie", "B) Antonymie complémentaire", "C) Synonymie contextuelle", "D) Holonymie"],
    "answer": "A",
    "explanation": "Mari/femme sont hétéronymes : sens liés (couple) mais radicaux différents.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'effet stylistique recherché dans une accumulation ?",
    "options": ["A) Simplifier", "B) Amplifier par une suite d'éléments de même nature", "C) Opposer deux idées", "D) Atténuer une réalité"],
    "answer": "B",
    "explanation": "L'accumulation (ou énumération) crée un effet d'intensité ou d'exhaustivité.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie l'expression « avoir le cafard » ?",
    "options": ["A) Être joyeux", "B) Être mélancolique, déprimé", "C) Avoir peur des insectes", "D) Être bavard"],
    "answer": "B",
    "explanation": "« Avoir le cafard » est une métaphore figée signifiant être triste ou déprimé.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle est la caractéristique d'un oxymoron ?",
    "options": ["A) Répétition d'un même son", "B) Association de deux termes contradictoires", "C) Énumération croissante", "D) Personnification d'un objet"],
    "answer": "B",
    "explanation": "L'oxymoron unit deux mots de sens opposés (ex. : « une obscure clarté »).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel phénomène désigne un mot dont le sens a évolué positivement (mélioratif) au fil du temps ?",
    "options": ["A) Dépréciation", "B) Aménagement", "C) Amélioration sémantique", "D) Néologisme"],
    "answer": "C",
    "explanation": "Certains mots gagnent un sens plus positif avec le temps : c'est l'amélioration sémantique.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qu'est-ce que l'isotopie dans un texte ?",
    "options": ["A) Un ensemble de syllabes répétées", "B) La récurrence de traits sémantiques qui assurent la cohérence d'un texte", "C) L'utilisation de synonymes parfaits", "D) La répétition de la même figure de style"],
    "answer": "B",
    "explanation": "L'isotopie est la répétition de traits sémantiques identiques donnant sa cohérence thématique au texte.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans « le crayon d'un enfant », quel type de relation désigne « de » ?",
    "options": ["A) Relation de possession", "B) Relation méronymique", "C) Relation hyperonymique", "D) Relation d'antonymie"],
    "answer": "A",
    "explanation": "Le génitif (de) indique ici une relation d'appartenance/possession.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel mot est à la fois son propre antonyme (autoantonyme) ?",
    "options": ["A) Chaud", "B) Hôte", "C) Méchant", "D) Clair"],
    "answer": "B",
    "explanation": "« Hôte » peut désigner celui qui reçoit et celui qui est reçu : c'est un autoantonyme (ou contronyime).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle figure de style consiste à interrompre brusquement son discours ?",
    "options": ["A) Ellipse", "B) Aposiopèse", "C) Prétérition", "D) Périphrase"],
    "answer": "B",
    "explanation": "L'aposiopèse est l'interruption brusque du discours, laissant la phrase en suspens.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel procédé désigne l'emprunt d'un mot étranger tel quel dans la langue française ?",
    "options": ["A) Calque", "B) Néologisme", "C) Xénisme/emprunt direct", "D) Dérivation"],
    "answer": "C",
    "explanation": "L'emprunt direct intègre le mot étranger sans le traduire (ex. : weekend, marketing).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le contraire d'une hyperbole ?",
    "options": ["A) Litote", "B) Métaphore", "C) Antithèse", "D) Anaphore"],
    "answer": "A",
    "explanation": "La litote dit moins que la réalité (antiphrase atténuée) ; l'hyperbole dit plus : elles sont en quelque sorte opposées.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le synonyme de 'prolixe' ?",
    "options": ["A) Concis", "B) Bavard", "C) Éloquent", "D) Silencieux"],
    "answer": "B",
    "explanation": "Quelqu'un de prolixe parle ou écrit beaucoup, de façon trop longue.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de 'altruiste' ?",
    "options": ["A) Généreux", "B) Bienveillant", "C) Égoïste", "D) Héroïque"],
    "answer": "C",
    "explanation": "Altruiste signifie se consacrer aux autres, son opposé est égoïste.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Choisissez le paronyme correct : 'Il y a une bonne ___ économique en ce moment.'",
    "options": ["A) conjecture", "B) conjoncture", "C) conjuration", "D) conjugaison"],
    "answer": "B",
    "explanation": "Une conjoncture est une situation qui résulte d'une rencontre de circonstances.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie le mot 'abstrus' ?",
    "options": ["A) Difficile à comprendre", "B) Absurde", "C) Très évident", "D) Lourd"],
    "answer": "A",
    "explanation": "Abstrus se dit d'un concept ou d'un discours très obscur, difficile à comprendre.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Analogie : L'oiseau est à la plume ce que le mouton est à ___",
    "options": ["A) L'herbe", "B) L'enclos", "C) La laine", "D) Le berger"],
    "answer": "C",
    "explanation": "La plume couvre l'oiseau comme la laine couvre le mouton.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel mot est un synonyme de 'versatile' en français ?",
    "options": ["A) Polyvalent", "B) Changeant", "C) Talentueux", "D) Têtu"],
    "answer": "B",
    "explanation": "En français, 'versatile' signifie qui change souvent d'avis (faux ami avec l'anglais).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de 'éphémère' ?",
    "options": ["A) Passager", "B) Transitoire", "C) Pérenne", "D) Mortel"],
    "answer": "C",
    "explanation": "Pérenne signifie qui dure très longtemps ou toujours, à l'opposé d'éphémère.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Complétez avec le bon paronyme : 'Il a subi une ___ de son salaire.'",
    "options": ["A) gradation", "B) dégradation", "C) rétrogradation", "D) amputation"],
    "answer": "D",
    "explanation": "On parle d'une amputation de salaire pour désigner une réduction importante. (Rétrogradation concerne le grade).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'pusillanime' ?",
    "options": ["A) Courageux", "B) Qui manque d'audace, craintif", "C) Très fort", "D) Maladif"],
    "answer": "B",
    "explanation": "Un individu pusillanime est timoré, il fuit les responsabilités ou le danger.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Analogie : 'Livre' est à 'Bibliothèque' ce que 'Tableau' est à ___",
    "options": ["A) Pinceau", "B) Artiste", "C) Pinacothèque", "D) Cadre"],
    "answer": "C",
    "explanation": "Une pinacothèque est un musée ou un lieu où l'on conserve des peintures.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Trouvez le synonyme de 'loquace' :",
    "options": ["A) Silencieux", "B) Volubile", "C) Laconique", "D) Taciturne"],
    "answer": "B",
    "explanation": "Volubile et loquace qualifient une personne qui parle beaucoup.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de 'laconique' ?",
    "options": ["A) Bref", "B) Concis", "C) Prolixe", "D) Sommaire"],
    "answer": "C",
    "explanation": "Laconique signifie s'exprimer en peu de mots. Prolixe est son contraire.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Choisissez le bon paronyme : 'Le suspect est entré par ___.'",
    "options": ["A) effraction", "B) infraction", "C) réfraction", "D) diffraction"],
    "answer": "A",
    "explanation": "Une effraction est le bris d'une clôture ou serrure pour s'introduire quelque part.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie l'expression 'avoir des accointances' ?",
    "options": ["A) Avoir des dettes", "B) Avoir des relations familières avec quelqu'un", "C) Avoir de la chance", "D) Être fâché"],
    "answer": "B",
    "explanation": "Les accointances désignent des relations, souvent jugées péjorativement.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Analogie : L'eau est à la soif ce que la nourriture est à ___",
    "options": ["A) La digestion", "B) L'appétit", "C) La faim", "D) La gastronomie"],
    "answer": "C",
    "explanation": "L'eau apaise la soif comme la nourriture apaise la faim.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le sens du mot 'gargantuesque' ?",
    "options": ["A) Minuscule", "B) Démesuré, énorme", "C) Très bruyant", "D) Silencieux"],
    "answer": "B",
    "explanation": "Tiré du personnage Gargantua, signifie gigantesque, souvent lié à l'appétit.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de 'endémique' ?",
    "options": ["A) Pandémique", "B) Indigène", "C) Sporadique", "D) Permanent"],
    "answer": "C",
    "explanation": "Endémique désigne quelque chose de constant dans une région, tandis que sporadique signifie dispersé, irrégulier.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Paronymes : 'Il n'est pas permis d'___ les règles.'",
    "options": ["A) éluder", "B) élucider", "C) luder", "D) illuminer"],
    "answer": "A",
    "explanation": "Éluder signifie éviter, contourner habilement.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie le mot 'iconoclaste' ?",
    "options": ["A) Qui détruit les images saintes, qui s'attaque aux croyances établies", "B) Qui adore les icônes", "C) Qui collectionne les images", "D) Qui peint des icônes"],
    "answer": "A",
    "explanation": "Un iconoclaste détruit les icônes ou rejette la tradition.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Analogie : Chirurgien est à bistouri ce que menuisier est à ___",
    "options": ["A) Bois", "B) Forêt", "C) Rabot", "D) Meuble"],
    "answer": "C",
    "explanation": "Le rabot est l'outil du menuisier comme le bistouri est celui du chirurgien.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que veut dire 'ineffable' ?",
    "options": ["A) Qu'on ne peut pas effacer", "B) Qu'on ne peut exprimer par des mots", "C) Qui est inutile", "D) Qui ne peut pas faillir"],
    "answer": "B",
    "explanation": "Ineffable décrit ce qui est si intense ou extraordinaire qu'on ne peut le décrire (du latin ineffabilis).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Antonyme de 'opulent' :",
    "options": ["A) Riche", "B) Luxueux", "C) Indigent", "D) Fastueux"],
    "answer": "C",
    "explanation": "Indigent qualifie une personne qui manque du nécessaire (pauvre), contrairement à opulent (très riche).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Choisissez le bon mot : 'Il a fait une ___ dans son discours pour parler d'autre chose.'",
    "options": ["A) digression", "B) régression", "C) transgression", "D) agression"],
    "answer": "A",
    "explanation": "Une digression est un développement qui s'écarte du sujet principal.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'obséquieux' ?",
    "options": ["A) Autoritaire", "B) Trop poli, hypocrite et flatteur", "C) Mortuaire", "D) Oublieux"],
    "answer": "B",
    "explanation": "Qui exagère les marques de politesse ou de respect, par servilité.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Analogie : L'apiculteur est aux abeilles ce que le colombophile est aux ___",
    "options": ["A) Poissons", "B) Pigeons", "C) Moutons", "D) Chevaux"],
    "answer": "B",
    "explanation": "La colombophilie est l'élevage des pigeons voyageurs.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le sens de 'frivole' ?",
    "options": ["A) Sérieux", "B) Léger, sans consistance, futile", "C) Ennuyeux", "D) Épais"],
    "answer": "B",
    "explanation": "Une chose ou une personne frivole manque de sérieux, s'attache à ce qui est futile.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de 'veule' ?",
    "options": ["A) Faible", "B) Lâche", "C) Énergique", "D) Mou"],
    "answer": "C",
    "explanation": "Veule signifie qui n'a aucune énergie, aucune volonté. Son antonyme est énergique ou courageux.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Choisissez le bon paronyme : 'Une explosion a eu lieu, c'est un véritable ___.'",
    "options": ["A) cataclysme", "B) catéchisme", "C) catalytique", "D) cataplasme"],
    "answer": "A",
    "explanation": "Un cataclysme est un grand bouleversement destructeur.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Analogie : Pédiatre est à enfant ce que gériatre est à ___",
    "options": ["A) Femme", "B) Vieillard", "C) Animal", "D) Homme"],
    "answer": "B",
    "explanation": "Le gériatre est le médecin spécialisé pour les personnes âgées.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie le mot 'acrimonie' ?",
    "options": ["A) Joie", "B) Aigreur, mauvaise humeur", "C) Harmonie", "D) Intelligence"],
    "answer": "B",
    "explanation": "L'acrimonie est un trait de caractère d'une personne aigrie, amère.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de 'tacite' ?",
    "options": ["A) Implicite", "B) Sous-entendu", "C) Explicite", "D) Caché"],
    "answer": "C",
    "explanation": "Tacite signifie non exprimé (implicite). Son contraire est explicite.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Paronymes : 'Il a reçu une belle ___ financière.'",
    "options": ["A) allocation", "B) allocution", "C) allégation", "D) allitération"],
    "answer": "A",
    "explanation": "Une allocation est une aide financière, une allocution est un discours.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'véloce' ?",
    "options": ["A) Lent", "B) Qui va à bicyclette", "C) Rapide, agile", "D) Lourd"],
    "answer": "C",
    "explanation": "Véloce est un adjectif signifiant rapide.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Analogie : Cécité est à la vue ce que surdité est à ___",
    "options": ["A) L'odorat", "B) L'ouïe", "C) La parole", "D) Le toucher"],
    "answer": "B",
    "explanation": "La surdité est la perte de l'ouïe.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Synonyme de 'désuet' :",
    "options": ["A) Moderne", "B) Obsolete, passé de mode", "C) Inutile", "D) Sale"],
    "answer": "B",
    "explanation": "Ce qui est désuet n'est plus en usage, obsolète.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Antonyme de 'indulgent' :",
    "options": ["A) Tolérant", "B) Sévère, intransigeant", "C) Clément", "D) Bon"],
    "answer": "B",
    "explanation": "L'indulgence est la disposition à excuser. Sévère ou intransigeant est le contraire.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Paronyme : 'Il a commis une grave ___ de jugement.'",
    "options": ["A) erreur", "B) errements", "C) éruption", "D) irruption"],
    "answer": "A",
    "explanation": "Une erreur de jugement. (Les autres mots ne conviennent pas au sens).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que veut dire 'dithyrambique' ?",
    "options": ["A) Très critique, sévère", "B) Très élogieux, enthousiaste", "C) Dépressif", "D) Ennuyeux"],
    "answer": "B",
    "explanation": "Dithyrambique qualifie un éloge enthousiaste et exalté.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Analogie : L'architecte est au plan ce que le compositeur est à la ___",
    "options": ["A) Musique", "B) Chanson", "C) Partition", "D) Note"],
    "answer": "C",
    "explanation": "L'architecte écrit son œuvre sur un plan, le compositeur sur une partition.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Synonyme de 'fallacieux' :",
    "options": ["A) Trompeur, illusoire", "B) Authentique", "C) Faisable", "D) Aisé"],
    "answer": "A",
    "explanation": "Ce qui est fallacieux cherche à tromper ou induire en erreur.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Antonyme de 'exacerbé' :",
    "options": ["A) Atténué, apaisé", "B) Aggravé", "C) Exagéré", "D) Amplifié"],
    "answer": "A",
    "explanation": "Exacerber signifie rendre plus vif ou violent. Apaisé est son contraire.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Paronymes : 'Il faut ___ les informations.'",
    "options": ["A) corrompre", "B) corroborer", "C) collaborer", "D) colporter"],
    "answer": "B",
    "explanation": "Corroborer signifie appuyer, renforcer une idée ou une information.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'polymorphe' ?",
    "options": ["A) Qui n'a pas de forme", "B) Qui peut prendre plusieurs formes", "C) Qui aime les formes", "D) Qui est très grand"],
    "answer": "B",
    "explanation": "Du grec 'poly' (plusieurs) et 'morphè' (forme).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Analogie : Le bois est au menuisier ce que l'argile est au ___",
    "options": ["A) Potier", "B) Forgeron", "C) Verrier", "D) Peintre"],
    "answer": "A",
    "explanation": "Le potier modèle l'argile pour créer des objets.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Synonyme de 'flegmatique' :",
    "options": ["A) Agité", "B) Colérique", "C) Calme, imperturbable", "D) Malade"],
    "answer": "C",
    "explanation": "Une personne flegmatique garde son sang-froid en toutes circonstances.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Antonyme de 'sporadique' :",
    "options": ["A) Irrégulier", "B) Continu, régulier", "C) Épisodique", "D) Rare"],
    "answer": "B",
    "explanation": "Sporadique veut dire qui apparaît de façon irrégulière.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Paronymes : 'Cet enfant est un véritable ___.'",
    "options": ["A) prodige", "B) prodigue", "C) profil", "D) profit"],
    "answer": "A",
    "explanation": "Un prodige est une personne extraordinairement douée. Prodigue signifie dépensier.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'sycophante' ?",
    "options": ["A) Un instrument de musique", "B) Un délateur, un dénonciateur", "C) Un type d'arbre", "D) Une maladie"],
    "answer": "B",
    "explanation": "Dans la Grèce antique, délateur professionnel, et par extension un espion ou dénonciateur méprisable.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Analogie : Pompier est à l'incendie ce que le policier est à la ___",
    "options": ["A) Sirène", "B) Voiture", "C) Criminalité", "D) Caserne"],
    "answer": "C",
    "explanation": "Le pompier combat l'incendie, le policier combat la criminalité.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'Abstrus' ?",
    "options": ["A) Obscur", "B) Clair", "C) Lourd", "D) Triste"],
    "answer": "A",
    "explanation": "Difficile à comprendre.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Antonyme de 'Prolixe' :",
    "options": ["A) Bavard", "B) Concis", "C) Sombre", "D) Vaste"],
    "answer": "B",
    "explanation": "Bref dans ses discours.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Ciel est à Bleu ce que Sang est à :",
    "options": ["A) Rouge", "B) Cœur", "C) Liquide", "D) Veine"],
    "answer": "A",
    "explanation": "Couleur caractéristique.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'Conjoncture' ?",
    "options": ["A) Hypothèse", "B) Situation globale", "C) Maladie", "D) Articulation"],
    "answer": "B",
    "explanation": "La situation économique ou politique.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Il a fait une ___.",
    "options": ["A) conjecture", "B) conjoncture", "C) conjuration", "D) conjonctive"],
    "answer": "A",
    "explanation": "Une hypothèse.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Il a su ___ l'argent.",
    "options": ["A) recouvrir", "B) recouvrer", "C) récupérer", "D) couvrir"],
    "answer": "B",
    "explanation": "Rentrer en possession (finances, santé).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Son arrivée est ___.",
    "options": ["A) éminente", "B) imminente", "C) iminente", "D) émanente"],
    "answer": "B",
    "explanation": "Qui va se produire bientôt.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Un professeur ___.",
    "options": ["A) imminent", "B) éminent", "C) aminent", "D) émanent"],
    "answer": "B",
    "explanation": "Remarquable, supérieur.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'Pallier' ?",
    "options": ["A) Résoudre", "B) Remédier provisoirement", "C) Remplacer", "D) Détruire"],
    "answer": "B",
    "explanation": "Remède temporaire (sans 'à').",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Phrase correcte :",
    "options": ["A) Pallier au problème", "B) Pallier le problème", "C) Pallier du problème", "D) Pallier sur le problème"],
    "answer": "B",
    "explanation": "Verbe transitif direct.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Synonyme de 'Laconique' :",
    "options": ["A) Bref", "B) Long", "C) Triste", "D) Joyeux"],
    "answer": "A",
    "explanation": "Exprimé en peu de mots.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que désigne 'Acception' ?",
    "options": ["A) Consentement", "B) Sens d'un mot", "C) Refus", "D) Erreur"],
    "answer": "B",
    "explanation": "Le sens dans lequel un mot est employé.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Le mot 'Acceptation' désigne :",
    "options": ["A) Sens d'un mot", "B) Fait d'accepter", "C) Définition", "D) Pléonasme"],
    "answer": "B",
    "explanation": "L'action de consentir.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Un repas organisé à son ___.",
    "options": ["A) attention", "B) intention", "C) inattention", "D) inttention"],
    "answer": "B",
    "explanation": "Pour lui faire honneur.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Une lettre à l'___ du chef.",
    "options": ["A) intention", "B) attention", "C) inttention", "D) attension"],
    "answer": "B",
    "explanation": "Pour qu'il la lise.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'Apanage' ?",
    "options": ["A) Privilège", "B) Désavantage", "C) Nourriture", "D) Décoration"],
    "answer": "A",
    "explanation": "Un bien ou avantage exclusif.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Antonyme de 'Gargantuesque' :",
    "options": ["A) Frugal", "B) Homérique", "C) Énorme", "D) Dantesque"],
    "answer": "A",
    "explanation": "Repas simple et peu abondant.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Synonyme de 'Pugnace' :",
    "options": ["A) Pacifique", "B) Combatif", "C) Lâche", "D) Peureux"],
    "answer": "B",
    "explanation": "Qui aime le combat.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Un comportement 'Velléitaire' :",
    "options": ["A) Déterminé", "B) Hésitant", "C) Fort", "D) Rapide"],
    "answer": "B",
    "explanation": "Qui n'a pas la volonté de passer à l'acte.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'Inanition' ?",
    "options": ["A) Absence de mouvement", "B) Manque de nourriture", "C) Folie", "D) Silence"],
    "answer": "B",
    "explanation": "Épuisement dû au manque de nourriture.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Figure: 'Une obscure clarté'",
    "options": ["A) Oxymore", "B) Euphémisme", "C) Litote", "D) Pléonasme"],
    "answer": "A",
    "explanation": "Deux termes de sens contraire liés.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Figure: 'Il nous a quittés' (pour mort)",
    "options": ["A) Euphémisme", "B) Litote", "C) Hyperbole", "D) Oxymore"],
    "answer": "A",
    "explanation": "Atténuation d'une réalité brutale.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Figure: 'Je ne te hais point'",
    "options": ["A) Litote", "B) Euphémisme", "C) Allitération", "D) Comparaison"],
    "answer": "A",
    "explanation": "Dire moins pour suggérer plus.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qu'est-ce qu'un 'Acrostiche' ?",
    "options": ["A) Poème où les initiales forment un mot", "B) Vers de 12 syllabes", "C) Répétition de son", "D) Roman court"],
    "answer": "A",
    "explanation": "Initiales des vers lues verticalement.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Adjectif 'Obséquieux' :",
    "options": ["A) Servile", "B) Funèbre", "C) Triste", "D) Rapide"],
    "answer": "A",
    "explanation": "Exagère la politesse par hypocrisie.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Une 'Invective' :",
    "options": ["A) Insulte", "B) Compliment", "C) Outil", "D) Solution"],
    "answer": "A",
    "explanation": "Discours violent et injurieux.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "'Volubile' signifie :",
    "options": ["A) Parle beaucoup", "B) Vole", "C) Rond", "D) Changeant"],
    "answer": "A",
    "explanation": "Parle avec abondance et rapidité.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Éphémère/Durable : Fictif/___",
    "options": ["A) Réel", "B) Virtuel", "C) Imaginaire", "D) Faux"],
    "answer": "A",
    "explanation": "Relation d'antonymie.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'Fiduciaire' ?",
    "options": ["A) Basé sur la confiance", "B) Légal", "C) Solide", "D) Faux"],
    "answer": "A",
    "explanation": "Du latin fiducia, relatif à la confiance (monnaie).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Adjectif 'Bucolique' :",
    "options": ["A) Campagnard", "B) Marin", "C) Urbain", "D) Céleste"],
    "answer": "A",
    "explanation": "Relatif à la campagne, pastoral.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Propos 'Dithyrambique' :",
    "options": ["A) Élogieux", "B) Critique", "C) Triste", "D) Court"],
    "answer": "A",
    "explanation": "Éloge très enthousiaste.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Antonyme de 'Taciturne' :",
    "options": ["A) Loquace", "B) Silencieux", "C) Muet", "D) Sombre"],
    "answer": "A",
    "explanation": "Taciturne = qui parle peu. Loquace = bavard.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "'Tomber en désuétude' :",
    "options": ["A) N'être plus utilisé", "B) Se casser", "C) Être populaire", "D) Disparaître subitement"],
    "answer": "A",
    "explanation": "Ne plus être en usage.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Intrus parmi synonymes de 'Pusillanime' :",
    "options": ["A) Hardi", "B) Timoré", "C) Couard", "D) Peureux"],
    "answer": "A",
    "explanation": "Hardi est l'antonyme (audacieux).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'Idoine' ?",
    "options": ["A) Approprié", "B) Stupide", "C) Ignorant", "D) Vaste"],
    "answer": "A",
    "explanation": "Qui convient parfaitement à la situation.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Antonyme de 'Altruiste' :",
    "options": ["A) Égoïste", "B) Généreux", "C) Bon", "D) Saint"],
    "answer": "A",
    "explanation": "Contraire du dévouement à autrui.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Propos 'Acerbe' :",
    "options": ["A) Blessant", "B) Doux", "C) Calme", "D) Court"],
    "answer": "A",
    "explanation": "Dur, piquant, acide.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "'Pécuniaire' est relatif à :",
    "options": ["A) L'argent", "B) La loi", "C) La santé", "D) L'art"],
    "answer": "A",
    "explanation": "De la pecunia (monnaie).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Il ne faut pas ___ la faute à d'autres.",
    "options": ["A) imputer", "B) amputer", "C) empoter", "D) impacter"],
    "answer": "A",
    "explanation": "Attribuer une faute.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "'Inhérent' :",
    "options": ["A) Lié de façon intime", "B) Extérieur", "C) Passager", "D) Lointain"],
    "answer": "A",
    "explanation": "Uni de façon inséparable.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "'Subreptice' :",
    "options": ["A) Furtif", "B) Légal", "C) Bruyant", "D) Long"],
    "answer": "A",
    "explanation": "Fait en cachette.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que désigne 'Apathie' ?",
    "options": ["A) Indifférence/Manque d'énergie", "B) Empathie", "C) Haine", "D) Peur"],
    "answer": "A",
    "explanation": "Absence de volonté et d'émotion.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Une réponse 'Ambiguë' :",
    "options": ["A) À double sens", "B) Claire", "C) Longue", "D) Courte"],
    "answer": "A",
    "explanation": "Peut s'interpréter de plusieurs façons.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "'Véloce' :",
    "options": ["A) Rapide", "B) Lourd", "C) Méchant", "D) Fort"],
    "answer": "A",
    "explanation": "Agile, rapide.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qu'est-ce qu'un 'Pléonasme' ?",
    "options": ["A) Répétition de mots de même sens", "B) Mots contraires", "C) Rime", "D) Contresens"],
    "answer": "A",
    "explanation": "Exemple: descendre en bas.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Un 'Syllogisme' :",
    "options": ["A) Raisonnement en 3 temps", "B) Poème", "C) Insulte", "D) Figure d'opposition"],
    "answer": "A",
    "explanation": "Déduction logique (prémisses + conclusion).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "'Synergies' :",
    "options": ["A) Actions coordonnées", "B) Conflits", "C) Divergences", "D) Échecs"],
    "answer": "A",
    "explanation": "Effet combiné supérieur aux effets isolés.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'Ajourner' ?",
    "options": ["A) Remettre à plus tard", "B) Annuler définitivement", "C) Accélérer", "D) Mettre au jour"],
    "answer": "A",
    "explanation": "Reporter à un autre jour.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le synonyme de 'Déluré' ?",
    "options": ["A) Dégourdi", "B) Timide", "C) Hésitant", "D) Naïf"],
    "answer": "A",
    "explanation": "Déluré signifie dégourdi.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le synonyme de 'Arbitraire' ?",
    "options": ["A) Juste", "B) Légal", "C) Discrétionnaire", "D) Logique"],
    "answer": "C",
    "explanation": "Arbitraire signifie discrétionnaire.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de 'Prolixe' ?",
    "options": ["A) Bavard", "B) Laconique", "C) Éloquent", "D) Verbeux"],
    "answer": "B",
    "explanation": "Prolixe (bavard) a pour antonyme laconique (bref).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de 'Coordination' ?",
    "options": ["A) Entente", "B) Désorganisation", "C) Accord", "D) Harmonie"],
    "answer": "B",
    "explanation": "Désorganisation est l'antonyme de coordination.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de 'Estimer' ?",
    "options": ["A) Évaluer", "B) Déprécier", "C) Juger", "D) Calculer"],
    "answer": "B",
    "explanation": "L'antonyme d'estimer est déprécier.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le synonyme de 'Austère' ?",
    "options": ["A) Joyeux", "B) Luxueux", "C) Sévère", "D) Frivole"],
    "answer": "C",
    "explanation": "Austère est synonyme de sévère.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Parmi les propositions, quel est l'antonyme de 'Austère' ?",
    "options": ["A) Sévère", "B) Luxueux", "C) Rigide", "D) Sobre"],
    "answer": "B",
    "explanation": "Luxueux ou Frivole sont des antonymes de austère.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le synonyme de 'Magnanime' ?",
    "options": ["A) Rancunier", "B) Égoïste", "C) Généreux", "D) Cruel"],
    "answer": "C",
    "explanation": "Magnanime signifie généreux.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de 'Magnanime' ?",
    "options": ["A) Généreux", "B) Altruiste", "C) Rancunier", "D) Bienveillant"],
    "answer": "C",
    "explanation": "Rancunier est l'antonyme de magnanime.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie le mot 'Taciturne' ?",
    "options": ["A) Bavard", "B) Bruyant", "C) Silencieux", "D) Expressif"],
    "answer": "C",
    "explanation": "Taciturne est synonyme de silencieux.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de 'Taciturne' ?",
    "options": ["A) Silencieux", "B) Mutique", "C) Bavard", "D) Renfermé"],
    "answer": "C",
    "explanation": "L'antonyme de taciturne est bavard.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que veut dire 'Succinct' ?",
    "options": ["A) Bref", "B) Détaillé", "C) Long", "D) Vaste"],
    "answer": "A",
    "explanation": "Succinct signifie bref.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de 'Succinct' ?",
    "options": ["A) Bref", "B) Court", "C) Concis", "D) Détaillé"],
    "answer": "D",
    "explanation": "Détaillé est l'antonyme de succinct.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le synonyme de 'Péremptoire' ?",
    "options": ["A) Hésitant", "B) Catégorique", "C) Douteux", "D) Souple"],
    "answer": "B",
    "explanation": "Péremptoire signifie catégorique.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de 'Fallacieux' ?",
    "options": ["A) Trompeur", "B) Illusoire", "C) Sincère", "D) Mensonger"],
    "answer": "C",
    "explanation": "Sincère est l'antonyme de fallacieux.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Comment s'écrit correctement le mot signifiant un choc violent ?",
    "options": ["A) Collusion", "B) Collision", "C) Colusion", "D) Colision"],
    "answer": "B",
    "explanation": "Une collision est un choc, à ne pas confondre avec collusion (entente secrète).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie le paronyme 'Collusion' ?",
    "options": ["A) Choc", "B) Accident", "C) Entente secrète", "D) Dispute"],
    "answer": "C",
    "explanation": "Une collusion est une entente secrète.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle est la définition de 'Conjoncture' ?",
    "options": ["A) Hypothèse", "B) Supposition", "C) Situation", "D) Conséquence"],
    "answer": "C",
    "explanation": "La conjoncture désigne une situation (ex: économique).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle est la définition de 'Conjecture' ?",
    "options": ["A) Situation", "B) Hypothèse", "C) Fait avéré", "D) Preuve"],
    "answer": "B",
    "explanation": "Une conjecture est une hypothèse.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Complétez : Des robes ___",
    "options": ["A) bleues ciel", "B) bleues ciels", "C) bleu ciel", "D) bleu ciels"],
    "answer": "C",
    "explanation": "Les adjectifs de couleur composés sont invariables (bleu ciel).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Complétez : Des vestes ___",
    "options": ["A) rouge sang", "B) rouges sangs", "C) rouges sang", "D) rouge sangs"],
    "answer": "A",
    "explanation": "Invariable car adjectif de couleur composé.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Comment s'écrit le nombre 300 en lettres ?",
    "options": ["A) Trois cent", "B) Trois cents", "C) Trois-cents", "D) Trois-cent"],
    "answer": "B",
    "explanation": "Cent prend un s s'il est multiplié et termine le nombre (trois cents).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Comment s'écrit 82 en lettres ?",
    "options": ["A) Quatre-vingt-deux", "B) Quatre-vingts-deux", "C) Quatre-vingt deux", "D) Quatre vingts deux"],
    "answer": "A",
    "explanation": "Vingt ne prend pas de s car il ne termine pas le nombre (quatre-vingt-deux).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Comment s'écrit 300 000 en lettres ?",
    "options": ["A) Trois cents milles", "B) Trois cents mille", "C) Trois cent mille", "D) Trois cent milles"],
    "answer": "C",
    "explanation": "Cent est multiplié mais suivi de mille, donc invariable (trois cent mille).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le pluriel de 'chou-fleur' ?",
    "options": ["A) chou-fleur", "B) choux-fleur", "C) chou-fleurs", "D) choux-fleurs"],
    "answer": "D",
    "explanation": "Nom composé (nom+nom), les deux prennent la marque du pluriel.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le pluriel de 'arc-en-ciel' ?",
    "options": ["A) arcs-en-ciel", "B) arc-en-ciels", "C) arcs-en-ciels", "D) arcs-en-cieux"],
    "answer": "A",
    "explanation": "Le premier mot (nom) prend la marque du pluriel, le second (complément) reste invariable.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le pluriel de 'timbre-poste' ?",
    "options": ["A) timbre-postes", "B) timbres-postes", "C) timbres-poste", "D) timbre-poste"],
    "answer": "C",
    "explanation": "Pluriel : timbres-poste (des timbres pour la poste).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Complétez : Les pommes qu'il a ___",
    "options": ["A) mangé", "B) mangés", "C) mangées", "D) mangée"],
    "answer": "C",
    "explanation": "Le PP avec avoir s'accorde avec le COD placé avant (les pommes = féminin pluriel).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Complétez : Elles se sont ___ les mains.",
    "options": ["A) lavé", "B) lavés", "C) lavées", "D) lavée"],
    "answer": "A",
    "explanation": "Le COD (les mains) est placé après, le participe reste invariable.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Complétez : Ils se sont ___ la vérité.",
    "options": ["A) dit", "B) dits", "C) dite", "D) dites"],
    "answer": "A",
    "explanation": "Le pronom 'se' est COI (ils ont dit la vérité à qui ? à eux-mêmes), donc invariable.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle figure de style consiste à feindre de ne pas dire ce qu'on exprime néanmoins ?",
    "options": ["A) Oxymore", "B) Prétérition", "C) Métaphore", "D) Hyperbole"],
    "answer": "B",
    "explanation": "C'est la prétérition.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "L'expression 'obscure clarté' est un exemple de :",
    "options": ["A) Pléonasme", "B) Litote", "C) Oxymore", "D) Euphémisme"],
    "answer": "C",
    "explanation": "Un oxymore relie deux mots de sens opposés.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "La phrase 'la nature est un temple' est un exemple de :",
    "options": ["A) Comparaison", "B) Métaphore", "C) Allégorie", "D) Personnification"],
    "answer": "B",
    "explanation": "C'est une métaphore car c'est une comparaison sans outil de comparaison.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dire 'je meurs de soif' relève de quelle figure de style ?",
    "options": ["A) Euphémisme", "B) Hyperbole", "C) Antithèse", "D) Chiasme"],
    "answer": "B",
    "explanation": "C'est une exagération, donc une hyperbole.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Comment appelle-t-on l'emploi d'un mot déformé (ex: rénumérations) ?",
    "options": ["A) Solécisme", "B) Néologisme", "C) Barbarisme", "D) Archaïsme"],
    "answer": "C",
    "explanation": "C'est un barbarisme.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que désigne un 'janotisme' ou 'amphibologie' ?",
    "options": ["A) Une faute d'accord", "B) Une construction de phrase ambiguë", "C) Un mot inventé", "D) Une figure d'atténuation"],
    "answer": "B",
    "explanation": "C'est une phrase ambiguë prête à double sens.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel mot parmi ces choix est un palindrome ?",
    "options": ["A) Avion", "B) Ressasser", "C) Bateau", "D) Refaire"],
    "answer": "B",
    "explanation": "Ressasser peut se lire dans les deux sens, c'est un palindrome.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie la locution latine 'A priori' ?",
    "options": ["A) Après l'expérience", "B) Avant l'expérience", "C) Par conséquent", "D) Sans preuve"],
    "answer": "B",
    "explanation": "A priori signifie 'avant l'expérience'.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'Casus belli' ?",
    "options": ["A) Cas de paix", "B) Raison d'État", "C) Motif de guerre", "D) Alliance militaire"],
    "answer": "C",
    "explanation": "Casus belli est un motif de guerre.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie 'In vino veritas' ?",
    "options": ["A) La vie est dans le vin", "B) Le vin rend fort", "C) Le vin est dangereux", "D) La vérité est dans le vin"],
    "answer": "D",
    "explanation": "Cela signifie que l'alcool délie les langues et révèle la vérité.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle est la traduction de 'Pacta sunt servanda' ?",
    "options": ["A) Les pactes sont secrets", "B) Les contrats doivent être respectés", "C) Les alliances sont éphémères", "D) La paix est primordiale"],
    "answer": "B",
    "explanation": "Cette maxime juridique indique que les contrats lient les parties.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Lequel de ces mots possède un double genre ?",
    "options": ["A) Augure", "B) Amour", "C) Termite", "D) Tubercule"],
    "answer": "B",
    "explanation": "Amour est de double genre (masculin au singulier, souvent féminin au pluriel dans la poésie).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le genre du mot 'scolopendre' ?",
    "options": ["A) Masculin", "B) Féminin", "C) Neutre", "D) Double genre"],
    "answer": "B",
    "explanation": "Scolopendre est de genre féminin (une scolopendre).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'auteur de l'œuvre 'Climbié' ?",
    "options": ["A) Seydou Badian", "B) Sembène Ousmane", "C) Bernard Dadié", "D) Mongo Beti"],
    "answer": "C",
    "explanation": "Climbié a été écrit par Bernard Dadié.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qui a rédigé 'Le pauvre Christ de Bomba' ?",
    "options": ["A) Mongo Beti", "B) Ferdinand Oyono", "C) Camara Laye", "D) Bernard Dadié"],
    "answer": "A",
    "explanation": "Le pauvre Christ de Bomba est de Mongo Beti.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel auteur a écrit 'Une vie de boy' ?",
    "options": ["A) Sembène Ousmane", "B) Seydou Badian", "C) Ferdinand Oyono", "D) Ahmadou Kourouma"],
    "answer": "C",
    "explanation": "L'auteur d'Une vie de boy est Ferdinand Oyono.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "De qui est l'ouvrage 'L'Enfant noir' ?",
    "options": ["A) Camara Laye", "B) Mongo Beti", "C) Bernard Dadié", "D) Seydou Badian"],
    "answer": "A",
    "explanation": "C'est le chef-d'œuvre de Camara Laye.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est l'antonyme de 'austère' ?",
    "options": ["A) Luxueux", "B) Sévère", "C) Péremptoire", "D) Déluré"],
    "answer": "A",
    "explanation": "Austère signifie dépourvu d'ornement, rigide. Son antonyme le plus commun dans ce contexte est luxueux ou fastueux.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans la phrase 'Cette obscure clarté qui tombe des étoiles' (Corneille), quelle est la figure de style ?",
    "options": ["A) Oxymore", "B) Métaphore", "C) Antithèse", "D) Hyperbole"],
    "answer": "A",
    "explanation": "L'alliance de deux termes de sens opposés (obscure / clarté) dans un même syntagme est un oxymore.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie l'expression 'péremptoire' ?",
    "options": ["A) Silencieux", "B) Catégorique", "C) Généreux", "D) Trompeur"],
    "answer": "B",
    "explanation": "Péremptoire : qui détruit d'avance toute objection, qui est catégorique.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Trouvez le synonyme de 'fallacieux' :",
    "options": ["A) Véridique", "B) Succinct", "C) Trompeur", "D) Taciturne"],
    "answer": "C",
    "explanation": "Fallacieux vient du latin 'fallax' (trompeur) ; un argument fallacieux cherche à tromper, à induire en erreur.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que dénonce la locution latine 'casus belli' ?",
    "options": ["A) Un motif de guerre", "B) Un jugement final", "C) Une paix durable", "D) La vérité dans le vin"],
    "answer": "A",
    "explanation": "Casus belli se traduit par 'cas de guerre', l'acte de nature à déclencher un conflit.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie la locution 'pacta sunt servanda' ?",
    "options": ["A) La chose est jugée.", "B) Les conventions doivent être respectées.", "C) La vérité est dans le vin.", "D) Avant toute expérience."],
    "answer": "B",
    "explanation": "C'est un principe fondamental du droit international : les pactes (traités) doivent être respectés.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Lequel de ces couples de mots correspond à des paronymes ?",
    "options": ["A) Mer / Mère", "B) Collision / Collusion", "C) Grand / Petit", "D) Rapide / Véloce"],
    "answer": "B",
    "explanation": "Les paronymes sont des mots qui se ressemblent fortement par leur forme ou leur prononciation mais qui n'ont pas le même sens.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle est la figure de style dans : 'La nature est un temple où de vivants piliers...' ?",
    "options": ["A) Métonymie", "B) Comparaison", "C) Métaphore", "D) Oxymore"],
    "answer": "C",
    "explanation": "L'assimilation directe de la nature à un temple sans outil de comparaison ('comme') est une métaphore.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Complétez l'analogie. Chien est à aboyer ce que Cheval est à :",
    "options": ["A) Hennir", "B) Bêler", "C) Mugir", "D) Rugir"],
    "answer": "A",
    "explanation": "Le cri du chien est l'aboiement, celui du cheval est le hennissement.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "La confusion entre deux paronymes s'appelle :",
    "options": ["A) Un barbarisme", "B) Une prétérition", "C) Une amphibologie", "D) Un solécisme"],
    "answer": "A",
    "explanation": "Le fait de forger un mot inexistant, de déformer un mot ou de confondre deux paronymes peut être qualifié de barbarisme lexical.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "L'auteur du roman 'Les Soleils des indépendances' est :",
    "options": ["A) Bernard Dadié", "B) Ahmadou Kourouma", "C) Mongo Beti", "D) Ferdinand Oyono"],
    "answer": "B",
    "explanation": "Publié en 1968, c'est l'œuvre majeure de l'Ivoirien Ahmadou Kourouma.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans l'expression 'Je ne vous dirai pas que son intelligence est remarquable', il y a :",
    "options": ["A) Une litote", "B) Une prétérition", "C) Un euphémisme", "D) Une métaphore"],
    "answer": "B",
    "explanation": "La prétérition consiste à affirmer que l'on ne va pas dire quelque chose tout en le disant.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie l'adjectif 'taciturne' ?",
    "options": ["A) Bruyant", "B) Silencieux", "C) Arrogant", "D) Frivole"],
    "answer": "B",
    "explanation": "Taciturne se dit d'une personne qui par nature parle peu, qui est silencieuse, souvent d'humeur sombre.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Différence de sens entre 'conjoncture' et 'conjecture' :",
    "options": ["A) Situation économique / Hypothèse", "B) Hypothèse / Situation", "C) Affirmation / Négation", "D) Vrai / Faux"],
    "answer": "A",
    "explanation": "Conjoncture : situation, ensemble d'éléments (économiques, politiques). Conjecture : hypothèse, supposition.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel écrivain africain a écrit 'Une vie de boy' ?",
    "options": ["A) Camara Laye", "B) Ferdinand Oyono", "C) Sembène Ousmane", "D) Seydou Badian"],
    "answer": "B",
    "explanation": "Roman publié en 1956 par le Camerounais Ferdinand Oyono.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle figure de style est présente dans 'Je meurs de soif' ?",
    "options": ["A) La litote", "B) La prétérition", "C) L'hyperbole", "D) La métaphore"],
    "answer": "C",
    "explanation": "L'hyperbole est une figure d'exagération (on ne meurt pas réellement à l'instant même de soif).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qui a écrit 'Le Docker noir' ?",
    "options": ["A) Sembène Ousmane", "B) Bernard Dadié", "C) Mongo Beti", "D) Ahmadou Kourouma"],
    "answer": "A",
    "explanation": "Publié en 1956, c'est le premier roman de l'écrivain et cinéaste sénégalais Sembène Ousmane.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie la locution 'in vino veritas' ?",
    "options": ["A) Le vin est un poison.", "B) La vérité est dans le vin.", "C) Le vin de la victoire.", "D) Acheter du vin."],
    "answer": "B",
    "explanation": "Proverbe latin signifiant qu'une personne ivre a tendance à dire la vérité ou ce qu'elle pense réellement.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Si 'arbitraire' correspond à 'discrétionnaire', alors 'succinct' correspond à :",
    "options": ["A) Détaillé", "B) Bref", "C) Allongé", "D) Verbeux"],
    "answer": "B",
    "explanation": "Succinct signifie qui est énoncé en peu de mots, bref, concis.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Le janotisme ou l'amphibologie désigne :",
    "options": ["A) Une construction syntaxique obscure à double sens.", "B) Un néologisme régional.", "C) Une figure d'exagération.", "D) Une faute d'orthographe."],
    "answer": "A",
    "explanation": "L'amphibologie est un double sens dû à la syntaxe ('J'ai vu un homme avec des jumelles').",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Qui est l'auteur de 'Climbié' ?",
    "options": ["A) Bernard Dadié", "B) Camara Laye", "C) Mongo Beti", "D) Seydou Badian"],
    "answer": "A",
    "explanation": "Climbié est un roman largement autobiographique de l'écrivain ivoirien Bernard Dadié, paru en 1956.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Le mot 'Kayak' est un exemple de :",
    "options": ["A) Métaphore", "B) Paronyme", "C) Palindrome", "D) Pléonasme"],
    "answer": "C",
    "explanation": "Comme 'radar', 'kayak' se lit de la même façon dans les deux sens.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel écrivain guinéen est l'auteur de 'L'Enfant noir' (1953) ?",
    "options": ["A) Ahmadou Kourouma", "B) Camara Laye", "C) Sembène Ousmane", "D) Cheikh Hamidou Kane"],
    "answer": "B",
    "explanation": "Camara Laye a écrit ce célèbre roman autobiographique décrivant son enfance en Haute-Guinée.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que veut dire l'expression 'res judicata' ?",
    "options": ["A) La chose publique", "B) L'autorité de la chose jugée", "C) L'affaire en cours", "D) Le droit de juger"],
    "answer": "B",
    "explanation": "Res judicata pro veritate habetur (la chose jugée est tenue pour vérité), ce qui signifie qu'un jugement définitif ne peut être remis en cause.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Complétez l'analogie : Le pauvre Mongo Beti est l'auteur de 'Le Pauvre Christ de Bomba', Seydou Badian est l'auteur de :",
    "options": ["A) Une vie de boy", "B) Sous l'orage", "C) Docker noir", "D) Climbié"],
    "answer": "B",
    "explanation": "Seydou Badian Kouyaté, écrivain et homme politique malien, est l'auteur de 'Sous l'orage'.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le synonyme de l'adjectif 'véloce' ?",
    "options": ["A) Lent", "B) Rapide", "C) Agréable", "D) Cruel"],
    "answer": "B",
    "explanation": "Véloce (qui a de la vélocité) signifie rapide.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Dans 'Elle est belle à mourir', quelle figure de style utilise-t-on ?",
    "options": ["A) La litote", "B) L'hyperbole", "C) La métaphore", "D) La métonymie"],
    "answer": "B",
    "explanation": "L'exagération 'à mourir' souligne l'intensité de la beauté, c'est une hyperbole.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Si 'discrétionnaire' = 'arbitraire', alors 'taciturne' =",
    "options": ["A) Loquace", "B) Silencieux", "C) Affable", "D) Joyeux"],
    "answer": "B",
    "explanation": "Un synonyme direct.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Le mot 'mémoire' (le document écrit) est de quel genre ?",
    "options": ["A) Féminin", "B) Masculin", "C) Neutre", "D) Variable"],
    "answer": "B",
    "explanation": "Un mémoire (document, écrit académique) est masculin. La mémoire (la faculté) est féminine.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que qualifie-t-on d' 'éphémère' ?",
    "options": ["A) Ce qui dure toujours", "B) Ce qui ne dure qu'un jour", "C) Ce qui est transparent", "D) Ce qui est lumineux"],
    "answer": "B",
    "explanation": "Éphémère (du grec ephemeros, d'un jour) qualifie ce qui a une durée très courte.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que veut dire le mot 'allégorie' ?",
    "options": ["A) Une fausse vérité", "B) La représentation d'une idée abstraite sous une forme concrète", "C) Une exagération manifeste", "D) L'omission d'une conjonction"],
    "answer": "B",
    "explanation": "Comme la faucheuse pour la mort, ou la balance pour la justice.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel paronyme faut-il utiliser dans : 'Il a fait une ... pour expliquer la crise' ?",
    "options": ["A) conjoncture", "B) conjecture", "C) collision", "D) collusion"],
    "answer": "B",
    "explanation": "Conjecture = hypothèse, explication non vérifiée.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel auteur africain a écrit 'Les Soleils des indépendances' ?",
    "options": ["A) Léopold Sédar Senghor", "B) Ahmadou Kourouma", "C) Wole Soyinka", "D) Tchicaya U Tam'si"],
    "answer": "B",
    "explanation": "Kourouma est l'auteur des Soleils des indépendances.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Le mot 'voile' a un double genre. Quel est son sens au masculin ?",
    "options": ["A) Pièce de tissu pour faire avancer un bateau", "B) Pièce de tissu destinée à cacher, à recouvrir", "C) Le sport nautique", "D) Le dôme du palais"],
    "answer": "B",
    "explanation": "Un voile (pour cacher le visage ou mariée). La voile (bateau).",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que signifie l'adjectif 'dithyrambique' ?",
    "options": ["A) Très critique", "B) Élogieux, enthousiaste à l'excès", "C) Silencieux", "D) Avare"],
    "answer": "B",
    "explanation": "Faire des éloges emphatiques.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Complétez la locution latine : 'Errare humanum est, perseverare ...'",
    "options": ["A) divinum", "B) diabolicum", "C) veritas", "D) absurdum"],
    "answer": "B",
    "explanation": "L'erreur est humaine, s'entêter [dans son erreur] est diabolique.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Le néologisme consiste à :",
    "options": ["A) Emprunter un mot à une autre langue", "B) Créer un nouveau mot ou donner un sens nouveau à un mot existant", "C) Répéter un mot en fin de phrase", "D) Inverser l'ordre des mots"],
    "answer": "B",
    "explanation": "Néologisme : mot nouveau.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Si 'prolixe' = 'bavard', 'laconique' =",
    "options": ["A) Triste", "B) Concis, bref", "C) Volubile", "D) Bavard"],
    "answer": "B",
    "explanation": "Laconique : qui s'exprime en peu de mots.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "L'expression 'c'est mon talon d'Achille' est :",
    "options": ["A) Une périphrase", "B) Une métaphore lexicalisée (ou allusion mythologique)", "C) Un pléonasme", "D) Un palindrome"],
    "answer": "B",
    "explanation": "Désigne le point faible de quelqu'un.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Que désigne le terme 'synecdoque' ?",
    "options": ["A) Prendre le tout pour la partie ou la partie pour le tout", "B) Exagérer une vérité", "C) Remplacer un mot par un autre de même sonorité", "D) Parler de soi à la troisième personne"],
    "answer": "A",
    "explanation": "C'est un type particulier de métonymie.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Parmi ces auteurs, lequel n'est pas ivoirien ?",
    "options": ["A) Bernard Dadié", "B) Ahmadou Kourouma", "C) Ferdinand Oyono", "D) Isaie Biton Koulibaly"],
    "answer": "C",
    "explanation": "Ferdinand Oyono est d'origine camerounaise.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel mot n'a pas le double genre ?",
    "options": ["A) Manche", "B) Mémoire", "C) Livre", "D) Tentacule"],
    "answer": "D",
    "explanation": "Tentacule est exclusivement masculin.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Un discours 'ampoulé' est un discours :",
    "options": ["A) Très clair et concis", "B) Éclairant et instructif", "C) Prétentieux, chargé, emphatique", "D) Dénué de sens"],
    "answer": "C",
    "explanation": "Style emphatique, boursouflé.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "L'antonyme de 'altruiste' est :",
    "options": ["A) Généreux", "B) Égoïste", "C) Taciturne", "D) Habile"],
    "answer": "B",
    "explanation": "L'altruisme est le dévouement aux autres, l'égoïsme est le contraire.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quel est le sens figuré de 'jeter l'éponge' ?",
    "options": ["A) Nettoyer", "B) Se fâcher", "C) Abandonner", "D) Vaincre"],
    "answer": "C",
    "explanation": "Issu de la boxe, jeter l'éponge signifie abandonner le combat.",
    "theme": "Aptitude Verbale — Phénomènes lexicaux"
  },
  {
    "question": "Quelle est la capitale du Togo ?",
    "options": ["A) Porto-Novo", "B) Lomé", "C) Cotonou", "D) Ouagadougou"],
    "answer": "B",
    "explanation": "Lomé est la capitale du Togo.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Burkina Faso ?",
    "options": ["A) Bamako", "B) Niamey", "C) Ouagadougou", "D) Dakar"],
    "answer": "C",
    "explanation": "Ouagadougou est la capitale du Burkina Faso.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quelle partie du corps se trouve le fémur ?",
    "options": ["A) Le bras", "B) La jambe", "C) Le dos", "D) Le pied"],
    "answer": "B",
    "explanation": "Le fémur est l'os de la cuisse, dans la jambe.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Si je suis le gendre de Paul, qui est Paul pour moi ?",
    "options": ["A) Mon père", "B) Mon frère", "C) Mon beau-père", "D) Mon oncle"],
    "answer": "C",
    "explanation": "Le gendre est le mari de la fille, donc Paul est mon beau-père.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Sur quoi portent principalement les recherches de Louis Pasteur ?",
    "options": ["A) L'électricité", "B) Les microbes et vaccins", "C) La mécanique", "D) L'astronomie"],
    "answer": "B",
    "explanation": "Louis Pasteur est célèbre pour ses travaux sur les microbes et la vaccination.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quel océan navigue-t-on au large de Tokyo ?",
    "options": ["A) Océan Atlantique", "B) Océan Pacifique", "C) Océan Indien", "D) Océan Arctique"],
    "answer": "B",
    "explanation": "Tokyo se situe sur la côte de l'océan Pacifique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le plus petit pays du monde ?",
    "options": ["A) Monaco", "B) Le Vatican", "C) Saint-Marin", "D) Le Liechtenstein"],
    "answer": "B",
    "explanation": "Le Vatican est le plus petit pays du monde avec 0,44 km².",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays a pour monnaie le Cedi ?",
    "options": ["A) Le Ghana", "B) Le Nigeria", "C) Le Sénégal", "D) Le Togo"],
    "answer": "A",
    "explanation": "Le Cedi est la monnaie du Ghana.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "De quelle région Abengourou est-il le chef-lieu ?",
    "options": ["A) Le Moronou", "B) L'Indénié-Djuablin", "C) Le N'Zi", "D) Le Bounkani"],
    "answer": "B",
    "explanation": "Abengourou est le chef-lieu de la région de l'Indénié-Djuablin.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "De quel pays Nairobi est-il la capitale ?",
    "options": ["A) Tanzanie", "B) Kenya", "C) Ouganda", "D) Rwanda"],
    "answer": "B",
    "explanation": "Nairobi est la capitale du Kenya.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Laquelle de ces inventions est la plus récente ?",
    "options": ["A) Le téléphone", "B) L'ampoule électrique", "C) Internet", "D) La radio"],
    "answer": "C",
    "explanation": "Internet a été développé dans les années 1960-1990, bien après les autres.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l'auteur de l'œuvre « Le Petit Prince » ?",
    "options": ["A) Victor Hugo", "B) Antoine de Saint-Exupéry", "C) Albert Camus", "D) Jules Verne"],
    "answer": "B",
    "explanation": "Antoine de Saint-Exupéry a écrit « Le Petit Prince » en 1943.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le cri du corbeau ?",
    "options": ["A) Croasse", "B) Coasse", "C) Siffle", "D) Piaule"],
    "answer": "A",
    "explanation": "Le corbeau croasse.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Comment écrit-on 200 en lettres ?",
    "options": ["A) Deux-cent", "B) Deux-cents", "C) Deux cent", "D) Deux cents"],
    "answer": "D",
    "explanation": "« Deux cents » s'écrit avec « cents » au pluriel car suivi de rien.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel mode suit la conjonction « Avant que » ?",
    "options": ["A) L'indicatif", "B) Le subjonctif", "C) Le conditionnel", "D) L'impératif"],
    "answer": "B",
    "explanation": "« Avant que » est toujours suivi du subjonctif.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Cameroun ?",
    "options": ["A) Douala", "B) Yaoundé", "C) Libreville", "D) Bangui"],
    "answer": "B",
    "explanation": "Yaoundé est la capitale politique du Cameroun.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de la République démocratique du Congo ?",
    "options": ["A) Brazzaville", "B) Kinshasa", "C) Lubumbashi", "D) Goma"],
    "answer": "B",
    "explanation": "Kinshasa est la capitale de la RDC.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Gabon ?",
    "options": ["A) Libreville", "B) Port-Gentil", "C) Franceville", "D) Oyem"],
    "answer": "A",
    "explanation": "Libreville est la capitale du Gabon.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Tchad ?",
    "options": ["A) Abéché", "B) Moundou", "C) N'Djamena", "D) Sarh"],
    "answer": "C",
    "explanation": "N'Djamena est la capitale du Tchad.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Ghana ?",
    "options": ["A) Kumasi", "B) Tamale", "C) Accra", "D) Tema"],
    "answer": "C",
    "explanation": "Accra est la capitale du Ghana.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Bénin ?",
    "options": ["A) Cotonou", "B) Porto-Novo", "C) Parakou", "D) Abomey"],
    "answer": "B",
    "explanation": "Porto-Novo est la capitale administrative du Bénin, bien que Cotonou soit la capitale économique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Niger ?",
    "options": ["A) Niamey", "B) Zinder", "C) Maradi", "D) Agadez"],
    "answer": "A",
    "explanation": "Niamey est la capitale du Niger.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Sénégal ?",
    "options": ["A) Saint-Louis", "B) Thiès", "C) Dakar", "D) Ziguinchor"],
    "answer": "C",
    "explanation": "Dakar est la capitale du Sénégal.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Mali ?",
    "options": ["A) Bamako", "B) Tombouctou", "C) Sikasso", "D) Kayes"],
    "answer": "A",
    "explanation": "Bamako est la capitale du Mali.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le plus long fleuve d'Afrique ?",
    "options": ["A) Congo", "B) Niger", "C) Nil", "D) Zambèze"],
    "answer": "C",
    "explanation": "Le Nil est le plus long fleuve d'Afrique (6 650 km).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le plus haut sommet d'Afrique ?",
    "options": ["A) Mont Kenya", "B) Kilimandjaro", "C) Mont Stanley", "D) Ras Dashan"],
    "answer": "B",
    "explanation": "Le Kilimandjaro en Tanzanie culmine à 5 895 m.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de pays partagent le bassin du fleuve Niger ?",
    "options": ["A) 5", "B) 7", "C) 10", "D) 12"],
    "answer": "C",
    "explanation": "Le fleuve Niger traverse ou borde 10 pays africains.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel désert est le plus grand du monde ?",
    "options": ["A) Sahara", "B) Gobi", "C) Antarctique", "D) Kalahari"],
    "answer": "C",
    "explanation": "L'Antarctique est techniquement le plus grand désert (désert froid).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le plus grand désert chaud du monde ?",
    "options": ["A) Kalahari", "B) Sahara", "C) Gobi", "D) Arabie"],
    "answer": "B",
    "explanation": "Le Sahara est le plus grand désert chaud avec environ 9 millions de km².",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Comment appelle-t-on le gendre pour les parents de l'épouse ?",
    "options": ["A) Beau-fils", "B) Beau-frère", "C) Neveu", "D) Cousin"],
    "answer": "A",
    "explanation": "Le gendre est le beau-fils pour les parents de l'épouse.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Comment appelle-t-on la belle-fille pour les parents du mari ?",
    "options": ["A) Nièce", "B) Bru", "C) Belle-sœur", "D) Cousine"],
    "answer": "B",
    "explanation": "La bru est l'épouse du fils (belle-fille).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le nom scientifique de la rotule ?",
    "options": ["A) Tibia", "B) Fémur", "C) Patella", "D) Humérus"],
    "answer": "C",
    "explanation": "La rotule est appelée 'patella' en nomenclature anatomique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le nom scientifique du péroné ?",
    "options": ["A) Fibula", "B) Tibia", "C) Fémur", "D) Malléole"],
    "answer": "A",
    "explanation": "Le péroné est appelé 'fibula' en nomenclature anatomique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est l'os le plus long du corps humain ?",
    "options": ["A) Humérus", "B) Tibia", "C) Fémur", "D) Radius"],
    "answer": "C",
    "explanation": "Le fémur (os de la cuisse) est l'os le plus long.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien d'os compte le squelette humain adulte ?",
    "options": ["A) 186", "B) 206", "C) 226", "D) 246"],
    "answer": "B",
    "explanation": "Le squelette adulte compte 206 os.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a découvert la loi de la gravitation universelle ?",
    "options": ["A) Galilée", "B) Newton", "C) Einstein", "D) Kepler"],
    "answer": "B",
    "explanation": "Isaac Newton a formulé la loi de la gravitation en 1687.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a découvert les rayons X ?",
    "options": ["A) Marie Curie", "B) Wilhelm Röntgen", "C) Henri Becquerel", "D) Pierre Curie"],
    "answer": "B",
    "explanation": "Wilhelm Röntgen a découvert les rayons X en 1895.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a découvert la radioactivité ?",
    "options": ["A) Marie Curie", "B) Pierre Curie", "C) Henri Becquerel", "D) Ernest Rutherford"],
    "answer": "C",
    "explanation": "Henri Becquerel a découvert la radioactivité en 1896.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a développé la théorie de la relativité ?",
    "options": ["A) Newton", "B) Bohr", "C) Einstein", "D) Planck"],
    "answer": "C",
    "explanation": "Albert Einstein a publié la relativité restreinte en 1905 et générale en 1915.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel scientifique a créé le premier vaccin contre la rage ?",
    "options": ["A) Edward Jenner", "B) Louis Pasteur", "C) Robert Koch", "D) Jonas Salk"],
    "answer": "B",
    "explanation": "Louis Pasteur a développé le vaccin contre la rage en 1885.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a inventé la première vaccination contre la variole ?",
    "options": ["A) Louis Pasteur", "B) Edward Jenner", "C) Robert Koch", "D) Alexander Fleming"],
    "answer": "B",
    "explanation": "Edward Jenner a développé le vaccin contre la variole en 1796.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le cri du lion ?",
    "options": ["A) Rugit", "B) Brame", "C) Hurle", "D) Gronde"],
    "answer": "A",
    "explanation": "Le lion rugit.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le cri de l'âne ?",
    "options": ["A) Hennit", "B) Brait", "C) Mugit", "D) Bêle"],
    "answer": "B",
    "explanation": "L'âne brait.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le cri du cerf ?",
    "options": ["A) Brame", "B) Rugit", "C) Hurle", "D) Aboie"],
    "answer": "A",
    "explanation": "Le cerf brame.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le cri de la grenouille ?",
    "options": ["A) Croasse", "B) Coasse", "C) Siffle", "D) Piaule"],
    "answer": "B",
    "explanation": "La grenouille coasse.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année a eu lieu la chute du mur de Berlin ?",
    "options": ["A) 1987", "B) 1989", "C) 1991", "D) 1993"],
    "answer": "B",
    "explanation": "Le mur de Berlin est tombé le 9 novembre 1989.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année a eu lieu la Révolution française ?",
    "options": ["A) 1789", "B) 1799", "C) 1804", "D) 1815"],
    "answer": "A",
    "explanation": "La Révolution française a commencé en 1789.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui était le premier président des États-Unis ?",
    "options": ["A) Thomas Jefferson", "B) John Adams", "C) George Washington", "D) Benjamin Franklin"],
    "answer": "C",
    "explanation": "George Washington a été le premier président (1789-1797).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année Christophe Colomb a-t-il découvert l'Amérique ?",
    "options": ["A) 1482", "B) 1492", "C) 1502", "D) 1512"],
    "answer": "B",
    "explanation": "Christophe Colomb a découvert l'Amérique en 1492.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de l'Australie ?",
    "options": ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"],
    "answer": "C",
    "explanation": "Canberra est la capitale de l'Australie.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Canada ?",
    "options": ["A) Toronto", "B) Montréal", "C) Vancouver", "D) Ottawa"],
    "answer": "D",
    "explanation": "Ottawa est la capitale du Canada.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Brésil ?",
    "options": ["A) Rio de Janeiro", "B) São Paulo", "C) Brasília", "D) Salvador"],
    "answer": "C",
    "explanation": "Brasília est la capitale du Brésil depuis 1960.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la devise de l'Union européenne ?",
    "options": ["A) Dollar", "B) Livre", "C) Euro", "D) Franc"],
    "answer": "C",
    "explanation": "L'euro est la monnaie officielle de l'Union européenne.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la devise du Royaume-Uni ?",
    "options": ["A) Euro", "B) Livre sterling", "C) Dollar", "D) Couronne"],
    "answer": "B",
    "explanation": "La livre sterling (GBP) est la devise du Royaume-Uni.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la planète la plus proche du Soleil ?",
    "options": ["A) Vénus", "B) Mars", "C) Mercure", "D) Terre"],
    "answer": "C",
    "explanation": "Mercure est la planète la plus proche du Soleil.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de continents existe-t-il ?",
    "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
    "answer": "C",
    "explanation": "Il y a 7 continents : Afrique, Amérique du Nord, Amérique du Sud, Antarctique, Asie, Europe, Océanie.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays a remporté la première Coupe du monde de football ?",
    "options": ["A) Brésil", "B) Argentine", "C) Uruguay", "D) Italie"],
    "answer": "C",
    "explanation": "L'Uruguay a remporté la première Coupe du monde en 1930.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a peint la Joconde ?",
    "options": ["A) Michel-Ange", "B) Léonard de Vinci", "C) Raphaël", "D) Donatello"],
    "answer": "B",
    "explanation": "Léonard de Vinci a peint la Joconde vers 1503-1506.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quel pays se trouve la tour Eiffel ?",
    "options": ["A) Italie", "B) Espagne", "C) France", "D) Belgique"],
    "answer": "C",
    "explanation": "La tour Eiffel se trouve à Paris, en France.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le symbole chimique de l'or ?",
    "options": ["A) Or", "B) Au", "C) Ag", "D) Go"],
    "answer": "B",
    "explanation": "Le symbole de l'or est Au (du latin 'aurum').",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le symbole chimique de l'argent ?",
    "options": ["A) Ar", "B) Ag", "C) Si", "D) Al"],
    "answer": "B",
    "explanation": "Le symbole de l'argent est Ag (du latin 'argentum').",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien y a-t-il de secondes dans une heure ?",
    "options": ["A) 3 000", "B) 3 600", "C) 6 000", "D) 7 200"],
    "answer": "B",
    "explanation": "1 heure = 60 minutes × 60 secondes = 3 600 secondes.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de l'Éthiopie ?",
    "options": ["A) Nairobi", "B) Khartoum", "C) Addis-Abeba", "D) Kampala"],
    "answer": "C",
    "explanation": "Addis-Abeba est la capitale de l'Éthiopie.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel océan borde l'ouest de l'Afrique ?",
    "options": ["A) Océan Indien", "B) Océan Atlantique", "C) Océan Pacifique", "D) Océan Arctique"],
    "answer": "B",
    "explanation": "L'océan Atlantique borde la côte ouest de l'Afrique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de planètes compte le système solaire ?",
    "options": ["A) 7", "B) 8", "C) 9", "D) 10"],
    "answer": "B",
    "explanation": "Le système solaire compte 8 planètes depuis le déclassement de Pluton en 2006.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays est surnommé le 'pays du Soleil Levant' ?",
    "options": ["A) Chine", "B) Corée du Sud", "C) Japon", "D) Thaïlande"],
    "answer": "C",
    "explanation": "Le Japon est traditionnellement appelé le 'pays du Soleil Levant'.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la langue officielle du Brésil ?",
    "options": ["A) Espagnol", "B) Portugais", "C) Français", "D) Anglais"],
    "answer": "B",
    "explanation": "Le portugais est la langue officielle du Brésil.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le chef-lieu du District des Lacs en Côte d'Ivoire ?",
    "options": ["A) Yamoussoukro", "B) Dimbokro", "C) Bouaflé", "D) Toumodi"],
    "answer": "B",
    "explanation": "Dimbokro est le chef-lieu du District des Lacs.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "De quelle région Bouna est-il le chef-lieu ?",
    "options": ["A) Le Zanzan", "B) Le Bounkani", "C) Le Gontougo", "D) Le Tchologo"],
    "answer": "B",
    "explanation": "Bouna est le chef-lieu de la région du Bounkani.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "De quel pays Lilongwe est-il la capitale ?",
    "options": ["A) Zambie", "B) Zimbabwe", "C) Malawi", "D) Mozambique"],
    "answer": "C",
    "explanation": "Lilongwe est la capitale du Malawi.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel nom d'oiseau utilise-t-on pour désigner un auteur de lettres anonymes ?",
    "options": ["A) Un aigle", "B) Un vautour", "C) Un corbeau", "D) Un faucon"],
    "answer": "C",
    "explanation": "On appelle « corbeau » la personne qui envoie des lettres anonymes malveillantes.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle traversée Louis Blériot a-t-il réussie en avion le 25 juillet 1909 ?",
    "options": ["A) L'Atlantique", "B) La Méditerranée", "C) La Manche", "D) Le Pacifique"],
    "answer": "C",
    "explanation": "Louis Blériot a été le premier à traverser la Manche en avion.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le nom de la maladie qui entraîne un battement trop rapide du cœur ?",
    "options": ["A) Tachycardie", "B) Bradycardie", "C) Arythmie", "D) Angine"],
    "answer": "A",
    "explanation": "La tachycardie est l'accélération anormale du rythme cardiaque.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l'auteur de l'œuvre « Le Malade imaginaire » ?",
    "options": ["A) Molière", "B) Racine", "C) Corneille", "D) Voltaire"],
    "answer": "A",
    "explanation": "Molière (Jean-Baptiste Poquelin) a écrit « Le Malade imaginaire » en 1673.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quelle ville siège l'Organisation des pays exportateurs de pétrole (OPEP) ?",
    "options": ["A) Genève", "B) New York", "C) Vienne", "D) Riyad"],
    "answer": "C",
    "explanation": "L'OPEP a son siège à Vienne, en Autriche.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Lequel de ces personnages n'est PAS issu du roman « Les Misérables » ?",
    "options": ["A) Fleur de lys", "B) Jean Valjean", "C) Cosette", "D) Gavroche"],
    "answer": "A",
    "explanation": "Fleur de lys est un personnage de « Notre-Dame de Paris », pas des « Misérables ».",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année la Côte d'Ivoire a-t-elle accédé à l'indépendance ?",
    "options": ["A) 1958", "B) 1960", "C) 1962", "D) 1963"],
    "answer": "B",
    "explanation": "La Côte d'Ivoire a proclamé son indépendance le 7 août 1960.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est le premier président de la Côte d'Ivoire ?",
    "options": ["A) Henri Konan Bédié", "B) Laurent Gbagbo", "C) Félix Houphouët-Boigny", "D) Robert Guéï"],
    "answer": "C",
    "explanation": "Félix Houphouët-Boigny est le père fondateur et premier président (1960-1993).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale administrative de la Côte d'Ivoire ?",
    "options": ["A) Abidjan", "B) Bouaké", "C) Yamoussoukro", "D) San-Pédro"],
    "answer": "C",
    "explanation": "Yamoussoukro est la capitale politique et administrative depuis 1983.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a écrit « L'enfant noir » ?",
    "options": ["A) Léopold Sédar Senghor", "B) Camara Laye", "C) Ahmadou Kourouma", "D) Mongo Béti"],
    "answer": "B",
    "explanation": "Camara Laye, écrivain guinéen, a écrit « L'enfant noir » en 1953.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a écrit « Les Soleils des Indépendances » ?",
    "options": ["A) Bernard Dadié", "B) Ahmadou Kourouma", "C) Félix Tchicaya", "D) Birago Diop"],
    "answer": "B",
    "explanation": "Ahmadou Kourouma, écrivain ivoirien, a publié ce roman en 1968.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel poète et homme politique sénégalais a cofondé le mouvement de la Négritude ?",
    "options": ["A) Aimé Césaire", "B) Léopold Sédar Senghor", "C) Léon-Gontran Damas", "D) Les trois ensemble"],
    "answer": "D",
    "explanation": "La Négritude a été fondée par Senghor, Césaire et Damas dans les années 1930.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays africain est le plus grand producteur mondial de cacao ?",
    "options": ["A) Ghana", "B) Nigeria", "C) Côte d'Ivoire", "D) Cameroun"],
    "answer": "C",
    "explanation": "La Côte d'Ivoire est le premier producteur mondial de cacao.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays a pour monnaie le Naira ?",
    "options": ["A) Ghana", "B) Nigeria", "C) Liberia", "D) Sierra Leone"],
    "answer": "B",
    "explanation": "Le Naira est la monnaie officielle du Nigeria.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays a pour monnaie le Rand ?",
    "options": ["A) Kenya", "B) Éthiopie", "C) Afrique du Sud", "D) Tanzanie"],
    "answer": "C",
    "explanation": "Le Rand est la monnaie de l'Afrique du Sud.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Rwanda ?",
    "options": ["A) Bujumbura", "B) Kigali", "C) Kampala", "D) Gitega"],
    "answer": "B",
    "explanation": "Kigali est la capitale du Rwanda.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de la Guinée-Bissau ?",
    "options": ["A) Conakry", "B) Bissau", "C) Freetown", "D) Banjul"],
    "answer": "B",
    "explanation": "Bissau est la capitale de la Guinée-Bissau.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de la Gambie ?",
    "options": ["A) Banjul", "B) Dakar", "C) Freetown", "D) Bissau"],
    "answer": "A",
    "explanation": "Banjul est la capitale de la Gambie.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Liberia ?",
    "options": ["A) Freetown", "B) Accra", "C) Monrovia", "D) Abidjan"],
    "answer": "C",
    "explanation": "Monrovia est la capitale du Liberia.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de la Sierra Leone ?",
    "options": ["A) Monrovia", "B) Freetown", "C) Conakry", "D) Banjul"],
    "answer": "B",
    "explanation": "Freetown est la capitale de la Sierra Leone.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de la République Centrafricaine ?",
    "options": ["A) Bangui", "B) Yaoundé", "C) Libreville", "D) Malabo"],
    "answer": "A",
    "explanation": "Bangui est la capitale de la République Centrafricaine.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel lac est le plus grand d'Afrique ?",
    "options": ["A) Lac Tanganyika", "B) Lac Tchad", "C) Lac Victoria", "D) Lac Malawi"],
    "answer": "C",
    "explanation": "Le lac Victoria est le plus grand lac d'Afrique (environ 68 000 km²).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a écrit « Les Fleurs du Mal » ?",
    "options": ["A) Arthur Rimbaud", "B) Charles Baudelaire", "C) Paul Verlaine", "D) Stéphane Mallarmé"],
    "answer": "B",
    "explanation": "Charles Baudelaire a publié « Les Fleurs du Mal » en 1857.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a écrit « Candide » ?",
    "options": ["A) Montesquieu", "B) Rousseau", "C) Voltaire", "D) Diderot"],
    "answer": "C",
    "explanation": "Voltaire a écrit « Candide ou l'Optimisme » en 1759.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel fleuve est le plus long d'Europe ?",
    "options": ["A) Danube", "B) Rhin", "C) Volga", "D) Loire"],
    "answer": "C",
    "explanation": "La Volga est le plus long fleuve d'Europe (environ 3 530 km).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année le Sénégal a-t-il accédé à l'indépendance ?",
    "options": ["A) 1958", "B) 1960", "C) 1962", "D) 1963"],
    "answer": "B",
    "explanation": "Le Sénégal a proclamé son indépendance le 4 avril 1960.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la principale base de lancement d'engins spatiaux aux États-Unis ?",
    "options": ["A) Houston", "B) Cap Canaveral", "C) Los Angeles", "D) Washington"],
    "answer": "B",
    "explanation": "Cap Canaveral (Kennedy Space Center) est la principale base spatiale américaine.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Depuis 2020, quel territoire pourrait devenir le 51ème État des États-Unis ?",
    "options": ["A) Porto Rico", "B) Guam", "C) Washington D.C.", "D) Samoa américaines"],
    "answer": "A",
    "explanation": "Porto Rico a voté en 2020 en faveur de son intégration comme 51ème État.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de districts administratifs compte la Côte d'Ivoire ?",
    "options": ["A) 10", "B) 12", "C) 14", "D) 31"],
    "answer": "C",
    "explanation": "La Côte d'Ivoire compte 14 districts, dont 2 districts autonomes (Abidjan et Yamoussoukro).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le symbole chimique du fer ?",
    "options": ["A) Fr", "B) Fe", "C) Fa", "D) Fi"],
    "answer": "B",
    "explanation": "Le symbole du fer est Fe (du latin 'ferrum').",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le cri de l'éléphant ?",
    "options": ["A) Barrit", "B) Rugit", "C) Mugit", "D) Brame"],
    "answer": "A",
    "explanation": "L'éléphant barrit.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le cri du cheval ?",
    "options": ["A) Brait", "B) Mugit", "C) Hennit", "D) Bêle"],
    "answer": "C",
    "explanation": "Le cheval hennit.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le plus grand fleuve de Côte d'Ivoire ?",
    "options": ["A) Le Sassandra", "B) Le Bandama", "C) Le Comoé", "D) Le Cavally"],
    "answer": "B",
    "explanation": "Le Bandama est le plus grand fleuve de Côte d'Ivoire (environ 1 050 km).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel organe détient le pouvoir législatif en Côte d'Ivoire ?",
    "options": ["A) Le gouvernement", "B) Le Sénat seul", "C) L'Assemblée nationale et le Sénat", "D) La Cour suprême"],
    "answer": "C",
    "explanation": "Le Parlement ivoirien est bicaméral : Assemblée nationale et Sénat.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la religion la plus pratiquée dans le monde ?",
    "options": ["A) L'islam", "B) Le christianisme", "C) L'hindouisme", "D) Le bouddhisme"],
    "answer": "B",
    "explanation": "Le christianisme est la religion la plus pratiquée avec environ 2,4 milliards de fidèles.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays africain a accueilli la CAN 2023 ?",
    "options": ["A) Cameroun", "B) Côte d'Ivoire", "C) Sénégal", "D) Nigeria"],
    "answer": "B",
    "explanation": "La Côte d'Ivoire a accueilli la CAN 2023 (jouée en janvier-février 2024).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a remporté la CAN 2023 ?",
    "options": ["A) Le Nigeria", "B) Le Sénégal", "C) La Côte d'Ivoire", "D) La RDC"],
    "answer": "C",
    "explanation": "La Côte d'Ivoire a remporté la CAN 2023 en battant le Nigeria en finale.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le symbole chimique du cuivre ?",
    "options": ["A) Cr", "B) Cu", "C) Co", "D) Ci"],
    "answer": "B",
    "explanation": "Le symbole du cuivre est Cu (du latin 'cuprum').",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel organe du corps humain produit l'insuline ?",
    "options": ["A) Le foie", "B) Le rein", "C) Le pancréas", "D) La rate"],
    "answer": "C",
    "explanation": "Le pancréas produit l'insuline qui régule le taux de glucose dans le sang.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le plus grand pays d'Afrique en superficie ?",
    "options": ["A) RDC", "B) Soudan", "C) Algérie", "D) Libye"],
    "answer": "C",
    "explanation": "L'Algérie est le plus grand pays d'Afrique avec environ 2,38 millions de km².",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a écrit « Une vie de boy » ?",
    "options": ["A) Mongo Béti", "B) Ferdinand Oyono", "C) Camara Laye", "D) Cheikh Hamidou Kane"],
    "answer": "B",
    "explanation": "Ferdinand Oyono, écrivain camerounais, a publié « Une vie de boy » en 1956.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a écrit « L'aventure ambiguë » ?",
    "options": ["A) Birago Diop", "B) Cheikh Hamidou Kane", "C) Ousmane Sembène", "D) Léopold Sédar Senghor"],
    "answer": "B",
    "explanation": "Cheikh Hamidou Kane, écrivain sénégalais, a publié ce roman en 1961.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de la Guinée équatoriale ?",
    "options": ["A) Bata", "B) Malabo", "C) Libreville", "D) Douala"],
    "answer": "B",
    "explanation": "Malabo est la capitale de la Guinée équatoriale.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Soudan ?",
    "options": ["A) Khartoum", "B) Djouba", "C) Le Caire", "D) Asmara"],
    "answer": "A",
    "explanation": "Khartoum est la capitale du Soudan.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Soudan du Sud ?",
    "options": ["A) Khartoum", "B) Djouba", "C) Kampala", "D) Nairobi"],
    "answer": "B",
    "explanation": "Djouba (Juba) est la capitale du Soudan du Sud.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays a pour monnaie le Yen ?",
    "options": ["A) Chine", "B) Corée du Sud", "C) Japon", "D) Thaïlande"],
    "answer": "C",
    "explanation": "Le Yen est la monnaie du Japon.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le plus petit continent ?",
    "options": ["A) Antarctique", "B) Europe", "C) Océanie", "D) Amérique du Sud"],
    "answer": "C",
    "explanation": "L'Océanie est le plus petit continent.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien d'arrondissements compte la ville d'Abidjan ?",
    "options": ["A) 10", "B) 13", "C) 15", "D) 20"],
    "answer": "A",
    "explanation": "La ville d'Abidjan compte 10 communes (arrondissements).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le sigle de la monnaie utilisée en Côte d'Ivoire ?",
    "options": ["A) CDF", "B) XOF", "C) EUR", "D) GHS"],
    "answer": "B",
    "explanation": "XOF est le code ISO du franc CFA de l'Afrique de l'Ouest (BCEAO).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel savant grec est considéré comme le père de la médecine ?",
    "options": ["A) Aristote", "B) Hippocrate", "C) Galien", "D) Archimède"],
    "answer": "B",
    "explanation": "Hippocrate (460-370 av. J.-C.) est considéré comme le père de la médecine.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays africain n'a jamais été colonisé ?",
    "options": ["A) Ghana", "B) Liberia", "C) Éthiopie", "D) Liberia et Éthiopie"],
    "answer": "D",
    "explanation": "L'Éthiopie et le Liberia sont les deux seuls pays africains n'ayant jamais été colonisés.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a découvert la pénicilline ?",
    "options": ["A) Louis Pasteur", "B) Alexander Fleming", "C) Robert Koch", "D) Jonas Salk"],
    "answer": "B",
    "explanation": "Alexander Fleming a découvert la pénicilline (antibiotique) en 1928.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le fleuve le plus long du monde ?",
    "options": ["A) Amazone", "B) Nil", "C) Mississippi", "D) Yangzi Jiang"],
    "answer": "B",
    "explanation": "Le Nil est le fleuve le plus long du monde avec environ 6 650 km.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année les attentats du 11 septembre ont-ils eu lieu ?",
    "options": ["A) 2000", "B) 2001", "C) 2002", "D) 2003"],
    "answer": "B",
    "explanation": "Les attentats du World Trade Center ont eu lieu le 11 septembre 2001.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel philosophe grec est l'auteur de « La République » ?",
    "options": ["A) Aristote", "B) Socrate", "C) Platon", "D) Épicure"],
    "answer": "C",
    "explanation": "Platon a écrit « La République » où il développe sa vision de la cité idéale.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de Madagascar ?",
    "options": ["A) Moroni", "B) Antananarivo", "C) Maputo", "D) Victoria"],
    "answer": "B",
    "explanation": "Antananarivo est la capitale de Madagascar.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel organe du corps humain filtre le sang ?",
    "options": ["A) Le cœur", "B) Le foie", "C) Le rein", "D) Le poumon"],
    "answer": "C",
    "explanation": "Les reins filtrent le sang pour éliminer les déchets sous forme d'urine.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quelle articulation du corps se situe la rotule ?",
    "options": ["A) La hanche", "B) L'epaule", "C) Le genou", "D) Le coude"],
    "answer": "C",
    "explanation": "La rotule est l'os qui protege l'articulation du genou.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Si je suis la bru de Michelle, qui est Michelle pour moi ?",
    "options": ["A) Ma soeur", "B) Ma tante", "C) Ma belle-mere", "D) Ma belle-soeur"],
    "answer": "C",
    "explanation": "La bru est l'epouse du fils : Michelle est donc la belle-mere.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel nom d'oiseau designe un auteur de lettres anonymes ?",
    "options": ["A) Aigle", "B) Perroquet", "C) Corbeau", "D) Hibou"],
    "answer": "C",
    "explanation": "Un corbeau est familierement une personne qui envoie des lettres anonymes.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Maroc ?",
    "options": ["A) Casablanca", "B) Marrakech", "C) Fes", "D) Rabat"],
    "answer": "D",
    "explanation": "Rabat est la capitale officielle du Maroc.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de la C?te d'Ivoire ?",
    "options": ["A) Abidjan", "B) Yamoussoukro", "C) Bouake", "D) San-Pedro"],
    "answer": "B",
    "explanation": "Yamoussoukro est la capitale politique de la C?te d'Ivoire depuis 1983.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le plus grand pays du monde ?",
    "options": ["A) La Russie", "B) Le Canada", "C) Les ?tats-Unis", "D) La Chine"],
    "answer": "A",
    "explanation": "La Russie est le plus grand pays du monde avec environ 17,1 millions de km2.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays a pour monnaie le Shekel ?",
    "options": ["A) Israel", "B) Jordanie", "C) Liban", "D) Syrie"],
    "answer": "A",
    "explanation": "Le nouveau Shekel est la monnaie officielle d'Israel.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle traversee Louis Bleriot a-t-il reussie en avion le 25 juillet 1909 ?",
    "options": ["A) La Mediterranee", "B) La Manche", "C) Le Rhin", "D) Le detroit de Gibraltar"],
    "answer": "B",
    "explanation": "Louis Bleriot a traverse la Manche en avion pour la premiere fois le 25 juillet 1909.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le nom de la maladie qui entraine un battement trop rapide du coeur ?",
    "options": ["A) Tachycardie", "B) Bradycardie", "C) Arythmie", "D) Angine"],
    "answer": "A",
    "explanation": "La tachycardie est une frequence cardiaque anormalement elevee (plus de 100 battements par minute).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quelle ville siege l'OPEP ?",
    "options": ["A) Ryad", "B) Dubai", "C) Vienne", "D) Geneve"],
    "answer": "C",
    "explanation": "Le siege de l'OPEP est a Vienne, en Autriche, depuis 1965.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l'auteur de Le malade imaginaire ?",
    "options": ["A) Moliere", "B) Racine", "C) Corneille", "D) La Fontaine"],
    "answer": "A",
    "explanation": "Le malade imaginaire est une comedie-ballet de Moliere (1673).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "De quelle region Bouna est-il le chef-lieu ?",
    "options": ["A) Le Poro", "B) Le Bounkani", "C) Le Hambol", "D) Le Moronou"],
    "answer": "B",
    "explanation": "Bouna est le chef-lieu de la region du Bounkani dans le Nord-Est de la C?te d'Ivoire.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de l'Egypte ?",
    "options": ["A) Alexandrie", "B) Louxor", "C) Le Caire", "D) Assouan"],
    "answer": "C",
    "explanation": "Le Caire est la capitale de l'Egypte et la ville la plus peuplee d'Afrique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Sur quoi reposent principalement les travaux de Pierre et Marie Curie ?",
    "options": ["A) La physique quantique", "B) La theorie de la relativite", "C) La radioactivite", "D) L'electromagnetisme"],
    "answer": "C",
    "explanation": "Pierre et Marie Curie ont consacre leurs recherches a la radioactivite.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quel océan navigue-t-on au large de New York ?",
    "options": ["A) Océan Indien", "B) Océan Atlantique", "C) Océan Pacifique", "D) Océan Arctique"],
    "answer": "B",
    "explanation": "New York est située sur la côte est des États-Unis, au bord de l'Océan Atlantique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de l'Afrique du Sud ?",
    "options": ["A) Johannesburg", "B) Le Cap", "C) Pretoria", "D) Durban"],
    "answer": "C",
    "explanation": "Pretoria est la capitale administrative (exécutive) de l'Afrique du Sud.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le plus haut sommet du monde ?",
    "options": ["A) K2", "B) Kilimandjaro", "C) Everest", "D) Mont Blanc"],
    "answer": "C",
    "explanation": "L'Everest (8 849 m) est le plus haut sommet du monde, situé dans l'Himalaya.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Kenya ?",
    "options": ["A) Mombasa", "B) Nairobi", "C) Kampala", "D) Dar es-Salaam"],
    "answer": "B",
    "explanation": "Nairobi est la capitale du Kenya.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Nigeria ?",
    "options": ["A) Lagos", "B) Ibadan", "C) Abuja", "D) Kano"],
    "answer": "C",
    "explanation": "Abuja est la capitale politique du Nigeria depuis 1991 (remplaçant Lagos).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le plus long fleuve d'Afrique subsaharienne ?",
    "options": ["A) Le Congo", "B) Le Niger", "C) Le Zambèze", "D) Le Sénégal"],
    "answer": "B",
    "explanation": "Le Niger est le plus long fleuve d'Afrique subsaharienne (4 200 km).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année la Côte d'Ivoire a-t-elle été admise à l'ONU ?",
    "options": ["A) 1960", "B) 1961", "C) 1963", "D) 1965"],
    "answer": "A",
    "explanation": "La Côte d'Ivoire a été admise à l'ONU le 20 septembre 1960, l'année de son indépendance.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays possède la plus grande forêt tropicale du monde ?",
    "options": ["A) La RDC", "B) L'Indonésie", "C) Le Brésil", "D) La Colombie"],
    "answer": "C",
    "explanation": "Le Brésil possède la plus grande forêt tropicale du monde : l'Amazonie.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle montagne est la plus haute d'Afrique ?",
    "options": ["A) Mont Kenya", "B) Kilimandjaro", "C) Ras Dashen", "D) Mont Cameroun"],
    "answer": "B",
    "explanation": "Le Kilimandjaro (5 895 m), en Tanzanie, est le point culminant d'Afrique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays d'Afrique de l'Ouest est le plus peuplé ?",
    "options": ["A) Ghana", "B) Sénégal", "C) Nigeria", "D) Côte d'Ivoire"],
    "answer": "C",
    "explanation": "Le Nigeria est le pays le plus peuplé d'Afrique et d'Afrique de l'Ouest (environ 220 millions d'hab.).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Sur quel continent se trouve le Sahara ?",
    "options": ["A) Asie", "B) Amérique du Sud", "C) Afrique", "D) Australie"],
    "answer": "C",
    "explanation": "Le Sahara, plus grand désert chaud du monde, se trouve en Afrique du Nord.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la monnaie officielle du Ghana ?",
    "options": ["A) Franc CFA", "B) Cedi", "C) Naira", "D) Dalasi"],
    "answer": "B",
    "explanation": "La monnaie du Ghana est le Cedi (GHS).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays d'Afrique partage ses frontières avec la Côte d'Ivoire au nord ?",
    "options": ["A) Le Ghana", "B) La Guinée", "C) Le Burkina Faso", "D) Le Mali"],
    "answer": "C",
    "explanation": "Le Burkina Faso est au nord de la Côte d'Ivoire. Le Mali est aussi voisin au nord-ouest.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de la Guinée ?",
    "options": ["A) Conakry", "B) Bissau", "C) Freetown", "D) Monrovia"],
    "answer": "A",
    "explanation": "Conakry est la capitale de la République de Guinée.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel prix a reçu Nelson Mandela en 1993 ?",
    "options": ["A) Prix Nobel de la Paix", "B) Prix Nobel de Littérature", "C) Prix Nobel d'Économie", "D) Prix Pulitzer"],
    "answer": "A",
    "explanation": "Nelson Mandela a reçu le Prix Nobel de la Paix en 1993, partagé avec F. W. de Klerk.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la principale source d'énergie de la Côte d'Ivoire ?",
    "options": ["A) L'énergie nucléaire", "B) Le pétrole", "C) L'hydroélectricité et le gaz", "D) Le charbon"],
    "answer": "C",
    "explanation": "La CI tire l'essentiel de son énergie de l'hydroélectricité (Taabo, Kossou) et du gaz naturel.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a inventé le téléphone ?",
    "options": ["A) Thomas Edison", "B) Alexander Graham Bell", "C) Nikola Tesla", "D) James Watt"],
    "answer": "B",
    "explanation": "Alexander Graham Bell est généralement crédité de l'invention du téléphone (1876).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le nom de la lagune sur laquelle se trouve Abidjan ?",
    "options": ["A) Lagune Ébrié", "B) Lagune de Grand-Lahou", "C) Lagune Ouladine", "D) Lagune de Fresco"],
    "answer": "A",
    "explanation": "Abidjan est construite autour de la lagune Ébrié.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel philosophe a énoncé « Je pense donc je suis » ?",
    "options": ["A) Kant", "B) Descartes", "C) Locke", "D) Hegel"],
    "answer": "B",
    "explanation": "René Descartes a formulé « Cogito ergo sum » (Je pense donc je suis) dans ses Méditations.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le plus grand océan du monde ?",
    "options": ["A) Atlantique", "B) Indien", "C) Arctique", "D) Pacifique"],
    "answer": "D",
    "explanation": "L'océan Pacifique est le plus grand et le plus profond des océans.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année a eu lieu la Conférence de Berlin qui a partagé l'Afrique ?",
    "options": ["A) 1878", "B) 1884-1885", "C) 1900", "D) 1910"],
    "answer": "B",
    "explanation": "La Conférence de Berlin (1884-1885) a organisé le partage colonial de l'Afrique entre puissances européennes.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le plus grand désert froid du monde ?",
    "options": ["A) Sahara", "B) Gobi", "C) Antarctique", "D) Atacama"],
    "answer": "C",
    "explanation": "L'Antarctique est le plus grand désert (froid) du monde avec 14,2 millions de km².",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays d'Afrique possède la plus grande économie ?",
    "options": ["A) Afrique du Sud", "B) Égypte", "C) Nigeria", "D) Kenya"],
    "answer": "C",
    "explanation": "Le Nigeria est la première économie africaine en termes de PIB nominal.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le nom du port autonome d'Abidjan ?",
    "options": ["A) Port de San Pedro", "B) Port Bouët", "C) Port Autonome d'Abidjan (PAA)", "D) Port de Vridi"],
    "answer": "C",
    "explanation": "Le Port Autonome d'Abidjan (PAA) est le premier port d'Afrique de l'Ouest.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est l'arbre emblématique des savanes africaines ?",
    "options": ["A) Baobab", "B) Iroko", "C) Palmier", "D) Acacia"],
    "answer": "A",
    "explanation": "Le baobab est l'arbre emblématique des savanes et régions semi-arides d'Afrique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Où se situe la basilique Notre-Dame de la Paix de Yamoussoukro ?",
    "options": ["A) Abidjan", "B) Bouaké", "C) Yamoussoukro", "D) Daloa"],
    "answer": "C",
    "explanation": "La basilique Notre-Dame de la Paix, la plus grande basilique au monde, est à Yamoussoukro.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le nom du premier chef de gouvernement ivoirien (Premier ministre) après 1990 ?",
    "options": ["A) Alassane Ouattara", "B) Laurent Gbagbo", "C) Henri Konan Bédié", "D) Daniel Kablan Duncan"],
    "answer": "A",
    "explanation": "Alassane Ouattara a été le premier Premier ministre de Côte d'Ivoire (1990-1993) sous Houphouët-Boigny.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année la Côte d'Ivoire a-t-elle accueilli le Sommet Afrique-France ?",
    "options": ["A) 1999", "B) 2014", "C) 2021", "D) 1982"],
    "answer": "B",
    "explanation": "Le sommet Afrique-France s'est tenu à Paris en 2014. Abidjan a accueilli ce sommet en 2008.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le principal produit agricole d'exportation de la Côte d'Ivoire ?",
    "options": ["A) Café", "B) Coton", "C) Cacao", "D) Anacarde"],
    "answer": "C",
    "explanation": "La Côte d'Ivoire est le premier producteur mondial de cacao (environ 40% de la production mondiale).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle rivière délimite en partie la frontière entre la Côte d'Ivoire et le Ghana ?",
    "options": ["A) Le Sassandra", "B) Le Bandama", "C) La Bia/Comoé", "D) Le Cavally"],
    "answer": "C",
    "explanation": "Le fleuve Comoé/Bia forme en partie la frontière entre la Côte d'Ivoire et le Ghana.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est l'animal emblème de la Côte d'Ivoire ?",
    "options": ["A) Le lion", "B) L'éléphant", "C) Le guépard", "D) La panthère"],
    "answer": "B",
    "explanation": "L'éléphant est l'animal emblème de la Côte d'Ivoire, d'où le nom « Les Éléphants » pour l'équipe nationale de football.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel scientifique a établi la théorie de la relativité générale ?",
    "options": ["A) Isaac Newton", "B) Albert Einstein", "C) Niels Bohr", "D) Max Planck"],
    "answer": "B",
    "explanation": "Albert Einstein a publié la théorie de la relativité générale en 1915.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est l'hymne national de la Côte d'Ivoire ?",
    "options": ["A) Abidjanaise", "B) L'Abidjanaise", "C) Côte d'Ivoire", "D) La terre de l'espérance"],
    "answer": "B",
    "explanation": "L'hymne national de la Côte d'Ivoire est « L'Abidjanaise ».",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année a eu lieu la découverte de l'Amérique par Christophe Colomb ?",
    "options": ["A) 1492", "B) 1498", "C) 1504", "D) 1488"],
    "answer": "A",
    "explanation": "Christophe Colomb a atteint les Bahamas le 12 octobre 1492.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le nom de la communauté villageoise traditionnelle en Côte d'Ivoire ?",
    "options": ["A) Le kpando", "B) Le village", "C) La chefferie", "D) Le dozo"],
    "answer": "C",
    "explanation": "La chefferie traditionnelle est l'unité de base de l'organisation sociale en Côte d'Ivoire.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la surface totale de la Côte d'Ivoire ?",
    "options": ["A) 222 000 km²", "B) 322 463 km²", "C) 150 000 km²", "D) 410 000 km²"],
    "answer": "B",
    "explanation": "La Côte d'Ivoire couvre environ 322 463 km².",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le nom du Président du Liberia qui a reçu le Prix Nobel de la Paix en 2011 ?",
    "options": ["A) Charles Taylor", "B) Ellen Johnson Sirleaf", "C) George Weah", "D) Samuel Doe"],
    "answer": "B",
    "explanation": "Ellen Johnson Sirleaf, première femme présidente africaine, a reçu le Prix Nobel de la Paix en 2011.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quel pays se trouve le mont Olympe, montagne sacrée des dieux grecs ?",
    "options": ["A) Turquie", "B) Albanie", "C) Grèce", "D) Macédoine du Nord"],
    "answer": "C",
    "explanation": "Le mont Olympe (2917 m), le plus haut sommet de Grèce, était la demeure des dieux dans la mythologie grecque.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le nom de l'aéroport international de la ville d'Abidjan ?",
    "options": ["A) Aéroport de Port-Bouët", "B) Aéroport Félix Houphouët-Boigny", "C) Aéroport d'Abidjan-Plateau", "D) Aéroport de Cocody"],
    "answer": "B",
    "explanation": "L'aéroport international d'Abidjan porte le nom de Félix Houphouët-Boigny.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la superficie totale de la Côte d'Ivoire ?",
    "options": ["A) 322 462 km²", "B) 322 463 km²", "C) 324 462 km²", "D) 324 463 km²"],
    "answer": "B",
    "explanation": "La superficie de la Côte d'Ivoire est exactement de 322 463 km².",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui fut le premier explorateur français à signer des traités avec les chefs côtiers en Côte d'Ivoire en 1843 ?",
    "options": ["A) Louis-Gustave Binger", "B) Marcel Treich-Laplène", "C) Arthur Verdier", "D) Louis-Édouard Bouët-Willaumez"],
    "answer": "D",
    "explanation": "L'Amiral Bouët-Willaumez a signé les premiers traités de protectorat sur la côte en 1843.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année la Côte d'Ivoire est-elle devenue une colonie française autonome ?",
    "options": ["A) 1889", "B) 1893", "C) 1904", "D) 1946"],
    "answer": "B",
    "explanation": "La Côte d'Ivoire est érigée en colonie française le 10 mars 1893 avec Binger comme premier gouverneur.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le point culminant de la Côte d'Ivoire ?",
    "options": ["A) Mont Tonkoui", "B) Mont Nimba", "C) Mont Momi", "D) Mont Zo"],
    "answer": "B",
    "explanation": "Le Mont Nimba, situé à la frontière avec la Guinée, est le point culminant à 1752 m.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Lequel de ces fleuves ivoiriens est le plus long ?",
    "options": ["A) Le Cavally", "B) Le Sassandra", "C) Le Bandama", "D) La Comoé"],
    "answer": "C",
    "explanation": "Le Bandama, coulant entièrement sur le territoire ivoirien, est considéré comme le plus long fleuve du pays (environ 1050 km).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle ville est reconnue comme la capitale économique de la Côte d'Ivoire ?",
    "options": ["A) Yamoussoukro", "B) Bouaké", "C) San-Pédro", "D) Abidjan"],
    "answer": "D",
    "explanation": "Abidjan est la capitale économique, bien que Yamoussoukro soit la capitale politique depuis 1983.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a composé l'Abidjanaise, l'hymne national de la Côte d'Ivoire ?",
    "options": ["A) Pierre-Michel Pango", "B) Mathieu Ekra", "C) Joachim Bony", "D) L'Abbé Pierre-Michel Pango et le révérend père Michel Coty"],
    "answer": "D",
    "explanation": "L'hymne a été composé par l'Abbé Pierre-Michel Pango (musique) et l'Abbé Michel Coty, avec des paroles co-écrites par Mathieu Ekra, Joachim Bony.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la devise de la Côte d'Ivoire ?",
    "options": ["A) Union, Discipline, Travail", "B) Fraternité, Travail, Progrès", "C) Paix, Travail, Patrie", "D) Union, Travail, Justice"],
    "answer": "A",
    "explanation": "La devise officielle de la République de Côte d'Ivoire est 'Union, Discipline, Travail'.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année Félix Houphouët-Boigny est-il décédé ?",
    "options": ["A) 1990", "B) 1993", "C) 1995", "D) 1999"],
    "answer": "B",
    "explanation": "Félix Houphouët-Boigny, le premier président de la Côte d'Ivoire, est décédé le 7 décembre 1993.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel traité de 1919 a redéfini les frontières de la Côte d'Ivoire en créant la Haute-Volta ?",
    "options": ["A) Décret du 1er mars 1919", "B) Traité de Versailles", "C) Accords de Brazzaville", "D) Conférence de Berlin"],
    "answer": "A",
    "explanation": "Le décret de 1919 a séparé des territoires de la Côte d'Ivoire et du Haut-Sénégal-Niger pour créer la colonie de la Haute-Volta.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel sommet ivoirien culmine à 1752 m ?",
    "options": ["A) Mont Tonkoui", "B) Mont Nimba", "C) Mont Momi", "D) Mont Zo"],
    "answer": "B",
    "explanation": "Le Mont Nimba est le point culminant du pays.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel fleuve naît exclusivement en CI ?",
    "options": ["A) Cavally", "B) Bandama", "C) Comoé", "D) Sassandra"],
    "answer": "B",
    "explanation": "Le Bandama prend sa source au nord de la CI.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Yamoussoukro est devenue capitale en :",
    "options": ["A) 1983", "B) 1990", "C) 1978", "D) 1980"],
    "answer": "A",
    "explanation": "Loi du 21 mars 1983.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Plus grande forêt d'Abidjan ?",
    "options": ["A) Banco", "B) Azagny", "C) Taï", "D) Sangoué"],
    "answer": "A",
    "explanation": "Parc National du Banco.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Groupe ethnique Gour inclut :",
    "options": ["A) Baoulé", "B) Sénoufo", "C) Dan", "D) Bété"],
    "answer": "B",
    "explanation": "Les Sénoufo font partie du groupe Gour.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Ville non chef-lieu de district autonome ?",
    "options": ["A) San Pédro", "B) Korhogo", "C) Man", "D) Bouaflé"],
    "answer": "D",
    "explanation": "Bouaflé est chef-lieu de région (Marahoué) mais pas de district autonome.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Explorateur ayant signé traités en 1887 ?",
    "options": ["A) Binger", "B) Verdier", "C) Treich-Laplène", "D) Caillié"],
    "answer": "C",
    "explanation": "Marcel Treich-Laplène.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Inauguration canal de Vridi ?",
    "options": ["A) 1950", "B) 1960", "C) 1934", "D) 1948"],
    "answer": "A",
    "explanation": "Ouvert en 1950.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Premier PM en 1990 ?",
    "options": ["A) Bédié", "B) Ouattara", "C) Duncan", "D) Diarra"],
    "answer": "B",
    "explanation": "Alassane Ouattara fut nommé PM en 1990.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Objectif majeur PND 2021-2025 ?",
    "options": ["A) Écologie", "B) Transformation par industrialisation", "C) Autosuffisance", "D) Dette 0"],
    "answer": "B",
    "explanation": "Transformation structurelle par l'industrialisation.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Gisement gazier majeur 2021 ?",
    "options": ["A) Baleine", "B) Espoir", "C) Baobab", "D) Bélier"],
    "answer": "A",
    "explanation": "Gisement Baleine.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Successeur de Binger (1896) ?",
    "options": ["A) Clozel", "B) Mouttet", "C) Roberdeau", "D) Angoulvant"],
    "answer": "B",
    "explanation": "Eugène Mouttet.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Réserve de faune d'Abokouamékro dans quelle région ?",
    "options": ["A) Bélier", "B) Gbêkê", "C) Agnéby", "D) Iffou"],
    "answer": "A",
    "explanation": "Région du Bélier, près de Yamoussoukro.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Part de la CI en prod mondiale de cajou (2023) ?",
    "options": ["A) 15%", "B) 25%", "C) 40%", "D) 60%"],
    "answer": "C",
    "explanation": "Environ 40%, 1er producteur mondial.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Fondateur royaume Sanwi ?",
    "options": ["A) Amon N'Douffou Ier", "B) Aka Essoh", "C) Mian Amou", "D) Amalaman Anoh"],
    "answer": "D",
    "explanation": "Amalaman Anoh (XVIIIe).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Ethnie du groupe Krou ?",
    "options": ["A) Abouré", "B) Dida", "C) Gouro", "D) Lobi"],
    "answer": "B",
    "explanation": "Les Dida.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Miracle ivoirien ?",
    "options": ["A) 1950-1960", "B) 1960-1980", "C) 1980-1990", "D) 1990-2000"],
    "answer": "B",
    "explanation": "Période de forte croissance 1960-1980.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Barrage inauguré en 2017 ?",
    "options": ["A) Kossou", "B) Soubré", "C) Taabo", "D) Buyo"],
    "answer": "B",
    "explanation": "Barrage de Soubré.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Origine du nom 'Côte d'Ivoire' ?",
    "options": ["A) Mammouths", "B) Commerce ivoire", "C) Binger", "D) Tribu Ivori"],
    "answer": "B",
    "explanation": "Nommé par les marins pour le commerce de l'ivoire.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Colonie rattachée à la CI en 1932 ?",
    "options": ["A) Soudan", "B) Haute-Volta", "C) Guinée", "D) Dahomey"],
    "answer": "B",
    "explanation": "Haute-Volta (jusqu'en 1947).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Nombre de parcs nationaux en CI ?",
    "options": ["A) 5", "B) 8", "C) 12", "D) 15"],
    "answer": "B",
    "explanation": "8 Parcs Nationaux.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "San Pédro 1er port mondial pour :",
    "options": ["A) Café", "B) Cacao", "C) Bois", "D) Hévéa"],
    "answer": "B",
    "explanation": "Exportation de fèves de cacao.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Ville ivoirienne UNESCO (2012) ?",
    "options": ["A) Abidjan", "B) Yamoussoukro", "C) Grand-Bassam", "D) Kong"],
    "answer": "C",
    "explanation": "Ville historique de Grand-Bassam.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Fondateur royaume de Bouna ?",
    "options": ["A) Bounkani", "B) Samory", "C) Tutu", "D) Pokou"],
    "answer": "A",
    "explanation": "Roi Bounkani.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Création du PDCI ?",
    "options": ["A) 1944", "B) 1946", "C) 1958", "D) 1960"],
    "answer": "B",
    "explanation": "9 avril 1946.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Loi Houphouët (abolition travail forcé) ?",
    "options": ["A) 1944", "B) 1946", "C) 1950", "D) 1956"],
    "answer": "B",
    "explanation": "11 avril 1946.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Consécration Basilique ND de la Paix ?",
    "options": ["A) 1989", "B) 1990", "C) 1992", "D) 1994"],
    "answer": "B",
    "explanation": "Septembre 1990 par Jean-Paul II.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Plus long fleuve s'écoulant entièrement en CI ?",
    "options": ["A) Bandama", "B) Comoé", "C) Sassandra", "D) Cavally"],
    "answer": "A",
    "explanation": "Le Bandama (1050 km).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Part investissements privé dans PND 2021-2025 ?",
    "options": ["A) 50%", "B) 60%", "C) 74%", "D) 85%"],
    "answer": "C",
    "explanation": "74% du financement attendu.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Altitude Mont Tonkoui ?",
    "options": ["A) 1073 m", "B) 1189 m", "C) 1223 m", "D) 1752 m"],
    "answer": "B",
    "explanation": "Environ 1189 m.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Jour de l'indépendance CI ?",
    "options": ["A) 7 Août", "B) 4 Décembre", "C) 15 Août", "D) 1er Juillet"],
    "answer": "A",
    "explanation": "7 août 1960.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Premier chef du Conseil de gouvernement (1958) ?",
    "options": ["A) Denise", "B) Houphouët", "C) Mockey", "D) Coulibaly"],
    "answer": "A",
    "explanation": "Auguste Denise.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Fête du nouvel an Nzima ?",
    "options": ["A) Dipri", "B) Abissa", "C) Popo", "D) Goly"],
    "answer": "B",
    "explanation": "Fête de l'Abissa.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Prix Ahmadou Kourouma 2021 ?",
    "options": ["A) Tadjo", "B) Gauz", "C) Abouet", "D) Diallo"],
    "answer": "B",
    "explanation": "Armand Gauz.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Accord de paix 2007 ?",
    "options": ["A) Marcoussis", "B) Pretoria", "C) Ouagadougou", "D) Accra"],
    "answer": "C",
    "explanation": "Accord de Ouagadougou.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Promulgation Constitution 3e République ?",
    "options": ["A) 8 Nov 2016", "B) 30 Oct 2016", "C) 1 Aou 2000", "D) 15 Mai 2020"],
    "answer": "A",
    "explanation": "8 novembre 2016.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Plus grand lac artificiel de CI ?",
    "options": ["A) Kossou", "B) Soubré", "C) Buyo", "D) Taabo"],
    "answer": "A",
    "explanation": "Lac de Kossou.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Signification BNETD ?",
    "options": ["A) Bureau National d'Études Techniques et de Développement", "B) Bureau National de l'Économie...", "C) Base Nationale...", "D) Bureau National d'Équipement..."],
    "answer": "A",
    "explanation": "Bureau National d'Études Techniques et de Développement.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Mont Nimba classé UNESCO en :",
    "options": ["A) 1981", "B) 1990", "C) 2001", "D) 1974"],
    "answer": "A",
    "explanation": "Inscrit en 1981/1982.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Stade finale CAN 2023 ?",
    "options": ["A) 2021", "B) 2023", "C) 2019", "D) 2025"],
    "answer": "B",
    "explanation": "La question était sur l'année de la CAN (2023).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Gouverneur 'pacification' (1908-1916) ?",
    "options": ["A) Angoulvant", "B) Binger", "C) Ponty", "D) Eboué"],
    "answer": "A",
    "explanation": "Gabriel Angoulvant.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Hymne de la CI ?",
    "options": ["A) L'Abidjanaise", "B) La Concorde", "C) Le Ditanyè", "D) La Renaissance"],
    "answer": "A",
    "explanation": "L'Abidjanaise.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Chef-lieu du Gôh ?",
    "options": ["A) Daloa", "B) Gagnoa", "C) Soubré", "D) Issia"],
    "answer": "B",
    "explanation": "Gagnoa.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Mosquées inscrites à l'UNESCO (2021) ?",
    "options": ["A) Kong", "B) Style soudanais du nord", "C) Samatiguila", "D) Mankono"],
    "answer": "B",
    "explanation": "Ensemble de 8 mosquées de style soudanais.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Communes du Grand Abidjan ?",
    "options": ["A) 10", "B) 13", "C) 14", "D) 15"],
    "answer": "B",
    "explanation": "13 entités communales (10 urbaines + 3 sous-préfectures).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Création de la RTI ?",
    "options": ["A) 1960", "B) 1963", "C) 1970", "D) 1973"],
    "answer": "B",
    "explanation": "1963.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Zone forestière actuelle CI estimée à :",
    "options": ["A) <3M ha", "B) 8M ha", "C) 12M ha", "D) 16M ha"],
    "answer": "A",
    "explanation": "Moins de 3 millions d'hectares.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Port historiquement bois ?",
    "options": ["A) Abidjan", "B) San Pédro", "C) Sassandra", "D) Tabou"],
    "answer": "B",
    "explanation": "San Pédro a été créé pour le bois.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Ethnie Lobi connue pour :",
    "options": ["A) Zaouli", "B) Soukalas", "C) Poids à or", "D) Kita"],
    "answer": "B",
    "explanation": "Habitats fortifiés en banco appelés soukalas.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Monnaie précoloniale Akan ?",
    "options": ["A) Cauri", "B) Manille", "C) Sel", "D) Poudre d'or"],
    "answer": "D",
    "explanation": "La poudre d'or et les poids à peser.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Lequel de ces pays est actuellement dirigé par une femme ?",
    "options": ["A) Libéria", "B) Sierra Léone", "C) Tanzanie", "D) Éthiopie"],
    "answer": "C",
    "explanation": "La Tanzanie est dirigée par Samia Suluhu Hassan.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle école Aristote a-t-il créée ?",
    "options": ["A) Le Jardin des Plantes", "B) L'Académie", "C) Le Lycée", "D) L’Université d’Athènes"],
    "answer": "C",
    "explanation": "Aristote a fondé le Lycée à Athènes.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui fut le premier Directeur Général de l'ENA-CI ?",
    "options": ["A) Laurent Dona Fologo", "B) Ropion Robert", "C) Zadi Zaourou", "D) Alassane Ouattara"],
    "answer": "B",
    "explanation": "Ropion Robert a été le premier DG de l'ENA.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel acte a permis l’indépendance du Soudan du Sud en 2011 ?",
    "options": ["A) L’Accord de paix global", "B) Les Accords de Naivasha", "C) Les Accords de Khartoum", "D) Le Référendum d’autodétermination"],
    "answer": "D",
    "explanation": "C'est le référendum d'autodétermination de 2011 qui a conduit à l'indépendance.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Un savoir ésotérique est un savoir :",
    "options": ["A) Populaire et accessible", "B) Réservé à un cercle initié", "C) Pratique", "D) Public"],
    "answer": "B",
    "explanation": "L'ésotérisme désigne un enseignement réservé à des initiés.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de la Tanzanie ?",
    "options": ["A) Freetown", "B) Banjul", "C) Bissau", "D) Dodoma"],
    "answer": "D",
    "explanation": "Dodoma est la capitale politique de la Tanzanie.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Les députés ivoiriens sont :",
    "options": ["A) Nommés", "B) Élus", "C) Élus pour certains, nommés pour d’autres", "D) Nommés par le président"],
    "answer": "B",
    "explanation": "Les députés de l'Assemblée nationale sont élus au suffrage universel direct.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Lequel de ces personnalités n’a jamais été président de l’Assemblée Nationale ?",
    "options": ["A) Henri Konan Bédié", "B) Mamadou Koulibaly", "C) Soro Guillaume", "D) Kandia Camara"],
    "answer": "D",
    "explanation": "Kandia Camara a été présidente du Sénat, mais pas de l'Assemblée nationale.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En CI, le président de la République est membre du gouvernement.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Le Président de la République n'est pas formellement membre du gouvernement, bien qu'il le préside.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "L’Assemblée Nationale ivoirienne comprend désormais des sénateurs :",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "L'Assemblée Nationale et le Sénat sont deux chambres distinctes du Parlement.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année le Printemps arabe a-t-il débuté ?",
    "options": ["A) 2008", "B) 2012", "C) 2010", "D) 2005"],
    "answer": "C",
    "explanation": "Le Printemps arabe a commencé fin 2010 en Tunisie.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année le FEMUA a-t-il débuté ?",
    "options": ["A) 2006", "B) 2008", "C) 2009", "D) 2010"],
    "answer": "B",
    "explanation": "Le FEMUA a été lancé en 2008.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l’actuel Directeur Général de la Fonction Publique ivoirienne ?",
    "options": ["A) Aka Kacou", "B) Yéo Nahoua", "C) Kouakou Edouard", "D) SORO Gninagafol"],
    "answer": "D",
    "explanation": "Soro Gninagafol a été nommé DG de la Fonction Publique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année Yamoussoukro devint-elle la capitale politique ivoirienne ?",
    "options": ["A) 1980", "B) 1983", "C) 1990", "D) 1995"],
    "answer": "B",
    "explanation": "Le transfert de la capitale à Yamoussoukro a été décidé en 1983.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l'actuel Premier ministre du Canada ?",
    "options": ["A) Justin Trudeau", "B) Chrystia Freeland", "C) Jagmeet Singh", "D) Mark Carney"],
    "answer": "A",
    "explanation": "Justin Trudeau est le Premier ministre du Canada.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le rang de la Côte d’Ivoire dans le classement mondial des producteurs de café ?",
    "options": ["A) 3e", "B) 5e", "C) 14e", "D) 15e"],
    "answer": "C",
    "explanation": "La Côte d'Ivoire se situe autour du 14e rang mondial.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle science étudie les insectes ?",
    "options": ["A) Ornithologie", "B) Mycologie", "C) Entomologie", "D) Arachnologie"],
    "answer": "C",
    "explanation": "L'entomologie est la science qui étudie les insectes.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle femme a été la première à arbitrer un match de football professionnel ?",
    "options": ["A) Wendie Renard", "B) Stéphanie Frappart", "C) Bibiana Steinhaus", "D) Salima Mukansanga"],
    "answer": "C",
    "explanation": "Bibiana Steinhaus a été la première femme à arbitrer un match masculin de haut niveau.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année les accords de Bretton Woods ont-ils été signés ?",
    "options": ["A) 1940", "B) 1944", "C) 1945", "D) 1939"],
    "answer": "B",
    "explanation": "Les accords de Bretton Woods ont été signés en 1944.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l'actuel président du Conseil constitutionnel ivoirien ?",
    "options": ["A) Mamadou Koné", "B) Chantal Nanaba Camara", "C) Francis Wodié", "D) Tia Koné"],
    "answer": "B",
    "explanation": "Chantal Nanaba Camara a été nommée présidente du Conseil constitutionnel.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel peintre espagnol est connu pour avoir cofondé le cubisme ?",
    "options": ["A) Salvador Dalí", "B) Pablo Picasso", "C) Juan Gris"],
    "answer": "B",
    "explanation": "Pablo Picasso est l'un des fondateurs du cubisme.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a été couronné empereur français le 2 décembre 1804 ?",
    "options": ["A) Napoléon Bonaparte", "B) Charlemagne", "C) Louis XIV"],
    "answer": "A",
    "explanation": "Napoléon Bonaparte a été sacré empereur en 1804.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le nom de la science qui étudie les fossiles ?",
    "options": ["A) Paléontologie", "B) Botanique", "C) Archéologie"],
    "answer": "A",
    "explanation": "La paléontologie est l'étude des fossiles.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l’actuel Secrétaire Général de l’ENA ?",
    "options": ["A) Narcisse Sepy Yessoh", "B) Koné Aline", "C) François Kouma"],
    "answer": "A",
    "explanation": "Narcisse Sepy Yessoh est le SG actuel de l'ENA.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de pattes possède une araignée ?",
    "options": ["A) 6", "B) 8", "C) 12"],
    "answer": "B",
    "explanation": "Les araignées sont des arachnides et possèdent 8 pattes.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel gaz représente environ 78 % de l’atmosphère terrestre ?",
    "options": ["A) L’oxygène", "B) Le carbone", "C) Le diazote", "D) L'argon"],
    "answer": "C",
    "explanation": "Le diazote constitue 78% de l'atmosphère.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Le Pakistan a pour capitale :",
    "options": ["A) Kuala Lumpur", "B) Bangkok", "C) Islamabad", "D) Kaboul"],
    "answer": "C",
    "explanation": "Islamabad est la capitale du Pakistan.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel éminent diplomate et Ministre des Affaires Etrangères de Cote d’Ivoire a tiré sa révérence le 8 avril 2025 ?",
    "options": ["A) Essy Amara", "B) Charles Koffi Diby", "C) Siméon Aké"],
    "answer": "A",
    "explanation": "Essy Amara est un diplomate ivoirien.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle maison a pour emblème un loup dans la série Game of Thrones ?",
    "options": ["A) La maison Stark", "B) La maison Baratheon", "C) La maison Lannister"],
    "answer": "A",
    "explanation": "L'emblème de la Maison Stark est un loup-garou.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a écrit « Les bouts de bois de Dieu » ?",
    "options": ["A) Aimé Césaire", "B) Sembene Ousmane", "C) Soro Guéfala"],
    "answer": "B",
    "explanation": "Ousmane Sembène a écrit Les Bouts de bois de Dieu.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle planète est surnommée « l’étoile du berger » ?",
    "options": ["A) Mars", "B) Terre", "C) Vénus"],
    "answer": "C",
    "explanation": "Vénus est souvent appelée l'étoile du berger.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel personnage mythologique a été condamné à pousser éternellement un rocher en haut d’une montagne ?",
    "options": ["A) Sisyphe", "B) Prométhée", "C) Tantale"],
    "answer": "A",
    "explanation": "C'est le mythe de Sisyphe.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel traité a mis fin à la première guerre mondiale en 1919 ?",
    "options": ["A) Le traité de Versailles", "B) Les accords d’Evian", "C) Le traité de Rome"],
    "answer": "A",
    "explanation": "Le Traité de Versailles a mis fin à la Première Guerre mondiale.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui était le président américain pendant la seconde guerre mondiale ?",
    "options": ["A) Richard Nixon", "B) Delano Roosevelt", "C) John Kennedy"],
    "answer": "B",
    "explanation": "Franklin Delano Roosevelt était président pendant la majeure partie de la guerre.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est le plus médaillé aux Jeux Olympiques ?",
    "options": ["A) Usain Bolt", "B) Michael Phelps", "C) Larissa Latynina", "D) Mark Spitz"],
    "answer": "B",
    "explanation": "Michael Phelps détient le record du nombre de médailles olympiques.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel stade a accueilli la confrontation entre la Cote d’Ivoire et le Sénégal lors des huitièmes de finale de la 34e édition de la CAN ?",
    "options": ["A) Le Stade Laurent Pokou", "B) Le Stade de la paix", "C) Le Stade Charles Konan Banny"],
    "answer": "C",
    "explanation": "Le match a eu lieu au stade Charles Konan Banny de Yamoussoukro.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien d’Océans il y a-t-il ?",
    "options": ["A) 4", "B) 5", "C) 6"],
    "answer": "B",
    "explanation": "Il y a 5 océans : Atlantique, Pacifique, Indien, Arctique, Antarctique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le nom à l’état civil de l’artiste zouglou Pat Sacko ?",
    "options": ["A) Hughes-Patrick Ossohou", "B) Blaise-Patrick Daté", "C) Patrick Yao"],
    "answer": "A",
    "explanation": "Son nom à l'état civil est Ossohou Patrick.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le chef-lieu de la région de l’Agnéby -Tiassa ?",
    "options": ["A) Dabou", "B) Adzopé", "C) Agboville"],
    "answer": "C",
    "explanation": "Agboville est le chef-lieu de l'Agnéby-Tiassa.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle mer sépare l’Europe de l’Afrique ?",
    "options": ["A) Mer Rouge", "B) Mer Noire", "C) Mer Méditerranée"],
    "answer": "C",
    "explanation": "La mer Méditerranée sépare l'Europe de l'Afrique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le seul continent à ne pas avoir de pays ?",
    "options": ["A) Océanie", "B) Arctique", "C) Antarctique"],
    "answer": "C",
    "explanation": "L'Antarctique ne compte aucun pays.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de la Turquie ?",
    "options": ["A) Istanbul", "B) Ankara", "C) Izmir", "D) Antalya"],
    "answer": "B",
    "explanation": "Ankara est la capitale de la Turquie.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "A quelles dates se sont déroulées la 3e édition des Journées Portes Ouvertes de l’ENA ?",
    "options": ["A) Du 25 au 26 février 2025", "B) Du 13 au 15 février 2025", "C) Du 23 au 24 février 2025"],
    "answer": "B",
    "explanation": "C'est généralement autour de ces dates.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la nouvelle dénomination de l’ENA France ?",
    "options": ["A) INSP", "B) ENAMF", "C) APF", "D) ENA-Paris"],
    "answer": "A",
    "explanation": "L'École nationale d'administration a été remplacée par l'Institut national du service public (INSP).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année a eu lieu la prise de la Bastille ?",
    "options": ["A) 1789", "B) 1791", "C) 1793"],
    "answer": "A",
    "explanation": "La prise de la Bastille a eu lieu en 1789.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de langues officielles compte l’Union Européenne ?",
    "options": ["A) 20", "B) 24", "C) 3"],
    "answer": "B",
    "explanation": "L'UE compte 24 langues officielles.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le pourcentage de suffrages obtenu par Brice Clotaire Oligui N’Guema selon les résultats provisoires de l'élection présidentielle d'avril 2025 au Gabon ?",
    "options": ["A) 87,50 %", "B) 90,35 %", "C) 94,85 %", "D) 98,85 %"],
    "answer": "B",
    "explanation": "Selon les résultats provisoires annoncés le 13 avril 2025 par le ministère de l'Intérieur, Brice Clotaire Oligui N'Guema a obtenu 90,35 % des voix (proclamation définitive le 25 avril 2025 à 94,85 % par la Cour constitutionnelle).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l’actuel secrétaire général de la francophonie ?",
    "options": ["A) Louise Mushikiwabo", "B) Michael Jean", "C) Abdou Diouf"],
    "answer": "A",
    "explanation": "Louise Mushikiwabo est l'actuelle Secrétaire générale.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Où a eu lieu la COP 29 ?",
    "options": ["A) Bakou", "B) Paris", "C) Belém"],
    "answer": "A",
    "explanation": "La COP 29 a eu lieu à Bakou, en Azerbaïdjan.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Sous quel thème est placé le FEMUA 18 ?",
    "options": ["A) La santé mentale", "B) Intelligence artificielle : menace ou opportunité pour l'Afrique ?", "C) Civisme et sécurité Routière"],
    "answer": "B",
    "explanation": "L'IA est le thème du FEMUA 18.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année furent signés les accords de Maastricht ?",
    "options": ["A) 1962", "B) 1981", "C) 1992"],
    "answer": "C",
    "explanation": "Le traité de Maastricht a été signé en 1992.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la monnaie utilisée en Russie ?",
    "options": ["A) l’euro", "B) le rouble", "C) l’hryvnia"],
    "answer": "B",
    "explanation": "Le rouble est la monnaie russe.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "A combien est estimée la population ivoirienne à l’issu du dernier recensement général de la population et de l’habitat ?",
    "options": ["A) 29 389 150 hbts", "B) 32 167 255 hbts", "C) autre"],
    "answer": "A",
    "explanation": "La population est estimée à environ 29,4 millions d'habitants.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Comment appelle-t-on les habitants de Gaza ?",
    "options": ["A) Les Gazaouis", "B) Les Gazavites", "C) Les Gazawites"],
    "answer": "A",
    "explanation": "Les habitants de Gaza sont les Gazaouis.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En mathématiques, quelle est la valeur arrondie de pi ?",
    "options": ["A) 3,14028", "B) 3,14159", "C) 3,14217"],
    "answer": "B",
    "explanation": "La valeur de Pi commence par 3,14159.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la langue principale parlée en Iran ?",
    "options": ["A) Persan", "B) Kurde", "C) Iranien"],
    "answer": "A",
    "explanation": "Le persan est la langue officielle de l'Iran.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le seul pays au monde à posséder une capitale qui commence par la lettre Z ?",
    "options": ["A) Suisse", "B) Croatie", "C) Ouganda"],
    "answer": "B",
    "explanation": "Zagreb est la capitale de la Croatie.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel verbe est utilisé pour désigner le cri des dauphins ?",
    "options": ["A) Gazouiller", "B) Glapir", "C) Siffler"],
    "answer": "C",
    "explanation": "Les dauphins sifflent.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est le coréalisateur du film Marabout chéri au côté de Luis Marquès ?",
    "options": ["A) Cheick Yvhane", "B) Michel Bohiri", "C) Kadhy Touré"],
    "answer": "C",
    "explanation": "Kadhy Touré est co-réalisatrice de Marabout Chéri.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "“Je punirai les serviteurs, les fils et leurs pères” est une :",
    "options": ["A) Méthaphore", "B) Allégorie", "C) Gradation"],
    "answer": "C",
    "explanation": "Il s'agit d'une gradation.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui détient le record du monde du 100 m masculin ?",
    "options": ["A) Usain Bolt", "B) Noah Lyles", "C) Justin Gatlin", "D) Asafa Powell"],
    "answer": "A",
    "explanation": "Usain Bolt détient le record du monde du 100 m.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est considéré comme le meilleur joueur de basketball de tous les temps ?",
    "options": ["A) Lebron James", "B) Michael Jordan", "C) Kobe Bryant"],
    "answer": "B",
    "explanation": "Michael Jordan est généralement considéré comme le meilleur joueur de basketball.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a été le premier pays à remporter la coupe du monde de football ?",
    "options": ["A) Urugay", "B) Grande Bretagne", "C) Italie"],
    "answer": "A",
    "explanation": "L'Uruguay a remporté la première Coupe du monde en 1930.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a remporté le ballon d’or France football en 2022 ?",
    "options": ["A) Lionnel Messi", "B) Karim Benzema", "C) Luka Modric"],
    "answer": "B",
    "explanation": "Karim Benzema a remporté le Ballon d'or 2022.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel boxeur nommé « the greatest » est considéré comme l’un des plus grands boxeurs de tous les temps ?",
    "options": ["A) Floyd Mayweather Jr", "B) Mike Tyson", "C) Mohamed Ali"],
    "answer": "C",
    "explanation": "Mohamed Ali était surnommé The Greatest.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est le joueur de tennis espagnol qui est considéré comme l’un des meilleurs joueurs sur terre battue de tous les temps ?",
    "options": ["A) Rafael Nadal", "B) Carlos Alcaraz", "C) Manuel Alonzo"],
    "answer": "A",
    "explanation": "Rafael Nadal est le roi de la terre battue.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est le joueur de golf américain qui est considéré comme l’un des plus grands golfeurs de tous les temps ?",
    "options": ["A) Jack Nicklaus", "B) Tiger Woods", "C) Arnold Palmer"],
    "answer": "B",
    "explanation": "Tiger Woods est l'un des plus grands golfeurs.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est le premier joueur ivoirien à avoir marqué en finale d’une CAN ?",
    "options": ["A) Laurent Pokou", "B) Didier Drogba", "C) Franck Kessié"],
    "answer": "A",
    "explanation": "Laurent Pokou.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de buts ont été marqués à la Coupe d’Afrique des Nations 2023 organisé en Côte d’ivoire ?",
    "options": ["A) 109 buts", "B) 119 buts", "C) 135 buts"],
    "answer": "B",
    "explanation": "119 buts ont été marqués lors de la CAN 2023.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est le meilleur buteur de l’histoire de la CAN ?",
    "options": ["A) Didier Drogba", "B) Roger Mila", "C) Samuel Eto’o"],
    "answer": "C",
    "explanation": "Samuel Eto'o est le meilleur buteur de l'histoire de la CAN avec 18 buts.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Lors du tour de France, qui est récompensé d’un maillot blanc à pois rouges ?",
    "options": ["A) Le meilleur grimpeur", "B) Le meilleur coureur", "C) Le meilleur cycliste"],
    "answer": "A",
    "explanation": "Le maillot à pois récompense le meilleur grimpeur.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Où se dérouleront les prochains jeux olympiques ?",
    "options": ["A) Paris", "B) Mexico", "C) Los Angeles"],
    "answer": "C",
    "explanation": "Les prochains Jeux Olympiques d'été après 2024 auront lieu à Los Angeles en 2028.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Depuis quelle année le badminton est devenu une discipline olympique ?",
    "options": ["A) 1992", "B) 2010", "C) 2023"],
    "answer": "A",
    "explanation": "Le badminton est sport olympique depuis 1992.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Les IXème jeux de la francophonie se sont déroulés du ……. Au ……….. 2023 à Kinshasa :",
    "options": ["A) Du 28 juillet au 6 aout", "B) Du 28 février au 7 mars 2023", "C) Du 28 juin au 6 juillet"],
    "answer": "A",
    "explanation": "Les Jeux de la Francophonie 2023 se sont tenus fin juillet - début août.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Comment appelle-t-on le tournoi de tennis joué à Paris ?",
    "options": ["A) Roland-Garros", "B) Wimbledon", "C) Us Open"],
    "answer": "A",
    "explanation": "Le tournoi de Paris est Roland-Garros.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a remporté le ballon d’or africain quatre fois consécutives ?",
    "options": ["A) Georges Weah", "B) Yaya Touré", "C) Samuel Eto’o"],
    "answer": "B",
    "explanation": "Yaya Touré a gagné le Ballon d'Or africain quatre fois de suite (2011-2014).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a été le meilleur buteur de la coupe du monde 2014 ?",
    "options": ["A) James Rodriguez", "B) Thomas Muller", "C) Lionnel Messi"],
    "answer": "A",
    "explanation": "James Rodriguez a été le meilleur buteur (6 buts).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est le dernier vainqueur français de Roland Garros ?",
    "options": ["A) Tsonga", "B) Monfils", "C) Noah"],
    "answer": "C",
    "explanation": "Yannick Noah en 1983.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quel pays est né le judo ?",
    "options": ["A) Chine", "B) Japon", "C) Vietnam", "D) Corée du Sud"],
    "answer": "B",
    "explanation": "Le judo a été créé au Japon par Jigoro Kano.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays a remporté la Coupe du Monde FIFA 2022 ?",
    "options": ["A) France", "B) Brésil", "C) Argentine", "D) Allemagne"],
    "answer": "C",
    "explanation": "L'Argentine a remporté la Coupe du Monde 2022.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle ville a accueilli les Jeux Olympiques d’été 2024 ?",
    "options": ["A) Tokyo", "B) Paris", "C) Los Angelès", "D) Londres"],
    "answer": "B",
    "explanation": "Paris a accueilli les JO en 2024.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de joueurs composent une équipe de basketball sur le terrain ?",
    "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
    "answer": "B",
    "explanation": "Il y a 5 joueurs par équipe sur le terrain.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quel sport évolue Novak Djokovic ?",
    "options": ["A) Golf", "B) Tennis", "C) Handball", "D) Boxe"],
    "answer": "B",
    "explanation": "Djokovic est un joueur de tennis.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays domine historiquement les Jeux Olympiques d’hiver ?",
    "options": ["A) Norvège", "B) Canada", "C) Russie", "D) USA"],
    "answer": "A",
    "explanation": "La Norvège est le pays le plus titré aux JO d'hiver.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a remporté le Ballon d’Or 2020 ?",
    "options": ["A) Erling Halland", "B) Lionnel Messi", "C) Cristiano R", "D) Modric"],
    "answer": "B",
    "explanation": "Le Ballon d'Or 2020 n'a pas été attribué. Il s'agit peut-être d'une erreur dans les options. En l'absence de meilleur choix, on retient Messi.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de sets gagnants faut-il pour remporter un match masculin en Grand Chelem ?",
    "options": ["A) 2", "B) 3", "C) 4", "D) 5"],
    "answer": "B",
    "explanation": "Il faut 3 sets gagnants pour remporter un match masculin en Grand Chelem.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel sport utilise les termes “birdie” et “eagle” ?",
    "options": ["A) Tennis", "B) Golf", "C) Badminton", "D) Baseball"],
    "answer": "B",
    "explanation": "Ce sont des termes de golf.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle nation a remporté la CAN 2023 (jouée en 2024) ?",
    "options": ["A) Sénégal", "B) Maroc", "C) Côte d’Ivoire", "D) Nigéria"],
    "answer": "C",
    "explanation": "La Côte d'Ivoire a remporté la CAN 2023.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de kilomètres mesure un marathon ?",
    "options": ["A) 40", "B) 41", "C) 41, 195", "D) 43 km"],
    "answer": "C",
    "explanation": "Un marathon mesure 42,195 km, l'option C (bien que 41,195 y soit écrite) est l'option la plus proche visée ou une coquille du document original.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quel sport retrouve-t-on la NBA ?",
    "options": ["A) Hockey", "B) Baseball", "C) Football", "D) Basketball"],
    "answer": "D",
    "explanation": "La NBA est la ligue américaine de basketball.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel joueur est associé au club d’Al Nassr depuis 2023 ?",
    "options": ["A) Neymar", "B) Benzema", "C) Cristiano R", "D) Messi"],
    "answer": "C",
    "explanation": "Cristiano Ronaldo joue pour Al Nassr.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays a organisé la Coupe du Monde 2022 ?",
    "options": ["A) Qatar", "B) Russie", "C) France", "D) Mexique"],
    "answer": "A",
    "explanation": "Le Qatar a organisé la Coupe du monde 2022.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En rugby, combien de points vaut un essai ?",
    "options": ["A) 3", "B) 5", "C) 6", "D) 7"],
    "answer": "B",
    "explanation": "Un essai au rugby vaut 5 points.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel club est le plus titré en Ligue des Champions CAF ?",
    "options": ["A) Al ahly sc", "B) TP Mazembe", "C) Zamalek", "D) Pyramids fc"],
    "answer": "A",
    "explanation": "Al Ahly SC est le club le plus titré.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quel sport évolue Francis Ngannou ?",
    "options": ["A) Boxe MMA", "B) Football", "C) Athlétisme", "D) Lutte"],
    "answer": "A",
    "explanation": "Francis Ngannou évolue en MMA et Boxe.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la nature du pouvoir exécutif ivoirien ?",
    "options": ["A) Monocéphale", "B) Bicéphale", "C) Tricéphale"],
    "answer": "B",
    "explanation": "Le pouvoir exécutif ivoirien est bicéphale (Président et Premier Ministre).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est le Vice-président de la République de Côte d’Ivoire ?",
    "options": ["A) Tiemoko Meyliet Koné", "B) Yua Koffi", "C) Beugré Mambé"],
    "answer": "A",
    "explanation": "Tiémoko Meyliet Koné est le Vice-président.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Le médiateur de la République est nommé pour ?",
    "options": ["A) 4 ans", "B) 5 ans", "C) 6 ans"],
    "answer": "C",
    "explanation": "Le Médiateur de la République est nommé pour un mandat de 6 ans non renouvelable.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l’actuel médiateur de la République de Côte d’Ivoire ?",
    "options": ["A) Adama Toungara", "B) Eugène Aka Aouelé", "C) Gaoussou Touré"],
    "answer": "A",
    "explanation": "Adama Toungara est le Médiateur de la République.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année a été nommé le Haut représentant du Président de la république ?",
    "options": ["A) 2024", "B) 2023", "C) 2022"],
    "answer": "B",
    "explanation": "Le Haut représentant a été nommé en 2023.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Le parlement ivoirien est ?",
    "options": ["A) Monocamérale", "B) Bicamérale", "C) aucune réponse n’est correcte"],
    "answer": "B",
    "explanation": "Le parlement ivoirien est bicaméral (Assemblée nationale et Sénat).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a été le premier président du Sénat ivoirien ?",
    "options": ["A) Kandia Camara", "B) Jeannot Ahoussou Kouadio", "C) Dagri Diabaté"],
    "answer": "B",
    "explanation": "Jeannot Ahoussou-Kouadio fut le premier président du Sénat.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Comment s’appelle l’actuel président du Conseil Constitutionnel ivoirien ?",
    "options": ["A) Chantal Naneba Camara", "B) Chantal Nanaba Camara", "C) Chantal Massereba Camara"],
    "answer": "B",
    "explanation": "Chantal Nanaba Camara est la présidente du Conseil constitutionnel.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Le président du Conseil Régional est élu pour ?",
    "options": ["A) 6 ans", "B) 5 ans", "C) 4 ans"],
    "answer": "B",
    "explanation": "Il est élu pour 5 ans.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est le ministre de la fonction publique et de la modernisation de l’administration ?",
    "options": ["A) Mathieu Ekra", "B) Ally Coulibaly", "C) Anne Ouloto"],
    "answer": "C",
    "explanation": "Anne Ouloto est la ministre de la fonction publique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "L’ordre juridictionnel ivoirien est ?",
    "options": ["A) Moniste", "B) Dualiste", "C) Atypique"],
    "answer": "B",
    "explanation": "L'ordre est dualiste, avec un ordre judiciaire et un ordre administratif.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est le président du Conseil d’Etat ivoirien ?",
    "options": ["A) Patrice Yao Kouakou", "B) Yua Koffi", "C) Lamine Ouattara"],
    "answer": "A",
    "explanation": "Patrice Yao Kouakou préside le Conseil d'Etat.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est le président de la Cour de Cassation ivoirienne ?",
    "options": ["A) Yua Koffi", "B) Patrice Yao Kouakou", "C) Théophile Ahoua N’dol"],
    "answer": "A",
    "explanation": "Yua Koffi préside la Cour de Cassation.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est le président de la Haute Autorité à la Bonne gouvernance ?",
    "options": ["A) Mamadou Sangafowa", "B) Epiphane Zoro BI", "C) Patrick Achi"],
    "answer": "B",
    "explanation": "Epiphane Zoro BI Ballo est le président de la HABG.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Le général Apalo Touré est issu de ?",
    "options": ["A) La Police", "B) L’armée de l’air", "C) La Gendarmerie"],
    "answer": "C",
    "explanation": "Alexandre Apalo Touré est Commandant Supérieur de la Gendarmerie.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la dénomination exacte du Ministère de l’éducation ?",
    "options": ["A) Ministère d’Etat, Ministère de l’Education Nationale et de l’Alphabétisation", "B) Ministère de l’Education Nationale, de l’Alphabétisation et de l’Enseignement technique", "C) Ministère de l’Education Nationale et de l’Enseignement Supérieur"],
    "answer": "A",
    "explanation": "C'est le Ministère de l'Éducation Nationale et de l'Alphabétisation.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Kanvaly Diomandé est le président de laquelle de ces institutions ?",
    "options": ["A) Commission Electorale Indépendante", "B) Cour des Comptes", "C) Grande Chancellerie de l’ordre national"],
    "answer": "B",
    "explanation": "Kanvaly Diomandé est président de la Cour des Comptes.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est le président de la Chambre des Rois et chefs traditionnels de Cote d’ivoire ?",
    "options": ["A) Sa majesté Nanan Desire Amon-Tanoe", "B) Sa majesté Nanan Desire Amoi-Tano", "C) Sa majesté Nanan Desire Amani-Tanoe"],
    "answer": "A",
    "explanation": "Nanan Amon Tanoé Désiré préside la Chambre.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Parmi ces personnalités, laquelle n’a jamais été président de l’Assemblée Nationale en CI ?",
    "options": ["A) Mamadou Koulibaly", "B) Soro Guillaume", "C) Coulibaly Kuibiert"],
    "answer": "C",
    "explanation": "Coulibaly Kuibiert est président de la CEI, non de l'Assemblée Nationale.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de femmes ministres compte l’actuel gouvernement ivoirien ?",
    "options": ["A) 7", "B) 8", "C) 10"],
    "answer": "A",
    "explanation": "Le gouvernement compte plusieurs femmes ministres (autour de 6-7).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la plus haute juridiction de l’ordre judiciaire ?",
    "options": ["A) Cour d’appel", "B) TPI", "C) Cour suprême", "D) Conseil d’État"],
    "answer": "C",
    "explanation": "La Cour de Cassation (anciennement chambre judiciaire de la Cour Suprême).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle juridiction est compétente en matière administrative ?",
    "options": ["A) Cour de cassation", "B) Conseil d’État", "C) Tribunal pénal"],
    "answer": "B",
    "explanation": "Le Conseil d'État est la plus haute juridiction en matière administrative.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle juridiction juge les crimes les plus graves ?",
    "options": ["A) Tribunal correctionnel", "B) Cour d’assises", "C) Tribunal administratif"],
    "answer": "B",
    "explanation": "La Cour d'assises juge les crimes.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Les collectivités territoriales comprennent :",
    "options": ["A) États fédérés", "B) Régions, districts, communes", "C) Régions, départements, villages"],
    "answer": "B",
    "explanation": "En Côte d'Ivoire, ce sont principalement les communes, régions et districts autonomes.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l’actuel Ministre de l’urbanisme, du logement et du cadre de vie ?",
    "options": ["A) Bruno N. Koné", "B) Moussa Sanogo", "C) Mariatou Koné"],
    "answer": "A",
    "explanation": "Bruno Nabagné Koné occupe ce poste.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a été le premier Directeur Général de l'ENA-CI ?",
    "options": ["A) Félix Houphouët-Boigny", "B) Robert Ropion", "C) Alassane Ouattara", "D) Jeannot Ahoussou Kouadio"],
    "answer": "B",
    "explanation": "Robert Ropion fut le premier DG de l'ENA-CI.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Depuis quelle année Yamoussoukro est-elle la capitale politique de la Côte d'Ivoire ?",
    "options": ["A) 1960", "B) 1983", "C) 1990", "D) 1993"],
    "answer": "B",
    "explanation": "Yamoussoukro est la capitale politique depuis 1983.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "De quelles chambres est composé le parlement bicaméral ivoirien ?",
    "options": ["A) Assemblée Nationale et Conseil Constitutionnel", "B) Sénat et Conseil Économique et Social", "C) Assemblée Nationale et Sénat", "D) Chambre des Députés et Sénat"],
    "answer": "C",
    "explanation": "Le parlement est composé de l'Assemblée Nationale et du Sénat.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui occupe le poste de Vice-Président de la République de Côte d'Ivoire selon les notes ?",
    "options": ["A) Daniel Kablan Duncan", "B) Tiemoko Meyliet Koné", "C) Patrick Achi", "D) Robert Beugré Mambé"],
    "answer": "B",
    "explanation": "Le VP actuel de la République est Tiemoko Meyliet Koné.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la juridiction administrative suprême en Côte d'Ivoire ?",
    "options": ["A) La Cour Suprême", "B) La Cour de Cassation", "C) Le Conseil d'État", "D) Le Conseil Constitutionnel"],
    "answer": "C",
    "explanation": "Le Conseil d'État est la juridiction administrative suprême.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle juridiction judiciaire est considérée comme suprême ?",
    "options": ["A) Le Conseil d'État", "B) La Cour d'Appel", "C) La Cour d'assises", "D) La Cour de Cassation"],
    "answer": "D",
    "explanation": "La Cour de Cassation est la juridiction judiciaire suprême.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Comment qualifie-t-on l'ordre juridictionnel ivoirien ?",
    "options": ["A) Moniste", "B) Unifié", "C) Dualiste", "D) Mixte"],
    "answer": "C",
    "explanation": "L'ordre juridictionnel ivoirien est dualiste.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui préside le Conseil Constitutionnel ivoirien ?",
    "options": ["A) Mamadou Koné", "B) Chantal Nanaba Camara", "C) Tiemoko Meyliet Koné", "D) René Degni-Ségui"],
    "answer": "B",
    "explanation": "Chantal Nanaba Camara est présidente du Conseil Constitutionnel.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Par quelle cour sont jugés les crimes graves ?",
    "options": ["A) Le Tribunal de Première Instance", "B) La Cour de Cassation", "C) La Cour d'assises", "D) Le Conseil d'État"],
    "answer": "C",
    "explanation": "Les crimes graves sont jugés par la Cour d'assises.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année eut lieu la prise de la Bastille ?",
    "options": ["A) 1789", "B) 1792", "C) 1804", "D) 1799"],
    "answer": "A",
    "explanation": "La prise de la Bastille date de 1789.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "À quelle date Napoléon a-t-il été couronné ?",
    "options": ["A) 14 juillet 1789", "B) 2 décembre 1804", "C) 18 juin 1815", "D) 2 décembre 1851"],
    "answer": "B",
    "explanation": "Napoléon a été couronné le 2 décembre 1804.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quand le Traité de Versailles a-t-il été signé ?",
    "options": ["A) 1914", "B) 1918", "C) 1919", "D) 1945"],
    "answer": "C",
    "explanation": "Le Traité de Versailles date de 1919.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année le Soudan du Sud a-t-il obtenu son indépendance ?",
    "options": ["A) 2010", "B) 2011", "C) 2012", "D) 2013"],
    "answer": "B",
    "explanation": "Le Soudan du Sud est devenu indépendant en 2011 suite à un référendum.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle ville organise les Jeux Olympiques en 2024 ?",
    "options": ["A) Londres", "B) Los Angeles", "C) Paris", "D) Tokyo"],
    "answer": "C",
    "explanation": "Les JO de 2024 se déroulent à Paris.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale du Pakistan ?",
    "options": ["A) Karachi", "B) Lahore", "C) Islamabad", "D) Kaboul"],
    "answer": "C",
    "explanation": "La capitale du Pakistan est Islamabad.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la monnaie de la Russie ?",
    "options": ["A) Le rouble", "B) L'euro", "C) Le dinar", "D) Le peso"],
    "answer": "A",
    "explanation": "La monnaie de la Russie est le rouble.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l'actuelle Secrétaire Générale de la Francophonie ?",
    "options": ["A) Michaëlle Jean", "B) Louise Mushikiwabo", "C) Aminata Touré", "D) Nkosazana Dlamini-Zuma"],
    "answer": "B",
    "explanation": "Louise Mushikiwabo est la SG de la Francophonie.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Où s'est déroulée la CAN 2023 ?",
    "options": ["A) Cameroun", "B) Sénégal", "C) Côte d'Ivoire", "D) Maroc"],
    "answer": "C",
    "explanation": "La CAN 2023 a été organisée en Côte d'Ivoire.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle célèbre école a été créée par Aristote ?",
    "options": ["A) L'Académie", "B) Le Lycée", "C) La Sorbonne", "D) Le Portique"],
    "answer": "B",
    "explanation": "Aristote a créé Le Lycée.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Que l'entomologie étudie-t-elle ?",
    "options": ["A) Les mots", "B) Les champignons", "C) Les insectes", "D) Les fossiles"],
    "answer": "C",
    "explanation": "L'entomologie est l'étude des insectes.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle science a pour objet l'étude des fossiles ?",
    "options": ["A) La paléontologie", "B) L'archéologie", "C) L'entomologie", "D) La géologie"],
    "answer": "A",
    "explanation": "La paléontologie étudie les fossiles.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la proportion approximative de diazote dans l'atmosphère ?",
    "options": ["A) 21%", "B) 50%", "C) 78%", "D) 90%"],
    "answer": "C",
    "explanation": "Le diazote compose environ 78% de l'atmosphère.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel mouvement artistique Pablo Picasso a-t-il cofondé ?",
    "options": ["A) L'impressionnisme", "B) Le surréalisme", "C) Le cubisme", "D) Le fauvisme"],
    "answer": "C",
    "explanation": "Pablo Picasso est le cofondateur du cubisme.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l'auteur de l'œuvre 'Les bouts de bois de Dieu' ?",
    "options": ["A) Ahmadou Kourouma", "B) Léopold Sédar Senghor", "C) Sembène Ousmane", "D) Camara Laye"],
    "answer": "C",
    "explanation": "Sembène Ousmane a écrit 'Les bouts de bois de Dieu'.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans la mythologie grecque, qui a été condamné à pousser éternellement un rocher ?",
    "options": ["A) Atlas", "B) Prométhée", "C) Sisyphe", "D) Tantale"],
    "answer": "C",
    "explanation": "C'est Sisyphe qui fut condamné à pousser un rocher.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est la première femme à avoir arbitré un match de football professionnel masculin ?",
    "options": ["A) Bibiana Steinhaus", "B) Stéphanie Frappart", "C) Salima Mukansanga", "D) Yoshimi Yamashita"],
    "answer": "B",
    "explanation": "Stéphanie Frappart est la première femme à arbitrer du foot pro masculin.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel athlète détient le record du 100m masculin ?",
    "options": ["A) Tyson Gay", "B) Yohan Blake", "C) Asafa Powell", "D) Usain Bolt"],
    "answer": "D",
    "explanation": "Usain Bolt détient le record du 100m masculin.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la distance exacte du marathon ?",
    "options": ["A) 41,195 km", "B) 42,195 km", "C) 42,000 km", "D) 43,195 km"],
    "answer": "B",
    "explanation": "La distance officielle d'un marathon est de 42,195 km.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Que récompense le maillot blanc à pois rouges sur le Tour de France ?",
    "options": ["A) Le meilleur jeune", "B) Le meilleur sprinteur", "C) Le meilleur grimpeur", "D) Le vainqueur du classement général"],
    "answer": "C",
    "explanation": "Il récompense le meilleur grimpeur.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays a été le premier champion du monde de football ?",
    "options": ["A) L'Italie", "B) Le Brésil", "C) L'Argentine", "D) L'Uruguay"],
    "answer": "D",
    "explanation": "L'Uruguay a remporté la première coupe du monde.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays a remporté la Coupe du Monde de football 2022 au Qatar ?",
    "options": ["A) La France", "B) L'Argentine", "C) Le Brésil", "D) L'Espagne"],
    "answer": "B",
    "explanation": "L'Argentine a gagné la Coupe du Monde 2022.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "De quel pays est originaire le judo ?",
    "options": ["A) Chine", "B) Corée du Sud", "C) Japon", "D) Thaïlande"],
    "answer": "C",
    "explanation": "Le judo est d'origine japonaise.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Sur quelle surface se joue le tournoi de Roland-Garros ?",
    "options": ["A) Gazon", "B) Dur", "C) Terre battue", "D) Moquette"],
    "answer": "C",
    "explanation": "Roland-Garros se joue sur terre battue à Paris.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de joueurs par équipe y a-t-il sur un terrain de basketball ?",
    "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
    "answer": "B",
    "explanation": "Le basketball se joue à 5 joueurs par équipe.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de points vaut un essai au rugby ?",
    "options": ["A) 3 points", "B) 4 points", "C) 5 points", "D) 7 points"],
    "answer": "C",
    "explanation": "Un essai vaut 5 points au rugby.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel sportif est le plus médaillé de l'histoire des Jeux Olympiques ?",
    "options": ["A) Usain Bolt", "B) Carl Lewis", "C) Michael Phelps", "D) Mark Spitz"],
    "answer": "C",
    "explanation": "Michael Phelps est le sportif le plus médaillé aux JO.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale politique de la CI ?",
    "options": ["A) Abidjan", "B) Bouaké", "C) Yamoussoukro", "D) Korhogo"],
    "answer": "C",
    "explanation": "Yamoussoukro est la capitale politique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Où s'est tenu le référendum d'indépendance de 2011 ?",
    "options": ["A) Erythrée", "B) Timor oriental", "C) Soudan du Sud", "D) Kosovo"],
    "answer": "C",
    "explanation": "Indépendance du Soudan du Sud en 2011 par référendum.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Le mouvement 'Printemps arabe' a commencé en...",
    "options": ["A) 2008", "B) 2010", "C) 2011", "D) 2012"],
    "answer": "B",
    "explanation": "Débuté en 2010.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel évènement sportif majeur se tiendra à Paris en 2024 ?",
    "options": ["A) La Coupe du monde de Rugby", "B) Les Jeux Olympiques", "C) L'Euro de football", "D) Le championnat du monde d'athlétisme"],
    "answer": "B",
    "explanation": "Paris accueille les JO 2024.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a été le premier Directeur Général de l'ENA de Côte d'Ivoire ?",
    "options": ["A) Félix Houphouët-Boigny", "B) Robert Ropion", "C) Charles Konan Banny", "D) Alassane Ouattara"],
    "answer": "B",
    "explanation": "Robert Ropion a été le premier DG de l'École Nationale d'Administration de Côte d'Ivoire à sa création en 1960.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année Yamoussoukro est-elle devenue la capitale politique de la Côte d'Ivoire ?",
    "options": ["A) 1960", "B) 1983", "C) 1990", "D) 1993"],
    "answer": "B",
    "explanation": "Le transfert de la capitale politique et administrative à Yamoussoukro a été acté par la loi de mars 1983.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l'actuel Vice-Président de la République de Côte d'Ivoire (en 2026/2027) ?",
    "options": ["A) Daniel Kablan Duncan", "B) Amadou Gon Coulibaly", "C) Tiemoko Meyliet Koné", "D) Patrick Achi"],
    "answer": "C",
    "explanation": "Tiemoko Meyliet Koné, ancien gouverneur de la BCEAO, occupe ce poste depuis avril 2022.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Laquelle de ces institutions est à la tête de l'ordre juridictionnel administratif en Côte d'Ivoire, instaurant ainsi le dualisme juridictionnel ?",
    "options": ["A) La Cour de Cassation", "B) Le Conseil Constitutionnel", "C) Le Conseil d'État", "D) La Cour des Comptes"],
    "answer": "C",
    "explanation": "La réforme constitutionnelle a éclaté l'ancienne Cour Suprême. Le Conseil d'État gère le volet administratif, la Cour de Cassation le judiciaire.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a été nommée Présidente du Conseil Constitutionnel de Côte d'Ivoire en 2023 ?",
    "options": ["A) Henriette Diabaté", "B) Kandia Camara", "C) Chantal Nanaba Camara", "D) Simone Gbagbo"],
    "answer": "C",
    "explanation": "Chantal Nanaba Camara est la première femme à présider cette haute institution, nommée par Alassane Ouattara en 2023.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pays a remporté la Coupe d'Afrique des Nations (CAN) 2023 organisée en début 2024 ?",
    "options": ["A) Nigeria", "B) Sénégal", "C) Côte d'Ivoire", "D) Maroc"],
    "answer": "C",
    "explanation": "La Côte d'Ivoire (le pays hôte) a remporté la compétition en battant le Nigeria 2-1 en finale.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Lequel de ces joueurs ivoiriens a marqué l'un des buts lors de la finale de la CAN 2023 contre le Nigeria ?",
    "options": ["A) Didier Drogba", "B) Sébastien Haller", "C) Yaya Touré", "D) Wilfried Zaha"],
    "answer": "B",
    "explanation": "Sébastien Haller a marqué le but décisif de la victoire (2-1) en finale, après l'égalisation de Franck Kessié.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle ville a accueilli les Jeux Olympiques d'été en 2024 ?",
    "options": ["A) Los Angeles", "B) Londres", "C) Paris", "D) Tokyo"],
    "answer": "C",
    "explanation": "Les JO de 2024 se sont déroulés à Paris, en France.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans le sport du rugby (à XV), combien de points rapporte un essai marqué (avant transformation) ?",
    "options": ["A) 3 points", "B) 5 points", "C) 7 points", "D) 2 points"],
    "answer": "B",
    "explanation": "Un essai vaut 5 points, la transformation 2 points, le drop et la pénalité 3 points.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Le judo est un art martial originaire de quel pays ?",
    "options": ["A) Chine", "B) Corée du Sud", "C) Japon", "D) Thaïlande"],
    "answer": "C",
    "explanation": "Créé par Jigoro Kano en 1882 au Japon.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Le tournoi de tennis de Roland-Garros se joue sur quelle surface ?",
    "options": ["A) Gazon", "B) Terre battue", "C) Dur", "D) Moquette"],
    "answer": "B",
    "explanation": "Roland-Garros est le tournoi du Grand Chelem disputé sur terre battue à Paris.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "À quelle date Napoléon Bonaparte a-t-il été couronné Empereur des Français ?",
    "options": ["A) 14 juillet 1789", "B) 2 décembre 1804", "C) 18 juin 1815", "D) 9 novembre 1799"],
    "answer": "B",
    "explanation": "Le sacre a eu lieu le 2 décembre 1804 à Notre-Dame de Paris.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année se sont tenus les accords de Bretton Woods instituant le FMI et la Banque Mondiale ?",
    "options": ["A) 1919", "B) 1944", "C) 1945", "D) 1957"],
    "answer": "B",
    "explanation": "La conférence de Bretton Woods s'est tenue en juillet 1944 aux États-Unis.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la distance exacte du marathon en athlétisme ?",
    "options": ["A) 40,000 km", "B) 42,195 km", "C) 45,000 km", "D) 50,000 km"],
    "answer": "B",
    "explanation": "Distance fixée définitivement depuis les JO de Londres en 1908.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le gaz le plus abondant dans l'atmosphère terrestre ?",
    "options": ["A) Le dioxygène", "B) Le dioxyde de carbone", "C) Le diazote", "D) L'argon"],
    "answer": "C",
    "explanation": "Le diazote compose environ 78% de l'air que nous respirons.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel philosophe grec a fondé l'école appelée 'Le Lycée' ?",
    "options": ["A) Socrate", "B) Platon", "C) Aristote", "D) Épicure"],
    "answer": "C",
    "explanation": "Platon a fondé l'Académie, Aristote a fondé le Lycée (école péripatéticienne).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "De quel courant artistique Pablo Picasso est-il l'un des fondateurs ?",
    "options": ["A) L'impressionnisme", "B) Le surréalisme", "C) Le cubisme", "D) Le fauvisme"],
    "answer": "C",
    "explanation": "Avec Georges Braque, Picasso a été le pionnier du cubisme au début du XXe siècle (ex: Les Demoiselles d'Avignon).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans la mythologie grecque, qui fut condamné à pousser éternellement un lourd rocher au sommet d'une montagne ?",
    "options": ["A) Prométhée", "B) Atlas", "C) Sisyphe", "D) Hercule"],
    "answer": "C",
    "explanation": "Le châtiment de Sisyphe symbolise le travail absurde et sans fin.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale de la région de l'Agnéby-Tiassa en Côte d'Ivoire ?",
    "options": ["A) Divo", "B) Agboville", "C) Adzopé", "D) Sikensi"],
    "answer": "B",
    "explanation": "La région de l'Agnéby-Tiassa (sud de la CI) a pour chef-lieu la ville d'Agboville.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Le Parlement de la 3ème République ivoirienne est bicaméral. Il comprend l'Assemblée nationale et...",
    "options": ["A) Le Conseil Économique et Social", "B) Le Sénat", "C) Le Conseil Constitutionnel", "D) La Cour Suprême"],
    "answer": "B",
    "explanation": "La Constitution de 2016 a instauré un Sénat, rendant le parlement bicaméral.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a été le premier Président du Sénat de Côte d'Ivoire ?",
    "options": ["A) Amadou Soumahoro", "B) Adama Bictogo", "C) Jeannot Ahoussou Kouadio", "D) Charles Koffi Diby"],
    "answer": "C",
    "explanation": "Jeannot Ahoussou Kouadio a été élu premier président du Sénat ivoirien en 2018.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "L'élection présidentielle d'octobre 2025 en Côte d'Ivoire a été remportée, selon la CEI, par :",
    "options": ["A) Tidjane Thiam", "B) Jean-Louis Billon", "C) Alassane Ouattara", "D) Simone Gbagbo"],
    "answer": "C",
    "explanation": "Le président sortant, Alassane Ouattara (RHDP), a été réélu pour un quatrième mandat dès le premier tour avec environ 89,7% des suffrages.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En 2025, trois pays ouest-africains ont officialisé leur retrait de la CEDEAO pour former la Confédération des États du Sahel (AES). Lesquels ?",
    "options": ["A) Mali, Sénégal, Guinée", "B) Mali, Burkina Faso, Niger", "C) Burkina Faso, Togo, Bénin", "D) Niger, Tchad, Mauritanie"],
    "answer": "B",
    "explanation": "Le Mali, le Burkina Faso et le Niger ont quitté la CEDEAO en janvier 2025 et institutionnalisé l'AES.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a remporté le Prix Nobel de Littérature en 2024 ?",
    "options": ["A) Annie Ernaux", "B) Jon Fosse", "C) Han Kang", "D) Haruki Murakami"],
    "answer": "C",
    "explanation": "L'autrice sud-coréenne Han Kang a remporté le prix Nobel de littérature en 2024.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien d'États membres compte la CEDEAO depuis le retrait définitif des pays de l'AES en 2025 ?",
    "options": ["A) 15", "B) 12", "C) 10", "D) 14"],
    "answer": "B",
    "explanation": "Avec le retrait du Mali, du Burkina Faso et du Niger, la CEDEAO est passée de 15 à 12 membres actifs.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Lors des JO de Paris 2024, quel sportif détient encore historiquement le record absolu du nombre de médailles olympiques toutes éditions confondues ?",
    "options": ["A) Usain Bolt", "B) Michael Phelps", "C) Carl Lewis", "D) Léon Marchand"],
    "answer": "B",
    "explanation": "Le nageur américain Michael Phelps détient le record absolu avec 28 médailles, dont 23 en or.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Laquelle de ces institutions n'appartient pas au pouvoir judiciaire en Côte d'Ivoire ?",
    "options": ["A) La Cour de Cassation", "B) La Haute Cour de Justice", "C) La Cour des Comptes", "D) Le Conseil des Ministres"],
    "answer": "D",
    "explanation": "Le Conseil des ministres est l'organe du pouvoir exécutif. La Cour des Comptes appartient à l'ordre juridictionnel financier.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "L'athlète jamaïcain Usain Bolt est célèbre pour son record du monde sur 100m. Quel est son temps record ?",
    "options": ["A) 9,69 s", "B) 9,72 s", "C) 9,58 s", "D) 9,52 s"],
    "answer": "C",
    "explanation": "Il a établi le record de 9,58 s lors des championnats du monde d'athlétisme à Berlin en 2009.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Où se situe le siège de l'Union Économique et Monétaire Ouest-Africaine (UEMOA) ?",
    "options": ["A) Dakar", "B) Abidjan", "C) Lomé", "D) Ouagadougou"],
    "answer": "D",
    "explanation": "Le siège de la Commission de l'UEMOA est à Ouagadougou (Burkina Faso).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Où se trouve le siège de la BCEAO (Banque Centrale des États de l'Afrique de l'Ouest) ?",
    "options": ["A) Abidjan", "B) Dakar", "C) Lomé", "D) Niamey"],
    "answer": "B",
    "explanation": "Le siège de la BCEAO est situé à Dakar au Sénégal (bien que son gouverneur actuel, Jean-Claude Kassi Brou, soit de nationalité ivoirienne).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Lors de la CAN 2023, quelle équipe la Côte d'Ivoire a-t-elle éliminée en demi-finale ?",
    "options": ["A) Sénégal", "B) Mali", "C) RD Congo", "D) Guinée équatoriale"],
    "answer": "C",
    "explanation": "La Côte d'Ivoire a battu la RD Congo 1-0 en demi-finale, grâce à un but de Sébastien Haller.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En Côte d'Ivoire, l'Autorité Nationale de la Presse (ANP) remplace :",
    "options": ["A) Le CNP", "B) La HACA", "C) Le CICG", "D) Le Conseil d'État"],
    "answer": "A",
    "explanation": "L'ANP (Autorité Nationale de la Presse) a remplacé le Conseil National de la Presse (CNP) comme organe de régulation de la presse écrite.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Le 7 août 1960 marque pour la Côte d'Ivoire :",
    "options": ["A) La proclamation de la République", "B) L'indépendance", "C) L'adoption de l'hymne national", "D) Le transfert de la capitale"],
    "answer": "B",
    "explanation": "C'est la date officielle de l'accession de la Côte d'Ivoire à l'indépendance.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le nom de l'hymne national de la Côte d'Ivoire ?",
    "options": ["A) La Concorde", "B) L'Abidjanaise", "C) Le Ditanyè", "D) La Dessalinienne"],
    "answer": "B",
    "explanation": "L'Abidjanaise a été adoptée comme hymne national en 1960.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Laquelle de ces villes n'est pas un chef-lieu de district autonome en Côte d'Ivoire ?",
    "options": ["A) Abidjan", "B) Yamoussoukro", "C) San-Pédro", "D) Bocanda"],
    "answer": "D",
    "explanation": "Bocanda est un département situé dans la région du N'Zi, ce n'est pas un chef-lieu de district autonome (comme Abidjan, Yamoussoukro, etc.).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En août 2026, l'Alliance des États du Sahel (AES) a officiellement installé son Parlement confédéral dans quelle ville ?",
    "options": ["A) Bamako", "B) Ouagadougou", "C) Niamey", "D) Agadez"],
    "answer": "C",
    "explanation": "Le parlement confédéral de l'AES (45 députés) a été installé à Niamey au Niger fin août 2026.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En histoire, quel traité a mis fin à la Première Guerre mondiale en 1919 ?",
    "options": ["A) Le Traité de Vienne", "B) Le Traité de Versailles", "C) Le Traité de Rome", "D) Le Traité de Tordesillas"],
    "answer": "B",
    "explanation": "Signé le 28 juin 1919 dans la galerie des Glaces du château de Versailles.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a succédé à Henri Konan Bédié à la tête du PDCI-RDA après son décès ?",
    "options": ["A) Maurice Kakou Guikahué", "B) Tidjane Thiam", "C) Jean-Louis Billon", "D) Thierry Tanoh"],
    "answer": "B",
    "explanation": "Tidjane Thiam a été élu président du PDCI-RDA en décembre 2023.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel était le taux de participation officiel selon la CEI lors de l'élection présidentielle ivoirienne d'octobre 2025 ?",
    "options": ["A) Environ 35%", "B) Environ 50%", "C) Environ 75%", "D) Environ 90%"],
    "answer": "B",
    "explanation": "La CEI a enregistré un taux de participation d'environ 50,10 % lors de ce scrutin.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans le cadre de l'exécution du PND (Plan National de Développement), quelle est la période couverte par le dernier plan en cours avant 2026 ?",
    "options": ["A) 2012-2015", "B) 2016-2020", "C) 2021-2025", "D) 2025-2030"],
    "answer": "C",
    "explanation": "Le gouvernement ivoirien a exécuté le PND sur la période 2021-2025 visant la transformation structurelle de l'économie.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Lors de la phase de groupes de la CAN 2023, la Côte d'Ivoire a subi une lourde défaite (0-4) face à quelle équipe ?",
    "options": ["A) Le Nigeria", "B) La Guinée-Bissau", "C) La Guinée équatoriale", "D) Le Sénégal"],
    "answer": "C",
    "explanation": "Le 'Nzalang Nacional' de la Guinée équatoriale a battu les Éléphants 4 à 0 lors de leur 3e match de poule.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel fleuve ivoirien donne son nom à une région dont le chef-lieu est Sassandra ?",
    "options": ["A) Le Bandama", "B) Le Cavally", "C) Le Sassandra", "D) La Comoé"],
    "answer": "C",
    "explanation": "Le fleuve Sassandra traverse l'ouest du pays et se jette dans le golfe de Guinée au niveau de la ville de Sassandra (région du Gbôklè).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la devise de la République de Côte d'Ivoire ?",
    "options": ["A) Union - Travail - Justice", "B) Union - Discipline - Travail", "C) Paix - Travail - Patrie", "D) Fraternité - Travail - Progrès"],
    "answer": "B",
    "explanation": "C'est la devise officielle figurant sur les armoiries de la CI.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "La Basilique Notre-Dame de la Paix, l'édifice religieux chrétien le plus grand du monde, se trouve à :",
    "options": ["A) Abidjan", "B) Rome", "C) Yamoussoukro", "D) Korhogo"],
    "answer": "C",
    "explanation": "Construite sous la présidence de Félix Houphouët-Boigny, elle a été consacrée en 1990 par le Pape Jean-Paul II.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quel sport évolue l'athlète ivoirienne Marie-Josée Ta Lou-Smith ?",
    "options": ["A) Saut en longueur", "B) Taekwondo", "C) Sprint (Athlétisme)", "D) Natation"],
    "answer": "C",
    "explanation": "Elle est une sprinteuse spécialiste des 100m et 200m.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui fut le fondateur du célèbre empire de Kong au nord de la Côte d'Ivoire au XVIIIe siècle ?",
    "options": ["A) Samory Touré", "B) Sékou Ouattara", "C) Osei Tutu", "D) Abla Pokou"],
    "answer": "B",
    "explanation": "Sékou Ouattara a fondé l'Empire de Kong vers 1710.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "L'organisation sous-régionale CEDEAO a pour siège principal :",
    "options": ["A) Abidjan", "B) Dakar", "C) Abuja", "D) Accra"],
    "answer": "C",
    "explanation": "Le siège de la Commission de la CEDEAO se trouve à Abuja, la capitale du Nigeria.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans le contexte de la crise du Sahel, l'opération militaire française qui a pris fin en 2022 s'appelait :",
    "options": ["A) Serval", "B) Sangaris", "C) Barkhane", "D) Takuba"],
    "answer": "C",
    "explanation": "Lancée en 2014 pour succéder à Serval, Barkhane s'est achevée officiellement en novembre 2022 suite aux retraits successifs du Mali puis du Burkina.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est l'année de l'indépendance de la Côte d'Ivoire ?",
    "options": ["A) 1958", "B) 1960", "C) 1962", "D) 1964"],
    "answer": "B",
    "explanation": "La Côte d'Ivoire a obtenu son indépendance le 7 août 1960.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui fut le premier président de la Côte d'Ivoire ?",
    "options": ["A) Henri Konan Bédié", "B) Laurent Gbagbo", "C) Félix Houphouët-Boigny", "D) Alassane Ouattara"],
    "answer": "C",
    "explanation": "Félix Houphouët-Boigny fut le premier président du pays.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale politique de la Côte d'Ivoire ?",
    "options": ["A) Abidjan", "B) Bouaké", "C) Yamoussoukro", "D) San-Pédro"],
    "answer": "C",
    "explanation": "Yamoussoukro est la capitale politique de la CI depuis 1983.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quelle ville ivoirienne se trouve la basilique Notre-Dame de la Paix ?",
    "options": ["A) Abidjan", "B) Yamoussoukro", "C) Korhogo", "D) Man"],
    "answer": "B",
    "explanation": "La basilique est située à Yamoussoukro.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Comment s'appelle l'hymne national ivoirien ?",
    "options": ["A) L'Abidjanaise", "B) La Concorde", "C) Le Ditanyè", "D) L'Ivoirienne"],
    "answer": "A",
    "explanation": "L'hymne national est L'Abidjanaise.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel fleuve ivoirien donne son nom à un grand barrage hydroélectrique ?",
    "options": ["A) Sassandra", "B) Bandama", "C) Comoé", "D) Cavally"],
    "answer": "B",
    "explanation": "Le barrage de Kossou est sur le fleuve Bandama.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l'auteur du roman 'Les Soleils des indépendances' ?",
    "options": ["A) Bernard Dadié", "B) Ahmadou Kourouma", "C) Camara Laye", "D) Léopold Sédar Senghor"],
    "answer": "B",
    "explanation": "Ahmadou Kourouma a écrit ce célèbre roman.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la principale culture d'exportation de la Côte d'Ivoire ?",
    "options": ["A) Café", "B) Coton", "C) Cacao", "D) Anacarde"],
    "answer": "C",
    "explanation": "La CI est le premier producteur mondial de cacao.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de districts autonomes compte la Côte d'Ivoire ?",
    "options": ["A) 2", "B) 12", "C) 14", "D) 31"],
    "answer": "C",
    "explanation": "La CI compte 14 districts dont 2 autonomes (Abidjan et Yamoussoukro).",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel parc national ivoirien est célèbre pour ses chimpanzés et sa forêt primaire ?",
    "options": ["A) Parc national de Taï", "B) Parc national du Banco", "C) Parc national de la Comoé", "D) Réserve d'Abokouamékro"],
    "answer": "A",
    "explanation": "Le parc de Taï est classé au patrimoine mondial de l'UNESCO.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "De quelle région Daloa est-il le chef-lieu ?",
    "options": ["A) Haut-Sassandra", "B) Marahoué", "C) Gôh", "D) Tonkpi"],
    "answer": "A",
    "explanation": "Daloa est la capitale du Haut-Sassandra.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année a eu lieu le coup d'État de Robert Guéï ?",
    "options": ["A) 1993", "B) 1999", "C) 2002", "D) 2010"],
    "answer": "B",
    "explanation": "Le coup d'État a eu lieu le 24 décembre 1999.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le sommet le plus élevé de Côte d'Ivoire ?",
    "options": ["A) Mont Tonkoui", "B) Mont Nimba", "C) Mont Momi", "D) Mont Zo"],
    "answer": "B",
    "explanation": "Le Mont Nimba (1752m) est le point culminant.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quel district se trouve la ville de Korhogo ?",
    "options": ["A) District des Savanes", "B) District du Denguélé", "C) District du Woroba", "D) District de la Vallée du Bandama"],
    "answer": "A",
    "explanation": "Korhogo est le chef-lieu du district des Savanes.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel peuple célèbre la fête de l'Abissa ?",
    "options": ["A) Baoulé", "B) Bété", "C) Nzima", "D) Sénoufo"],
    "answer": "C",
    "explanation": "Les Nzima (Grand-Bassam) célèbrent l'Abissa.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l'actuel Premier ministre de Côte d'Ivoire (2024) ?",
    "options": ["A) Patrick Achi", "B) Robert Beugré Mambé", "C) Amadou Gon Coulibaly", "D) Hamed Bakayoko"],
    "answer": "B",
    "explanation": "Robert Beugré Mambé a été nommé en 2023.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle ville ivoirienne est surnommée 'La perle des lagunes' ?",
    "options": ["A) San-Pédro", "B) Grand-Bassam", "C) Abidjan", "D) Jacqueville"],
    "answer": "C",
    "explanation": "Abidjan est surnommée la perle des lagunes.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel instrument traditionnel est typique de la musique balafon ?",
    "options": ["A) Kora", "B) Balafon", "C) Tam-tam", "D) Djembe"],
    "answer": "B",
    "explanation": "Le balafon est un xylophone traditionnel d'Afrique de l'Ouest.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Laquelle de ces villes fut la première capitale de la Côte d'Ivoire coloniale ?",
    "options": ["A) Bingerville", "B) Grand-Bassam", "C) Abidjan", "D) Yamoussoukro"],
    "answer": "B",
    "explanation": "Grand-Bassam fut la première capitale de 1893 à 1896.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle ethnie appartient au groupe Akan ?",
    "options": ["A) Les Dan", "B) Les Baoulé", "C) Les Sénoufo", "D) Les Malinké"],
    "answer": "B",
    "explanation": "Les Baoulé font partie du groupe Akan.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel animal est l'emblème national de la Côte d'Ivoire ?",
    "options": ["A) L'aigle", "B) Le lion", "C) L'éléphant", "D) La panthère"],
    "answer": "C",
    "explanation": "L'éléphant est l'animal symbole du pays.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel port ivoirien est le premier port exportateur mondial de cacao ?",
    "options": ["A) Port d'Abidjan", "B) Port de San-Pédro", "C) Port de Sassandra", "D) Port de Tabou"],
    "answer": "B",
    "explanation": "San-Pédro est le premier port exportateur de cacao au monde.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a composé la musique de l'Abidjanaise ?",
    "options": ["A) Mathieu Ekra", "B) Pierre-Michel Pango", "C) Joachim Bony", "D) Bernard Dadié"],
    "answer": "B",
    "explanation": "L'Abbé Pierre-Michel Pango a composé la musique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel pont emblématique relie le Plateau à Treichville à Abidjan ?",
    "options": ["A) Pont Houphouët-Boigny", "B) Pont De Gaulle", "C) Pont HKB", "D) Pont Alassane Ouattara"],
    "answer": "A",
    "explanation": "Le pont Félix Houphouët-Boigny fut le premier pont construit.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En Côte d'Ivoire, quelle institution juge les contentieux électoraux des élections locales ?",
    "options": ["A) La Cour de Cassation", "B) Le Conseil Constitutionnel", "C) Le Conseil d'État", "D) La Commission Électorale Indépendante"],
    "answer": "C",
    "explanation": "Le Conseil d'État juge les contentieux des élections locales.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le plus long fleuve s'écoulant entièrement sur le territoire ivoirien ?",
    "options": ["A) Le Cavally", "B) La Comoé", "C) Le Bandama", "D) Le Sassandra"],
    "answer": "C",
    "explanation": "Le Bandama (1050 km) coule uniquement en CI.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle danse traditionnelle est inscrite au patrimoine culturel immatériel de l'UNESCO ?",
    "options": ["A) Le Gbofe", "B) Le Zaouli", "C) Le Tématé", "D) Le Boloye"],
    "answer": "B",
    "explanation": "Le Zaouli des communautés Gouro est inscrit à l'UNESCO.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Dans quelle région se trouve la ville de Man ?",
    "options": ["A) Tonkpi", "B) Guémon", "C) Cavally", "D) Bafing"],
    "answer": "A",
    "explanation": "Man est le chef-lieu de la région du Tonkpi.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle célèbre figure féminine a conduit les Baoulé en Côte d'Ivoire ?",
    "options": ["A) Anne Zingha", "B) Abla Pokou", "C) Yennenga", "D) Ndaté Yalla"],
    "answer": "B",
    "explanation": "La reine Abla Pokou a mené l'exode des Baoulé depuis le Ghana.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel traité de 1893 a officialisé la colonie de Côte d'Ivoire ?",
    "options": ["A) Traité de Berlin", "B) Décret de 1893", "C) Traité de Versailles", "D) Accords de Grand-Bassam"],
    "answer": "B",
    "explanation": "Le décret du 10 mars 1893 institue la colonie.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est l'organisation sous-régionale dont le siège est à Abuja ?",
    "options": ["A) UEMOA", "B) CEDEAO", "C) CEMAC", "D) Union Africaine"],
    "answer": "B",
    "explanation": "La CEDEAO a son siège au Nigeria, à Abuja.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui est l'actuelle directrice générale de l'OMC (Organisation mondiale du commerce) ?",
    "options": ["A) Ngozi Okonjo-Iweala", "B) Christine Lagarde", "C) Kristalina Georgieva", "D) Amina J. Mohammed"],
    "answer": "A",
    "explanation": "La Nigériane Ngozi Okonjo-Iweala dirige l'OMC.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est le nombre de membres actuels du Conseil de Sécurité de l'ONU ?",
    "options": ["A) 10", "B) 15", "C) 20", "D) 25"],
    "answer": "B",
    "explanation": "Il y a 5 membres permanents et 10 non permanents.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle est la capitale économique du Bénin ?",
    "options": ["A) Porto-Novo", "B) Cotonou", "C) Parakou", "D) Ouidah"],
    "answer": "B",
    "explanation": "Cotonou est la capitale économique, Porto-Novo la politique.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui fut le premier secrétaire général africain de l'ONU ?",
    "options": ["A) Kofi Annan", "B) Boutros Boutros-Ghali", "C) Ban Ki-moon", "D) U Thant"],
    "answer": "B",
    "explanation": "L'Égyptien Boutros Boutros-Ghali fut le premier Africain SG de l'ONU.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En mathématiques, comment appelle-t-on un polygone à 8 côtés ?",
    "options": ["A) Hexagone", "B) Heptagone", "C) Octogone", "D) Décagone"],
    "answer": "C",
    "explanation": "Un octogone a 8 côtés.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quelle planète est surnommée la planète rouge ?",
    "options": ["A) Vénus", "B) Jupiter", "C) Mars", "D) Saturne"],
    "answer": "C",
    "explanation": "Mars est surnommée la planète rouge.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a écrit le célèbre roman 'L'Étranger' ?",
    "options": ["A) Jean-Paul Sartre", "B) Albert Camus", "C) Marcel Proust", "D) Victor Hugo"],
    "answer": "B",
    "explanation": "Albert Camus a publié L'Étranger en 1942.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Quel est l'océan le plus profond du monde ?",
    "options": ["A) Atlantique", "B) Indien", "C) Arctique", "D) Pacifique"],
    "answer": "D",
    "explanation": "L'océan Pacifique contient la fosse des Mariannes, le point le plus profond.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Combien de jours compte une année bissextile ?",
    "options": ["A) 364", "B) 365", "C) 366", "D) 367"],
    "answer": "C",
    "explanation": "Une année bissextile compte 366 jours.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Comment Brice Clotaire Oligui N'Guema est-il d'abord arrivé au pouvoir au Gabon avant l'élection présidentielle de 2025 ?",
    "options": ["A) Par élection en 2020", "B) Suite au coup d'État militaire du 30 août 2023", "C) Par succession constitutionnelle", "D) Sur décision de l'Union Africaine"],
    "answer": "B",
    "explanation": "Le général Oligui N'Guema a pris le pouvoir le 30 août 2023 à la tête du CTRI suite à un coup d'État renversant Ali Bongo, avant la transition et l'élection d'avril 2025.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "Qui a remporté le Ballon d'Or 2023 ?",
    "options": ["A) Erling Haaland", "B) Lionel Messi", "C) Kylian Mbappé", "D) Karim Benzema"],
    "answer": "B",
    "explanation": "Lionel Messi a remporté son 8e Ballon d'Or en 2023, l'édition 2020 ayant été annulée.",
    "theme": "Culture Générale — Géographie et connaissances"
  },
  {
    "question": "En quelle année l'ONU a-t-elle été officiellement créée ?",
    "options": ["A) 1945", "B) 1946", "C) 1944", "D) 1950"],
    "answer": "A",
    "explanation": "L'ONU a été créée le 24 octobre 1945.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de membres permanents compte le Conseil de Sécurité de l'ONU ?",
    "options": ["A) 3", "B) 5", "C) 7", "D) 10"],
    "answer": "B",
    "explanation": "Il y a 5 membres permanents : USA, Russie, Chine, France, Royaume-Uni.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où siège la Cour internationale de Justice ?",
    "options": ["A) New York", "B) La Haye", "C) Genève", "D) Paris"],
    "answer": "B",
    "explanation": "La CIJ siège à La Haye aux Pays-Bas.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel Secrétaire Général de l'ONU a obtenu le prix Nobel de la paix en 2001 ?",
    "options": ["A) Ban Ki-moon", "B) Kofi Annan", "C) Boutros Boutros-Ghali", "D) António Guterres"],
    "answer": "B",
    "explanation": "Kofi Annan, Secrétaire Général ghanéen, a reçu le prix Nobel en 2001.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année a été créée l'OTAN ?",
    "options": ["A) 1949", "B) 1945", "C) 1955", "D) 1960"],
    "answer": "A",
    "explanation": "L'OTAN a été créée le 4 avril 1949.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où siège le Parlement européen ?",
    "options": ["A) Bruxelles", "B) Luxembourg", "C) Strasbourg", "D) Paris"],
    "answer": "C",
    "explanation": "Le Parlement européen siège principalement à Strasbourg.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien d'États membres compte l'Union Européenne actuellement ?",
    "options": ["A) 25", "B) 27", "C) 28", "D) 30"],
    "answer": "B",
    "explanation": "L'UE compte 27 États membres depuis le Brexit.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Le Mercosur est une organisation de quel continent ?",
    "options": ["A) Afrique", "B) Asie", "C) Amérique du Sud", "D) Europe"],
    "answer": "C",
    "explanation": "Le Mercosur est une organisation sud-américaine.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de l'Union africaine ?",
    "options": ["A) Accra", "B) Addis-Abeba", "C) Abidjan", "D) Le Caire"],
    "answer": "B",
    "explanation": "Le siège de l'UA est à Addis-Abeba en Éthiopie.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'Union africaine a succédé à quelle organisation ?",
    "options": ["A) ONU", "B) OUA", "C) CEDEAO", "D) UEMOA"],
    "answer": "B",
    "explanation": "L'UA a remplacé l'Organisation de l'Unité Africaine (OUA) en 2002.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année a été créée la CEDEAO ?",
    "options": ["A) 1970", "B) 1975", "C) 1980", "D) 1985"],
    "answer": "B",
    "explanation": "La CEDEAO a été créée en 1975.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien d'États membres compte actuellement l'UEMOA ?",
    "options": ["A) 6", "B) 8", "C) 10", "D) 12"],
    "answer": "B",
    "explanation": "L'UEMOA compte 8 États membres.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de l'UEMOA ?",
    "options": ["A) Dakar", "B) Ouagadougou", "C) Abidjan", "D) Lomé"],
    "answer": "B",
    "explanation": "Le siège de l'UEMOA est à Ouagadougou au Burkina Faso.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de la Banque africaine de développement ?",
    "options": ["A) Abidjan", "B) Lagos", "C) Accra", "D) Dakar"],
    "answer": "A",
    "explanation": "La BAD a son siège à Abidjan en Côte d'Ivoire.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel organisme a reçu le prix Nobel de la Paix en 2012 ?",
    "options": ["A) L'ONU", "B) L'Union Européenne", "C) La CEDEAO", "D) L'UA"],
    "answer": "B",
    "explanation": "L'Union Européenne a reçu le prix Nobel de la Paix en 2012.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de membres compte l'Assemblée générale de l'ONU ?",
    "options": ["A) 173", "B) 183", "C) 193", "D) 203"],
    "answer": "C",
    "explanation": "L'Assemblée générale compte 193 États membres.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège principal de l'ONU ?",
    "options": ["A) Washington", "B) Genève", "C) New York", "D) Paris"],
    "answer": "C",
    "explanation": "Le siège principal de l'ONU est à New York.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Qui est le Secrétaire Général actuel de l'ONU ?",
    "options": ["A) Ban Ki-moon", "B) Kofi Annan", "C) António Guterres", "D) Boutros Boutros-Ghali"],
    "answer": "C",
    "explanation": "António Guterres est Secrétaire Général depuis 2017.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel organe de l'ONU peut imposer des sanctions ?",
    "options": ["A) L'Assemblée générale", "B) Le Conseil de Sécurité", "C) La CIJ", "D) Le Secrétariat"],
    "answer": "B",
    "explanation": "Le Conseil de Sécurité a le pouvoir d'imposer des sanctions.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de membres non permanents siègent au Conseil de Sécurité ?",
    "options": ["A) 5", "B) 8", "C) 10", "D) 15"],
    "answer": "C",
    "explanation": "Il y a 10 membres non permanents élus pour 2 ans.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle est la durée du mandat des membres non permanents du Conseil de Sécurité ?",
    "options": ["A) 1 an", "B) 2 ans", "C) 3 ans", "D) 4 ans"],
    "answer": "B",
    "explanation": "Les membres non permanents sont élus pour un mandat de 2 ans.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le siège de l'Organisation mondiale de la Santé (OMS) ?",
    "options": ["A) Paris", "B) Genève", "C) New York", "D) Londres"],
    "answer": "B",
    "explanation": "L'OMS a son siège à Genève en Suisse.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année a été créée l'OUA (Organisation de l'Unité Africaine) ?",
    "options": ["A) 1960", "B) 1963", "C) 1965", "D) 1970"],
    "answer": "B",
    "explanation": "L'OUA a été créée le 25 mai 1963 à Addis-Abeba.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année l'UA a-t-elle remplacé l'OUA ?",
    "options": ["A) 1999", "B) 2000", "C) 2001", "D) 2002"],
    "answer": "D",
    "explanation": "L'Union africaine a été créée en 2002.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien d'États membres compte l'Union africaine ?",
    "options": ["A) 50", "B) 53", "C) 54", "D) 55"],
    "answer": "D",
    "explanation": "L'UA compte 55 États membres africains.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel pays africain n'est pas membre de l'Union africaine ?",
    "options": ["A) Somalie", "B) Soudan du Sud", "C) Maroc (suspendu)", "D) Aucun, tous sont membres"],
    "answer": "D",
    "explanation": "Tous les 55 pays africains sont membres de l'UA.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de l'OTAN ?",
    "options": ["A) Washington", "B) Bruxelles", "C) Paris", "D) Londres"],
    "answer": "B",
    "explanation": "Le siège de l'OTAN est à Bruxelles en Belgique.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de pays sont membres de l'OTAN actuellement ?",
    "options": ["A) 28", "B) 30", "C) 31", "D) 32"],
    "answer": "D",
    "explanation": "L'OTAN compte 32 pays membres depuis l'adhésion de la Suède en 2024.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel article du traité de l'OTAN définit la défense collective ?",
    "options": ["A) Article 3", "B) Article 5", "C) Article 7", "D) Article 10"],
    "answer": "B",
    "explanation": "L'article 5 stipule qu'une attaque contre un membre est une attaque contre tous.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de la Commission européenne ?",
    "options": ["A) Strasbourg", "B) Luxembourg", "C) Bruxelles", "D) Paris"],
    "answer": "C",
    "explanation": "La Commission européenne siège à Bruxelles.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle monnaie est utilisée par l'UEMOA ?",
    "options": ["A) Le dollar", "B) L'euro", "C) Le franc CFA", "D) Le cedi"],
    "answer": "C",
    "explanation": "Les pays de l'UEMOA utilisent le franc CFA.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien d'États membres compte la CEDEAO ?",
    "options": ["A) 12", "B) 13", "C) 14", "D) 15"],
    "answer": "D",
    "explanation": "La CEDEAO compte 15 États membres.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de la CEDEAO ?",
    "options": ["A) Dakar", "B) Abuja", "C) Accra", "D) Abidjan"],
    "answer": "B",
    "explanation": "Le siège de la CEDEAO est à Abuja au Nigeria.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle organisation africaine est dédiée à l'intégration économique et monétaire ?",
    "options": ["A) L'UA", "B) La CEDEAO", "C) L'UEMOA", "D) La BAD"],
    "answer": "C",
    "explanation": "L'UEMOA vise l'intégration économique et monétaire de ses membres.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année a été créée l'Organisation mondiale du Commerce (OMC) ?",
    "options": ["A) 1985", "B) 1990", "C) 1995", "D) 2000"],
    "answer": "C",
    "explanation": "L'OMC a été créée en 1995, succédant au GATT.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de l'OMC ?",
    "options": ["A) New York", "B) Genève", "C) Bruxelles", "D) Paris"],
    "answer": "B",
    "explanation": "L'OMC a son siège à Genève en Suisse.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel organe de l'ONU s'occupe de l'éducation, la science et la culture ?",
    "options": ["A) UNICEF", "B) UNESCO", "C) OMS", "D) FAO"],
    "answer": "B",
    "explanation": "L'UNESCO est dédiée à l'éducation, la science et la culture.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de l'UNESCO ?",
    "options": ["A) Londres", "B) Rome", "C) Paris", "D) Genève"],
    "answer": "C",
    "explanation": "L'UNESCO a son siège à Paris en France.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel organe de l'ONU s'occupe des réfugiés ?",
    "options": ["A) UNICEF", "B) HCR", "C) OIM", "D) PNUD"],
    "answer": "B",
    "explanation": "Le HCR (Haut-Commissariat aux Réfugiés) protège les réfugiés.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel organe de l'ONU s'occupe des enfants ?",
    "options": ["A) UNICEF", "B) UNESCO", "C) OMS", "D) PAM"],
    "answer": "A",
    "explanation": "L'UNICEF (Fonds des Nations Unies pour l'Enfance) protège les enfants.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année a été créé le FMI (Fonds Monétaire International) ?",
    "options": ["A) 1944", "B) 1945", "C) 1946", "D) 1950"],
    "answer": "A",
    "explanation": "Le FMI a été créé en 1944 lors de la conférence de Bretton Woods.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège du FMI ?",
    "options": ["A) New York", "B) Washington", "C) Genève", "D) Londres"],
    "answer": "B",
    "explanation": "Le FMI a son siège à Washington D.C. aux États-Unis.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de la Banque mondiale ?",
    "options": ["A) New York", "B) Washington", "C) Londres", "D) Genève"],
    "answer": "B",
    "explanation": "La Banque mondiale a son siège à Washington D.C.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel traité a créé l'Union européenne ?",
    "options": ["A) Traité de Rome", "B) Traité de Maastricht", "C) Traité de Lisbonne", "D) Traité de Paris"],
    "answer": "B",
    "explanation": "Le traité de Maastricht (1992) a créé l'Union européenne.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année le traité de Maastricht a-t-il été signé ?",
    "options": ["A) 1990", "B) 1992", "C) 1995", "D) 2000"],
    "answer": "B",
    "explanation": "Le traité de Maastricht a été signé le 7 février 1992.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle organisation régionale réunit les pays d'Asie du Sud-Est ?",
    "options": ["A) APEC", "B) ASEAN", "C) SAARC", "D) BRICS"],
    "answer": "B",
    "explanation": "L'ASEAN (Association des Nations de l'Asie du Sud-Est) réunit 10 pays.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de pays composent le G7 ?",
    "options": ["A) 5", "B) 7", "C) 8", "D) 10"],
    "answer": "B",
    "explanation": "Le G7 comprend 7 pays industrialisés : USA, Canada, Japon, Allemagne, France, Royaume-Uni, Italie.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel pays a été exclu du G8 en 2014 ?",
    "options": ["A) La Chine", "B) La Russie", "C) L'Inde", "D) Le Brésil"],
    "answer": "B",
    "explanation": "La Russie a été exclue du G8 en 2014 suite à l'annexion de la Crimée.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Que signifie BRICS ?",
    "options": ["A) Brésil, Russie, Inde, Chine, Suisse", "B) Brésil, Russie, Inde, Chine, Afrique du Sud", "C) Belgique, Russie, Iran, Chine, Sénégal", "D) Brésil, Roumanie, Inde, Canada, Suède"],
    "answer": "B",
    "explanation": "BRICS = Brésil, Russie, Inde, Chine, South Africa (Afrique du Sud).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle charte, proclamée en 1941 par Roosevelt et Churchill, annonça la création de l'ONU ?",
    "options": ["A) La Charte de San Francisco", "B) La Charte de l'Atlantique", "C) La Charte de Genève", "D) La Charte de Yalta"],
    "answer": "B",
    "explanation": "La Charte de l'Atlantique, signée en août 1941, posa les bases de l'ONU.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Lors de la conférence de Yalta (1945), quel dirigeant tenait le plus à la création de l'ONU ?",
    "options": ["A) Roosevelt", "B) Churchill", "C) Staline", "D) De Gaulle"],
    "answer": "A",
    "explanation": "Le président américain Roosevelt fut le plus grand défenseur de la création de l'ONU.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le dernier pays à avoir intégré l'ONU ?",
    "options": ["A) Le Monténégro", "B) Le Soudan du Sud", "C) Le Kosovo", "D) Le Timor oriental"],
    "answer": "B",
    "explanation": "Le Soudan du Sud a rejoint l'ONU en 2011.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelles sont les langues de travail au Secrétariat Général de l'ONU ?",
    "options": ["A) Français et Anglais", "B) Anglais et Espagnol", "C) Anglais et Chinois", "D) Français et Espagnol"],
    "answer": "A",
    "explanation": "Les deux langues de travail du Secrétariat de l'ONU sont l'anglais et le français.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Que représente la sculpture « Non-violence » devant le siège de l'ONU ?",
    "options": ["A) Une colombe", "B) Un revolver noué", "C) Un globe terrestre", "D) Des mains jointes"],
    "answer": "B",
    "explanation": "La sculpture de Carl Fredrik Reuterswärd représente un revolver au canon noué.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le statut de la Palestine à l'ONU ?",
    "options": ["A) Membre à part entière", "B) Membre associé", "C) Observateur", "D) Aucun statut"],
    "answer": "C",
    "explanation": "La Palestine a un statut d'État observateur non membre à l'ONU.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'ONU dispose-t-elle d'une armée propre ?",
    "options": ["A) Oui, avec des soldats permanents", "B) Non, elle utilise les forces des États membres", "C) Oui, basée à Genève"],
    "answer": "B",
    "explanation": "L'ONU n'a pas d'armée propre. Les casques bleus sont fournis par les États membres.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Qui est l'actuel Secrétaire Général de l'OTAN ?",
    "options": ["A) Jens Stoltenberg", "B) Anders Rasmussen", "C) Mark Rutte", "D) Ursula von der Leyen"],
    "answer": "C",
    "explanation": "Mark Rutte est devenu Secrétaire Général de l'OTAN en 2024.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le dernier pays à avoir rejoint l'OTAN ?",
    "options": ["A) La Finlande", "B) L'Ukraine", "C) La Suède", "D) La Géorgie"],
    "answer": "C",
    "explanation": "La Suède a rejoint l'OTAN le 7 mars 2024.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Qui est le président en exercice de l'Union africaine ?",
    "options": ["A) Macky Sall", "B) Évariste N'dayishimiye", "C) Félix Tshisekedi", "D) William Ruto"],
    "answer": "B",
    "explanation": "Évariste N'dayishimiye, président du Burundi, est président en exercice de l'UA.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de membres élus composent le Conseil de Paix et de Sécurité (CPS) de l'UA ?",
    "options": ["A) 10", "B) 15", "C) 20", "D) 25"],
    "answer": "B",
    "explanation": "Le CPS de l'UA est composé de 15 membres élus.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de pays compte actuellement la CEDEAO ?",
    "options": ["A) 10", "B) 12", "C) 15", "D) 16"],
    "answer": "B",
    "explanation": "La CEDEAO compte actuellement 12 pays après le retrait du Mali, du Burkina Faso et du Niger.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel pays a été réintégré à la CEDEAO après sa suspension en 2021 ?",
    "options": ["A) Le Mali", "B) La Guinée", "C) Le Niger", "D) Le Burkina Faso"],
    "answer": "B",
    "explanation": "La Guinée a été réintégrée à la CEDEAO après sa suspension suite au coup d'État de 2021.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le statut juridique de l'AES (Alliance des États du Sahel) ?",
    "options": ["A) Une fédération d'États", "B) Une confédération d'États", "C) Une organisation régionale", "D) Une union économique"],
    "answer": "B",
    "explanation": "L'AES (Mali, Burkina Faso, Niger) est une confédération d'États.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "La ZLECAF (Zone de Libre-Échange Continentale Africaine) relève de :",
    "options": ["A) La CEDEAO", "B) Un accord sous l'égide de l'UA", "C) L'ONU", "D) L'OMC"],
    "answer": "B",
    "explanation": "La ZLECAF est un accord commercial continental sous l'égide de l'Union africaine.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de la SADC (Communauté de développement de l'Afrique australe) ?",
    "options": ["A) Gaborone", "B) Pretoria", "C) Lusaka", "D) Harare"],
    "answer": "A",
    "explanation": "Le siège de la SADC est à Gaborone au Botswana.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de pays composent actuellement les BRICS ?",
    "options": ["A) 8", "B) 10", "C) 11", "D) 12"],
    "answer": "B",
    "explanation": "Les BRICS comptent actuellement 10 pays : Brésil, Russie, Inde, Chine, Afrique du Sud, Égypte, Éthiopie, Indonésie, Iran et Émirats arabes unis.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel pays a été suspendu du Mercosur ?",
    "options": ["A) L'Argentine", "B) Le Venezuela", "C) Le Paraguay", "D) L'Uruguay"],
    "answer": "B",
    "explanation": "Le Venezuela a été suspendu du Mercosur pour rupture de l'ordre démocratique.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de membres de plein droit compte le Mercosur ?",
    "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
    "answer": "B",
    "explanation": "Le Mercosur compte 5 membres de plein droit : Argentine, Bolivie, Brésil, Paraguay et Uruguay. Le Venezuela est suspendu.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année la Côte d'Ivoire a-t-elle pris la présidence de la CEDEAO ?",
    "options": ["A) 2012", "B) 2015", "C) 2018", "D) 2020"],
    "answer": "A",
    "explanation": "La Côte d'Ivoire a présidé la CEDEAO en 2012.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Qui est le président actuel de la BAD (Banque africaine de développement) ?",
    "options": ["A) Sidi Ould Tah", "B) Akinwumi Adesina", "C) Donald Kaberuka", "D) Cristina Duarte"],
    "answer": "A",
    "explanation": "Sidi Ould Tah est le président actuel de la BAD.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où a été signée en 1992 la Convention-cadre de l'ONU sur les changements climatiques ?",
    "options": ["A) Sommet de Kyoto", "B) Sommet de Paris", "C) Sommet de la Terre à Rio de Janeiro", "D) Sommet de Copenhague"],
    "answer": "C",
    "explanation": "La Convention-cadre a été signée au Sommet de la Terre à Rio de Janeiro en 1992.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Le mécanisme africain d'évaluation par les pairs relève de :",
    "options": ["A) La CEDEAO", "B) L'Union africaine", "C) L'ONU", "D) La BAD"],
    "answer": "B",
    "explanation": "Le MAEP est un instrument de l'Union africaine pour promouvoir la bonne gouvernance.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "La Banque mondiale et le FMI sont-ils associés à l'ONU ?",
    "options": ["A) Oui, ce sont des institutions spécialisées", "B) Non, ils sont totalement indépendants", "C) Seulement la Banque mondiale"],
    "answer": "A",
    "explanation": "La Banque mondiale et le FMI sont des institutions spécialisées du système des Nations Unies.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle est la deuxième puissance économique mondiale ?",
    "options": ["A) Le Japon", "B) L'Union européenne", "C) La Chine", "D) L'Inde"],
    "answer": "C",
    "explanation": "La Chine est la deuxième puissance économique mondiale derrière les États-Unis.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Qui est l'actuel président de la Commission de la CEDEAO ?",
    "options": ["A) Omar Alieu Touray", "B) Jean-Claude Brou", "C) Julius Maada Bio", "D) Nana Akufo-Addo"],
    "answer": "A",
    "explanation": "Omar Alieu Touray est le président de la Commission de la CEDEAO depuis 2022.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Qui est le président actuel de la Commission de l'UEMOA ?",
    "options": ["A) Abdoulaye Diop", "B) Cheickna Seydi Ahamadi Diawara", "C) Boureima Badini", "D) Soumaïla Cissé"],
    "answer": "A",
    "explanation": "Abdoulaye Diop est le président actuel de la Commission de l'UEMOA.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de l'Organisation internationale de la Francophonie (OIF) ?",
    "options": ["A) Genève", "B) Bruxelles", "C) Paris", "D) Montréal"],
    "answer": "C",
    "explanation": "Le siège de l'OIF est à Paris.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de pays membres compte l'Organisation internationale de la Francophonie ?",
    "options": ["A) 54", "B) 68", "C) 88", "D) 93"],
    "answer": "C",
    "explanation": "L'OIF compte 88 États et gouvernements membres, observateurs et associés.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de la Cour pénale internationale (CPI) ?",
    "options": ["A) New York", "B) La Haye", "C) Genève", "D) Bruxelles"],
    "answer": "B",
    "explanation": "La CPI siège à La Haye, aux Pays-Bas.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année la CPI a-t-elle été créée par le Statut de Rome ?",
    "options": ["A) 1998", "B) 2000", "C) 2002", "D) 2005"],
    "answer": "C",
    "explanation": "La CPI est entrée en vigueur le 1er juillet 2002, le Statut de Rome ayant été adopté en 1998.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Qu'est-ce que la CEMAC ?",
    "options": ["A) Communauté Économique des États de l'Afrique de l'Ouest", "B) Communauté Économique et Monétaire de l'Afrique Centrale", "C) Commission Européenne des Marchés de Capitaux", "D) Comité Économique des Marchés Africains"],
    "answer": "B",
    "explanation": "La CEMAC est la Communauté Économique et Monétaire de l'Afrique Centrale.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de pays composent la CEMAC ?",
    "options": ["A) 4", "B) 6", "C) 8", "D) 10"],
    "answer": "B",
    "explanation": "La CEMAC compte 6 pays : Cameroun, Centrafrique, Congo, Gabon, Guinée équatoriale et Tchad.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de la Ligue arabe ?",
    "options": ["A) Riyad", "B) Le Caire", "C) Beyrouth", "D) Tunis"],
    "answer": "B",
    "explanation": "Le siège de la Ligue arabe est au Caire, en Égypte.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de pays composent le G20 ?",
    "options": ["A) 19 pays + l'UE", "B) 20 pays exactement", "C) 18 pays + 2 organisations", "D) 20 pays + l'ONU"],
    "answer": "A",
    "explanation": "Le G20 comprend 19 pays + l'Union européenne.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle est la différence entre le Conseil de l'Europe et le Conseil européen ?",
    "options": ["A) Aucune, c'est la même chose", "B) Le Conseil de l'Europe est une organisation distincte de l'UE", "C) Le Conseil européen est plus ancien", "D) Le Conseil de l'Europe fait partie de l'ONU"],
    "answer": "B",
    "explanation": "Le Conseil de l'Europe (46 membres, siège à Strasbourg) est indépendant de l'UE. Le Conseil européen est un organe de l'UE.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année ont été signés les Accords de Paris sur le climat ?",
    "options": ["A) 2012", "B) 2015", "C) 2018", "D) 2020"],
    "answer": "B",
    "explanation": "L'Accord de Paris sur le climat a été adopté le 12 décembre 2015 lors de la COP21.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de langues officielles compte l'ONU ?",
    "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
    "answer": "C",
    "explanation": "L'ONU a 6 langues officielles : anglais, arabe, chinois, espagnol, français et russe.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel organe de l'ONU s'occupe de l'alimentation et l'agriculture ?",
    "options": ["A) PAM", "B) FAO", "C) FIDA", "D) UNICEF"],
    "answer": "B",
    "explanation": "La FAO (Organisation des Nations Unies pour l'Alimentation et l'Agriculture) a son siège à Rome.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de la FAO ?",
    "options": ["A) Paris", "B) Rome", "C) Genève", "D) New York"],
    "answer": "B",
    "explanation": "Le siège de la FAO est à Rome, en Italie.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le rôle principal du PAM (Programme Alimentaire Mondial) ?",
    "options": ["A) Financer les pays pauvres", "B) Lutter contre la faim dans le monde", "C) Protéger les réfugiés", "D) Promouvoir l'éducation"],
    "answer": "B",
    "explanation": "Le PAM est l'organisme d'aide alimentaire de l'ONU, luttant contre la faim.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel pays membre fondateur a quitté l'Union européenne ?",
    "options": ["A) La Suisse", "B) La Norvège", "C) Le Royaume-Uni", "D) L'Islande"],
    "answer": "C",
    "explanation": "Le Royaume-Uni a quitté l'UE le 31 janvier 2020 (Brexit).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année le Brexit a-t-il été effectif ?",
    "options": ["A) 2016", "B) 2018", "C) 2020", "D) 2021"],
    "answer": "C",
    "explanation": "Le Brexit est devenu effectif le 31 janvier 2020 (le référendum avait eu lieu en 2016).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de pays membres l'OPEP compte-t-elle actuellement ?",
    "options": ["A) 10", "B) 11", "C) 12", "D) 15"],
    "answer": "B",
    "explanation": "L'OPEP compte 11 pays membres.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel organisme de l'ONU est chargé du maintien de la paix ?",
    "options": ["A) L'Assemblée générale", "B) Le Conseil de Sécurité", "C) La CIJ", "D) Le Conseil économique et social"],
    "answer": "B",
    "explanation": "Le Conseil de Sécurité est l'organe principal chargé du maintien de la paix et de la sécurité internationales.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le nombre total de membres du Conseil de Sécurité (permanents + non permanents) ?",
    "options": ["A) 10", "B) 12", "C) 15", "D) 20"],
    "answer": "C",
    "explanation": "Le Conseil de Sécurité compte 15 membres : 5 permanents + 10 non permanents.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle convention internationale protège les droits de l'Homme ?",
    "options": ["A) Convention de Genève", "B) Déclaration universelle des droits de l'homme", "C) Traité de Versailles", "D) Charte de l'Atlantique"],
    "answer": "B",
    "explanation": "La DUDH a été adoptée le 10 décembre 1948 par l'Assemblée générale de l'ONU.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année la Déclaration universelle des droits de l'homme a-t-elle été adoptée ?",
    "options": ["A) 1945", "B) 1948", "C) 1950", "D) 1955"],
    "answer": "B",
    "explanation": "La DUDH a été adoptée le 10 décembre 1948 à Paris.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de l'Organisation Internationale du Travail (OIT) ?",
    "options": ["A) New York", "B) Genève", "C) Paris", "D) Bruxelles"],
    "answer": "B",
    "explanation": "L'OIT a son siège à Genève, en Suisse.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel accord de libre-échange lie les États-Unis, le Mexique et le Canada ?",
    "options": ["A) ALENA", "B) ACEUM (USMCA)", "C) MERCOSUR", "D) APEC"],
    "answer": "B",
    "explanation": "L'ACEUM (ou USMCA en anglais) a remplacé l'ALENA en 2020.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle ann?e l'ONU a-t-elle ete creee ?",
    "options": ["A) 24 octobre 1945", "B) 8 mai 1945", "C) 26 juin 1945", "D) 1er janvier 1946"],
    "answer": "A",
    "explanation": "L'ONU a officiellement ete creee le 24 octobre 1945, date d'entree en vigueur de la Charte des Nations Unies.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien d'?tats membres compte l'ONU ?",
    "options": ["A) 185", "B) 193", "C) 197", "D) 200"],
    "answer": "B",
    "explanation": "L'ONU compte actuellement 193 ?tats membres.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le dernier pays a avoir integre l'ONU ?",
    "options": ["A) Kosovo", "B) Soudan du Sud", "C) Timor oriental", "D) Montenegro"],
    "answer": "B",
    "explanation": "Le Soudan du Sud est le 193e et dernier ?tat a integrer l'ONU, en juillet 2011.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle est la nationalit? de l'actuel Secretaire General des Nations Unies ?",
    "options": ["A) Ghaneenne", "B) Portugaise", "C) Bresilienne", "D) Canadienne"],
    "answer": "B",
    "explanation": "Antonio Guterres, Secretaire General de l'ONU depuis janvier 2017, est Portugais.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel Secretaire General de l'ONU a obtenu le prix Nobel de la Paix en 2001 ?",
    "options": ["A) Boutros Boutros-Ghali", "B) Kofi Annan", "C) Ban Ki-moon", "D) Javier Perez de Cuellar"],
    "answer": "B",
    "explanation": "Kofi Annan et l'ONU ont conjointement recu le prix Nobel de la Paix le 10 decembre 2001.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle ann?e l'OTAN a-t-elle ete creee ?",
    "options": ["A) 4 avril 1949", "B) 5 mai 1950", "C) 24 octobre 1945", "D) 14 aout 1941"],
    "answer": "A",
    "explanation": "L'OTAN a ete creee le 4 avril 1949 par le traite de Washington.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Ou se trouve le siege de l'OTAN ?",
    "options": ["A) Bruxelles", "B) Paris", "C) Londres", "D) Geneve"],
    "answer": "A",
    "explanation": "Le siege de l'OTAN est a Bruxelles, en Belgique.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est l'actuel Secretaire General de l'OTAN ?",
    "options": ["A) Jens Stoltenberg", "B) Anders Fogh Rasmussen", "C) Mark Rutte", "D) George Robertson"],
    "answer": "C",
    "explanation": "Mark Rutte est l'actuel Secretaire General de l'OTAN depuis octobre 2024.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le dernier ?tat a avoir adhre a l'OTAN ?",
    "options": ["A) La Finlande", "B) La Suede", "C) L'Ukraine", "D) La Georgie"],
    "answer": "B",
    "explanation": "La Suede a rejoint l'OTAN le 7 mars 2024, devenant le 32e ?tat membre.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien d'?tats membres compte l'Union Europeenne ?",
    "options": ["A) 25", "B) 27", "C) 28", "D) 30"],
    "answer": "B",
    "explanation": "L'UE compte 27 ?tats membres depuis le Brexit en 2020.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Ou siege principalement le Parlement europeen ?",
    "options": ["A) Bruxelles", "B) Luxembourg", "C) Strasbourg", "D) Paris"],
    "answer": "C",
    "explanation": "Le Parlement europeen siege principalement a Strasbourg.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "La CEDEAO a ete creee en :",
    "options": ["A) 1960", "B) 1975", "C) 1980", "D) 1990"],
    "answer": "B",
    "explanation": "La CEDEAO a ete creee en 1975 par le traite de Lagos.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de pays membres compte la CEDEAO aujourd'hui ?",
    "options": ["A) 15", "B) 12", "C) 16", "D) 10"],
    "answer": "B",
    "explanation": "Suite aux suspensions et retraits (Mali, Burkina Faso, Niger), la CEDEAO compte actuellement 12 membres.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Ou se trouve le siege de l'UEMOA ?",
    "options": ["A) Abidjan", "B) Ouagadougou", "C) Dakar", "D) Lome"],
    "answer": "B",
    "explanation": "Le siege de l'UEMOA est a Ouagadougou, au Burkina Faso.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "La Banque africaine de developpement (BAD) a son siege a :",
    "options": ["A) Abidjan", "B) Addis-Abeba", "C) Le Caire", "D) Nairobi"],
    "answer": "A",
    "explanation": "Le siege permanent de la BAD est a Abidjan, en C?te d'Ivoire.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel organisme a obtenu le prix Nobel de la Paix en 2012 ?",
    "options": ["A) L'ONU", "B) L'Union Europeenne", "C) L'OTAN", "D) L'OMS"],
    "answer": "B",
    "explanation": "L'Union Europeenne a ete couronnee du prix Nobel de la Paix en 2012.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'Union africaine a succede a :",
    "options": ["A) La CEDEAO", "B) L'OUA", "C) La CEMAC", "D) L'UEMOA"],
    "answer": "B",
    "explanation": "L'UA a succede a l'Organisation de l'Unite Africaine (OUA) en 2002.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le statut juridique de l'AES (Alliance des ?tats du Sahel) ?",
    "options": ["A) Une federation", "B) Une confederation d'?tats", "C) Une communaute ?conomique", "D) Une alliance militaire"],
    "answer": "B",
    "explanation": "L'AES regroupe le Mali, le Burkina Faso et le Niger sous forme de confederation d'?tats.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "La ZLECAF releve de :",
    "options": ["A) La CEDEAO", "B) L'Union Africaine", "C) L'ONU", "D) La Banque mondiale"],
    "answer": "B",
    "explanation": "La Zone de Libre-Echange Continentale Africaine (ZLECAF) est un accord sous l'egide de l'Union Africaine.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien d'États membres compte l'UEMOA ?",
    "options": ["A) 5", "B) 8", "C) 10", "D) 12"],
    "answer": "B",
    "explanation": "L'UEMOA compte 8 États membres partageant le franc CFA.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le siège de la Banque Centrale des États de l'Afrique de l'Ouest (BCEAO) ?",
    "options": ["A) Abidjan", "B) Bamako", "C) Dakar", "D) Ouagadougou"],
    "answer": "C",
    "explanation": "La BCEAO a son siège à Dakar (Sénégal).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel organisme de l'ONU s'occupe des réfugiés ?",
    "options": ["A) UNICEF", "B) HCR (UNHCR)", "C) OMS", "D) PAM"],
    "answer": "B",
    "explanation": "Le Haut-Commissariat des Nations Unies pour les Réfugiés (HCR) protège les réfugiés dans le monde.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle organisation africaine a succédé à l'Organisation de l'Unité Africaine (OUA) ?",
    "options": ["A) La CEDEAO", "B) L'Union Africaine", "C) La SADC", "D) Le NEPAD"],
    "answer": "B",
    "explanation": "L'Union Africaine a remplacé l'OUA en 2002 à Durban (Afrique du Sud).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le rôle du FMI (Fonds Monétaire International) ?",
    "options": ["A) Financer les guerres", "B) Assurer la stabilité financière internationale", "C) Construire des infrastructures", "D) Gérer les migrations"],
    "answer": "B",
    "explanation": "Le FMI assure la stabilité du système monétaire international et aide les pays en difficulté.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle est la différence entre la Cour Internationale de Justice (CIJ) et la Cour Pénale Internationale (CPI) ?",
    "options": ["A) Aucune différence", "B) CIJ juge les États ; CPI juge les individus", "C) CPI est plus ancienne", "D) La CIJ est privée"],
    "answer": "B",
    "explanation": "La CIJ règle les différends entre États ; la CPI poursuit les individus pour crimes internationaux.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le siège de l'Organisation Mondiale du Commerce (OMC) ?",
    "options": ["A) New York", "B) Bruxelles", "C) Genève", "D) Paris"],
    "answer": "C",
    "explanation": "L'OMC est basée à Genève, en Suisse.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le siège de la CEDEAO ?",
    "options": ["A) Dakar", "B) Accra", "C) Abuja", "D) Lagos"],
    "answer": "C",
    "explanation": "Le siège de la CEDEAO est à Abuja, Nigeria.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle organisation internationale a pour mission principale le maintien de la paix et de la sécurité internationales ?",
    "options": ["A) L'UNESCO", "B) Le FMI", "C) L'ONU", "D) L'OMC"],
    "answer": "C",
    "explanation": "L'ONU, notamment via son Conseil de Sécurité, a pour mission centrale le maintien de la paix.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel traité fonde l'Union Européenne dans sa forme actuelle ?",
    "options": ["A) Traité de Rome", "B) Traité de Maastricht", "C) Traité de Lisbonne", "D) Traité de Paris"],
    "answer": "C",
    "explanation": "Le Traité de Lisbonne (2007, en vigueur en 2009) fonde l'UE dans sa forme actuelle.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle est la devise officielle de l'Union Africaine ?",
    "options": ["A) « Unité, Solidarité, Développement »", "B) « Une Afrique unie et forte »", "C) « Afrique d'abord »", "D) « L'Afrique en marche »"],
    "answer": "A",
    "explanation": "La devise de l'UA est « Une Afrique unie et forte » en réalité, mais son slogan est souvent résumé à l'unité africaine.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le nom du programme de développement de l'UA lancé en 2001 ?",
    "options": ["A) Plan Marshall africain", "B) NEPAD", "C) AGOA", "D) Agenda 2063"],
    "answer": "B",
    "explanation": "Le NEPAD (Nouveau Partenariat pour le Développement de l'Afrique) a été lancé en 2001.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel organe de l'ONU conseille sur les questions économiques et sociales ?",
    "options": ["A) Le Conseil de sécurité", "B) L'Assemblée Générale", "C) Le ECOSOC", "D) La CIJ"],
    "answer": "C",
    "explanation": "Le Conseil Économique et Social (ECOSOC) coordonne les travaux économiques et sociaux de l'ONU.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le siège de l'Organisation Internationale du Travail (OIT) ?",
    "options": ["A) Paris", "B) New York", "C) Genève", "D) Bruxelles"],
    "answer": "C",
    "explanation": "L'OIT, fondée en 1919, a son siège à Genève. C'est la plus ancienne agence spécialisée de l'ONU.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle organisation regroupe les pays d'Afrique centrale ?",
    "options": ["A) CEDEAO", "B) UEMOA", "C) CEEAC", "D) SADC"],
    "answer": "C",
    "explanation": "La Communauté Économique des États de l'Afrique Centrale (CEEAC) regroupe les pays d'Afrique centrale.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le siège du G20 (secrétariat) ?",
    "options": ["A) Washington", "B) Bruxelles", "C) Il est tournant (présidence rotative)", "D) New York"],
    "answer": "C",
    "explanation": "Le G20 n'a pas de siège fixe. La présidence et le secrétariat tournent chaque année.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle organisation émet le franc CFA de la zone CEMAC ?",
    "options": ["A) BCEAO", "B) BEAC", "C) BM", "D) FMI"],
    "answer": "B",
    "explanation": "La BEAC (Banque des États de l'Afrique Centrale) émet le franc CFA pour la zone CEMAC.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel pays a été exclu de l'Union Africaine en 2019 suite à un coup d'État ?",
    "options": ["A) Mali", "B) Guinée", "C) Soudan", "D) Zimbabwe"],
    "answer": "C",
    "explanation": "Le Soudan a été suspendu de l'UA en 2019 après la chute d'Omar el-Béchir.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle organisation régionale regroupe les pays du Maghreb ?",
    "options": ["A) UMA", "B) CEN-SAD", "C) IGAD", "D) Ligue arabe"],
    "answer": "A",
    "explanation": "L'Union du Maghreb Arabe (UMA) regroupe Algérie, Libye, Maroc, Mauritanie et Tunisie.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le rôle de l'AIEA (Agence Internationale de l'Énergie Atomique) ?",
    "options": ["A) Produire l'énergie nucléaire", "B) Promouvoir l'usage pacifique du nucléaire et prévenir sa prolifération", "C) Gérer les déchets nucléaires mondiaux", "D) Financer les centrales nucléaires"],
    "answer": "B",
    "explanation": "L'AIEA, basée à Vienne, promeut l'utilisation pacifique du nucléaire et surveille la non-prolifération.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle institution internationale a pour mission l'éradication de la pauvreté dans le monde ?",
    "options": ["A) FMI", "B) Banque Mondiale", "C) OMC", "D) OMS"],
    "answer": "B",
    "explanation": "La Banque Mondiale a pour objectif principal la réduction de la pauvreté et le développement.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le programme des Nations Unies pour l'environnement ?",
    "options": ["A) PNUE", "B) FAO", "C) UNESCO", "D) PNUD"],
    "answer": "A",
    "explanation": "Le PNUE (Programme des Nations Unies pour l'Environnement) coordonne les actions environnementales de l'ONU.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle organisation internationale régit le commerce international des armes ?",
    "options": ["A) Interpol", "B) Traité sur le commerce des armes (TCA/ONU)", "C) OTAN", "D) OMC"],
    "answer": "B",
    "explanation": "Le Traité sur le Commerce des Armes (2013) encadre les transferts internationaux d'armements.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le siège de l'OCDE (Organisation de Coopération et de Développement Économiques) ?",
    "options": ["A) Bruxelles", "B) Genève", "C) Paris", "D) New York"],
    "answer": "C",
    "explanation": "L'OCDE est basée à Paris, France.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année l'OUA (Organisation de l'Unité Africaine) a-t-elle été fondée ?",
    "options": ["A) 1955", "B) 1963", "C) 1970", "D) 1980"],
    "answer": "B",
    "explanation": "L'OUA a été fondée le 25 mai 1963 à Addis-Abeba, Éthiopie.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le programme de développement durable de l'ONU à l'horizon 2030 ?",
    "options": ["A) Agenda 2063", "B) ODD (Objectifs de Développement Durable)", "C) Plan Marshall", "D) Accord de Paris"],
    "answer": "B",
    "explanation": "Les 17 ODD (Objectifs de Développement Durable) ont été adoptés en 2015 pour l'horizon 2030.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le siège du Parlement Panafricain ?",
    "options": ["A) Addis-Abeba", "B) Midrand (Afrique du Sud)", "C) Abuja", "D) Accra"],
    "answer": "B",
    "explanation": "Le Parlement Panafricain siège à Midrand, en Afrique du Sud.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel accord international a remplacé le Protocole de Kyoto ?",
    "options": ["A) Accord de Copenhague", "B) Accord de Paris", "C) Accord de Montréal", "D) Convention de Rio"],
    "answer": "B",
    "explanation": "L'Accord de Paris (COP21, 2015) a remplacé le Protocole de Kyoto pour la lutte contre le changement climatique.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle organisation internationale défend les droits de l'enfant ?",
    "options": ["A) HCR", "B) UNICEF", "C) OMS", "D) OIT"],
    "answer": "B",
    "explanation": "L'UNICEF (Fonds des Nations Unies pour l'Enfance) œuvre pour les droits et le bien-être des enfants.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle est la principale mission de l'UNESCO ?",
    "options": ["A) Maintien de la paix militaire", "B) Promotion de la coopération internationale en éducation, sciences et culture", "C) Régulation du commerce mondial", "D) Contrôle de l'armement nucléaire"],
    "answer": "B",
    "explanation": "L'UNESCO promeut la paix par l'éducation, les sciences, la culture et la communication.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel État membre de l'ONU bénéficie d'un statut d'observateur (non-membre votant) ?",
    "options": ["A) La Suisse", "B) Le Vatican", "C) Le Liechtenstein", "D) San Marin"],
    "answer": "B",
    "explanation": "Le Vatican (Saint-Siège) est observateur non-membre à l'ONU. La Suisse est membre à part entière depuis 2002.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel organe de l'ONU élit le Secrétaire Général ?",
    "options": ["A) Le Conseil de Sécurité seul", "B) L'Assemblée Générale sur recommandation du Conseil de Sécurité", "C) Les 5 membres permanents", "D) L'Assemblée Générale seule"],
    "answer": "B",
    "explanation": "Le SG est nommé par l'AG sur recommandation du CS (article 97 de la Charte de l'ONU).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle organisation internationale lutte contre le blanchiment d'argent ?",
    "options": ["A) Interpol", "B) GAFI (FATF)", "C) FMI", "D) OMC"],
    "answer": "B",
    "explanation": "Le GAFI (Groupe d'Action Financière/Financial Action Task Force) combat le blanchiment et le financement du terrorisme.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de langues officielles compte l'Union Africaine ?",
    "options": ["A) 2", "B) 4", "C) 6", "D) 11"],
    "answer": "C",
    "explanation": "L'Union Africaine compte 6 langues officielles de travail : l'arabe, l'anglais, le français, le portugais, l'espagnol et le kiswahili (adopté officiellement en 2022).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le siège de la Banque Africaine de Développement (BAD) ?",
    "options": ["A) Addis-Abeba", "B) Abidjan", "C) Dakar", "D) Johannesburg"],
    "answer": "B",
    "explanation": "Le siège de la BAD est à Abidjan, Côte d'Ivoire.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'accord de Cotonou (2000) régissait les relations entre quels acteurs ?",
    "options": ["A) CEDEAO et UA", "B) UE et pays ACP (Afrique-Caraïbes-Pacifique)", "C) ONU et pays en développement", "D) FMI et pays endettés"],
    "answer": "B",
    "explanation": "L'accord de Cotonou organisait le partenariat entre l'UE et les 79 pays ACP en matière de développement et commerce.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le siège du Conseil de Sécurité de l'ONU ?",
    "options": ["A) Genève", "B) Washington", "C) New York", "D) La Haye"],
    "answer": "C",
    "explanation": "Le Conseil de Sécurité siège au Siège de l'ONU à New York.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel mécanisme de l'ONU permet aux États de soumettre des questions à l'Assemblée Générale pour une session extraordinaire d'urgence ?",
    "options": ["A) La résolution « Acheson »", "B) La résolution 377 (Unis pour la Paix)", "C) L'article 51 de la Charte", "D) Le protocole facultatif"],
    "answer": "B",
    "explanation": "La résolution 377 (Unis pour la Paix, 1950) permet à l'AG de se réunir en session d'urgence si le CS est bloqué.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle organisation internationale coordonne les politiques d'aviation civile ?",
    "options": ["A) OACI", "B) IATA", "C) OTAN", "D) OMM"],
    "answer": "A",
    "explanation": "L'OACI (Organisation de l'Aviation Civile Internationale) est l'agence spécialisée de l'ONU pour l'aviation civile.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le principal organe judiciaire de l'UEMOA ?",
    "options": ["A) La Cour de Justice", "B) La Cour Arbitrale", "C) La Cour Suprême régionale", "D) La Chambre d'appel"],
    "answer": "A",
    "explanation": "La Cour de Justice de l'UEMOA est l'organe juridictionnel chargé d'interpréter et d'appliquer le droit communautaire.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le nom complet de la CEDEAO en anglais ?",
    "options": ["A) ECOWAS", "B) OECAS", "C) WAEMU", "D) SADC"],
    "answer": "A",
    "explanation": "ECOWAS = Economic Community of West African States (CEDEAO en français).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le rôle du Conseil de Paix et de Sécurité (CPS) de l'UA ?",
    "options": ["A) Gérer les élections africaines", "B) Prévenir, gérer et résoudre les conflits en Afrique", "C) Coordonner les politiques économiques", "D) Contrôler les migrations"],
    "answer": "B",
    "explanation": "Le CPS de l'UA est l'organe de sécurité collective chargé de prévenir et gérer les conflits africains.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le siège de la Cour de Justice de la CEDEAO ?",
    "options": ["A) Lagos", "B) Accra", "C) Abuja", "D) Dakar"],
    "answer": "C",
    "explanation": "La Cour de Justice de la CEDEAO siège à Abuja, Nigeria.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de la Commission de la CEDEAO ?",
    "options": ["A) Dakar, Sénégal", "B) Abuja, Nigeria", "C) Accra, Ghana", "D) Abidjan, Côte d'Ivoire"],
    "answer": "B",
    "explanation": "Le siège de la CEDEAO (Commission) est situé à Abuja au Nigeria.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle est la date de création de la CEDEAO ?",
    "options": ["A) 25 mai 1963", "B) 28 mai 1975", "C) 10 janvier 1994", "D) 15 avril 1975"],
    "answer": "B",
    "explanation": "La CEDEAO a été créée le 28 mai 1975 par le Traité de Lagos.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Parmi les institutions suivantes, laquelle ne fait pas partie de l'UEMOA ?",
    "options": ["A) La Cour de Justice", "B) La Banque Ouest Africaine de Développement (BOAD)", "C) Le Parlement de la CEDEAO", "D) La Cour des Comptes"],
    "answer": "C",
    "explanation": "Le Parlement de la CEDEAO est une institution de la CEDEAO, non de l'UEMOA.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année l'Organisation de l'Unité Africaine (OUA) est-elle devenue l'Union Africaine (UA) ?",
    "options": ["A) 1999", "B) 2000", "C) 2001", "D) 2002"],
    "answer": "D",
    "explanation": "L'OUA a été officiellement remplacée par l'Union Africaine en 2002 à Durban.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de pays membres compte l'UEMOA ?",
    "options": ["A) 7", "B) 8", "C) 15", "D) 16"],
    "answer": "B",
    "explanation": "L'UEMOA compte 8 États membres : Bénin, Burkina Faso, Côte d'Ivoire, Guinée-Bissau, Mali, Niger, Sénégal et Togo.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où est situé le siège de la Banque Africaine de Développement (BAD) ?",
    "options": ["A) Tunis", "B) Addis-Abeba", "C) Abidjan", "D) Johannesburg"],
    "answer": "C",
    "explanation": "Le siège statutaire de la BAD est à Abidjan, en Côte d'Ivoire.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Lequel de ces organes est l'organe décisionnel suprême de l'Union Africaine ?",
    "options": ["A) Le Conseil de Paix et de Sécurité", "B) Le Conseil exécutif", "C) La Commission de l'Union africaine", "D) La Conférence des chefs d'État et de gouvernement"],
    "answer": "D",
    "explanation": "La Conférence des chefs d'État et de gouvernement est l'organe suprême de l'UA.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le but principal de la ZLECAf ?",
    "options": ["A) Créer une monnaie unique africaine", "B) Établir une zone de libre-échange continentale en Afrique", "C) Unifier les armées africaines", "D) Promouvoir la culture africaine exclusivement"],
    "answer": "B",
    "explanation": "La ZLECAf vise à créer un marché unique pour les biens et services en Afrique.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel organe de l'ONU est responsable du maintien de la paix et de la sécurité internationales ?",
    "options": ["A) L'Assemblée générale", "B) Le Conseil de sécurité", "C) La Cour internationale de Justice", "D) Le Secrétariat"],
    "answer": "B",
    "explanation": "C'est la mission principale du Conseil de sécurité de l'ONU.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de membres permanents siègent au Conseil de sécurité de l'ONU ?",
    "options": ["A) 5", "B) 10", "C) 15", "D) 20"],
    "answer": "A",
    "explanation": "Il y a 5 membres permanents (Chine, États-Unis, France, Royaume-Uni, Russie).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où siège la Cour pénale internationale (CPI) ?",
    "options": ["A) Genève", "B) New York", "C) La Haye", "D) Strasbourg"],
    "answer": "C",
    "explanation": "La CPI a son siège à La Haye, aux Pays-Bas.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle institution de Bretton Woods a pour but principal d'aider au développement économique et de réduire la pauvreté ?",
    "options": ["A) L'OMC", "B) Le FMI", "C) La Banque Mondiale", "D) L'OIT"],
    "answer": "C",
    "explanation": "La Banque Mondiale finance le développement, tandis que le FMI gère la stabilité financière mondiale.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Lequel de ces pays a quitté la CEDEAO puis y est retourné ?",
    "options": ["A) Mauritanie", "B) Maroc", "C) Mali", "D) Aucun, la Mauritanie a quitté et n'est pas revenue"],
    "answer": "D",
    "explanation": "La Mauritanie a quitté la CEDEAO en 2000 et n'en est plus membre à part entière.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel traité a institué l'UEMOA ?",
    "options": ["A) Traité de Dakar", "B) Traité de Lomé", "C) Traité de Bamako", "D) Traité de Cotonou"],
    "answer": "A",
    "explanation": "L'UEMOA a été créée par le Traité de Dakar signé le 10 janvier 1994.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Laquelle de ces institutions est une agence spécialisée de l'ONU basée à Paris ?",
    "options": ["A) OMS", "B) UNESCO", "C) FAO", "D) OIT"],
    "answer": "B",
    "explanation": "L'UNESCO, chargée de l'éducation, de la science et de la culture, a son siège à Paris.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel Ivoirien a été Secrétaire général adjoint des Nations Unies aux opérations de maintien de la paix ?",
    "options": ["A) Amara Essy", "B) Jean-Claude Brou", "C) Youssoufou Bamba", "D) Il n'y a pas eu d'Ivoirien à ce poste spécifique récemment"],
    "answer": "D",
    "explanation": "Piège, c'est le Français Jean-Pierre Lacroix ou Hervé Ladsous, pas un Ivoirien. (Amara Essy fut SG de l'OUA).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Qui a été le premier Secrétaire général de l'Organisation de l'Unité Africaine (OUA) ?",
    "options": ["A) Diallo Telli", "B) Edem Kodjo", "C) Nzo Ekangaki", "D) William Eteki Mboumoua"],
    "answer": "A",
    "explanation": "Le Guinéen Diallo Telli fut le premier Secrétaire général de l'OUA de 1964 à 1972.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Laquelle de ces organisations a pour siège Genève ?",
    "options": ["A) FMI", "B) OMC", "C) FAO", "D) AIEA"],
    "answer": "B",
    "explanation": "L'Organisation Mondiale du Commerce (OMC) est basée à Genève, Suisse.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En 2024, quel pays a annoncé son retrait de la CEDEAO avec le Mali et le Burkina Faso ?",
    "options": ["A) Guinée", "B) Niger", "C) Tchad", "D) Sénégal"],
    "answer": "B",
    "explanation": "Le Niger, avec le Mali et le Burkina Faso, a annoncé son retrait de la CEDEAO début 2024.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'Organisation Internationale de la Francophonie (OIF) a son siège à :",
    "options": ["A) Bruxelles", "B) Genève", "C) Paris", "D) Montréal"],
    "answer": "C",
    "explanation": "Le siège de l'OIF est à Paris, en France.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'Ivoirien Jean-Claude Kassi Brou a été président de quelle commission de 2018 à 2022 ?",
    "options": ["A) Commission de l'UEMOA", "B) Commission de la CEDEAO", "C) Commission de l'Union Africaine", "D) Commission économique pour l'Afrique"],
    "answer": "B",
    "explanation": "Il fut Président de la Commission de la CEDEAO avant de diriger la BCEAO.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le nom actuel du traité liant l'Union européenne aux pays ACP (Afrique, Caraïbes, Pacifique) ?",
    "options": ["A) Accord de Cotonou", "B) Accord de Lomé", "C) Accord de Samoa", "D) Accord de Yaoundé"],
    "answer": "C",
    "explanation": "L'Accord de Samoa a remplacé l'Accord de Cotonou depuis 2023.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Dans le système des Nations Unies, que signifie le sigle HCR ?",
    "options": ["A) Haut Commissariat aux Réfugiés", "B) Haut Conseil pour la Reconstruction", "C) Haut Commissariat pour le Climat et les Réfugiés", "D) Haut Comité de Résolution"],
    "answer": "A",
    "explanation": "HCR signifie Haut Commissariat des Nations Unies pour les Réfugiés.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Qui nomme le Secrétaire général des Nations Unies ?",
    "options": ["A) Le Conseil de Sécurité", "B) L'Assemblée générale sur recommandation du Conseil de sécurité", "C) La Cour internationale de Justice", "D) Les 5 membres permanents seuls"],
    "answer": "B",
    "explanation": "L'Assemblée générale nomme le SG sur recommandation du Conseil de sécurité.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "La Cour de justice de la CEDEAO a son siège à :",
    "options": ["A) Lomé", "B) Abuja", "C) Dakar", "D) Abidjan"],
    "answer": "B",
    "explanation": "Le siège de la Cour de justice de la CEDEAO est également à Abuja, au Nigeria.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est l'objectif principal du NEPAD ?",
    "options": ["A) Favoriser la démocratie en Europe", "B) Éradiquer la pauvreté et placer l'Afrique sur la voie du développement", "C) Créer une alliance militaire africaine", "D) Lutter contre les pandémies"],
    "answer": "B",
    "explanation": "Le Nouveau Partenariat pour le Développement de l'Afrique vise le développement socio-économique du continent.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "La monnaie de l'UEMOA, le franc CFA, est émise par :",
    "options": ["A) La BEAC", "B) La BCEAO", "C) La BOAD", "D) La BAD"],
    "answer": "B",
    "explanation": "La Banque Centrale des États de l'Afrique de l'Ouest (BCEAO) émet le franc CFA de l'UEMOA.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Lequel de ces États est membre de la CEMAC mais pas de l'UEMOA ?",
    "options": ["A) Togo", "B) Mali", "C) Gabon", "D) Guinée-Bissau"],
    "answer": "C",
    "explanation": "Le Gabon appartient à la CEMAC (Afrique centrale) et non à l'UEMOA (Afrique de l'Ouest).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel traité est à l'origine de l'Union européenne (1992) ?",
    "options": ["A) Traité de Rome", "B) Traité de Maastricht", "C) Traité d'Amsterdam", "D) Traité de Lisbonne"],
    "answer": "B",
    "explanation": "Le traité de Maastricht a officiellement créé l'Union européenne.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "La Côte d'Ivoire est le premier producteur mondial de :",
    "options": ["A) Café", "B) Cacao", "C) Hévéa", "D) Anacarde"],
    "answer": "B",
    "explanation": "La Côte d'Ivoire est le 1er producteur mondial de cacao.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Le Conseil de l'Entente, créé en 1959, regroupe combien d'États ?",
    "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
    "answer": "B",
    "explanation": "Il regroupe 5 pays : Côte d'Ivoire, Niger, Burkina Faso, Bénin et Togo.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle est la plus ancienne organisation intergouvernementale africaine encore en activité ?",
    "options": ["A) CEDEAO", "B) Conseil de l'Entente", "C) Union du Fleuve Mano", "D) OUA"],
    "answer": "B",
    "explanation": "Le Conseil de l'Entente, fondé en 1959, est la doyenne des organisations sous-régionales ouest-africaines.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'Union du Fleuve Mano regroupe :",
    "options": ["A) Sénégal, Mauritanie, Mali", "B) Guinée, Sierra Leone, Liberia, Côte d'Ivoire", "C) Côte d'Ivoire, Ghana, Togo, Bénin", "D) Niger, Nigeria, Tchad, Cameroun"],
    "answer": "B",
    "explanation": "L'Union du fleuve Mano comprend le Liberia, la Sierra Leone, la Guinée et la Côte d'Ivoire.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de l'Organisation Mondiale de la Santé (OMS) ?",
    "options": ["A) New York", "B) Genève", "C) Rome", "D) Vienne"],
    "answer": "B",
    "explanation": "Le siège de l'OMS est à Genève, en Suisse.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "La FAO (Organisation des Nations Unies pour l'alimentation et l'agriculture) a son siège à :",
    "options": ["A) Paris", "B) New York", "C) Rome", "D) Londres"],
    "answer": "C",
    "explanation": "Le siège de la FAO se trouve à Rome, en Italie.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Lequel de ces présidents ivoiriens a été Secrétaire exécutif du Conseil de l'Entente ?",
    "options": ["A) Félix Houphouët-Boigny", "B) Henri Konan Bédié", "C) Laurent Gbagbo", "D) Alassane Ouattara"],
    "answer": "D",
    "explanation": "Piège, c'est Félix Houphouët-Boigny qui a été le fondateur et l'initiateur principal. Aucun n'a été Secrétaire exécutif, car c'est un poste administratif.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel a été le premier Ivoirien élu à l'Académie française ?",
    "options": ["A) Bernard Dadié", "B) Ahmadou Kourouma", "C) aucun Ivoirien n'a été élu", "D) Maurice Bandaman"],
    "answer": "C",
    "explanation": "Léopold Sédar Senghor (Sénégal) y fut élu, mais aucun Ivoirien n'est membre de l'Académie française.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'Organisation pour l'Harmonisation en Afrique du Droit des Affaires (OHADA) a été créée par le traité de :",
    "options": ["A) Dakar", "B) Abidjan", "C) Port-Louis", "D) Libreville"],
    "answer": "C",
    "explanation": "Le traité créant l'OHADA a été signé à Port-Louis (Île Maurice) en 1993.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve la Cour commune de justice et d'arbitrage de l'OHADA ?",
    "options": ["A) Yaoundé", "B) Dakar", "C) Abidjan", "D) Cotonou"],
    "answer": "C",
    "explanation": "La CCJA a son siège à Abidjan, Côte d'Ivoire.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'ECOWAS correspond en français à :",
    "options": ["A) La CEDEAO", "B) L'UEMOA", "C) L'Union Africaine", "D) La BAD"],
    "answer": "A",
    "explanation": "Economic Community of West African States (ECOWAS) est la CEDEAO.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Qui est le Secrétaire général de l'ONU en 2026/2027 ?",
    "options": ["A) Ban Ki-moon", "B) Kofi Annan", "C) António Guterres", "D) Boutros Boutros-Ghali"],
    "answer": "C",
    "explanation": "António Guterres est le Secrétaire général de l'ONU.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle est l'institution spécialisée de l'ONU chargée de la réglementation de l'aviation civile internationale ?",
    "options": ["A) OMI", "B) OACI", "C) IATA", "D) OMT"],
    "answer": "B",
    "explanation": "L'Organisation de l'Aviation Civile Internationale (OACI).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Le FMI (Fonds Monétaire International) a été créé lors de la conférence de :",
    "options": ["A) Yalta", "B) Bretton Woods", "C) San Francisco", "D) Paris"],
    "answer": "B",
    "explanation": "Le FMI et la Banque Mondiale sont nés à la Conférence de Bretton Woods en 1944.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Lequel de ces droits n'est pas reconnu par la Déclaration Universelle des Droits de l'Homme ?",
    "options": ["A) Le droit au travail", "B) Le droit à l'éducation", "C) Le droit de polluer", "D) Le droit d'asile"],
    "answer": "C",
    "explanation": "Le droit de polluer n'existe pas dans la DUDH.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Le G5 Sahel comprenait à l'origine :",
    "options": ["A) Mali, Burkina Faso, Niger, Tchad, Mauritanie", "B) Sénégal, Mali, Mauritanie, Niger, Tchad", "C) Burkina Faso, Mali, Niger, Nigeria, Cameroun", "D) Mali, Niger, Burkina Faso, Côte d'Ivoire, Tchad"],
    "answer": "A",
    "explanation": "Le G5 Sahel a été fondé par le Mali, le Burkina Faso, le Niger, le Tchad et la Mauritanie.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle est l'organisation mondiale chargée de la protection des droits de propriété intellectuelle ?",
    "options": ["A) OMC", "B) OMPI", "C) OIT", "D) OIF"],
    "answer": "B",
    "explanation": "L'Organisation Mondiale de la Propriété Intellectuelle (OMPI).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est l'organe judiciaire principal des Nations Unies ?",
    "options": ["A) La Cour Pénale Internationale (CPI)", "B) La Cour Internationale de Justice (CIJ)", "C) Le Tribunal de Nuremberg", "D) La Cour Européenne des Droits de l'Homme"],
    "answer": "B",
    "explanation": "La CIJ est l'organe judiciaire principal de l'ONU, siégeant à La Haye.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel Ivoirien dirige le groupe de la Banque Africaine de Développement (BAD) ?",
    "options": ["A) Tidjane Thiam", "B) Jean-Louis Billon", "C) Akinwumi Adesina", "D) Thierry Tanoh"],
    "answer": "C",
    "explanation": "Piège, Akinwumi Adesina est Nigérian. Il n'y a pas d'Ivoirien à la tête de la BAD actuellement.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de pays africains sont membres fondateurs de l'ONU en 1945 ?",
    "options": ["A) 2", "B) 4", "C) 10", "D) 15"],
    "answer": "B",
    "explanation": "L'Égypte, l'Éthiopie, le Libéria et l'Afrique du Sud étaient les 4 membres fondateurs africains de l'ONU.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le nom de la monnaie unique envisagée par la CEDEAO ?",
    "options": ["A) Le Cauri", "B) L'Afro", "C) L'Eco", "D) Le Cedi"],
    "answer": "C",
    "explanation": "L'Eco est le nom choisi pour la monnaie unique de la CEDEAO.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "What year did the revised ECOWAS treaty, which created the ECOWAS Parliament and Court of Justice, get signed in Cotonou?",
    "options": ["A) 1975", "B) 1981", "C) 1993", "D) 1999"],
    "answer": "C",
    "explanation": "The revised treaty was signed on July 24, 1993.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which specific protocol or treaty established the ECOWAS specialized agency WAHO (West African Health Organization) in 1987, merging OCCGE and WAHC?",
    "options": ["A) Protocol A/P1/7/87", "B) Protocol A/P2/7/87", "C) Treaty of Lagos", "D) Revised Treaty of Cotonou"],
    "answer": "B",
    "explanation": "WAHO was created by Protocol A/P2/7/87 signed in Abuja in 1987.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Where is the headquarters of the African Union Development Agency (AUDA-NEPAD) located?",
    "options": ["A) Addis Ababa", "B) Johannesburg", "C) Midrand", "D) Abuja"],
    "answer": "C",
    "explanation": "AUDA-NEPAD is headquartered in Midrand, South Africa.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which UN specialized agency is responsible for intellectual property services and is headquartered in Geneva?",
    "options": ["A) ITU", "B) WIPO (OMPI)", "C) UPU", "D) WMO (OMM)"],
    "answer": "B",
    "explanation": "The World Intellectual Property Organization (WIPO/OMPI) is based in Geneva.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The African Development Bank (AfDB) approved the Abidjan Urban Transport Project (PTUA). In which year did the AfDB relocate its headquarters temporarily to Tunis before returning to Abidjan?",
    "options": ["A) 1999", "B) 2003", "C) 2011", "D) 2014"],
    "answer": "B",
    "explanation": "The AfDB temporarily relocated to Tunis in 2003 due to the Ivorian Civil War, returning in 2014.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which AU organ is the highest decision-making organ, replacing the OAU Assembly of Heads of State and Government?",
    "options": ["A) The Executive Council", "B) The Pan-African Parliament", "C) The Assembly of the Union", "D) The Peace and Security Council"],
    "answer": "C",
    "explanation": "The Assembly of the Union is the supreme organ of the AU.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "What is the primary function of the Inter-Governmental Action Group against Money Laundering in West Africa (GIABA)?",
    "options": ["A) Public Health", "B) Peacekeeping", "C) Anti-Money Laundering", "D) Telecommunications"],
    "answer": "C",
    "explanation": "GIABA is an ECOWAS institution responsible for strengthening the capacity of member states towards the prevention and control of money laundering.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The World Meteorological Organization (OMM) originated from which former organization created in 1873?",
    "options": ["A) International Meteorological Organization", "B) World Weather Watch", "C) Global Atmospheric Research Program", "D) League of Nations Meteorology Bureau"],
    "answer": "A",
    "explanation": "WMO originated from the International Meteorological Organization (IMO).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Under the ECOWAS Protocol relating to Free Movement of Persons, Residence and Establishment, what is the maximum duration a citizen can stay in a member state without a visa?",
    "options": ["A) 30 days", "B) 60 days", "C) 90 days", "D) 120 days"],
    "answer": "C",
    "explanation": "The Protocol grants community citizens the right to enter and reside in any member state without a visa for up to 90 days.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which UN body has the primary responsibility for the maintenance of international peace and security?",
    "options": ["A) General Assembly", "B) Security Council", "C) Economic and Social Council", "D) International Court of Justice"],
    "answer": "B",
    "explanation": "The UN Security Council holds this primary responsibility.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "In which city is the headquarters of the ECOWAS Bank for Investment and Development (EBID) located?",
    "options": ["A) Abuja", "B) Lome", "C) Abidjan", "D) Dakar"],
    "answer": "B",
    "explanation": "EBID is headquartered in Lome, Togo.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which African Union treaty established the African Continental Free Trade Area (AfCFTA)?",
    "options": ["A) Abuja Treaty", "B) Maputo Protocol", "C) Kigali Declaration", "D) Lagos Plan of Action"],
    "answer": "C",
    "explanation": "The AfCFTA agreement was brokered by the African Union and signed in Kigali on 21 March 2018.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which of the following is NOT an official language of the United Nations?",
    "options": ["A) Arabic", "B) Spanish", "C) Portuguese", "D) Russian"],
    "answer": "C",
    "explanation": "The six official languages of the UN are Arabic, Chinese, English, French, Russian, and Spanish.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Who was the first Secretary-General of the United Nations?",
    "options": ["A) Trygve Lie", "B) Dag Hammarskjold", "C) U Thant", "D) Boutros Boutros-Ghali"],
    "answer": "A",
    "explanation": "Trygve Lie of Norway was the first Secretary-General, serving from 1946 to 1952.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The African Peer Review Mechanism (APRM) is a mutually agreed instrument voluntarily acceded to by the Member States of the African Union. When was it established?",
    "options": ["A) 1999", "B) 2003", "C) 2007", "D) 2010"],
    "answer": "B",
    "explanation": "The APRM was established in 2003 by the NEPAD Heads of State and Government Implementation Committee.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "How many member states currently constitute the Economic Community of West African States (ECOWAS) following the recent withdrawals?",
    "options": ["A) 12", "B) 13", "C) 14", "D) 15"],
    "answer": "A",
    "explanation": "With the withdrawal of Mali, Burkina Faso, and Niger, ECOWAS currently has 12 members (as of 2024).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "What is the acronym for the specialized agency of the UN responsible for information and communication technologies?",
    "options": ["A) ITU", "B) UPU", "C) ICAO", "D) IMO"],
    "answer": "A",
    "explanation": "The International Telecommunication Union (ITU) is the UN specialized agency for ICTs.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Where is the Secretariat of the African Continental Free Trade Area (AfCFTA) located?",
    "options": ["A) Addis Ababa, Ethiopia", "B) Accra, Ghana", "C) Cairo, Egypt", "D) Pretoria, South Africa"],
    "answer": "B",
    "explanation": "The AfCFTA Secretariat is located in Accra, Ghana.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which protocol to the African Charter on Human and Peoples' Rights deals specifically with the Rights of Women in Africa?",
    "options": ["A) Maputo Protocol", "B) Malabo Protocol", "C) Arusha Protocol", "D) Dakar Protocol"],
    "answer": "A",
    "explanation": "The Maputo Protocol guarantees comprehensive rights to women in Africa.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The ECOWAS military force, ECOMOG, was first deployed in 1990 to intervene in the civil war of which member state?",
    "options": ["A) Sierra Leone", "B) Guinea-Bissau", "C) Liberia", "D) Côte d'Ivoire"],
    "answer": "C",
    "explanation": "ECOMOG was first deployed to Liberia in August 1990.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which UN organ consists of 54 members elected by the General Assembly for three-year terms?",
    "options": ["A) Trusteeship Council", "B) Security Council", "C) Economic and Social Council (ECOSOC)", "D) International Court of Justice"],
    "answer": "C",
    "explanation": "ECOSOC consists of 54 members elected for three-year terms.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The African Development Bank (AfDB) Group comprises three distinct entities. Which of the following is NOT one of them?",
    "options": ["A) African Development Bank", "B) African Development Fund", "C) Nigeria Trust Fund", "D) African Finance Corporation"],
    "answer": "D",
    "explanation": "The AfDB Group consists of the AfDB, the ADF, and the NTF. The AFC is a separate entity.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "What is the primary mandate of the West African Health Organization (WAHO)?",
    "options": ["A) Military defense", "B) Economic integration", "C) Health protection and improvement", "D) Educational standardization"],
    "answer": "C",
    "explanation": "WAHO's objective is the attainment of the highest possible standard and protection of health of the peoples in the sub-region.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The Universal Postal Union (UPU), a specialized agency of the UN, is headquartered in which city?",
    "options": ["A) Geneva", "B) Bern", "C) Paris", "D) Vienna"],
    "answer": "B",
    "explanation": "The UPU headquarters is located in Bern, Switzerland.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which AU organ is responsible for the peaceful resolution of conflicts in Africa, established by a protocol adopted in 2002?",
    "options": ["A) Peace and Security Council (PSC)", "B) African Court of Justice", "C) Pan-African Parliament", "D) Economic, Social and Cultural Council (ECOSOCC)"],
    "answer": "A",
    "explanation": "The Peace and Security Council is the standing decision-making organ of the AU for the prevention, management and resolution of conflicts.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The ECOWAS Court of Justice is based in which city?",
    "options": ["A) Lome", "B) Accra", "C) Abuja", "D) Dakar"],
    "answer": "C",
    "explanation": "The ECOWAS Court of Justice is headquartered in Abuja, Nigeria.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which organization preceded the African Union?",
    "options": ["A) Organization of African States", "B) Organization of African Unity", "C) African Economic Community", "D) Pan-African Congress"],
    "answer": "B",
    "explanation": "The Organization of African Unity (OAU) preceded the African Union (AU).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The World Intellectual Property Organization (WIPO) administers several treaties. Which treaty specifically deals with the protection of literary and artistic works?",
    "options": ["A) Paris Convention", "B) Berne Convention", "C) Madrid Agreement", "D) Patent Cooperation Treaty"],
    "answer": "B",
    "explanation": "The Berne Convention, adopted in 1886, deals with the protection of works and the rights of their authors.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "What is the primary currency unit used for accounting by the African Development Bank?",
    "options": ["A) US Dollar", "B) Euro", "C) Unit of Account (UA)", "D) CFA Franc"],
    "answer": "C",
    "explanation": "The AfDB uses the Unit of Account (UA), which is equivalent to the Special Drawing Right (SDR) of the IMF.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which specialized agency of the UN focuses on the promotion of social justice and internationally recognized human and labour rights?",
    "options": ["A) WHO", "B) ILO", "C) UNESCO", "D) FAO"],
    "answer": "B",
    "explanation": "The International Labour Organization (ILO) focuses on labour rights and social justice.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The Lome Peace Agreement of 1999 was brokered by ECOWAS to end the civil war in which country?",
    "options": ["A) Liberia", "B) Sierra Leone", "C) Guinea-Bissau", "D) Côte d'Ivoire"],
    "answer": "B",
    "explanation": "The Lome Peace Agreement was signed in 1999 to end the Sierra Leone Civil War.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The African Union's Agenda 2063 is a strategic framework for the socio-economic transformation of the continent over a 50-year period. When was it adopted?",
    "options": ["A) 2013", "B) 2015", "C) 2000", "D) 2020"],
    "answer": "B",
    "explanation": "Agenda 2063 was adopted by the AU Assembly in January 2015.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which UN agency is tasked with providing humanitarian and developmental aid to children worldwide?",
    "options": ["A) UNESCO", "B) UNICEF", "C) UNHCR", "D) WFP"],
    "answer": "B",
    "explanation": "The United Nations Children's Fund (UNICEF) focuses on aid to children.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The ECOWAS Commission replaced the ECOWAS Secretariat. In what year did this transformation take place?",
    "options": ["A) 1993", "B) 2000", "C) 2007", "D) 2010"],
    "answer": "C",
    "explanation": "The Secretariat was transformed into the Commission in 2007 to enhance the organization's supranational powers.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Where is the International Court of Justice (ICJ), the principal judicial organ of the UN, located?",
    "options": ["A) Geneva", "B) New York", "C) The Hague", "D) Vienna"],
    "answer": "C",
    "explanation": "The ICJ is located at the Peace Palace in The Hague, Netherlands.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The Constitutive Act of the African Union was adopted in which city?",
    "options": ["A) Sirte", "B) Lome", "C) Addis Ababa", "D) Lusaka"],
    "answer": "B",
    "explanation": "The Constitutive Act was adopted in Lome, Togo, on July 11, 2000.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which institution is the supreme audit institution of ECOWAS?",
    "options": ["A) ECOWAS Parliament", "B) ECOWAS Court of Justice", "C) ECOWAS Commission", "D) Office of the Auditor General of ECOWAS"],
    "answer": "D",
    "explanation": "The Office of the Auditor General ensures transparency and accountability in the management of ECOWAS resources.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The World Meteorological Organization (WMO) operates the World Weather Watch. What year was this program launched?",
    "options": ["A) 1950", "B) 1963", "C) 1975", "D) 1980"],
    "answer": "B",
    "explanation": "The World Weather Watch was established in 1963 to combine observing systems, telecommunication facilities, and data-processing.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Who represents Côte d'Ivoire on the Board of Governors of the African Development Bank?",
    "options": ["A) The President of the Republic", "B) The Minister of Economy and Finance", "C) The Governor of the BCEAO", "D) The Minister of Foreign Affairs"],
    "answer": "B",
    "explanation": "Each member country is represented on the AfDB Board of Governors by its Minister of Finance or a similar high-ranking official.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The ECOWAS single currency project adopted a name for its proposed currency. What is this name?",
    "options": ["A) Afro", "B) Cedi", "C) Eco", "D) West African Franc"],
    "answer": "C",
    "explanation": "The proposed single currency for the ECOWAS region is named the Eco.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which organ of the African Union is intended to provide civil society organizations with a platform to be involved in the AU's programs?",
    "options": ["A) The Executive Council", "B) The Pan-African Parliament", "C) The Economic, Social and Cultural Council (ECOSOCC)", "D) The Permanent Representatives Committee"],
    "answer": "C",
    "explanation": "ECOSOCC is an advisory organ composed of different social and professional groups of the member states.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The Food and Agriculture Organization (FAO) of the UN is headquartered in which city?",
    "options": ["A) Geneva", "B) Rome", "C) Paris", "D) New York"],
    "answer": "B",
    "explanation": "The FAO is headquartered in Rome, Italy.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which agreement established the World Intellectual Property Organization (WIPO)?",
    "options": ["A) Paris Convention", "B) Berne Convention", "C) WIPO Convention", "D) TRIPS Agreement"],
    "answer": "C",
    "explanation": "The WIPO Convention, signed in Stockholm in 1967, established WIPO.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The African Development Fund (ADF) provides concessional funding. Which countries are eligible for ADF funding?",
    "options": ["A) All African countries", "B) Only low-income African countries", "C) Only middle-income African countries", "D) Only North African countries"],
    "answer": "B",
    "explanation": "The ADF provides concessional resources to low-income regional member countries.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The ECOWAS Parliament consists of how many seats?",
    "options": ["A) 115", "B) 120", "C) 150", "D) 200"],
    "answer": "A",
    "explanation": "The ECOWAS Parliament, also known as the Community Parliament, has 115 seats.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which UN agency focuses on the regulation of international civil aviation?",
    "options": ["A) IMO", "B) ICAO", "C) ITU", "D) WMO"],
    "answer": "B",
    "explanation": "The International Civil Aviation Organization (ICAO) manages the administration and governance of the Convention on International Civil Aviation.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The African Continental Free Trade Area (AfCFTA) requires member states to remove tariffs from what percentage of goods?",
    "options": ["A) 50%", "B) 70%", "C) 90%", "D) 100%"],
    "answer": "C",
    "explanation": "Members are committed to eliminate tariffs on 90% of goods.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Which specialized agency of the UN is responsible for promoting responsible, sustainable and universally accessible tourism?",
    "options": ["A) UNWTO", "B) UNESCO", "C) UNDP", "D) UNEP"],
    "answer": "A",
    "explanation": "The World Tourism Organization (UNWTO) is the UN agency for tourism.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The headquarters of the West African Health Organization (WAHO) is located in which city?",
    "options": ["A) Abuja", "B) Bobo-Dioulasso", "C) Dakar", "D) Abidjan"],
    "answer": "B",
    "explanation": "WAHO is headquartered in Bobo-Dioulasso, Burkina Faso.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "The United Nations Charter was signed in which year?",
    "options": ["A) 1944", "B) 1945", "C) 1946", "D) 1948"],
    "answer": "B",
    "explanation": "The UN Charter was signed on 26 June 1945 in San Francisco.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "A quelle date le retrait du Mali, du Burkina Faso et du Niger de la CEDEAO est-il devenu effectif ?",
    "options": ["A) 28 janvier 2024", "B) 29 janvier 2025", "C) 15 mars 2024", "D) 1er janvier 2025"],
    "answer": "B",
    "explanation": "Le retrait est effectif un an après l'annonce (28 janvier 2024).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Comment s'appelle l'organisation créée par le Mali, le Burkina Faso et le Niger suite à leur retrait de la CEDEAO ?",
    "options": ["A) G5 Sahel", "B) Alliance des États du Sahel (AES)", "C) Union du Fleuve Mano", "D) Liptako-Gourma unifié"],
    "answer": "B",
    "explanation": "L'AES a été formée puis transformée en confédération en 2024.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est le siège de la Commission de la CEDEAO ?",
    "options": ["A) Lomé", "B) Dakar", "C) Abuja", "D) Accra"],
    "answer": "C",
    "explanation": "Le siège de la CEDEAO est à Abuja au Nigeria.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Malgré leur retrait de la CEDEAO, le Mali, le Burkina Faso et le Niger sont-ils restés membres de l'UEMOA en 2025 ?",
    "options": ["A) Non, ils ont créé leur propre monnaie", "B) Oui, ils ont maintenu leur adhésion à l'UEMOA", "C) Seulement le Mali est resté", "D) Ils ont été suspendus définitivement"],
    "answer": "B",
    "explanation": "Ils n'ont pas quitté l'UEMOA ni la zone Franc CFA en 2025.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de la Commission de l'UEMOA ?",
    "options": ["A) Ouagadougou", "B) Dakar", "C) Abidjan", "D) Bamako"],
    "answer": "A",
    "explanation": "Le siège de l'UEMOA est à Ouagadougou.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de la BCEAO ?",
    "options": ["A) Ouagadougou", "B) Dakar", "C) Abidjan", "D) Lomé"],
    "answer": "B",
    "explanation": "Le siège de la Banque Centrale des États de l'Afrique de l'Ouest est à Dakar.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de l'Union Africaine (UA) ?",
    "options": ["A) Johannesburg", "B) Addis-Abeba", "C) Nairobi", "D) Le Caire"],
    "answer": "B",
    "explanation": "Le siège de l'UA est en Éthiopie.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Comment s'appelle la feuille de route stratégique de l'Union Africaine pour le développement du continent ?",
    "options": ["A) Vision 2030", "B) Agenda 2063", "C) Plan NEPAD 2050", "D) Initiative Afrique 21"],
    "answer": "B",
    "explanation": "C'est l'Agenda 2063 : L'Afrique que nous voulons.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'Union Africaine a succédé à quelle organisation en 2002 ?",
    "options": ["A) L'Organisation de l'Unité Africaine (OUA)", "B) La Communauté Économique Africaine", "C) Le NEPAD", "D) L'Union Panafricaine"],
    "answer": "A",
    "explanation": "L'OUA a été remplacée par l'UA en 2002.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de membres permanents le Conseil de Sécurité de l'ONU compte-il ?",
    "options": ["A) 5", "B) 10", "C) 15", "D) 193"],
    "answer": "A",
    "explanation": "Il y a 5 membres permanents avec droit de véto.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Parmi ces pays, lequel N'EST PAS un membre permanent du Conseil de Sécurité de l'ONU ?",
    "options": ["A) France", "B) Royaume-Uni", "C) Allemagne", "D) Russie"],
    "answer": "C",
    "explanation": "Les 5 sont: USA, Russie, Chine, France, Royaume-Uni.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Qui est le Secrétaire Général de l'ONU en 2025 ?",
    "options": ["A) Ban Ki-moon", "B) Kofi Annan", "C) António Guterres", "D) Boutros Boutros-Ghali"],
    "answer": "C",
    "explanation": "António Guterres est en poste depuis 2017.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de l'OMS ?",
    "options": ["A) Genève", "B) Vienne", "C) Washington", "D) Paris"],
    "answer": "A",
    "explanation": "L'Organisation Mondiale de la Santé siège à Genève.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle agence spécialisée de l'ONU a son siège à Paris ?",
    "options": ["A) L'UNICEF", "B) L'UNESCO", "C) Le HCR", "D) L'OIT"],
    "answer": "B",
    "explanation": "L'Organisation pour l'éducation, la science et la culture est à Paris.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où siège la Banque Africaine de Développement (BAD) ?",
    "options": ["A) Tunis", "B) Dakar", "C) Abidjan", "D) Pretoria"],
    "answer": "C",
    "explanation": "Le siège statutaire de la BAD est à Abidjan, Côte d'Ivoire.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Qui est le Président de la Banque Africaine de Développement dont le second mandat se termine en 2025 ?",
    "options": ["A) Donald Kaberuka", "B) Akinwumi Adesina", "C) Tidjane Thiam", "D) Ngozi Okonjo-Iweala"],
    "answer": "B",
    "explanation": "Le Nigérian Akinwumi Adesina a été réélu en 2020 pour 5 ans.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En quelle année le second mandat d'António Guterres à la tête de l'ONU se termine-t-il ?",
    "options": ["A) 2025", "B) 2026", "C) 2027", "D) 2030"],
    "answer": "B",
    "explanation": "Son second mandat s'achève le 31 décembre 2026.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel traité a institué la CEDEAO en 1975 ?",
    "options": ["A) Traité de Lagos", "B) Traité d'Abuja", "C) Traité de Dakar", "D) Traité de Niamey"],
    "answer": "A",
    "explanation": "La CEDEAO a été créée par le Traité de Lagos le 28 mai 1975.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle est l'agence de l'ONU basée à Montréal ?",
    "options": ["A) OMI", "B) OACI", "C) OMPI", "D) UPU"],
    "answer": "B",
    "explanation": "L'Organisation de l'aviation civile internationale siège à Montréal.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège de l'Organisation Maritime Internationale (OMI) ?",
    "options": ["A) Hambourg", "B) Londres", "C) Athènes", "D) Genève"],
    "answer": "B",
    "explanation": "L'OMI a son siège à Londres.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel accord lie les pays d'Afrique, des Caraïbes et du Pacifique (ACP) à l'Union Européenne depuis 2023, remplaçant l'accord de Cotonou ?",
    "options": ["A) L'Accord de Lomé", "B) L'Accord des Samoa", "C) L'Accord de Bruxelles", "D) L'Accord de Dakar"],
    "answer": "B",
    "explanation": "L'Accord de Samoa a remplacé l'Accord de Cotonou.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel impact majeur le Brexit a-t-il eu sur le rôle du Royaume-Uni dans le Commonwealth ?",
    "options": ["A) Le Royaume-Uni a quitté le Commonwealth", "B) Le Royaume-Uni a recentré ses accords commerciaux sur les pays du Commonwealth", "C) Le Commonwealth a été dissous", "D) Les pays du Commonwealth ont imposé des visas aux Britanniques"],
    "answer": "B",
    "explanation": "Après le Brexit, le RU a cherché à renforcer ses liens avec le Commonwealth (Global Britain).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'Organisation Mondiale de la Propriété Intellectuelle (OMPI) est basée à :",
    "options": ["A) Paris", "B) New York", "C) Genève", "D) Vienne"],
    "answer": "C",
    "explanation": "L'OMPI est une institution spécialisée des Nations Unies basée à Genève.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle cour de justice est l'organe judiciaire principal de l'ONU ?",
    "options": ["A) La Cour Pénale Internationale (CPI)", "B) La Cour Internationale de Justice (CIJ)", "C) Le Tribunal de La Haye", "D) La Cour Européenne des Droits de l'Homme"],
    "answer": "B",
    "explanation": "La CIJ est l'organe judiciaire de l'ONU. La CPI est indépendante.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "La CPI (Cour Pénale Internationale) fait-elle partie du système de l'ONU ?",
    "options": ["A) Oui, c'est une agence spécialisée", "B) Non, c'est une organisation internationale indépendante", "C) Oui, elle remplace la CIJ", "D) Non, elle dépend de l'Union Européenne"],
    "answer": "B",
    "explanation": "Bien qu'elle coopère avec l'ONU, la CPI a été créée par le Statut de Rome et est indépendante.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel statut l'État de Palestine a-t-il obtenu à l'ONU en 2012, réaffirmé dans les récents débats de 2024-2025 ?",
    "options": ["A) Membre à part entière", "B) État observateur non membre", "C) Membre du Conseil de Sécurité", "D) Territoire sous tutelle"],
    "answer": "B",
    "explanation": "La Palestine est un État observateur non membre à l'Assemblée générale.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Parmi ces organisations, laquelle n'est pas une institution spécialisée de l'ONU ?",
    "options": ["A) Le FMI", "B) Le Groupe de la Banque Mondiale", "C) L'OMC", "D) L'OIT"],
    "answer": "C",
    "explanation": "L'Organisation Mondiale du Commerce n'est pas une agence spécialisée de l'ONU, bien qu'elles coopèrent.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Dans le cadre des réformes débattues en 2025, quel continent revendique au moins deux sièges permanents avec droit de veto au Conseil de sécurité de l'ONU (Consensus d'Ezulwini) ?",
    "options": ["A) L'Amérique du Sud", "B) L'Afrique", "C) L'Asie", "D) L'Océanie"],
    "answer": "B",
    "explanation": "Le Consensus d'Ezulwini est la position commune africaine revendiquant des sièges permanents.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel traité fonde l'Union Européenne telle qu'on la connaît aujourd'hui, entré en vigueur en 1993 ?",
    "options": ["A) Traité de Rome", "B) Traité de Maastricht", "C) Traité de Lisbonne", "D) Traité d'Amsterdam"],
    "answer": "B",
    "explanation": "Le Traité de Maastricht a institué l'Union Européenne.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Le G20 est composé de 19 pays et de deux unions d'États. Lesquelles ?",
    "options": ["A) L'UE et l'ALENA", "B) L'UE et l'Union Africaine", "C) L'ASEAN et l'UE", "D) Le Mercosur et l'Union Africaine"],
    "answer": "B",
    "explanation": "L'Union Africaine a été admise comme membre permanent du G20 en 2023.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle est l'institution de l'UEMOA chargée de contrôler les comptes de l'Union ?",
    "options": ["A) La Commission de l'UEMOA", "B) La Cour de Justice", "C) La Cour des Comptes", "D) Le Parlement de l'UEMOA"],
    "answer": "C",
    "explanation": "La Cour des Comptes de l'UEMOA contrôle les finances de l'Union.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Qui a été élu Secrétaire Général de l'Organisation Internationale de la Francophonie (OIF) en 2018, puis réélue ?",
    "options": ["A) Michaëlle Jean", "B) Louise Mushikiwabo", "C) Abdou Diouf", "D) Boutros Boutros-Ghali"],
    "answer": "B",
    "explanation": "La Rwandaise Louise Mushikiwabo dirige l'OIF.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où est le siège de l'OIF ?",
    "options": ["A) Paris", "B) Genève", "C) Bruxelles", "D) Dakar"],
    "answer": "A",
    "explanation": "L'OIF siège à Paris.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "En 2024, quel nouveau pays a officiellement rejoint les BRICS, aux côtés de l'Égypte, de l'Éthiopie, de l'Iran et des EAU ?",
    "options": ["A) L'Argentine", "B) L'Arabie Saoudite", "C) Le Nigeria", "D) Le Mexique"],
    "answer": "B",
    "explanation": "L'Arabie Saoudite a été invitée et a rejoint les BRICS (bien que l'Argentine ait décliné sous Milei).",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Combien de pays forment l'Alliance des États du Sahel (AES) ?",
    "options": ["A) 2", "B) 3", "C) 4", "D) 5"],
    "answer": "B",
    "explanation": "Le Mali, le Burkina Faso et le Niger.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'Agence Internationale de l'Énergie Atomique (AIEA) est basée à :",
    "options": ["A) Genève", "B) Vienne", "C) New York", "D) Londres"],
    "answer": "B",
    "explanation": "L'AIEA siège en Autriche à Vienne.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Le Programme des Nations Unies pour le Développement (PNUD) est dirigé par un :",
    "options": ["A) Directeur Général", "B) Administrateur", "C) Secrétaire Général", "D) Président"],
    "answer": "B",
    "explanation": "Le chef du PNUD porte le titre d'Administrateur.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Le siège de la Cour Pénale Internationale (CPI) est à :",
    "options": ["A) La Haye", "B) Genève", "C) New York", "D) Rome"],
    "answer": "A",
    "explanation": "La CPI, bien qu'issue du Statut de Rome, siège à La Haye aux Pays-Bas.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Le siège d'INTERPOL se trouve en France. Dans quelle ville ?",
    "options": ["A) Paris", "B) Lyon", "C) Marseille", "D) Strasbourg"],
    "answer": "B",
    "explanation": "Interpol est basé à Lyon.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'ALENA (NAFTA), l'accord de libre-échange nord-américain, a été remplacé par :",
    "options": ["A) L'USMCA (AEUMC)", "B) Le MERCOSUR", "C) L'AELC", "D) Le Partenariat Transpacifique"],
    "answer": "A",
    "explanation": "L'Accord États-Unis-Mexique-Canada a remplacé l'ALENA en 2020.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Où se trouve le siège du Parlement Européen (les sessions plénières) ?",
    "options": ["A) Bruxelles", "B) Strasbourg", "C) Luxembourg", "D) Francfort"],
    "answer": "B",
    "explanation": "Le siège officiel pour les sessions plénières est à Strasbourg.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle est l'institution de l'ONU qui réunit tous les États membres (193 en 2025) ?",
    "options": ["A) Le Conseil de Sécurité", "B) L'Assemblée Générale", "C) L'ECOSOC", "D) Le Secrétariat"],
    "answer": "B",
    "explanation": "L'AG regroupe tous les États membres avec une voix chacun.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quel est l'objectif principal de la ZLECAf ?",
    "options": ["A) Créer une monnaie unique africaine", "B) Créer une Zone de Libre-Échange Continentale Africaine", "C) Lutter contre le terrorisme au Sahel", "D) Unifier les armées africaines"],
    "answer": "B",
    "explanation": "La ZLECAf vise à créer un marché unique pour les biens et services en Afrique.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'Organisation de la Coopération Islamique (OCI) siège à :",
    "options": ["A) Riyad", "B) Djeddah", "C) Doha", "D) Istanbul"],
    "answer": "B",
    "explanation": "Le siège de l'OCI est à Djeddah en Arabie Saoudite.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Le Conseil de l'Europe (qui n'est pas une institution de l'UE) siège à :",
    "options": ["A) Bruxelles", "B) Genève", "C) Strasbourg", "D) La Haye"],
    "answer": "C",
    "explanation": "Le Conseil de l'Europe, garant de la Cour EDH, siège à Strasbourg.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "L'OPEP (Organisation des Pays Exportateurs de Pétrole) a son siège à :",
    "options": ["A) Riyad", "B) Vienne", "C) Dubaï", "D) Caracas"],
    "answer": "B",
    "explanation": "Bien qu'aucun pays européen ne soit membre, le siège est à Vienne, Autriche.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle organisation africaine a été suspendue de la CEDEAO en 2022 et s'en est finalement retirée ?",
    "options": ["A) La Mauritanie", "B) Le Mali", "C) Le Sénégal", "D) Le Togo"],
    "answer": "B",
    "explanation": "Le Mali s'est retiré de la CEDEAO aux côtés du Burkina et du Niger.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Quelle cour a son siège à Arusha, Tanzanie, et est un organe de l'Union Africaine ?",
    "options": ["A) La Cour africaine des droits de l'homme et des peuples", "B) La Cour de justice de la CEDEAO", "C) La Cour suprême panafricaine", "D) Le Tribunal pénal international pour le Rwanda"],
    "answer": "A",
    "explanation": "La CADHP siège à Arusha.",
    "theme": "Organisations Internationales"
  },
  {
    "question": "Complete: 'If I ___ you, I would apologize.'",
    "options": ["A) am", "B) was", "C) were", "D) be"],
    "answer": "C",
    "explanation": "Type 2 conditional uses 'were' for all persons with the verb 'to be'.",
    "theme": "English Grammar"
  },
  {
    "question": "Which sentence is correct?",
    "options": ["A) If it will rain, I stay home", "B) If it rains, I will stay home", "C) If it rains, I would stay home"],
    "answer": "B",
    "explanation": "Type 1 conditional: never use 'will' immediately after 'if'. Structure: If + Present, will + verb.",
    "theme": "English Grammar"
  },
  {
    "question": "'You ___ park here. It's forbidden.'",
    "options": ["A) mustn't", "B) needn't", "C) shouldn't", "D) can't"],
    "answer": "A",
    "explanation": "'Mustn't' expresses prohibition (interdiction). 'Needn't' means no obligation.",
    "theme": "English Grammar"
  },
  {
    "question": "Choose the correct article: 'She is ___ honest woman.'",
    "options": ["A) a", "B) an", "C) the", "D) Ø"],
    "answer": "B",
    "explanation": "Use 'an' before words starting with a vowel SOUND. 'Honest' starts with a silent 'h'.",
    "theme": "English Grammar"
  },
  {
    "question": "'I travel ___ bus every day.'",
    "options": ["A) by", "B) on the", "C) in a", "D) with"],
    "answer": "A",
    "explanation": "'By' + means of transport (without article) is used for general transport.",
    "theme": "English Grammar"
  },
  {
    "question": "'If I had known, I ___ differently.'",
    "options": ["A) would act", "B) would have acted", "C) will act", "D) acted"],
    "answer": "B",
    "explanation": "Type 3 conditional (past regret): If + Past Perfect → Would have + Past Participle.",
    "theme": "English Grammar"
  },
  {
    "question": "'You ___ come if you don't want to.'",
    "options": ["A) mustn't", "B) don't have to", "C) can't", "D) shouldn't"],
    "answer": "B",
    "explanation": "'Don't have to' expresses absence of obligation. 'Mustn't' is prohibition.",
    "theme": "English Grammar"
  },
  {
    "question": "Which preposition? 'The meeting is ___ Monday.'",
    "options": ["A) at", "B) in", "C) on", "D) by"],
    "answer": "C",
    "explanation": "Use 'on' for specific days: on Monday, on Tuesday, on my birthday.",
    "theme": "English Grammar"
  },
  {
    "question": "'She ___ speak three languages.' (Present ability)",
    "options": ["A) can", "B) could", "C) may", "D) might"],
    "answer": "A",
    "explanation": "'Can' expresses ability in the present. 'Could' is past or politeness.",
    "theme": "English Grammar"
  },
  {
    "question": "'___ water boils at 100°C.'",
    "options": ["A) A", "B) The", "C) Ø (no article)", "D) An"],
    "answer": "C",
    "explanation": "No article for general truths with uncountable nouns like 'water'.",
    "theme": "English Grammar"
  },
  {
    "question": "'If water reaches 0°C, it ___.'",
    "options": ["A) freezes", "B) will freeze", "C) would freeze", "D) freeze"],
    "answer": "A",
    "explanation": "Type Zero conditional (general truth): If + Present → Present.",
    "theme": "English Grammar"
  },
  {
    "question": "'He ___ be at home. His car is in the driveway.' (Deduction)",
    "options": ["A) might", "B) must", "C) should", "D) can"],
    "answer": "B",
    "explanation": "'Must' expresses strong deduction/logical certainty (quasi-certitude).",
    "theme": "English Grammar"
  },
  {
    "question": "'I was sitting ___ the train when I saw him.'",
    "options": ["A) by", "B) in", "C) on", "D) at"],
    "answer": "C",
    "explanation": "'On' is used for public transport: on the bus, on the train, on the plane.",
    "theme": "English Grammar"
  },
  {
    "question": "'You ___ to see a doctor. You look ill.' (Advice)",
    "options": ["A) ought", "B) must", "C) might", "D) need"],
    "answer": "A",
    "explanation": "'Ought to' expresses advice/recommendation (conseil).",
    "theme": "English Grammar"
  },
  {
    "question": "'___ dogs are loyal animals.'",
    "options": ["A) A", "B) The", "C) Ø (no article)", "D) An"],
    "answer": "C",
    "explanation": "No article for general statements with plural nouns.",
    "theme": "English Grammar"
  },
  {
    "question": "'The concert is ___ 8 PM.'",
    "options": ["A) at", "B) in", "C) on", "D) by"],
    "answer": "A",
    "explanation": "Use 'at' for precise times: at 8 PM, at noon, at midnight.",
    "theme": "English Grammar"
  },
  {
    "question": "'If she ___ harder, she would pass the exam.'",
    "options": ["A) studies", "B) studied", "C) will study", "D) study"],
    "answer": "B",
    "explanation": "Type 2 conditional (imaginary present): If + Past Simple → Would + verb.",
    "theme": "English Grammar"
  },
  {
    "question": "'He travels to work ___ car.'",
    "options": ["A) by", "B) in", "C) on", "D) with"],
    "answer": "A",
    "explanation": "'By car' (no article) for general transport method. 'In a car' for specific vehicle.",
    "theme": "English Grammar"
  },
  {
    "question": "'It ___ rain later. Take an umbrella.' (Possibility ~50%)",
    "options": ["A) must", "B) may", "C) should", "D) will"],
    "answer": "B",
    "explanation": "'May' expresses possibility (~50% probability).",
    "theme": "English Grammar"
  },
  {
    "question": "'My birthday is ___ July 15th.'",
    "options": ["A) at", "B) in", "C) on", "D) by"],
    "answer": "C",
    "explanation": "Use 'on' for specific dates: on July 15th, on December 25th.",
    "theme": "English Grammar"
  },
  {
    "question": "'She has lived here ___ 2010.'",
    "options": ["A) since", "B) for", "C) during", "D) from"],
    "answer": "A",
    "explanation": "'Since' is used with a specific point in time (depuis 2010).",
    "theme": "English Grammar"
  },
  {
    "question": "'I have studied English ___ five years.'",
    "options": ["A) since", "B) for", "C) during", "D) ago"],
    "answer": "B",
    "explanation": "'For' is used with a duration (pendant 5 ans).",
    "theme": "English Grammar"
  },
  {
    "question": "'I visited Paris three years ___.'",
    "options": ["A) since", "B) for", "C) ago", "D) before"],
    "answer": "C",
    "explanation": "'Ago' is used with past simple for a point in the past (il y a 3 ans).",
    "theme": "English Grammar"
  },
  {
    "question": "'He ___ finished his homework yet.'",
    "options": ["A) hasn't", "B) didn't", "C) doesn't", "D) wasn't"],
    "answer": "A",
    "explanation": "'Yet' with present perfect negative: hasn't/haven't + past participle.",
    "theme": "English Grammar"
  },
  {
    "question": "'Have you ___ been to Japan?'",
    "options": ["A) yet", "B) ever", "C) already", "D) never"],
    "answer": "B",
    "explanation": "'Ever' is used in questions with present perfect (déjà dans ta vie).",
    "theme": "English Grammar"
  },
  {
    "question": "'I have ___ finished my work.'",
    "options": ["A) yet", "B) ever", "C) already", "D) ago"],
    "answer": "C",
    "explanation": "'Already' with present perfect affirmative: have already + past participle.",
    "theme": "English Grammar"
  },
  {
    "question": "'Neither John ___ Mary came to the party.'",
    "options": ["A) or", "B) nor", "C) and", "D) but"],
    "answer": "B",
    "explanation": "'Neither...nor' is the correct correlative conjunction.",
    "theme": "English Grammar"
  },
  {
    "question": "'Either you apologize, ___ I will leave.'",
    "options": ["A) and", "B) but", "C) or", "D) nor"],
    "answer": "C",
    "explanation": "'Either...or' expresses a choice/alternative.",
    "theme": "English Grammar"
  },
  {
    "question": "'She is not only intelligent ___ also kind.'",
    "options": ["A) and", "B) but", "C) or", "D) yet"],
    "answer": "B",
    "explanation": "'Not only...but also' is the correct correlative conjunction.",
    "theme": "English Grammar"
  },
  {
    "question": "'I would rather ___ at home today.'",
    "options": ["A) stay", "B) to stay", "C) staying", "D) stayed"],
    "answer": "A",
    "explanation": "'Would rather' is followed by base form (infinitive without 'to').",
    "theme": "English Grammar"
  },
  {
    "question": "'She made me ___ my homework.'",
    "options": ["A) do", "B) to do", "C) doing", "D) did"],
    "answer": "A",
    "explanation": "'Make' is followed by object + base form (without 'to').",
    "theme": "English Grammar"
  },
  {
    "question": "'He let me ___ his car.'",
    "options": ["A) use", "B) to use", "C) using", "D) used"],
    "answer": "A",
    "explanation": "'Let' is followed by object + base form (without 'to').",
    "theme": "English Grammar"
  },
  {
    "question": "'She wants me ___ her.'",
    "options": ["A) help", "B) to help", "C) helping", "D) helped"],
    "answer": "B",
    "explanation": "'Want' is followed by object + to-infinitive.",
    "theme": "English Grammar"
  },
  {
    "question": "'I'm looking forward ___ you.'",
    "options": ["A) see", "B) to see", "C) to seeing", "D) seeing"],
    "answer": "C",
    "explanation": "'Look forward to' is followed by gerund (verb + -ing).",
    "theme": "English Grammar"
  },
  {
    "question": "'He is used ___ early.'",
    "options": ["A) wake up", "B) to wake up", "C) to waking up", "D) waking up"],
    "answer": "C",
    "explanation": "'Be used to' (être habitué à) is followed by gerund.",
    "theme": "English Grammar"
  },
  {
    "question": "'He used ___ in London.'",
    "options": ["A) live", "B) to live", "C) living", "D) lived"],
    "answer": "B",
    "explanation": "'Used to' (habitude passée) is followed by base form.",
    "theme": "English Grammar"
  },
  {
    "question": "'The book ___ by millions of people.'",
    "options": ["A) was read", "B) read", "C) is reading", "D) reads"],
    "answer": "A",
    "explanation": "Passive voice (past): was/were + past participle.",
    "theme": "English Grammar"
  },
  {
    "question": "'The house ___ built in 1990.'",
    "options": ["A) is", "B) was", "C) has", "D) had"],
    "answer": "B",
    "explanation": "Passive voice with specific past date uses 'was/were'.",
    "theme": "English Grammar"
  },
  {
    "question": "'English ___ all over the world.'",
    "options": ["A) speaks", "B) is spoken", "C) is speaking", "D) has spoken"],
    "answer": "B",
    "explanation": "Passive voice (present): is/are + past participle.",
    "theme": "English Grammar"
  },
  {
    "question": "'I wish I ___ rich.'",
    "options": ["A) am", "B) was", "C) were", "D) be"],
    "answer": "C",
    "explanation": "'I wish' + past tense for present unreal situation. Use 'were' for 'to be'.",
    "theme": "English Grammar"
  },
  {
    "question": "'I wish I ___ studied harder.' (Past regret)",
    "options": ["A) have", "B) had", "C) would", "D) could"],
    "answer": "B",
    "explanation": "'I wish' + past perfect for past regret.",
    "theme": "English Grammar"
  },
  {
    "question": "'If only I ___ more time!'",
    "options": ["A) have", "B) had", "C) will have", "D) would have"],
    "answer": "B",
    "explanation": "'If only' + past tense for present wish/regret.",
    "theme": "English Grammar"
  },
  {
    "question": "'He asked me where I ___.'",
    "options": ["A) live", "B) lived", "C) am living", "D) lives"],
    "answer": "B",
    "explanation": "Reported speech: present → past (backshift).",
    "theme": "English Grammar"
  },
  {
    "question": "'She said she ___ come tomorrow.'",
    "options": ["A) will", "B) would", "C) can", "D) may"],
    "answer": "B",
    "explanation": "Reported speech: 'will' becomes 'would'.",
    "theme": "English Grammar"
  },
  {
    "question": "'There ___ many people at the party yesterday.'",
    "options": ["A) was", "B) were", "C) is", "D) are"],
    "answer": "B",
    "explanation": "'There were' for plural subjects in the past.",
    "theme": "English Grammar"
  },
  {
    "question": "'There ___ a problem with the system.'",
    "options": ["A) is", "B) are", "C) was", "D) were"],
    "answer": "A",
    "explanation": "'There is' for singular subjects in the present.",
    "theme": "English Grammar"
  },
  {
    "question": "'Few people ___ the answer.'",
    "options": ["A) knows", "B) know", "C) knowing", "D) knew"],
    "answer": "B",
    "explanation": "'Few people' is plural, so use 'know' (no -s).",
    "theme": "English Grammar"
  },
  {
    "question": "'Each student ___ a book.'",
    "options": ["A) have", "B) has", "C) having", "D) are having"],
    "answer": "B",
    "explanation": "'Each' is singular, so use 'has'.",
    "theme": "English Grammar"
  },
  {
    "question": "'Neither of the answers ___ correct.'",
    "options": ["A) is", "B) are", "C) were", "D) being"],
    "answer": "A",
    "explanation": "'Neither' is singular, so use 'is'.",
    "theme": "English Grammar"
  },
  {
    "question": "'The team ___ playing well.' (as a unit)",
    "options": ["A) is", "B) are", "C) was", "D) were"],
    "answer": "A",
    "explanation": "Collective nouns can be singular (unit) or plural (individuals). Here, 'is' for unit.",
    "theme": "English Grammar"
  },
  {
    "question": "'She is ___ than her sister.' (intelligent)",
    "options": ["A) more intelligent", "B) most intelligent", "C) intelligenter", "D) more intelligenter"],
    "answer": "A",
    "explanation": "Long adjectives use 'more' for comparatives: more intelligent.",
    "theme": "English Grammar"
  },
  {
    "question": "'He is the ___ student in the class.'",
    "options": ["A) most tallest", "B) tallest", "C) more tall", "D) taller"],
    "answer": "B",
    "explanation": "Short adjectives use '-est' for superlatives: the tallest.",
    "theme": "English Grammar"
  },
  {
    "question": "'You like coffee, ___?'",
    "options": ["A) don't you", "B) do you", "C) isn't it", "D) aren't you"],
    "answer": "A",
    "explanation": "Question tags: positive statement → negative tag. 'You like' → 'don't you?'",
    "theme": "English Grammar"
  },
  {
    "question": "'She can't swim, ___?'",
    "options": ["A) can't she", "B) can she", "C) could she", "D) does she"],
    "answer": "B",
    "explanation": "Question tags: negative statement → positive tag. 'Can't swim' → 'can she?'",
    "theme": "English Grammar"
  },
  {
    "question": "'The man ___ lives next door is a doctor.'",
    "options": ["A) which", "B) who", "C) whom", "D) whose"],
    "answer": "B",
    "explanation": "'Who' is used for people as subject in relative clauses.",
    "theme": "English Grammar"
  },
  {
    "question": "'The book ___ I read was fascinating.'",
    "options": ["A) who", "B) which", "C) whose", "D) whom"],
    "answer": "B",
    "explanation": "'Which' (or 'that') is used for things in relative clauses.",
    "theme": "English Grammar"
  },
  {
    "question": "'The girl ___ father is a pilot studies here.'",
    "options": ["A) who", "B) which", "C) whose", "D) whom"],
    "answer": "C",
    "explanation": "'Whose' indicates possession in relative clauses.",
    "theme": "English Grammar"
  },
  {
    "question": "'If I ___ about the meeting, I would have attended.'",
    "options": ["A) know", "B) knew", "C) had known", "D) have known"],
    "answer": "C",
    "explanation": "Type 3 conditional: If + Past Perfect → Would have + Past Participle.",
    "theme": "English Grammar"
  },
  {
    "question": "'She asked me ___ I was going.'",
    "options": ["A) where", "B) that", "C) what", "D) if"],
    "answer": "A",
    "explanation": "Reported questions with 'wh-' words keep the question word: 'Where are you going?' → 'where I was going.'",
    "theme": "English Grammar"
  },
  {
    "question": "'He told me ___ he would come.'",
    "options": ["A) what", "B) that", "C) if", "D) where"],
    "answer": "B",
    "explanation": "Reported statements use 'that' (optional): He said, 'I will come' → He told me that he would come.",
    "theme": "English Grammar"
  },
  {
    "question": "Choose the correct sentence:",
    "options": ["A) He suggested to go out", "B) He suggested going out", "C) He suggested go out", "D) He suggested that going out"],
    "answer": "B",
    "explanation": "'Suggest' is followed by gerund (verb + -ing) or 'that + subject + base form'.",
    "theme": "English Grammar"
  },
  {
    "question": "'I ___ up at 6 AM every day.' (habitual action)",
    "options": ["A) wake", "B) woke", "C) waken", "D) waking"],
    "answer": "A",
    "explanation": "Present simple for habitual actions: I wake up every day.",
    "theme": "English Grammar"
  },
  {
    "question": "'By next year, I ___ here for ten years.'",
    "options": ["A) will work", "B) will have worked", "C) will be working", "D) work"],
    "answer": "B",
    "explanation": "Future perfect: 'will have + past participle' for actions completed before a future point.",
    "theme": "English Grammar"
  },
  {
    "question": "'She enjoys ___ books in her free time.'",
    "options": ["A) read", "B) to read", "C) reading", "D) reads"],
    "answer": "C",
    "explanation": "'Enjoy' is always followed by gerund (verb + -ing).",
    "theme": "English Grammar"
  },
  {
    "question": "'He avoided ___ the question.'",
    "options": ["A) answer", "B) to answer", "C) answering", "D) answered"],
    "answer": "C",
    "explanation": "'Avoid' is followed by gerund. Some verbs require -ing form.",
    "theme": "English Grammar"
  },
  {
    "question": "'Despite ___ hard, he failed the exam.'",
    "options": ["A) study", "B) to study", "C) studying", "D) studied"],
    "answer": "C",
    "explanation": "'Despite' is followed by a noun or gerund: despite studying hard.",
    "theme": "English Grammar"
  },
  {
    "question": "'I'm not ___ tall ___ my brother.'",
    "options": ["A) so...than", "B) as...as", "C) more...than", "D) so...so"],
    "answer": "B",
    "explanation": "'As...as' is used for comparisons of equality (or inequality with 'not').",
    "theme": "English Grammar"
  },
  {
    "question": "'The more you study, the ___ you learn.'",
    "options": ["A) much", "B) more", "C) most", "D) many"],
    "answer": "B",
    "explanation": "'The more...the more' is a correlative comparative structure.",
    "theme": "English Grammar"
  },
  {
    "question": "'He ___ to the gym three times a week.' (regular habit)",
    "options": ["A) is going", "B) goes", "C) go", "D) going"],
    "answer": "B",
    "explanation": "Present simple for regular habits: He goes (third person -s).",
    "theme": "English Grammar"
  },
  {
    "question": "'We arrived ___ the airport ___ time.'",
    "options": ["A) at / on", "B) in / on", "C) at / in", "D) to / at"],
    "answer": "A",
    "explanation": "'Arrive at' + specific place, 'on time' = à l'heure.",
    "theme": "English Grammar"
  },
  {
    "question": "'I have been living here ___ January.'",
    "options": ["A) for", "B) since", "C) during", "D) from"],
    "answer": "B",
    "explanation": "'Since' + specific point in time (since January). 'For' + duration.",
    "theme": "English Grammar"
  },
  {
    "question": "Choose the correct article: '___ university is a place of learning.'",
    "options": ["A) An", "B) A", "C) The", "D) Ø"],
    "answer": "B",
    "explanation": "'A' before 'university' because the first sound is /juː/ (consonant sound), not a vowel sound.",
    "theme": "English Grammar"
  },
  {
    "question": "'He ___ be tired. He has been working all day.' (logical deduction)",
    "options": ["A) can", "B) may", "C) must", "D) should"],
    "answer": "C",
    "explanation": "'Must' for strong logical deduction based on evidence.",
    "theme": "English Grammar"
  },
  {
    "question": "'They ___ have left already. The lights are off.' (deduction about past)",
    "options": ["A) can", "B) must", "C) should", "D) would"],
    "answer": "B",
    "explanation": "'Must have + past participle' for deductions about the past.",
    "theme": "English Grammar"
  },
  {
    "question": "'I ___ dinner when the phone rang.'",
    "options": ["A) cooked", "B) was cooking", "C) have cooked", "D) cook"],
    "answer": "B",
    "explanation": "Past continuous for an ongoing action interrupted by another event.",
    "theme": "English Grammar"
  },
  {
    "question": "'She ___ for two hours when he arrived.'",
    "options": ["A) waited", "B) was waiting", "C) had been waiting", "D) has waited"],
    "answer": "C",
    "explanation": "Past perfect continuous for a duration before a past event: had been + -ing.",
    "theme": "English Grammar"
  },
  {
    "question": "'How ___ sugar do you need?'",
    "options": ["A) many", "B) much", "C) few", "D) several"],
    "answer": "B",
    "explanation": "'Much' for uncountable nouns. 'Many' for countable nouns.",
    "theme": "English Grammar"
  },
  {
    "question": "'There are ___ apples in the basket.'",
    "options": ["A) much", "B) a few", "C) a little", "D) less"],
    "answer": "B",
    "explanation": "'A few' for countable nouns (positive sense). 'A little' for uncountable.",
    "theme": "English Grammar"
  },
  {
    "question": "Which noun is uncountable?",
    "options": ["A) Book", "B) Chair", "C) Information", "D) Apple"],
    "answer": "C",
    "explanation": "'Information' is uncountable: 'some information' (never 'informations' in English).",
    "theme": "English Grammar"
  },
  {
    "question": "'She ___ here for three years.' (and still works here)",
    "options": ["A) worked", "B) works", "C) has been working", "D) was working"],
    "answer": "C",
    "explanation": "Present perfect continuous for an action that started in the past and continues.",
    "theme": "English Grammar"
  },
  {
    "question": "'He ___ while I ___ .' (read / study)",
    "options": ["A) was reading / was studying", "B) read / studied", "C) was reading / studied", "D) read / was studying"],
    "answer": "A",
    "explanation": "Two simultaneous ongoing past actions: both in past continuous.",
    "theme": "English Grammar"
  },
  {
    "question": "'Although it was raining, ___'",
    "options": ["A) but they went out", "B) they went out", "C) so they stayed", "D) however they left"],
    "answer": "B",
    "explanation": "'Although' introduces a concession — no need for 'but'. Avoid double conjunction.",
    "theme": "English Grammar"
  },
  {
    "question": "'___ the rain, they went out.'",
    "options": ["A) Although", "B) Despite", "C) However", "D) Because of"],
    "answer": "B",
    "explanation": "'Despite' + noun/gerund for concession. 'Although' needs a clause.",
    "theme": "English Grammar"
  },
  {
    "question": "'He is good ___ mathematics.'",
    "options": ["A) in", "B) at", "C) on", "D) for"],
    "answer": "B",
    "explanation": "'Good at' is the correct preposition for skills/subjects.",
    "theme": "English Grammar"
  },
  {
    "question": "'She is interested ___ history.'",
    "options": ["A) about", "B) at", "C) in", "D) for"],
    "answer": "C",
    "explanation": "'Interested in' is the correct preposition.",
    "theme": "English Grammar"
  },
  {
    "question": "'He depends ___ his parents financially.'",
    "options": ["A) of", "B) on", "C) from", "D) in"],
    "answer": "B",
    "explanation": "'Depend on' is the correct preposition (not 'depend of').",
    "theme": "English Grammar"
  },
  {
    "question": "'Could you look ___ my cat while I'm away?' (take care of)",
    "options": ["A) at", "B) for", "C) after", "D) up"],
    "answer": "C",
    "explanation": "'Look after' means to take care of someone/something.",
    "theme": "English Grammar"
  },
  {
    "question": "'I need to look ___ a word in the dictionary.' (search for)",
    "options": ["A) at", "B) for", "C) up", "D) after"],
    "answer": "C",
    "explanation": "'Look up' means to search for information in a reference.",
    "theme": "English Grammar"
  },
  {
    "question": "'He ___ up smoking last year.' (stop)",
    "options": ["A) gave", "B) put", "C) took", "D) got"],
    "answer": "A",
    "explanation": "'Give up' means to stop/quit a habit.",
    "theme": "English Grammar"
  },
  {
    "question": "'___ you study hard, you won't pass the exam.'",
    "options": ["A) If", "B) Unless", "C) Although", "D) Despite"],
    "answer": "B",
    "explanation": "'Unless' = 'if not'. Unless you study hard = if you don't study hard.",
    "theme": "English Grammar"
  },
  {
    "question": "'He ran fast ___ he could catch the bus.'",
    "options": ["A) so that", "B) because", "C) although", "D) unless"],
    "answer": "A",
    "explanation": "'So that' expresses purpose (pour que/afin que).",
    "theme": "English Grammar"
  },
  {
    "question": "'___ I finish this report, I will call you.'",
    "options": ["A) While", "B) During", "C) As soon as", "D) Until"],
    "answer": "C",
    "explanation": "'As soon as' = dès que. Followed by present tense for future meaning.",
    "theme": "English Grammar"
  },
  {
    "question": "'This is the city ___ I was born.'",
    "options": ["A) which", "B) who", "C) where", "D) that"],
    "answer": "C",
    "explanation": "'Where' for places in relative clauses.",
    "theme": "English Grammar"
  },
  {
    "question": "'I don't know ___ he is coming or not.'",
    "options": ["A) if", "B) whether", "C) that", "D) Both A and B"],
    "answer": "D",
    "explanation": "Both 'if' and 'whether' can introduce indirect yes/no questions. 'Whether' is more formal.",
    "theme": "English Grammar"
  },
  {
    "question": "'He speaks English ___ fluently ___ French.' (comparison of equality)",
    "options": ["A) so / than", "B) as / as", "C) more / than", "D) less / as"],
    "answer": "B",
    "explanation": "'As...as' for comparisons of equality: He speaks English as fluently as French.",
    "theme": "English Grammar"
  },
  {
    "question": "'___ having a headache, she went to work.'",
    "options": ["A) Although", "B) In spite of", "C) Because", "D) Due to"],
    "answer": "B",
    "explanation": "'In spite of' + gerund/noun for concession (synonym of 'despite').",
    "theme": "English Grammar"
  },
  {
    "question": "'He ___ to London twice this year.' (experience up to now)",
    "options": ["A) went", "B) has been", "C) was going", "D) goes"],
    "answer": "B",
    "explanation": "Present perfect for experiences within an unfinished time period ('this year').",
    "theme": "English Grammar"
  },
  {
    "question": "'The exam was ___ than I expected.'",
    "options": ["A) more easier", "B) easier", "C) most easy", "D) easy"],
    "answer": "B",
    "explanation": "Short adjectives: comparative = adjective + '-er'. Never 'more + -er'.",
    "theme": "English Grammar"
  },
  {
    "question": "'You ___ to see a doctor. You look ill.' (conseil)",
    "options": ["A) ought", "B) must", "C) might", "D) can"],
    "answer": "A",
    "explanation": "'Ought to' expresses advice, similar to 'should'.",
    "theme": "English Grammar"
  },
  {
    "question": "'___ dogs are loyal animals.' (generalite)",
    "options": ["A) A", "B) The", "C) An", "D) No article"],
    "answer": "D",
    "explanation": "No article for generalities with plural countable nouns.",
    "theme": "English Grammar"
  },
  {
    "question": "'If water reaches 0 degrees, it ___.'",
    "options": ["A) freezes", "B) will freeze", "C) would freeze", "D) froze"],
    "answer": "A",
    "explanation": "Type Zero conditional for scientific truths: If + Present, Present.",
    "theme": "English Grammar"
  },
  {
    "question": "'He ___ be at home. His car is in the driveway.' (deduction forte)",
    "options": ["A) might", "B) must", "C) should", "D) could"],
    "answer": "B",
    "explanation": "'Must' expresses strong logical deduction based on evidence.",
    "theme": "English Grammar"
  },
  {
    "question": "'You ___ park here. It is forbidden.'",
    "options": ["A) mustn't", "B) needn't", "C) don't have to", "D) shouldn't"],
    "answer": "A",
    "explanation": "'Mustn't' expresses prohibition. 'Needn't/don't have to' express absence of obligation.",
    "theme": "English Grammar"
  },
  {
    "question": "Complete: 'If I had studied harder, I ___ the exam.'",
    "options": ["A) would pass", "B) will have passed", "C) would have passed", "D) passed"],
    "answer": "C",
    "explanation": "Type 3 conditional: If + Past Perfect, Would have + Past Participle.",
    "theme": "English Grammar"
  },
  {
    "question": "Which sentence uses the correct article?",
    "options": ["A) She plays the tennis every morning.", "B) She plays tennis every morning.", "C) She plays a tennis every morning.", "D) She plays an tennis every morning."],
    "answer": "B",
    "explanation": "No article before sports: she plays tennis.",
    "theme": "English Grammar"
  },
  {
    "question": "Complete: 'By next year, she ___ her degree.'",
    "options": ["A) will finish", "B) will have finished", "C) finishes", "D) would finish"],
    "answer": "B",
    "explanation": "Future perfect: actions completed before a future point in time.",
    "theme": "English Grammar"
  },
  {
    "question": "Complete: '___ honest man always tells the truth.'",
    "options": ["A) A", "B) An", "C) The", "D) No article"],
    "answer": "B",
    "explanation": "Use 'an' before vowel sounds. 'Honest' starts with a silent h.",
    "theme": "English Grammar"
  },
  {
    "question": "Which sentence is grammatically correct?",
    "options": ["A) He doesn't know nothing.", "B) He knows nothing.", "C) He don't know nothing.", "D) He knows not nothing."],
    "answer": "B",
    "explanation": "In standard English, double negatives are incorrect. Use 'He knows nothing.'",
    "theme": "English Grammar"
  },
  {
    "question": "'She ___ speak three languages.' (capacite presente)",
    "options": ["A) can", "B) could", "C) may", "D) might"],
    "answer": "A",
    "explanation": "'Can' expresses present ability. 'Could' is for past ability or polite requests.",
    "theme": "English Grammar"
  },
  {
    "question": "'The report ___ by the committee next week.' (future passive)",
    "options": ["A) is reviewed", "B) will be reviewed", "C) has been reviewed", "D) was reviewed"],
    "answer": "B",
    "explanation": "Future passive: will + be + past participle.",
    "theme": "English Grammar"
  },
  {
    "question": "Choose the correct preposition: 'She is interested ___ history.'",
    "options": ["A) about", "B) in", "C) for", "D) on"],
    "answer": "B",
    "explanation": "'Interested in' is the correct fixed collocation.",
    "theme": "English Grammar"
  },
  {
    "question": "'I haven't seen him ___ last Monday.'",
    "options": ["A) for", "B) since", "C) during", "D) until"],
    "answer": "B",
    "explanation": "'Since' is used with a specific point in time (last Monday). 'For' is used with durations.",
    "theme": "English Grammar"
  },
  {
    "question": "Which word correctly completes: 'He apologised ___ being late.'",
    "options": ["A) about", "B) for", "C) of", "D) to"],
    "answer": "B",
    "explanation": "'Apologise for' is the correct collocation.",
    "theme": "English Grammar"
  },
  {
    "question": "What is the correct plural of 'child'?",
    "options": ["A) childs", "B) childes", "C) children", "D) child's"],
    "answer": "C",
    "explanation": "'Children' is the irregular plural of 'child'.",
    "theme": "English Grammar"
  },
  {
    "question": "'By the time I arrived, the movie ___.'",
    "options": ["A) already started", "B) has already started", "C) had already started", "D) was already starting"],
    "answer": "C",
    "explanation": "Past perfect for an action completed before another past action: had + past participle.",
    "theme": "English Grammar"
  },
  {
    "question": "Which sentence uses 'yet' correctly?",
    "options": ["A) I have finished yet.", "B) Have you finished yet?", "C) Yet I finished.", "D) I yet finished."],
    "answer": "B",
    "explanation": "'Yet' in questions means 'up to now'. In negatives: 'I haven't finished yet.'",
    "theme": "English Grammar"
  },
  {
    "question": "'She made him ___ the dishes.'",
    "options": ["A) wash", "B) to wash", "C) washing", "D) washed"],
    "answer": "A",
    "explanation": "Causative 'make' + object + bare infinitive (without 'to').",
    "theme": "English Grammar"
  },
  {
    "question": "Which is the correct indirect question?",
    "options": ["A) He asked where did she live.", "B) He asked where she lived.", "C) He asked where she does live.", "D) He asked where lived she."],
    "answer": "B",
    "explanation": "In indirect questions, use statement word order (no inversion, no auxiliary verb).",
    "theme": "English Grammar"
  },
  {
    "question": "'___ you mind opening the window?' (polite request)",
    "options": ["A) Do", "B) Would", "C) Could", "D) Both B and C"],
    "answer": "D",
    "explanation": "Both 'Would you mind...' and 'Could you mind...' are polite requests. 'Would' is slightly more formal.",
    "theme": "English Grammar"
  },
  {
    "question": "Complete: 'He suggested that she ___ a doctor.'",
    "options": ["A) sees", "B) see", "C) saw", "D) should sees"],
    "answer": "B",
    "explanation": "After 'suggest that', use the base form (subjunctive mood in formal English).",
    "theme": "English Grammar"
  },
  {
    "question": "What does 'albeit' mean?",
    "options": ["A) Because", "B) Although / even though", "C) Therefore", "D) Unless"],
    "answer": "B",
    "explanation": "'Albeit' is a formal conjunction meaning 'although' or 'even though'.",
    "theme": "English Grammar"
  },
  {
    "question": "Choose the correct form: 'Neither of the students ___ prepared.'",
    "options": ["A) were", "B) are", "C) was", "D) be"],
    "answer": "C",
    "explanation": "'Neither' as a subject takes a singular verb: 'was'.",
    "theme": "English Grammar"
  },
  {
    "question": "Which sentence uses the gerund correctly?",
    "options": ["A) I enjoy to swim.", "B) I enjoy swim.", "C) I enjoy swimming.", "D) I enjoy swam."],
    "answer": "C",
    "explanation": "'Enjoy' is always followed by a gerund (verb + -ing).",
    "theme": "English Grammar"
  },
  {
    "question": "What is the passive form of 'They will announce the results tomorrow'?",
    "options": ["A) The results are announced tomorrow.", "B) The results will be announced tomorrow.", "C) The results have been announced tomorrow.", "D) The results were announced tomorrow."],
    "answer": "B",
    "explanation": "Future passive: will + be + past participle.",
    "theme": "English Grammar"
  },
  {
    "question": "What does 'henceforth' mean?",
    "options": ["A) In the past", "B) From this point on", "C) Nevertheless", "D) Therefore"],
    "answer": "B",
    "explanation": "'Henceforth' is a formal adverb meaning 'from now on / from this point forward'.",
    "theme": "English Grammar"
  },
  {
    "question": "'I ___ here for two years by next January.' (future perfect continuous)",
    "options": ["A) will live", "B) will have been living", "C) have been living", "D) am living"],
    "answer": "B",
    "explanation": "Future perfect continuous: will have been + -ing. Used for duration up to a future point.",
    "theme": "English Grammar"
  },
  {
    "question": "Which is the correct tag question for 'Let's go, ___?'",
    "options": ["A) shall we", "B) will we", "C) do we", "D) won't we"],
    "answer": "A",
    "explanation": "The tag question for 'Let's...' is always 'shall we?'",
    "theme": "English Grammar"
  },
  {
    "question": "Choose the correct meaning of 'notwithstanding':",
    "options": ["A) In addition to", "B) Despite / in spite of", "C) Because of", "D) Instead of"],
    "answer": "B",
    "explanation": "'Notwithstanding' is a formal word meaning 'despite' or 'in spite of'.",
    "theme": "English Grammar"
  },
  {
    "question": "Complete: '___ hard work, he failed the exam.'",
    "options": ["A) Although", "B) Despite", "C) However", "D) Because of"],
    "answer": "B",
    "explanation": "'Despite' + noun/gerund. 'Although' needs a full clause with subject + verb.",
    "theme": "English Grammar"
  },
  {
    "question": "What is the correct form? 'The news ___ shocking.'",
    "options": ["A) are", "B) were", "C) is", "D) have been"],
    "answer": "C",
    "explanation": "'News' is an uncountable noun that takes a singular verb.",
    "theme": "English Grammar"
  },
  {
    "question": "Which phrasal verb means 'to investigate or look into'?",
    "options": ["A) look up", "B) look into", "C) look after", "D) look out"],
    "answer": "B",
    "explanation": "'Look into' means to investigate or examine something carefully.",
    "theme": "English Grammar"
  },
  {
    "question": "Choose the correct sentence about habitual past:",
    "options": ["A) I used to eating there.", "B) I would eat there every week.", "C) I was used to eat there.", "D) I have used to eat there."],
    "answer": "B",
    "explanation": "Both 'used to' and 'would' express past habits, but 'would' cannot refer to past states.",
    "theme": "English Grammar"
  },
  {
    "question": "'She advised me ___ the contract before signing.'",
    "options": ["A) read", "B) reading", "C) to read", "D) to reading"],
    "answer": "C",
    "explanation": "'Advise' + object + to-infinitive.",
    "theme": "English Grammar"
  },
  {
    "question": "What is the difference between 'few' and 'a few'?",
    "options": ["A) No difference", "B) 'Few' is negative (almost none); 'a few' is positive (some)", "C) 'A few' is used with uncountable nouns", "D) 'Few' is formal, 'a few' is informal"],
    "answer": "B",
    "explanation": "'Few' emphasises scarcity; 'a few' emphasises that there is at least some quantity.",
    "theme": "English Grammar"
  },
  {
    "question": "Complete: '___ he studied hard, he passed the exam.' (result of condition)",
    "options": ["A) If", "B) Although", "C) Because", "D) Unless"],
    "answer": "C",
    "explanation": "'Because' introduces a cause/reason. The sentence means his hard work caused him to pass.",
    "theme": "English Grammar"
  },
  {
    "question": "Which is the correct form of reported speech for 'I will call you'?",
    "options": ["A) He said he will call me.", "B) He said he would call me.", "C) He said he calls me.", "D) He said he had called me."],
    "answer": "B",
    "explanation": "In reported speech, 'will' shifts to 'would' (backshift of tenses).",
    "theme": "English Grammar"
  },
  {
    "question": "What does 'to be on the fence' mean?",
    "options": ["A) To be in danger", "B) To be undecided/neutral", "C) To be very happy", "D) To be at work"],
    "answer": "B",
    "explanation": "Idiom: 'to be on the fence' means to be undecided, neutral, or avoid taking a side.",
    "theme": "English Grammar"
  },
  {
    "question": "Choose the correct collocation:",
    "options": ["A) Do a mistake", "B) Make a mistake", "C) Have a mistake", "D) Take a mistake"],
    "answer": "B",
    "explanation": "The correct collocation is 'make a mistake', not 'do'.",
    "theme": "English Grammar"
  },
  {
    "question": "Which sentence correctly uses the present perfect continuous?",
    "options": ["A) She has been working here for two years.", "B) She is working here for two years.", "C) She has worked here since two years.", "D) She works here for two years."],
    "answer": "A",
    "explanation": "Present perfect continuous: have/has + been + -ing, often with 'for' or 'since'.",
    "theme": "English Grammar"
  },
  {
    "question": "Complete: 'If only I ___ more time to prepare!'",
    "options": ["A) have", "B) had", "C) will have", "D) would have"],
    "answer": "B",
    "explanation": "'If only' + past tense expresses a wish about the present (unreal condition).",
    "theme": "English Grammar"
  },
  {
    "question": "Which sentence is INCORRECT?",
    "options": ["A) The police are investigating.", "B) My family are coming tomorrow.", "C) The committee has reached a decision.", "D) These informations are useful."],
    "answer": "D",
    "explanation": "'Information' is uncountable in English: 'this information' or 'these pieces of information'.",
    "theme": "English Grammar"
  },
  {
    "question": "What is the meaning of 'to get cold feet'?",
    "options": ["A) To be cold", "B) To become nervous and lose courage", "C) To be unprepared", "D) To arrive late"],
    "answer": "B",
    "explanation": "Idiom: 'to get cold feet' means to become nervous and reluctant to do something.",
    "theme": "English Grammar"
  },
  {
    "question": "Which is the correct conditional type 3?",
    "options": ["A) If she studied harder, she would pass.", "B) If she had studied harder, she would have passed.", "C) If she studies harder, she will pass.", "D) If she would study harder, she passes."],
    "answer": "B",
    "explanation": "Type 3 conditional: If + past perfect, would have + past participle. It refers to unreal past situations.",
    "theme": "English Grammar"
  },
  {
    "question": "Choose the correct preposition: 'She is very good ___ solving problems.'",
    "options": ["A) in", "B) on", "C) at", "D) for"],
    "answer": "C",
    "explanation": "'Good at' + gerund is the correct collocation for skills/abilities.",
    "theme": "English Grammar"
  },
  {
    "question": "What does 'to beat around the bush' mean?",
    "options": ["A) To be very direct", "B) To avoid the main topic", "C) To work hard", "D) To be confused"],
    "answer": "B",
    "explanation": "Idiom: 'to beat around the bush' means to avoid coming to the main point.",
    "theme": "English Grammar"
  },
  {
    "question": "What is the gerund form of 'write'?",
    "options": ["A) Written", "B) Wrote", "C) Writing", "D) To write"],
    "answer": "C",
    "explanation": "The gerund is the -ing form used as a noun: 'Writing is important.'",
    "theme": "English Grammar"
  },
  {
    "question": "Choose the correct form: '___ the meeting, I took notes.'",
    "options": ["A) Since", "B) During", "C) While", "D) For"],
    "answer": "B",
    "explanation": "'During' + noun. 'While' needs a clause with subject + verb.",
    "theme": "English Grammar"
  },
  {
    "question": "What is the superlative of 'bad'?",
    "options": ["A) More bad", "B) Worse", "C) The worst", "D) Baddest"],
    "answer": "C",
    "explanation": "Irregular superlative: bad → worse → the worst.",
    "theme": "English Grammar"
  },
  {
    "question": "Which sentence correctly uses 'unless'?",
    "options": ["A) Unless you don't hurry, you'll miss the train.", "B) Unless you hurry, you'll miss the train.", "C) Unless you hurry, you won't miss the train.", "D) Unless you hurried, you miss the train."],
    "answer": "B",
    "explanation": "'Unless' = 'if...not'. Never combine with another negative: 'unless you hurry' = 'if you don't hurry'.",
    "theme": "English Grammar"
  },
  {
    "question": "If I _____ you, I wouldn't have accepted the offer.",
    "options": ["A) was", "B) am", "C) had been", "D) were"],
    "answer": "D",
    "explanation": "In conditional type 2 (unreal present), 'were' is used for all subjects. However, due to 'wouldn't have accepted' (type 3), the first part should technically be 'had been', but mixed conditionals exist: If I were you (now/general), I wouldn't have done that (past).",
    "theme": "English Grammar"
  },
  {
    "question": "By the time we get to the cinema, the movie _____.",
    "options": ["A) will start", "B) will have started", "C) started", "D) has started"],
    "answer": "B",
    "explanation": "The future perfect 'will have started' is used for an action that will be completed before a certain time in the future.",
    "theme": "English Grammar"
  },
  {
    "question": "He has been working here _____ 2015.",
    "options": ["A) since", "B) for", "C) in", "D) from"],
    "answer": "A",
    "explanation": "'Since' is used with a specific point in time to indicate the beginning of an ongoing action.",
    "theme": "English Grammar"
  },
  {
    "question": "I look forward to _____ from you soon.",
    "options": ["A) hear", "B) heard", "C) hearing", "D) be hearing"],
    "answer": "C",
    "explanation": "The phrase 'look forward to' is always followed by a gerund (verb + -ing).",
    "theme": "English Grammar"
  },
  {
    "question": "Hardly _____ entered the room when the phone rang.",
    "options": ["A) I had", "B) had I", "C) I", "D) did I"],
    "answer": "B",
    "explanation": "After 'Hardly', subject-verb inversion is required in formal English.",
    "theme": "English Grammar"
  },
  {
    "question": "She is used to _____ up early.",
    "options": ["A) wake", "B) waking", "C) woke", "D) woken"],
    "answer": "B",
    "explanation": "'To be used to' is followed by a gerund (verb + -ing).",
    "theme": "English Grammar"
  },
  {
    "question": "The manager _____ the meeting until next week.",
    "options": ["A) put off", "B) put on", "C) put out", "D) put away"],
    "answer": "A",
    "explanation": "The phrasal verb 'put off' means to postpone.",
    "theme": "English Grammar"
  },
  {
    "question": "If you don't know the word, look it _____ in the dictionary.",
    "options": ["A) out", "B) for", "C) up", "D) at"],
    "answer": "C",
    "explanation": "'Look up' means to search for information in a reference book.",
    "theme": "English Grammar"
  },
  {
    "question": "Neither the manager nor the employees _____ aware of the changes.",
    "options": ["A) was", "B) is", "C) were", "D) has been"],
    "answer": "C",
    "explanation": "With 'neither... nor', the verb agrees with the subject closest to it ('employees', which is plural).",
    "theme": "English Grammar"
  },
  {
    "question": "It's high time you _____ studying for the ENA exam.",
    "options": ["A) start", "B) started", "C) will start", "D) had started"],
    "answer": "B",
    "explanation": "The phrase 'It is high time' is followed by the past simple to refer to the present or future.",
    "theme": "English Grammar"
  },
  {
    "question": "The company went bankrupt because it was heavily _____.",
    "options": ["A) in debt", "B) on debt", "C) with debt", "D) of debt"],
    "answer": "A",
    "explanation": "The correct idiom is 'in debt'.",
    "theme": "English Grammar"
  },
  {
    "question": "Despite _____ hard, he failed the test.",
    "options": ["A) he tried", "B) trying", "C) to try", "D) of trying"],
    "answer": "B",
    "explanation": "'Despite' is followed by a noun or a gerund ('trying').",
    "theme": "English Grammar"
  },
  {
    "question": "The committee _____ composed of five members.",
    "options": ["A) are", "B) is", "C) have", "D) has"],
    "answer": "B",
    "explanation": "'Committee' is a collective noun often treated as singular when acting as a single unit.",
    "theme": "English Grammar"
  },
  {
    "question": "I would rather you _____ home now.",
    "options": ["A) go", "B) going", "C) went", "D) gone"],
    "answer": "C",
    "explanation": "'Would rather' followed by a subject takes the past tense to express a present preference.",
    "theme": "English Grammar"
  },
  {
    "question": "Choose the correct spelling:",
    "options": ["A) Accomodation", "B) Accommodation", "C) Accomadation", "D) Acommodation"],
    "answer": "B",
    "explanation": "'Accommodation' takes two c's and two m's.",
    "theme": "English Grammar"
  },
  {
    "question": "He denied _____ the money.",
    "options": ["A) to steal", "B) steal", "C) stole", "D) stealing"],
    "answer": "D",
    "explanation": "The verb 'deny' is followed by a gerund.",
    "theme": "English Grammar"
  },
  {
    "question": "Let's grab a coffee, _____ we?",
    "options": ["A) will", "B) do", "C) shall", "D) won't"],
    "answer": "C",
    "explanation": "The question tag for 'Let's' is always 'shall we'.",
    "theme": "English Grammar"
  },
  {
    "question": "The new policy will be _____ next month.",
    "options": ["A) implemented", "B) implies", "C) implicate", "D) implicit"],
    "answer": "A",
    "explanation": "Policies are 'implemented' (put into effect).",
    "theme": "English Grammar"
  },
  {
    "question": "I am not used to _____ on the left side of the road.",
    "options": ["A) drive", "B) driving", "C) drove", "D) driven"],
    "answer": "B",
    "explanation": "'Used to' acting as an adjective (meaning accustomed to) takes a gerund.",
    "theme": "English Grammar"
  },
  {
    "question": "He is the man _____ car was stolen yesterday.",
    "options": ["A) who", "B) whom", "C) whose", "D) which"],
    "answer": "C",
    "explanation": "'Whose' is the relative pronoun used to indicate possession.",
    "theme": "English Grammar"
  },
  {
    "question": "The project was delayed _____ a lack of funds.",
    "options": ["A) because", "B) due to", "C) since", "D) for"],
    "answer": "B",
    "explanation": "'Due to' is followed by a noun phrase.",
    "theme": "English Grammar"
  },
  {
    "question": "If he had known the truth, he _____ differently.",
    "options": ["A) would act", "B) will act", "C) would have acted", "D) acts"],
    "answer": "C",
    "explanation": "Third conditional requires 'would have + past participle' in the main clause.",
    "theme": "English Grammar"
  },
  {
    "question": "They rarely speak to each other, _____ they?",
    "options": ["A) do", "B) don't", "C) are", "D) aren't"],
    "answer": "A",
    "explanation": "'Rarely' has a negative meaning, so the question tag is positive.",
    "theme": "English Grammar"
  },
  {
    "question": "She succeeded in _____ the difficult exam.",
    "options": ["A) pass", "B) passing", "C) passed", "D) to pass"],
    "answer": "B",
    "explanation": "Prepositions like 'in' are followed by the gerund form of a verb.",
    "theme": "English Grammar"
  },
  {
    "question": "I wish I _____ richer.",
    "options": ["A) am", "B) was", "C) were", "D) have been"],
    "answer": "C",
    "explanation": "After 'I wish', 'were' is used for all persons to express an unreal present situation.",
    "theme": "English Grammar"
  },
  {
    "question": "Not only _____ late, but he also forgot his documents.",
    "options": ["A) he arrived", "B) did he arrive", "C) he did arrive", "D) arrives he"],
    "answer": "B",
    "explanation": "When 'Not only' starts a sentence, it triggers inversion.",
    "theme": "English Grammar"
  },
  {
    "question": "The term 'false friend' (faux ami) 'Actual' in English means:",
    "options": ["A) Currently happening", "B) Real or exact", "C) Modern", "D) Updated"],
    "answer": "B",
    "explanation": "'Actual' means real, true, or exact, unlike 'actuel' in French which means current.",
    "theme": "English Grammar"
  },
  {
    "question": "Which of these is a synonym for 'mitigate'?",
    "options": ["A) Worsen", "B) Alleviate", "C) Provoke", "D) Startle"],
    "answer": "B",
    "explanation": "'Mitigate' means to make something less severe or painful, similar to 'alleviate'.",
    "theme": "English Grammar"
  },
  {
    "question": "He gave me a lot of _____ on how to pass the ENA exam.",
    "options": ["A) advices", "B) advise", "C) advice", "D) advising"],
    "answer": "C",
    "explanation": "'Advice' is an uncountable noun and does not take an 's'.",
    "theme": "English Grammar"
  },
  {
    "question": "They _____ to Paris twice this year.",
    "options": ["A) went", "B) go", "C) have been", "D) had been"],
    "answer": "C",
    "explanation": "The present perfect 'have been' is used for actions completed in a time period that is not yet over ('this year').",
    "theme": "English Grammar"
  },
  {
    "question": "She avoids _____ in public.",
    "options": ["A) to speak", "B) speak", "C) speaking", "D) spoken"],
    "answer": "C",
    "explanation": "The verb 'avoid' is followed by a gerund.",
    "theme": "English Grammar"
  },
  {
    "question": "You had better _____ your doctor.",
    "options": ["A) to see", "B) seeing", "C) see", "D) saw"],
    "answer": "C",
    "explanation": "'Had better' is followed by the bare infinitive (without 'to').",
    "theme": "English Grammar"
  },
  {
    "question": "There is a _____ difference between the two proposals.",
    "options": ["A) subtle", "B) sutil", "C) subtil", "D) sutle"],
    "answer": "A",
    "explanation": "The correct spelling in English is 'subtle'.",
    "theme": "English Grammar"
  },
  {
    "question": "He speaks English _____ than his brother.",
    "options": ["A) more better", "B) much better", "C) most better", "D) best"],
    "answer": "B",
    "explanation": "'Better' is the comparative form of well/good, modified correctly by 'much'.",
    "theme": "English Grammar"
  },
  {
    "question": "By 2030, the government _____ building the new hospital.",
    "options": ["A) will finish", "B) has finished", "C) will have finished", "D) finishes"],
    "answer": "C",
    "explanation": "Future perfect is used for an action completed before a specific time in the future.",
    "theme": "English Grammar"
  },
  {
    "question": "The English translation of 'assister à une réunion' is:",
    "options": ["A) to assist a meeting", "B) to attend a meeting", "C) to follow a meeting", "D) to participate a meeting"],
    "answer": "B",
    "explanation": "'To attend' means to be present at an event. 'To assist' means to help.",
    "theme": "English Grammar"
  },
  {
    "question": "I can't figure _____ how to solve this math problem.",
    "options": ["A) out", "B) in", "C) on", "D) up"],
    "answer": "A",
    "explanation": "The phrasal verb 'figure out' means to solve or understand.",
    "theme": "English Grammar"
  },
  {
    "question": "He has little experience, _____?",
    "options": ["A) has he", "B) hasn't he", "C) does he", "D) doesn't he"],
    "answer": "C",
    "explanation": "'Little' has a negative meaning, and 'has' as a main verb often takes 'does' in tags.",
    "theme": "English Grammar"
  },
  {
    "question": "It's imperative that he _____ present at the meeting.",
    "options": ["A) is", "B) be", "C) was", "D) will be"],
    "answer": "B",
    "explanation": "The subjunctive mood is used after adjectives of urgency like 'imperative'.",
    "theme": "English Grammar"
  },
  {
    "question": "We ran out _____ petrol on the highway.",
    "options": ["A) of", "B) from", "C) off", "D) with"],
    "answer": "A",
    "explanation": "The phrasal verb 'run out of' means to use all of a supply.",
    "theme": "English Grammar"
  },
  {
    "question": "She accused him _____ stealing the documents.",
    "options": ["A) for", "B) of", "C) about", "D) with"],
    "answer": "B",
    "explanation": "The verb 'accuse' is followed by the preposition 'of'.",
    "theme": "English Grammar"
  },
  {
    "question": "I remember _____ him at the conference last year.",
    "options": ["A) meet", "B) to meet", "C) meeting", "D) met"],
    "answer": "C",
    "explanation": "'Remember' + gerund refers to a memory of a past event.",
    "theme": "English Grammar"
  },
  {
    "question": "The English false friend 'sensible' translates to French as:",
    "options": ["A) sensible", "B) raisonnable", "C) sensitif", "D) sensationnel"],
    "answer": "B",
    "explanation": "'Sensible' in English means logical, practical, or 'raisonnable'. 'Sensitive' means 'sensible' (French).",
    "theme": "English Grammar"
  },
  {
    "question": "He is _____ engineer.",
    "options": ["A) a", "B) an", "C) the", "D) no article"],
    "answer": "B",
    "explanation": "'An' is used before professions starting with a vowel sound.",
    "theme": "English Grammar"
  },
  {
    "question": "I would have called you if I _____ my phone.",
    "options": ["A) had", "B) have had", "C) had had", "D) have"],
    "answer": "C",
    "explanation": "Third conditional 'if' clause requires the past perfect ('had had').",
    "theme": "English Grammar"
  },
  {
    "question": "The boss made him _____ late to finish the report.",
    "options": ["A) to stay", "B) stay", "C) staying", "D) stayed"],
    "answer": "B",
    "explanation": "'Make' is a causative verb followed by an object and a bare infinitive.",
    "theme": "English Grammar"
  },
  {
    "question": "They objected _____ treated like children.",
    "options": ["A) to be", "B) being", "C) to being", "D) against being"],
    "answer": "C",
    "explanation": "'Object to' is followed by a gerund ('being').",
    "theme": "English Grammar"
  },
  {
    "question": "Only when the plane landed safely _____ to relax.",
    "options": ["A) we began", "B) began we", "C) did we begin", "D) we did begin"],
    "answer": "C",
    "explanation": "Inversion is required when a sentence starts with 'Only when'.",
    "theme": "English Grammar"
  },
  {
    "question": "The word 'comprehensive' means:",
    "options": ["A) Understanding", "B) Thorough and complete", "C) Compromising", "D) Complicated"],
    "answer": "B",
    "explanation": "'Comprehensive' is a false friend; it means 'exhaustif' or 'complet' in French, not 'compréhensif'.",
    "theme": "English Grammar"
  },
  {
    "question": "Complete the sentence: It is crucial that the newly appointed director _____ the upcoming board meeting.",
    "options": ["A) attends", "B) attend", "C) attending", "D) will attend"],
    "answer": "B",
    "explanation": "The subjunctive mood is used after expressions of necessity like 'It is crucial that', requiring the base form of the verb.",
    "theme": "English Grammar"
  },
  {
    "question": "Hardly _____ the office when the phone started ringing.",
    "options": ["A) he had entered", "B) did he enter", "C) had he entered", "D) he entered"],
    "answer": "C",
    "explanation": "Negative adverbial phrases like 'Hardly' at the beginning of a sentence require subject-auxiliary inversion, typically past perfect 'had + subject + past participle'.",
    "theme": "English Grammar"
  },
  {
    "question": "If the committee had approved the budget last week, we _____ the project right now.",
    "options": ["A) would have started", "B) will start", "C) would be starting", "D) had started"],
    "answer": "C",
    "explanation": "This is a mixed conditional: a past unreal condition ('had approved') resulting in a present unreal result ('would be starting right now').",
    "theme": "English Grammar"
  },
  {
    "question": "The manager decided to _____ the less productive employees due to budget cuts.",
    "options": ["A) lay off", "B) lay out", "C) put off", "D) call off"],
    "answer": "A",
    "explanation": "'Lay off' means to discharge a worker temporarily or permanently because of a shortage of work.",
    "theme": "English Grammar"
  },
  {
    "question": "Not only _____ the new policy increase efficiency, but it also improves employee morale.",
    "options": ["A) does", "B) do", "C) has", "D) did"],
    "answer": "A",
    "explanation": "Inversion is required after 'Not only' at the beginning of a sentence. Since the second clause uses 'improves' (present tense), 'does' is appropriate.",
    "theme": "English Grammar"
  },
  {
    "question": "I suggest that the applicant _____ all relevant documents before the deadline.",
    "options": ["A) submits", "B) submitted", "C) submit", "D) has submitted"],
    "answer": "C",
    "explanation": "Verbs like 'suggest', 'recommend', and 'demand' are followed by a 'that' clause with a verb in the subjunctive mood (base form).",
    "theme": "English Grammar"
  },
  {
    "question": "She couldn't quite _____ what the speaker was trying to say amidst the noise.",
    "options": ["A) make up", "B) make out", "C) figure off", "D) take in"],
    "answer": "B",
    "explanation": "'Make out' means to manage to see, hear, or understand something.",
    "theme": "English Grammar"
  },
  {
    "question": "By the time the delegation arrives next week, the necessary preparations _____.",
    "options": ["A) are completed", "B) will have been completed", "C) will be completing", "D) have been completed"],
    "answer": "B",
    "explanation": "The future perfect passive ('will have been completed') is used to describe an action that will be finished before a specific time in the future.",
    "theme": "English Grammar"
  },
  {
    "question": "The contractor promised that the building _____ by the end of November.",
    "options": ["A) would be finished", "B) will finish", "C) is finished", "D) finishes"],
    "answer": "A",
    "explanation": "Reported speech in the past ('promised') typically shifts future tense ('will be finished') to conditional ('would be finished').",
    "theme": "English Grammar"
  },
  {
    "question": "Despite _____ a lack of resources, the team successfully launched the application.",
    "options": ["A) of facing", "B) facing", "C) to face", "D) they faced"],
    "answer": "B",
    "explanation": "'Despite' is a preposition and should be followed by a noun or a gerund ('facing'), without 'of'.",
    "theme": "English Grammar"
  },
  {
    "question": "We must _____ the fact that our competitors are gaining market share.",
    "options": ["A) face up to", "B) put up with", "C) get away with", "D) look down on"],
    "answer": "A",
    "explanation": "'Face up to' means to accept a difficult situation and deal with it.",
    "theme": "English Grammar"
  },
  {
    "question": "It is imperative that the regulations _____ strictly enforced to ensure safety.",
    "options": ["A) are", "B) be", "C) will be", "D) have been"],
    "answer": "B",
    "explanation": "'It is imperative that' triggers the subjunctive mood, requiring the base form of the verb ('be').",
    "theme": "English Grammar"
  },
  {
    "question": "Were _____ not for his timely intervention, the project would have failed.",
    "options": ["A) he", "B) it", "C) there", "D) that"],
    "answer": "B",
    "explanation": "'Were it not for' is a formal, inverted conditional phrase meaning 'If it were not for'.",
    "theme": "English Grammar"
  },
  {
    "question": "The CEO decided to step down, _____ paving the way for a younger leadership team.",
    "options": ["A) thereby", "B) however", "C) moreover", "D) nevertheless"],
    "answer": "A",
    "explanation": "'Thereby' means 'as a result of that action', which fits contextually.",
    "theme": "English Grammar"
  },
  {
    "question": "The company's profits have been declining steadily; _____, they have announced a hiring freeze.",
    "options": ["A) conversely", "B) consequently", "C) furthermore", "D) nonetheless"],
    "answer": "B",
    "explanation": "'Consequently' indicates that the hiring freeze is a result of the declining profits.",
    "theme": "English Grammar"
  },
  {
    "question": "I would rather you _____ the proposal before submitting it to the client.",
    "options": ["A) review", "B) reviewed", "C) have reviewed", "D) will review"],
    "answer": "B",
    "explanation": "'Would rather' followed by a subject requires the past subjunctive (past simple form) to express a preference about the present or future.",
    "theme": "English Grammar"
  },
  {
    "question": "The auditor found several discrepancies that need to be _____ immediately.",
    "options": ["A) looked into", "B) brought up", "C) taken over", "D) passed out"],
    "answer": "A",
    "explanation": "'Looked into' means to investigate or examine.",
    "theme": "English Grammar"
  },
  {
    "question": "Rarely _____ such a dedicated group of professionals.",
    "options": ["A) have I seen", "B) I have seen", "C) did I saw", "D) I saw"],
    "answer": "A",
    "explanation": "Negative adverbial 'Rarely' at the beginning of a sentence requires subject-auxiliary inversion.",
    "theme": "English Grammar"
  },
  {
    "question": "The new software is designed to _____ the administrative process, making it much faster.",
    "options": ["A) streamline", "B) undermine", "C) compromise", "D) exacerbate"],
    "answer": "A",
    "explanation": "'Streamline' means to make a process more efficient and effective.",
    "theme": "English Grammar"
  },
  {
    "question": "He was _____ on the spot for his gross misconduct.",
    "options": ["A) laid off", "B) fired", "C) stepped down", "D) taken back"],
    "answer": "B",
    "explanation": "'Fired' implies dismissal for cause, such as misconduct, whereas 'laid off' implies redundancy.",
    "theme": "English Grammar"
  },
  {
    "question": "If she had known about the traffic, she _____ another route.",
    "options": ["A) would take", "B) took", "C) would have taken", "D) had taken"],
    "answer": "C",
    "explanation": "Third conditional requires 'would have + past participle' in the main clause.",
    "theme": "English Grammar"
  },
  {
    "question": "The board requires that every member _____ present at the annual general meeting.",
    "options": ["A) is", "B) be", "C) are", "D) will be"],
    "answer": "B",
    "explanation": "'Requires that' is followed by the subjunctive mood, which uses the base form 'be'.",
    "theme": "English Grammar"
  },
  {
    "question": "The manager had to _____ the meeting because several key participants were unavailable.",
    "options": ["A) call off", "B) bring about", "C) carry out", "D) set up"],
    "answer": "A",
    "explanation": "'Call off' means to cancel an event.",
    "theme": "English Grammar"
  },
  {
    "question": "We are looking forward to _____ from you soon.",
    "options": ["A) hear", "B) hearing", "C) be heard", "D) have heard"],
    "answer": "B",
    "explanation": "The phrase 'look forward to' is followed by a gerund ('hearing').",
    "theme": "English Grammar"
  },
  {
    "question": "Scarcely had the president began his speech _____ the lights went out.",
    "options": ["A) than", "B) when", "C) that", "D) before"],
    "answer": "B",
    "explanation": "The correlative conjunction pair is 'Scarcely... when' (or 'Hardly... when').",
    "theme": "English Grammar"
  },
  {
    "question": "The new regulations will _____ effect on January 1st.",
    "options": ["A) make", "B) take", "C) put", "D) set"],
    "answer": "B",
    "explanation": "The correct collocation is 'take effect', meaning to come into operation.",
    "theme": "English Grammar"
  },
  {
    "question": "She is accustomed _____ working long hours during the tax season.",
    "options": ["A) with", "B) to", "C) for", "D) in"],
    "answer": "B",
    "explanation": "The adjective 'accustomed' is followed by the preposition 'to'.",
    "theme": "English Grammar"
  },
  {
    "question": "He was accused _____ embezzling company funds.",
    "options": ["A) for", "B) of", "C) with", "D) about"],
    "answer": "B",
    "explanation": "The correct preposition after 'accused' is 'of'.",
    "theme": "English Grammar"
  },
  {
    "question": "Under no circumstances _____ allowed to leave the premises without permission.",
    "options": ["A) employees are", "B) are employees", "C) employees will be", "D) have employees"],
    "answer": "B",
    "explanation": "Negative prepositional phrases like 'Under no circumstances' at the beginning of a sentence require inversion.",
    "theme": "English Grammar"
  },
  {
    "question": "The project was completed ahead of schedule, _____ surprised everyone.",
    "options": ["A) that", "B) which", "C) what", "D) who"],
    "answer": "B",
    "explanation": "The relative pronoun 'which' is used to refer back to the entire preceding clause.",
    "theme": "English Grammar"
  },
  {
    "question": "If it _____ rain tomorrow, we will have to reschedule the outdoor event.",
    "options": ["A) would", "B) should", "C) might", "D) could"],
    "answer": "B",
    "explanation": "'If it should rain' is a formal way to express a conditional future possibility.",
    "theme": "English Grammar"
  },
  {
    "question": "The committee demanded that the controversial proposal _____ withdrawn immediately.",
    "options": ["A) is", "B) be", "C) was", "D) has been"],
    "answer": "B",
    "explanation": "'Demanded that' requires the subjunctive base form 'be'.",
    "theme": "English Grammar"
  },
  {
    "question": "She speaks English fluently, _____ a slight accent.",
    "options": ["A) albeit", "B) despite", "C) whereas", "D) nonetheless"],
    "answer": "A",
    "explanation": "'Albeit' is a formal conjunction meaning 'although' or 'even if'.",
    "theme": "English Grammar"
  },
  {
    "question": "The company has decided to _____ its operations in the Asian market.",
    "options": ["A) scale back", "B) bring up", "C) pass out", "D) turn down"],
    "answer": "A",
    "explanation": "'Scale back' means to reduce the size or extent of something.",
    "theme": "English Grammar"
  },
  {
    "question": "Having _____ the document, he handed it to the director for signature.",
    "options": ["A) write", "B) written", "C) wrote", "D) writing"],
    "answer": "B",
    "explanation": "A perfect participle clause requires 'Having + past participle'.",
    "theme": "English Grammar"
  },
  {
    "question": "The instructions were convoluted; I couldn't make _____ of them.",
    "options": ["A) sense", "B) head nor tail", "C) meaning", "D) understanding"],
    "answer": "B",
    "explanation": "'Make head nor tail' is an idiom meaning to be completely unable to understand something.",
    "theme": "English Grammar"
  },
  {
    "question": "It is high time you _____ looking for a more stable job.",
    "options": ["A) start", "B) started", "C) are starting", "D) will start"],
    "answer": "B",
    "explanation": "'It is high time' is followed by the past simple tense to suggest something should be done now.",
    "theme": "English Grammar"
  },
  {
    "question": "The speaker _____ the importance of international cooperation during his address.",
    "options": ["A) emphasized on", "B) emphasized", "C) stressed on", "D) highlighted on"],
    "answer": "B",
    "explanation": "The verbs 'emphasize' and 'stress' are transitive and do not take the preposition 'on'.",
    "theme": "English Grammar"
  },
  {
    "question": "She was totally engrossed _____ her research.",
    "options": ["A) in", "B) at", "C) on", "D) with"],
    "answer": "A",
    "explanation": "The adjective 'engrossed' is followed by the preposition 'in'.",
    "theme": "English Grammar"
  },
  {
    "question": "No sooner had the minister arrived _____ the meeting commenced.",
    "options": ["A) when", "B) than", "C) that", "D) before"],
    "answer": "B",
    "explanation": "The correlative conjunction pair is 'No sooner... than'.",
    "theme": "English Grammar"
  },
  {
    "question": "The negotiations broke _____ after neither side was willing to compromise.",
    "options": ["A) out", "B) down", "C) through", "D) off"],
    "answer": "B",
    "explanation": "'Break down' refers to the failure of discussions or negotiations.",
    "theme": "English Grammar"
  },
  {
    "question": "Had I known about the policy change, I _____ differently.",
    "options": ["A) will have acted", "B) would act", "C) would have acted", "D) had acted"],
    "answer": "C",
    "explanation": "Third conditional requires 'would have + past participle' for the result of a past unfulfilled condition.",
    "theme": "English Grammar"
  },
  {
    "question": "The new employee is still trying to _____ the ropes.",
    "options": ["A) learn", "B) pull", "C) hold", "D) cut"],
    "answer": "A",
    "explanation": "'Learn the ropes' is an idiom meaning to understand how to do a particular job or task.",
    "theme": "English Grammar"
  },
  {
    "question": "He will not accept the offer unless it _____ his salary expectations.",
    "options": ["A) meets", "B) will meet", "C) meet", "D) met"],
    "answer": "A",
    "explanation": "'Unless' introduces a conditional clause, which takes the present simple tense ('meets') for future meaning.",
    "theme": "English Grammar"
  },
  {
    "question": "The company's success is largely contingent _____ securing this contract.",
    "options": ["A) on", "B) to", "C) with", "D) for"],
    "answer": "A",
    "explanation": "The adjective 'contingent' is followed by the preposition 'on' or 'upon'.",
    "theme": "English Grammar"
  },
  {
    "question": "He was completely taken _____ by the fraudulent scheme.",
    "options": ["A) back", "B) in", "C) off", "D) up"],
    "answer": "B",
    "explanation": "'Take in' in passive voice means to be deceived or cheated.",
    "theme": "English Grammar"
  },
  {
    "question": "It's essential that the data _____ backed up regularly.",
    "options": ["A) is", "B) be", "C) are", "D) will be"],
    "answer": "B",
    "explanation": "'It's essential that' requires the subjunctive base form 'be'.",
    "theme": "English Grammar"
  },
  {
    "question": "By the end of this year, she _____ as a diplomat for twenty years.",
    "options": ["A) will work", "B) will be working", "C) will have been working", "D) has worked"],
    "answer": "C",
    "explanation": "The future perfect continuous emphasizes the duration of an ongoing action up to a future point.",
    "theme": "English Grammar"
  },
  {
    "question": "His reckless behavior is bound to _____ consequences.",
    "options": ["A) bring about", "B) come across", "C) put off", "D) take after"],
    "answer": "A",
    "explanation": "'Bring about' means to cause something to happen.",
    "theme": "English Grammar"
  },
  {
    "question": "They were _____ the impression that the deadline had been extended.",
    "options": ["A) in", "B) on", "C) under", "D) with"],
    "answer": "C",
    "explanation": "The correct prepositional phrase is 'under the impression'.",
    "theme": "English Grammar"
  },
  {
    "question": "Which of the following sentences is grammatically correct?",
    "options": ["A) He cans swim.", "B) He can to swim.", "C) He can swim.", "D) He does can swim."],
    "answer": "C",
    "explanation": "Modals are invariable and are followed by the base form of the verb without 'to'.",
    "theme": "English Grammar"
  },
  {
    "question": "How do you form the interrogative of the modal 'can'?",
    "options": ["A) Do you can?", "B) Can you?", "C) Are you can?", "D) Can you to?"],
    "answer": "B",
    "explanation": "Interrogation with modals is formed by inversion, without using the auxiliary 'do'.",
    "theme": "English Grammar"
  },
  {
    "question": "Choose the correct negative form:",
    "options": ["A) You don't must go.", "B) You mustn't to go.", "C) You must not go.", "D) You don't must to go."],
    "answer": "C",
    "explanation": "Negation with modals is formed directly with 'not' (must not / mustn't), without 'do' and without 'to'.",
    "theme": "English Grammar"
  },
  {
    "question": "Which form is used to express capability in the future?",
    "options": ["A) will can", "B) will be able to", "C) shall can", "D) cans"],
    "answer": "B",
    "explanation": "Modals like 'can' do not have a future form; 'be able to' is used instead (will be able to).",
    "theme": "English Grammar"
  },
  {
    "question": "Despite the heavy fire, they ___ escape from the building.",
    "options": ["A) could", "B) can", "C) were able to", "D) might"],
    "answer": "C",
    "explanation": "For a specific successful achievement in the past (réussite effective), 'was/were able to' must be used instead of 'could'.",
    "theme": "English Grammar"
  },
  {
    "question": "Which modal is used to ask for formal permission?",
    "options": ["A) Must I", "B) Might I", "C) May I", "D) Shall I"],
    "answer": "C",
    "explanation": "'May' is used for formal permission (e.g., May I?).",
    "theme": "English Grammar"
  },
  {
    "question": "Is 'May you swim?' grammatically correct to ask about capability?",
    "options": ["A) Yes, it is formal.", "B) Yes, in British English.", "C) No, 'can' or 'are you able to' should be used.", "D) No, 'might' should be used."],
    "answer": "C",
    "explanation": "'May' expresses permission or possibility, not physical capacity.",
    "theme": "English Grammar"
  },
  {
    "question": "Which phrase expresses a past reproach?",
    "options": ["A) You might have told me!", "B) You must tell me!", "C) You can have told me!", "D) You may tell me!"],
    "answer": "A",
    "explanation": "'Might have + PP' can express a reproach about a past event.",
    "theme": "English Grammar"
  },
  {
    "question": "He has a big house and two expensive cars. He ___ be very rich.",
    "options": ["A) has to", "B) can", "C) ought", "D) must"],
    "answer": "D",
    "explanation": "'Must' is used to express a strong subjective deduction (déduction forte).",
    "theme": "English Grammar"
  },
  {
    "question": "What is the negative equivalent (negative deduction) of 'He must be at home'?",
    "options": ["A) He mustn't be at home.", "B) He doesn't have to be at home.", "C) He can't be at home.", "D) He shouldn't be at home."],
    "answer": "C",
    "explanation": "The negative deduction of 'must' is 'cannot/can't', not 'mustn't'.",
    "theme": "English Grammar"
  },
  {
    "question": "I ___ wear a uniform at my new job; it is the company's rule.",
    "options": ["A) must", "B) have to", "C) may", "D) would"],
    "answer": "B",
    "explanation": "'Have to' is used for an external or objective obligation, unlike the subjective 'must'.",
    "theme": "English Grammar"
  },
  {
    "question": "Which modal is traditionally used in modern English legal documents to express an obligation?",
    "options": ["A) shall", "B) should", "C) would", "D) might"],
    "answer": "A",
    "explanation": "'Shall' is used for legal (juridique) obligations.",
    "theme": "English Grammar"
  },
  {
    "question": "___ we go out for dinner tonight?",
    "options": ["A) Will", "B) Shall", "C) Ought", "D) Must"],
    "answer": "B",
    "explanation": "'Shall we?' is used to make a suggestion.",
    "theme": "English Grammar"
  },
  {
    "question": "It's strange that he ___ say such a thing.",
    "options": ["A) would", "B) shall", "C) should", "D) must"],
    "answer": "C",
    "explanation": "'Should' is used to express surprise after certain expressions like 'It's strange that'.",
    "theme": "English Grammar"
  },
  {
    "question": "Even when I tell him to stop, he ___ keep talking!",
    "options": ["A) should", "B) will", "C) might", "D) ought to"],
    "answer": "B",
    "explanation": "'Will' can be used to express insistence or a persistent present habit.",
    "theme": "English Grammar"
  },
  {
    "question": "When I was a child, I ___ be very shy.",
    "options": ["A) would", "B) used to", "C) should", "D) could"],
    "answer": "B",
    "explanation": "'Used to' describes a past state. 'Would' cannot replace 'used to' for states (e.g., 'I would be shy' is incorrect).",
    "theme": "English Grammar"
  },
  {
    "question": "You ___ to apologize to her; it's your moral duty.",
    "options": ["A) ought", "B) should", "C) must", "D) have"],
    "answer": "A",
    "explanation": "'Ought to' expresses a moral duty or strong advice and is followed by 'to'.",
    "theme": "English Grammar"
  },
  {
    "question": "___ you use to play football when you were younger?",
    "options": ["A) Do", "B) Were", "C) Are", "D) Did"],
    "answer": "D",
    "explanation": "The interrogative form for a past habit with 'used to' is formed with 'Did' (Did you use to?).",
    "theme": "English Grammar"
  },
  {
    "question": "He doesn't ___ to speak in front of the crowd.",
    "options": ["A) dare", "B) dares", "C) daring", "D) dared"],
    "answer": "A",
    "explanation": "When 'dare' is used as an ordinary verb, it uses 'do/does' for negation and takes the infinitive with 'to'.",
    "theme": "English Grammar"
  },
  {
    "question": "You ___ worry about the exam, it will be easy.",
    "options": ["A) don't need", "B) needn't to", "C) needn't", "D) needs not"],
    "answer": "C",
    "explanation": "When 'need' acts as a modal, it is followed directly by 'not' (needn't) and the base verb without 'to'.",
    "theme": "English Grammar"
  },
  {
    "question": "You don't ___ worry about it.",
    "options": ["A) need to", "B) need", "C) needs to", "D) needing"],
    "answer": "A",
    "explanation": "When used as an ordinary verb with 'don't', 'need' is followed by 'to' + base verb.",
    "theme": "English Grammar"
  },
  {
    "question": "I failed the test. I ___ studied more.",
    "options": ["A) must have", "B) should have", "C) might have", "D) can have"],
    "answer": "B",
    "explanation": "'Should have + PP' is used to express a regret about a past action.",
    "theme": "English Grammar"
  },
  {
    "question": "Her car is not in the driveway. She ___ left already.",
    "options": ["A) should have", "B) might have", "C) must have", "D) cannot have"],
    "answer": "C",
    "explanation": "'Must have + PP' expresses a strong logical deduction about the past.",
    "theme": "English Grammar"
  },
  {
    "question": "I can't find my keys. I ___ dropped them on the street.",
    "options": ["A) must to have", "B) might have", "C) should have", "D) can have"],
    "answer": "B",
    "explanation": "'Might have + PP' expresses a past possibility.",
    "theme": "English Grammar"
  },
  {
    "question": "He ___ stolen the money, he was with me the whole time!",
    "options": ["A) mustn't have", "B) shouldn't have", "C) cannot have", "D) mightn't have"],
    "answer": "C",
    "explanation": "'Cannot have + PP' is the negative logical deduction about the past.",
    "theme": "English Grammar"
  },
  {
    "question": "I will meet you ___ the station.",
    "options": ["A) in", "B) on", "C) at", "D) by"],
    "answer": "C",
    "explanation": "'At' is used for precise points or institutions like the station, school, or work.",
    "theme": "English Grammar"
  },
  {
    "question": "He is currently working ___ France.",
    "options": ["A) at", "B) on", "C) in", "D) into"],
    "answer": "C",
    "explanation": "'In' is used for countries, cities, and enclosed spaces.",
    "theme": "English Grammar"
  },
  {
    "question": "The book is ___ the table.",
    "options": ["A) on", "B) in", "C) at", "D) above"],
    "answer": "A",
    "explanation": "'On' is used for surfaces.",
    "theme": "English Grammar"
  },
  {
    "question": "They opened a new shop ___ Oxford Street.",
    "options": ["A) at", "B) in", "C) on", "D) by"],
    "answer": "C",
    "explanation": "'On' is used for streets.",
    "theme": "English Grammar"
  },
  {
    "question": "Which of the following is correct?",
    "options": ["A) at bed", "B) in bed", "C) on bed", "D) to bed"],
    "answer": "B",
    "explanation": "'In bed' is the correct exception for this enclosed space concept.",
    "theme": "English Grammar"
  },
  {
    "question": "I heard the news ___ TV.",
    "options": ["A) in", "B) at", "C) by", "D) on"],
    "answer": "D",
    "explanation": "'On TV' is an idiomatic exception using 'on'.",
    "theme": "English Grammar"
  },
  {
    "question": "The picture is hanging ___ the sofa.",
    "options": ["A) above", "B) over", "C) on", "D) under"],
    "answer": "A",
    "explanation": "'Above' means a higher position without direct physical contact or movement/covering.",
    "theme": "English Grammar"
  },
  {
    "question": "The cat ran ___ the table.",
    "options": ["A) below", "B) under", "C) at", "D) in"],
    "answer": "B",
    "explanation": "'Under' is used when there is movement or covering involved.",
    "theme": "English Grammar"
  },
  {
    "question": "Our flight leaves ___ 6:00 AM.",
    "options": ["A) in", "B) on", "C) at", "D) by"],
    "answer": "C",
    "explanation": "'At' is used for specific times.",
    "theme": "English Grammar"
  },
  {
    "question": "He likes to read ___ night.",
    "options": ["A) in", "B) on", "C) at", "D) during"],
    "answer": "C",
    "explanation": "'At night' is an exception. (We say 'in the morning', but 'at night').",
    "theme": "English Grammar"
  },
  {
    "question": "We usually go to the beach ___ July.",
    "options": ["A) on", "B) in", "C) at", "D) for"],
    "answer": "B",
    "explanation": "'In' is used for months, years, seasons, and centuries.",
    "theme": "English Grammar"
  },
  {
    "question": "The project will be finished ___ two days.",
    "options": ["A) at", "B) on", "C) in", "D) by"],
    "answer": "C",
    "explanation": "'In' is used to mean 'at the end of a period' (e.g., in two days).",
    "theme": "English Grammar"
  },
  {
    "question": "The meeting is scheduled ___ Monday.",
    "options": ["A) on", "B) in", "C) at", "D) by"],
    "answer": "A",
    "explanation": "'On' is used for days of the week and dates.",
    "theme": "English Grammar"
  },
  {
    "question": "We will have a party ___ 15th August.",
    "options": ["A) in", "B) at", "C) on", "D) from"],
    "answer": "C",
    "explanation": "'On' is used for specific dates.",
    "theme": "English Grammar"
  },
  {
    "question": "I am leaving for Paris ___ tomorrow.",
    "options": ["A) on", "B) in", "C) at", "D) (no preposition)"],
    "answer": "D",
    "explanation": "No preposition is used before 'tomorrow', 'yesterday', or 'today'.",
    "theme": "English Grammar"
  },
  {
    "question": "I go ___ school every morning.",
    "options": ["A) in", "B) at", "C) to", "D) into"],
    "answer": "C",
    "explanation": "'To' indicates direction or destination.",
    "theme": "English Grammar"
  },
  {
    "question": "After work, I usually go ___ home.",
    "options": ["A) at", "B) to", "C) in", "D) (no preposition)"],
    "answer": "D",
    "explanation": "'Home' takes no preposition indicating direction (e.g., 'go home', NOT 'go to home').",
    "theme": "English Grammar"
  },
  {
    "question": "He jumped ___ the swimming pool.",
    "options": ["A) on", "B) into", "C) in", "D) to"],
    "answer": "B",
    "explanation": "'Into' shows movement towards the inside of something.",
    "theme": "English Grammar"
  },
  {
    "question": "The train went ___ the tunnel.",
    "options": ["A) across", "B) through", "C) along", "D) to"],
    "answer": "B",
    "explanation": "'Through' means moving from one side to the other of an enclosed space.",
    "theme": "English Grammar"
  },
  {
    "question": "We walked ___ the street to reach the bakery on the other side.",
    "options": ["A) through", "B) across", "C) along", "D) from"],
    "answer": "B",
    "explanation": "'Across' means moving from one side to the other.",
    "theme": "English Grammar"
  },
  {
    "question": "They were walking ___ the river.",
    "options": ["A) across", "B) along", "C) through", "D) over"],
    "answer": "B",
    "explanation": "'Along' means moving parallel to a line (like a river or a road).",
    "theme": "English Grammar"
  },
  {
    "question": "This book was written ___ an unknown author.",
    "options": ["A) from", "B) with", "C) by", "D) of"],
    "answer": "C",
    "explanation": "'By' is used to introduce the passive agent.",
    "theme": "English Grammar"
  },
  {
    "question": "I usually travel to London ___ plane.",
    "options": ["A) on", "B) by", "C) in", "D) at"],
    "answer": "B",
    "explanation": "'By + noun without article' indicates the means of transport (by plane).",
    "theme": "English Grammar"
  },
  {
    "question": "He was trembling ___ fear when he saw the ghost.",
    "options": ["A) of", "B) with", "C) by", "D) from"],
    "answer": "B",
    "explanation": "'With' is used for cause in expressions like 'trembling with fear'.",
    "theme": "English Grammar"
  },
  {
    "question": "I have been living here ___ two years.",
    "options": ["A) since", "B) for", "C) during", "D) in"],
    "answer": "B",
    "explanation": "'For' is used for a duration (e.g., for two years).",
    "theme": "English Grammar"
  },
  {
    "question": "I have been working here ___ 2020.",
    "options": ["A) for", "B) since", "C) from", "D) in"],
    "answer": "B",
    "explanation": "'Since' indicates the starting point of an action.",
    "theme": "English Grammar"
  },
  {
    "question": "He slept ___ the meeting.",
    "options": ["A) for", "B) during", "C) since", "D) in"],
    "answer": "B",
    "explanation": "'During' is used before a period or an event, never followed by a quantified duration.",
    "theme": "English Grammar"
  },
  {
    "question": "We met some interesting people ___ a bus.",
    "options": ["A) on", "B) by", "C) in", "D) at"],
    "answer": "A",
    "explanation": "'On + article' is used for positioning aboard collective transports (on a bus).",
    "theme": "English Grammar"
  },
  {
    "question": "He arrived ___ a taxi.",
    "options": ["A) by", "B) on", "C) in", "D) at"],
    "answer": "C",
    "explanation": "'In + article' is used for individual vehicles like a car or taxi.",
    "theme": "English Grammar"
  },
  {
    "question": "Most people go to the village ___ foot.",
    "options": ["A) on", "B) by", "C) with", "D) in"],
    "answer": "A",
    "explanation": "'On foot' is the correct exception instead of 'by foot'.",
    "theme": "English Grammar"
  },
  {
    "question": "He heavily depends ___ his parents.",
    "options": ["A) of", "B) from", "C) on", "D) to"],
    "answer": "C",
    "explanation": "'Depend on' is an idiomatic construction in English.",
    "theme": "English Grammar"
  },
  {
    "question": "Are you interested ___ modern art?",
    "options": ["A) on", "B) at", "C) in", "D) by"],
    "answer": "C",
    "explanation": "The correct idiomatic preposition is 'interested in'.",
    "theme": "English Grammar"
  },
  {
    "question": "He is really good ___ mathematics.",
    "options": ["A) at", "B) in", "C) on", "D) with"],
    "answer": "A",
    "explanation": "The idiomatic expression is 'good at'.",
    "theme": "English Grammar"
  },
  {
    "question": "She is terrified, she is afraid ___ the dark.",
    "options": ["A) from", "B) at", "C) of", "D) by"],
    "answer": "C",
    "explanation": "The correct expression is 'afraid of'.",
    "theme": "English Grammar"
  },
  {
    "question": "We are going on vacation ___ next week.",
    "options": ["A) on", "B) in", "C) at", "D) (no preposition)"],
    "answer": "D",
    "explanation": "No preposition is used before 'last', 'next', 'this', or 'every'.",
    "theme": "English Grammar"
  },
  {
    "question": "By the time the firemen arrived, the house ____ down.",
    "options": ["A) had burned", "B) burned", "C) has burned", "D) was burning"],
    "answer": "A",
    "explanation": "L'action s'est terminée avant une autre action au passé (past perfect).",
    "theme": "English Grammar"
  },
  {
    "question": "Never before ____ such a spectacular sunset.",
    "options": ["A) I have seen", "B) have I seen", "C) I saw", "D) did I saw"],
    "answer": "B",
    "explanation": "Inversion obligatoire après 'Never' en début de phrase.",
    "theme": "English Grammar"
  },
  {
    "question": "If I ____ you, I would apply for that job.",
    "options": ["A) was", "B) am", "C) were", "D) had been"],
    "answer": "C",
    "explanation": "Conditionnel irréel du présent, on utilise toujours 'were' à toutes les personnes.",
    "theme": "English Grammar"
  },
  {
    "question": "PIÈGE: If he had caught the train yesterday, he ____ here right now.",
    "options": ["A) would be", "B) would have been", "C) will be", "D) had been"],
    "answer": "A",
    "explanation": "Mixed conditional: condition passée (Type 3) avec conséquence présente (Type 2, right now).",
    "theme": "English Grammar"
  },
  {
    "question": "Not only ____ the exam, but she also got the highest score.",
    "options": ["A) she passed", "B) did she pass", "C) passed she", "D) she did pass"],
    "answer": "B",
    "explanation": "Inversion sujet/auxiliaire après 'Not only' en tête de phrase.",
    "theme": "English Grammar"
  },
  {
    "question": "It was in 1998 ____ he started his own company.",
    "options": ["A) when", "B) which", "C) that", "D) where"],
    "answer": "C",
    "explanation": "Cleft sentence : It is/was [élément souligné] THAT...",
    "theme": "English Grammar"
  },
  {
    "question": "I am not used ____ up so early in the morning.",
    "options": ["A) to wake", "B) to waking", "C) waking", "D) wake"],
    "answer": "B",
    "explanation": "BE USED TO est suivi du gérondif (-ing). C'est une habitude actuelle.",
    "theme": "English Grammar"
  },
  {
    "question": "PIÈGE: He ____ smoke a lot, but he quit last year.",
    "options": ["A) is used to", "B) was used to", "C) used to", "D) would"],
    "answer": "C",
    "explanation": "Habitude révolue. 'Would' ne s'emploie pas ici car c'est un état/une habitude globale sans contexte de temps précis.",
    "theme": "English Grammar"
  },
  {
    "question": "Hardly had I left the building ____ it started to rain.",
    "options": ["A) than", "B) when", "C) that", "D) then"],
    "answer": "B",
    "explanation": "Corrélation: Hardly... when / No sooner... than.",
    "theme": "English Grammar"
  },
  {
    "question": "No sooner had we sat down to eat ____ the phone rang.",
    "options": ["A) than", "B) when", "C) that", "D) then"],
    "answer": "A",
    "explanation": "No sooner est suivi de 'than'.",
    "theme": "English Grammar"
  },
  {
    "question": "I suggest that he ____ a doctor immediately.",
    "options": ["A) sees", "B) see", "C) saw", "D) is seeing"],
    "answer": "B",
    "explanation": "Subjonctif présent en anglais après 'suggest', 'recommend', on utilise la base verbale.",
    "theme": "English Grammar"
  },
  {
    "question": "You ____ be tired after such a long journey! Go to bed.",
    "options": ["A) can", "B) must", "C) should", "D) ought to"],
    "answer": "B",
    "explanation": "Déduction forte / quasi-certitude (must).",
    "theme": "English Grammar"
  },
  {
    "question": "He ____ have committed the crime; he was with me all day.",
    "options": ["A) mustn't", "B) shouldn't", "C) can't", "D) won't"],
    "answer": "C",
    "explanation": "La déduction négative passée se forme avec can't / couldn't + have + PP.",
    "theme": "English Grammar"
  },
  {
    "question": "PIÈGE: Even though the door was locked, he ____ open it.",
    "options": ["A) could", "B) was able to", "C) can", "D) might"],
    "answer": "B",
    "explanation": "Pour une réussite spécifique dans le passé (avec effort), on utilise 'was able to' ou 'managed to', pas 'could'.",
    "theme": "English Grammar"
  },
  {
    "question": "PIÈGE: I look forward ____ you next week.",
    "options": ["A) to see", "B) to seeing", "C) seeing", "D) for seeing"],
    "answer": "B",
    "explanation": "Le 'to' de 'look forward to' est une préposition, il est donc suivi d'un gérondif (-ing).",
    "theme": "English Grammar"
  },
  {
    "question": "She didn't come to the party, ____ was a pity.",
    "options": ["A) what", "B) which", "C) that", "D) it"],
    "answer": "B",
    "explanation": "Le pronom relatif 'which' reprend l'ensemble de la proposition précédente.",
    "theme": "English Grammar"
  },
  {
    "question": "We have been living here ____ ten years.",
    "options": ["A) since", "B) for", "C) during", "D) ago"],
    "answer": "B",
    "explanation": "For + durée (ten years).",
    "theme": "English Grammar"
  },
  {
    "question": "We have been living here ____ 2015.",
    "options": ["A) since", "B) for", "C) in", "D) from"],
    "answer": "A",
    "explanation": "Since + point de départ dans le temps.",
    "theme": "English Grammar"
  },
  {
    "question": "He usually travels ____ train, but today he came ____ foot.",
    "options": ["A) by / by", "B) on / on", "C) by / on", "D) with / by"],
    "answer": "C",
    "explanation": "By train (moyen de transport général) mais on foot (exception).",
    "theme": "English Grammar"
  },
  {
    "question": "PIÈGE: They arrived ____ the airport at 9 PM.",
    "options": ["A) in", "B) at", "C) on", "D) to"],
    "answer": "B",
    "explanation": "On arrive AT un point précis (airport, station) et IN un pays/une ville.",
    "theme": "English Grammar"
  },
  {
    "question": "They arrived ____ Paris yesterday.",
    "options": ["A) at", "B) in", "C) on", "D) to"],
    "answer": "B",
    "explanation": "Arrive IN pour une ville ou un pays.",
    "theme": "English Grammar"
  },
  {
    "question": "PIÈGE: He was born ____ the 15th of August, ____ 1990.",
    "options": ["A) in / in", "B) on / in", "C) at / on", "D) on / on"],
    "answer": "B",
    "explanation": "ON devant un jour précis (15th August), IN devant une année.",
    "theme": "English Grammar"
  },
  {
    "question": "It's strange that she ____ be so rude.",
    "options": ["A) would", "B) should", "C) will", "D) can"],
    "answer": "B",
    "explanation": "Should d'appréciation après des adjectifs comme strange, surprising, odd.",
    "theme": "English Grammar"
  },
  {
    "question": "I ____ to work yesterday because it was a public holiday.",
    "options": ["A) didn't have to go", "B) mustn't go", "C) shouldn't go", "D) haven't to go"],
    "answer": "A",
    "explanation": "L'absence d'obligation au passé (have to). Mustn't exprime l'interdiction, pas l'absence d'obligation.",
    "theme": "English Grammar"
  },
  {
    "question": "The meeting will take place ____ Monday morning.",
    "options": ["A) in", "B) at", "C) on", "D) -"],
    "answer": "C",
    "explanation": "Dès qu'il y a un jour (Monday), la préposition est ON, même s'il est suivi de 'morning'.",
    "theme": "English Grammar"
  },
  {
    "question": "We are going ____ home after work.",
    "options": ["A) at", "B) to", "C) towards", "D) -"],
    "answer": "D",
    "explanation": "Pas de préposition 'to' avant 'home' avec des verbes de mouvement.",
    "theme": "English Grammar"
  },
  {
    "question": "PIÈGE: He works hard, ____?",
    "options": ["A) isn't he", "B) doesn't he", "C) don't he", "D) does he"],
    "answer": "B",
    "explanation": "Question tag avec un verbe d'action au présent régulier (works) nécessite l'auxiliaire do/does.",
    "theme": "English Grammar"
  },
  {
    "question": "Rarely ____ anyone in the office before 8 AM.",
    "options": ["A) I see", "B) see I", "C) do I see", "D) I do see"],
    "answer": "C",
    "explanation": "Inversion avec auxiliaire (do) après un adverbe de sens négatif (Rarely).",
    "theme": "English Grammar"
  },
  {
    "question": "You had better ____ a doctor.",
    "options": ["A) to see", "B) see", "C) seeing", "D) saw"],
    "answer": "B",
    "explanation": "Had better est suivi de la base verbale sans 'to'.",
    "theme": "English Grammar"
  },
  {
    "question": "It's time we ____.",
    "options": ["A) leave", "B) left", "C) to leave", "D) are leaving"],
    "answer": "B",
    "explanation": "It's time / It's high time est suivi du prétérit modal (left).",
    "theme": "English Grammar"
  },
  {
    "question": "PIÈGE: I remember ____ the door, but now it's open!",
    "options": ["A) to lock", "B) locking", "C) lock", "D) having lock"],
    "answer": "B",
    "explanation": "Remember + V-ing = se souvenir d'avoir fait qqch au passé.",
    "theme": "English Grammar"
  },
  {
    "question": "Don't forget ____ the door when you leave.",
    "options": ["A) to lock", "B) locking", "C) lock", "D) locked"],
    "answer": "A",
    "explanation": "Forget / Remember + To-V = penser/oublier de faire qqch (action future par rapport au moment de la pensée).",
    "theme": "English Grammar"
  },
  {
    "question": "PIÈGE: Neither John nor his brothers ____ coming to the party.",
    "options": ["A) is", "B) are", "C) isn't", "D) aren't"],
    "answer": "B",
    "explanation": "Avec 'neither... nor', l'accord se fait avec le sujet le plus proche (his brothers = pluriel).",
    "theme": "English Grammar"
  },
  {
    "question": "____ I open the window? It's hot in here.",
    "options": ["A) Will", "B) Shall", "C) Would", "D) Do"],
    "answer": "B",
    "explanation": "Pour faire une proposition ou demander un avis avec I ou WE, on utilise 'Shall'.",
    "theme": "English Grammar"
  },
  {
    "question": "The book ____ published next month.",
    "options": ["A) is to be", "B) is to", "C) will to be", "D) are being"],
    "answer": "A",
    "explanation": "BE + TO-V exprime un programme officiel, ici au passif 'is to be published'.",
    "theme": "English Grammar"
  },
  {
    "question": "PIÈGE: The committee ____ reached a decision.",
    "options": ["A) have", "B) has", "C) is", "D) are"],
    "answer": "B",
    "explanation": "En anglais américain, et généralement pour l'action du groupe uni, le collectif prend le singulier (has).",
    "theme": "English Grammar"
  },
  {
    "question": "PIÈGE: The police ____ investigating the murder.",
    "options": ["A) is", "B) are", "C) has", "D) does"],
    "answer": "B",
    "explanation": "Le mot 'police' est toujours suivi d'un verbe au pluriel en anglais.",
    "theme": "English Grammar"
  },
  {
    "question": "I would rather you ____ me the truth yesterday.",
    "options": ["A) told", "B) had told", "C) tell", "D) have told"],
    "answer": "B",
    "explanation": "Would rather + sujet + past perfect pour un regret portant sur le passé.",
    "theme": "English Grammar"
  },
  {
    "question": "I would rather ____ at home tonight.",
    "options": ["A) to stay", "B) staying", "C) stay", "D) stayed"],
    "answer": "C",
    "explanation": "Would rather + base verbale sans 'to' quand les sujets sont identiques (I / stay).",
    "theme": "English Grammar"
  },
  {
    "question": "If only I ____ richer!",
    "options": ["A) am", "B) would be", "C) were", "D) have been"],
    "answer": "C",
    "explanation": "If only s'emploie comme wish avec le prétérit modal (were).",
    "theme": "English Grammar"
  },
  {
    "question": "Under no circumstances ____ open this box.",
    "options": ["A) you should", "B) should you", "C) you must", "D) can you to"],
    "answer": "B",
    "explanation": "Inversion après 'Under no circumstances' (adverbe restrictif/négatif en tête).",
    "theme": "English Grammar"
  },
  {
    "question": "PIÈGE: What ____ when you saw him?",
    "options": ["A) did he do", "B) was he doing", "C) had he done", "D) has he done"],
    "answer": "B",
    "explanation": "Action en progression (past continuous) interrompue par une action brève (saw).",
    "theme": "English Grammar"
  },
  {
    "question": "He told me he ____ call me the next day.",
    "options": ["A) will", "B) would", "C) shall", "D) can"],
    "answer": "B",
    "explanation": "Discours indirect au passé: 'will' devient 'would'.",
    "theme": "English Grammar"
  },
  {
    "question": "PIÈGE: If it ____ rain tomorrow, we will cancel the match.",
    "options": ["A) would", "B) will", "C) should", "D) might"],
    "answer": "C",
    "explanation": "If it should rain = S'il venait à pleuvoir (probabilité faible mais Type 1).",
    "theme": "English Grammar"
  },
  {
    "question": "I DO ____ you, believe me!",
    "options": ["A) to love", "B) loving", "C) love", "D) loved"],
    "answer": "C",
    "explanation": "Emphatic DO: suivi de la base verbale pour insister.",
    "theme": "English Grammar"
  },
  {
    "question": "The CEO, along with his managers, ____ expected to attend.",
    "options": ["A) are", "B) is", "C) were", "D) have been"],
    "answer": "B",
    "explanation": "Le sujet est The CEO. 'along with...' est une parenthèse, donc le verbe est au singulier.",
    "theme": "English Grammar"
  },
  {
    "question": "By this time next year, I ____ my studies.",
    "options": ["A) will finish", "B) finish", "C) will have finished", "D) have finished"],
    "answer": "C",
    "explanation": "Future perfect (will have + PP) avec une date butoir (By this time).",
    "theme": "English Grammar"
  },
  {
    "question": "PIÈGE: It's the first time I ____ this movie.",
    "options": ["A) watch", "B) am watching", "C) watched", "D) have watched"],
    "answer": "D",
    "explanation": "Après 'It's the first time', on utilise TOUJOURS le present perfect.",
    "theme": "English Grammar"
  },
  {
    "question": "I object to ____ like a child.",
    "options": ["A) be treated", "B) being treated", "C) treat", "D) treating"],
    "answer": "B",
    "explanation": "Object to + V-ing, ici à la forme passive 'being treated'.",
    "theme": "English Grammar"
  },
  {
    "question": "____ you need any help, please contact the manager.",
    "options": ["A) Would", "B) Could", "C) Should", "D) If only"],
    "answer": "C",
    "explanation": "Inversion de la conditionnelle Type 1: 'Should you need...' = 'If you should need...'.",
    "theme": "English Grammar"
  },
  {
    "question": "Quelle est la différence entre une loi et un règlement ?",
    "options": ["A) Une loi est générale et abstraite, le règlement précise son application", "B) Le règlement est supérieur à la loi", "C) Une loi ne s'applique qu'aux entreprises", "D) Il n'y a pas de différence"],
    "answer": "A",
    "explanation": "La loi fixe les principes généraux, tandis que les règlements les appliquent au niveau technique et administratif.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le rôle principal du Conseil constitutionnel en France ?",
    "options": ["A) Gérer le budget", "B) Contrôler la constitutionnalité des lois", "C) Diriger les administrations", "D) Nommer les juges"],
    "answer": "B",
    "explanation": "Le Conseil constitutionnel veille à la conformité des lois à la Constitution.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Que signifie le principe de laïcité ?",
    "options": ["A) L'État impose une religion", "B) La séparation des Églises et de l'État", "C) L'abolition des droits fondamentaux", "D) L'État ne protège que les croyants"],
    "answer": "B",
    "explanation": "La laïcité garantit la neutralité religieuse de l'État et la liberté de conscience.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le devoir citoyen le plus directement lié au vote ?",
    "options": ["A) Le respect des horaires", "B) La participation politique", "C) Le paiement des impôts", "D) Le port de l'uniforme"],
    "answer": "B",
    "explanation": "Le vote est un acte central de participation à la vie politique et de citoyenneté.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qui est titulaire du pouvoir exécutif en France ?",
    "options": ["A) Le Parlement", "B) Le Président de la République et le Gouvernement", "C) Le Conseil d'État", "D) Le Tribunal administratif"],
    "answer": "B",
    "explanation": "Le pouvoir exécutif est exercé par le Président et le Gouvernement, dans le cadre de la Constitution.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce qu'un citoyen ?",
    "options": ["A) Un individu soumis uniquement aux règles fiscales", "B) Un membre d'une communauté politique jouissant de droits et devoirs", "C) Une personne ayant un passeport", "D) Un fonctionnaire"],
    "answer": "B",
    "explanation": "Le citoyen est inscrit dans une communauté politique et bénéficie de droits, avec des devoirs corrélatifs.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel document fonde les droits fondamentaux en France ?",
    "options": ["A) Le Code civil", "B) La Constitution", "C) Le règlement intérieur", "D) Le code du travail"],
    "answer": "B",
    "explanation": "La Constitution et la Déclaration des droits de l'homme placent les droits fondamentaux au cœur de l'ordre juridique.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Que garantit le principe d'égalité ?",
    "options": ["A) Une égalité totale de fortune", "B) Une égalité devant la loi et l'accès aux droits", "C) L'absence de différences sociales", "D) Une égalité des compétences"],
    "answer": "B",
    "explanation": "L'égalité juridique ne signifie pas l'uniformité des situations, mais une même protection devant la loi.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce qu'une institution ?",
    "options": ["A) Un objet de décoration", "B) Une organisation dotée d'un rôle public", "C) Un simple document administratif", "D) Une loi fiscale"],
    "answer": "B",
    "explanation": "Une institution est une structure organisée qui assure un rôle au sein de la société et de l'État.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le rôle du Parlement ?",
    "options": ["A) Dire le droit en dernier ressort", "B) Élaborer et voter les lois", "C) Nommer les maires", "D) Gérer la police"],
    "answer": "B",
    "explanation": "Le Parlement a pour fonction principale la préparation, le vote et le contrôle des lois.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que la séparation des pouvoirs ?",
    "options": ["A) Un régime où une seule personne détient tous les pouvoirs", "B) Le principe selon lequel le pouvoir exécutif, législatif et judiciaire sont distincts", "C) Un mode d'organisation des partis politiques", "D) La séparation de l'Église et de l'État"],
    "answer": "B",
    "explanation": "La séparation des pouvoirs (Montesquieu) garantit que les pouvoirs législatif, exécutif et judiciaire sont exercés par des organes distincts.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le suffrage universel ?",
    "options": ["A) Le droit de vote réservé aux propriétaires", "B) Le droit de vote accordé à tous les citoyens sans condition de fortune", "C) Le droit de vote réservé aux hommes", "D) Le vote au sein des parlements"],
    "answer": "B",
    "explanation": "Le suffrage universel accorde le droit de vote à tous les citoyens majeurs, sans distinction.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que la présomption d'innocence ?",
    "options": ["A) Toute personne est coupable jusqu'à preuve du contraire", "B) Toute personne est présumée innocente jusqu'à preuve de sa culpabilité", "C) Les accusés n'ont pas droit à un avocat", "D) Les condamnations ne peuvent pas être contestées"],
    "answer": "B",
    "explanation": "La présomption d'innocence est un droit fondamental : nul n'est coupable sans jugement.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce qu'une constitution ?",
    "options": ["A) Un règlement interne d'une entreprise", "B) Un code pénal", "C) La loi fondamentale qui organise l'État et protège les droits fondamentaux", "D) Un traité international"],
    "answer": "C",
    "explanation": "La constitution est la norme suprême d'un État organisant les pouvoirs publics et garantissant les droits fondamentaux.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le droit de grève ?",
    "options": ["A) Le droit de refuser de payer des impôts", "B) Le droit pour les travailleurs de cesser le travail pour défendre leurs intérêts", "C) Le droit de manifester contre le gouvernement", "D) Le droit de quitter son emploi"],
    "answer": "B",
    "explanation": "Le droit de grève est un droit constitutionnel permettant aux travailleurs de cesser le travail collectivement.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle institution ivoirienne contrôle la constitutionnalité des lois ?",
    "options": ["A) Le Tribunal de Première Instance", "B) La Cour d'Appel", "C) Le Conseil constitutionnel", "D) La Cour des Comptes"],
    "answer": "C",
    "explanation": "Le Conseil constitutionnel ivoirien veille à la conformité des lois à la Constitution.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Combien de districts compte la Côte d'Ivoire ?",
    "options": ["A) 10", "B) 12", "C) 14", "D) 33"],
    "answer": "C",
    "explanation": "La Côte d'Ivoire compte 14 districts, dont 2 districts autonomes (Abidjan et Yamoussoukro).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce qu'un référendum ?",
    "options": ["A) Un vote réservé au Parlement", "B) Une procédure par laquelle les citoyens se prononcent directement sur une question", "C) L'élection du Président de la République", "D) Un vote de confiance au gouvernement"],
    "answer": "B",
    "explanation": "Le référendum est un mécanisme de démocratie directe.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le Défenseur des droits en France ?",
    "options": ["A) Il défend la France devant les juridictions internationales", "B) Il protège les droits fondamentaux des citoyens face aux administrations", "C) Il gère le budget de l'État", "D) Il nomme les juges"],
    "answer": "B",
    "explanation": "Le Défenseur des droits veille au respect des droits et libertés des citoyens.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le rôle du Défenseur des droits ?",
    "options": ["A) Il défend la France devant les juridictions internationales", "B) Il protège les droits fondamentaux des citoyens face aux administrations", "C) Il gère le budget de l'État", "D) Il nomme les juges"],
    "answer": "B",
    "explanation": "Le Défenseur des droits veille au respect des droits et libertés des citoyens face aux administrations.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "En quelle année la CI a-t-elle accédé à l'indépendance ?",
    "options": ["A) 1958", "B) 1960", "C) 1962", "D) 1956"],
    "answer": "B",
    "explanation": "La CI a proclamé son indépendance le 7 août 1960.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le premier président de la CI ?",
    "options": ["A) Henri Konan Bédié", "B) Laurent Gbagbo", "C) Félix Houphouët-Boigny", "D) Alassane Ouattara"],
    "answer": "C",
    "explanation": "Félix Houphouët-Boigny est le père fondateur et premier président (1960-1993).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel organe exerce le contrôle de constitutionnalité en CI ?",
    "options": ["A) La Cour Supr?me", "B) Le Conseil constitutionnel", "C) L'Assemblée nationale", "D) Le Sénat"],
    "answer": "B",
    "explanation": "Le Conseil constitutionnel ivoirien veille à la conformité des lois à la Constitution.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Combien de régions compte la CI ?",
    "options": ["A) 19", "B) 26", "C) 31", "D) 33"],
    "answer": "C",
    "explanation": "La CI compte 31 régions et 2 districts autonomes.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le mandat du Président ivoirien ?",
    "options": ["A) 4 ans renouvelable une fois", "B) 5 ans renouvelable une fois", "C) 6 ans renouvelable une fois", "D) 7 ans non renouvelable"],
    "answer": "B",
    "explanation": "La Constitution de 2016 fixe le mandat présidentiel à 5 ans renouvelable une seule fois.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle institution vérifie les comptes de l'État en CI ?",
    "options": ["A) Le Ministère des Finances", "B) La Cour des Comptes", "C) L'Assemblée nationale", "D) La BCEAO"],
    "answer": "B",
    "explanation": "La Cour des Comptes vérifie la régularité des comptes publics.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le rôle du CESEC en CI ?",
    "options": ["A) Voter les lois", "B) Conseiller le gouvernement sur les questions économiques et sociales", "C) Contrôler le gouvernement", "D) Administrer les régions"],
    "answer": "B",
    "explanation": "Le Conseil Économique, Social, Environnemental et Culturel est une assemblée consultative.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Piège : la CI a-t-elle un régime présidentialiste ou semi-présidentiel ?",
    "options": ["A) Présidentialiste pur", "B) Semi-présidentiel avec cohabitation possible", "C) Présidentiel fort : le Président est chef de l'État et du gouvernement", "D) Parlementaire"],
    "answer": "C",
    "explanation": "La Constitution de 2016 instaure un régime présidentiel fort sans cohabitation.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Combien de membres compte le Conseil constitutionnel ivoirien ?",
    "options": ["A) 7", "B) 9", "C) 11", "D) 13"],
    "answer": "B",
    "explanation": "Le Conseil constitutionnel est composé de 9 membres nommés par le Président.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "La hiérarchie des normes en CI est ?",
    "options": ["A) La loi prévaut sur la Constitution", "B) Les traités sont toujours supérieurs à la Constitution", "C) Constitution > lois organiques > lois ordinaires > règlements", "D) Les arrêtés priment sur les décrets"],
    "answer": "C",
    "explanation": "Hiérarchie : Constitution (2016) > lois organiques > lois ordinaires > décrets > arrêtés.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Piège : combien de constitutions la CI a-t-elle eues depuis 1960 ?",
    "options": ["A) 1", "B) 2", "C) 3 : 1960, 2000 et 2016", "D) 4"],
    "answer": "C",
    "explanation": "Trois constitutions : 1960 (indépendance), 2000 (Gbagbo) et 2016 (Ouattara).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Piège : le Sénat de CI peut-il renverser le gouvernement ?",
    "options": ["A) Oui par une motion de censure", "B) Oui en refusant le budget", "C) Non, seule l'Assemblée nationale peut voter une motion de censure", "D) Oui avec l'accord du Conseil constitutionnel"],
    "answer": "C",
    "explanation": "Seule l'Assemblée nationale peut engager la responsabilité du gouvernement.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle est la différence entre décret et ordonnance en droit ivoirien ?",
    "options": ["A) Ce sont des synonymes", "B) Le décret est réglementaire ; l'ordonnance est un acte législatif pris après habilitation parlementaire", "C) L'ordonnance est supérieure au décret", "D) Le décret est pris par le Premier ministre"],
    "answer": "B",
    "explanation": "L'ordonnance a valeur législative (habilitation) ; le décret est réglementaire.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle est la condition de nationalité pour candidater à la présidentielle ivoirienne ?",
    "options": ["A) Être né en CI", "B) Être ivoirien de naissance sans autre nationalité", "C) Être ivoirien de naissance de père et de mère ivoiriens sans autre nationalité", "D) Être naturalisé depuis 10 ans"],
    "answer": "C",
    "explanation": "Article 55 : nationalité ivoirienne de naissance de père et de mère ivoiriens sans autre nationalité.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Piège : un Ivoirien naturalisé étranger peut-il se présenter à la présidentielle ?",
    "options": ["A) Oui s'il renonce avant la candidature", "B) Oui, la double nationalité est tolérée", "C) Non, la Constitution exige de n'avoir jamais eu une autre nationalité", "D) Oui après 10 ans de retour"],
    "answer": "C",
    "explanation": "Article 55 : n'avoir jamais acquis d'autre nationalité. L'acquisition antérieure est rédhibitoire.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que la CEI en CI ?",
    "options": ["A) Un tribunal électoral", "B) L'organe indépendant chargé d'organiser et superviser les élections", "C) Un parti politique", "D) Un organe de l'ONU"],
    "answer": "B",
    "explanation": "La Commission Électorale Indépendante organise et supervise les élections ivoiriennes.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Combien de mandats peut effectuer un président ivoirien ?",
    "options": ["A) Un seul de 7 ans", "B) Deux mandats de 5 ans", "C) Trois mandats de 5 ans", "D) Sans limitation"],
    "answer": "B",
    "explanation": "La Constitution de 2016 limite à deux mandats de 5 ans.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Les étrangers résidents peuvent-ils voter en CI ?",
    "options": ["A) Oui pour les élections locales", "B) Oui après 5 ans de résidence", "C) Non, seuls les citoyens ivoiriens peuvent voter", "D) Oui pour les référendums"],
    "answer": "C",
    "explanation": "Le droit de vote est réservé aux seuls citoyens ivoiriens.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le principal produit d'exportation de la CI ?",
    "options": ["A) Le pétrole", "B) Le cacao", "C) Le diamant", "D) Le café"],
    "answer": "B",
    "explanation": "La CI est le premier producteur mondial de cacao (environ 40 % de la production mondiale).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle monnaie est utilisée en CI ?",
    "options": ["A) Le franc ivoirien", "B) Le franc CFA de l'UEMOA (XOF)", "C) L'euro", "D) Le dollar CEDEAO"],
    "answer": "B",
    "explanation": "Le franc CFA de l'Afrique de l'Ouest (XOF) est géré par la BCEAO.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle organisation gère le franc CFA des pays de l'UEMOA ?",
    "options": ["A) La Banque mondiale", "B) La BCEAO", "C) La BAD", "D) La Banque de France"],
    "answer": "B",
    "explanation": "La BCEAO (Banque Centrale des États de l'Afrique de l'Ouest) siège à Dakar.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "En quelle année la Constitution actuelle de la CI a-t-elle été adoptée ?",
    "options": ["A) 2000", "B) 2011", "C) 2016", "D) 2020"],
    "answer": "C",
    "explanation": "La Constitution de 2016 a été adoptée par référendum le 30 octobre 2016.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le principe de spécialité d'un établissement public ?",
    "options": ["A) Il peut agir dans n'importe quel domaine", "B) Il est limité à la mission précise pour laquelle il a été créé", "C) Il dépend uniquement du ministre", "D) Il peut voter des lois"],
    "answer": "B",
    "explanation": "Le principe de spécialité limite l'action de l'établissement public à l'objet fixé par ses textes.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Piège : qui préside le Conseil supérieur de la magistrature en CI ?",
    "options": ["A) Le Ministre de la Justice", "B) Le Premier Président de la Cour Suprême", "C) Le Président de la République", "D) Le Procureur général"],
    "answer": "C",
    "explanation": "En CI, le CSM est présidé par le Président de la République.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le Médiateur de la République en CI ?",
    "options": ["A) Un juge civil", "B) Une autorité indépendante qui reçoit les réclamations des citoyens contre l'administration", "C) Le président de l'Assemblée nationale", "D) Un représentant du gouvernement"],
    "answer": "B",
    "explanation": "Le Médiateur de la République traite les réclamations des citoyens contre les administrations.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que la distinction SPA et SPIC ?",
    "options": ["A) Aucune différence", "B) SPA = droit administratif ; SPIC = principalement droit privé", "C) SPIC géré par l'État SPA par des privés", "D) SPA génère des profits SPIC non"],
    "answer": "B",
    "explanation": "SPA = droit public. SPIC (eau, électricité) = droit privé pour usagers et personnel.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que la déconcentration administrative en CI ?",
    "options": ["A) Transfert de compétences à des collectivités autonomes", "B) Déplacement de l'autorité de l'État vers ses représentants locaux (préfets, sous-préfets)", "C) Privatisation des services publics", "D) Suppression des ministères régionaux"],
    "answer": "B",
    "explanation": "La déconcentration déplace des pouvoirs au sein de l'État vers ses agents sur le terrain.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle institution forme les hauts fonctionnaires en CI ?",
    "options": ["A) L'ENA", "B) L'Université Félix Houphouët-Boigny", "C) Le Centre de Formation Administrative", "D) La BCEAO"],
    "answer": "A",
    "explanation": "L'ENA de CI forme les hauts fonctionnaires pour les corps préfectoraux, diplomatiques et administratifs.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce qu'un établissement public national (EPN) en CI ?",
    "options": ["A) Une entreprise privée sous contrôle de l'État", "B) Une personne morale de droit public autonome chargée d'une mission de service public", "C) Un ministère", "D) Une collectivité territoriale"],
    "answer": "B",
    "explanation": "Les EPN (ex. CNPS, SODEXAM) sont des personnes morales de droit public autonomes.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que la LOLF en CI ?",
    "options": ["A) Loi organique relative aux lois de finances", "B) Loi sur les libertés fondamentales", "C) Loi sur le livre foncier", "D) Loi contre la fraude"],
    "answer": "A",
    "explanation": "La LOLF est le cadre juridique de la gestion budgétaire moderne orientée vers la performance.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le principe de séparation entre ordonnateur et comptable public ?",
    "options": ["A) Aucun principe en CI", "B) L'agent qui autorise une dépense ne peut pas être celui qui la paie : garantie contre les détournements", "C) Le comptable est supérieur à l'ordonnateur", "D) Ce principe ne s'applique qu'aux grandes villes"],
    "answer": "B",
    "explanation": "Ce principe empêche une même personne d'autoriser et de réaliser une dépense.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Combien de langues et dialectes compte la CI ?",
    "options": ["A) 20-30", "B) 60-70", "C) Plus de 60", "D) 10-15"],
    "answer": "C",
    "explanation": "La CI compte plus de 60 langues et dialectes en 4 grands groupes.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le plus grand groupe ethnique en CI ?",
    "options": ["A) Les Baoulé", "B) Les Dioula", "C) Les Bété", "D) Les Sénoufo"],
    "answer": "A",
    "explanation": "Les Baoulé du groupe Akan sont le groupe ethnique le plus important.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que l'initiative PPTE pour la CI en 2012 ?",
    "options": ["A) Programme de planification économique", "B) Initiative Pays Pauvres Très Endettés : allègement de la dette", "C) Plan de promotion du tourisme", "D) Programme de protection des terres"],
    "answer": "B",
    "explanation": "En 2012, la CI a bénéficié de l'initiative PPTE, obtenant un allègement substantiel de sa dette.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Piège : un acte administratif illégalement signé peut-il être validé ?",
    "options": ["A) Oui par ratification expresse de l'autorité compétente", "B) Non, jamais", "C) Oui automatiquement après 3 mois", "D) Non sauf si le Conseil constitutionnel l'approuve"],
    "answer": "A",
    "explanation": "Certains actes irréguliers peuvent être régularisés par ratification expresse.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que l'ARTCI en CI ?",
    "options": ["A) Un ministère", "B) Une autorité administrative indépendante qui régule les télécommunications et les TIC", "C) Une entreprise publique", "D) Un tribunal spécialisé"],
    "answer": "B",
    "explanation": "L'ARTCI est l'autorité administrative indépendante de régulation du marché des télécommunications.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le nom du processus de décentralisation en CI qui transfère des compétences aux communes ?",
    "options": ["A) La d?concentration", "B) La d?centralisation", "C) La privatisation", "D) La d?l?gation"],
    "answer": "B",
    "explanation": "La décentralisation transfère des compétences et des ressources à des collectivités territoriales autonomes (communes, régions, districts).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le role d un conseil municipal en CI ?",
    "options": ["A) Gerer les affaires de l'?tat central", "B) Deliberer sur les affaires d interet communal et voter le budget de la commune", "C) Nomrme les prefets", "D) Adopter les lois nationales"],
    "answer": "B",
    "explanation": "Le conseil municipal est l assembl?e deliberante de la commune. Il vote le budget et prend les decisions d interet local.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le principe de libre administration des collectivites territoriales en CI ?",
    "options": ["A) Les collectivites peuvent ignorer les lois nationales", "B) Les collectivites gerent librement leurs affaires dans le cadre de la loi sous le controle de l'?tat", "C) Les collectivites peuvent creer leurs propres lois", "D) Les collectivites sont independantes de l'?tat"],
    "answer": "B",
    "explanation": "Le principe de libre administration permet aux collectivites de gerer leurs affaires dans les limites fixees par la loi et sous controle de l'?tat.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle est la diff?rence entre un maire et un pr?fet en CI ?",
    "options": ["A) Aucune diff?rence", "B) Le maire est ?lu par les habitants pour g?rer la commune ; le pr?fet est nomm? par l'?tat pour le repr?senter dans le d?partement", "C) Le prefet est superieur au maire en tout", "D) Le maire est nomme par le gouvernement"],
    "answer": "B",
    "explanation": "Le maire est ?lu local ; le pr?fet est agent de l'?tat nomm? par d?cret. Leurs r?les et l?gitimit?s diff?rent.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce qu'un service d?concentr? de l'?tat ?",
    "options": ["A) Un service prive", "B) Un service de l'?tat implant? localement sous l'autorit? d'un repr?sentant de l'?tat (pr?fet, sous-pr?fet)", "C) Un etablissement public", "D) Une collectivit? territoriale"],
    "answer": "B",
    "explanation": "Les services d?concentr?s (DRE, DRSP, etc.) repr?sentent les minist?res au niveau local sous l'autorit? du pr?fet.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le contr?le de l?gitimit? dans le cadre de la d?centralisation ?",
    "options": ["A) Le controle exerce par les citoyens sur les elus locaux", "B) Le contr?le exerc? par le repr?sentant de l'?tat sur la l?galit? des actes des collectivit?s locales", "C) Le controle financier des collectivites", "D) L audit annuel des collectivites"],
    "answer": "B",
    "explanation": "Le repr?sentant de l'?tat contr?le que les actes des collectivit?s sont conformes ? la loi.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le budget communal en CI ?",
    "options": ["A) Le budget de l'?tat central", "B) Le document financier qui pr?voit les recettes et d?penses de la commune pour l'ann?e", "C) Le budget du departement", "D) Le budget alloue aux fonctionnaires communaux"],
    "answer": "B",
    "explanation": "Le budget communal est vot? par le conseil municipal. Il pr?voit les ressources et les d?penses de la commune.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le financement des collectivites locales en CI ?",
    "options": ["A) Uniquement par l'?tat central", "B) Par les imp?ts locaux, dotations de l'?tat, fonds de d?centralisation et emprunts", "C) Uniquement par les impots locaux", "D) Par les dons internationaux uniquement"],
    "answer": "B",
    "explanation": "Les collectivit?s sont financ?es par une combinaison de ressources propres (imp?ts locaux) et de transferts de l'?tat.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que l'?tat civil en CI ?",
    "options": ["A) Le registre des entreprises", "B) L'enregistrement des faits d'?tat civil (naissances, mariages, d?c?s) qui ?tablit l'identit? juridique des personnes", "C) Le registre des fonctionnaires", "D) La liste electorale"],
    "answer": "B",
    "explanation": "L'?tat civil enregistre les ??v?nements majeurs de la vie (naissances, mariages, d?c?s) et ?tablit l'identit? juridique.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le Tr?sor public en CI ?",
    "options": ["A) La banque centrale", "B) Le service de l'?tat qui g?re les finances publiques : encaissement des recettes et paiement des d?penses", "C) Un organisme prive", "D) La banque du gouvernement"],
    "answer": "B",
    "explanation": "Le Tr?sor public g?re les flux financiers de l'?tat : recettes fiscales, paiement des salaires, remboursement de la dette.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Pi?ge : la Constitution de 2016 a-t-elle supprim? le poste de Premier ministre en CI ?",
    "options": ["A) Oui d?finitivement", "B) Non le poste existe toujours mais ses attributions sont encadr?es par l'organisation institutionnelle", "C) Oui mais il peut etre r?tabli par loi organique", "D) Non le Premier ministre reste chef du gouvernement"],
    "answer": "B",
    "explanation": "La Constitution de 2016 n'a pas supprimé le poste de Premier ministre ; elle a réorganisé l'exécutif et ses équilibres.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que la responsabilit? politique du gouvernement en CI ?",
    "options": ["A) Le gouvernement est responsable devant le Pr?sident uniquement", "B) Le gouvernement est responsable devant l'Assembl?e nationale qui peut le renverser par une motion de censure", "C) Le gouvernement est irresponsable", "D) Le gouvernement est responsable devant le Senat"],
    "answer": "B",
    "explanation": "L'Assembl?e nationale peut engager la responsabilit? du gouvernement par une motion de censure.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Pi?ge : le contr?le parlementaire s'exerce-t-il sur les actes du Pr?sident en CI ?",
    "options": ["A) Oui pleinement comme en r?gime semi-pr?sidentiel", "B) Non en r?gime pr?sidentiel le Pr?sident n est pas responsable devant le Parlement", "C) Oui uniquement sur les questions budg?taires", "D) Non le Parlement ne peut pas questionner le gouvernement"],
    "answer": "B",
    "explanation": "En r?gime pr?sidentiel ivoirien le Pr?sident n est pas responsable devant le Parlement. Seul le gouvernement l est.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le principe de l inamovibilite des magistrats en CI ?",
    "options": ["A) Les magistrats ne peuvent pas etre mutes", "B) Les magistrats du siege ne peuvent pas etre deplactes sanctionnes ou destitues sans leur consentement ou une procedure disciplinaire", "C) Les magistrats ne peuvent pas demissionner", "D) Les magistrats sont nommes a vie"],
    "answer": "B",
    "explanation": "L inamovibilite protege les magistrats du siege contre toute pression : ils ne peuvent etre mutas ou sanctionnes que par procedure disciplinaire.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que la citoyennete ivoirienne confere comme droits politiques ?",
    "options": ["A) Uniquement le droit de vote", "B) Le droit de vote d eligibilite de petition d acces aux fonctions publiques et d exercice des libert?s civiques", "C) Uniquement le droit d acces aux fonctions publiques", "D) Aucun droit politique pour les citoyens ordinaires"],
    "answer": "B",
    "explanation": "La citoyennete ivoirienne confere l ensemble des droits politiques : vote eligibilite libert?s civiques acces aux fonctions publiques.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le droit d asile en CI ?",
    "options": ["A) Le droit pour un Ivoirien de quitter le pays", "B) La protection accordee a un ?tranger persecute dans son pays qui en fait la demande", "C) Le droit de refugier des biens a l ?tranger", "D) L exemption d impots pour les diplomates"],
    "answer": "B",
    "explanation": "Le droit d asile accorde une protection a tout ?tranger qui fuit des persecutions dans son pays d origine.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Pi?ge : la peine de mort est-elle abolie en CI ?",
    "options": ["A) Oui depuis la Constitution de 2016", "B) Non elle est toujours en vigueur pour les crimes les plus graves", "C) Oui depuis 2000", "D) Oui depuis 1960"],
    "answer": "A",
    "explanation": "La Constitution de 2016 a aboli la peine de mort en CI. C est une avancee majeure des droits fondamentaux.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le Parlement ivoirien en matière de contrôle du gouvernement ?",
    "options": ["A) Il ne dispose d'aucun pouvoir de contrôle", "B) Il exerce un contrôle par les questions orales et écrites, commissions d'enquête et motion de censure", "C) Il peut dissoudre le gouvernement à tout moment", "D) Il peut refuser d'appliquer les lois présidentielles"],
    "answer": "B",
    "explanation": "Le Parlement ivoirien contrôle le gouvernement par les questions, les commissions et la motion de censure.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le principe de la neutralité du service public ?",
    "options": ["A) Le service public doit être gratuit", "B) Le service public ne doit pas être influencé par des considérations politiques, religieuses ou idéologiques", "C) Le service public ne peut pas sous-traiter", "D) Le service public doit être géré par des fonctionnaires uniquement"],
    "answer": "B",
    "explanation": "La neutralité du service public garantit que les agents traitent tous les usagers de façon égale sans discrimination.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Piège : un fonctionnaire peut-il militer pour un parti politique en CI ?",
    "options": ["A) Oui totalement sans restriction", "B) Non, un fonctionnaire doit se garder de tout engagement politique ostensible dans l'exercice de ses fonctions", "C) Oui, mais uniquement après les heures de service", "D) Non, aucun fonctionnaire ne peut voter"],
    "answer": "B",
    "explanation": "Le devoir de réserve interdit au fonctionnaire de manifester ostensiblement ses opinions politiques dans l'exercice de ses fonctions.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que la notion d autorite de l'?tat ?",
    "options": ["A) La capacite de l'?tat a emettre des billets de banque", "B) La capacite de l'?tat a imposer le respect de l ordre juridique et a faire executer ses decisions en recourant si necessaire a la contrainte", "C) La capacite de l'?tat a conclure des traites", "D) La capacite de l'?tat a lever des impots"],
    "answer": "B",
    "explanation": "L autorite de l'?tat est sa capacite a maintenir l ordre et a faire respecter la loi en utilisant si necessaire la force legitime.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que la nationalit? ivoirienne par naissance ?",
    "options": ["A) ?tre n? en CI", "B) ?tre n? de p?re ou de m?re ivoirien(ne)", "C) ?tre n? en CI ou d'un parent ivoirien sous conditions", "D) Uniquement ?tre n? de deux parents ivoiriens"],
    "answer": "C",
    "explanation": "La nationalit? ivoirienne par naissance est attribu?e ? ceux n?s en CI dans certaines conditions ou n?s d'un parent ivoirien.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Pi?ge : une personne doublement nationale peut-elle obtenir le statut de refugie en CI ?",
    "options": ["A) Non un national CI ne peut pas etre refugie en CI", "B) Oui si elle prouve la persecution dans son autre pays", "C) Non les doubles nationaux n ont aucun droit au refuge", "D) Oui automatiquement"],
    "answer": "A",
    "explanation": "Un citoyen ivoirien ne peut pas demander le statut de refugie en CI. Le droit d asile protege les ?trangers dans un pays dont ils ne sont pas ressortissants.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle est la duree de la session parlementaire ordinaire en CI ?",
    "options": ["A) 3 mois par an", "B) 6 mois par an en deux sessions", "C) Permanente", "D) 9 mois par an"],
    "answer": "B",
    "explanation": "Le Parlement ivoirien se reunit en deux sessions ordinaires de 3 mois chacune soit 6 mois au total.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Pi?ge : les actes du Pr?sident de la R?publique sont-ils soumis au contr?le du juge administratif ?",
    "options": ["A) Oui pleinement", "B) Non les actes de gouvernement (li?s ? la politique) ?chappent au contr?le juridictionnel mais les actes r?glementaires peuvent ?tre contr?l?s", "C) Non aucun acte pr?sidentiel n'est contr?lable", "D) Oui mais uniquement par le Conseil constitutionnel"],
    "answer": "B",
    "explanation": "Les actes de gouvernement (ex. trait?s, relations diplomatiques) ?chappent au juge administratif. Seuls les actes r?glementaires peuvent ?tre attaqu?s.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le principe d egalite devant le service public ?",
    "options": ["A) Tout le monde paye le meme prix", "B) Tous les usagers dans la meme situation doivent etre traites identiquement par le service public", "C) Tous les services publics sont gratuits", "D) Les fonctionnaires et les usagers ont les memes droits"],
    "answer": "B",
    "explanation": "L egalite devant le service public est une application du principe general d egalite : meme traitement pour les usagers dans des situations identiques.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle est la difference entre une commune de plein exercice et une commune de moyen exercice en CI ?",
    "options": ["A) La taille de la population", "B) Le niveau d autonomie et de competences : une commune de plein exercice dispose d une autonomie plus grande", "C) La localisation geographique", "D) Le montant du budget"],
    "answer": "B",
    "explanation": "En CI les communes sont classees selon leur niveau d autonomie. Les communes de plein exercice ont plus de competences et de ressources.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le principe de neutralité religieuse dans la fonction publique ivoirienne ?",
    "options": ["A) Les fonctionnaires ne peuvent pas pratiquer une religion", "B) Les fonctionnaires ne peuvent pas manifester leurs convictions religieuses dans l'exercice de leurs fonctions", "C) Les fonctionnaires doivent être athées", "D) La religion est interdite dans les locaux administratifs"],
    "answer": "B",
    "explanation": "La neutralité religieuse interdit aux fonctionnaires d'exprimer leurs convictions religieuses dans l'exercice de leurs fonctions.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le principe de gratuité du service public ?",
    "options": ["A) Tous les services publics sont gratuits", "B) Ce principe signifie que le financement du service public ne doit pas reposer uniquement sur les usagers : il peut être financé par les impôts", "C) Les usagers ne paient jamais pour les services publics", "D) Les fonctionnaires travaillent bénévolement"],
    "answer": "B",
    "explanation": "La gratuité du service public ne signifie pas absence de paiement, mais que le service est accessible sans que le prix soit un obstacle dirimant.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle est la distinction entre le préfet et le gouverneur en CI ?",
    "options": ["A) Aucune différence", "B) En CI, depuis 2011, le gouverneur dirige le district autonome (Abidjan, Yamoussoukro) tandis que le préfet dirige le département", "C) Le gouverneur est un rôle historique supprimé", "D) Le gouverneur est élu ; le préfet est nommé"],
    "answer": "B",
    "explanation": "La Constitution de 2011-2016 a créé des districts autonomes dirigés par des gouverneurs nommés par le Président pour les grandes agglomérations.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que la délégation de signature ?",
    "options": ["A) Un fonctionnaire signe à la place d'un autre sans habilitation", "B) Une autorité administrative autorise un de ses subordonnés à signer en son nom certains actes", "C) Le Président délègue ses pouvoirs au Premier ministre", "D) L'Assemblée nationale délègue ses pouvoirs au gouvernement"],
    "answer": "B",
    "explanation": "La délégation de signature permet à un chef de service d'autoriser son subordonné à signer certains actes en son nom. Le délégant reste responsable.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Piège : la délégation de pouvoirs est-elle différente de la délégation de signature ?",
    "options": ["A) Non, ce sont des synonymes", "B) Oui : dans la délégation de pouvoirs le délégataire exerce le pouvoir en son nom propre et le délégant ne peut plus l'exercer ; dans la délégation de signature le délégant reste responsable", "C) Oui : la délégation de pouvoirs est illégale", "D) Non, elles ont les mêmes effets juridiques"],
    "answer": "B",
    "explanation": "Délégation de pouvoirs : transfert du pouvoir lui-même (le délégant ne peut plus exercer). Délégation de signature : seule la signature est transférée, le délégant reste responsable.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle est la différence entre la tutelle administrative et la hiérarchie administrative ?",
    "options": ["A) Aucune différence", "B) La tutelle ne permet que des contrôles de légalité et d'opportunité définis par la loi ; la hiérarchie permet un pouvoir de commandement direct", "C) La hiérarchie s'exerce entre collectivités", "D) La tutelle est plus puissante que la hiérarchie"],
    "answer": "B",
    "explanation": "La hiérarchie = pouvoir de commandement direct. La tutelle = contrôle externe, encadré par la loi.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le principe de la légalité des délits et des peines ?",
    "options": ["A) Les peines sont fixées par le juge librement", "B) Nul ne peut être puni pour un acte qui n'est pas prévu et puni par la loi au moment où il a été commis", "C) Les délits sont définis par le gouvernement", "D) La loi pénale s'applique rétroactivement"],
    "answer": "B",
    "explanation": "« Nullum crimen, nulla poena sine lege » : principe fondamental du droit pénal et constitutionnel.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le droit de pétition en Côte d'Ivoire ?",
    "options": ["A) Le droit de faire une requête à l'administration", "B) Le droit pour les citoyens d'adresser des demandes écrites aux autorités publiques", "C) Le droit de manifester", "D) Le droit de vote"],
    "answer": "B",
    "explanation": "Le droit de pétition permet aux citoyens d'adresser des demandes collectives ou individuelles aux pouvoirs publics.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle est la différence entre le droit privé et le droit public ?",
    "options": ["A) Aucune différence", "B) Le droit public régit les relations entre l'État et les particuliers ; le droit privé régit les relations entre particuliers", "C) Le droit privé est plus important", "D) Le droit public ne s'applique pas aux citoyens"],
    "answer": "B",
    "explanation": "Droit public = État / personnes publiques. Droit privé = relations entre personnes privées.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le principe de l'accès à la justice en Côte d'Ivoire ?",
    "options": ["A) Seuls les riches ont accès à la justice", "B) Tout citoyen a le droit de soumettre un litige à un tribunal et de bénéficier d'un procès équitable", "C) La justice est réservée aux fonctionnaires", "D) Les étrangers n'ont pas accès à la justice"],
    "answer": "B",
    "explanation": "L'accès à la justice est un droit fondamental : tout citoyen peut saisir un tribunal et bénéficier d'un procès équitable.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que la déclaration d'utilité publique (DUP) en CI ?",
    "options": ["A) Un décret qui nationalise une entreprise", "B) Un acte administratif qui reconnaît l'intérêt général d'un projet et autorise l'expropriation si nécessaire", "C) Un document d'inscription d'une association", "D) Un permis de construire"],
    "answer": "B",
    "explanation": "La DUP est la condition préalable à toute expropriation en droit ivoirien.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le rôle du Sénat dans la procédure législative en Côte d'Ivoire ?",
    "options": ["A) Voter le budget national", "B) Examiner et amender les textes de loi adoptés par l'Assemblée nationale", "C) Nommer les juges", "D) Déclarer la guerre"],
    "answer": "B",
    "explanation": "Le Sénat ivoirien examine les lois, propose des amendements, mais l'Assemblée nationale a le dernier mot.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle est la composition du Sénat de Côte d'Ivoire selon la Constitution de 2016 ?",
    "options": ["A) Entièrement élu au suffrage direct", "B) 2/3 élus et 1/3 nommés par le Président", "C) Entièrement nommé par le Président", "D) Moitié élus, moitié tirés au sort"],
    "answer": "B",
    "explanation": "Le Sénat ivoirien : 2/3 des membres sont élus, 1/3 sont nommés par le Président de la République.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le droit à la sécurité sociale en Côte d'Ivoire ?",
    "options": ["A) Le droit d'être armé", "B) Le droit de tout citoyen à des prestations sociales en cas de maladie, vieillesse, maternité ou accident du travail", "C) Le droit à une police privée", "D) Un droit réservé aux fonctionnaires"],
    "answer": "B",
    "explanation": "La sécurité sociale garantit des protections aux travailleurs : gérée par la CNPS en Côte d'Ivoire.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le principe d'inamovibilité des magistrats du siège en CI ?",
    "options": ["A) Ils ne peuvent pas être mutés sans leur accord ou procédure disciplinaire", "B) Ils peuvent être révoqués à tout moment", "C) Ils sont nommés à vie sans possibilité de départ", "D) Ils ne peuvent pas prendre de congés"],
    "answer": "A",
    "explanation": "L'inamovibilité protège l'indépendance des magistrats du siège contre les pressions politiques.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est l'âge minimum pour être élu député à l'Assemblée nationale en Côte d'Ivoire ?",
    "options": ["A) 18 ans", "B) 25 ans", "C) 30 ans", "D) 35 ans"],
    "answer": "B",
    "explanation": "En Côte d'Ivoire, il faut avoir au moins 25 ans pour être candidat à l'Assemblée nationale.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que la responsabilité civile extracontractuelle (délictuelle) ?",
    "options": ["A) La responsabilité née d'un contrat", "B) La responsabilité pour un dommage causé sans relation contractuelle préalable (accident, faute)", "C) La responsabilité pénale", "D) La responsabilité de l'État uniquement"],
    "answer": "B",
    "explanation": "La responsabilité délictuelle (art. 1382 CC français, code ivoirien) s'applique hors contrat : faute → dommage → réparation.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le droit de grève dans la fonction publique ivoirienne ?",
    "options": ["A) Il est totalement interdit", "B) Il est reconnu mais encadré : certains agents ne peuvent y recourir (forces de l'ordre) et un préavis est obligatoire", "C) Il est illimité", "D) Il est réservé aux agents de catégorie A"],
    "answer": "B",
    "explanation": "Le droit de grève existe dans la fonction publique mais il est encadré : préavis, services minimum, interdiction pour certains corps.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le principe de continuité du service public en CI ?",
    "options": ["A) Les services publics ne ferment jamais", "B) Les services publics essentiels doivent fonctionner de manière continue sans interruption injustifiée", "C) Les fonctionnaires ne peuvent pas prendre de congés", "D) Les marchés publics doivent être renouvelés annuellement"],
    "answer": "B",
    "explanation": "La continuité est une des lois de Rolland : les services publics ne doivent pas connaître d'interruptions injustifiées.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le principe de sincérité budgétaire en CI ?",
    "options": ["A) Le budget doit être présenté honnêtement, sans sous-estimation des recettes ni surestimation des dépenses", "B) Le budget doit être voté à l'unanimité", "C) Le budget doit être équilibré", "D) Le budget ne peut pas être modifié en cours d'année"],
    "answer": "A",
    "explanation": "La sincérité budgétaire exige que les prévisions de recettes et de dépenses soient aussi précises et honnêtes que possible.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le Conseil Économique, Social, Environnemental et Culturel (CESEC) de CI ?",
    "options": ["A) Un organe exécutif", "B) Une assemblée consultative qui émet des avis sur les questions économiques, sociales, environnementales et culturelles", "C) Un tribunal spécialisé", "D) Un organe législatif de remplacement"],
    "answer": "B",
    "explanation": "Le CESEC est une institution consultative : le gouvernement peut le consulter mais n'est pas obligé de suivre ses avis.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le droit de propriété en CI ?",
    "options": ["A) Un droit absolu sans aucune restriction", "B) Un droit fondamental garanti par la Constitution, mais susceptible de limitations pour cause d'utilité publique avec indemnisation juste", "C) Un droit réservé aux nationaux ivoiriens", "D) Un droit qui disparaît à la mort du propriétaire"],
    "answer": "B",
    "explanation": "Le droit de propriété est garanti par la Constitution mais peut être limité par l'expropriation pour utilité publique, moyennant indemnisation.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce qu'une loi de finances en Côte d'Ivoire ?",
    "options": ["A) Une loi fiscale ordinaire", "B) La loi qui autorise, pour l'année, la perception des ressources de l'État et fixe les dépenses publiques", "C) Une loi sur les finances des collectivités locales", "D) Une loi sur les investissements étrangers"],
    "answer": "B",
    "explanation": "La loi de finances (budget de l'État) est votée annuellement par le Parlement et encadrée par la LOLF.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle est la durée du mandat sénatorial en Côte d'Ivoire ?",
    "options": ["A) 4 ans", "B) 5 ans", "C) 6 ans", "D) 7 ans"],
    "answer": "C",
    "explanation": "En Côte d'Ivoire, les sénateurs sont élus ou nommés pour 6 ans, renouvelables par moitié tous les 3 ans.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que la décentralisation fiscale en CI ?",
    "options": ["A) L'État perçoit tous les impôts pour les redistribuer", "B) Le transfert aux collectivités territoriales du pouvoir de lever certains impôts locaux pour financer leurs compétences", "C) La suppression des impôts nationaux", "D) La gestion par les banques des impôts locaux"],
    "answer": "B",
    "explanation": "La décentralisation fiscale donne aux collectivités le pouvoir de lever des impôts locaux pour financer leurs activités.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le rôle du Gouverneur dans un district autonome en Côte d'Ivoire ?",
    "options": ["A) Il est élu par les habitants du district", "B) Il est nommé par le Président et représente l'État tout en gérant le district autonome", "C) Il est nommé par le Parlement", "D) Il est choisi par le Conseil municipal"],
    "answer": "B",
    "explanation": "Le Gouverneur d'un district autonome (Abidjan, Yamoussoukro) est nommé par le Président de la République.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que l'égalité des citoyens devant les charges publiques ?",
    "options": ["A) Tous les citoyens paient le même montant d'impôts", "B) Les charges publiques (impôts, obligations) doivent être réparties équitablement selon les capacités", "C) L'État ne peut pas imposer de charges aux citoyens", "D) Seuls les fonctionnaires contribuent aux charges publiques"],
    "answer": "B",
    "explanation": "Ce principe constitutionnel garantit une répartition équitable des charges fiscales et non-fiscales.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle institution ivoirienne protège les droits des consommateurs ?",
    "options": ["A) Le CESEC", "B) La Direction de la Protection du Consommateur et de la Concurrence (DPCC)", "C) La Cour Suprême", "D) L'Assemblée nationale"],
    "answer": "B",
    "explanation": "La DPCC est l'organe administratif chargé de surveiller les pratiques commerciales et protéger les consommateurs en CI.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le Conseil National des Droits de l'Homme (CNDH) de CI ?",
    "options": ["A) Un tribunal", "B) Une institution indépendante chargée de promouvoir et protéger les droits de l'homme en CI", "C) Un ministère", "D) Un organe de l'ONU en CI"],
    "answer": "B",
    "explanation": "Le CNDH est une institution nationale indépendante qui surveille le respect des droits humains et formule des recommandations.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quel est le principe d'impartialité dans le service public ivoirien ?",
    "options": ["A) Les agents peuvent favoriser leurs proches", "B) Les agents doivent traiter tous les usagers sans discrimination ni favoritisme", "C) L'administration n'a pas d'opinion officielle", "D) Les agents ne peuvent pas avoir d'opinions politiques"],
    "answer": "B",
    "explanation": "L'impartialité oblige les agents publics à traiter tous les usagers de manière égale, sans discrimination.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le contrôle de gestion dans l'administration publique ivoirienne ?",
    "options": ["A) Le contrôle policier des fonctionnaires", "B) L'ensemble des processus qui permettent de maîtriser les ressources et d'atteindre les objectifs fixés", "C) L'audit externe uniquement", "D) Le contrôle exercé par le Parlement sur les ministères"],
    "answer": "B",
    "explanation": "Le contrôle de gestion est un outil interne de pilotage de la performance dans l'administration.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le principe de laïcité en Côte d'Ivoire ?",
    "options": ["A) L'État impose le christianisme", "B) L'État est neutre religieusement et garantit la liberté de conscience et de culte", "C) Les religions sont interdites dans l'espace public", "D) L'État subventionne toutes les religions"],
    "answer": "B",
    "explanation": "La Constitution ivoirienne garantit la liberté de conscience et la neutralité religieuse de l'État.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le droit à l'éducation en Côte d'Ivoire ?",
    "options": ["A) Un droit privé facultatif", "B) Un droit fondamental garanti par la Constitution : l'enseignement de base est obligatoire et gratuit", "C) Un droit réservé aux enfants des fonctionnaires", "D) Un droit qui s'achète"],
    "answer": "B",
    "explanation": "La Constitution ivoirienne garantit le droit à l'éducation ; l'enseignement primaire est obligatoire.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le système de l'État unitaire décentralisé adopté par la CI ?",
    "options": ["A) Un État fédéral avec des États autonomes", "B) Un État unique avec des collectivités locales dotées de compétences et d'autonomie propres", "C) Un État sans niveaux de gouvernement locaux", "D) Un État où les régions ont leur propre constitution"],
    "answer": "B",
    "explanation": "La CI est un État unitaire décentralisé : une seule loi nationale mais des collectivités locales autonomes dans leurs domaines.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qu'est-ce que le Fonds de Développement de la Formation Professionnelle (FDFP) en CI ?",
    "options": ["A) Un fonds pour les investissements étrangers", "B) Un organisme paritaire qui finance la formation professionnelle des salariés du secteur privé", "C) Un fonds pour les retraites des fonctionnaires", "D) Une caisse d'assurance maladie"],
    "answer": "B",
    "explanation": "Le FDFP collecte les taxes de formation professionnelle et finance les actions de formation dans le secteur privé ivoirien.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Sous la 3ème République ivoirienne (depuis 2016), le mandat du Président de la République est-il renouvelable ?",
    "options": ["A) Oui, indéfiniment", "B) Oui, une seule fois consécutivement", "C) Non, il est unique", "D) Oui, deux fois"],
    "answer": "B",
    "explanation": "Selon la Constitution de 2016, le mandat est de 5 ans renouvelable une seule fois.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qui assure l'intérim en cas de vacance de la Présidence de la République selon la Constitution de 2016 modifiée en 2020 ?",
    "options": ["A) Le Président de l'Assemblée Nationale", "B) Le Vice-Président de la République", "C) Le Premier Ministre", "D) Le Président du Sénat"],
    "answer": "B",
    "explanation": "Le Vice-Président de la République devient Président de plein droit en cas de vacance.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Combien de membres composent le Conseil Constitutionnel de la Côte d'Ivoire ?",
    "options": ["A) 7 membres", "B) 9 membres", "C) 11 membres", "D) 15 membres"],
    "answer": "A",
    "explanation": "Le Conseil Constitutionnel comprend un Président et six (6) conseillers, soit 7 membres au total.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle est l'institution ivoirienne chargée de la régulation de la communication audiovisuelle ?",
    "options": ["A) La HACA", "B) Le CNP", "C) L'ANP", "D) L'ARTCI"],
    "answer": "A",
    "explanation": "La Haute Autorité de la Communication Audiovisuelle (HACA) régule le secteur audiovisuel.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Le Sénat ivoirien a été mis en place pour la première fois en quelle année ?",
    "options": ["A) 1990", "B) 2000", "C) 2016", "D) 2018"],
    "answer": "D",
    "explanation": "Prévu par la Constitution de 2016, le Sénat a été installé officiellement en 2018.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qui préside le CSM en CI ?",
    "options": ["A) Ministre Justice", "B) Pt Cour Cassation", "C) Président République", "D) Pt Cons Constit"],
    "answer": "C",
    "explanation": "Le Président de la République préside le CSM.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Pilier PND 2021-2025 modernisant l'Etat ?",
    "options": ["A) Pilier 2", "B) Pilier 4", "C) Pilier 6", "D) Pilier 1"],
    "answer": "C",
    "explanation": "Pilier 6 : Gouvernance et modernisation.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Mandat Médiateur de la République ?",
    "options": ["A) 4 ans renouv", "B) 5 ans non renouv", "C) 6 ans non renouv", "D) 6 ans renouv"],
    "answer": "C",
    "explanation": "6 ans non renouvelable.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Organe régulant marchés publics ?",
    "options": ["A) ANRMP", "B) ARCOP", "C) Cour Comptes", "D) BNETD"],
    "answer": "B",
    "explanation": "ARCOP a remplacé l'ANRMP.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Successeur PR en cas de vacance ?",
    "options": ["A) Pt AN", "B) Vice-Président", "C) Premier Ministre", "D) Pt Sénat"],
    "answer": "B",
    "explanation": "Le Vice-Président de la République.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Nombre conseillers Conseil Constit (hors ex-PR) ?",
    "options": ["A) 7", "B) 6", "C) 9", "D) 5"],
    "answer": "B",
    "explanation": "1 Président et 6 Conseillers.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Composition Sénat ivoirien ?",
    "options": ["A) 100% élus", "B) 2/3 élus, 1/3 nommés", "C) 50% élus", "D) 100% nommés"],
    "answer": "B",
    "explanation": "2/3 élus, 1/3 nommé par le PR.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Collectivités territoriales actuelles ?",
    "options": ["A) Région/Commune", "B) District/Commune", "C) Département/Commune", "D) Village/Région"],
    "answer": "A",
    "explanation": "Région et Commune (Loi d'organisation).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qui peut dissoudre l'AN ?",
    "options": ["A) Cons Constit", "B) Premier Ministre", "C) Président Rép", "D) Vice-Président"],
    "answer": "C",
    "explanation": "Le Président de la République.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Juridiction non suprême depuis 2016 ?",
    "options": ["A) Cour Cassation", "B) Conseil Etat", "C) Cour d'Appel", "D) Cour Comptes"],
    "answer": "C",
    "explanation": "La Cour d'Appel est du second degré.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Initiative des lois ?",
    "options": ["A) PR et Députés", "B) PR, Députés et Sénateurs", "C) Gouv seul", "D) Parlement seul"],
    "answer": "B",
    "explanation": "Concurremment PR, Députés, Sénateurs.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Age minimum présidentielle (révision) ?",
    "options": ["A) 40 ans", "B) 35 ans", "C) 45 ans", "D) 30 ans"],
    "answer": "B",
    "explanation": "35 ans minimum.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Mandat Députés ?",
    "options": ["A) 4 ans", "B) 5 ans", "C) 6 ans", "D) 7 ans"],
    "answer": "B",
    "explanation": "5 ans.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Rôle de la HABG ?",
    "options": ["A) Elections", "B) Lutte corruption", "C) Médias", "D) Lois"],
    "answer": "B",
    "explanation": "Haute Autorité pour la Bonne Gouvernance (Anti-corruption).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Loi organique adoptée à :",
    "options": ["A) Maj relative", "B) Maj absolue", "C) Maj 2/3", "D) Unanimité"],
    "answer": "B",
    "explanation": "Majorité absolue des membres de chaque chambre.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Acte signé par le PR ?",
    "options": ["A) Arrêté", "B) Circulaire", "C) Décret Conseil Min", "D) Ordonnance locale"],
    "answer": "C",
    "explanation": "Décrets et ordonnances en Conseil des Ministres.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Naturalisation accordée par :",
    "options": ["A) Juge", "B) Arrêté Min", "C) Décret PR", "D) Loi Parl"],
    "answer": "C",
    "explanation": "Décret présidentiel.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Prorogation état de siège > 15j ?",
    "options": ["A) Cons Constit", "B) Parlement", "C) CSM", "D) Min Défense"],
    "answer": "B",
    "explanation": "Parlement l'autorise.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Régulateur com audiovisuelle ?",
    "options": ["A) HACA", "B) ANP", "C) CNCA", "D) RTI"],
    "answer": "A",
    "explanation": "Haute Autorité de la Com Audiovisuelle.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Principe non constitutionnel CI ?",
    "options": ["A) Laïcité", "B) Décentralisation", "C) Droit grève", "D) Peine de mort"],
    "answer": "D",
    "explanation": "Peine de mort abolie.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Membres du CESEC appelés :",
    "options": ["A) Députés", "B) Conseillers", "C) Sénateurs", "D) Vénérables"],
    "answer": "B",
    "explanation": "Conseillers.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Président CEI est :",
    "options": ["A) Nommé AN", "B) Élu par CEI", "C) Nommé Cons Constit", "D) Nommé PR seul"],
    "answer": "B",
    "explanation": "Élu par les commissaires centraux.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Impôt revenu foncier (IRF) ?",
    "options": ["A) Terrains nus", "B) Loyers bâtis", "C) Achats", "D) Successions"],
    "answer": "B",
    "explanation": "Taxes sur revenus locatifs.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Contrôle financier a posteriori ?",
    "options": ["A) IGF", "B) Trésor", "C) Cour Comptes", "D) Cons Constit"],
    "answer": "C",
    "explanation": "La Cour des Comptes vérifie l'exécution budgétaire.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Révocation requiert avis :",
    "options": ["A) Conseil discipline", "B) Conseil Min", "C) Conseil Etat", "D) Min Tutelle"],
    "answer": "A",
    "explanation": "Le Conseil de discipline pour sanction du 2nd degré.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Saisine Cons Constit (par parlementaires) ?",
    "options": ["A) Tout citoyen", "B) 1/10 membres", "C) Premier Min", "D) Bâtonnier"],
    "answer": "B",
    "explanation": "1/10 des députés ou sénateurs.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Pouvoirs exceptionnels (Art 73) si :",
    "options": ["A) Menace grave + Interruption instit", "B) Baisse PIB", "C) Grève", "D) Rejet budget"],
    "answer": "A",
    "explanation": "Conditions très strictes de menace sur l'Etat.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Révision constitutionnelle via Parlement ?",
    "options": ["A) Refus total", "B) Vote Congrès 2/3", "C) Décret", "D) Cour Cassation"],
    "answer": "B",
    "explanation": "Adoptée par 2/3 du Congrès réuni.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Contreseing décrets PR ?",
    "options": ["A) Aucun", "B) PM et Ministres", "C) Pt Sénat", "D) SGG"],
    "answer": "B",
    "explanation": "PM et ministres concernés (hors pouvoirs propres).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Chambre Rois/Chefs reconnue en :",
    "options": ["A) 1960", "B) 2000", "C) 2016", "D) 2020"],
    "answer": "C",
    "explanation": "Constitution de la IIIe République (2016).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Citoyenneté active ?",
    "options": ["A) Nationalité pure", "B) Respect lois", "C) Participation civique", "D) Impôts"],
    "answer": "C",
    "explanation": "Participation active aux affaires de la cité.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Droit du sol CI ?",
    "options": ["A) 5 ans", "B) 10 ans", "C) Non automatique", "D) 2 ans"],
    "answer": "C",
    "explanation": "Droit du sol pur supprimé (Code nationalité 1972).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Service militaire en CI ?",
    "options": ["A) Obligatoire 18a", "B) Devoir encadré", "C) Supprimé", "D) Pour hommes"],
    "answer": "B",
    "explanation": "Devoir civique, bien que non strictement universel en pratique.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Egalité garantie par Article :",
    "options": ["A) 1", "B) 4", "C) 10", "D) Préambule"],
    "answer": "B",
    "explanation": "Article 4 de la Constitution 2016.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "CDH a remplacé :",
    "options": ["A) CNDHCI", "B) FIDH", "C) MIDH", "D) LIDHO"],
    "answer": "A",
    "explanation": "CNDH a remplacé la CNDHCI.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Défend l'Etat en justice ?",
    "options": ["A) Procureur", "B) Agent Judiciaire Trésor", "C) Bâtonnier", "D) Avocat Gal"],
    "answer": "B",
    "explanation": "L'AJT.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Emblèmes République CI ?",
    "options": ["A) Drapeau Hymne Armoiries", "B) Devise Drapeau Hymne", "C) Drapeau Hymne Armoiries Devise", "D) PR Drapeau"],
    "answer": "C",
    "explanation": "Les 4 emblèmes constitutionnels.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Budget adopté par :",
    "options": ["A) Loi habilitation", "B) Loi organique", "C) Loi finances", "D) Ordonnance"],
    "answer": "C",
    "explanation": "Loi de finances.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Inspecteur Etat dépend de :",
    "options": ["A) PM", "B) PR", "C) Cour Comptes", "D) Min Eco"],
    "answer": "B",
    "explanation": "L'IGE est rattachée à la Présidence.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Désaccord AN / Sénat sur loi :",
    "options": ["A) Abandon", "B) AN décide", "C) Sénat décide", "D) Com Mixte Paritaire"],
    "answer": "D",
    "explanation": "Le Gouv convoque la CMP.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Le vote en CI est :",
    "options": ["A) Droit+Devoir", "B) Pénal", "C) Privilège", "D) Civil"],
    "answer": "A",
    "explanation": "Droit et devoir civique non pénalement sanctionné.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Condition formation partis ?",
    "options": ["A) Respect Chef", "B) <10 ans", "C) Respect Rép/Souveraineté", "D) Sièges région"],
    "answer": "C",
    "explanation": "Respect des principes démocratiques et de la souveraineté.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Délibérations Conseil Ministres ?",
    "options": ["A) Publiques", "B) Secrètes", "C) JO complet", "D) Direct TV"],
    "answer": "B",
    "explanation": "Le secret des délibérations est la règle.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Mariage relève du domaine de :",
    "options": ["A) Loi ordinaire", "B) Constitution", "C) Décret", "D) Coutume"],
    "answer": "A",
    "explanation": "Etat des personnes = loi (Code civil).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Limite âge max PR (2020) ?",
    "options": ["A) 75 ans", "B) 80 ans", "C) Aucune", "D) 70 ans"],
    "answer": "C",
    "explanation": "La limite de 75 ans a sauté en 2016.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Ordre national dirigé par :",
    "options": ["A) Min Intérieur", "B) Grand Chancelier", "C) Pt Sénat", "D) Archevêque"],
    "answer": "B",
    "explanation": "Le Grand Chancelier de l'Ordre.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Mandat arrêt député (session) ?",
    "options": ["A) Accord Pt AN", "B) Accord Bureau AN", "C) Plénière", "D) Aucun"],
    "answer": "B",
    "explanation": "Le Bureau de l'AN lève l'immunité/autorise l'arrestation.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Création Conseil Entente ?",
    "options": ["A) 1959", "B) 1960", "C) 1973", "D) 1975"],
    "answer": "A",
    "explanation": "Mai 1959.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Femme étrangère épouse ivoirien :",
    "options": ["A) Direct", "B) Déclaration (après délai)", "C) Naturalisation 5a", "D) Impossible"],
    "answer": "B",
    "explanation": "Acquisition par déclaration possible après un délai légal.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Mandat conseiller régional ?",
    "options": ["A) 4 ans", "B) 5 ans", "C) 6 ans", "D) 7 ans"],
    "answer": "B",
    "explanation": "Les mandats locaux durent 5 ans.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Selon la Constitution ivoirienne de 2016 (modifiée en 2020), le pouvoir exécutif est :",
    "options": ["A) Monocéphale", "B) Bicéphale (Président de la République et Vice-Président)", "C) Collégial", "D) Exercé exclusivement par le Premier Ministre"],
    "answer": "B",
    "explanation": "L'exécutif est bicéphale, partagé entre le Président de la République et le Vice-Président (et le Premier ministre).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qui fut le premier Président du Sénat ivoirien institué par la Constitution de 2016 ?",
    "options": ["A) Tiemoko Meyliet Koné", "B) Jeannot Ahoussou Kouadio", "C) Chantal Nanaba Camara", "D) Amadou Soumahoro"],
    "answer": "B",
    "explanation": "Jeannot Ahoussou Kouadio a été le premier président du Sénat de Côte d'Ivoire.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "En 2027, la Cour des Comptes de Côte d'Ivoire a pour mission principale :",
    "options": ["A) De juger les conflits entre l'État et les particuliers", "B) Le contrôle supérieur des finances publiques", "C) La validation des candidatures à l'élection présidentielle", "D) L'organisation du référendum"],
    "answer": "B",
    "explanation": "La Cour des Comptes, institution de la République, assure le contrôle des finances publiques et juge les comptes des comptables publics.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Laquelle de ces entités N'EST PAS une collectivité territoriale en Côte d'Ivoire ?",
    "options": ["A) La Région", "B) La Commune", "C) Le Département", "D) Le District Autonome"],
    "answer": "C",
    "explanation": "Depuis la réorganisation, les collectivités territoriales décentralisées sont les Communes et les Régions. Les Districts Autonomes sont des entités particulières déconcentrées et décentralisées, mais le Département n'est plus une collectivité territoriale décentralisée (il est une circonscription administrative).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Le droit du sol en Côte d'Ivoire :",
    "options": ["A) Est la règle absolue pour acquérir la nationalité", "B) A été supprimé par le Code de la nationalité de 1972", "C) S'applique uniquement aux enfants de réfugiés", "D) A été réintroduit par la Constitution de 2016"],
    "answer": "B",
    "explanation": "Le Code de la nationalité ivoirienne de 1972 a supprimé le droit du sol au profit du droit du sang (filiation).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Parmi les emblèmes de la République de Côte d'Ivoire, on compte :",
    "options": ["A) L'éléphant d'or", "B) Le drapeau tricolore, l'hymne, les armoiries et la devise", "C) Le pagne baoulé", "D) La basilique de Yamoussoukro"],
    "answer": "B",
    "explanation": "L'article 29 de la Constitution cite les 4 emblèmes : le Drapeau (Orange, Blanc, Vert), l'Hymne (L'Abidjanaise), la Devise (Union, Discipline, Travail) et les Armoiries.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "La Chambre nationale des Rois et Chefs traditionnels (CNRCT) :",
    "options": ["A) Est une simple association de droit privé", "B) Est une juridiction d'appel", "C) Est reconnue par la Constitution de 2016", "D) A été supprimée en 2020"],
    "answer": "C",
    "explanation": "La Constitution de 2016 consacre l'existence de la CNRCT en tant qu'institution de la République.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qui assure l'intérim de la Présidence de la République en cas de vacance définitive (décès, démission) selon la Constitution ?",
    "options": ["A) Le Président de l'Assemblée Nationale", "B) Le Vice-Président de la République", "C) Le Premier Ministre", "D) Le Président du Conseil Constitutionnel"],
    "answer": "B",
    "explanation": "En cas de vacance, le Vice-Président devient de plein droit Président de la République (art. 62 de la Constitution modifiée).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "La nomination du Vice-Président en Côte d'Ivoire se fait par :",
    "options": ["A) Élection au suffrage universel direct", "B) Le Président de la République, en accord avec le Parlement", "C) Le Conseil Constitutionnel", "D) Le Premier ministre"],
    "answer": "B",
    "explanation": "Depuis la révision constitutionnelle de 2020, le Vice-Président est nommé par le Président de la République avec l'accord du Parlement réuni en Congrès.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Dans le système ivoirien, le contreseing des actes du Président de la République est apposé par :",
    "options": ["A) Le Vice-Président exclusivement", "B) Le Premier ministre et les ministres chargés de l'exécution, pour les actes non dispensés", "C) Le Président du Sénat", "D) Le Président de la Cour Suprême"],
    "answer": "B",
    "explanation": "Les actes du PR, sauf exceptions (nomination PM, etc.), sont contresignés par le PM et les ministres concernés.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Le Sénat ivoirien est composé :",
    "options": ["A) Entièrement de membres élus au suffrage direct", "B) De deux tiers élus au suffrage indirect et d'un tiers nommé par le Président de la République", "C) Entièrement de membres nommés", "D) Exclusivement de représentants de la diaspora"],
    "answer": "B",
    "explanation": "Le Sénat comprend 2/3 de sénateurs élus (suffrage universel indirect) et 1/3 nommés par le Chef de l'État.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle autorité est compétente pour juger la constitutionnalité des lois en Côte d'Ivoire ?",
    "options": ["A) Le Conseil d'État", "B) La Cour de Cassation", "C) Le Conseil Constitutionnel", "D) L'Assemblée Nationale"],
    "answer": "C",
    "explanation": "Le Conseil Constitutionnel est le juge de la constitutionnalité des lois (actuellement présidé par Chantal Nanaba Camara).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Le District Autonome d'Abidjan est :",
    "options": ["A) Une collectivité territoriale ordinaire", "B) Une entité territoriale particulière dotée de la personnalité morale et de l'autonomie financière", "C) Une simple préfecture de police", "D) Un quartier de Yamoussoukro"],
    "answer": "B",
    "explanation": "Les Districts autonomes (Abidjan, Yamoussoukro) jouissent d'un statut particulier (déconcentration et décentralisation).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "L'institution chargée de garantir l'indépendance de la magistrature est :",
    "options": ["A) Le Ministère de la Justice", "B) Le Conseil Supérieur de la Magistrature (CSM)", "C) Le Conseil Constitutionnel", "D) L'ARCOP"],
    "answer": "B",
    "explanation": "Le CSM, présidé par le Président de la République, assiste ce dernier pour garantir l'indépendance de la justice.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Le Médiateur de la République en Côte d'Ivoire :",
    "options": ["A) Est un juge pénal", "B) Est une autorité administrative indépendante chargée de régler les litiges entre l'Administration et les administrés", "C) Dirige la politique étrangère", "D) Valide les traités internationaux"],
    "answer": "B",
    "explanation": "Le Médiateur reçoit les requêtes concernant le fonctionnement des administrations et aide au règlement amiable des conflits.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Le Parlement ivoirien de la 3ème République est :",
    "options": ["A) Monocaméral", "B) Bicaméral (Assemblée Nationale et Sénat)", "C) Tricaméral", "D) Inexistant"],
    "answer": "B",
    "explanation": "La Constitution de 2016 a instauré un Parlement bicaméral composé de l'Assemblée nationale et du Sénat.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Qui a été nommé Vice-Président de la République de Côte d'Ivoire en 2022 ?",
    "options": ["A) Daniel Kablan Duncan", "B) Tiémoko Meyliet Koné", "C) Patrick Achi", "D) Robert Beugré Mambé"],
    "answer": "B",
    "explanation": "Tiémoko Meyliet Koné a été nommé Vice-Président en avril 2022.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "En Côte d'Ivoire, l'initiative des lois appartient concurremment :",
    "options": ["A) Au Président de la République et aux membres du Parlement", "B) Uniquement au Premier Ministre", "C) Au Conseil Constitutionnel et au Sénat", "D) Aux Maires et au Président de la République"],
    "answer": "A",
    "explanation": "L'initiative des lois appartient au Président de la République et aux parlementaires (députés et sénateurs).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "La Loi d'orientation de l'Administration territoriale (1998) a consacré :",
    "options": ["A) La centralisation totale", "B) Les principes de déconcentration et de décentralisation", "C) La suppression des mairies", "D) L'élection des préfets"],
    "answer": "B",
    "explanation": "La loi a organisé l'administration territoriale ivoirienne autour des principes de déconcentration (préfets) et de décentralisation (collectivités locales).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Le mandat du Président de la République en Côte d'Ivoire est actuellement de :",
    "options": ["A) 4 ans", "B) 5 ans, renouvelable une seule fois consécutivement", "C) 7 ans", "D) A vie"],
    "answer": "B",
    "explanation": "Selon la Constitution de 2016, le mandat présidentiel est de 5 ans, et le Président n'est rééligible qu'une seule fois consécutivement.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "En matière de révision de la Constitution, le projet est définitivement adopté :",
    "options": ["A) Exclusivement par référendum", "B) Par référendum, ou par voie parlementaire si le PR décide de le soumettre au Congrès", "C) Par un décret du Conseil d'État", "D) Par le vote des conseils régionaux"],
    "answer": "B",
    "explanation": "Le projet de loi de révision constitutionnelle est soumis au référendum ou, sur décision du Président, au Parlement réuni en Congrès (majorité des 2/3).",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "La Haute Autorité pour la Bonne Gouvernance (HABG) a principalement pour rôle :",
    "options": ["A) La lutte contre la corruption et les infractions assimilées", "B) L'organisation des examens du baccalauréat", "C) La régulation des médias", "D) La nomination des ambassadeurs"],
    "answer": "A",
    "explanation": "La HABG est chargée de la prévention et de la lutte contre la corruption en Côte d'Ivoire.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Le Conseil Économique, Social, Environnemental et Culturel (CESEC) :",
    "options": ["A) Vote le budget de l'État", "B) Donne un avis consultatif sur les projets de loi à caractère économique, social, environnemental ou culturel", "C) Juge les ministres", "D) Gère les réserves forestières"],
    "answer": "B",
    "explanation": "Le CESEC est une assemblée consultative qui donne des avis et mène des études sur ces domaines spécifiques.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Le principe de l'inamovibilité s'applique à quels magistrats en Côte d'Ivoire ?",
    "options": ["A) Les magistrats du Parquet", "B) Les magistrats du Siège", "C) Tous les magistrats (Siège et Parquet)", "D) Uniquement aux juges du Conseil Constitutionnel"],
    "answer": "B",
    "explanation": "Seuls les magistrats du Siège (les juges) bénéficient de l'inamovibilité pour garantir leur indépendance, contrairement au Parquet, soumis à la subordination hiérarchique.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "L'âge minimum pour être candidat à l'élection présidentielle sous la Constitution de 2016 est de :",
    "options": ["A) 40 ans", "B) 35 ans", "C) 45 ans", "D) 50 ans"],
    "answer": "B",
    "explanation": "La Constitution de 2016 a abaissé l'âge minimum d'éligibilité à la Présidence de 40 à 35 ans et a supprimé le plafond d'âge.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Dans la Constitution de 2016, l'école en Côte d'Ivoire est-elle une obligation fondamentale ?",
    "options": ["A) Non, c'est une simple recommandation.", "B) Oui, elle est obligatoire et gratuite pour les enfants des deux sexes jusqu'à l'âge requis.", "C) Elle est obligatoire uniquement pour les garçons.", "D) Elle est obligatoire, mais le financement est exclusivement privé."],
    "answer": "B",
    "explanation": "L'article 10 de la Constitution de 2016 (et modifiée 2020) garantit le droit à l'éducation, et précise que l'école est obligatoire pour tous les enfants des deux sexes. Elle est gratuite dans les établissements publics.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Parmi ces libertés, laquelle est expressément garantie par le Titre I de la Constitution ivoirienne ?",
    "options": ["A) Le droit d'acquérir des armes à feu", "B) La liberté d'association, de réunion et de manifestation", "C) Le droit absolu de refuser l'impôt", "D) L'immunité parlementaire pour tout citoyen"],
    "answer": "B",
    "explanation": "L'article 20 garantit les libertés d'association, de réunion et de manifestation pacifiques.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Selon la Constitution ivoirienne, qui peut saisir le Conseil constitutionnel pour contrôler la conformité d'une loi avant sa promulgation ?",
    "options": ["A) Uniquement le Président de la République", "B) Le PR, les Présidents de l'AN et du Sénat, ou 1/10ème des parlementaires", "C) Tout citoyen sans exception", "D) Le Procureur de la République"],
    "answer": "B",
    "explanation": "Le contrôle de constitutionnalité a priori peut être déclenché par le Président de la République, le Président de l'Assemblée Nationale, le Président du Sénat ou au moins un dixième des députés ou des sénateurs.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Le Médiateur de la République ivoirien peut être saisi :",
    "options": ["A) Pour annuler un jugement d'assises", "B) Pour des différends opposant des personnes physiques ou morales à l'Administration", "C) Pour destituer le Président de la République", "D) Pour lever l'immunité d'un député"],
    "answer": "B",
    "explanation": "Le Médiateur est une AAI chargée de régler à l'amiable les litiges entre les usagers et l'Administration publique.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Dans le processus législatif, si une commission paritaire ne parvient pas à un accord sur un texte (navette parlementaire), qui a le dernier mot en Côte d'Ivoire ?",
    "options": ["A) Le Sénat", "B) L'Assemblée Nationale", "C) Le Conseil d'État", "D) La Haute Autorité pour la Bonne Gouvernance"],
    "answer": "B",
    "explanation": "En cas de désaccord persistant (échec de la commission mixte paritaire), c'est l'Assemblée Nationale (élue au suffrage direct) qui a le dernier mot, sur demande du Président de la République.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "La Haute Autorité pour la Bonne Gouvernance (HABG) a notamment pour mission de :",
    "options": ["A) Recueillir les déclarations de patrimoine des hautes personnalités.", "B) Auditer les partis politiques pendant les campagnes.", "C) Gérer les fonds souverains de l'État.", "D) Nommer les ambassadeurs."],
    "answer": "A",
    "explanation": "L'une des missions centrales de la HABG est la réception, le traitement et la conservation des déclarations de patrimoine des assujettis (ministres, hauts fonctionnaires) pour prévenir l'enrichissement illicite.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Selon la Constitution ivoirienne de 2016, la nomination du Premier Ministre par le Président de la République :",
    "options": ["A) Doit obligatoirement être contresignée par le Vice-Président.", "B) Est un pouvoir propre du Président, exercé sans contreseing.", "C) Nécessite l'approbation préalable de l'Assemblée Nationale.", "D) Est contresignée par le Président du Sénat."],
    "answer": "B",
    "explanation": "La nomination du Premier Ministre est l'un des pouvoirs propres du Chef de l'État (comme la dissolution de l'AN ou le recours au référendum), elle est dispensée du contreseing ministériel.",
    "theme": "Culture Générale — Institutions et citoyenneté"
  },
  {
    "question": "Quelle est la source historique du droit administratif français ?",
    "options": ["A) L'arrêt Blanco", "B) Le droit civil", "C) Le Code pénal", "D) La Constitution de 1848"],
    "answer": "A",
    "explanation": "L'arrêt Blanco (1873) fonde la spécificité du droit administratif français et la responsabilité de l'État.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle juridiction est la plus haute dans l'ordre administratif français ?",
    "options": ["A) Le tribunal judiciaire", "B) Le Conseil d'État", "C) La Cour de cassation", "D) Le tribunal de commerce"],
    "answer": "B",
    "explanation": "Le Conseil d'État est la juridiction suprême de l'ordre administratif en France.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel principe signifie que l'administration doit agir dans le cadre de la loi ?",
    "options": ["A) Le principe de légalité", "B) Le principe de gratuité", "C) Le principe de hiérarchie", "D) Le principe d'efficacité"],
    "answer": "A",
    "explanation": "Le principe de légalité impose à l'administration d'agir conformément à la loi et à la Constitution.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qu'une personne publique ?",
    "options": ["A) Un individu privé", "B) Un organisme de droit public exerçant une mission d'intérêt général", "C) Une entreprise commerciale", "D) Une association de loisirs"],
    "answer": "B",
    "explanation": "Les personnes publiques (État, collectivités, établissements publics) sont à la base de l'organisation administrative.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel est le rôle du préfet ?",
    "options": ["A) Représenter le gouvernement dans le département", "B) Gérer uniquement les impôts", "C) Juger les litiges privés", "D) Diriger les tribunaux administratifs"],
    "answer": "A",
    "explanation": "Le préfet représente l'État au niveau départemental et assure le contrôle administratif.",
    "theme": "Droit administratif"
  },
  {
    "question": "Que signifie le principe de non-rétroactivité de la loi pénale ?",
    "options": ["A) Une loi nouvelle ne peut pas s'appliquer rétroactivement", "B) Une loi ne s'applique qu'après son vote", "C) Une loi peut toujours être appliquée avec effet immédiat", "D) Une loi ne s'applique jamais aux personnes publiques"],
    "answer": "A",
    "explanation": "Le principe de non-rétroactivité est un principe fondamental du droit, surtout en matière pénale.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel acte administratif est généralement pris par le pouvoir exécutif pour un cas particulier ?",
    "options": ["A) La norme générale", "B) L'acte individuel", "C) Le contrat privé", "D) Le code civil"],
    "answer": "B",
    "explanation": "Un acte individuel vise un cas particulier, par exemple une nomination, une autorisation ou une sanction.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le contrôle de légalité ?",
    "options": ["A) Le contrôle de la moralité des agents", "B) Le contrôle de la conformité d'un acte à la loi", "C) Le contrôle de la qualité des produits", "D) Le contrôle du budget privé"],
    "answer": "B",
    "explanation": "Le contrôle de légalité consiste à vérifier si un acte administratif est conforme aux normes supérieures.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qui est le gardien du droit administratif en France ?",
    "options": ["A) La Cour de cassation", "B) Le Conseil d'État", "C) Le ministère de la Justice", "D) Le Tribunal de grande instance"],
    "answer": "B",
    "explanation": "Le Conseil d'État a une place centrale dans l'interprétation et le développement du droit administratif.",
    "theme": "Droit administratif"
  },
  {
    "question": "Que signifie le principe de sécurité juridique ?",
    "options": ["A) L'État peut agir sans limites", "B) Les citoyens doivent pouvoir connaître les règles et leurs conséquences", "C) La loi ne s'applique qu'aux entreprises", "D) L'administration ne doit jamais expliquer ses décisions"],
    "answer": "B",
    "explanation": "La sécurité juridique garantit la prévisibilité du droit et la protection contre l'arbitraire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le service public selon le droit administratif ?",
    "options": ["A) Toute entreprise commerciale", "B) Une activite d interet general assuree ou controlee par la puissance publique", "C) Un service rendu uniquement aux fonctionnaires", "D) Un tribunal administratif"],
    "answer": "B",
    "explanation": "Le service public est une activite d interet general prise en charge par une personne publique.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel principe du service public signifie qu il doit fonctionner sans interruption ?",
    "options": ["A) Le principe de mutabilite", "B) Le principe de continuite", "C) Le principe d egalite", "D) Le principe de neutralite"],
    "answer": "B",
    "explanation": "La continuite du service public impose que le service ne soit pas interrompu.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel principe du service public impose son adaptation aux besoins de la societe ?",
    "options": ["A) La neutralite", "B) L egalite", "C) La mutabilite", "D) La gratuite"],
    "answer": "C",
    "explanation": "Le principe de mutabilite oblige le service public a evoluer en fonction des besoins.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qu un etablissement public ?",
    "options": ["A) Une entreprise privee", "B) Une personne morale de droit public chargee d une mission de service public", "C) Un tribunal administratif", "D) Un service deconcentre"],
    "answer": "B",
    "explanation": "Un etablissement public est une personne morale de droit public gerant une mission de service public.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle est la difference entre d?concentration et d?centralisation ?",
    "options": ["A) Aucune", "B) La d?concentration transfere des pouvoirs a des agents de l'?tat, la d?centralisation a des collectivites autonomes", "C) La d?centralisation est au profit des agents de l'?tat", "D) La d?concentration concerne uniquement les communes"],
    "answer": "B",
    "explanation": "La d?concentration deplace des competences au sein de l'?tat, la d?centralisation les transfere a des entites distinctes.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qu un recours pour exces de pouvoir ?",
    "options": ["A) Un recours visant a obtenir une indemnite", "B) Un recours en annulation d un acte administratif illegal", "C) Un recours contre les decisions judiciaires", "D) Un recours en interpr?tation"],
    "answer": "B",
    "explanation": "Le recours pour exces de pouvoir permet l annulation d un acte administratif illegal.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la hi?rarchie des normes ?",
    "options": ["A) L organisation des minist?res", "B) L organisation pyramidale des regles juridiques, avec la Constitution au sommet", "C) Le classement des juges par anciennete", "D) L ordre alphabetique des lois"],
    "answer": "B",
    "explanation": "La hi?rarchie des normes place la Constitution au sommet, suivie des traites, des lois et des r?glements.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la responsabilite sans faute de l'?tat ?",
    "options": ["A) L ?tat ne peut jamais etre condamne", "B) L ?tat peut etre condamne a indemniser meme sans avoir commis de faute", "C) La responsabilite personnelle des fonctionnaires", "D) L ?tat est responsable uniquement des accidents"],
    "answer": "B",
    "explanation": "La responsabilite sans faute repose sur le principe d egalite devant les charges publiques.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qu un acte unilateral de l administration ?",
    "options": ["A) Un acte signe par deux parties", "B) Un acte par lequel l administration cree des obligations sans le consentement du destinataire", "C) Un contrat administratif", "D) Une loi votee par le Parlement"],
    "answer": "B",
    "explanation": "L acte unilateral est pris par l administration seule et s impose aux administres sans leur consentement.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qu un contrat administratif ?",
    "options": ["A) Un contrat entre deux entreprises privees", "B) Un contrat conclu par une personne publique dans le cadre d une mission de service public", "C) Un acte unilateral de l administration", "D) Un accord entre deux ?tats"],
    "answer": "B",
    "explanation": "Le contrat administratif implique au moins une personne publique et presente des clauses exorbitantes du droit commun.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle est la procedure de revision constitutionnelle en CI ?",
    "options": ["A) Uniquement par r?f?rendum", "B) Par le Parlement seul a la majorite simple", "C) Par le Parlement a la majorite des 3/5 ou par r?f?rendum a l initiative du Pr?sident", "D) Par le Conseil constitutionnel"],
    "answer": "C",
    "explanation": "La revision peut etre adoptee par le Parlement (3/5) ou soumise a r?f?rendum.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qu une loi organique en droit ivoirien ?",
    "options": ["A) Une loi votee par r?f?rendum", "B) Une loi qui precise la Constitution dans les domaines qu elle designe expressement", "C) Une loi adoptee a l unanimite", "D) Un decret du Pr?sident"],
    "answer": "B",
    "explanation": "Les lois organiques completent la Constitution et sont superieures aux lois ordinaires.",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : le preambule de la Constitution de 2016 a-t-il une valeur juridique ?",
    "options": ["A) Non c est un simple texte declaratoire", "B) Oui il fait partie du bloc de constitutionnalit?", "C) Non seul le corps de la Constitution a force contraignante", "D) Oui mais uniquement pour les lois penales"],
    "answer": "B",
    "explanation": "Le preambule est integre au bloc de constitutionnalit? et peut servir de base a la censure d une loi.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de non-retroactivite des actes administratifs ?",
    "options": ["A) Un acte ne peut pas etre abroge", "B) Un acte administratif ne peut produire d effets que pour l avenir pas pour le passe", "C) Les actes s appliquent uniquement aux ?trangers", "D) Les r?glements ne s appliquent qu au moment de leur signature"],
    "answer": "B",
    "explanation": "L acte administratif prend effet a sa publication. Il ne peut pas s appliquer retroactivement.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe du contradictoire en procedure administrative ?",
    "options": ["A) L administration peut decider sans informer l administre", "B) Avant toute decision defavorable l administre doit pouvoir presenter ses observations", "C) L administre peut contredire toutes les decisions", "D) Les fonctionnaires peuvent refuser les ordres"],
    "answer": "B",
    "explanation": "Garantie fondamentale : avant toute decision qui lui fait grief l administre doit pouvoir s expliquer.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle est la difference entre recours gracieux et recours hierarchique ?",
    "options": ["A) Ce sont des synonymes", "B) Recours gracieux adresse a l auteur de l acte ; recours hierarchique adresse au superieur", "C) Le recours gracieux va devant un juge", "D) Le hierarchique est plus rapide"],
    "answer": "B",
    "explanation": "Gracieux : on demande a l auteur de retirer son acte. Hierarchique : on demande a son superieur de l annuler.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que l exception d illegalite en droit administratif ?",
    "options": ["A) Impossibilite d attaquer un acte apres 2 mois", "B) La possibilite de soulever l illegalite d un acte r?glementaire de facon incidente lors d un litige meme hors delai de recours", "C) L annulation automatique de tout acte illegal", "D) Un recours special devant le Conseil constitutionnel"],
    "answer": "B",
    "explanation": "L exception d illegalite est imprescriptible pour les actes r?glementaires.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le pouvoir discrecionnaire de l administration ?",
    "options": ["A) Le droit d agir en dehors de la loi", "B) La liberte de choix dont dispose l administration dans les limites fixees par la loi", "C) Le droit de ne pas repondre aux requetes", "D) La possibilite d ignorer les jugements"],
    "answer": "B",
    "explanation": "Le pouvoir discrecionnaire permet de choisir comment agir dans un cadre legal.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelles sont les trois lois de Rolland du service public ?",
    "options": ["A) Gratuite impartialite efficacite", "B) Continuite egalite mutabilite", "C) Rapidite transparence accessibilite", "D) Neutralite gratuite universalite"],
    "answer": "B",
    "explanation": "Lois de Rolland : continuite (pas d interruption) egalite (traitement egaux) mutabilite (adaptation aux besoins).",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : le service public peut-il etre gere par une personne privee ?",
    "options": ["A) Non seul l'?tat peut gerer un service public", "B) Oui via la delegation de service public (concession affermage)", "C) Oui mais uniquement les services industriels", "D) Non c est inconstitutionnel"],
    "answer": "B",
    "explanation": "La d?l?gation de service public permet de confier la gestion a un prive.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qu un contrat de concession de service public ?",
    "options": ["A) Un contrat de travail d un fonctionnaire", "B) Un contrat par lequel une personne publique confie a un prive la gestion d un service public a ses risques et perils", "C) Un accord international", "D) Un marche public de fournitures"],
    "answer": "B",
    "explanation": "Le concessionnaire est remunere par les usagers et assume le risque d exploitation.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle est la distinction fondamentale entre marche public et delegation de service public ?",
    "options": ["A) Aucune distinction", "B) Marche public : remuneration par l administration ; delegation : remuneration par les usagers ou les resultats", "C) Marche public = travaux delegation = services", "D) La d?l?gation s applique uniquement aux communes"],
    "answer": "B",
    "explanation": "La difference : le mode de remuneration et le transfert du risque d exploitation.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que l IGE en CI ?",
    "options": ["A) Un tribunal administratif", "B) Un corps de controle charge d inspecter les services de l'?tat et de lutter contre la corruption", "C) Le service de securite de la presidence", "D) Un organe de l Assemblee nationale"],
    "answer": "B",
    "explanation": "L Inspection Generale d ?tat placee aupres du Pr?sident controle l utilisation des ressources publiques.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la titularisation dans la fonction publique ivoirienne ?",
    "options": ["A) Le recrutement initial", "B) La confirmation definitive du statut de fonctionnaire apres la periode de stage", "C) La promotion a un grade superieur", "D) La mutation vers une autre administration"],
    "answer": "B",
    "explanation": "La titularisation met fin au statut de stagiaire et confere le statut definitif de fonctionnaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : un fonctionnaire peut-il refuser d obeir a un ordre manifestement illegal ?",
    "options": ["A) Non l obeissance hierarchique est absolue", "B) Oui il peut et doit refuser un ordre manifestement illegal comprometant serieusement un interet public", "C) Oui mais uniquement avec accord du syndicat", "D) Non il doit obeir et signaler apres"],
    "answer": "B",
    "explanation": "Le devoir de refuser un ordre manifestement illegal est un principe fondamental de la deontologie fonctionnaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la disponibilite dans la fonction publique ivoirienne ?",
    "options": ["A) La periode de conge annuel", "B) La position ou un fonctionnaire cesse temporairement ses fonctions sans perdre son statut", "C) Le droit au teletravail", "D) Une sanction disciplinaire"],
    "answer": "B",
    "explanation": "La disponibilite est une position administrative temporaire sans remuneration de l'?tat.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le detachement dans la fonction publique ?",
    "options": ["A) La mise a la retraite anticipee", "B) La position du fonctionnaire qui exerce dans une autre administration en conservant ses droits dans son corps d origine", "C) Une mutation definitive", "D) Un conge pour raisons personnelles"],
    "answer": "B",
    "explanation": "Le detachement : exercice temporaire ailleurs avec conservation des droits dans le corps d origine.",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge tres difficile : un acte nul et un acte inexistant sont-ils identiques ?",
    "options": ["A) Oui synonymes", "B) Non : l acte nul a une apparence juridique et doit etre annule ; l acte inexistant n a aucune valeur et peut etre ignore", "C) Oui memes effets juridiques", "D) Non l acte inexistant entraine des sanctions penales"],
    "answer": "B",
    "explanation": "Acte nul : existe juridiquement mais vicie doit etre annule. Acte inexistant : aucune realite juridique.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le recours en cassation devant la chambre administrative de la Cour Supr?me ?",
    "options": ["A) Un appel qui rejuge les faits", "B) Un recours qui controle uniquement la legalite de la decision sans reexaminer les faits", "C) Un recours reserve aux ?trangers", "D) Un recours en responsabilite de l'?tat"],
    "answer": "B",
    "explanation": "La cassation verifie que la loi a ete correctement appliquee sans rejuger les faits.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de proportionnalite dans l action administrative ?",
    "options": ["A) L administration traite les fonctionnaires proportionnellement a leur salaire", "B) Les mesures de l administration doivent etre adaptees et proportionnees a l objectif poursuivi", "C) Les taxes sont proportionnelles aux revenus", "D) Les sanctions sont proportionnelles au grade"],
    "answer": "B",
    "explanation": "La proportionnalite empeche les mesures excessives par rapport au but recherche.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le detournement de pouvoir en droit administratif ?",
    "options": ["A) Utiliser un droit dans un but autre que celui pour lequel il a ete accorde", "B) Refuser d appliquer la loi", "C) Depasser son budget", "D) Utiliser un droit legal de facon financierement abusive"],
    "answer": "A",
    "explanation": "Detournement de pouvoir : une autorite utilise un pouvoir legal a des fins autres que celles prevues.",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : la force majeure exonere-t-elle toujours l'?tat de sa responsabilite ?",
    "options": ["A) Oui toujours et totalement", "B) Non l'?tat reste responsable pour certains services dangereux meme en cas de force majeure", "C) Oui si l evenement est imprevisible et irresistible", "D) Non la force majeure n existe pas en droit administratif"],
    "answer": "B",
    "explanation": "Pour les activites dangereuses la responsabilite sans faute peut subsister meme en cas de force majeure.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de continuite de l'?tat ?",
    "options": ["A) L ?tat dure indefiniment et ses engagements subsistent au-dela des gouvernements successifs", "B) Le Pr?sident ne peut pas demissionner", "C) Les lois ne peuvent pas etre abrogees", "D) Les fonctionnaires restent en poste independamment des ?lections"],
    "answer": "A",
    "explanation": "La continuite de l'?tat : ses engagements juridiques et financiers subsistent malgre les changements de gouvernement.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la faute personnelle detachable du service ?",
    "options": ["A) Un fonctionnaire ne peut jamais etre poursuivi penalement", "B) La faute grave qui revele un comportement incompatible avec les obligations du service exposant le fonctionnaire a des poursuites", "C) Seul le ministre peut etre poursuivi", "D) La faute personnelle engage l'?tat"],
    "answer": "B",
    "explanation": "La faute personnelle detachable engage la responsabilite personnelle du fonctionnaire (ex corruption violence deliberee).",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : l annulation d un acte administratif par le juge a-t-elle un effet retroactif ?",
    "options": ["A) Non l annulation ne vaut que pour l avenir", "B) Oui l annulation a un effet retroactif : l acte est cense n avoir jamais existe", "C) Oui mais seulement pour les actes individuels", "D) Non sauf si le juge le decide expressement"],
    "answer": "B",
    "explanation": "L annulation par le juge administratif a un effet retroactif (ex tunc) : l acte est cense n avoir jamais produit d effets.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe d egalite de traitement dans la fonction publique ?",
    "options": ["A) Tous les fonctionnaires ont le meme salaire", "B) Des agents dans des situations identiques doivent etre traites de maniere identique sans discrimination", "C) Le meme travail est effectue par le meme nombre d agents", "D) Tous les grades sont equivalents"],
    "answer": "B",
    "explanation": "Le principe d egalite de traitement interdit toute discrimination dans la gestion des carrieres.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le controle de legalite interne d un acte administratif ?",
    "options": ["A) Verifier la signature", "B) Verifier le fond : le but les motifs de droit et de fait et l objet de l acte", "C) Verifier si l acte a ete publie", "D) Verifier la competence de l auteur"],
    "answer": "B",
    "explanation": "Le controle interne porte sur le fond : but motifs de droit motifs de fait contenu.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le pouvoir de tutelle administrative en CI ?",
    "options": ["A) La supervision des orphelins", "B) Le controle exerce par l'?tat sur les collectivites locales et EPN pour garantir la legalite", "C) La supervision des entreprises ?trangeres", "D) Le controle du Pr?sident sur les ministres"],
    "answer": "B",
    "explanation": "La tutelle administrative permet a l'?tat de controler les actes des collectivites locales et EPN.",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : un fonctionnaire detache peut-il etre discipline par son administration d accueil ET son corps d origine ?",
    "options": ["A) Non seule l administration d accueil est competente", "B) Non seul le corps d origine l est", "C) Oui : administration d accueil pour fautes liees au poste ; corps d origine pour manquements au statut", "D) Oui les deux peuvent sanctionner pour les memes faits"],
    "answer": "C",
    "explanation": "La discipline en detachement est partagee selon la nature de la faute.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la responsabilite de l'?tat du fait des lois ?",
    "options": ["A) L ?tat ne peut jamais etre condamne pour une loi", "B) Une loi ne peut pas engager la responsabilite de l'?tat", "C) L ?tat peut etre condamne si une loi cause un prejudice anormal et special meme si elle est legale", "D) Seul le Parlement est responsable des lois"],
    "answer": "C",
    "explanation": "Responsabilite sans faute du legislateur : meme une loi valide peut creer une rupture d egalite devant les charges publiques.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de bonne foi dans l administration publique ?",
    "options": ["A) Les agents doivent etre de confession chretienne", "B) L administration doit agir avec loyaute et sincerite dans ses relations avec les administres", "C) Les contrats administratifs n engagent pas l administration", "D) Les agents doivent croire en leur mission"],
    "answer": "B",
    "explanation": "La bonne foi implique que l administration agit loyalement et respecte les expectatives legitimes creees.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe d accessibilite du service public ?",
    "options": ["A) Le service doit etre gratuit pour tous", "B) Le service doit etre physiquement et financierement accessible a tous les usagers de maniere egale", "C) Le service doit etre disponible 24h/24", "D) Le service doit etre numerique"],
    "answer": "B",
    "explanation": "L accessibilite est une expression du principe d egalite : le service public doit etre accessible a tous sans discrimination.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qu un acte r?glementaire en droit administratif ?",
    "options": ["A) Un acte individuel visant une personne nommement designee", "B) Un acte a portee generale et impersonnelle qui s applique a tous", "C) Un acte du Parlement", "D) Un acte des collectivites locales uniquement"],
    "answer": "B",
    "explanation": "L acte r?glementaire a une portee generale : il s applique a toutes les personnes dans la situation qu il definit.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle est la difference entre un acte administratif unilateral et un contrat administratif ?",
    "options": ["A) Aucune diff?rence", "B) L acte unilateral est impose sans consentement du destinataire ; le contrat implique un accord de volontes entre les parties", "C) Le contrat est superieur a l acte unilateral", "D) L acte unilateral est reserved au Pr?sident"],
    "answer": "B",
    "explanation": "L acte unilateral s impose sans accord ; le contrat resulte d un accord de volontes entre personne publique et cocontractant.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la prescription quadriennale des creances contre l'?tat ?",
    "options": ["A) L ?tat doit payer ses dettes en 4 mois", "B) Les creances non reclamees contre l'?tat se prescrivent (s eteignent) apres 4 ans", "C) Les impots non payes se prescrivent apres 4 ans", "D) Les contrats administratifs expirent apres 4 ans"],
    "answer": "B",
    "explanation": "La prescription quadriennale (4 ans en droit francais inspire le droit ivoirien) eteint les creances non reclamees contre l'?tat.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qu un acte administratif declaratif ?",
    "options": ["A) Un acte qui cree des droits nouveaux", "B) Un acte qui constate l existence d une situation juridique prexistante sans creer de droits nouveaux", "C) Un acte qui punit un administre", "D) Un acte qui nomme un fonctionnaire"],
    "answer": "B",
    "explanation": "Un acte declaratif (ex diplome reconnaissance de nationalit?) constate ; il ne cree pas de droits nouveaux contrairement a l acte constitutif.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le droit de retrait d un acte administratif ?",
    "options": ["A) L administre peut retirer son dossier", "B) L administration peut supprimer retroactivement un acte illegal dans un delai limite", "C) L administre peut ignorer un acte avec lequel il n est pas d accord", "D) L annulation par un juge"],
    "answer": "B",
    "explanation": "Le droit de retrait permet a l autorite administrative de supprimer retroactivement un acte illegal. Le delai est en general de 4 mois.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que l abrogation d un acte administratif ?",
    "options": ["A) L annulation retroactive par un juge", "B) La suppression de l acte pour l avenir seulement sans retroactivite", "C) La modification de l acte", "D) Le remplacement de l acte par un autre"],
    "answer": "B",
    "explanation": "L abrogation supprime l acte pour l avenir (ex nunc), contrairement au retrait qui est retroactif (ex tunc).",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : retrait et abrogation d un acte administratif ont-ils les memes effets ?",
    "options": ["A) Oui identiques", "B) Non : retrait = effet retroactif (l acte est cense n avoir jamais existe) ; abrogation = effet seulement pour l avenir", "C) Le retrait est plus favorable a l administre", "D) L abrogation est plus grave que le retrait"],
    "answer": "B",
    "explanation": "Retrait = retroactif (ex tunc). Abrogation = pour l avenir (ex nunc).",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de la securite des relations juridiques ?",
    "options": ["A) L ?tat garantit la securite physique des citoyens", "B) Les relations juridiques etablies ne peuvent pas etre remises en cause indefiniment ; il faut des delais de stabilisation", "C) Les contrats ne peuvent pas etre modifies", "D) Les lois ne peuvent pas etre changees"],
    "answer": "B",
    "explanation": "La securite juridique exige que les relations et les actes acquierent une certaine stabilite apres expiration des delais de recours.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que l erreur manifeste d appreciation en droit administratif ?",
    "options": ["A) Une erreur de calcul dans un acte administratif", "B) Une erreur grossiere dans l appreciation des faits par l administration qui entraine l illegalite de l acte", "C) Une faute professionnelle d un fonctionnaire", "D) Un acte redige avec des erreurs de forme"],
    "answer": "B",
    "explanation": "L erreur manifeste d appreciation est un controle restreint du juge : il censure les erreurs grossieres dans l appreciation des faits par l administration.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le pouvoir de substitution d action en droit administratif ?",
    "options": ["A) Remplacer un agent par un autre", "B) Le pouvoir du superieur de se substituer a l autorite inferieure defaillante pour agir a sa place", "C) Le droit de l administre de faire appel", "D) La d?l?gation de signature"],
    "answer": "B",
    "explanation": "La substitution d action permet au superieur (ex prefet) d agir a la place d une autorite locale defaillante pour garantir l execution des obligations legales.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de la responsabilite pour risque en droit administratif ?",
    "options": ["A) L ?tat est responsable uniquement si ses agents ont commis une faute", "B) L ?tat est responsable du simple fait de la creation d une situation dangereuse meme sans faute", "C) L ?tat n est jamais responsable pour risque", "D) La responsabilite pour risque n existe qu en droit priv?"],
    "answer": "B",
    "explanation": "La responsabilite pour risque engage l'?tat du fait d activites dangereuses (armes explosifs) meme en l absence de faute.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la Commission Administrative Paritaire (CAP) dans la fonction publique ivoirienne ?",
    "options": ["A) Un tribunal pour fonctionnaires", "B) Un organisme consultatif paritaire (autant d elus du personnel que de representants de l administration) consulte sur les decisions individuelles (mutations avancement sanctions)", "C) Un syndicat de fonctionnaires", "D) Une instance de controle budg?taire"],
    "answer": "B",
    "explanation": "La CAP est consultee sur les decisions individuelles concernant la carriere des fonctionnaires.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le droit disciplinaire dans la fonction publique ?",
    "options": ["A) Le droit du fonctionnaire de refuser des sanctions", "B) L ensemble des regles relatives aux sanctions pouvant etre infligees a un fonctionnaire qui a manque a ses obligations professionnelles", "C) Le droit de retraite des fonctionnaires", "D) Le droit de greve des fonctionnaires"],
    "answer": "B",
    "explanation": "Le droit disciplinaire fixe les fautes professionnelles et les sanctions applicables (avertissement bleme suspension revocation).",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : un fonctionnaire condamne penalement peut-il etre aussi sanctionne disciplinairement pour les memes faits ?",
    "options": ["A) Non le principe non bis in idem l interdit", "B) Oui les deux procedures sont independantes", "C) Non il faut choisir l une ou l autre", "D) Oui mais uniquement si la peine est superieure a 6 mois"],
    "answer": "B",
    "explanation": "Les procedures penale et disciplinaire sont independantes. Un meme fait peut donner lieu a une sanction penale et a une sanction disciplinaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que l avancement a l anciennete dans la fonction publique ivoirienne ?",
    "options": ["A) La promotion automatique basee uniquement sur la duree de service", "B) L avancement qui tient compte du temps de service et parfois des notes mais sans selection rigoureuse", "C) La promotion uniquement au merite", "D) L avancement accorde par le Parlement"],
    "answer": "B",
    "explanation": "L avancement a l anciennete (increments) est automatique ou semi-automatique en fonction du temps de service.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que l avancement au choix (ou au merite) dans la fonction publique ivoirienne ?",
    "options": ["A) L avancement automatique annuel", "B) L avancement decide par l administration apres evaluation des performances et choix parmi les agents eligibles", "C) L avancement par concours interne", "D) L avancement accorde au plus anciens"],
    "answer": "B",
    "explanation": "L avancement au choix est decide par l administration parmi les agents eligibles en tenant compte de leurs merites et de leurs notes.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la mise en non-activite d un fonctionnaire ivoirien ?",
    "options": ["A) Le conge annuel", "B) La position administrative ou le fonctionnaire est suspendu temporairement de ses fonctions en attendant une decision (ex enquete disciplinaire)", "C) La retraite", "D) Le detachement"],
    "answer": "B",
    "explanation": "La mise en non-activite est une suspension temporaire des fonctions dans l attente d une decision disciplinaire ou judiciaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : un fonctionnaire suspendu pendant une enquete disciplinaire a-t-il droit a son salaire ?",
    "options": ["A) Non il perd tout droit a remuneration", "B) Oui il conserve sa remuneration pendant la periode de suspension dans l attente de la decision", "C) Il recoit 50% de son salaire", "D) Cela depend de la gravite des faits"],
    "answer": "B",
    "explanation": "Pendant la suspension provisoire en attente de decision disciplinaire le fonctionnaire conserve generalement sa remuneration.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe d impartialite de l administration ?",
    "options": ["A) L administration n a aucune opinion", "B) L administration traite toutes les situations similaires de la meme maniere sans favoritisme ni discrimination", "C) L administration ne peut pas donner d avis", "D) L administration doit toujours donner raison au citoyen"],
    "answer": "B",
    "explanation": "L impartialite garantit l absence de favoritisme : les agents de l administration ne peuvent pas avantager ou penaliser arbitrairement les administres.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la notion de service public en reseau ?",
    "options": ["A) Un service gere via internet", "B) Un service public organise en infrastructure nationale (eau electricite transport rail) qui necessite des investissements lourds et un acces universel", "C) Un service public gerant les reseaux sociaux", "D) Un service prive de telecommunications"],
    "answer": "B",
    "explanation": "Les services en reseau (eau electricite routes ferrees) sont des services publics a acces universel necessitant des infrastructures nationales.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le pouvoir de police administrative ?",
    "options": ["A) Le pouvoir de la police judiciaire de poursuivre les criminels", "B) Le pouvoir des autorites administratives de restreindre les libert?s individuelles pour maintenir l ordre public", "C) Le pouvoir du Parlement de voter des lois securitaires", "D) Le pouvoir des communes de creer des services de securite"],
    "answer": "B",
    "explanation": "La police administrative permet a l administration de prevenir les troubles a l ordre public en imposant des restrictions aux libert?s.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quels sont les trois elements de l ordre public en police administrative ?",
    "options": ["A) Surete tranquillite salubrité", "B) Surete securite efficacite", "C) Egalite liberte fraternite", "D) Ordre paix justice"],
    "answer": "A",
    "explanation": "L ordre public en police administrative comprend la surete (securite des personnes et biens) la tranquillite (absence de troubles) et la salubrite (hygiene publique).",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : la police administrative peut-elle etre exercee par une personne privee ?",
    "options": ["A) Non, c'est une prerogative de puissance publique", "B) Oui dans le cadre de la delegation de service public", "C) Oui toujours", "D) Non meme en cas de delegation"],
    "answer": "A",
    "explanation": "La police administrative est une prerogative de puissance publique et ne se delegate pas a une personne privee.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le domaine public en droit administratif ivoirien ?",
    "options": ["A) L ensemble des biens prives de l'?tat", "B) L ensemble des biens affectes a l usage direct du public ou a un service public et soumis a un r?gime de protection special", "C) Les terres agricoles de l'?tat", "D) Les immeubles des minist?res uniquement"],
    "answer": "B",
    "explanation": "Le domaine public est insaisissable inalienable et imprescriptible. Il comprend les routes les ponts les cours d eau navigables etc.",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : l'?tat peut-il vendre un bien du domaine public ivoirien ?",
    "options": ["A) Oui librement", "B) Non le domaine public est inalienable ; il faut d abord le desaffecter du domaine public pour le vendre", "C) Oui avec l accord du Parlement", "D) Oui mais uniquement a une personne publique"],
    "answer": "B",
    "explanation": "L inalienabilite du domaine public interdit sa vente directe. La desaffectation prealable est obligatoire avant toute cession.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le droit de preemption de l'?tat en CI ?",
    "options": ["A) Le droit de l'?tat d acheter en priorite certains biens mis en vente", "B) Le droit de l'?tat de prendre les biens sans indemnisation", "C) Le droit de l'?tat de louer des proprietes privees", "D) Le droit de l'?tat de reclamer des impots en priorite"],
    "answer": "A",
    "explanation": "Le droit de preemption permet a l'?tat d acquerir en priorite certains biens mis en vente notamment dans le cadre de l amenagement du territoire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que l expropriation pour cause d utilite publique ?",
    "options": ["A) La confiscation des biens des criminels", "B) La procedure permettant a l'?tat de prendre propriete d un bien prive contre une indemnisation juste et prealable pour un projet d interet general", "C) La saisie des biens en cas de dettes fiscales", "D) La nationalisation d une entreprise"],
    "answer": "B",
    "explanation": "L expropriation est encadree : elle necessite une utilite publique reconnue une procedure legale et une indemnisation juste et prealable.",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : l expropriation sans indemnisation est-elle possible en CI ?",
    "options": ["A) Oui en cas d urgence nationale", "B) Non elle est inconstitutionnelle : l indemnisation juste et prealable est une garantie constitutionnelle", "C) Oui avec l accord du Conseil constitutionnel", "D) Oui uniquement pour les ?trangers"],
    "answer": "B",
    "explanation": "La Constitution garantit le droit de propriete. L expropriation n est possible qu avec une juste et prealable indemnisation.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de continuite de l activite administrative ?",
    "options": ["A) L administration ne ferme jamais", "B) Les services administratifs essentiels doivent fonctionner de maniere continue sans interruption injustifiee", "C) Les fonctionnaires travaillent 24h/24", "D) Les lois ne peuvent pas suspendre les services"],
    "answer": "B",
    "explanation": "La continuite administrative garantit que les services publics essentiels (sante securite eau) ne s interrompent pas meme lors de greves.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le recours de plein contentieux (ou recours de pleine juridiction) ?",
    "options": ["A) Un recours qui ne peut annuler un acte", "B) Un recours ou le juge peut annuler reformer ou condamner l administration a payer des dommages et interets", "C) Un recours reserve aux ?trangers", "D) Un recours devant le Conseil constitutionnel"],
    "answer": "B",
    "explanation": "Le recours de plein contentieux va au-dela de la simple annulation : le juge peut reformer l acte et accorder des dommages et interets.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qu un arrete ministeriel ?",
    "options": ["A) Un arrete pris par le Premier ministre", "B) Un acte r?glementaire ou individuel pris par un ministre dans le cadre de ses attributions", "C) Une loi adoptee par le Parlement", "D) Un decret pr?sidentiel"],
    "answer": "B",
    "explanation": "L arrete ministeriel est un acte de l executif pris par un ministre. Il a une portee inferieure aux decrets.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la hi?rarchie des actes administratifs en CI ?",
    "options": ["A) Les decrets > les arretes ministeriels > les arretes prefectoraux > les arretes municipaux", "B) Les arretes municipaux > les arretes prefectoraux", "C) Les arretes ministeriels > les decrets", "D) Tous les actes administratifs ont la meme valeur"],
    "answer": "A",
    "explanation": "La hi?rarchie : decrets presidetiels > decrets en conseil des ministres > arretes ministeriels > arretes prefectoraux > arretes municipaux.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la competence liee de l administration ?",
    "options": ["A) L administration a une totale liberte de choix", "B) L administration n a pas de liberte de choix : la loi definit precisement ce qu elle doit faire et comment", "C) La competence exclusive d un minist?re", "D) La competence partagee entre deux autorites"],
    "answer": "B",
    "explanation": "La competence liee s oppose au pouvoir discrecionnaire : l administration doit agir d une certaine maniere sans avoir le choix.",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : l administration peut-elle abroger un r?glement en vigueur a tout moment ?",
    "options": ["A) Non elle doit maintenir les r?glements en vigueur indefiniment", "B) Oui l administration peut abroger ses propres r?glements a tout moment sauf si l abrogation porte atteinte aux droits acquis", "C) Oui mais uniquement avec l accord du Parlement", "D) Non seul le juge peut abroger un r?glement"],
    "answer": "B",
    "explanation": "L administration a le droit et parfois l obligation d abroger ses r?glements illegaux. Cependant l abrogation ne peut pas porter atteinte a des droits acquis legitimes.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de la hi?rarchie administrative ?",
    "options": ["A) Les fonctionnaires sont ordonnes par salaire", "B) Le superieur hierarchique peut donner des instructions a ses subordonnes et exercer sur eux un pouvoir de controle et de sanction", "C) Tous les agents ont la meme autorite", "D) Le plus ancien commande toujours"],
    "answer": "B",
    "explanation": "La hi?rarchie administrative implique que le superieur peut donner des instructions des ordres et exercer un pouvoir disciplinaire sur ses subordonnes.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qu une autorite administrative independante (AAI) ?",
    "options": ["A) Un tribunal administratif", "B) Une structure administrative dotee d une independance vis-a-vis du gouvernement creee pour reguler des secteurs sensibles", "C) Un minist?re autonome", "D) Une collectivit? territoriale"],
    "answer": "B",
    "explanation": "Les AAI (ex ARTCI HACA CMI) sont des structures administratives independantes du gouvernement chargees de reguler des secteurs qui necessitent une neutralite politique.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la HACA en CI ?",
    "options": ["A) Haute Autorite des Collectivites Administratives", "B) Haute Autorite de la Communication Audiovisuelle : autorite qui regule les medias audiovisuels en CI", "C) Haute Assemblee des Citoyens Africains", "D) Haute Administration des Charges et Achats"],
    "answer": "B",
    "explanation": "La HACA est l autorite administrative independante chargee de reguler la communication audiovisuelle (television radio) en C?te d'Ivoire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : les AAI (autorites administratives independantes) font-elles partie de l'?tat ?",
    "options": ["A) Non elles sont totalement independantes", "B) Oui elles font partie de l'?tat mais disposent d une independance organique et fonctionnelle vis-a-vis du gouvernement", "C) Non elles sont des organismes prives", "D) Oui elles sont sous l autorite directe du Pr?sident"],
    "answer": "B",
    "explanation": "Les AAI font partie de l'?tat mais avec une independance institutionnelle garantissant leur neutralite par rapport au gouvernement du jour.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le contentieux de la responsabilite administrative ?",
    "options": ["A) La responsabilite penale des fonctionnaires", "B) Le litige devant le juge administratif tendant a obtenir la reparation d un dommage cause par une personne publique", "C) Le contentieux fiscal entre l'?tat et les entreprises", "D) Les litiges entre fonctionnaires"],
    "answer": "B",
    "explanation": "Le contentieux de la responsabilite administrative permet aux victimes d actes ou de comportements fautifs de l administration d obtenir une indemnisation.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la rupture d egalite devant les charges publiques ?",
    "options": ["A) Une inegalite de traitement entre fonctionnaires", "B) Le fait qu une decision ou une action de l administration fait supporter a un particulier un prejudice anormal et special que les autres citoyens ne supportent pas", "C) Une inegalite fiscale", "D) Une discrimination a l embauche dans la fonction publique"],
    "answer": "B",
    "explanation": "La rupture d egalite fonde la responsabilite sans faute : si l action de l'?tat cree un prejudice anormal et special l'?tat doit indemniser meme sans avoir commis de faute.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le recours indemnitaire en droit administratif ?",
    "options": ["A) Un recours pour annuler un acte", "B) Un recours tendant a obtenir une compensation financiere pour un prejudice subi du fait de l administration", "C) Un recours pour obtenir un logement social", "D) Un recours contre les impots"],
    "answer": "B",
    "explanation": "Le recours indemnitaire (ou de plein contentieux) permet d obtenir la condamnation de l administration a payer des dommages et interets.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la mise en demeure de l administration ?",
    "options": ["A) Une sanction administrative", "B) Un acte par lequel l administre ou le juge somme l administration d executer ses obligations dans un delai determine", "C) Une convocation disciplinaire", "D) Un ordre de paiement"],
    "answer": "B",
    "explanation": "La mise en demeure invite l administration a remplir ses obligations. Si elle ne s execute pas le juge peut prononcer des astreintes.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que l astreinte en droit administratif ?",
    "options": ["A) Une peine privative de liberte pour un fonctionnaire", "B) Une sanction financiere prononcee par le juge pour contraindre l administration a executer une decision de justice", "C) Une amende fiscale", "D) Une retenue sur salaire"],
    "answer": "B",
    "explanation": "L astreinte est une condamnation financiere par jour de retard : elle vise a contraindre l administration a executer les decisions de justice.",
    "theme": "Droit administratif"
  },
  {
    "question": "Pi?ge : le juge administratif peut-il adresser des injonctions a l administration en CI ?",
    "options": ["A) Non le juge ne peut qu annuler les actes", "B) Oui depuis les reformes recentes le juge administratif peut adresser des injonctions et prononcer des astreintes pour assurer l execution de ses decisions", "C) Non le juge administratif n a aucun pouvoir d execution", "D) Oui mais uniquement en matiere financiere"],
    "answer": "B",
    "explanation": "Les reformes du droit administratif modeme reconnaissent au juge le pouvoir d injonction et d astreinte pour faire executer ses decisions.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de publicite des actes administratifs ?",
    "options": ["A) Tous les actes doivent passer a la television", "B) Pour etre opposables les actes administratifs doivent etre portes a la connaissance de leurs destinataires par publication ou notification", "C) Les actes administratifs sont confidentiels", "D) Seuls les decrets pr?sidentiels doivent etre publies"],
    "answer": "B",
    "explanation": "La publicite des actes administratifs est une condition de leur opposabilite : les r?glements doivent etre publies les actes individuels notifies.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe du service minimum en cas de greve dans les services publics essentiels ?",
    "options": ["A) Les greves sont interdites dans les services publics", "B) En cas de greve dans les services essentiels (hopitaux transports) un service minimum doit etre maintenu pour proteger la continuite", "C) Les fonctionnaires greves doivent assurer 100% du service", "D) Le service minimum n existe pas en CI"],
    "answer": "B",
    "explanation": "Le service minimum concilie le droit de greve et la continuite des services essentiels. Des agents doivent maintenir un service de base.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de l autorite de la chose jugee en droit administratif ?",
    "options": ["A) Un acte administratif ne peut jamais etre modifie", "B) Une decision de justice devient definitive et lie les parties une fois les voies de recours epuisees", "C) L administration doit obeir aux jugements uniquement si elle le souhaite", "D) Seul le Conseil constitutionnel peut rendre des decisions definitives"],
    "answer": "B",
    "explanation": "L autorite de la chose jugee signifie qu une decision definitive s impose a tous y compris a l administration.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le pouvoir réglementaire autonome en CI ?",
    "options": ["A) Le pouvoir du Parlement de prendre des règlements", "B) Le pouvoir du Président et du gouvernement de prendre des règlements dans des matières non réservées à la loi", "C) Le pouvoir des communes de voter leurs propres lois", "D) Le pouvoir du Conseil constitutionnel de réguler les lois"],
    "answer": "B",
    "explanation": "Le pouvoir réglementaire autonome permet à l'exécutif de régler les matières qui ne sont pas du domaine de la loi défini par la Constitution.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le droit de retrait d'un acte administratif créateur de droits ?",
    "options": ["A) Il peut être retiré à tout moment", "B) Il ne peut être retiré que dans un délai de 4 mois s'il est illégal, pour ne pas priver injustement un administré de ses droits acquis", "C) Il ne peut jamais être retiré", "D) Seul le juge peut l'annuler"],
    "answer": "B",
    "explanation": "Un acte créateur de droits illégal peut être retiré dans un délai de 4 mois (principe de sécurité juridique vs légalité).",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle est la différence entre un marché public et une concession de service public ?",
    "options": ["A) Aucune différence", "B) Dans un marché public l'administration paye le prestataire ; dans la concession le concessionnaire se rémunère sur les usagers", "C) La concession est réservée aux collectivités locales", "D) Le marché public implique un transfert de risque"],
    "answer": "B",
    "explanation": "Marché public : rémunération par l'administration. Concession : rémunération par les usagers + transfert du risque d'exploitation.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la faute de service en droit administratif ?",
    "options": ["A) Une faute personnelle du fonctionnaire", "B) Une faute commise dans l'exercice de la mission de service public, engageant la responsabilité de l'administration", "C) Un manquement disciplinaire", "D) Une infraction pénale"],
    "answer": "B",
    "explanation": "La faute de service (impersonnelle) engage la responsabilité de l'État ; la faute personnelle engage celle du fonctionnaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de mutabilité du service public ?",
    "options": ["A) Le service public peut être supprimé à tout moment", "B) Le service public doit s'adapter à l'évolution des besoins collectifs", "C) Le service public ne peut jamais être modifié", "D) Le service public est immuable dans ses tarifs"],
    "answer": "B",
    "explanation": "La mutabilité (adaptabilité) oblige le service public à évoluer en fonction des besoins de la société.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qu'un arrêté préfectoral ?",
    "options": ["A) Un acte du Président de la République", "B) Un acte réglementaire ou individuel pris par un préfet dans le cadre de ses attributions territoriales", "C) Une loi locale", "D) Un acte du gouvernement central"],
    "answer": "B",
    "explanation": "L'arrêté préfectoral est un acte administratif unilatéral du préfet, applicable dans son département.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle est la condition de l'urgence dans le recours en référé administratif ?",
    "options": ["A) Il suffit que l'administré le demande", "B) Il faut que le délai ordinaire mette en péril un intérêt légitime de façon grave et immédiate", "C) Il n'y a pas de condition d'urgence", "D) L'urgence doit être déclarée par le gouvernement"],
    "answer": "B",
    "explanation": "Le référé-suspension (art. L.521-1 CJA) exige une urgence et un doute sérieux sur la légalité de l'acte.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la clause exorbitante de droit commun dans les contrats administratifs ?",
    "options": ["A) Une clause habituelle dans tous les contrats", "B) Une clause qui ne pourrait exister dans un contrat de droit privé et qui traduit le caractère inégalitaire du contrat administratif", "C) Une clause pénale", "D) Une clause secrète"],
    "answer": "B",
    "explanation": "Les clauses exorbitantes (ex. : pouvoir de modification unilatérale, résiliation pour motif d'intérêt général) marquent les contrats administratifs.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la prescription quadriennale des créances sur l'État en droit ivoirien ?",
    "options": ["A) L'État peut s'endetter pendant 4 ans sans limite", "B) Les créances non réclamées contre l'État s'éteignent après 4 ans", "C) Les impôts se prescrivent en 4 ans", "D) Les contrats administratifs expirent après 4 ans"],
    "answer": "B",
    "explanation": "La prescription quadriennale (inspirée du droit français) éteint les créances sur l'État non réclamées dans les 4 ans.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle est la différence entre déconcentration et délégation de compétence ?",
    "options": ["A) Ce sont des synonymes", "B) La déconcentration est un déplacement interne de compétences au sein de l'État ; la délégation est un transfert de pouvoirs d'une autorité à une autre", "C) La délégation concerne uniquement les collectivités", "D) La déconcentration supprime les intermédiaires"],
    "answer": "B",
    "explanation": "Déconcentration = mouvement interne de l'État (préfets). Délégation = transfert de compétences d'une autorité à une autre.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que l'acte de gouvernement en droit administratif ?",
    "options": ["A) Tout acte pris par le gouvernement", "B) Un acte relatif aux relations entre les pouvoirs publics ou avec des États étrangers, insusceptible de recours juridictionnel", "C) Un acte législatif", "D) Un acte pris par décret"],
    "answer": "B",
    "explanation": "Les actes de gouvernement (diplomatie, grâce, dissolution) échappent au contrôle du juge administratif.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le pouvoir de suspension d'un acte administratif par le préfet ?",
    "options": ["A) Le préfet peut annuler tout acte local", "B) Le préfet peut demander au tribunal de suspendre un acte local illégal", "C) Le préfet peut abroger un acte local", "D) Le préfet peut modifier les actes locaux"],
    "answer": "B",
    "explanation": "En droit ivoirien, le représentant de l'État peut saisir le juge pour suspendre des actes des collectivités illégaux.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel est le délai de recours pour excès de pouvoir devant le juge administratif en CI ?",
    "options": ["A) 10 jours", "B) 2 mois à compter de la publication ou notification de l'acte", "C) 1 an", "D) 6 mois"],
    "answer": "B",
    "explanation": "Le délai de recours pour excès de pouvoir est généralement de 2 mois en droit administratif ivoirien.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe d'égalité des usagers devant le service public ?",
    "options": ["A) Tous les usagers paient le même prix", "B) Les usagers dans une situation identique doivent recevoir le même traitement", "C) Les étrangers sont exclus du service public", "D) Les fonctionnaires ont accès prioritaire"],
    "answer": "B",
    "explanation": "L'égalité devant le service public interdit les discriminations entre usagers se trouvant dans une situation comparable.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qu'un établissement public industriel et commercial (EPIC) ?",
    "options": ["A) Une entreprise privée", "B) Un établissement public gérant une activité à caractère industriel ou commercial, soumis principalement au droit privé pour ses rapports commerciaux", "C) Une collectivité territoriale", "D) Un service déconcentré"],
    "answer": "B",
    "explanation": "Un EPIC (ex : SODEXAM, CIE en CI) est une personne publique dont les activités relèvent principalement du droit privé.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que l'obligation de motivation des actes administratifs en CI ?",
    "options": ["A) Tout acte doit obligatoirement être motivé", "B) Certains actes défavorables doivent être motivés (rejet de demande, sanction) pour permettre à l'administré de comprendre et contester la décision", "C) La motivation est facultative", "D) Seuls les actes réglementaires sont motivés"],
    "answer": "B",
    "explanation": "L'obligation de motivation s'applique notamment aux actes individuels défavorables, garantissant les droits de la défense.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la personnalité juridique d'une collectivité territoriale ?",
    "options": ["A) Elle n'a pas de personnalité juridique", "B) Elle lui permet d'avoir des droits et des obligations propres, d'agir en justice et de contracter", "C) Elle lui permet de voter des lois", "D) Elle est identique à la personnalité de l'État"],
    "answer": "B",
    "explanation": "La personnalité juridique donne à la collectivité la capacité de contracter, d'ester en justice et d'avoir un budget propre.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de proportionnalité dans les mesures de police administrative ?",
    "options": ["A) La police peut prendre toutes mesures nécessaires", "B) Les restrictions apportées aux libertés doivent être strictement nécessaires et proportionnées à l'objectif d'ordre public poursuivi", "C) La proportionnalité s'applique uniquement en droit pénal", "D) Les mesures de police sont toujours définitives"],
    "answer": "B",
    "explanation": "Toute restriction à la liberté par la police administrative doit être proportionnée au risque : ni trop, ni trop peu.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la compétence liée de l'administration ?",
    "options": ["A) L'administration peut agir librement", "B) La loi détermine exactement comment l'administration doit agir : elle n'a aucune liberté de choix", "C) L'administration est compétente dans tous les domaines", "D) La compétence est déléguée à un tiers"],
    "answer": "B",
    "explanation": "En compétence liée, l'administration est obligée d'agir d'une manière précise définie par la loi, sans pouvoir discrétionnaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la théorie de l'imprévision dans les contrats administratifs ?",
    "options": ["A) Le cocontractant peut refuser d'exécuter le contrat", "B) Lorsqu'un événement imprévisible bouleverse l'économie du contrat, le cocontractant peut obtenir une indemnité partielle tout en continuant à exécuter le contrat", "C) L'administration peut modifier le contrat à tout moment", "D) Le contrat est automatiquement résilié en cas d'imprévision"],
    "answer": "B",
    "explanation": "La théorie de l'imprévision (arrêt Gaz de Bordeaux, 1916) permet d'indemniser partiellement le cocontractant sans résilier le contrat.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le contrôle de légalité interne d'un acte administratif ?",
    "options": ["A) Vérifier la signature de l'acte", "B) Vérifier le fond de l'acte : le but, les motifs de droit, les motifs de fait et le contenu", "C) Vérifier la publication de l'acte", "D) Vérifier la compétence de l'auteur"],
    "answer": "B",
    "explanation": "Le contrôle interne porte sur le fond : le but poursuivi, la base légale, les faits et le contenu de la décision.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la responsabilité de l'État du fait des lois ?",
    "options": ["A) L'État n'est jamais responsable des lois qu'il édicte", "B) L'État peut être tenu responsable si une loi, bien que légale, cause un préjudice anormal et spécial à un administré, rompant l'égalité devant les charges publiques", "C) Seul le Parlement est responsable des lois", "D) La responsabilité législative est couverte par l'immunité parlementaire"],
    "answer": "B",
    "explanation": "Même une loi valide peut engager la responsabilité sans faute de l'État si elle crée un préjudice anormal et spécial.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de légalité criminelle en droit administratif répressif ?",
    "options": ["A) L'administration peut sanctionner librement", "B) Les sanctions administratives doivent être prévues par un texte, proportionnées et respecter les droits de la défense", "C) Seul le juge pénal peut infliger des sanctions", "D) Il n'y a pas de sanctions administratives"],
    "answer": "B",
    "explanation": "Le principe de légalité s'applique aussi aux sanctions administratives : texte préalable, proportionnalité, droits de la défense.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le juge des référés administratifs ?",
    "options": ["A) Un juge pénal d'urgence", "B) Un juge administratif qui peut prononcer des mesures provisoires urgentes sans attendre un jugement au fond", "C) Un arbitre entre l'État et les entreprises", "D) Un juge spécialisé dans les collectivités locales"],
    "answer": "B",
    "explanation": "Le juge des référés administratifs peut suspendre un acte, ordonner des mesures conservatoires ou de sauvegarde en urgence.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le droit à un recours effectif en droit administratif ivoirien ?",
    "options": ["A) Tout citoyen peut saisir n'importe quelle juridiction", "B) Toute personne lésée par un acte administratif a le droit de soumettre sa contestation à un juge et d'obtenir une décision", "C) Seuls les nationaux ivoiriens ont ce droit", "D) Ce droit n'existe pas en droit ivoirien"],
    "answer": "B",
    "explanation": "Le droit à un recours effectif est garanti par la Constitution et les traités internationaux ratifiés par la CI.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la notion d'ordre public en police administrative ?",
    "options": ["A) L'ordre militaire", "B) L'ensemble des impératifs de sécurité, de tranquillité et de salubrité publiques que l'autorité administrative est chargée de maintenir", "C) L'ordre économique", "D) L'ordre parlementaire"],
    "answer": "B",
    "explanation": "L'ordre public comprend la sécurité des personnes et des biens, la tranquillité publique et la salubrité.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que l'interprétation administrative (circulaire interprétative) en CI ?",
    "options": ["A) Une loi issue de l'administration", "B) Un document interne qui guide les agents dans l'application d'un texte, sans créer de droits pour les administrés", "C) Un décret d'application", "D) Un arrêté ministériel"],
    "answer": "B",
    "explanation": "Les circulaires interprétatives orientent l'action des agents mais ne lient pas les administrés ni les juges.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le droit au logement opposable (DALO) dans sa conception théorique ?",
    "options": ["A) Le droit pour tout citoyen d'occuper n'importe quel logement vide", "B) Le droit pour certaines personnes défavorisées d'obtenir un logement décent et indépendant grâce à l'obligation faite à l'État", "C) Un droit sans mécanisme d'application", "D) Un droit réservé aux fonctionnaires"],
    "answer": "B",
    "explanation": "Le DALO rend opposable le droit au logement : les personnes sans abri peuvent saisir une commission pour être relogées.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la décision d'espèce (acte individuel non décisoire) ?",
    "options": ["A) Une décision applicable à tout le monde", "B) Une mesure qui ne crée pas de droits nouveaux et ne modifie pas l'ordonnancement juridique (ex. : avis, vœu, recommandation)", "C) Un acte de gouvernement", "D) Un acte réglementaire"],
    "answer": "B",
    "explanation": "Les mesures d'ordre intérieur et les actes préparatoires ne sont pas des décisions administratives attaquables.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le recours en cassation devant la Cour Suprême en CI ?",
    "options": ["A) Un nouveau jugement sur les faits", "B) Un contrôle de la régularité juridique d'une décision sans réexamen des faits", "C) Un appel de la décision de première instance", "D) Un recours réservé à l'État"],
    "answer": "B",
    "explanation": "La cassation vérifie que la loi a été correctement appliquée. Elle ne juge pas les faits à nouveau.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que l'exécution forcée en droit administratif ivoirien ?",
    "options": ["A) L'administration peut toujours exécuter ses décisions par la force", "B) L'administration peut recourir à la contrainte physique uniquement en cas d'urgence ou de texte l'autorisant expressément", "C) L'exécution forcée est interdite en droit ivoirien", "D) Seul le juge peut ordonner l'exécution forcée"],
    "answer": "B",
    "explanation": "Le recours à la force physique par l'administration (voie de fait) est exceptionnel et encadré en droit administratif.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la notion d'administration active en droit administratif ?",
    "options": ["A) L'administration qui contrôle les autres administrations", "B) L'administration qui agit, prend des décisions et exécute les politiques publiques (gouvernement, préfets, maires)", "C) L'administration consultative", "D) L'administration juridictionnelle"],
    "answer": "B",
    "explanation": "L'administration active est l'ensemble des organes qui prennent des décisions exécutoires : gouvernement, préfets, maires, etc.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel est le principe d'interdiction de la voie de fait en droit administratif ?",
    "options": ["A) L'administration peut toujours agir par la force", "B) L'administration ne peut pas porter atteinte à la liberté individuelle ou à la propriété privée de manière manifestement illégale sans texte l'y autorisant", "C) La voie de fait est autorisée en cas d'urgence", "D) Ce principe n'existe pas en CI"],
    "answer": "B",
    "explanation": "La voie de fait est une atteinte grave et illégale aux libertés fondamentales par l'administration, qui échappe au juge administratif et relève du juge judiciaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la notion de bloc de compétence en droit administratif ?",
    "options": ["A) Toutes les affaires vont au même juge", "B) Certains litiges sont attribués globalement à un ordre de juridiction (administratif ou judiciaire) pour éviter les conflits de compétence", "C) Les compétences sont réparties aléatoirement", "D) Le bloc de compétence concerne uniquement le droit pénal"],
    "answer": "B",
    "explanation": "Le bloc de compétence concentre les litiges d'un même domaine devant un seul juge pour des raisons de cohérence et d'efficacité.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le recours pour excès de pouvoir (REP) en droit administratif ivoirien ?",
    "options": ["A) Un recours pour obtenir des dommages et intérêts", "B) Un recours tendant à l'annulation d'un acte administratif illégal, ouvert à tout intéressé", "C) Un recours réservé aux fonctionnaires", "D) Un recours devant la Cour constitutionnelle"],
    "answer": "B",
    "explanation": "Le REP est le recours contentieux administratif le plus important : il vise à l'annulation des actes illégaux de l'administration.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle est la différence entre une autorité administrative indépendante (AAI) et un établissement public (EP) ?",
    "options": ["A) Aucune différence", "B) Une AAI bénéficie d'une indépendance vis-à-vis du gouvernement pour ses missions de régulation ; un EP est soumis à la tutelle de l'État", "C) Un EP est indépendant, une AAI dépend du gouvernement", "D) Les AAI ont plus de personnel"],
    "answer": "B",
    "explanation": "L'indépendance organisationnelle de l'AAI vis-à-vis du pouvoir exécutif est ce qui la distingue d'un établissement public classique.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de précaution en droit administratif français (applicable en CI) ?",
    "options": ["A) Agir seulement en cas de certitude scientifique", "B) En cas de risque grave et irréversible pour l'environnement ou la santé, prendre des mesures préventives sans attendre la certitude scientifique", "C) Interdire toute innovation", "D) Attendre l'autorisation parlementaire avant d'agir"],
    "answer": "B",
    "explanation": "Le principe de précaution (Charte de l'environnement 2004 en France) autorise l'action préventive en situation d'incertitude scientifique.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le principe de subsidiarité en droit administratif ?",
    "options": ["A) L'État décide de tout", "B) Les décisions doivent être prises au niveau le plus proche des citoyens, le niveau supérieur n'intervenant que si le niveau inférieur est insuffisant", "C) Les collectivités locales n'ont aucune compétence", "D) Le gouvernement peut toujours se substituer aux collectivités"],
    "answer": "B",
    "explanation": "Le principe de subsidiarité organise la répartition des compétences : le pouvoir local d'abord, le supérieur en dernier recours.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la notion de domaine privé de l'État en droit administratif ivoirien ?",
    "options": ["A) Les biens de l'État sont tous imprescriptibles et inaliénables", "B) Le domaine privé regroupe les biens de l'État non affectés à l'usage public ; il peut être géré, loué ou vendu comme des biens privés", "C) Le domaine privé appartient aux fonctionnaires", "D) Le domaine privé comprend les routes et les bâtiments publics"],
    "answer": "B",
    "explanation": "Le domaine privé de l'État (forêts, terres agricoles, actifs financiers) est géré selon des règles proches du droit privé, contrairement au domaine public.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que l'obligation de publication des actes administratifs réglementaires ?",
    "options": ["A) Les règlements sont secrets", "B) Les actes réglementaires doivent être publiés (Journal Officiel) pour être opposables aux administrés", "C) La publication est facultative", "D) Seuls les décrets présidentiels sont publiés"],
    "answer": "B",
    "explanation": "La publication (JO, recueil des actes) conditionne l'entrée en vigueur et l'opposabilité des actes réglementaires.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la responsabilité de l'État du fait des travaux publics ?",
    "options": ["A) L'État n'est pas responsable des travaux publics", "B) L'État peut être tenu responsable des dommages causés à des tiers ou à des usagers par des travaux publics, même sans faute", "C) Seul le maître d'ouvrage privé est responsable", "D) La responsabilité est limitée aux accidents mortels"],
    "answer": "B",
    "explanation": "La responsabilité du fait des travaux publics peut être engagée sans faute (pour les tiers) ou pour faute (pour les usagers).",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la notion de service public constitutionnel en CI ?",
    "options": ["A) Un service géré par le Conseil constitutionnel", "B) Un service public dont la création est imposée par la Constitution (enseignement, défense, justice)", "C) Un service public payant", "D) Un service public réservé aux élus"],
    "answer": "B",
    "explanation": "Certains services publics sont directement fondés et imposés par la Constitution (justice, défense, éducation).",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le droit de préemption de l'État en matière foncière en CI ?",
    "options": ["A) L'État peut prendre des terres sans compensation", "B) L'État peut acquérir en priorité certains biens mis en vente pour des raisons d'intérêt public", "C) Les particuliers ne peuvent pas vendre leurs terres", "D) L'État peut louer des terres privées de force"],
    "answer": "B",
    "explanation": "Le droit de préemption permet à l'État d'acheter prioritairement certains biens mis en vente, notamment pour l'aménagement du territoire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que l'acte administratif unilatéral à portée générale et impersonnelle ?",
    "options": ["A) Un acte visant une seule personne", "B) Un acte qui s'applique à une catégorie de personnes indéfiniment déterminées par des critères généraux (comme une loi)", "C) Un acte secret", "D) Un acte pris sans base légale"],
    "answer": "B",
    "explanation": "L'acte réglementaire est unilatéral, général et impersonnel : il s'applique à toute personne entrant dans la catégorie qu'il définit.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que le recours de pleine juridiction (plein contentieux) en droit administratif ivoirien ?",
    "options": ["A) Un recours qui ne peut annuler l'acte", "B) Un recours où le juge a tous les pouvoirs : annuler, réformer, condamner l'administration à payer des dommages et intérêts", "C) Un recours réservé aux étrangers", "D) Un recours uniquement devant la Cour Suprême"],
    "answer": "B",
    "explanation": "Le plein contentieux permet au juge d'aller au-delà de la simple annulation : il peut réformer et allouer une indemnité.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce que la notion de délégation interservices en administration ivoirienne ?",
    "options": ["A) Un agent qui signe pour un autre sans autorisation", "B) La coordination administrative entre différents services d'un ministère ou entre ministères pour gérer des projets transversaux", "C) La suppression d'un service", "D) Le transfert d'un service à une collectivité"],
    "answer": "B",
    "explanation": "La délégation interservices permet une coordination efficace entre directions et ministères sur des projets communs.",
    "theme": "Droit administratif"
  },
  {
    "question": "En Côte d'Ivoire, quel organe constitue la plus haute juridiction de l'ordre administratif ?",
    "options": ["A) La Cour Suprême", "B) Le Conseil d'État", "C) La Cour de Cassation", "D) La Cour des Comptes"],
    "answer": "B",
    "explanation": "Depuis la Constitution de 2016, le Conseil d'État est la plus haute juridiction de l'ordre administratif, succédant à la Chambre Administrative de la Cour Suprême.",
    "theme": "Droit administratif"
  },
  {
    "question": "Lequel de ces actes est insusceptible de recours pour excès de pouvoir en droit administratif ivoirien ?",
    "options": ["A) Un arrêté municipal", "B) Un décret de nomination", "C) Un acte de gouvernement", "D) Une circulaire réglementaire"],
    "answer": "C",
    "explanation": "Les actes de gouvernement (touchant aux rapports avec les pouvoirs publics ou les relations internationales) bénéficient d'une immunité juridictionnelle.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel principe régit la responsabilité de la puissance publique en cas de dommages causés par les travaux publics ?",
    "options": ["A) La responsabilité pour faute prouvée", "B) La responsabilité sans faute", "C) L'irresponsabilité totale", "D) La responsabilité contractuelle"],
    "answer": "B",
    "explanation": "Pour les dommages de travaux publics subis par un tiers, la responsabilité de l'administration est sans faute.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le Préfet de département en Côte d'Ivoire est-il une autorité déconcentrée ou décentralisée ?",
    "options": ["A) Décentralisée", "B) Déconcentrée", "C) À la fois déconcentrée et décentralisée", "D) Aucune des deux"],
    "answer": "B",
    "explanation": "Le préfet est le représentant de l'État dans le département, c'est une autorité déconcentrée.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle est la durée du mandat d'un maire en Côte d'Ivoire ?",
    "options": ["A) 4 ans", "B) 5 ans", "C) 6 ans", "D) 7 ans"],
    "answer": "B",
    "explanation": "Les conseillers municipaux et le maire sont élus pour un mandat de 5 ans.",
    "theme": "Droit administratif"
  },
  {
    "question": "Acte de Gouvernement :",
    "options": ["A) Nomination ministre", "B) Expropriation", "C) Mutation", "D) Marché public"],
    "answer": "A",
    "explanation": "Insusceptible de REP, motivé politiquement.",
    "theme": "Droit administratif"
  },
  {
    "question": "Sujétions imprévues donne droit à :",
    "options": ["A) Résiliation", "B) Indemnisation totale", "C) Pénalité", "D) Réduction"],
    "answer": "B",
    "explanation": "Compensation intégrale du surcoût matériel.",
    "theme": "Droit administratif"
  },
  {
    "question": "Délai REP en CI ?",
    "options": ["A) 1 mois", "B) 2 mois", "C) 3 mois", "D) 6 mois"],
    "answer": "B",
    "explanation": "2 mois après publication/notification.",
    "theme": "Droit administratif"
  },
  {
    "question": "Domaine public (propriété) :",
    "options": ["A) Inaliénable", "B) Imprescriptible", "C) Insaisissable", "D) Les trois"],
    "answer": "D",
    "explanation": "Les 3 grands principes de protection.",
    "theme": "Droit administratif"
  },
  {
    "question": "Recours circulaire interprétative ?",
    "options": ["A) Toujours", "B) Jamais", "C) Si ajoute à la loi", "D) Accord min"],
    "answer": "C",
    "explanation": "Circulaire réglementaire faisant grief (Duvignères).",
    "theme": "Droit administratif"
  },
  {
    "question": "Rémunération concessionnaire ?",
    "options": ["A) Par l'Etat", "B) Usagers", "C) Sans risque", "D) Salaire"],
    "answer": "B",
    "explanation": "Rémunération substantielle liée à l'exploitation (usagers).",
    "theme": "Droit administratif"
  },
  {
    "question": "Faute personnelle de l'agent :",
    "options": ["A) Gravité", "B) Détachable service", "C) Lieu", "D) Grade"],
    "answer": "B",
    "explanation": "Faute détachable de l'exercice normal des fonctions.",
    "theme": "Droit administratif"
  },
  {
    "question": "Fait du prince (contrat) :",
    "options": ["A) Nature", "B) Admin cocontractante modifie", "C) Résiliation", "D) Tiers"],
    "answer": "B",
    "explanation": "L'administration modifie les conditions, ouvrant indemnisation.",
    "theme": "Droit administratif"
  },
  {
    "question": "Juge suprême REP contre décrets ?",
    "options": ["A) TPI", "B) Conseil Etat", "C) Appel", "D) Cons Constit"],
    "answer": "B",
    "explanation": "Le Conseil d'Etat (compétence 1er/dernier ressort).",
    "theme": "Droit administratif"
  },
  {
    "question": "Délégation de signature :",
    "options": ["A) Dessaisit", "B) Ne dessaisit pas", "C) Juge", "D) Transmet auto"],
    "answer": "B",
    "explanation": "Le délégant conserve sa compétence.",
    "theme": "Droit administratif"
  },
  {
    "question": "Expropriation exige :",
    "options": ["A) Accord", "B) Juste/préalable indemnité", "C) Décret PM", "D) Loi"],
    "answer": "B",
    "explanation": "Protection constitutionnelle de la propriété.",
    "theme": "Droit administratif"
  },
  {
    "question": "Contrôle pouvoir discrétionnaire :",
    "options": ["A) Aucun", "B) Erreur manifeste", "C) Illégal", "D) Réservé PR"],
    "answer": "B",
    "explanation": "Le juge vérifie l'absence d'EMA (Erreur Manifeste d'Appréciation).",
    "theme": "Droit administratif"
  },
  {
    "question": "Principe Service Public :",
    "options": ["A) Rentabilité", "B) Mutabilité", "C) Concurrence", "D) Rigidité"],
    "answer": "B",
    "explanation": "Loi de Rolland : Adaptation/Mutabilité.",
    "theme": "Droit administratif"
  },
  {
    "question": "But police administrative :",
    "options": ["A) Répression", "B) Prévention troubles", "C) Enquête", "D) Arrestation"],
    "answer": "B",
    "explanation": "Prévention de l'ordre public.",
    "theme": "Droit administratif"
  },
  {
    "question": "Arrêt Blanco :",
    "options": ["A) Irresponsabilité", "B) Compétence JA/Autonomie", "C) Imprévision", "D) REP"],
    "answer": "B",
    "explanation": "Fonde l'autonomie du droit administratif (1873).",
    "theme": "Droit administratif"
  },
  {
    "question": "Silence 4 mois admin CI :",
    "options": ["A) Rejet", "B) Accept", "C) Sursis", "D) Juge"],
    "answer": "A",
    "explanation": "Silence vaut décision implicite de rejet (général).",
    "theme": "Droit administratif"
  },
  {
    "question": "Détournement pouvoir :",
    "options": ["A) Incompétence", "B) Forme", "C) Loi", "D) But autre"],
    "answer": "D",
    "explanation": "Utiliser son pouvoir pour un but illégitime.",
    "theme": "Droit administratif"
  },
  {
    "question": "Refus ordre manifestement illégal :",
    "options": ["A) Obéissance aveugle", "B) Baïonnette intelligente", "C) Insubordination", "D) Exception"],
    "answer": "B",
    "explanation": "Devoir de désobéissance si illégal et dangereux.",
    "theme": "Droit administratif"
  },
  {
    "question": "Exception illégalité :",
    "options": ["A) Annule après délai", "B) Écarte règlement illégal", "C) Punit min", "D) Modifie constit"],
    "answer": "B",
    "explanation": "Moyen de défense perpétuel contre un acte réglementaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Régularisation contrat (Tarn/Garonne) :",
    "options": ["A) Toujours annulé", "B) Sauvetage si possible", "C) Inattaquable", "D) Modifié usager"],
    "answer": "B",
    "explanation": "Privilégie la survie du contrat (loyauté contractuelle).",
    "theme": "Droit administratif"
  },
  {
    "question": "Imprévision (Gaz Bordeaux) :",
    "options": ["A) Prévisible", "B) Imprévisible/bouleversant", "C) Définitif", "D) Faute admin"],
    "answer": "B",
    "explanation": "Évènement exceptionnel déséquilibrant temporairement le contrat.",
    "theme": "Droit administratif"
  },
  {
    "question": "Préfet est autorité :",
    "options": ["A) Décentralisée", "B) Déconcentrée", "C) Fédérale", "D) Judiciaire"],
    "answer": "B",
    "explanation": "Représentant local du pouvoir central de l'Etat.",
    "theme": "Droit administratif"
  },
  {
    "question": "Maire agent de l'Etat (cas) :",
    "options": ["A) Marchés", "B) Personnel", "C) État civil", "D) Voies"],
    "answer": "C",
    "explanation": "Officier d'état civil agissant au nom de l'Etat.",
    "theme": "Droit administratif"
  },
  {
    "question": "Acte inexistant :",
    "options": ["A) 2 mois", "B) Aucun recours", "C) Nul, contestable tjrs", "D) Implicite"],
    "answer": "C",
    "explanation": "Vice si grave qu'il n'existe juridiquement pas (pas de délai).",
    "theme": "Droit administratif"
  },
  {
    "question": "Tutelle administrative s'exerce sur :",
    "options": ["A) Préfet", "B) Collectivités locales", "C) Ministres", "D) Sociétés"],
    "answer": "B",
    "explanation": "Contrôle de l'Etat sur les entités décentralisées.",
    "theme": "Droit administratif"
  },
  {
    "question": "Accident véhicule admin jugé par :",
    "options": ["A) TA", "B) Juge Judiciaire", "C) CE", "D) TM"],
    "answer": "B",
    "explanation": "Loi 1957 confie ces litiges au juge judiciaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Lien usager-SPIC :",
    "options": ["A) Administratif", "B) Privé (contractuel)", "C) Mixte", "D) Pénal"],
    "answer": "B",
    "explanation": "Contrat de droit privé.",
    "theme": "Droit administratif"
  },
  {
    "question": "Recours gracieux adressé à :",
    "options": ["A) Supérieur", "B) Auteur de l'acte", "C) Juge", "D) Médiateur"],
    "answer": "B",
    "explanation": "À l'autorité qui a pris la décision.",
    "theme": "Droit administratif"
  },
  {
    "question": "Fin phase admin expropriation :",
    "options": ["A) Arrêté cessibilité", "B) Jugement", "C) Ordonnance", "D) DUP"],
    "answer": "A",
    "explanation": "L'arrêté de cessibilité (qui transfère au juge civil la suite).",
    "theme": "Droit administratif"
  },
  {
    "question": "EPA soumis au principe de :",
    "options": ["A) Spécialité", "B) Concurrence", "C) Universalité", "D) Rentabilité"],
    "answer": "A",
    "explanation": "Principe de spécialité de l'établissement public.",
    "theme": "Droit administratif"
  },
  {
    "question": "Marché TP vs Fournitures :",
    "options": ["A) Montant", "B) Immeuble", "C) Passation", "D) Cocontractant"],
    "answer": "B",
    "explanation": "Le TP implique un travail sur un bien immobilier public.",
    "theme": "Droit administratif"
  },
  {
    "question": "Conseil Etat CI comme juge appel :",
    "options": ["A) Tous litiges", "B) Décisions TPI admin", "C) Impôts", "D) Jamais"],
    "answer": "B",
    "explanation": "Statuant sur les appels des juridictions du 1er degré admin.",
    "theme": "Droit administratif"
  },
  {
    "question": "Non-privilège admin :",
    "options": ["A) Décision exécutoire", "B) Exécution forcée", "C) Égalité stricte", "D) Expropriation"],
    "answer": "C",
    "explanation": "L'administration n'est pas l'égale du particulier (pouvoir exhorbitant).",
    "theme": "Droit administratif"
  },
  {
    "question": "Faute lourde exigée (tradition) :",
    "options": ["A) Police matérielle", "B) Hôpital simple", "C) Police terrain/fisc/justice", "D) TP"],
    "answer": "C",
    "explanation": "Activités régaliennes particulièrement difficiles.",
    "theme": "Droit administratif"
  },
  {
    "question": "Tiers victime TP :",
    "options": ["A) Faute simple", "B) Faute lourde", "C) Sans faute", "D) Contrat"],
    "answer": "C",
    "explanation": "Responsabilité sans faute (risque) pour le tiers.",
    "theme": "Droit administratif"
  },
  {
    "question": "Moyen d'ordre public :",
    "options": ["A) Non soulevable", "B) Juge soulève d'office", "C) Procureur", "D) Prescrit"],
    "answer": "B",
    "explanation": "Le juge a l'obligation de le soulever (ex: incompétence).",
    "theme": "Droit administratif"
  },
  {
    "question": "Responsabilité ministre (pénale/historique) :",
    "options": ["A) Cassation", "B) Haute Cour", "C) Cour Comptes", "D) CE"],
    "answer": "B",
    "explanation": "La Haute Cour de Justice (historiquement) juge les ministres pour crimes/délits.",
    "theme": "Droit administratif"
  },
  {
    "question": "Voie de fait :",
    "options": ["A) Route", "B) Atteinte grave hors droit", "C) Agression", "D) Annulation"],
    "answer": "B",
    "explanation": "Atteinte manifeste liberté/propriété non rattachable à un pouvoir.",
    "theme": "Droit administratif"
  },
  {
    "question": "Révocation étudiant :",
    "options": ["A) Appel civil", "B) REP", "C) Pénal", "D) Aucun"],
    "answer": "B",
    "explanation": "C'est une sanction administrative d'EPA, attaquable par REP.",
    "theme": "Droit administratif"
  },
  {
    "question": "Référé-liberté :",
    "options": ["A) Libérer", "B) Sauver liberté en urgence", "C) Impôt", "D) Indemnité"],
    "answer": "B",
    "explanation": "Procédure d'urgence pour cessation d'atteinte grave à liberté.",
    "theme": "Droit administratif"
  },
  {
    "question": "AAI (Autorité Admin Indép) :",
    "options": ["A) PM", "B) Pas de tutelle", "C) Privée", "D) Lois"],
    "answer": "B",
    "explanation": "Absence de pouvoir hiérarchique du gouvernement.",
    "theme": "Droit administratif"
  },
  {
    "question": "Contrat privé devient admin si :",
    "options": ["A) >10M", "B) Mandat pour Etat", "C) Notaire", "D) >5 ans"],
    "answer": "B",
    "explanation": "Théorie du mandat (Peyrot).",
    "theme": "Droit administratif"
  },
  {
    "question": "Contentieux fiscal CI :",
    "options": ["A) RAP (Réclamation pralable)", "B) Direct juge", "C) Incompétence JA", "D) Gratuit"],
    "answer": "A",
    "explanation": "Le RAP (recours administratif préalable) est obligatoire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Imprescriptibilité domaine pub :",
    "options": ["A) Vente", "B) Usucapion impossible", "C) Utilisation", "D) Déclassement"],
    "answer": "B",
    "explanation": "L'occupation prolongée ne donne pas la propriété.",
    "theme": "Droit administratif"
  },
  {
    "question": "Passage domaine public à privé :",
    "options": ["A) Mutation", "B) Déclassement", "C) Permis", "D) Bail"],
    "answer": "B",
    "explanation": "L'acte de déclassement fait sortir le bien du domaine public.",
    "theme": "Droit administratif"
  },
  {
    "question": "Exequatur sentence arbitrale marché public :",
    "options": ["A) Paix", "B) Juge compétent (Admin/Exécution)", "C) CC", "D) Cassation"],
    "answer": "B",
    "explanation": "Le juge compétent pour l'exécution du contrat le valide.",
    "theme": "Droit administratif"
  },
  {
    "question": "Cassation au CE :",
    "options": ["A) Uniquement droit", "B) Droit + faits", "C) Opportunité", "D) Constit"],
    "answer": "A",
    "explanation": "Contrôle uniquement l'application du droit par les juges du fond.",
    "theme": "Droit administratif"
  },
  {
    "question": "Révocation maire (CI) :",
    "options": ["A) Politique", "B) Acte tutelle attaquable", "C) Impossible", "D) Législatif"],
    "answer": "B",
    "explanation": "Acte administratif soumis au REP.",
    "theme": "Droit administratif"
  },
  {
    "question": "Directive UEMOA :",
    "options": ["A) Direct", "B) Fixe résultat/Laisse moyens", "C) Recommandation", "D) Jugement"],
    "answer": "B",
    "explanation": "Nécessite transposition en droit interne.",
    "theme": "Droit administratif"
  },
  {
    "question": "Pouvoir substitution Préfet :",
    "options": ["A) Agit si carence Maire", "B) Annule acte", "C) Dissout", "D) Remplace juge"],
    "answer": "A",
    "explanation": "Agit à la place du maire défaillant (sécurité/ordre) après mise en demeure.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le principe de la légalité administrative implique que l’administration doit respecter les textes qui émanent d’elle-même.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "L'administration doit respecter ses propres textes selon le principe de la légalité.",
    "theme": "Droit administratif"
  },
  {
    "question": "Selon l’arrêt Doublet, l’administration a l’obligation de faire respecter la loi.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "L'arrêt Doublet consacre l'obligation pour l'administration de faire respecter la loi.",
    "theme": "Droit administratif"
  },
  {
    "question": "Selon l’Arrêt Compagnie France Amérique, l’administration n’est tenue de respecter la loi.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "L'administration est tenue de respecter la loi.",
    "theme": "Droit administratif"
  },
  {
    "question": "Selon l’Arrêt Société pour l’Estéhétique de France, l’administration a la faculté de faire cesser les situations inégales.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Elle a l'obligation (et non la simple faculté) de faire cesser les situations inégales.",
    "theme": "Droit administratif"
  },
  {
    "question": "Selon l’Arrêt Couitéas, l’administration ne peut jamais refuser d’apporter son concours à l’exécution des décisions de justice.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Elle peut refuser exceptionnellement pour des motifs d'ordre public.",
    "theme": "Droit administratif"
  },
  {
    "question": "L’administration a le pouvoir d’apprécier les faits et les modalités d’exécution d’une obligation qui lui est faite.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "Cela découle de son pouvoir d'appréciation et du pouvoir discrétionnaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "L’administration n’est pas soumise au respect du préambule de la constitution.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Le préambule a valeur constitutionnelle et s'impose à l'administration (Arrêt Société EKY).",
    "theme": "Droit administratif"
  },
  {
    "question": "L’acte inexistant est un acte qui est rentre dans l’ordonnancement juridique avant d’en sortir.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "L'acte inexistant est censé n'avoir jamais existé.",
    "theme": "Droit administratif"
  },
  {
    "question": "Tout pouvoir discrétionnaire comporte une dose de compétence liée.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "Il y a toujours un contrôle minimum de légalité (compétence, forme).",
    "theme": "Droit administratif"
  },
  {
    "question": "Aucun recours n’est possible contre tous les actes de gouvernement.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Exceptionnellement, un recours en indemnité est possible pour rupture d'égalité devant les charges publiques (traités).",
    "theme": "Droit administratif"
  },
  {
    "question": "C’est l’arrêt Héyriès qui pose les conditions d’application de la théorie des circonstances exceptionnelles.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "L'arrêt Heyriès consacre les atteintes aux règles de forme et de procédure en période exceptionnelle.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le préfet d’Abidjan décide de l’interdiction de manifester sur toute l’étendue du territoire d’Abidjan jusqu’à nouvel ordre. Cette mesure sera confirmée par le juge au regard de la jurisprudence administrative.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Une interdiction générale et absolue est illégale.",
    "theme": "Droit administratif"
  },
  {
    "question": "Les mesures de police prises dans un but de brimade sont légales.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Elles constituent un détournement de pouvoir.",
    "theme": "Droit administratif"
  },
  {
    "question": "Les autorités parlementaires ne prennent jamais des actes administratifs.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Elles en prennent dans le cadre de la gestion de leurs fonctionnaires (CSCA, Anzian Niamiké).",
    "theme": "Droit administratif"
  },
  {
    "question": "Les autorités administratives peuvent prendre des actes privés.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "Oui, dans le cadre de la gestion de leur domaine privé.",
    "theme": "Droit administratif"
  },
  {
    "question": "Les circulaires ne sont jamais des actes administratifs décisoire.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Les circulaires réglementaires peuvent avoir un caractère décisoire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Les décisions du conseil municipal sont des délibérations.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "Le conseil municipal prend ses décisions sous forme de délibérations.",
    "theme": "Droit administratif"
  },
  {
    "question": "En CI, le premier ministre peut prendre des ordonnances.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "C'est le Président de la République qui prend des ordonnances.",
    "theme": "Droit administratif"
  },
  {
    "question": "La décision par laquelle l’inspecteur du travail refuse d’autoriser le licenciement d’un délégué du personnel est un acte administratif.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "C'est un acte administratif susceptible de REP.",
    "theme": "Droit administratif"
  },
  {
    "question": "Un particulier personne physique peut prendre des actes administratifs.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "Oui, s'il gère un service public et est doté de prérogatives de puissance publique (CE, Monpeurt, Magnier).",
    "theme": "Droit administratif"
  },
  {
    "question": "La notation des fonctionnaires sont des actes administratifs.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "La notation d'un fonctionnaire est un acte administratif (CSCA, Douka Yao Anderson).",
    "theme": "Droit administratif"
  },
  {
    "question": "L’appel d’offres a pour dessein d’attribuer le contrat au soumissionnaire le moins-disant.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "L'appel d'offres vise généralement l'offre économiquement la plus avantageuse, souvent la moins-disante.",
    "theme": "Droit administratif"
  },
  {
    "question": "La modification unilatérale du prix du contrat est admise par la jurisprudence administrative.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "L'administration ne peut modifier unilatéralement les clauses financières du contrat.",
    "theme": "Droit administratif"
  },
  {
    "question": "La mise en régie d’office est une matérialisation du pouvoir de sanction de l’autorité contractante.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "C'est une sanction coercitive en cas de défaillance du cocontractant.",
    "theme": "Droit administratif"
  },
  {
    "question": "La force majeure administrative résulte de plusieurs tentatives infructueuses de viabilisation du contrat par l’autorité administrative.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "La force majeure doit être extérieure, imprévisible et irrésistible.",
    "theme": "Droit administratif"
  },
  {
    "question": "Dans la théorie du fait du principe, l’indemnisation du cocontractant est partielle.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Le fait du prince donne droit à une indemnisation intégrale.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le contentieux des contrats administratifs est exclusivement un contentieux de pleine juridiction.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Le REP est possible contre les actes détachables.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'inaliénabilité du domaine public signifie que les biens affectés à l'utilité publique ne peuvent être vendus ou échangés tant qu'ils sont affectés à un service public.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "C'est la définition du principe d'inaliénabilité du domaine public.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qui distingue le domaine public naturel du domaine public artificiel ?",
    "options": ["A) a. L'intervention humaine", "B) b. Le type de propriété", "C) c. La taille des biens"],
    "answer": "A",
    "explanation": "Le domaine public artificiel résulte d'un aménagement humain.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le domaine privé est accessible à tous sans restriction.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Le domaine privé est géré comme la propriété d'un particulier et n'est pas librement accessible à tous.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel document est nécessaire pour déclencher la procédure d'expropriation ?",
    "options": ["A) a. Un contrat de vente", "B) b. Une déclaration d'utilité publique", "C) c. Un accord de voisinage"],
    "answer": "B",
    "explanation": "La DUP est l'acte préalable indispensable.",
    "theme": "Droit administratif"
  },
  {
    "question": "L’expropriation pour cause d’utilité publique est chevauchée par une phase administrative et une phase judiciaire.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "L'expropriation comporte une phase administrative (DUP, arrêté de cessibilité) et une phase judiciaire (transfert de propriété, indemnisation).",
    "theme": "Droit administratif"
  },
  {
    "question": "Dans la permission de voirie, les droits du permissionnaire sont précaires.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "L'autorisation d'occupation du domaine public est par nature précaire et révocable.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel type de fonctionnaires n'est pas concerné par le statut général des fonctionnaires parmi les propositions suivantes ?",
    "options": ["A) a - Les agents de la santé", "B) b - Les magistrats de l'ordre judiciaire", "C) c - Les enseignants", "D) d - Les policiers"],
    "answer": "B",
    "explanation": "Les magistrats ont un statut autonome particulier.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel grade est associé aux fonctions de conception et de direction selon la loi portant SGFP ?",
    "options": ["A) a - Catégorie C", "B) b - Catégorie A", "C) c - Catégorie D", "D) d - Catégorie B"],
    "answer": "B",
    "explanation": "La catégorie A correspond aux fonctions de conception et de direction.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle est la différence entre licenciement et révocation parmi les propositions suivantes ?",
    "options": ["A) a - Le licenciement peut être pour insuffisance professionnelle, la révocation est une sanction disciplinaire.", "B) b - Les deux sont des sanctions disciplinaires identiques.", "C) c - Le licenciement est toujours temporaire, la révocation est définitive.", "D) d - Le licenciement nécessite un vote, la révocation non"],
    "answer": "A",
    "explanation": "La révocation est disciplinaire, le licenciement non disciplinaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Les sanctions de premier degré sont réservées au ministre technique de l’agent.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "Le pouvoir disciplinaire pour le 1er degré appartient au Ministre technique, Préfet ou Directeur d'EP.",
    "theme": "Droit administratif"
  },
  {
    "question": "La responsabilité de l’administration est engagée sur la base d’une faute lourde pour les dommages causés à la personne visée au cours d’une opération de police matérielle par l’utilisation d’armes dangereuses est consacrée par l’arrêt AUBERGER ET DUMONT.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "C'est une faute simple si la victime est visée, et sans faute si c'est un tiers.",
    "theme": "Droit administratif"
  },
  {
    "question": "L’arrêt SOCIÉTÉ DES TRANSPORTS DU SUD consacre l’exonération totale de la responsabilité de l’administration en cas de faute de la victime.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "La faute de la victime peut être une cause d'exonération partielle ou totale selon les cas.",
    "theme": "Droit administratif"
  },
  {
    "question": "L’administration dispose d’une action récursoire contre l’agent fautif, mais l’agent n’en dispose pas contre l’administration lorsqu’il a réparé intégralement les dommages causés à la victime en cas de cumul de responsabilité.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "L'agent dispose également d'une action récursoire (Arrêt Delville).",
    "theme": "Droit administratif"
  },
  {
    "question": "La responsabilité de l’administration est acquise en cas de cumul de fautes.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "La victime peut poursuivre l'administration ou l'agent en cas de cumul de fautes.",
    "theme": "Droit administratif"
  },
  {
    "question": "L’intérêt du principe de cumul de responsabilité est d’octroyer un droit d’option à l’administration.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Le droit d'option est octroyé à la victime, pas à l'administration.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le fait du tiers est une cause d’exonération de la responsabilité de l’administration lorsqu’elle est la cause unique.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "Le fait du tiers exonère l'administration dans la responsabilité pour faute s'il est la cause exclusive.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel type d'intérêt doit être lésé pour qu'il y ait intérêt à agir ?",
    "options": ["A) a. Un intérêt personnel", "B) b. Un intérêt légitime", "C) c. Un intérêt collectif", "D) d. Un intérêt anonyme"],
    "answer": "A",
    "explanation": "L'intérêt à agir doit être personnel, direct et certain.",
    "theme": "Droit administratif"
  },
  {
    "question": "En matière de REP, le moyen d'annulation est synonyme de cas d'ouverture.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "Les cas d'ouverture (incompétence, vice de forme, violation de la loi, détournement de pouvoir) sont les moyens d'annulation.",
    "theme": "Droit administratif"
  },
  {
    "question": "Sont des conditions de recevabilité du REP, Le détournement de procédure et l’incompétence.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Ce sont des cas d'ouverture au fond, pas des conditions de recevabilité.",
    "theme": "Droit administratif"
  },
  {
    "question": "En matière d’acte inexistant, les délais sont identiques que les actes susceptibles d’être frappés d’une simple nullité.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "Le recours contre un acte inexistant peut être exercé à tout moment, sans condition de délai.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le titre foncier n’est pas susceptible de recours pour excès de pouvoir.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "A",
    "explanation": "Le titre foncier est définitif et inattaquable, sauf cas spécifiques de fraude devant le juge judiciaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "La déchéance du titre de propriété en terre urbaine n'est pas admise en droit ivoirien.",
    "options": ["A) Vrai", "B) Faux"],
    "answer": "B",
    "explanation": "La loi prévoit des hypothèses de déchéance en cas d'insuffisance de mise en valeur.",
    "theme": "Droit administratif"
  },
  {
    "question": "Sont considérés comme insuffisamment mis en valeur :",
    "options": ["A) a. Des chantiers de bâtiments inachevés, et laissés à l'abandon", "B) b. Des terrains faisant uniquement l'objet de clôtures", "C) c. Des terrains abritant des constructions en matériaux précaires"],
    "answer": "B",
    "explanation": "Une simple clôture ne constitue pas une mise en valeur suffisante.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Dame veuve Trompier-Gravier consacre quel principe général du droit ?",
    "options": ["A) La non-rétroactivité des actes", "B) Le droit de la défense", "C) L'égalité devant le service public", "D) Le recours pour excès de pouvoir"],
    "answer": "B",
    "explanation": "L'arrêt Dame veuve Trompier-Gravier est l'arrêt fondateur du principe général du droit de la défense, obligeant l'administration à entendre toute personne avant de prendre une décision défavorable.",
    "theme": "Droit administratif"
  },
  {
    "question": "Selon l'arrêt Société du journal l'Aurore, quel principe général du droit est dégagé ?",
    "options": ["A) Le droit de la défense", "B) L'égalité de traitement dans le SP", "C) La non-rétroactivité des actes administratifs", "D) L'accès au service public"],
    "answer": "C",
    "explanation": "L'arrêt Société du journal l'Aurore consacre le principe de non-rétroactivité des actes administratifs : un acte administratif ne peut en principe produire d'effets avant sa signature.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Dame Lamotte consacre quel principe ?",
    "options": ["A) L'obligation de motiver les actes", "B) L'existence d'un droit au recours pour excès de pouvoir", "C) Le droit de la défense", "D) La responsabilité sans faute de l'État"],
    "answer": "B",
    "explanation": "L'arrêt Dame Lamotte consacre comme principe général du droit le recours pour excès de pouvoir, qui est ouvert même sans texte contre tout acte administratif.",
    "theme": "Droit administratif"
  },
  {
    "question": "Selon l'arrêt Barel, quel principe général du droit est consacré ?",
    "options": ["A) L'égalité de traitement dans le service public", "B) L'égalité d'accès à la fonction publique", "C) Le droit de la défense", "D) La liberté du commerce et de l'industrie"],
    "answer": "B",
    "explanation": "L'arrêt Barel consacre le principe général d'égalité d'accès à la fonction publique, interdisant toute discrimination dans le recrutement des fonctionnaires.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Rubin de Servens concerne quel domaine ?",
    "options": ["A) La responsabilité sans faute de l'État", "B) Les actes de gouvernement échappant au REP", "C) La délégation de compétence", "D) Les circonstances exceptionnelles"],
    "answer": "B",
    "explanation": "L'arrêt Rubin de Servens traite des actes de gouvernement, qui sont des actes politiques par nature échappant au contrôle du juge administratif, notamment les actes pris dans les relations entre les pouvoirs constitutionnels.",
    "theme": "Droit administratif"
  },
  {
    "question": "Dans le cadre du principe de légalité, l'arrêt Société EKY établit que :",
    "options": ["A) Les traités internationaux priment sur la Constitution", "B) Le préambule de la Constitution est source de légalité", "C) Les actes de gouvernement sont inconstitutionnels", "D) Les PGD priment sur les lois"],
    "answer": "B",
    "explanation": "L'arrêt Société EKY affirme que le préambule de la Constitution constitue une source de légalité administrative, lui donnant ainsi une valeur juridique contraignante.",
    "theme": "Droit administratif"
  },
  {
    "question": "Lequel de ces arrêts concerne la théorie des circonstances exceptionnelles ?",
    "options": ["A) Arrêt Barel", "B) Arrêt Heyriès", "C) Arrêt Pariset", "D) Arrêt Pelletier"],
    "answer": "B",
    "explanation": "L'arrêt Heyriès (1918) est l'un des arrêts fondateurs de la théorie des circonstances exceptionnelles, permettant à l'administration de s'affranchir temporairement de certaines règles en période de crise.",
    "theme": "Droit administratif"
  },
  {
    "question": "Selon la théorie des circonstances exceptionnelles, laquelle de ces conditions N'EST PAS requise ?",
    "options": ["A) La situation doit être d'une gravité exceptionnelle", "B) La mesure doit être proportionnée et limitée dans le temps", "C) L'autorité compétente doit obtenir l'accord du Parlement", "D) Les moyens normaux doivent être insuffisants"],
    "answer": "C",
    "explanation": "La théorie des circonstances exceptionnelles ne requiert pas l'accord du Parlement. Elle permet à l'administration d'agir au-delà de ses compétences habituelles face à une situation de crise grave, sans texte d'habilitation préalable.",
    "theme": "Droit administratif"
  },
  {
    "question": "Lequel des arrêts suivants n'illustre PAS la théorie des circonstances exceptionnelles ?",
    "options": ["A) Arrêt Laugier", "B) Arrêt Dame de la murette", "C) Arrêt Adriamisera", "D) Arrêt Casanova"],
    "answer": "D",
    "explanation": "L'arrêt Casanova concerne les conditions de recevabilité du REP (l'intérêt pour agir), et non la théorie des circonstances exceptionnelles. Les arrêts Laugier, Dame de la murette et Adriamisera sont tous des arrêts relatifs aux circonstances exceptionnelles.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel est le délai de recours contentieux contre un acte administratif nul (nullité relative) ?",
    "options": ["A) 1 mois", "B) 2 mois", "C) 6 mois", "D) Aucun délai"],
    "answer": "B",
    "explanation": "Selon la jurisprudence (notamment l'arrêt Dame Cachet), le délai de recours en annulation d'un acte administratif irrégulier est de 2 mois à compter de sa publication ou notification.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'acte inexistant se distingue de l'acte nul notamment parce que :",
    "options": ["A) L'acte inexistant peut faire l'objet d'un retrait dans les 2 mois", "B) L'acte inexistant n'est soumis à aucun délai de recours", "C) L'acte inexistant produit des effets de droit jusqu'à son annulation", "D) L'acte inexistant ne peut être contesté que par les parties"],
    "answer": "B",
    "explanation": "L'acte inexistant est tellement entaché d'illégalité (ex: une usurpation de fonctions) qu'il est réputé n'avoir jamais existé. Il peut donc être contesté à tout moment, sans délai de recours.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Rosan Girard illustre quel concept de droit administratif ?",
    "options": ["A) La faute personnelle", "B) L'acte inexistant", "C) La théorie du fonctionnaire de fait", "D) L'imprévision"],
    "answer": "B",
    "explanation": "L'arrêt Rosan Girard, comme les arrêts Laffite et Megevand, illustre la notion d'acte inexistant : un acte si gravement irrégulier qu'il est dépourvu de toute existence juridique.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le critère organique de l'acte administratif unilatéral implique que :",
    "options": ["A) Seules les autorités administratives peuvent émettre des AAU", "B) Toute autorité administrative émet des actes présumés administratifs, avec exceptions", "C) Les actes des personnes privées ne peuvent jamais être administratifs", "D) Seuls les actes du Président de la République sont des AAU"],
    "answer": "B",
    "explanation": "Le critère organique établit une présomption d'administrativité pour les actes des autorités administratives. Mais il existe des exceptions : certains actes d'autorités administratives ne sont pas administratifs (ex: actes de gestion privée), et inversement, certains actes de personnes privées gérant un SP peuvent être administratifs.",
    "theme": "Droit administratif"
  },
  {
    "question": "Selon l'arrêt CE Monpeurt, une personne privée peut émettre des actes administratifs si elle :",
    "options": ["A) Est mandatée par une autorité publique", "B) Gère un service public industriel et commercial (SPIC)", "C) Gère un service public administratif (SPA)", "D) A reçu une délégation de signature"],
    "answer": "C",
    "explanation": "L'arrêt CE Monpeurt établit que les personnes privées gérant un service public administratif (SPA) peuvent être habilitées à prendre des actes administratifs unilatéraux.",
    "theme": "Droit administratif"
  },
  {
    "question": "Parmi les actes suivants, lequel est considéré comme un acte NON-décisoire (non-AAU) ?",
    "options": ["A) Un arrêté de nomination", "B) Une circulaire interprétative", "C) Un décret d'application d'une loi", "D) Une mise en demeure"],
    "answer": "B",
    "explanation": "Selon l'arrêt CE, Institution Notre-Dame du Kreisker, les circulaires purement interprétatives ne créent pas de droits et n'ont pas de caractère décisoire : elles ne font pas grief et sont donc insusceptibles de REP.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt CSCA, Nado Koutouan illustre le cas des :",
    "options": ["A) Mesures d'ordre intérieur", "B) Actes confirmatifs", "C) Actes préparatoires", "D) Circulaires réglementaires"],
    "answer": "C",
    "explanation": "L'arrêt CSCA Nado Koutouan illustre les actes préparatoires, qui sont des étapes procédurales préalables à un acte définitif. Ils ne font pas grief en eux-mêmes et ne sont donc pas susceptibles de REP.",
    "theme": "Droit administratif"
  },
  {
    "question": "La théorie du fonctionnaire de fait, illustrée par les arrêts Ducastel et Marrion, permet de :",
    "options": ["A) Poursuivre un agent pour faute personnelle", "B) Valider les actes pris par un agent dont le titre est irrégulier", "C) Déléguer une signature à un subordonné", "D) Permettre à l'administration de se retirer d'un contrat"],
    "answer": "B",
    "explanation": "La théorie du fonctionnaire de fait permet de maintenir la validité des actes pris par un agent dont la désignation ou le titre est entaché d'irrégularité, afin de protéger la continuité du service public et la sécurité juridique des administrés.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Dame Cachet régit principalement :",
    "options": ["A) Le retrait des actes irréguliers créateurs de droits (délai 2 mois)", "B) L'abrogation des règlements illégaux", "C) La responsabilité sans faute de l'État", "D) Les conditions de recevabilité du REP"],
    "answer": "A",
    "explanation": "L'arrêt Dame Cachet pose la règle du parallélisme des délais pour le retrait des actes irréguliers créateurs de droits : l'administration ne peut les retirer que dans le délai du recours contentieux (2 mois).",
    "theme": "Droit administratif"
  },
  {
    "question": "En droit des contrats administratifs, le critère matériel alternatif est :",
    "options": ["A) La présence d'au moins deux personnes publiques au contrat", "B) La clause exorbitante du droit commun OU la participation à l'exécution d'un SP", "C) L'objet financier du contrat supérieur à un seuil fixé par décret", "D) L'approbation préalable du contrôleur financier"],
    "answer": "B",
    "explanation": "Pour qu'un contrat soit qualifié d'administratif par le juge, il faut un critère organique (au moins une personne publique) ET un critère matériel alternatif : soit une clause exorbitante du droit commun, soit que le contrat porte sur l'exécution même d'un service public.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le 'fait du prince' en droit des contrats administratifs désigne :",
    "options": ["A) La décision du chef de l'État de mettre fin à un contrat", "B) Une mesure de l'autorité contractante qui modifie les conditions du contrat hors du champ contractuel", "C) La force majeure imputable à une décision d'État étranger", "D) L'exercice par l'administration de son pouvoir de modification unilatérale"],
    "answer": "B",
    "explanation": "Le fait du prince désigne une mesure prise par l'autorité publique contractante (mais en dehors de sa qualité de cocontractant) qui aggrave les charges du cocontractant. Il donne droit à une indemnisation intégrale.",
    "theme": "Droit administratif"
  },
  {
    "question": "La théorie de l'imprévision en droit administratif se distingue de la force majeure car :",
    "options": ["A) L'imprévision libère le cocontractant de ses obligations", "B) L'imprévision est un bouleversement temporaire, extérieur et imprévisible qui n'exonère pas mais donne droit à une indemnisation partielle", "C) L'imprévision ne donne droit à aucune indemnisation", "D) L'imprévision résulte nécessairement d'une décision de l'administration"],
    "answer": "B",
    "explanation": "À la différence de la force majeure qui libère les parties, la théorie de l'imprévision en droit administratif permet de poursuivre le contrat en accordant une indemnité partielle (non intégrale) au cocontractant confronté à un aléa économique extérieur, imprévisible et temporaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt TC Pelletier est le fondement de :",
    "options": ["A) La responsabilité sans faute pour risque", "B) La distinction entre faute personnelle et faute de service", "C) La théorie de l'imprévision", "D) Le principe d'égalité devant les charges publiques"],
    "answer": "B",
    "explanation": "L'arrêt TC Pelletier (1873) est l'arrêt fondateur de la distinction entre faute personnelle (engageant la responsabilité personnelle de l'agent) et faute de service (engageant la responsabilité de l'administration).",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt CE Anguet consacre :",
    "options": ["A) L'exonération de l'État en cas de faute de la victime", "B) Le cumul de fautes (personnelle et de service) engageant la double responsabilité", "C) La responsabilité exclusive de l'agent fautif", "D) Le principe de la faute lourde en matière de police judiciaire"],
    "answer": "B",
    "explanation": "L'arrêt CE Anguet consacre le cumul des fautes : lorsqu'un même dommage résulte à la fois d'une faute de service et d'une faute personnelle de l'agent, la victime peut choisir de mettre en jeu la responsabilité de l'administration ou celle de l'agent.",
    "theme": "Droit administratif"
  },
  {
    "question": "En matière de responsabilité sans faute pour risque, l'arrêt CE Regnault-Desroziers concerne :",
    "options": ["A) Les dommages causés lors d'activités sportives", "B) Les dommages résultant de l'utilisation d'armes et engins dangereux", "C) Les dommages causés par des détenus en liberté conditionnelle", "D) Les dommages résultant de travaux publics"],
    "answer": "B",
    "explanation": "L'arrêt CE Regnault-Desroziers fonde la responsabilité sans faute de l'État pour les dommages causés par des choses dangereuses (ici, des grenades et obus), établissant ainsi le régime de responsabilité pour risque dû aux armes et engins dangereux.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt CE La Fleurette consacre la responsabilité de l'État du fait :",
    "options": ["A) Des traités internationaux", "B) Des lois (rupture d'égalité devant les charges publiques)", "C) Des actes réglementaires", "D) Des décisions de justice"],
    "answer": "B",
    "explanation": "L'arrêt CE La Fleurette (1938) engage la responsabilité sans faute de l'État du fait des lois qui, sans en avoir l'intention, causent un préjudice spécial et anormal à certains administrés, rompant l'égalité devant les charges publiques.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt CE Couitéas engage la responsabilité de l'État sur quel fondement ?",
    "options": ["A) Faute de service grave", "B) Rupture d'égalité devant les charges publiques (refus d'exécuter une décision de justice)", "C) Risque créé par une chose dangereuse", "D) Faute personnelle d'un agent"],
    "answer": "B",
    "explanation": "L'arrêt CE Couitéas engage la responsabilité sans faute de l'État pour refus d'exécuter une décision de justice afin de préserver l'ordre public. Ce refus, justifié, crée néanmoins une rupture d'égalité devant les charges publiques ouvrant droit à indemnisation.",
    "theme": "Droit administratif"
  },
  {
    "question": "En matière de responsabilité administrative, la cause d'exonération de 'faute de la victime' est illustrée par :",
    "options": ["A) Arrêt CE Regnault-Desroziers", "B) Arrêt CE Amoudruz", "C) Arrêt CE Thouzellier", "D) Arrêt CE Perruche"],
    "answer": "B",
    "explanation": "L'arrêt CE Amoudruz traite de la faute de la victime comme cause d'exonération totale ou partielle de la responsabilité de l'administration.",
    "theme": "Droit administratif"
  },
  {
    "question": "Les opérations de police à chaud (interventions immédiates) requièrent, selon la jurisprudence, une faute de quelle nature pour engager la responsabilité de l'État ?",
    "options": ["A) Faute simple", "B) Faute personnelle détachable", "C) Faute lourde", "D) Aucune faute (responsabilité sans faute)"],
    "answer": "C",
    "explanation": "Selon l'arrêt CE Tomaso Grecco et la jurisprudence classique, les opérations de police à chaud (interventions immédiates sur le terrain) engagent la responsabilité de l'État uniquement en cas de faute lourde, compte tenu des difficultés inhérentes à ces interventions.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le recours pour excès de pouvoir (REP) est qualifié de recours :",
    "options": ["A) De plein contentieux, suspensif et réservé aux personnes lésées", "B) D'utilité publique, d'ordre public et non suspensif", "C) Gracieux, obligatoire et préalable à tout recours contentieux", "D) Exceptionnel, suspensif et à caractère personnel"],
    "answer": "B",
    "explanation": "Le REP est un recours d'utilité publique (ouvert à tout intéressé), d'ordre public (le juge peut le soulever d'office) et non suspensif (l'acte continue de produire ses effets pendant le recours).",
    "theme": "Droit administratif"
  },
  {
    "question": "Dans le REP, la condition d'intérêt pour agir a été précisée par l'arrêt CE Casanova qui étend le droit de recours :",
    "options": ["A) Aux seuls contribuables nationaux", "B) Aux contribuables locaux pour contester les actes de leur collectivité", "C) Aux seuls agents de l'administration", "D) Aux associations déclarées seulement"],
    "answer": "B",
    "explanation": "L'arrêt CE Casanova reconnaît la qualité pour agir des contribuables locaux pour contester la légalité d'actes pris par les collectivités territoriales dès lors qu'ils ont un intérêt à le faire.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt CE Pariset illustre quel cas d'ouverture du REP ?",
    "options": ["A) L'incompétence ratione materiae", "B) Le vice de procédure substantielle", "C) Le détournement de pouvoir", "D) L'erreur manifeste d'appréciation"],
    "answer": "C",
    "explanation": "L'arrêt CE Pariset est l'arrêt de référence sur le détournement de pouvoir : l'autorité a agi dans les limites de sa compétence, mais dans un but autre que celui pour lequel le pouvoir lui a été conféré.",
    "theme": "Droit administratif"
  },
  {
    "question": "En matière d'organisation administrative, le contrôle de tutelle se distingue du contrôle hiérarchique car :",
    "options": ["A) La tutelle est plus large que le contrôle hiérarchique", "B) Il ne peut exister de tutelle sans texte, contrairement au contrôle hiérarchique qui est de droit", "C) La tutelle permet de réformer les actes, ce que le contrôle hiérarchique ne permet pas", "D) La tutelle s'exerce sur les agents, et le contrôle hiérarchique sur les actes"],
    "answer": "B",
    "explanation": "Selon l'arrêt Commune de Néris-les-Bains, il ne peut exister de tutelle sans texte : la tutelle est d'attribution. En revanche, le contrôle hiérarchique est de droit ; il naît automatiquement de la relation entre supérieur et subordonné.",
    "theme": "Droit administratif"
  },
  {
    "question": "Lequel de ces arrêts concerne le contrôle hiérarchique sur les actes administratifs ?",
    "options": ["A) Arrêt Queralt", "B) Arrêt Casanova", "C) Arrêt Heyriès", "D) Arrêt Pelletier"],
    "answer": "A",
    "explanation": "L'arrêt Queralt est une référence en matière de contrôle hiérarchique, précisant l'étendue du pouvoir du supérieur hiérarchique sur les actes de ses subordonnés (pouvoir d'instruction, de réformation et d'annulation).",
    "theme": "Droit administratif"
  },
  {
    "question": "La police administrative se distingue de la police judiciaire en ce que :",
    "options": ["A) La police administrative réprime les infractions déjà commises", "B) La police administrative est une activité préventive qui vise à maintenir l'ordre public", "C) La police judiciaire relève de l'administration et la police administrative du ministère de la justice", "D) La police administrative n'est pas soumise au contrôle du juge"],
    "answer": "B",
    "explanation": "Selon l'arrêt CE Consorts Baud, la police administrative est une activité préventive visant à maintenir l'ordre public, tandis que la police judiciaire est répressive et vise à constater les infractions et en poursuivre les auteurs.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le triptyque classique de l'ordre public en police administrative comprend :",
    "options": ["A) Sécurité, moralité et dignité humaine", "B) Sécurité, tranquillité et salubrité publiques", "C) Liberté, égalité et fraternité", "D) Ordre, neutralité et continuité"],
    "answer": "B",
    "explanation": "Le triptyque classique de l'ordre public, objectif de la police administrative, comprend la sécurité, la tranquillité et la salubrité publiques. La jurisprudence a ajouté ultérieurement d'autres composantes comme la moralité, l'esthétique et la dignité humaine.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt CE Commune de Morsang-sur-Orge (1995) a élargi l'ordre public à :",
    "options": ["A) La moralité publique", "B) L'esthétique urbaine", "C) La dignité humaine", "D) La protection de l'environnement"],
    "answer": "C",
    "explanation": "L'arrêt CE Commune de Morsang-sur-Orge, dit 'arrêt du lancer de nain', a consacré la dignité humaine comme composante de l'ordre public, permettant d'interdire des spectacles portant atteinte à la dignité de la personne humaine, même avec le consentement de la victime.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt CE Lutetia (1959) a reconnu la moralité publique comme composante de l'ordre public afin de :",
    "options": ["A) Permettre au maire d'interdire une réunion politique", "B) Permettre au maire d'interdire des films contraires aux bonnes mœurs", "C) Interdire la vente de boissons alcoolisées", "D) Réglementer les horaires des établissements de nuit"],
    "answer": "B",
    "explanation": "L'arrêt CE Lutetia reconnaît la moralité publique comme composante de l'ordre public et valide le pouvoir du maire d'interdire la projection d'un film jugé contraire aux bonnes mœurs dans sa commune, même si ce film a reçu le visa ministériel.",
    "theme": "Droit administratif"
  },
  {
    "question": "Selon l'arrêt CE Benjamin, l'exercice du pouvoir de police administrative doit :",
    "options": ["A) Toujours favoriser l'ordre sur la liberté", "B) Être proportionné au risque de trouble à l'ordre public et respecter les libertés publiques", "C) Être préalablement soumis à l'approbation du préfet", "D) Se fonder exclusivement sur des textes législatifs"],
    "answer": "B",
    "explanation": "L'arrêt CE Benjamin pose le principe de proportionnalité en matière de police administrative : les mesures de police doivent être strictement nécessaires et proportionnées au trouble à l'ordre public. L'autorité de police ne peut pas interdire une réunion si des mesures moins restrictives suffisent à maintenir l'ordre.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qui est l'autorité de police administrative générale au niveau national ayant fondé sa compétence sur l'arrêt CE Labonne ?",
    "options": ["A) Le Premier Ministre", "B) Le Président de la République", "C) Le Ministre de l'Intérieur", "D) Le Préfet"],
    "answer": "B",
    "explanation": "L'arrêt CE Labonne reconnaît au Président de la République un pouvoir de police administrative générale au niveau national, même sans texte d'habilitation expresse, sur la base de ses pouvoirs propres d'organisation des services publics.",
    "theme": "Droit administratif"
  },
  {
    "question": "PIÈGE - L'arrêt CE Société des concerts du conservatoire consacre quel principe ?",
    "options": ["A) L'égalité d'accès à la fonction publique", "B) L'égalité de traitement des usagers au sein du service public", "C) Le droit de la défense dans le service public", "D) La liberté de conscience des agents publics"],
    "answer": "B",
    "explanation": "PIÈGE : L'arrêt Société des concerts du conservatoire (à ne pas confondre avec l'arrêt Barel sur l'égalité d'accès à la FP) consacre l'égalité de traitement entre usagers au sein d'un même service public.",
    "theme": "Droit administratif"
  },
  {
    "question": "PIÈGE - L'abrogation d'un acte administratif réglementaire illégal est :",
    "options": ["A) Facultative pour l'administration", "B) Obligatoire à tout moment sur demande d'un administré", "C) Impossible une fois que l'acte est entré en vigueur", "D) Soumise au délai de 2 mois"],
    "answer": "B",
    "explanation": "Selon l'arrêt CE Syndicat national de Meunerie à Seigle, l'administration a l'obligation d'abroger un règlement illégal dès lors qu'un administré en fait la demande. C'est le corollaire du principe de légalité.",
    "theme": "Droit administratif"
  },
  {
    "question": "PIÈGE - En matière de délégation de compétence, la délégation de signature diffère de la délégation de pouvoir car :",
    "options": ["A) La délégation de signature transfère définitivement la compétence", "B) La délégation de signature n'opère pas de transfert de compétence; le délégant reste responsable", "C) La délégation de pouvoir est toujours révocable", "D) La délégation de signature doit être approuvée par le juge administratif"],
    "answer": "B",
    "explanation": "Dans la délégation de signature, l'autorité délégante reste compétente et responsable ; le délégataire signe en son nom. Dans la délégation de pouvoir (ou de compétence), la compétence est réellement transférée au délégataire qui agit en son propre nom.",
    "theme": "Droit administratif"
  },
  {
    "question": "PIÈGE - Un acte administratif 'confirmatif' est-il susceptible de recours pour excès de pouvoir ?",
    "options": ["A) Oui, car il exprime une nouvelle décision de l'administration", "B) Non, car il ne fait que répéter une décision antérieure sans la modifier, donc sans faire grief", "C) Oui, si la décision initiale était illégale", "D) Non, sauf si le demandeur ignorait la décision initiale"],
    "answer": "B",
    "explanation": "Un acte confirmatif répète une décision antérieure sans y ajouter d'éléments nouveaux. Il ne fait donc pas grief par lui-même et n'est pas susceptible de REP. Pour contester, il faut attaquer la décision initiale (dans les délais).",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt CE Dégni-Segui (CSCA) précise que l'AAU doit avoir un caractère :",
    "options": ["A) Gracieux et motivé", "B) Exécutoire et décisoire", "C) Réglementaire et normatif", "D) Public et opposable"],
    "answer": "B",
    "explanation": "L'arrêt CSCA Dégni-Segui précise que pour qu'un acte soit qualifié d'acte administratif unilatéral, il doit avoir un caractère exécutoire (applicable de droit sans recours au juge) et décisoire (modifier l'ordonnancement juridique).",
    "theme": "Droit administratif"
  },
  {
    "question": "En droit administratif ivoirien, quel organe est compétent en matière de contentieux administratif ?",
    "options": ["A) La Cour d'Appel", "B) La Cour de Cassation", "C) Le Conseil d'État", "D) Le Tribunal de Première Instance"],
    "answer": "C",
    "explanation": "En Côte d'Ivoire, depuis la réforme de 2018, le Conseil d'État est la juridiction administrative suprême compétente pour connaître des contentieux administratifs. L'ordre juridictionnel ivoirien est dualiste (ordre judiciaire et ordre administratif).",
    "theme": "Droit administratif"
  },
  {
    "question": "L'ARCOP en Côte d'Ivoire est l'autorité de régulation compétente pour :",
    "options": ["A) La régulation de la presse et de la communication", "B) La commande publique (marchés publics)", "C) Le contrôle des concessions et délégations de service public", "D) La régulation du secteur bancaire"],
    "answer": "B",
    "explanation": "L'Autorité de Régulation de la Commande Publique (ARCOP) est l'organe ivoirien chargé de réguler et de contrôler la passation des marchés publics et des délégations de service public, garantissant la transparence et l'efficacité de la commande publique.",
    "theme": "Droit administratif"
  },
  {
    "question": "En Côte d'Ivoire, la décentralisation territoriale comprend quelles collectivités territoriales ?",
    "options": ["A) Seulement les communes et les régions", "B) Les communes, les régions et les districts autonomes", "C) Les communes, les départements et les régions", "D) Les villages, les communes et les préfectures"],
    "answer": "B",
    "explanation": "La décentralisation en Côte d'Ivoire reconnaît trois catégories de collectivités territoriales : les communes, les régions et les districts autonomes (notamment le District Autonome d'Abidjan et le District Autonome de Yamoussoukro).",
    "theme": "Droit administratif"
  },
  {
    "question": "PIÈGE - Quelle est la différence entre déconcentration et décentralisation ?",
    "options": ["A) La déconcentration confère la personnalité juridique aux entités locales, la décentralisation non", "B) La décentralisation transfère des compétences à des collectivités ayant la personnalité morale, la déconcentration transfère des pouvoirs à des agents de l'État", "C) La déconcentration s'applique au niveau national et la décentralisation au niveau international", "D) Il n'y a pas de différence fondamentale entre les deux"],
    "answer": "B",
    "explanation": "La déconcentration consiste à transférer des pouvoirs à des agents de l'État (préfets, sous-préfets) qui restent soumis au pouvoir hiérarchique central. La décentralisation transfère des compétences à des collectivités distinctes de l'État, dotées de la personnalité morale et d'une autonomie de gestion.",
    "theme": "Droit administratif"
  },
  {
    "question": "PIÈGE - La compétence ratione loci d'une autorité administrative concerne :",
    "options": ["A) La durée pendant laquelle elle peut exercer ses fonctions", "B) La matière (le domaine) dans laquelle elle peut agir", "C) Le territoire géographique sur lequel elle peut exercer ses attributions", "D) La hiérarchie des normes qu'elle doit respecter"],
    "answer": "C",
    "explanation": "La compétence ratione loci est la compétence territoriale : elle définit le territoire géographique dans les limites duquel une autorité administrative peut exercer légalement ses attributions. La compétence ratione materiae est la compétence par matière et la compétence ratione temporis est la compétence temporelle.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel est le fondement de la compétence du Conseil d'État ivoirien en matière de contrôle des actes des collectivités territoriales ?",
    "options": ["A) La Constitution de 1960", "B) La loi organique sur le Conseil d'État issue des réformes de la IIIe République", "C) Un traité CEDEAO sur la gouvernance locale", "D) Le Code général des collectivités territoriales de 2003"],
    "answer": "B",
    "explanation": "Le Conseil d'État ivoirien, réorganisé dans le cadre des réformes institutionnelles de la IIIe République (Constitution 2016 et textes organiques suivants), exerce le contrôle juridictionnel sur les actes des collectivités territoriales décentralisées.",
    "theme": "Droit administratif"
  },
  {
    "question": "PIÈGE AVANCÉ - Lorsqu'un agent public commet une faute personnelle 'non dépourvue de tout lien avec le service', la victime peut-elle agir contre l'administration ?",
    "options": ["A) Non, seul l'agent est responsable de sa faute personnelle", "B) Oui, grâce à la théorie du cumul de responsabilités (arrêt Epoux Lemonnier)", "C) Oui, mais uniquement si la faute a été commise dans les locaux administratifs", "D) Non, car la responsabilité personnelle exclut totalement la responsabilité du service"],
    "answer": "B",
    "explanation": "L'arrêt CE Epoux Lemonnier admet que lorsqu'une faute personnelle d'un agent n'est pas dépourvue de tout lien avec le service, la victime peut engager la responsabilité de l'administration (cumul de responsabilités), lui offrant ainsi une meilleure garantie d'indemnisation.",
    "theme": "Droit administratif"
  },
  {
    "question": "PIÈGE AVANCÉ - La police administrative spéciale diffère de la police administrative générale en ce que :",
    "options": ["A) La police spéciale a un champ d'application plus large", "B) La police spéciale n'est exercée que par le Préfet", "C) La police spéciale est attribuée par des textes particuliers à des autorités précises pour des domaines déterminés", "D) La police spéciale peut s'exercer sans base légale"],
    "answer": "C",
    "explanation": "La police administrative spéciale est définie et attribuée par des textes particuliers à des autorités précises (ministres, maires, présidents d'université) pour des domaines réglementés spécifiques (cinéma, santé, urbanisme...). Elle coexiste avec la police générale mais ses règles propres priment dans son domaine.",
    "theme": "Droit administratif"
  },
  {
    "question": "PIÈGE AVANCÉ - En cas de conflit entre police générale et police spéciale, quelle est la règle ?",
    "options": ["A) La police générale prime toujours sur la police spéciale", "B) La police spéciale prime sur la police générale dans son domaine, sauf circonstances exceptionnelles autorisant le recours à la police générale", "C) Le préfet décide au cas par cas lequel des deux régimes s'applique", "D) Les deux régimes s'appliquent simultanément et cumulativement"],
    "answer": "B",
    "explanation": "Lorsqu'une police spéciale est instituée dans un domaine, ses règles priment sur celles de la police générale. Cependant, en cas de circonstances exceptionnelles (trouble grave à l'ordre public), l'autorité de police générale peut intervenir en complément, comme l'illustre la jurisprudence sur le cinéma (arrêts Lutétia et Société Les Films Lutetia).",
    "theme": "Droit administratif"
  },
  {
    "question": "PIÈGE AVANCÉ - Une circulaire réglementaire (impérative) diffère d'une circulaire interprétative car :",
    "options": ["A) La circulaire réglementaire ne peut être attaquée par REP", "B) La circulaire réglementaire édicte des normes nouvelles et peut être attaquée par REP, contrairement à la circulaire interprétative", "C) La circulaire interprétative a une valeur supérieure à la circulaire réglementaire", "D) Les deux types de circulaires ont exactement la même valeur juridique"],
    "answer": "B",
    "explanation": "Depuis l'arrêt CE Institution Notre-Dame du Kreisker, la jurisprudence distingue les circulaires interprétatives (qui se bornent à interpréter un texte sans créer de règle nouvelle, non susceptibles de REP) des circulaires réglementaires (qui créent des règles nouvelles, susceptibles de REP).",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel arrêt consacre le principe selon lequel le juge administratif peut annuler un acte administratif pour détournement de pouvoir ?",
    "options": ["A) Arrêt Pariset", "B) Arrêt Barel", "C) Arrêt Jamart", "D) Arrêt Casanova"],
    "answer": "A",
    "explanation": "L'arrêt Pariset (1875) est fondateur sur le détournement de pouvoir.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Trompier-Gravier (1944) est célèbre pour avoir consacré :",
    "options": ["A) La non-rétroactivité des actes administratifs", "B) Le respect des droits de la défense", "C) L'égalité devant le service public", "D) L'exception d'illégalité"],
    "answer": "B",
    "explanation": "Il consacre le PGD du respect des droits de la défense avant toute sanction.",
    "theme": "Droit administratif"
  },
  {
    "question": "Laquelle de ces affirmations sur l'arrêt Société des concerts du conservatoire (1951) est exacte ?",
    "options": ["A) Il crée le PGD d'égalité devant le service public.", "B) Il interdit le droit de grève.", "C) Il soumet les SPIC au droit privé exclusivement.", "D) Il donne aux ministres le pouvoir de police générale."],
    "answer": "A",
    "explanation": "Cet arrêt érige en PGD le principe d'égalité régissant le fonctionnement des services publics.",
    "theme": "Droit administratif"
  },
  {
    "question": "En droit administratif ivoirien, la théorie des 'circonstances exceptionnelles' permettant d'assouplir la légalité est issue de :",
    "options": ["A) L'arrêt Heyriès (1918)", "B) L'arrêt GISTI (1978)", "C) L'arrêt Barel (1954)", "D) L'arrêt Couitéas (1923)"],
    "answer": "A",
    "explanation": "L'arrêt Heyriès a consacré la théorie des circonstances exceptionnelles (ici, la Première Guerre mondiale).",
    "theme": "Droit administratif"
  },
  {
    "question": "Selon l'arrêt Jamart (1936), les ministres disposent :",
    "options": ["A) D'un pouvoir réglementaire général", "B) Du pouvoir d'organiser leurs services", "C) Du pouvoir de police générale", "D) D'aucun pouvoir réglementaire"],
    "answer": "B",
    "explanation": "Même sans texte, tout chef de service (ministres) a le pouvoir d'organiser ses services.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel arrêt admet que l'Administration engage sa responsabilité sans faute pour le préjudice causé par une loi ?",
    "options": ["A) Arrêt La Fleurette (1938)", "B) Arrêt Regnault-Desroziers (1919)", "C) Arrêt Thouzellier (1956)", "D) Arrêt Couitéas (1923)"],
    "answer": "A",
    "explanation": "La Fleurette consacre la responsabilité de l'État du fait des lois sur le fondement de l'égalité devant les charges publiques.",
    "theme": "Droit administratif"
  },
  {
    "question": "Dans quel cas la responsabilité pour 'faute lourde' est-elle traditionnellement exigée ?",
    "options": ["A) Les actes médicaux", "B) Le fonctionnement de la justice administrative", "C) Les activités de police difficiles (Tomaso Grecco)", "D) Les contrats de marché public"],
    "answer": "C",
    "explanation": "L'arrêt Tomaso Grecco (1905) admet la responsabilité de l'État pour l'activité des services de police, mais exigeait traditionnellement une faute lourde.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel arrêt fait la distinction entre la faute personnelle et la faute de service ?",
    "options": ["A) Pelletier (1873)", "B) Anguet (1911)", "C) Époux Lemonnier (1918)", "D) Blanco (1873)"],
    "answer": "A",
    "explanation": "L'arrêt Pelletier (Tribunal des conflits) fonde le partage de responsabilité entre l'agent et l'administration.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le cumul d'une faute personnelle et d'une faute de service ayant causé un même dommage a été reconnu par :",
    "options": ["A) L'arrêt Anguet (1911)", "B) L'arrêt Pelletier (1873)", "C) L'arrêt Tomaso Grecco (1905)", "D) L'arrêt Barel (1954)"],
    "answer": "A",
    "explanation": "Anguet admet le cumul de fautes (faute personnelle commise à l'occasion du service et faute de service distincte).",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Barel (1954) concerne :",
    "options": ["A) L'égalité d'accès à la fonction publique", "B) La protection de la dignité humaine", "C) L'interdiction d'extrader pour un motif politique", "D) La liberté d'association"],
    "answer": "A",
    "explanation": "Le Conseil d'État a annulé la décision refusant à des candidats de se présenter à l'ENA pour des motifs politiques (communisme), consacrant l'égalité d'accès.",
    "theme": "Droit administratif"
  },
  {
    "question": "Sur le contrôle de l'esthétique par la police administrative, quel est l'arrêt de référence ?",
    "options": ["A) Lutetia (1959)", "B) Leroux (1997)", "C) Consorts Baud (1951)", "D) Commune de Morsang-sur-Orge (1995)"],
    "answer": "B",
    "explanation": "L'arrêt Leroux (1997) permet à la police d'intervenir pour des motifs d'esthétique (protection de l'environnement).",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Commune de Morsang-sur-Orge (1995) a intégré dans l'ordre public :",
    "options": ["A) La moralité publique", "B) La dignité de la personne humaine", "C) L'esthétique", "D) La sécurité des biens"],
    "answer": "B",
    "explanation": "L'arrêt sur le 'lancer de nains' consacre le respect de la dignité de la personne humaine comme composante de l'ordre public.",
    "theme": "Droit administratif"
  },
  {
    "question": "Dans quel arrêt le Conseil d'État a-t-il affirmé qu'une mesure de police doit être proportionnée ?",
    "options": ["A) Arrêt Benjamin (1933)", "B) Arrêt Labonne (1919)", "C) Arrêt Daudignac (1951)", "D) Arrêt Lutetia (1959)"],
    "answer": "A",
    "explanation": "L'arrêt Benjamin exige un contrôle de proportionnalité entre les risques de trouble et la liberté de réunion.",
    "theme": "Droit administratif"
  },
  {
    "question": "Selon l'arrêt Monpeurt (1942), des organismes privés peuvent :",
    "options": ["A) Prendre des actes administratifs unilatéraux s'ils gèrent un SPA.", "B) Être jugés par les tribunaux de l'ordre judiciaire exclusivement.", "C) Échapper à tout contrôle de légalité.", "D) Adopter des lois de police."],
    "answer": "A",
    "explanation": "Monpeurt admet qu'une personne privée gérant un SPA (Service Public Administratif) peut édicter des actes administratifs unilatéraux.",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'établit l'arrêt Magnier (1961) en matière d'AAU ?",
    "options": ["A) Les actes des SPIC gérés par des personnes privées sont administratifs s'ils manifestent des prérogatives de puissance publique.", "B) Tous les actes des SPIC sont privés.", "C) Les circulaires ne sont jamais des AAU.", "D) Les mesures d'ordre intérieur peuvent être annulées."],
    "answer": "A",
    "explanation": "Magnier étend la solution Monpeurt aux SPIC (gérés par des personnes privées) si la décision traduit l'exercice d'une prérogative de puissance publique.",
    "theme": "Droit administratif"
  },
  {
    "question": "Concernant les circulaires, la distinction entre circulaires réglementaires et interprétatives a été dégagée par :",
    "options": ["A) L'arrêt Chapou (1954)", "B) L'arrêt Kreisker (1954)", "C) L'arrêt Jamart (1936)", "D) L'arrêt Gomard (2000)"],
    "answer": "B",
    "explanation": "L'arrêt Notre-Dame du Kreisker (1954) distinguait circulaires réglementaires (susceptibles de recours) et interprétatives (insusceptibles).",
    "theme": "Droit administratif"
  },
  {
    "question": "Un acte administratif préparatoire est-il susceptible de REP (Recours pour Excès de Pouvoir) selon la jurisprudence ?",
    "options": ["A) Oui, toujours", "B) Non, jamais (ex: Arrêt Nado Koutouan)", "C) Uniquement s'il est publié", "D) Uniquement s'il émane d'un ministre"],
    "answer": "B",
    "explanation": "Les actes préparatoires ne font pas grief et ne peuvent faire l'objet d'un REP direct (jurisprudence constante, ex: Nado Koutouan en CI).",
    "theme": "Droit administratif"
  },
  {
    "question": "Laquelle des théories suivantes justifie la continuité du service public malgré l'illégalité de la nomination de l'agent (Arrêt Ducastel) ?",
    "options": ["A) Le fonctionnaire de fait", "B) L'urgence absolue", "C) La force majeure", "D) L'imprévision"],
    "answer": "A",
    "explanation": "La théorie du fonctionnaire de fait permet de valider les actes d'une personne dont l'investiture est irrégulière, pour garantir la continuité du service public.",
    "theme": "Droit administratif"
  },
  {
    "question": "En matière de contrats administratifs, l'imprévision (Gaz de Bordeaux, 1916) donne droit à :",
    "options": ["A) Une résiliation de plein droit", "B) Une indemnisation intégrale du cocontractant", "C) Une indemnité d'imprévision pour l'aider à surmonter la difficulté", "D) L'annulation du contrat"],
    "answer": "C",
    "explanation": "Le cocontractant a droit à une aide (indemnité d'imprévision) mais doit continuer à exécuter le contrat.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le 'fait du prince' se caractérise par :",
    "options": ["A) Un bouleversement économique extérieur", "B) Une mesure prise par l'Administration contractante qui alourdit les charges du cocontractant", "C) Une force majeure irrésistible", "D) Une faute du cocontractant"],
    "answer": "B",
    "explanation": "Le fait du prince ouvre droit à une indemnisation intégrale si l'Administration, agissant à un autre titre que contractant, aggrave les charges de son partenaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Une clause exorbitante du droit commun est un critère :",
    "options": ["A) De qualification d'un acte administratif unilatéral", "B) Matériel de qualification d'un contrat administratif", "C) De responsabilité sans faute", "D) De la compétence judiciaire"],
    "answer": "B",
    "explanation": "La présence d'une clause exorbitante (ou participation au service public) est le critère matériel du contrat administratif.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Dame Lamotte (1950) pose que :",
    "options": ["A) Le REP est ouvert contre tout acte administratif sans qu'aucun texte ne le prévoie.", "B) Le REP est interdit en matière de police des étrangers.", "C) Seuls les actes publiés peuvent être contestés.", "D) L'Administration ne peut engager sa responsabilité sans faute."],
    "answer": "A",
    "explanation": "Le REP est ouvert même sans texte contre tout acte administratif (PGD).",
    "theme": "Droit administratif"
  },
  {
    "question": "La responsabilité de l'État du fait d'une décision de justice régulière est issue de :",
    "options": ["A) L'arrêt Couitéas (1923)", "B) L'arrêt La Fleurette (1938)", "C) L'arrêt Barel (1954)", "D) L'arrêt Tomaso Grecco (1905)"],
    "answer": "A",
    "explanation": "Dans Couitéas, l'État a refusé de prêter le concours de la force publique pour exécuter une décision de justice, engageant sa responsabilité sans faute (rupture égalité).",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle autorité dispose du pouvoir de police générale au niveau national (Jurisprudence Labonne) ?",
    "options": ["A) Le Premier ministre / Le Chef de l'État", "B) Le Ministre de l'Intérieur", "C) Le Préfet", "D) Le Maire"],
    "answer": "A",
    "explanation": "L'arrêt Labonne (1919) reconnaît au Chef de l'État (transféré au Premier ministre en France) le pouvoir de police générale sur tout le territoire.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Casanova (1901) a admis la recevabilité du recours :",
    "options": ["A) D'un fonctionnaire contre son supérieur", "B) D'un contribuable local contre une dépense de sa commune", "C) D'un ministre contre un décret", "D) D'un étranger contre son expulsion"],
    "answer": "B",
    "explanation": "Casanova consacre l'intérêt à agir du contribuable local contre les décisions ayant des répercussions sur les finances de sa collectivité.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt L'Aurore (1948) érige en PGD :",
    "options": ["A) La liberté d'expression", "B) Le principe de non-rétroactivité des actes administratifs", "C) Le droit à un procès équitable", "D) L'égalité de traitement"],
    "answer": "B",
    "explanation": "L'Aurore affirme que les actes administratifs ne peuvent pas avoir d'effet rétroactif, sauf exception législative.",
    "theme": "Droit administratif"
  },
  {
    "question": "Un recours hiérarchique :",
    "options": ["A) N'est possible que si un texte le prévoit", "B) S'adresse au supérieur hiérarchique de l'auteur de l'acte", "C) Remplace le juge administratif", "D) Doit obligatoirement être précédé d'un recours gracieux"],
    "answer": "B",
    "explanation": "L'arrêt Queralt a établi que le pouvoir hiérarchique existe de plein droit et permet un recours auprès du supérieur de l'auteur de l'acte.",
    "theme": "Droit administratif"
  },
  {
    "question": "La jurisprudence Commune de Néris-les-Bains (1902) reconnaît :",
    "options": ["A) Qu'une autorité de police locale peut aggraver une mesure de police nationale si les circonstances locales l'exigent.", "B) Qu'un maire ne peut jamais prendre d'arrêté de police.", "C) Que l'État n'est jamais responsable des fautes des maires.", "D) Qu'un maire est soumis au pouvoir hiérarchique du préfet dans tous les cas."],
    "answer": "A",
    "explanation": "Une autorité inférieure peut rendre une mesure de police plus rigoureuse que celle de l'autorité supérieure, justifiée par des circonstances locales.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'ARCOP en Côte d'Ivoire est chargée :",
    "options": ["A) Du contrôle budgétaire de l'État", "B) De la régulation de la commande publique", "C) De l'organisation des élections", "D) De la nomination des magistrats"],
    "answer": "B",
    "explanation": "L'ARCOP (Autorité de Régulation de la Commande Publique) régule les marchés publics en Côte d'Ivoire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le contentieux du foncier en Côte d'Ivoire constitue actuellement :",
    "options": ["A) La minorité des affaires devant le Conseil d'État", "B) Une partie insignifiante depuis la réforme de 2020", "C) Le contentieux le plus abondant devant le Conseil d'État", "D) Une matière exclusivement judiciaire"],
    "answer": "C",
    "explanation": "Les bilans récents de l'activité du CE ivoirien (2025-2026) montrent que le foncier est le contentieux dominant.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Nicolo (1989) consacre :",
    "options": ["A) La primauté des traités internationaux sur les lois nationales postérieures", "B) La primauté de la Constitution sur les traités", "C) L'incompétence du juge administratif pour interpréter un traité", "D) La responsabilité sans faute pour acte de gouvernement"],
    "answer": "A",
    "explanation": "Nicolo marque l'acceptation par le juge administratif de contrôler la conformité d'une loi à un traité international (article 55 Constitution).",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Rubin de Servens (1962) qualifie la décision de recourir à l'article 16 (pleins pouvoirs) de :",
    "options": ["A) Acte administratif réglementaire", "B) Acte de gouvernement insusceptible de recours", "C) Acte préparatoire", "D) Mesure d'ordre intérieur"],
    "answer": "B",
    "explanation": "Le recours aux pouvoirs de crise est un acte de gouvernement, échappant au contrôle du juge administratif.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Consorts Baud (1951) fait la distinction entre :",
    "options": ["A) Police administrative et police judiciaire", "B) Faute lourde et faute simple", "C) SPA et SPIC", "D) Contrat administratif et contrat privé"],
    "answer": "A",
    "explanation": "Consorts Baud (CE) et Noualek (TC) posent le critère finaliste (prévention vs répression) pour distinguer police administrative et judiciaire.",
    "theme": "Droit administratif"
  },
  {
    "question": "Une mesure d'ordre intérieur (ex: Arrêt Chapou) :",
    "options": ["A) Est toujours annulable par le juge", "B) Ne fait généralement pas grief et échappe au REP", "C) Est un synonyme d'acte de gouvernement", "D) Ne concerne que la fonction publique"],
    "answer": "B",
    "explanation": "Traditionnellement, les mesures d'ordre intérieur (ex: affectation dans une classe, punition scolaire minime) sont insusceptibles de REP car elles ne font pas grief (sauf si elles affectent les libertés).",
    "theme": "Droit administratif"
  },
  {
    "question": "Le juge de l'excès de pouvoir contrôle-t-il l'opportunité d'une décision administrative ?",
    "options": ["A) Oui, de manière systématique", "B) Non, il ne contrôle que la légalité", "C) Oui, depuis l'arrêt Barel", "D) Uniquement pour les actes réglementaires"],
    "answer": "B",
    "explanation": "Le REP est un contentieux de la légalité, pas de l'opportunité (sauf dans le contrôle de proportionnalité qui s'en rapproche sans être un contrôle pur d'opportunité).",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Époux Lemonnier (1918) complète l'arrêt Anguet en admettant :",
    "options": ["A) La responsabilité sans faute", "B) Le cumul de responsabilités pour une faute unique commise dans le service", "C) L'irresponsabilité de l'État", "D) L'enrichissement sans cause"],
    "answer": "B",
    "explanation": "Pour une même faute (unique) commise dans le service, la victime peut rechercher la responsabilité de l'agent (faute personnelle) ET celle de l'Administration (faute de service).",
    "theme": "Droit administratif"
  },
  {
    "question": "Selon la jurisprudence Daudignac (1951), l'instauration d'un régime d'autorisation préalable par la police administrative :",
    "options": ["A) Est toujours légale", "B) Est illégale si elle porte atteinte à la liberté du commerce et de l'industrie sans base légale", "C) Relève du pouvoir discrétionnaire du maire", "D) N'est possible que pour la presse"],
    "answer": "B",
    "explanation": "Seul le législateur peut instaurer un régime d'autorisation préalable touchant aux libertés publiques. Le maire ne peut le faire par arrêté (Daudignac).",
    "theme": "Droit administratif"
  },
  {
    "question": "L'arrêt Regnault-Desroziers (1919) fonde la responsabilité de l'État sur :",
    "options": ["A) Le risque (choses dangereuses)", "B) La faute lourde", "C) Le défaut d'entretien d'un ouvrage public", "D) La rupture de l'égalité devant les charges publiques"],
    "answer": "A",
    "explanation": "L'explosion d'un dépôt de munitions a engagé la responsabilité sans faute de l'État basée sur le risque lié aux choses dangereuses.",
    "theme": "Droit administratif"
  },
  {
    "question": "En Côte d'Ivoire, l'ordre de juridiction administrative est coiffé par :",
    "options": ["A) La Cour Suprême", "B) Le Conseil d'État", "C) Le Conseil Constitutionnel", "D) La Haute Cour de Justice"],
    "answer": "B",
    "explanation": "Depuis la Constitution de 2016, l'ordre administratif est dirigé par le Conseil d'État (la Cour Suprême ayant été scindée en Cour de Cassation, CE et Cour des Comptes).",
    "theme": "Droit administratif"
  },
  {
    "question": "Une décision de l'ARCOP peut-elle faire l'objet d'un recours devant le Conseil d'État ivoirien ?",
    "options": ["A) Non, ses décisions sont souveraines", "B) Oui, par la voie du REP", "C) Uniquement devant les juridictions civiles", "D) Uniquement par arbitrage international"],
    "answer": "B",
    "explanation": "L'ARCOP est une AAI (Autorité Administrative Indépendante) ; ses décisions faisant grief sont des actes administratifs contestables devant le juge administratif.",
    "theme": "Droit administratif"
  },
  {
    "question": "Laquelle des affirmations suivantes caractérise un Service Public Industriel et Commercial (SPIC) en droit ivoirien ?",
    "options": ["A) Il est régi exclusivement par le droit public.", "B) Le personnel est soumis au statut général de la fonction publique.", "C) Ses litiges avec les usagers relèvent du juge judiciaire.", "D) Il ne peut jamais prendre d'actes administratifs."],
    "answer": "C",
    "explanation": "Les litiges entre un SPIC et ses usagers relèvent en principe du juge judiciaire (Tribunal des conflits, Bac d'Eloka, 1921), même s'il est géré par une personne publique.",
    "theme": "Droit administratif"
  },
  {
    "question": "Dans le cadre des marchés publics ivoiriens, quel est le principe général de passation ?",
    "options": ["A) Le gré à gré", "B) L'appel d'offres ouvert", "C) L'appel d'offres restreint", "D) L'adjudication"],
    "answer": "B",
    "explanation": "Selon le Code des marchés publics ivoirien, l'appel d'offres ouvert est la règle. Le gré à gré est une exception strictement encadrée.",
    "theme": "Droit administratif"
  },
  {
    "question": "Une décision de l'ARCOP (Autorité de Régulation de la Commande Publique) excluant une entreprise des marchés publics pendant 5 ans :",
    "options": ["A) Est une mesure d'ordre intérieur insusceptible de recours", "B) Relève de la compétence exclusive de la Chambre de Commerce et d'Industrie", "C) Est un acte administratif faisant grief, susceptible de recours pour excès de pouvoir", "D) Ne peut être contestée que par la voie diplomatique"],
    "answer": "C",
    "explanation": "L'ARCOP est une Autorité Administrative Indépendante ; ses décisions de sanction font grief et peuvent être attaquées par la voie du REP devant le Conseil d'État.",
    "theme": "Droit administratif"
  },
  {
    "question": "En matière de contrats administratifs, si le cocontractant de l'Administration est en faute, celle-ci peut :",
    "options": ["A) S'adresser systématiquement au juge pour prononcer la résiliation.", "B) Prononcer une sanction unilatérale, y compris la résiliation, même sans texte.", "C) Uniquement suspendre le paiement.", "D) Demander l'annulation du contrat pour erreur sur la personne."],
    "answer": "B",
    "explanation": "L'Administration dispose d'un pouvoir de sanction unilatérale (pénalités, résiliation pour faute) inhérent aux contrats administratifs, sans avoir besoin de s'adresser au juge au préalable (Arrêt Deville-lès-Rouen).",
    "theme": "Droit administratif"
  },
  {
    "question": "Selon la jurisprudence de la Compagnie générale française des tramways (1910), l'Administration peut :",
    "options": ["A) Modifier unilatéralement un contrat pour motif d'intérêt général.", "B) Refuser de payer son cocontractant sans motif.", "C) Être exemptée de toute responsabilité en cas de force majeure.", "D) Annuler tous les contrats à la fin de l'année budgétaire."],
    "answer": "A",
    "explanation": "Cet arrêt reconnaît le pouvoir de modification unilatérale de l'Administration pour les besoins du service public, moyennant une indemnisation du cocontractant.",
    "theme": "Droit administratif"
  },
  {
    "question": "En Côte d'Ivoire, qu'est-ce qui caractérise le domaine public par rapport au domaine privé de l'État ?",
    "options": ["A) Il est prescriptible.", "B) Il est aliénable et saisissable.", "C) Il est inaliénable, imprescriptible et insaisissable.", "D) Il est géré exclusivement par des sociétés privées."],
    "answer": "C",
    "explanation": "Le domaine public est protégé par les principes d'inaliénabilité, d'imprescriptibilité et d'insaisissabilité pour garantir son affectation à l'utilité publique.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel critère principal permet de déterminer si un bien appartient au domaine public artificiel ?",
    "options": ["A) L'affectation à l'usage direct du public ou à un service public avec aménagement spécial.", "B) La simple propriété d'une personne publique.", "C) Son enregistrement au cadastre.", "D) Sa valeur vénale supérieure à un milliard de FCFA."],
    "answer": "A",
    "explanation": "Pour qu'un bien entre dans le domaine public artificiel, il doit appartenir à une personne publique ET être affecté à l'usage du public, ou à un service public pourvu qu'il fasse l'objet d'un aménagement spécial (ou indispensable depuis la jurisprudence française plus récente).",
    "theme": "Droit administratif"
  },
  {
    "question": "Un ouvrage public est :",
    "options": ["A) Tout immeuble appartenant à un particulier.", "B) Un bien meuble affecté à un service public.", "C) Un immeuble résultant d'un travail public affecté à un but d'utilité générale.", "D) Obligatoirement une route ou un pont."],
    "answer": "C",
    "explanation": "L'ouvrage public est un bien immobilier (immeuble par nature ou par destination) qui est le résultat d'un travail public et qui est affecté à une fin d'intérêt général.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel est le fondement du recours dit 'Tropic Travaux Signalisation' (2007) ?",
    "options": ["A) Permettre aux tiers évincés de contester la validité du contrat administratif.", "B) Interdire la passation de marchés de gré à gré.", "C) Obliger l'Administration à indemniser en cas d'imprévision.", "D) Transférer le contentieux contractuel au juge judiciaire."],
    "answer": "A",
    "explanation": "Cette jurisprudence (puis Tarn-et-Garonne) a ouvert le recours de plein contentieux contre le contrat lui-même aux tiers (notamment les concurrents évincés) justifiant d'un intérêt lésé.",
    "theme": "Droit administratif"
  },
  {
    "question": "En droit administratif ivoirien, la concession de service public se distingue du marché public principalement par :",
    "options": ["A) La nature du cocontractant qui doit être obligatoirement public.", "B) Le mode de rémunération, lié substantiellement aux résultats de l'exploitation.", "C) L'absence de procédure de mise en concurrence.", "D) La durée du contrat, qui ne peut excéder un an."],
    "answer": "B",
    "explanation": "Dans la concession (ou délégation de service public), la rémunération du cocontractant provient substantiellement des résultats de l'exploitation du service (le risque d'exploitation est transféré au concessionnaire).",
    "theme": "Droit administratif"
  },
  {
    "question": "Selon l'arrêt TC, Bac d'Eloka (1921), les services publics gérés dans des conditions similaires à celles d'une entreprise privée sont des :",
    "options": ["A) SPA (Services Publics Administratifs).", "B) SPIC (Services Publics Industriels et Commerciaux).", "C) Établissements d'utilité publique.", "D) Organismes de bienfaisance."],
    "answer": "B",
    "explanation": "Cet arrêt fondateur donne naissance à la notion de SPIC, gérés selon des méthodes comparables à celles des entreprises privées et soumis largement au droit privé.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle autorité en Côte d'Ivoire est compétente pour déclarer l'utilité publique en vue d'une expropriation ?",
    "options": ["A) Le Juge civil", "B) Le Chef de village", "C) L'Administration (par décret ou arrêté, selon l'importance)", "D) Le Conseil Constitutionnel"],
    "answer": "C",
    "explanation": "La Déclaration d'Utilité Publique (DUP) est un acte administratif préalable à la procédure d'expropriation, relevant de l'exécutif.",
    "theme": "Droit administratif"
  },
  {
    "question": "Dans le régime du gré à gré (entente directe) en matière de commande publique ivoirienne :",
    "options": ["A) L'Administration contracte librement sans aucune justification.", "B) Une autorisation préalable est requise dans des cas limitativement énumérés par le Code (ex: urgence impérieuse).", "C) Le contrat n'a pas la qualification de contrat administratif.", "D) Seules les entreprises étrangères sont éligibles."],
    "answer": "B",
    "explanation": "Le marché de gré à gré est une procédure exceptionnelle qui nécessite l'accord des autorités de contrôle (ministre du budget) et doit s'inscrire dans des cas précis (urgence, secret, brevet exclusif...).",
    "theme": "Droit administratif"
  },
  {
    "question": "Le privilège de l'exécution d'office permet à l'Administration de :",
    "options": ["A) Forcer le juge à rendre une décision.", "B) Imposer directement l'exécution de ses décisions unilatérales sans recourir au juge.", "C) Poursuivre pénalement tout citoyen.", "D) S'exonérer de ses obligations contractuelles sans motif."],
    "answer": "B",
    "explanation": "C'est l'essence même de l'acte administratif unilatéral : le privilège du préalable ou de l'exécution d'office permet à l'Administration d'agir sans autorisation du juge.",
    "theme": "Droit administratif"
  },
  {
    "question": "En cas de dommage causé par un dommage de travaux publics, la victime a le statut de :",
    "options": ["A) Usager, tiers ou participant.", "B) Fonctionnaire, stagiaire ou contractuel.", "C) Contribuable ou administré.", "D) Créancier chirographaire."],
    "answer": "A",
    "explanation": "La responsabilité de l'Administration diffère selon la qualité de la victime : tiers (responsabilité sans faute), usager (faute présumée), ou participant (faute prouvée en général).",
    "theme": "Droit administratif"
  },
  {
    "question": "Quelle est la principale différence entre la théorie de l'imprévision et la force majeure dans les contrats administratifs ?",
    "options": ["A) L'imprévision entraîne une résiliation immédiate ; la force majeure permet la poursuite du contrat.", "B) L'imprévision donne droit à une aide financière pour continuer ; la force majeure justifie la résiliation.", "C) L'imprévision est causée par l'Administration ; la force majeure par un tiers.", "D) Il n'y a aucune différence en droit ivoirien."],
    "answer": "B",
    "explanation": "La force majeure (imprévisible, irrésistible, extérieure) empêche l'exécution et entraîne la résiliation sans indemnisation de l'Administration ; l'imprévision bouleverse l'économie mais ne rend pas l'exécution impossible, donnant droit à une indemnité d'imprévision pour continuer.",
    "theme": "Droit administratif"
  },
  {
    "question": "L'occupation du domaine public :",
    "options": ["A) Est un droit inaliénable pour tout citoyen.", "B) Est nécessairement temporaire, révocable et précaire.", "C) Confère la propriété des sols occupés au bout de 10 ans.", "D) Ne nécessite aucune autorisation préalable."],
    "answer": "B",
    "explanation": "L'autorisation d'occupation du domaine public est toujours délivrée à titre précaire et révocable (pour des motifs d'intérêt général).",
    "theme": "Droit administratif"
  },
  {
    "question": "Lorsqu'un contrat contient une clause par laquelle l'Administration s'octroie des pouvoirs de contrôle sur le cocontractant qui n'existent pas en droit privé, on parle de :",
    "options": ["A) Clause de sauvegarde", "B) Clause exorbitante du droit commun", "C) Clause compromissoire", "D) Clause pénale"],
    "answer": "B",
    "explanation": "C'est la définition même de la clause exorbitante du droit commun, critère matériel du contrat administratif (jurisprudence Société des granits porphyroïdes des Vosges, 1912).",
    "theme": "Droit administratif"
  },
  {
    "question": "En matière de domaine public, la 'théorie des mutations domaniales' permet :",
    "options": ["A) De vendre un bien du domaine public à un particulier.", "B) À l'État de transférer l'affectation d'un bien du domaine public d'une collectivité vers un autre usage public d'intérêt supérieur.", "C) D'intégrer un bien privé dans le domaine public sans DUP.", "D) De modifier les frontières communales."],
    "answer": "B",
    "explanation": "Cette théorie jurisprudentielle permet à l'État, garant de l'intérêt général, de modifier l'affectation d'une dépendance du domaine public d'une collectivité (moyennant indemnisation) si un intérêt public supérieur le justifie.",
    "theme": "Droit administratif"
  },
  {
    "question": "Un contrat passé entre deux personnes publiques est présumé être :",
    "options": ["A) Un contrat de droit privé.", "B) Un contrat administratif.", "C) Insusceptible de recours.", "D) Un acte unilatéral déguisé."],
    "answer": "B",
    "explanation": "Selon la jurisprudence UAP (1983), un contrat conclu entre deux personnes publiques est présumé revêtir un caractère administratif (sauf s'il ne fait naître que des rapports de droit privé).",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel principe régit le fonctionnement continu des services publics (lois de Rolland) ?",
    "options": ["A) Le principe d'adaptation (ou mutabilité)", "B) Le principe de continuité", "C) Le principe d'égalité", "D) Le principe de laïcité"],
    "answer": "B",
    "explanation": "Les trois 'Lois de Rolland' sont : Continuité, Mutabilité (adaptation), et Égalité. Le fonctionnement continu est dicté par le principe de continuité (Arrêt Dehaene).",
    "theme": "Droit administratif"
  },
  {
    "question": "Dans le contentieux de l'expropriation, quelle étape relève de la compétence exclusive du juge judiciaire (en l'absence d'accord amiable) ?",
    "options": ["A) La déclaration d'utilité publique", "B) L'enquête parcellaire", "C) Le transfert de propriété et la fixation de l'indemnité", "D) L'arrêté de cessibilité"],
    "answer": "C",
    "explanation": "L'expropriation comprend une phase administrative (DUP, arrêtés) et une phase judiciaire. Le juge judiciaire est seul compétent (protecteur de la propriété) pour prononcer le transfert de propriété et fixer le montant de l'indemnité s'il n'y a pas d'accord.",
    "theme": "Droit administratif"
  },
  {
    "question": "La régie est un mode de gestion du service public dans lequel :",
    "options": ["A) L'Administration confie le service à une société anonyme cotée en bourse.", "B) L'Administration gère elle-même le service avec son propre personnel et ses propres deniers.", "C) Un particulier s'engage à gérer le service à ses risques et périls.", "D) Une ONG gère le service sur fonds internationaux."],
    "answer": "B",
    "explanation": "La régie (simple ou autonome) est le mode de gestion directe par la personne publique.",
    "theme": "Droit administratif"
  },
  {
    "question": "En Côte d'Ivoire, pour être qualifié de marché de partenariat (ou Partenariat Public-Privé - PPP) :",
    "options": ["A) Le partenaire privé doit assumer la construction, l'entretien, l'exploitation ou la gestion d'un équipement public.", "B) L'État doit transférer la souveraineté au partenaire privé.", "C) Le contrat doit être gratuit.", "D) Le paiement de l'entreprise doit être exclusivement assuré par les péages des usagers."],
    "answer": "A",
    "explanation": "Le PPP (marché de partenariat) est un contrat global où le partenaire privé finance, construit, et gère un ouvrage, avec une rémunération versée par la personne publique (contrairement à la concession où l'usager paie en majorité).",
    "theme": "Droit administratif"
  },
  {
    "question": "Le déclassement d'un bien du domaine public (pour le faire entrer dans le domaine privé) exige au préalable :",
    "options": ["A) Une simple décision du conseil municipal.", "B) La désaffectation de fait ou de droit du bien (fin de son affectation à l'utilité publique).", "C) L'approbation du juge de cassation.", "D) Sa vente aux enchères."],
    "answer": "B",
    "explanation": "Pour qu'un bien sorte du domaine public, il faut qu'il y ait d'abord désaffectation matérielle (il ne sert plus au public/service) PUIS un acte juridique de déclassement.",
    "theme": "Droit administratif"
  },
  {
    "question": "En Côte d'Ivoire, quelle juridiction est compétente en premier ressort pour statuer sur les litiges relatifs à la carrière des fonctionnaires de l'État ?",
    "options": ["A) Le Conseil d'État, compétence exclusive et directe", "B) Les Tribunaux administratifs", "C) La Cour administrative d'appel", "D) Le Tribunal du Travail"],
    "answer": "A",
    "explanation": "Historiquement et encore en grande partie, en attendant le déploiement effectif complet des tribunaux administratifs sur tout le territoire, le Conseil d'État ivoirien (ex-Chambre administrative) a souvent gardé une compétence directe en premier et dernier ressort pour les recours pour excès de pouvoir des fonctionnaires nommés par décret, bien que la loi organique prévoie un démembrement progressif.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel est le délai de droit commun pour introduire un recours pour excès de pouvoir (REP) devant le juge administratif ivoirien ?",
    "options": ["A) 1 mois", "B) 2 mois", "C) 3 mois", "D) 6 mois"],
    "answer": "B",
    "explanation": "Le délai de droit commun pour exercer un REP contre une décision administrative est de deux (2) mois à compter de sa publication ou de sa notification.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le recours gracieux adressé à l'auteur de l'acte a pour effet de :",
    "options": ["A) Suspendre immédiatement l'exécution de l'acte administratif.", "B) Proroger le délai de recours contentieux.", "C) Rendre l'acte nul de plein droit.", "D) Saisir automatiquement le Conseil d'État après 10 jours."],
    "answer": "B",
    "explanation": "Le dépôt d'un recours administratif préalable (gracieux ou hiérarchique) dans le délai de 2 mois interrompt (proroge) le délai de recours contentieux, qui recommence à courir après la réponse de l'Administration.",
    "theme": "Droit administratif"
  },
  {
    "question": "Dans le cadre d'un contentieux de pleine juridiction (ou plein contentieux), le juge administratif peut :",
    "options": ["A) Uniquement annuler la décision administrative.", "B) Modifier la décision, condamner l'Administration au paiement d'indemnités et substituer sa propre décision.", "C) Juger les litiges entre particuliers.", "D) Demander l'avis du Parlement."],
    "answer": "B",
    "explanation": "Contrairement au REP où le juge ne peut qu'annuler, dans le plein contentieux, le juge dispose de pouvoirs très étendus : condamnation pécuniaire, réformation de l'acte.",
    "theme": "Droit administratif"
  },
  {
    "question": "Quel est le sort d'un recours pour excès de pouvoir (REP) si le requérant ne démontre pas d'intérêt à agir ?",
    "options": ["A) Il est jugé sur le fond mais les dommages-intérêts sont refusés.", "B) Il est irrecevable.", "C) L'affaire est renvoyée au juge civil.", "D) Le Médiateur de la République est automatiquement saisi."],
    "answer": "B",
    "explanation": "L'intérêt à agir (personnel, direct, légitime) est une condition de recevabilité absolue du REP. À défaut, la requête est rejetée pour irrecevabilité (Arrêt Casanova).",
    "theme": "Droit administratif"
  },
  {
    "question": "En procédure administrative ivoirienne, l'introduction d'un recours contentieux a-t-elle un effet suspensif ?",
    "options": ["A) Oui, toujours, c're le principe de précaution.", "B) Non, le recours n'a pas d'effet suspensif, sauf exception prévue par la loi ou décision du juge (sursis à exécution/référé).", "C) Oui, si le requérant verse une caution.", "D) Non, sauf si l'acte émane d'un préfet."],
    "answer": "B",
    "explanation": "C'est la règle fondamentale du privilège du préalable : le recours contentieux ne suspend pas l'exécution de l'acte administratif, sauf si le juge prononce un sursis à exécution (référé-suspension).",
    "theme": "Droit administratif"
  },
  {
    "question": "Pour obtenir un sursis à exécution (référé-suspension) d'une décision administrative, quelles sont les deux conditions cumulatives traditionnellement exigées ?",
    "options": ["A) Urgence et faute grave de l'Administration.", "B) Urgence et doute sérieux quant à la légalité de l'acte.", "C) Préjudice financier et absence d'enquête publique.", "D) Faute personnelle de l'agent et compétence du juge judiciaire."],
    "answer": "B",
    "explanation": "Le juge des référés peut suspendre un acte si l'urgence le justifie ET s'il est fait état d'un moyen propre à créer, en l'état de l'instruction, un doute sérieux sur la légalité de la décision.",
    "theme": "Droit administratif"
  },
  {
    "question": "La procédure du 'référé-liberté' permet au juge administratif de statuer dans un délai d'urgence de :",
    "options": ["A) 48 heures", "B) 7 jours", "C) 1 mois", "D) 3 mois"],
    "answer": "A",
    "explanation": "Le référé-liberté (inspiré du droit français et intégré dans les procédures modernes) impose au juge de statuer dans les 48 heures en cas d'atteinte grave et manifestement illégale à une liberté fondamentale par l'Administration.",
    "theme": "Droit administratif"
  },
  {
    "question": "La Cour des Comptes, en tant que juridiction financière supérieure, relève-t-elle de l'ordre administratif ivoirien au sens strict des recours des particuliers ?",
    "options": ["A) Oui, elle juge les recours en annulation des contribuables contre les impôts.", "B) Non, elle forme un ordre juridictionnel financier distinct chargé du contrôle des comptables publics.", "C) Oui, c'est une chambre spécialisée du Conseil d'État.", "D) Non, c'est une juridiction civile."],
    "answer": "B",
    "explanation": "La Cour des Comptes juge les comptes des comptables publics et contrôle la gestion financière, mais elle ne juge pas les actes administratifs faisant grief aux citoyens (c'est le rôle du Conseil d'État/Tribunaux administratifs).",
    "theme": "Droit administratif"
  },
  {
    "question": "Une recommandation émise par la Haute Autorité de la Communication Audiovisuelle (HACA), acte de droit souple :",
    "options": ["A) N'est jamais susceptible de recours pour excès de pouvoir.", "B) Peut faire l'objet d'un REP si elle produit des effets notables ou a une influence significative sur les comportements (jurisprudence de type Fairvesta/Numericable).", "C) Doit obligatoirement être ratifiée par le Parlement.", "D) Relève exclusivement de la Cour de Cassation."],
    "answer": "B",
    "explanation": "Le droit administratif moderne (ex: arrêts Fairvesta et Numericable en France, dont s'inspire la CI) admet la recevabilité du REP contre des actes de droit souple (recommandations, avis) s'ils produisent des effets notables ou sont de nature à influer sur les comportements.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le contentieux de la responsabilité quasi-délictuelle de l'État (dommages causés par un véhicule militaire) relève :",
    "options": ["A) Du plein contentieux", "B) Du recours pour excès de pouvoir", "C) Du contentieux de l'interprétation", "D) Du contentieux de la répression"],
    "answer": "A",
    "explanation": "Tout recours visant à obtenir de l'Administration le versement d'une indemnité en réparation d'un dommage relève du contentieux de pleine juridiction.",
    "theme": "Droit administratif"
  },
  {
    "question": "Si l'Administration garde le silence pendant deux mois suite à un recours gracieux en Côte d'Ivoire, cela équivaut à :",
    "options": ["A) Une décision implicite d'acceptation.", "B) Une décision implicite de rejet, permettant de saisir le juge.", "C) Une faute lourde de l'Administration indemnisable d'office.", "D) Un renvoi du dossier au Médiateur de la République."],
    "answer": "B",
    "explanation": "Le silence gardé par l'Administration pendant plus de 2 mois vaut généralement décision de rejet, contre laquelle un REP peut être formé.",
    "theme": "Droit administratif"
  },
  {
    "question": "La Règle de la décision préalable stipule que :",
    "options": ["A) Le juge ne peut être saisi qu'après une tentative de conciliation en mairie.", "B) Le contentieux administratif ne peut naître que d'une décision (expresse ou implicite) de l'Administration liant le contentieux.", "C) L'Administration doit toujours demander l'avis du juge avant de décider.", "D) Le requérant doit d'abord publier sa requête dans un journal officiel."],
    "answer": "B",
    "explanation": "On ne peut saisir le juge administratif qu'en attaquant une décision. S'il n'y en a pas, il faut d'abord adresser une demande à l'Administration pour faire naître une décision (règle de la décision préalable).",
    "theme": "Droit administratif"
  },
  {
    "question": "Qu'est-ce qu'un recours en révision devant le Conseil d'État ?",
    "options": ["A) Un recours visant à faire rejuger l'affaire par la même juridiction si une pièce décisive, retenue par la partie adverse, est découverte après l'arrêt.", "B) L'appel d'un jugement du Tribunal administratif.", "C) La demande d'interprétation d'une loi obscure.", "D) Une plainte pénale contre un magistrat."],
    "answer": "A",
    "explanation": "Le recours en révision est une voie de rétractation très exceptionnelle ouverte si le jugement a été rendu sur pièces fausses ou si une pièce décisive a été découverte tardivement.",
    "theme": "Droit administratif"
  },
  {
    "question": "Un acte recognitif (qui se borne à reconnaître une situation juridique préexistante sans rien y ajouter) :",
    "options": ["A) Est l'équivalent d'un règlement autonome.", "B) Fait grief et est donc susceptible de REP.", "C) Ne fait pas grief et ne peut être attaqué par la voie du REP.", "D) Doit toujours être contresigné."],
    "answer": "C",
    "explanation": "L'acte purement recognitif ou confirmatif (comme un acte préparatoire ou une mesure d'ordre intérieur) ne modifie pas l'ordonnancement juridique et ne fait pas grief. Il est insusceptible de REP.",
    "theme": "Droit administratif"
  },
  {
    "question": "La compétence pour statuer sur le contentieux des élections municipales et régionales en Côte d'Ivoire appartient :",
    "options": ["A) À la Cour de Cassation", "B) Au Conseil Constitutionnel", "C) Au Conseil d'État", "D) À la Commission Électorale Indépendante (CEI)"],
    "answer": "C",
    "explanation": "Le Conseil Constitutionnel gère les élections présidentielles et législatives. Le Conseil d'État est le juge du contentieux des élections locales (municipales et régionales).",
    "theme": "Droit administratif"
  },
  {
    "question": "Dans le contentieux administratif, la tierce opposition est une voie de recours permettant :",
    "options": ["A) À l'Administration de refuser d'exécuter un jugement.", "B) À une personne non appelée à l'instance d'attaquer une décision de justice qui préjudicie à ses droits.", "C) D'obliger trois juges à statuer sur l'affaire.", "D) De suspendre le délai de recours contentieux."],
    "answer": "B",
    "explanation": "La tierce opposition protège les tiers lésés par un jugement auquel ils n'ont été ni parties ni représentés.",
    "theme": "Droit administratif"
  },
  {
    "question": "Un avis rendu par le Conseil d'État dans sa fonction consultative (avant l'adoption d'un projet de loi) :",
    "options": ["A) Est un acte administratif susceptible de recours.", "B) Lie obligatoirement le gouvernement qui doit s'y conformer.", "C) Ne fait pas grief et est insusceptible de recours contentieux.", "D) Doit être publié au Journal Officiel obligatoirement."],
    "answer": "C",
    "explanation": "Les avis (section consultative) sont des actes préparatoires qui ne font pas grief et ne lient pas l'Exécutif, ils ne peuvent donc pas faire l'objet d'un REP.",
    "theme": "Droit administratif"
  },
  {
    "question": "Le recours en appréciation de validité :",
    "options": ["A) Est porté devant le juge pénal pour juger de la constitutionnalité d'une loi.", "B) Est une question préjudicielle posée par un juge judiciaire au juge administratif pour contrôler la légalité d'un acte administratif.", "C) Concerne uniquement les actes de gouvernement.", "D) Permet au Président de la République d'évaluer le Parlement."],
    "answer": "B",
    "explanation": "Le juge civil, incompétent pour annuler un acte administratif, sursoit à statuer et renvoie la question de la légalité de cet acte au juge administratif via le recours en appréciation de validité.",
    "theme": "Droit administratif"
  },
  {
    "question": "Les litiges relatifs aux contrats comportant occupation du domaine public :",
    "options": ["A) Relèvent systématiquement de la compétence du juge administratif.", "B) Sont jugés par le juge judiciaire s'il n'y a pas de clause exorbitante.", "C) Relèvent de la Cour Commune de Justice et d'Arbitrage (CCJA).", "D) Sont insusceptibles de recours."],
    "answer": "A",
    "explanation": "Par détermination de la loi, les contrats comportant occupation du domaine public sont des contrats administratifs, de la compétence exclusive du juge administratif.",
    "theme": "Droit administratif"
  },
  {
    "question": "Laquelle de ces autorités judiciaires dirige les formations de jugement au sein du Conseil d'État de Côte d'Ivoire ?",
    "options": ["A) Le Procureur Général", "B) Le Président du Conseil d'État", "C) Le Premier Président de la Cour de Cassation", "D) Le Ministre de la Justice"],
    "answer": "B",
    "explanation": "Le Président du Conseil d'État dirige l'institution. Le Procureur Général est le chef du Parquet Général, mais il ne dirige pas les formations de jugement (siège).",
    "theme": "Droit administratif"
  },
  {
    "question": "Le contentieux fiscal en Côte d'Ivoire (recouvrement des impôts directs par l'État) relève en première instance de :",
    "options": ["A) La Chambre civile du Tribunal de Première Instance", "B) La juridiction administrative", "C) La Cour des Comptes", "D) La Chambre de Commerce"],
    "answer": "B",
    "explanation": "Le contentieux de l'assiette et du recouvrement des impôts directs est un contentieux administratif par excellence (plein contentieux).",
    "theme": "Droit administratif"
  },
  {
    "question": "L'exception d'illégalité permet :",
    "options": ["A) De soulever l'illégalité d'un règlement à l'occasion d'un recours contre une décision individuelle d'application, même après l'expiration du délai de recours contre le règlement.", "B) D'annuler un acte avec effet rétroactif.", "C) D'invoquer l'immunité diplomatique.", "D) De suspendre l'exécution d'un contrat de travail."],
    "answer": "A",
    "explanation": "L'exception d'illégalité permet d'écarter l'application d'un acte réglementaire illégal, même devenu définitif, lors de la contestation d'un acte d'application (principe de l'illégalité perpétuelle des règlements).",
    "theme": "Droit administratif"
  },
  {
    "question": "Si l'Administration refuse de prendre un règlement d'application d'une loi :",
    "options": ["A) Elle exerce son pouvoir discrétionnaire sans contrôle possible.", "B) Le refus est un acte faisant grief susceptible de REP, car l'Exécutif a l'obligation de prendre dans un délai raisonnable les mesures d'application des lois.", "C) Seul le Parlement peut la contraindre par une motion de censure.", "D) La loi est réputée inapplicable pour toujours."],
    "answer": "B",
    "explanation": "L'Administration est tenue de prendre les décrets d'application d'une loi dans un délai raisonnable. Son refus est illégal et peut être attaqué (Jurisprudence syndicat des ingénieurs conseils).",
    "theme": "Droit administratif"
  },
  {
    "question": "En Côte d'Ivoire, pour le contrôle de légalité des actes des collectivités territoriales (communes, régions), la tutelle a été remplacée par :",
    "options": ["A) Un contrôle a priori systématique exercé par le Conseil Constitutionnel.", "B) Un contrôle a posteriori exercé par le Préfet avec saisine du juge administratif (déféré préfectoral).", "C) L'absence totale de contrôle (libre administration absolue).", "D) Le contrôle financier de la BCEAO."],
    "answer": "B",
    "explanation": "La décentralisation a transformé la 'tutelle' (approbation préalable) en un 'contrôle de légalité a posteriori', où le Préfet défère l'acte au juge administratif s'il le juge illégal.",
    "theme": "Droit administratif"
  },
];
