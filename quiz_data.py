"""
Base de données de questions pour le quiz ENA
Organisée par thèmes selon les fiches de cours
"""

import random

# THÈME 1 : Langue française et vocabulaire
THEME_1 = [
    {
        "question": "Quel est le synonyme du mot « fugace » ?",
        "options": ["A) Permanent", "B) Éphémère", "C) Rapide", "D) Durable"],
        "answer": "B",
        "explanation": "« Fugace » signifie éphémère, qui dure peu de temps."
    },
    {
        "question": "Quel mot est l'antonyme de « prospère » ?",
        "options": ["A) Florissant", "B) Misérable", "C) Riche", "D) Opulent"],
        "answer": "B",
        "explanation": "« Misérable » est le contraire de « prospère » (qui réussit bien)."
    },
    {
        "question": "Complétez : « Il est arrivé …… faute ! »",
        "options": ["A) sans", "B) sang", "C) cent", "D) sens"],
        "answer": "A",
        "explanation": "« Sans » (sans faute) est la préposition correcte dans ce contexte."
    },
    {
        "question": "Quel est le genre du mot « armistice » ?",
        "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
        "answer": "B",
        "explanation": "« Armistice » est un nom masculin : un armistice."
    },
    {
        "question": "Quelle expression est correcte ?",
        "options": ["A) Je vous saurai gré", "B) Je vous saurais gré", "C) Je vous serais gré"],
        "answer": "A",
        "explanation": "L'expression correcte est « Je vous saurai gré » (futur simple)."
    },
    {
        "question": "Quel mot n'appartient pas à la même famille ?",
        "options": ["A) Terroir", "B) Territoire", "C) Terreur", "D) Terrain"],
        "answer": "C",
        "explanation": "« Terreur » vient du latin « terror » tandis que les autres viennent de « terra » (terre)."
    },
    {
        "question": "Trouvez le mot mal orthographié :",
        "options": ["A) Aréopage", "B) Anathème", "C) Apotheose", "D) Acrobate"],
        "answer": "C",
        "explanation": "L'orthographe correcte est « apothéose » avec un accent aigu."
    },
    {
        "question": "Quel mot est l'antonyme de « prolixe » ?",
        "options": ["A) Concis", "B) Verbeux", "C) Bavard", "D) Éloquent"],
        "answer": "A",
        "explanation": "« Prolixe » signifie bavard, son antonyme est « concis » (bref)."
    },
    {
        "question": "Quel pluriel est correct ?",
        "options": ["A) des cache-nez", "B) des cache-nezs", "C) des caches-nez"],
        "answer": "A",
        "explanation": "Les noms composés avec « cache » restent invariables : des cache-nez."
    },
    {
        "question": "Quelle phrase ne contient pas de pléonasme ?",
        "options": ["A) Monter en haut", "B) Prévoir à l'avance", "C) Répéter encore", "D) Examiner attentivement"],
        "answer": "D",
        "explanation": "« Examiner attentivement » n'est pas redondant, contrairement aux autres."
    },
    {
        "question": "Trouvez l'orthographe correcte :",
        "options": ["A) Dilemme", "B) Dilème", "C) Dilemne", "D) Dilenne"],
        "answer": "A",
        "explanation": "Le mot s'écrit « dilemme » avec deux m."
    },
    {
        "question": "Quel verbe se construit avec « de » ?",
        "options": ["A) Pallier", "B) Remédier", "C) Suppléer", "D) Obvier"],
        "answer": "B",
        "explanation": "On dit « remédier à » et non « remédier de ». « Pallier » se construit sans préposition."
    },
    {
        "question": "Quelle est la nature du mot « Épuisé » dans : « Épuisé, l'athlète abandonne » ?",
        "options": ["A) Adjectif qualificatif", "B) Participe passé épithète", "C) Participe passé en apposition"],
        "answer": "C",
        "explanation": "« Épuisé » est un participe passé mis en apposition (détaché par une virgule)."
    },
    {
        "question": "Quelle est la définition de « l'emphase » ?",
        "options": ["A) Un style exagéré", "B) La discrétion", "C) La clarté", "D) La concision"],
        "answer": "A",
        "explanation": "L'emphase est un ton, un style emphatique, exagéré et pompeux."
    },
    {
        "question": "Quel mot désigne une personne qui mange de tout ?",
        "options": ["A) Herbivore", "B) Carnivore", "C) Omnivore", "D) Frugivore"],
        "answer": "C",
        "explanation": "« Omnivore » désigne un être qui se nourrit de tout (végétaux et animaux)."
    },
    {
        "question": "Que signifie le sigle « ONU » ?",
        "options": ["A) Organisation des Nations Unies", "B) Office des Nations Unies", "C) Ordre des Nations Unies", "D) Organe des Nations Unies"],
        "answer": "A",
        "explanation": "ONU signifie Organisation des Nations Unies."
    },
    {
        "question": "Quel est l'antonyme de « appareiller » ?",
        "options": ["A) Accoster", "B) Fusionner", "C) Apprêter", "D) Partir"],
        "answer": "A",
        "explanation": "« Appareiller » signifie partir (pour un navire), son antonyme est « accoster » (arriver)."
    },
    {
        "question": "Une personne « dégingandée » est une personne :",
        "options": ["A) Élégante", "B) Ayant une démarche disloquée", "C) Timide", "D) Intelligente"],
        "answer": "B",
        "explanation": "« Dégingandée » qualifie une personne ayant des mouvements maladroits et une démarche disloquée."
    },
    {
        "question": "Quel dessert tire son nom d'une femme célèbre ?",
        "options": ["A) Tiramisu", "B) Pavlova", "C) Macaron", "D) Éclair"],
        "answer": "B",
        "explanation": "La Pavlova est nommée d'après la ballerine russe Anna Pavlova."
    },
    {
        "question": "Quel est le genre du mot « haltère » ?",
        "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
        "answer": "B",
        "explanation": "« Haltère » est masculin : un haltère."
    },
    {
        "question": "Quel mot n'appartient pas à la même famille que les autres ?",
        "options": ["A) Fable", "B) Fabuleux", "C) Affable", "D) Fabulation"],
        "answer": "C",
        "explanation": "« Affable » vient du latin « affabilis » (courtois), tandis que les autres viennent de « fabula » (récit)."
    },
    {
        "question": "Quelle relation n'existe pas (nature-adjectif) ?",
        "options": ["A) Eau-aquatique", "B) Église-ecclésiastique", "C) Humilité-modestie"],
        "answer": "C",
        "explanation": "« Humilité » et « modestie » sont deux noms, pas une relation nature-adjectif."
    },
    {
        "question": "Quel est l'antonyme du mot « truculent » ?",
        "options": ["A) Succulent", "B) Original", "C) Commun", "D) Savoureux"],
        "answer": "C",
        "explanation": "« Truculent » signifie haut en couleur, pittoresque ; son antonyme est « commun » (banal)."
    },
    {
        "question": "Trouvez l'intrus :",
        "options": ["A) Le Souverain Pontife", "B) Le Saint-Père", "C) La Bible", "D) Le Pape"],
        "answer": "C",
        "explanation": "Les trois autres désignent le Pape, la Bible est un livre sacré."
    },
    {
        "question": "Quel est l'antonyme du mot « pingre » ?",
        "options": ["A) Robuste", "B) Radin", "C) Généreux", "D) Avare"],
        "answer": "C",
        "explanation": "« Pingre » signifie avare, son antonyme est « généreux »."
    },
    {
        "question": "Quel pluriel est correct ?",
        "options": ["A) Des arcs-en-ciels", "B) Des passes-partout", "C) Des avant-premières", "D) Tous sont corrects"],
        "answer": "C",
        "explanation": "« Des avant-premières » est correct. « Arcs-en-ciel » et « passe-partout » restent invariables."
    },
    {
        "question": "Dans quelle phrase n'y a-t-il pas de pléonasme ?",
        "options": ["A) Le jeune lavandier travaille dans la laverie", "B) Pour la police, c'est un petit détail", "C) Ils vont tous se rencontrer ensemble"],
        "answer": "B",
        "explanation": "Cette phrase n'a pas de redondance, contrairement aux autres."
    },
    {
        "question": "Trouvez l'orthographe correcte :",
        "options": ["A) Pérégrination", "B) Pirégrination", "C) Perigrination", "D) Pérégrinassion"],
        "answer": "A",
        "explanation": "Le mot correct est « pérégrination » (voyage lointain)."
    },
    {
        "question": "Quel complément convient au verbe « luter » ?",
        "options": ["A) Une fissure", "B) Un vase", "C) Un trou", "D) Une fenêtre"],
        "answer": "B",
        "explanation": "« Luter » signifie boucher hermétiquement avec du lut (mastic). On lute un vase."
    },
    {
        "question": "Quel mot n'appartient pas à la même famille ?",
        "options": ["A) Ingénieur", "B) Géniteur", "C) Genèse", "D) Génération"],
        "answer": "A",
        "explanation": "« Ingénieur » vient de « ingenium » (talent), les autres de « genesis » (naissance)."
    },
    {
        "question": "Quelle est la définition de la « rhétorique » ?",
        "options": ["A) L'analyse de textes", "B) L'étude de la religion", "C) L'art du discours", "D) La grammaire"],
        "answer": "C",
        "explanation": "La rhétorique est l'art du discours et de l'éloquence."
    },
    {
        "question": "Quel mot désigne un amour excessif de soi-même ?",
        "options": ["A) Égoïsme", "B) Narcissisme", "C) Orgueil", "D) Vanité"],
        "answer": "B",
        "explanation": "Le narcissisme désigne un amour excessif de sa propre personne."
    },
    {
        "question": "Quel est le féminin de « empereur » ?",
        "options": ["A) Empereure", "B) Impératrice", "C) Empératrice", "D) Emperesse"],
        "answer": "B",
        "explanation": "Le féminin d'empereur est impératrice."
    },
    {
        "question": "Que signifie « ubiquité » ?",
        "options": ["A) Rapidité", "B) Capacité d'être partout", "C) Solitude", "D) Clarté"],
        "answer": "B",
        "explanation": "L'ubiquité est la capacité d'être présent partout à la fois."
    },
    {
        "question": "Quel mot désigne la peur des espaces clos ?",
        "options": ["A) Agoraphobie", "B) Claustrophobie", "C) Acrophobie", "D) Hydrophobie"],
        "answer": "B",
        "explanation": "La claustrophobie est la peur des espaces fermés."
    },
    {
        "question": "Complétez : « Il a fait cela de son propre …… »",
        "options": ["A) chef", "B) chèque", "C) chaire", "D) cher"],
        "answer": "A",
        "explanation": "L'expression est « de son propre chef » (de sa propre initiative)."
    },
    {
        "question": "Quel mot désigne l'art de bien manger ?",
        "options": ["A) Gastrologie", "B) Gastronomie", "C) Gastrosophie", "D) Gastromancie"],
        "answer": "B",
        "explanation": "La gastronomie est l'art de bien manger et de bien cuisiner."
    },
    {
        "question": "Quelle est l'origine du mot « bibliothèque » ?",
        "options": ["A) Latin", "B) Grec", "C) Arabe", "D) Sanskrit"],
        "answer": "B",
        "explanation": "« Bibliothèque » vient du grec « biblion » (livre) et « thêkê » (lieu de rangement)."
    },
    {
        "question": "Quel adjectif qualifie quelqu'un qui parle plusieurs langues ?",
        "options": ["A) Multilingue", "B) Polyglotte", "C) Bilingue", "D) Tous sont corrects"],
        "answer": "B",
        "explanation": "« Polyglotte » qualifie spécifiquement quelqu'un qui parle plusieurs langues."
    },
    {
        "question": "Que signifie le sigle « HLM » ?",
        "options": ["A) Habitation de longueur moyenne", "B) Habitation à loyer modéré", "C) Habitation de location moderne", "D) Hôtel de luxe moderne"],
        "answer": "B",
        "explanation": "HLM signifie Habitation à Loyer Modéré."
    },
    {
        "question": "Quel est le genre du mot « alvéole » ?",
        "options": ["A) Féminin", "B) Masculin", "C) Les deux sont acceptés"],
        "answer": "C",
        "explanation": "« Alvéole » est traditionnellement féminin mais le masculin est aussi admis par l'Académie française."
    },
    {
        "question": "Quelle figure de style consiste à dire le contraire de ce que l'on pense ?",
        "options": ["A) Litote", "B) Antiphrase", "C) Euphémisme", "D) Oxymore"],
        "answer": "B",
        "explanation": "L'antiphrase consiste à dire le contraire de ce que l'on veut faire comprendre, souvent avec ironie."
    },
    {
        "question": "Quelle figure de style associe deux termes contradictoires ?",
        "options": ["A) Métaphore", "B) Oxymore", "C) Antithèse", "D) Chiasme"],
        "answer": "B",
        "explanation": "L'oxymore unit deux termes de sens opposé. Ex : « un silence assourdissant »."
    },
    {
        "question": "Comment appelle-t-on un mot qui a une forme identique au masculin et au féminin ?",
        "options": ["A) Homonyme", "B) Épicène", "C) Polymorphe", "D) Androgyne"],
        "answer": "B",
        "explanation": "Un mot épicène a la même forme pour les deux genres. Ex : « un/une artiste »."
    },
    {
        "question": "Quel est l'adjectif verbal du verbe « naviguer » ?",
        "options": ["A) Naviguant", "B) Navigant", "C) Naviguent"],
        "answer": "B",
        "explanation": "L'adjectif verbal est « navigant » (variable) ; le participe présent est « naviguant » (invariable)."
    },
    {
        "question": "Quelle est l'orthographe correcte ?",
        "options": ["A) Echappatoire", "B) Échapattoire", "C) Échappatoire", "D) Échapatoire"],
        "answer": "C",
        "explanation": "Le mot s'écrit « échappatoire » avec deux p."
    },
    {
        "question": "Quel mode utilise-t-on après la conjonction « Bien que » ?",
        "options": ["A) L'indicatif", "B) Le subjonctif", "C) Le conditionnel", "D) L'impératif"],
        "answer": "B",
        "explanation": "« Bien que » est toujours suivi du subjonctif."
    },
    {
        "question": "Laquelle de ces phrases est correcte ?",
        "options": ["A) Après qu'il soit venu", "B) Après qu'il est venu", "C) Après qu'il ait venu"],
        "answer": "B",
        "explanation": "« Après que » est suivi de l'indicatif (contrairement à « avant que » qui prend le subjonctif)."
    },
    {
        "question": "Comment s'accorde l'adjectif de couleur « orange » ?",
        "options": ["A) Il s'accorde normalement", "B) Il reste invariable", "C) Il ne s'accorde qu'au pluriel"],
        "answer": "B",
        "explanation": "Les adjectifs de couleur issus de noms (orange, marron, crème…) sont invariables."
    },
    {
        "question": "Que signifie le sigle « PIB » ?",
        "options": ["A) Produit Intérieur Budgétaire", "B) Produit Intérieur Brut", "C) Plan d'Investissement Bancaire", "D) Programme d'Intervention Budgétaire"],
        "answer": "B",
        "explanation": "PIB signifie Produit Intérieur Brut, indicateur de la richesse d'un pays."
    },
    {
        "question": "Quelle est la bonne orthographe ?",
        "options": ["A) Aceuillir", "B) Accueillir", "C) Acceuillir", "D) Accueuillir"],
        "answer": "B",
        "explanation": "Le mot s'écrit « accueillir » (c-c-u-e-i-l-l-i-r)."
    },
    {
        "question": "Quelle figure de style consiste à remplacer un terme par une expression plus douce ?",
        "options": ["A) Hyperbole", "B) Litote", "C) Euphémisme", "D) Antiphrase"],
        "answer": "C",
        "explanation": "L'euphémisme adoucit une réalité. Ex : « il nous a quittés » pour « il est mort »."
    },
    {
        "question": "Quelle figure de style consiste à désigner un tout par une de ses parties ?",
        "options": ["A) Métonymie", "B) Synecdoque", "C) Périphrase", "D) Allégorie"],
        "answer": "B",
        "explanation": "La synecdoque prend la partie pour le tout. Ex : « les voiles » pour désigner les bateaux."
    },
    {
        "question": "Quelle est la définition d'une « périphrase » ?",
        "options": ["A) Dire le contraire de ce qu'on pense", "B) Utiliser plusieurs mots pour un seul", "C) Exagérer volontairement", "D) Comparer deux éléments"],
        "answer": "B",
        "explanation": "La périphrase remplace un mot par une expression. Ex : « l'astre du jour » pour « le soleil »."
    },
    {
        "question": "Quel est le genre du mot « tentacule » ?",
        "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
        "answer": "B",
        "explanation": "« Tentacule » est masculin : un tentacule."
    },
    {
        "question": "Quel est le genre du mot « obélisque » ?",
        "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
        "answer": "B",
        "explanation": "« Obélisque » est masculin : un obélisque."
    },
    {
        "question": "Que signifie l'expression « faire long feu » ?",
        "options": ["A) Durer longtemps", "B) Échouer, ne pas aboutir", "C) Provoquer un grand incendie"],
        "answer": "B",
        "explanation": "« Faire long feu » signifie ne pas aboutir, échouer (et non durer longtemps)."
    },
    {
        "question": "Quel mot désigne la peur du nombre 13 ?",
        "options": ["A) Arachnophobie", "B) Triskaïdékaphobie", "C) Nyctophobie", "D) Agoraphobie"],
        "answer": "B",
        "explanation": "La triskaïdékaphobie est la phobie du nombre 13."
    },
    {
        "question": "Comment s'écrit 80 en lettres ?",
        "options": ["A) Quatre-vingt", "B) Quatre-vingts", "C) Quatres-vingts", "D) Quatres-vingt"],
        "answer": "B",
        "explanation": "On écrit « quatre-vingts » avec un s quand il n'est pas suivi d'un autre nombre."
    },
    {
        "question": "« Il n'est pas mécontent » pour dire qu'il est ravi est une :",
        "options": ["A) Hyperbole", "B) Litote", "C) Antiphrase", "D) Métonymie"],
        "answer": "B",
        "explanation": "La litote dit moins pour suggérer plus (double négation atténuante)."
    },
    {
        "question": "« La diplomatie est le bras armé de la politique » est une :",
        "options": ["A) Métaphore", "B) Comparaison", "C) Métonymie", "D) Synecdoque"],
        "answer": "A",
        "explanation": "C'est une métaphore car il y a identification directe sans mot de comparaison."
    },
    {
        "question": "Quel mot désigne l'étude des noms propres ?",
        "options": ["A) Onomastique", "B) Toponymie", "C) Lexicologie", "D) Philologie"],
        "answer": "A",
        "explanation": "L'onomastique est l'étude des noms propres (personnes et lieux)."
    },
    {
        "question": "Quel est le contraire de « véhément » ?",
        "options": ["A) Violent", "B) Calme", "C) Passionné", "D) Fougueux"],
        "answer": "B",
        "explanation": "« Véhément » signifie ardent, impétueux ; son contraire est « calme »."
    },
    {
        "question": "Conjuguez : « Il faut que je …… ce travail avant demain. »",
        "options": ["A) finis", "B) finisse", "C) finirai", "D) finirais"],
        "answer": "B",
        "explanation": "Après « il faut que », on utilise le subjonctif présent : « que je finisse »."
    },
    {
        "question": "Quel est le genre du mot « pétale » ?",
        "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
        "answer": "B",
        "explanation": "« Pétale » est masculin : un pétale."
    },
    {
        "question": "Quel est le genre du mot « apostrophe » ?",
        "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
        "answer": "A",
        "explanation": "« Apostrophe » est féminin : une apostrophe."
    },
    {
        "question": "Que signifie l'expression « avoir maille à partir » ?",
        "options": ["A) Avoir beaucoup d'argent", "B) Avoir un différend avec quelqu'un", "C) Devoir partager", "D) Être pressé"],
        "answer": "B",
        "explanation": "« Avoir maille à partir » signifie avoir un conflit, un désaccord avec quelqu'un."
    },
    {
        "question": "Quel mot désigne un discours prononcé en l'honneur d'un défunt ?",
        "options": ["A) Panégyrique", "B) Oraison funèbre", "C) Réquisitoire", "D) Plaidoyer"],
        "answer": "B",
        "explanation": "L'oraison funèbre est un discours d'hommage prononcé lors des funérailles."
    },
    {
        "question": "Que signifie le sigle « BEPC » ?",
        "options": ["A) Brevet d'Études du Premier Cycle", "B) Bureau d'Études des Programmes Communs", "C) Bilan d'Évaluation Professionnelle Continu"],
        "answer": "A",
        "explanation": "BEPC signifie Brevet d'Études du Premier Cycle."
    },
    {
        "question": "Complétez : « Ces fleurs, je les ai …… »",
        "options": ["A) cueilli", "B) cueillie", "C) cueillies", "D) cueillis"],
        "answer": "C",
        "explanation": "Le participe passé s'accorde avec le COD « les » (= fleurs, féminin pluriel) placé avant."
    },
    {
        "question": "Quel verbe est correctement conjugué au passé simple ?",
        "options": ["A) Il prena", "B) Il prit", "C) Il prenna", "D) Il prendit"],
        "answer": "B",
        "explanation": "Le passé simple de « prendre » à la 3e personne est « il prit »."
    },
    {
        "question": "Quel mot désigne la science du droit ?",
        "options": ["A) Jurisprudence", "B) Juridiction", "C) Droit", "D) Jurisconsulte"],
        "answer": "A",
        "explanation": "La jurisprudence est l'ensemble des décisions de justice et la science du droit."
    },
    {
        "question": "Que signifie « apocryphe » ?",
        "options": ["A) Authentique", "B) D'authenticité douteuse", "C) Ancien", "D) Sacré"],
        "answer": "B",
        "explanation": "Un texte apocryphe est un écrit dont l'authenticité est contestée."
    },
    {
        "question": "Quel est le genre du mot « effluve » ?",
        "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
        "answer": "B",
        "explanation": "« Effluve » est masculin : un effluve."
    },
    {
        "question": "Que signifie « inique » ?",
        "options": ["A) Juste", "B) Injuste", "C) Unique", "D) Inutile"],
        "answer": "B",
        "explanation": "« Inique » signifie injuste, contraire à l'équité."
    },
    {
        "question": "Quel proverbe signifie qu'il faut être discret sur ses projets ?",
        "options": ["A) Pierre qui roule n'amasse pas mousse", "B) Pour vivre heureux, vivons cachés", "C) Qui sème le vent récolte la tempête"],
        "answer": "B",
        "explanation": "« Pour vivre heureux, vivons cachés » signifie qu'il faut rester discret."
    },
    {
        "question": "Que signifie « obtempérer » ?",
        "options": ["A) Refuser", "B) Obéir", "C) Hésiter", "D) Demander"],
        "answer": "B",
        "explanation": "« Obtempérer » signifie obéir, se soumettre à un ordre."
    },
    {
        "question": "Quel est le genre du mot « encaustique » ?",
        "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
        "answer": "A",
        "explanation": "« Encaustique » est féminin : une encaustique."
    },
    {
        "question": "Quelle est la bonne orthographe ?",
        "options": ["A) Imbécilité", "B) Imbécillité", "C) Imbésilité", "D) Imbescilité"],
        "answer": "A",
        "explanation": "Depuis la réforme de 1990, « imbécilité » s'écrit avec un seul l (anciennement deux)."
    },
    {
        "question": "Quelle est la bonne orthographe ?",
        "options": ["A) Acolade", "B) Accollade", "C) Accolade", "D) Acollade"],
        "answer": "C",
        "explanation": "Le mot s'écrit « accolade » avec deux c et un seul l."
    },
    {
        "question": "Que signifie « promulguer une loi » ?",
        "options": ["A) Proposer une loi", "B) Rendre une loi officielle et applicable", "C) Abroger une loi", "D) Modifier une loi"],
        "answer": "B",
        "explanation": "Promulguer une loi, c'est la rendre officiellement applicable par décret du président."
    },
    {
        "question": "Quel mot désigne un gouvernement dirigé par un petit nombre de personnes ?",
        "options": ["A) Démocratie", "B) Oligarchie", "C) Monarchie", "D) Théocratie"],
        "answer": "B",
        "explanation": "L'oligarchie est un régime où le pouvoir est entre les mains d'un petit groupe."
    },
    {
        "question": "Quel est le sens de « philantrope » ?",
        "options": ["A) Qui déteste l'humanité", "B) Qui aime l'humanité", "C) Qui collectionne les timbres", "D) Qui étudie les plantes"],
        "answer": "B",
        "explanation": "Un philanthrope (du grec philos = ami + anthropos = homme) aime l'humanité et agit pour son bien."
    },
    {
        "question": "Complétez : « Quoiqu'il …… riche, il reste modeste. »",
        "options": ["A) est", "B) soit", "C) serait", "D) sera"],
        "answer": "B",
        "explanation": "« Quoique » (= bien que) est suivi du subjonctif : « quoiqu'il soit »."
    },
    {
        "question": "Que signifie « abroger » ?",
        "options": ["A) Annuler une loi", "B) Publier une loi", "C) Modifier une loi", "D) Appliquer une loi"],
        "answer": "A",
        "explanation": "Abroger signifie supprimer, annuler une loi ou un décret."
    },
    {
        "question": "Quel est le contraire de « pléthorique » ?",
        "options": ["A) Abondant", "B) Insuffisant", "C) Excessif", "D) Immense"],
        "answer": "B",
        "explanation": "« Pléthorique » signifie en excès, surabondant ; son contraire est « insuffisant »."
    },
    {
        "question": "Que signifie « un arrêté » en droit administratif ?",
        "options": ["A) Une décision de justice", "B) Un acte administratif d'une autorité", "C) Un projet de loi", "D) Un discours officiel"],
        "answer": "B",
        "explanation": "Un arrêté est un acte administratif pris par un ministre, un préfet ou un maire."
    },
    {
        "question": "Quelle est la definition de la rhetorique ?",
        "options": ["A) L'etude d'une langue fondee sur l'analyse des textes", "B) L'etude de la religion", "C) L'art du discours et de l'eloquence", "D) La science des sons"],
        "answer": "C",
        "explanation": "La rhetorique est l'art du discours, de l'eloquence."
    },
    {
        "question": "Quel mot est mal orthographie ?",
        "options": ["A) echapattoire", "B) alveole", "C) anagramme", "D) peregrination"],
        "answer": "A",
        "explanation": "La bonne orthographe est ecchappatoire avec deux p."
    },
    {
        "question": "Quelle est la nature de Fatiguees dans : Fatiguees, les femmes se reposent ?",
        "options": ["A) Participe passe epithete", "B) Adjectif qualificatif epithete", "C) Participe passe mis en apposition", "D) Adjectif attribut"],
        "answer": "C",
        "explanation": "Fatiguees est un participe passe mis en apposition, detache par une virgule."
    },
    {
        "question": "Quel mot n'appartient pas a la meme famille que les autres ?",
        "options": ["A) ingenieur", "B) geniteur", "C) genese", "D) generation"],
        "answer": "A",
        "explanation": "Ingenieur vient du latin ingenium, tandis que les autres viennent de gignere (engendrer)."
    },
    {
        "question": "Choisissez le complement correct pour le verbe Luter :",
        "options": ["A) une fissure", "B) un vase", "C) un trou", "D) une bouteille"],
        "answer": "B",
        "explanation": "Luter signifie fermer hermetiquement avec du lut. On lute un vase, un creuset."
    },
    {
        "question": "Que signifie le sigle HLM ?",
        "options": ["A) Habitation de longueur moyenne", "B) Habitation a loyer modere", "C) Habitation de location moderne", "D) Habitation legere et modulable"],
        "answer": "B",
        "explanation": "HLM signifie Habitation a Loyer Modere, type de logement social."
    },
    {
        "question": "Quel terme designe un nom identique pour les deux genres ?",
        "options": ["A) Invariable", "B) Epicene", "C) Commun", "D) Neutre"],
        "answer": "B",
        "explanation": "Un nom epicene a la meme forme au masculin et au feminin (ex : enfant, artiste)."
    },
    {
        "question": "Comment ecrit-on correctement 80 en lettres ?",
        "options": ["A) Quatre-vingt", "B) Quatre-vingts", "C) Quatre vingt", "D) Quatre-vingts-s"],
        "answer": "B",
        "explanation": "Quatre-vingts s'ecrit avec un s final quand il n'est pas suivi d'un autre nombre."
    },
    {
        "question": "Quelle phrase est correcte apres la conjonction bien que ?",
        "options": ["A) Bien qu'il a termine son travail.", "B) Bien qu'il ait termine son travail.", "C) Bien qu'il termina son travail.", "D) Bien qu'il terminera son travail."],
        "answer": "B",
        "explanation": "Bien que impose le subjonctif : bien qu'il ait termine."
    },
    {
        "question": "Quelle phrase est correcte apres la conjonction apres que ?",
        "options": ["A) Apres qu'il soit venu", "B) Apres qu'il ait ete la", "C) Apres qu'il est venu", "D) Apres qu'il viendrait"],
        "answer": "C",
        "explanation": "Contrairement a avant que, apres que se construit avec l'indicatif."
    },
    {
        "question": "L'expression Il n'est pas mecontent pour dire qu'il est ravi est une :",
        "options": ["A) Hyperbole", "B) Litote", "C) Metaphore", "D) Euphemisme"],
        "answer": "B",
        "explanation": "La litote dit moins pour exprimer davantage : il n'est pas mecontent = il est tres content."
    },
    {
        "question": "La diplomatie est le bras arme de la politique est une :",
        "options": ["A) Metaphore", "B) Comparaison", "C) Metonymie", "D) Synecdoque"],
        "answer": "A",
        "explanation": "C'est une metaphore : assimilation directe sans terme comparatif."
    },
    {
        "question": "Comment s'accorde l'adjectif de couleur dans elle a achete des jupes orange ?",
        "options": ["A) orange (invariable)", "B) oranges", "C) orangee", "D) orangees"],
        "answer": "A",
        "explanation": "Les adjectifs de couleur issus d'un nom (orange, marron, kaki) sont invariables."
    },
    {
        "question": "Trouvez l'orthographe correcte :",
        "options": ["A) Peregrination", "B) Piregrination", "C) Perigrination", "D) Peregrination"],
        "answer": "A",
        "explanation": "Le mot correct est peregrination avec accent sur le premier e."
    },
    {
        "question": "Le mot navigant est l'adjectif verbal de naviguer. Il est :",
        "options": ["A) Variable", "B) Invariable", "C) Uniquement masculin", "D) Uniquement feminin"],
        "answer": "A",
        "explanation": "L'adjectif verbal navigant est variable : des personnels navigants."
    }
]

# THÈME 2 : Aptitude verbale - Phénomènes lexicaux
THEME_2 = [
    {
        "question": "Les mots « saut », « seau » et « sot » sont des :",
        "options": ["A) Paronymes", "B) Homographes", "C) Homophones", "D) Antonymes"],
        "answer": "C",
        "explanation": "Ces mots se prononcent de la même façon mais s'écrivent différemment : ce sont des homophones."
    },
    {
        "question": "La relation entre « rose » et « fleur » est une :",
        "options": ["A) Synonymie", "B) Hyponymie", "C) Antonymie", "D) Méronymie"],
        "answer": "B",
        "explanation": "« Rose » est un hyponyme de « fleur » (terme plus général, l'hyperonyme)."
    },
    {
        "question": "Le mot « Ressasser » est un exemple de :",
        "options": ["A) Anagramme", "B) Palindrome", "C) Homonyme", "D) Paronyme"],
        "answer": "B",
        "explanation": "« Ressasser » se lit dans les deux sens, c'est un palindrome."
    },
    {
        "question": "Les mots « éminent » et « imminent » sont des :",
        "options": ["A) Synonymes", "B) Homographes", "C) Paronymes", "D) Antonymes"],
        "answer": "C",
        "explanation": "Ces mots se ressemblent fortement mais ont des sens différents : ce sont des paronymes."
    },
    {
        "question": "Dans les expressions « avoir du cœur » et « le cœur bat », « cœur » illustre :",
        "options": ["A) Homonymie", "B) Polysémie", "C) Méronymie", "D) Synonymie"],
        "answer": "B",
        "explanation": "Un même mot avec plusieurs sens liés illustre la polysémie."
    },
    {
        "question": "« Marie » et « aimer » sont des :",
        "options": ["A) Palindromes", "B) Homophones", "C) Anagrammes", "D) Synonymes"],
        "answer": "C",
        "explanation": "Les mêmes lettres réorganisées forment des anagrammes."
    },
    {
        "question": "« Grand » et « petit » sont des :",
        "options": ["A) Antonymes", "B) Homonymes", "C) Hyponymes", "D) Paronymes"],
        "answer": "A",
        "explanation": "Ces mots ont des sens opposés : ce sont des antonymes."
    },
    {
        "question": "« Touche » est le méronyme de « clavier ». La méronymie décrit :",
        "options": ["A) Relation de sens proche", "B) Relation d'inclusion (partie/tout)", "C) Relation de ressemblance"],
        "answer": "B",
        "explanation": "La méronymie exprime une relation partie/tout."
    },
    {
        "question": "« Date » (jour) et « datte » (fruit) sont des :",
        "options": ["A) Mots polysémiques", "B) Homonymes", "C) Paronymes", "D) Synonymes"],
        "answer": "B",
        "explanation": "Ces mots se prononcent pareil mais n'ont aucun lien de sens : homonymes."
    },
    {
        "question": "Quel terme désigne des mots interchangeables avec un sens très proche ?",
        "options": ["A) Antonymes", "B) Synonymes", "C) Paronymes", "D) Homonymes"],
        "answer": "B",
        "explanation": "Les synonymes ont un sens identique ou très proche."
    },
    {
        "question": "L'expression « J'ai mille choses à faire » est un :",
        "options": ["A) Euphémisme", "B) Litote", "C) Hyperbole", "D) Métonymie"],
        "answer": "C",
        "explanation": "L'exagération volontaire est une hyperbole."
    },
    {
        "question": "Quel est l'hyperonyme de « voiture », « camion », « bus » ?",
        "options": ["A) Véhicule", "B) Transport", "C) Route", "D) Moteur"],
        "answer": "A",
        "explanation": "« Véhicule » est le terme général qui englobe ces mots."
    },
    {
        "question": "La répétition d'un mot en début de vers s'appelle :",
        "options": ["A) Anaphore", "B) Allitération", "C) Assonance", "D) Métaphore"],
        "answer": "A",
        "explanation": "L'anaphore est la répétition d'un mot ou groupe de mots en début de phrase."
    },
    {
        "question": "Les mots « poisson » et « poison » sont des :",
        "options": ["A) Homographes", "B) Paronymes", "C) Homophones", "D) Synonymes"],
        "answer": "B",
        "explanation": "Ils se ressemblent beaucoup mais ont des sens différents : paronymes."
    },
    {
        "question": "Quel terme désigne les mots cohyponymes de « animal » ?",
        "options": ["A) Arbre, plante", "B) Chat, chien, oiseau", "C) Maison, jardin", "D) Mammifère, reptile"],
        "answer": "B",
        "explanation": "Les cohyponymes sont des hyponymes d'un même hyperonyme (ici « animal »)."
    },
    {
        "question": "Les mots « ver », « verre » et « vert » sont des :",
        "options": ["A) Paronymes", "B) Homographes", "C) Homophones", "D) Synonymes"],
        "answer": "C",
        "explanation": "Ces mots se prononcent identiquement mais s'écrivent différemment : homophones."
    },
    {
        "question": "La relation entre « chien » et « animal » est une :",
        "options": ["A) Synonymie", "B) Hyponymie", "C) Antonymie", "D) Homonymie"],
        "answer": "B",
        "explanation": "« Chien » est un hyponyme (terme spécifique) de « animal » (terme général)."
    },
    {
        "question": "Le mot « Radar » est un exemple de :",
        "options": ["A) Anagramme", "B) Palindrome", "C) Homonyme", "D) Paronyme"],
        "answer": "B",
        "explanation": "« Radar » se lit identiquement dans les deux sens : c'est un palindrome."
    },
    {
        "question": "Quelle figure de style est une courte phrase qui se termine par une pointe satirique ?",
        "options": ["A) Métaphore", "B) Épigramme", "C) Hyperbole", "D) Allégorie"],
        "answer": "B",
        "explanation": "L'épigramme est une courte pièce satirique ou spirituelle."
    },
    {
        "question": "Les mots « cession » et « session » sont des :",
        "options": ["A) Synonymes", "B) Homographes", "C) Paronymes", "D) Homophones"],
        "answer": "C",
        "explanation": "Ces mots se ressemblent fortement mais ont des sens différents : paronymes."
    },
    {
        "question": "Dans « pied de la jambe » et « pied d'une montagne », « pied » illustre :",
        "options": ["A) Homonymie", "B) Polysémie", "C) Méronymie", "D) Paronymie"],
        "answer": "B",
        "explanation": "Un même mot avec plusieurs sens liés par l'origine : polysémie."
    },
    {
        "question": "« Imaginer » et « migraine » sont des :",
        "options": ["A) Palindromes", "B) Homophones", "C) Anagrammes", "D) Paronymes"],
        "answer": "C",
        "explanation": "Les lettres des deux mots peuvent être réorganisées : anagrammes."
    },
    {
        "question": "Dans « Sa bouche est une rose », quelle figure de style est utilisée ?",
        "options": ["A) Comparaison", "B) Métaphore", "C) Métonymie", "D) Hyperbole"],
        "answer": "B",
        "explanation": "Une métaphore établit une comparaison implicite sans utiliser « comme »."
    },
    {
        "question": "« Chaud » et « froid » sont des :",
        "options": ["A) Antonymes", "B) Homonymes", "C) Hyponymes", "D) Synonymes"],
        "answer": "A",
        "explanation": "Ces mots ont des sens opposés : ce sont des antonymes."
    },
    {
        "question": "« Roue » est le méronyme de « voiture ». La méronymie décrit :",
        "options": ["A) Relation de sens proche", "B) Relation d'inclusion (partie/tout)", "C) Relation de ressemblance"],
        "answer": "B",
        "explanation": "Un méronyme désigne une partie d'un tout (holonyme)."
    },
    {
        "question": "« Avocat » (fruit) et « avocat » (profession) sont des :",
        "options": ["A) Mots polysémiques", "B) Homonymes", "C) Paronymes", "D) Synonymes"],
        "answer": "B",
        "explanation": "Ces mots n'ont aucun lien de sens malgré leur forme identique : homonymes."
    },
    {
        "question": "Quel terme désigne des mots au sens identique ou très proche ?",
        "options": ["A) Antonymes", "B) Synonymes", "C) Paronymes", "D) Homophones"],
        "answer": "B",
        "explanation": "Les synonymes sont interchangeables dans un contexte donné."
    },
    {
        "question": "L'expression « Je meurs de faim » est un :",
        "options": ["A) Euphémisme", "B) Litote", "C) Hyperbole", "D) Oxymore"],
        "answer": "C",
        "explanation": "L'hyperbole est une exagération volontaire pour renforcer l'expression."
    },
    {
        "question": "Quel est l'hyperonyme de « chaise », « fauteuil », « tabouret » ?",
        "options": ["A) Meuble", "B) Bois", "C) Assise", "D) Salon"],
        "answer": "A",
        "explanation": "« Meuble » est le terme général qui englobe ces sièges."
    },
    {
        "question": "Comment appelle-t-on la répétition d'un mot en début de phrase ?",
        "options": ["A) Anaphore", "B) Allitération", "C) Assonance", "D) Épiphore"],
        "answer": "A",
        "explanation": "L'anaphore est la répétition d'un mot ou groupe en début de vers ou phrase."
    },
    {
        "question": "Les mots « pêcheur » et « pécheur » sont des :",
        "options": ["A) Homographes", "B) Homophones", "C) Synonymes", "D) Antonymes"],
        "answer": "B",
        "explanation": "Prononciation identique mais orthographe différente : homophones."
    },
    {
        "question": "Quel phénomène décrit des mots très ressemblants mais de sens différents ?",
        "options": ["A) Homonymie", "B) Synonymie", "C) Paronymie", "D) Polysémie"],
        "answer": "C",
        "explanation": "Les paronymes se ressemblent phonétiquement et graphiquement."
    },
    {
        "question": "« Engage le jeu que je le gagne » est un :",
        "options": ["A) Anagramme", "B) Palindrome", "C) Épigramme", "D) Calembour"],
        "answer": "B",
        "explanation": "Cette phrase se lit dans les deux sens : palindrome."
    },
    {
        "question": "L'hétéronymie concerne des mots de sens liés mais de radicaux différents ?",
        "options": ["A) Vrai", "B) Faux", "C) Partiellement vrai"],
        "answer": "A",
        "explanation": "Ex : « oncle/tante », « cheval/jument » - sens liés, radicaux différents."
    },
    {
        "question": "Quels mots sont cohyponymes de « fleur » ?",
        "options": ["A) Arbre, arbuste", "B) Rose, tulipe", "C) Bouquet, jardin", "D) Pétale, tige"],
        "answer": "B",
        "explanation": "Les cohyponymes partagent le même hyperonyme (ici « fleur »)."
    },
    {
        "question": "« Conte », « comte » et « compte » sont des :",
        "options": ["A) Paronymes", "B) Homophones", "C) Homographes", "D) Synonymes"],
        "answer": "B",
        "explanation": "Même prononciation, orthographes différentes : homophones."
    },
    {
        "question": "Dans « Il est mort de rire », quelle figure est utilisée ?",
        "options": ["A) Hyperbole", "B) Litote", "C) Euphémisme", "D) Antiphrase"],
        "answer": "A",
        "explanation": "Exagération volontaire pour renforcer l'expression : hyperbole."
    },
    {
        "question": "« Oncle » et « tante » illustrent :",
        "options": ["A) Synonymie", "B) Antonymie", "C) Hétéronymie", "D) Paronymie"],
        "answer": "C",
        "explanation": "Sens liés (famille) mais radicaux complètement différents : hétéronymie."
    },
    {
        "question": "L'allitération est la répétition de :",
        "options": ["A) Voyelles", "B) Consonnes", "C) Mots", "D) Syllabes"],
        "answer": "B",
        "explanation": "L'allitération répète des consonnes. L'assonance répète des voyelles."
    },
    {
        "question": "« Père » est l'holonyme de « main ». Vrai ou faux ?",
        "options": ["A) Vrai", "B) Faux"],
        "answer": "B",
        "explanation": "Faux. « Corps » serait l'holonyme de « main » (tout dont fait partie la main)."
    },
    {
        "question": "« Ce n'est pas mauvais » pour dire « c'est excellent » est une :",
        "options": ["A) Hyperbole", "B) Litote", "C) Métaphore", "D) Métonymie"],
        "answer": "B",
        "explanation": "La litote dit moins pour suggérer plus."
    },
    {
        "question": "« Nager » et « narguer » sont des :",
        "options": ["A) Synonymes", "B) Paronymes", "C) Homonymes", "D) Antonymes"],
        "answer": "B",
        "explanation": "Ressemblance phonétique et graphique forte : paronymes."
    },
    {
        "question": "Dans « Il pleut des cordes », quelle figure est utilisée ?",
        "options": ["A) Métaphore", "B) Comparaison", "C) Hyperbole", "D) Personnification"],
        "answer": "C",
        "explanation": "Exagération pour décrire une pluie forte : hyperbole."
    },
    {
        "question": "« Tête » (partie du corps) et « tête » (chef) illustrent :",
        "options": ["A) Homonymie", "B) Polysémie", "C) Paronymie", "D) Synonymie"],
        "answer": "B",
        "explanation": "Même mot, sens différents mais liés par l'origine : polysémie."
    },
    {
        "question": "L'assonance est la répétition de :",
        "options": ["A) Consonnes", "B) Voyelles", "C) Mots entiers", "D) Phrases"],
        "answer": "B",
        "explanation": "L'assonance est la répétition de voyelles. L'allitération répète des consonnes."
    },
    {
        "question": "« Boire un verre » est un exemple de :",
        "options": ["A) Métaphore", "B) Métonymie", "C) Synecdoque", "D) Litote"],
        "answer": "B",
        "explanation": "La métonymie remplace un mot par un autre lié logiquement. Ici le contenant (verre) pour le contenu (boisson)."
    },
    {
        "question": "Quel terme désigne un mot créé récemment dans une langue ?",
        "options": ["A) Archaïsme", "B) Néologisme", "C) Barbarisme", "D) Solécisme"],
        "answer": "B",
        "explanation": "Un néologisme est un mot nouveau ou récemment entré dans la langue."
    },
    {
        "question": "Quel terme désigne un mot tombé en désuétude, n'étant plus employé ?",
        "options": ["A) Néologisme", "B) Archaïsme", "C) Barbarisme", "D) Pléonasme"],
        "answer": "B",
        "explanation": "Un archaïsme est un mot ou une expression ancienne qui n'est plus en usage courant."
    },
    {
        "question": "Qu'est-ce qu'un barbarisme ?",
        "options": ["A) Un mot étranger", "B) Une faute de vocabulaire (mot déformé)", "C) Un mot ancien", "D) Un mot technique"],
        "answer": "B",
        "explanation": "Un barbarisme est l'emploi d'un mot inexistant ou déformé. Ex : « aéropage » au lieu d'« aréopage »."
    },
    {
        "question": "Qu'est-ce qu'un solécisme ?",
        "options": ["A) Une faute d'orthographe", "B) Une faute de syntaxe", "C) Un mot inventé", "D) Un mot étranger"],
        "answer": "B",
        "explanation": "Un solécisme est une faute de grammaire/syntaxe. Ex : « c'est à moi que je parle » au lieu de « c'est à moi qu'on parle »."
    },
    {
        "question": "« Le Roi Soleil » pour désigner Louis XIV est une :",
        "options": ["A) Métaphore", "B) Périphrase", "C) Antonomase", "D) Comparaison"],
        "answer": "C",
        "explanation": "L'antonomase utilise un nom propre comme nom commun ou inversement."
    },
    {
        "question": "L'épiphore est la répétition d'un mot ou groupe de mots :",
        "options": ["A) En début de phrase", "B) En fin de phrase", "C) Au milieu de phrase", "D) Partout dans la phrase"],
        "answer": "B",
        "explanation": "L'épiphore est le contraire de l'anaphore : elle répète un élément en fin de vers ou de phrase."
    },
    {
        "question": "« Blanc bonnet et bonnet blanc » est un exemple de :",
        "options": ["A) Chiasme", "B) Anaphore", "C) Palindrome", "D) Métonymie"],
        "answer": "A",
        "explanation": "Le chiasme est un croisement de termes selon le schéma AB-BA."
    },
    {
        "question": "« Courriel » est un néologisme français pour remplacer :",
        "options": ["A) Internet", "B) E-mail", "C) SMS", "D) Chat"],
        "answer": "B",
        "explanation": "« Courriel » est le néologisme officiel pour remplacer l'anglicisme « e-mail »."
    },
    {
        "question": "La catachrèse est :",
        "options": ["A) Une métaphore devenue si courante qu'on ne la remarque plus", "B) Un pléonasme", "C) Une exagération", "D) Une ironie"],
        "answer": "A",
        "explanation": "La catachrèse est une métaphore passée dans l'usage courant. Ex : « les pieds d'une table »."
    },
    {
        "question": "« Cheval » et « équestre » illustrent :",
        "options": ["A) Synonymie", "B) Un doublet étymologique", "C) Paronymie", "D) Homonymie"],
        "answer": "B",
        "explanation": "Le nom vient du latin populaire (caballus) et l'adjectif du latin savant (equester) : doublet étymologique."
    },
    {
        "question": "Quel est l'antonyme de « loquace » ?",
        "options": ["A) Bavard", "B) Taciturne", "C) Verbeux", "D) Prolixe"],
        "answer": "B",
        "explanation": "« Loquace » signifie bavard ; « taciturne » signifie silencieux, peu enclin à parler."
    },
    {
        "question": "Quel phénomène lexical lie « hôte » (celui qui reçoit) et « hôte » (celui qui est reçu) ?",
        "options": ["A) Polysémie", "B) Homonymie", "C) Énantiosémie", "D) Paronymie"],
        "answer": "C",
        "explanation": "L'énantiosémie (ou auto-antonymie) désigne un mot qui a deux sens opposés."
    },
    {
        "question": "« Clair-obscur » est un exemple de :",
        "options": ["A) Pléonasme", "B) Oxymore", "C) Antithèse", "D) Chiasme"],
        "answer": "B",
        "explanation": "L'oxymore associe deux termes contradictoires dans un même syntagme."
    },
    {
        "question": "Qu'est-ce qu'une antithèse ?",
        "options": ["A) Deux termes contradictoires accolés", "B) Opposition de deux idées dans une phrase", "C) Exagération volontaire", "D) Comparaison implicite"],
        "answer": "B",
        "explanation": "L'antithèse oppose deux idées dans une phrase ou un paragraphe, contrairement à l'oxymore qui accole les contraires."
    },
    {
        "question": "Quel procédé consiste à atténuer une vérité désagréable ?",
        "options": ["A) Hyperbole", "B) Litote", "C) Euphémisme", "D) Antiphrase"],
        "answer": "C",
        "explanation": "L'euphémisme adoucit une réalité brutale. Ex : « il s'est éteint » pour « il est mort »."
    },
    {
        "question": "« Frère » et « sœur » illustrent :",
        "options": ["A) Synonymie", "B) Antonymie", "C) Hétéronymie", "D) Paronymie"],
        "answer": "C",
        "explanation": "Sens liés (famille) mais radicaux totalement différents : c'est l'hétéronymie."
    },
    {
        "question": "Le mot « chrysanthème » est :",
        "options": ["A) Féminin", "B) Masculin", "C) Les deux"],
        "answer": "B",
        "explanation": "« Chrysanthème » est masculin : un chrysanthème."
    },
    {
        "question": "Qu'est-ce qu'une personnification ?",
        "options": ["A) Comparer deux éléments", "B) Attribuer des traits humains à un objet ou animal", "C) Exagérer un propos", "D) Dire le contraire de ce qu'on pense"],
        "answer": "B",
        "explanation": "La personnification donne des caractéristiques humaines à ce qui n'est pas humain. Ex : « le vent hurle »."
    },
    {
        "question": "Qu'est-ce qu'une gradation ?",
        "options": ["A) Répétition d'un mot", "B) Énumération de termes d'intensité croissante ou décroissante", "C) Opposition de deux idées", "D) Comparaison implicite"],
        "answer": "B",
        "explanation": "La gradation est une suite de mots d'intensité progressive. Ex : « je le vis, je rougis, je pâlis » (Racine)."
    },
    {
        "question": "Dans « La fourmi travaille sans relâche », quelle figure est utilisée ?",
        "options": ["A) Métaphore", "B) Personnification", "C) Comparaison", "D) Allégorie"],
        "answer": "B",
        "explanation": "Attribuer le travail (action humaine consciente) à un animal est une personnification."
    },
    {
        "question": "« Il prit son chapeau et la porte » est un exemple de :",
        "options": ["A) Pléonasme", "B) Zeugme", "C) Chiasme", "D) Oxymore"],
        "answer": "B",
        "explanation": "Le zeugme associe sur le même verbe des compléments de nature très différente (sens concret et figuré)."
    },
    {
        "question": "Qu'est-ce qu'un champ lexical ?",
        "options": ["A) L'ensemble des sens d'un mot", "B) L'ensemble des mots liés à un même thème", "C) Les mots de même famille", "D) Les mots de même racine"],
        "answer": "B",
        "explanation": "Le champ lexical regroupe les mots se rapportant à un même thème. Ex : école → élève, cours, tableau."
    },
    {
        "question": "Qu'est-ce qu'un champ sémantique ?",
        "options": ["A) Les mots d'un même thème", "B) L'ensemble des sens d'un seul mot", "C) Les mots de même sonorité", "D) Les synonymes d'un mot"],
        "answer": "B",
        "explanation": "Le champ sémantique est l'ensemble des significations d'un mot. Ex : « feuille » → papier, arbre, métal."
    },
    {
        "question": "Qu'est-ce qu'une prosopopée ?",
        "options": ["A) Faire parler un absent, un mort ou un objet", "B) Exagérer ses propos", "C) Répéter un mot pour insister", "D) Utiliser un mot pour un autre"],
        "answer": "A",
        "explanation": "La prosopopée fait parler un absent, un mort, un animal ou une abstraction."
    },
    {
        "question": "« Je suis venu, j'ai vu, j'ai vaincu » est un exemple de :",
        "options": ["A) Gradation", "B) Anaphore", "C) Les deux à la fois", "D) Allitération"],
        "answer": "C",
        "explanation": "C'est à la fois une anaphore (répétition de « je ») et une gradation (intensité croissante)."
    },
    {
        "question": "Quel est l'hyperonyme de « pomme », « banane », « mangue » ?",
        "options": ["A) Aliment", "B) Fruit", "C) Arbre", "D) Récolte"],
        "answer": "B",
        "explanation": "« Fruit » est le terme général englobant pomme, banane et mangue."
    },
    {
        "question": "« Prêt » et « près » sont des :",
        "options": ["A) Synonymes", "B) Homophones", "C) Paronymes", "D) Antonymes"],
        "answer": "B",
        "explanation": "Même prononciation mais sens et orthographe différents : homophones."
    },
    {
        "question": "« Éruption » et « irruption » sont des :",
        "options": ["A) Synonymes", "B) Homophones", "C) Paronymes", "D) Antonymes"],
        "answer": "C",
        "explanation": "Formes proches mais sens différents : éruption (sortie violente) vs irruption (entrée brusque)."
    },
    {
        "question": "« Page » (de livre) et « page » (jeune serviteur) sont des :",
        "options": ["A) Mots polysémiques", "B) Homonymes", "C) Paronymes", "D) Synonymes"],
        "answer": "B",
        "explanation": "Même forme mais origines et sens totalement différents : homonymes."
    },
    {
        "question": "Qu'est-ce qu'une allégorie ?",
        "options": ["A) Une comparaison abrégée", "B) Une métaphore filée représentant une idée abstraite", "C) Un pléonasme", "D) Une exagération"],
        "answer": "B",
        "explanation": "L'allégorie représente une idée abstraite par une image concrète prolongée. Ex : la Justice avec une balance."
    },
    {
        "question": "« Doigt » est le méronyme de :",
        "options": ["A) Ongle", "B) Main", "C) Bras", "D) Pied"],
        "answer": "B",
        "explanation": "Le doigt est une partie de la main : « doigt » (méronyme) → « main » (holonyme)."
    },
    {
        "question": "Qu'est-ce qu'une prétérition ?",
        "options": ["A) Parler d'une chose en disant qu'on n'en parlera pas", "B) Exagérer ses propos", "C) Dire le contraire", "D) Atténuer la réalité"],
        "answer": "A",
        "explanation": "La prétérition consiste à dire qu'on ne va pas parler de quelque chose tout en en parlant."
    },
    {
        "question": "« Été » et « hiver » sont des :",
        "options": ["A) Synonymes", "B) Antonymes", "C) Cohyponymes", "D) Homonymes"],
        "answer": "C",
        "explanation": "Ce sont des cohyponymes de l'hyperonyme « saison »."
    },
    {
        "question": "« Kayak » est un exemple de :",
        "options": ["A) Anagramme", "B) Palindrome", "C) Néologisme", "D) Emprunt"],
        "answer": "B",
        "explanation": "« Kayak » se lit dans les deux sens : c'est un palindrome."
    },
    {
        "question": "Dans « boire la tasse » (avaler de l'eau en nageant), quelle figure est utilisée ?",
        "options": ["A) Métaphore", "B) Métonymie", "C) Catachrèse", "D) Litote"],
        "answer": "C",
        "explanation": "C'est une catachrèse : une métaphore figée dans l'usage courant."
    },
    {
        "question": "Dans la phrase Sa bouche est une rose, quelle figure de style est utilisee ?",
        "options": ["A) Comparaison", "B) Metaphore", "C) Metonymie", "D) Synecdoque"],
        "answer": "B",
        "explanation": "C'est une metaphore : assimilation directe sans terme comparatif."
    },
    {
        "question": "Quelle figure de style se termine par une pointe satirique ?",
        "options": ["A) Metaphore", "B) Epigramme", "C) Hyperbole", "D) Anaphore"],
        "answer": "B",
        "explanation": "L'epigramme est une courte composition poetique a caractere satirique."
    },
    {
        "question": "avocat (fruit) et avocat (profession) sont des :",
        "options": ["A) Mots polysemiques", "B) Homonymes", "C) Paronymes", "D) Synonymes"],
        "answer": "B",
        "explanation": "Ce sont des homonymes parfaits, de sens et d'origines totalement differents."
    },
    {
        "question": "Les mots cession et session sont des :",
        "options": ["A) Synonymes", "B) Homographes", "C) Paronymes", "D) Antonymes"],
        "answer": "C",
        "explanation": "Ces mots se ressemblent fortement mais ont des sens differents : ce sont des paronymes."
    },
    {
        "question": "Dans pied de la jambe et pied d'une montagne, le mot pied illustre :",
        "options": ["A) Homonymie", "B) Polysemie", "C) Meronymie", "D) Antonymie"],
        "answer": "B",
        "explanation": "C'est de la polysemie : meme mot, sens differents mais lies par l'origine."
    },
    {
        "question": "L'expression Je meurs de faim est :",
        "options": ["A) Un euphemisme", "B) Une litote", "C) Une hyperbole", "D) Une metaphore"],
        "answer": "C",
        "explanation": "C'est une hyperbole : exageration deliberee pour produire un effet d'intensite."
    },
    {
        "question": "Les mots imaginer et migraine sont des :",
        "options": ["A) Palindromes", "B) Homophones", "C) Anagrammes", "D) Paronymes"],
        "answer": "C",
        "explanation": "On peut former migraine en reordonnant les lettres d'imaginer : ce sont des anagrammes."
    },
    {
        "question": "Quelle paire illustre l'heteronymie ?",
        "options": ["A) chaud / froid", "B) oncle / tante", "C) voiture / automobile", "D) fleur / rose"],
        "answer": "B",
        "explanation": "L'heteronymie concerne des mots a sens lies mais de radicaux differents : oncle/tante, cheval/jument."
    },
    {
        "question": "Quelle est la bonne definition de la meronymie ?",
        "options": ["A) Relation de sens proche", "B) Relation partie/tout", "C) Relation de ressemblance formelle", "D) Relation d'opposition"],
        "answer": "B",
        "explanation": "La meronymie decrit la relation d'inclusion partie/tout : roue est le meronyme de voiture."
    },
    {
        "question": "Quel terme designe les cohyponymes de animal ?",
        "options": ["A) Plante, arbre", "B) Chien, chat", "C) Jambe, bras", "D) Table, chaise"],
        "answer": "B",
        "explanation": "Chien et chat partagent le meme hyperonyme animal : ce sont des cohyponymes."
    },
    {
        "question": "Quel terme designe la relation entre main et doigt d un point de vue meronymique ?",
        "options": ["A) Doigt est l holonyme de main", "B) Main est l holonyme de doigt", "C) Main et doigt sont des cohyponymes", "D) Main est le meronyme de doigt"],
        "answer": "B",
        "explanation": "La main est le tout (holonyme) dont le doigt est une partie (meronyme)."
    },
    {
        "question": "Pi?ge : eminent et imminent sont-ils synonymes ?",
        "options": ["A) Oui ils signifient remarquable", "B) Non : eminent=remarquable imminent=qui va arriver tres bientot", "C) Oui ils expriment l urgence", "D) Non : eminent=lieu imminent=personne"],
        "answer": "B",
        "explanation": "Pi?ge de paronymie : eminent = qui se distingue ; imminent = sur le point de se produire."
    },
    {
        "question": "Quel phenomene illustre verre ver vers vert ?",
        "options": ["A) Paronymie", "B) Synonymie", "C) Homophonie", "D) Polysemie"],
        "answer": "C",
        "explanation": "Meme prononciation orthographes differentes : homophones."
    },
    {
        "question": "Quelle figure remplace une expression brusque par une formulation douce ?",
        "options": ["A) Litote", "B) Euphemisme", "C) Hyperbole", "D) Antiphrase"],
        "answer": "B",
        "explanation": "L euphemisme attenue la brutalite. Ex : il a quitte ce monde pour dire il est mort."
    },
    {
        "question": "Dans la phrase Il ne travaille pas mal quelle figure est utilisee ?",
        "options": ["A) Hyperbole", "B) Euphemisme", "C) Litote", "D) Metaphore"],
        "answer": "C",
        "explanation": "Litote : dire moins pour faire comprendre plus. Il ne travaille pas mal = il travaille bien."
    },
    {
        "question": "Quel terme designe la relation rose fleur en semantique ?",
        "options": ["A) Holonymie", "B) Hyponymie", "C) Synonymie", "D) Meronymie"],
        "answer": "B",
        "explanation": "Rose est un hyponyme de fleur : terme special inclus dans le terme general."
    },
    {
        "question": "Conjecture et conjoncture sont-ils des paronymes ?",
        "options": ["A) Non homonymes", "B) Oui : conjecture=supposition conjoncture=situation ?conomique", "C) Non antonymes", "D) Non synonymes"],
        "answer": "B",
        "explanation": "Conjecture/conjoncture : paronymes tres proches mais de sens tres differents."
    },
    {
        "question": "Quelle est la difference entre holonyme et hyperonyme ?",
        "options": ["A) Ce sont des synonymes", "B) Holonyme=tout dont le meronyme est une partie ; hyperonyme=terme general dont depend un hyponyme", "C) Hyperonyme=partie holonyme=ensemble", "D) Ces termes n existent pas"],
        "answer": "B",
        "explanation": "Holonyme/meronyme = relation partie-tout. Hyperonyme/hyponyme = inclusion semantique."
    },
    {
        "question": "Polysemie et homonymie sont-elles la meme chose ?",
        "options": ["A) Oui", "B) Non : polysemie=sens differents mais lies par etymologie ; homonymie=mots de formes identiques mais d origines differentes", "C) Oui dans les deux cas les sens sont totalement differents", "D) Non polysemie concerne verbes uniquement"],
        "answer": "B",
        "explanation": "Polysemie : tete corps/liste meme origine. Homonymie : avocat fruit/juriste origines distinctes."
    },
    {
        "question": "avocat fruit et avocat juriste illustrent quel phenomene ?",
        "options": ["A) Polysemie", "B) Homonymie car etymologies completement differentes", "C) Synonymie", "D) Paronymie"],
        "answer": "B",
        "explanation": "Avocat fruit vient du nahuatl ; avocat juriste du latin advocatus : homonymie."
    }
]

# THÈME 3 : Culture générale - Capitales, géographie et questions diverses
THEME_3 = [
    {
        "question": "Quelle est la capitale du Togo ?",
        "options": ["A) Porto-Novo", "B) Lomé", "C) Cotonou", "D) Ouagadougou"],
        "answer": "B",
        "explanation": "Lomé est la capitale du Togo."
    },
    {
        "question": "Quelle est la capitale du Burkina Faso ?",
        "options": ["A) Bamako", "B) Niamey", "C) Ouagadougou", "D) Dakar"],
        "answer": "C",
        "explanation": "Ouagadougou est la capitale du Burkina Faso."
    },
    {
        "question": "Dans quelle partie du corps se trouve le fémur ?",
        "options": ["A) Le bras", "B) La jambe", "C) Le dos", "D) Le pied"],
        "answer": "B",
        "explanation": "Le fémur est l'os de la cuisse, dans la jambe."
    },
    {
        "question": "Si je suis le gendre de Paul, qui est Paul pour moi ?",
        "options": ["A) Mon père", "B) Mon frère", "C) Mon beau-père", "D) Mon oncle"],
        "answer": "C",
        "explanation": "Le gendre est le mari de la fille, donc Paul est mon beau-père."
    },
    {
        "question": "Sur quoi portent principalement les recherches de Louis Pasteur ?",
        "options": ["A) L'électricité", "B) Les microbes et vaccins", "C) La mécanique", "D) L'astronomie"],
        "answer": "B",
        "explanation": "Louis Pasteur est célèbre pour ses travaux sur les microbes et la vaccination."
    },
    {
        "question": "Dans quel océan navigue-t-on au large de Tokyo ?",
        "options": ["A) Océan Atlantique", "B) Océan Pacifique", "C) Océan Indien", "D) Océan Arctique"],
        "answer": "B",
        "explanation": "Tokyo se situe sur la côte de l'océan Pacifique."
    },
    {
        "question": "Quel est le plus petit pays du monde ?",
        "options": ["A) Monaco", "B) Le Vatican", "C) Saint-Marin", "D) Le Liechtenstein"],
        "answer": "B",
        "explanation": "Le Vatican est le plus petit pays du monde avec 0,44 km²."
    },
    {
        "question": "Quel pays a pour monnaie le Cedi ?",
        "options": ["A) Le Ghana", "B) Le Nigeria", "C) Le Sénégal", "D) Le Togo"],
        "answer": "A",
        "explanation": "Le Cedi est la monnaie du Ghana."
    },
    {
        "question": "De quelle région Abengourou est-il le chef-lieu ?",
        "options": ["A) Le Moronou", "B) L'Indénié-Djuablin", "C) Le N'Zi", "D) Le Bounkani"],
        "answer": "B",
        "explanation": "Abengourou est le chef-lieu de la région de l'Indénié-Djuablin."
    },
    {
        "question": "De quel pays Nairobi est-il la capitale ?",
        "options": ["A) Tanzanie", "B) Kenya", "C) Ouganda", "D) Rwanda"],
        "answer": "B",
        "explanation": "Nairobi est la capitale du Kenya."
    },
    {
        "question": "Laquelle de ces inventions est la plus récente ?",
        "options": ["A) Le téléphone", "B) L'ampoule électrique", "C) Internet", "D) La radio"],
        "answer": "C",
        "explanation": "Internet a été développé dans les années 1960-1990, bien après les autres."
    },
    {
        "question": "Qui est l'auteur de l'œuvre « Le Petit Prince » ?",
        "options": ["A) Victor Hugo", "B) Antoine de Saint-Exupéry", "C) Albert Camus", "D) Jules Verne"],
        "answer": "B",
        "explanation": "Antoine de Saint-Exupéry a écrit « Le Petit Prince » en 1943."
    },
    {
        "question": "Quel est le cri du corbeau ?",
        "options": ["A) Croasse", "B) Coasse", "C) Siffle", "D) Piaule"],
        "answer": "A",
        "explanation": "Le corbeau croasse."
    },
    {
        "question": "Comment écrit-on 200 en lettres ?",
        "options": ["A) Deux-cent", "B) Deux-cents", "C) Deux cent", "D) Deux cents"],
        "answer": "D",
        "explanation": "« Deux cents » s'écrit avec « cents » au pluriel car suivi de rien."
    },
    {
        "question": "Quel mode suit la conjonction « Avant que » ?",
        "options": ["A) L'indicatif", "B) Le subjonctif", "C) Le conditionnel", "D) L'impératif"],
        "answer": "B",
        "explanation": "« Avant que » est toujours suivi du subjonctif."
    },
    {
        "question": "Quelle est la capitale du Cameroun ?",
        "options": ["A) Douala", "B) Yaoundé", "C) Libreville", "D) Bangui"],
        "answer": "B",
        "explanation": "Yaoundé est la capitale politique du Cameroun."
    },
    {
        "question": "Quelle est la capitale de la République démocratique du Congo ?",
        "options": ["A) Brazzaville", "B) Kinshasa", "C) Lubumbashi", "D) Goma"],
        "answer": "B",
        "explanation": "Kinshasa est la capitale de la RDC."
    },
    {
        "question": "Quelle est la capitale du Gabon ?",
        "options": ["A) Libreville", "B) Port-Gentil", "C) Franceville", "D) Oyem"],
        "answer": "A",
        "explanation": "Libreville est la capitale du Gabon."
    },
    {
        "question": "Quelle est la capitale du Tchad ?",
        "options": ["A) Abéché", "B) Moundou", "C) N'Djamena", "D) Sarh"],
        "answer": "C",
        "explanation": "N'Djamena est la capitale du Tchad."
    },
    {
        "question": "Quelle est la capitale du Ghana ?",
        "options": ["A) Kumasi", "B) Tamale", "C) Accra", "D) Tema"],
        "answer": "C",
        "explanation": "Accra est la capitale du Ghana."
    },
    {
        "question": "Quelle est la capitale du Bénin ?",
        "options": ["A) Cotonou", "B) Porto-Novo", "C) Parakou", "D) Abomey"],
        "answer": "B",
        "explanation": "Porto-Novo est la capitale administrative du Bénin, bien que Cotonou soit la capitale économique."
    },
    {
        "question": "Quelle est la capitale du Niger ?",
        "options": ["A) Niamey", "B) Zinder", "C) Maradi", "D) Agadez"],
        "answer": "A",
        "explanation": "Niamey est la capitale du Niger."
    },
    {
        "question": "Quelle est la capitale du Sénégal ?",
        "options": ["A) Saint-Louis", "B) Thiès", "C) Dakar", "D) Ziguinchor"],
        "answer": "C",
        "explanation": "Dakar est la capitale du Sénégal."
    },
    {
        "question": "Quelle est la capitale du Mali ?",
        "options": ["A) Bamako", "B) Tombouctou", "C) Sikasso", "D) Kayes"],
        "answer": "A",
        "explanation": "Bamako est la capitale du Mali."
    },
    {
        "question": "Quel est le plus long fleuve d'Afrique ?",
        "options": ["A) Congo", "B) Niger", "C) Nil", "D) Zambèze"],
        "answer": "C",
        "explanation": "Le Nil est le plus long fleuve d'Afrique (6 650 km)."
    },
    {
        "question": "Quel est le plus haut sommet d'Afrique ?",
        "options": ["A) Mont Kenya", "B) Kilimandjaro", "C) Mont Stanley", "D) Ras Dashan"],
        "answer": "B",
        "explanation": "Le Kilimandjaro en Tanzanie culmine à 5 895 m."
    },
    {
        "question": "Combien de pays partagent le bassin du fleuve Niger ?",
        "options": ["A) 5", "B) 7", "C) 10", "D) 12"],
        "answer": "C",
        "explanation": "Le fleuve Niger traverse ou borde 10 pays africains."
    },
    {
        "question": "Quel désert est le plus grand du monde ?",
        "options": ["A) Sahara", "B) Gobi", "C) Antarctique", "D) Kalahari"],
        "answer": "C",
        "explanation": "L'Antarctique est techniquement le plus grand désert (désert froid)."
    },
    {
        "question": "Quel est le plus grand désert chaud du monde ?",
        "options": ["A) Kalahari", "B) Sahara", "C) Gobi", "D) Arabie"],
        "answer": "B",
        "explanation": "Le Sahara est le plus grand désert chaud avec environ 9 millions de km²."
    },
    {
        "question": "Comment appelle-t-on le gendre pour les parents de l'épouse ?",
        "options": ["A) Beau-fils", "B) Beau-frère", "C) Neveu", "D) Cousin"],
        "answer": "A",
        "explanation": "Le gendre est le beau-fils pour les parents de l'épouse."
    },
    {
        "question": "Comment appelle-t-on la belle-fille pour les parents du mari ?",
        "options": ["A) Nièce", "B) Bru", "C) Belle-sœur", "D) Cousine"],
        "answer": "B",
        "explanation": "La bru est l'épouse du fils (belle-fille)."
    },
    {
        "question": "Quel est le nom scientifique de la rotule ?",
        "options": ["A) Tibia", "B) Fémur", "C) Patella", "D) Humérus"],
        "answer": "C",
        "explanation": "La rotule est appelée 'patella' en nomenclature anatomique."
    },
    {
        "question": "Quel est le nom scientifique du péroné ?",
        "options": ["A) Fibula", "B) Tibia", "C) Fémur", "D) Malléole"],
        "answer": "A",
        "explanation": "Le péroné est appelé 'fibula' en nomenclature anatomique."
    },
    {
        "question": "Quel est l'os le plus long du corps humain ?",
        "options": ["A) Humérus", "B) Tibia", "C) Fémur", "D) Radius"],
        "answer": "C",
        "explanation": "Le fémur (os de la cuisse) est l'os le plus long."
    },
    {
        "question": "Combien d'os compte le squelette humain adulte ?",
        "options": ["A) 186", "B) 206", "C) 226", "D) 246"],
        "answer": "B",
        "explanation": "Le squelette adulte compte 206 os."
    },
    {
        "question": "Qui a découvert la loi de la gravitation universelle ?",
        "options": ["A) Galilée", "B) Newton", "C) Einstein", "D) Kepler"],
        "answer": "B",
        "explanation": "Isaac Newton a formulé la loi de la gravitation en 1687."
    },
    {
        "question": "Qui a découvert les rayons X ?",
        "options": ["A) Marie Curie", "B) Wilhelm Röntgen", "C) Henri Becquerel", "D) Pierre Curie"],
        "answer": "B",
        "explanation": "Wilhelm Röntgen a découvert les rayons X en 1895."
    },
    {
        "question": "Qui a découvert la radioactivité ?",
        "options": ["A) Marie Curie", "B) Pierre Curie", "C) Henri Becquerel", "D) Ernest Rutherford"],
        "answer": "C",
        "explanation": "Henri Becquerel a découvert la radioactivité en 1896."
    },
    {
        "question": "Qui a développé la théorie de la relativité ?",
        "options": ["A) Newton", "B) Bohr", "C) Einstein", "D) Planck"],
        "answer": "C",
        "explanation": "Albert Einstein a publié la relativité restreinte en 1905 et générale en 1915."
    },
    {
        "question": "Quel scientifique a créé le premier vaccin contre la rage ?",
        "options": ["A) Edward Jenner", "B) Louis Pasteur", "C) Robert Koch", "D) Jonas Salk"],
        "answer": "B",
        "explanation": "Louis Pasteur a développé le vaccin contre la rage en 1885."
    },
    {
        "question": "Qui a inventé la première vaccination contre la variole ?",
        "options": ["A) Louis Pasteur", "B) Edward Jenner", "C) Robert Koch", "D) Alexander Fleming"],
        "answer": "B",
        "explanation": "Edward Jenner a développé le vaccin contre la variole en 1796."
    },
    {
        "question": "Quel est le cri du lion ?",
        "options": ["A) Rugit", "B) Brame", "C) Hurle", "D) Gronde"],
        "answer": "A",
        "explanation": "Le lion rugit."
    },
    {
        "question": "Quel est le cri de l'âne ?",
        "options": ["A) Hennit", "B) Brait", "C) Mugit", "D) Bêle"],
        "answer": "B",
        "explanation": "L'âne brait."
    },
    {
        "question": "Quel est le cri du cerf ?",
        "options": ["A) Brame", "B) Rugit", "C) Hurle", "D) Aboie"],
        "answer": "A",
        "explanation": "Le cerf brame."
    },
    {
        "question": "Quel est le cri de la grenouille ?",
        "options": ["A) Croasse", "B) Coasse", "C) Siffle", "D) Piaule"],
        "answer": "B",
        "explanation": "La grenouille coasse."
    },
    {
        "question": "En quelle année a eu lieu la chute du mur de Berlin ?",
        "options": ["A) 1987", "B) 1989", "C) 1991", "D) 1993"],
        "answer": "B",
        "explanation": "Le mur de Berlin est tombé le 9 novembre 1989."
    },
    {
        "question": "En quelle année a eu lieu la Révolution française ?",
        "options": ["A) 1789", "B) 1799", "C) 1804", "D) 1815"],
        "answer": "A",
        "explanation": "La Révolution française a commencé en 1789."
    },
    {
        "question": "Qui était le premier président des États-Unis ?",
        "options": ["A) Thomas Jefferson", "B) John Adams", "C) George Washington", "D) Benjamin Franklin"],
        "answer": "C",
        "explanation": "George Washington a été le premier président (1789-1797)."
    },
    {
        "question": "En quelle année Christophe Colomb a-t-il découvert l'Amérique ?",
        "options": ["A) 1482", "B) 1492", "C) 1502", "D) 1512"],
        "answer": "B",
        "explanation": "Christophe Colomb a découvert l'Amérique en 1492."
    },
    {
        "question": "Quelle est la capitale de l'Australie ?",
        "options": ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"],
        "answer": "C",
        "explanation": "Canberra est la capitale de l'Australie."
    },
    {
        "question": "Quelle est la capitale du Canada ?",
        "options": ["A) Toronto", "B) Montréal", "C) Vancouver", "D) Ottawa"],
        "answer": "D",
        "explanation": "Ottawa est la capitale du Canada."
    },
    {
        "question": "Quelle est la capitale du Brésil ?",
        "options": ["A) Rio de Janeiro", "B) São Paulo", "C) Brasília", "D) Salvador"],
        "answer": "C",
        "explanation": "Brasília est la capitale du Brésil depuis 1960."
    },
    {
        "question": "Quelle est la devise de l'Union européenne ?",
        "options": ["A) Dollar", "B) Livre", "C) Euro", "D) Franc"],
        "answer": "C",
        "explanation": "L'euro est la monnaie officielle de l'Union européenne."
    },
    {
        "question": "Quelle est la devise du Royaume-Uni ?",
        "options": ["A) Euro", "B) Livre sterling", "C) Dollar", "D) Couronne"],
        "answer": "B",
        "explanation": "La livre sterling (GBP) est la devise du Royaume-Uni."
    },
    {
        "question": "Quelle est la planète la plus proche du Soleil ?",
        "options": ["A) Vénus", "B) Mars", "C) Mercure", "D) Terre"],
        "answer": "C",
        "explanation": "Mercure est la planète la plus proche du Soleil."
    },
    {
        "question": "Combien de continents existe-t-il ?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "C",
        "explanation": "Il y a 7 continents : Afrique, Amérique du Nord, Amérique du Sud, Antarctique, Asie, Europe, Océanie."
    },
    {
        "question": "Quel pays a remporté la première Coupe du monde de football ?",
        "options": ["A) Brésil", "B) Argentine", "C) Uruguay", "D) Italie"],
        "answer": "C",
        "explanation": "L'Uruguay a remporté la première Coupe du monde en 1930."
    },
    {
        "question": "Qui a peint la Joconde ?",
        "options": ["A) Michel-Ange", "B) Léonard de Vinci", "C) Raphaël", "D) Donatello"],
        "answer": "B",
        "explanation": "Léonard de Vinci a peint la Joconde vers 1503-1506."
    },
    {
        "question": "Dans quel pays se trouve la tour Eiffel ?",
        "options": ["A) Italie", "B) Espagne", "C) France", "D) Belgique"],
        "answer": "C",
        "explanation": "La tour Eiffel se trouve à Paris, en France."
    },
    {
        "question": "Quel est le symbole chimique de l'or ?",
        "options": ["A) Or", "B) Au", "C) Ag", "D) Go"],
        "answer": "B",
        "explanation": "Le symbole de l'or est Au (du latin 'aurum')."
    },
    {
        "question": "Quel est le symbole chimique de l'argent ?",
        "options": ["A) Ar", "B) Ag", "C) Si", "D) Al"],
        "answer": "B",
        "explanation": "Le symbole de l'argent est Ag (du latin 'argentum')."
    },
    {
        "question": "Combien y a-t-il de secondes dans une heure ?",
        "options": ["A) 3 000", "B) 3 600", "C) 6 000", "D) 7 200"],
        "answer": "B",
        "explanation": "1 heure = 60 minutes × 60 secondes = 3 600 secondes."
    },
    {
        "question": "Quelle est la capitale de l'Éthiopie ?",
        "options": ["A) Nairobi", "B) Khartoum", "C) Addis-Abeba", "D) Kampala"],
        "answer": "C",
        "explanation": "Addis-Abeba est la capitale de l'Éthiopie."
    },
    {
        "question": "Quel océan borde l'ouest de l'Afrique ?",
        "options": ["A) Océan Indien", "B) Océan Atlantique", "C) Océan Pacifique", "D) Océan Arctique"],
        "answer": "B",
        "explanation": "L'océan Atlantique borde la côte ouest de l'Afrique."
    },
    {
        "question": "Combien de planètes compte le système solaire ?",
        "options": ["A) 7", "B) 8", "C) 9", "D) 10"],
        "answer": "B",
        "explanation": "Le système solaire compte 8 planètes depuis le déclassement de Pluton en 2006."
    },
    {
        "question": "Quel pays est surnommé le 'pays du Soleil Levant' ?",
        "options": ["A) Chine", "B) Corée du Sud", "C) Japon", "D) Thaïlande"],
        "answer": "C",
        "explanation": "Le Japon est traditionnellement appelé le 'pays du Soleil Levant'."
    },
    {
        "question": "Quelle est la langue officielle du Brésil ?",
        "options": ["A) Espagnol", "B) Portugais", "C) Français", "D) Anglais"],
        "answer": "B",
        "explanation": "Le portugais est la langue officielle du Brésil."
    },
    {
        "question": "Quel est le chef-lieu du District des Lacs en Côte d'Ivoire ?",
        "options": ["A) Yamoussoukro", "B) Dimbokro", "C) Bouaflé", "D) Toumodi"],
        "answer": "B",
        "explanation": "Dimbokro est le chef-lieu du District des Lacs."
    },
    {
        "question": "De quelle région Bouna est-il le chef-lieu ?",
        "options": ["A) Le Zanzan", "B) Le Bounkani", "C) Le Gontougo", "D) Le Tchologo"],
        "answer": "B",
        "explanation": "Bouna est le chef-lieu de la région du Bounkani."
    },
    {
        "question": "De quel pays Lilongwe est-il la capitale ?",
        "options": ["A) Zambie", "B) Zimbabwe", "C) Malawi", "D) Mozambique"],
        "answer": "C",
        "explanation": "Lilongwe est la capitale du Malawi."
    },
    {
        "question": "Quel nom d'oiseau utilise-t-on pour désigner un auteur de lettres anonymes ?",
        "options": ["A) Un aigle", "B) Un vautour", "C) Un corbeau", "D) Un faucon"],
        "answer": "C",
        "explanation": "On appelle « corbeau » la personne qui envoie des lettres anonymes malveillantes."
    },
    {
        "question": "Quelle traversée Louis Blériot a-t-il réussie en avion le 25 juillet 1909 ?",
        "options": ["A) L'Atlantique", "B) La Méditerranée", "C) La Manche", "D) Le Pacifique"],
        "answer": "C",
        "explanation": "Louis Blériot a été le premier à traverser la Manche en avion."
    },
    {
        "question": "Quel est le nom de la maladie qui entraîne un battement trop rapide du cœur ?",
        "options": ["A) Tachycardie", "B) Bradycardie", "C) Arythmie", "D) Angine"],
        "answer": "A",
        "explanation": "La tachycardie est l'accélération anormale du rythme cardiaque."
    },
    {
        "question": "Qui est l'auteur de l'œuvre « Le Malade imaginaire » ?",
        "options": ["A) Molière", "B) Racine", "C) Corneille", "D) Voltaire"],
        "answer": "A",
        "explanation": "Molière (Jean-Baptiste Poquelin) a écrit « Le Malade imaginaire » en 1673."
    },
    {
        "question": "Dans quelle ville siège l'Organisation des pays exportateurs de pétrole (OPEP) ?",
        "options": ["A) Genève", "B) New York", "C) Vienne", "D) Riyad"],
        "answer": "C",
        "explanation": "L'OPEP a son siège à Vienne, en Autriche."
    },
    {
        "question": "Lequel de ces personnages n'est PAS issu du roman « Les Misérables » ?",
        "options": ["A) Fleur de lys", "B) Jean Valjean", "C) Cosette", "D) Gavroche"],
        "answer": "A",
        "explanation": "Fleur de lys est un personnage de « Notre-Dame de Paris », pas des « Misérables »."
    },
    {
        "question": "En quelle année la Côte d'Ivoire a-t-elle accédé à l'indépendance ?",
        "options": ["A) 1958", "B) 1960", "C) 1962", "D) 1963"],
        "answer": "B",
        "explanation": "La Côte d'Ivoire a proclamé son indépendance le 7 août 1960."
    },
    {
        "question": "Qui est le premier président de la Côte d'Ivoire ?",
        "options": ["A) Henri Konan Bédié", "B) Laurent Gbagbo", "C) Félix Houphouët-Boigny", "D) Robert Guéï"],
        "answer": "C",
        "explanation": "Félix Houphouët-Boigny est le père fondateur et premier président (1960-1993)."
    },
    {
        "question": "Quelle est la capitale administrative de la Côte d'Ivoire ?",
        "options": ["A) Abidjan", "B) Bouaké", "C) Yamoussoukro", "D) San-Pédro"],
        "answer": "C",
        "explanation": "Yamoussoukro est la capitale politique et administrative depuis 1983."
    },
    {
        "question": "Qui a écrit « L'enfant noir » ?",
        "options": ["A) Léopold Sédar Senghor", "B) Camara Laye", "C) Ahmadou Kourouma", "D) Mongo Béti"],
        "answer": "B",
        "explanation": "Camara Laye, écrivain guinéen, a écrit « L'enfant noir » en 1953."
    },
    {
        "question": "Qui a écrit « Les Soleils des Indépendances » ?",
        "options": ["A) Bernard Dadié", "B) Ahmadou Kourouma", "C) Félix Tchicaya", "D) Birago Diop"],
        "answer": "B",
        "explanation": "Ahmadou Kourouma, écrivain ivoirien, a publié ce roman en 1968."
    },
    {
        "question": "Quel poète et homme politique sénégalais a cofondé le mouvement de la Négritude ?",
        "options": ["A) Aimé Césaire", "B) Léopold Sédar Senghor", "C) Léon-Gontran Damas", "D) Les trois ensemble"],
        "answer": "D",
        "explanation": "La Négritude a été fondée par Senghor, Césaire et Damas dans les années 1930."
    },
    {
        "question": "Quel pays africain est le plus grand producteur mondial de cacao ?",
        "options": ["A) Ghana", "B) Nigeria", "C) Côte d'Ivoire", "D) Cameroun"],
        "answer": "C",
        "explanation": "La Côte d'Ivoire est le premier producteur mondial de cacao."
    },
    {
        "question": "Quel pays a pour monnaie le Naira ?",
        "options": ["A) Ghana", "B) Nigeria", "C) Liberia", "D) Sierra Leone"],
        "answer": "B",
        "explanation": "Le Naira est la monnaie officielle du Nigeria."
    },
    {
        "question": "Quel pays a pour monnaie le Rand ?",
        "options": ["A) Kenya", "B) Éthiopie", "C) Afrique du Sud", "D) Tanzanie"],
        "answer": "C",
        "explanation": "Le Rand est la monnaie de l'Afrique du Sud."
    },
    {
        "question": "Quelle est la capitale du Rwanda ?",
        "options": ["A) Bujumbura", "B) Kigali", "C) Kampala", "D) Gitega"],
        "answer": "B",
        "explanation": "Kigali est la capitale du Rwanda."
    },
    {
        "question": "Quelle est la capitale de la Guinée-Bissau ?",
        "options": ["A) Conakry", "B) Bissau", "C) Freetown", "D) Banjul"],
        "answer": "B",
        "explanation": "Bissau est la capitale de la Guinée-Bissau."
    },
    {
        "question": "Quelle est la capitale de la Gambie ?",
        "options": ["A) Banjul", "B) Dakar", "C) Freetown", "D) Bissau"],
        "answer": "A",
        "explanation": "Banjul est la capitale de la Gambie."
    },
    {
        "question": "Quelle est la capitale du Liberia ?",
        "options": ["A) Freetown", "B) Accra", "C) Monrovia", "D) Abidjan"],
        "answer": "C",
        "explanation": "Monrovia est la capitale du Liberia."
    },
    {
        "question": "Quelle est la capitale de la Sierra Leone ?",
        "options": ["A) Monrovia", "B) Freetown", "C) Conakry", "D) Banjul"],
        "answer": "B",
        "explanation": "Freetown est la capitale de la Sierra Leone."
    },
    {
        "question": "Quelle est la capitale de la République Centrafricaine ?",
        "options": ["A) Bangui", "B) Yaoundé", "C) Libreville", "D) Malabo"],
        "answer": "A",
        "explanation": "Bangui est la capitale de la République Centrafricaine."
    },
    {
        "question": "Quel lac est le plus grand d'Afrique ?",
        "options": ["A) Lac Tanganyika", "B) Lac Tchad", "C) Lac Victoria", "D) Lac Malawi"],
        "answer": "C",
        "explanation": "Le lac Victoria est le plus grand lac d'Afrique (environ 68 000 km²)."
    },
    {
        "question": "Qui a écrit « Les Fleurs du Mal » ?",
        "options": ["A) Arthur Rimbaud", "B) Charles Baudelaire", "C) Paul Verlaine", "D) Stéphane Mallarmé"],
        "answer": "B",
        "explanation": "Charles Baudelaire a publié « Les Fleurs du Mal » en 1857."
    },
    {
        "question": "Qui a écrit « Candide » ?",
        "options": ["A) Montesquieu", "B) Rousseau", "C) Voltaire", "D) Diderot"],
        "answer": "C",
        "explanation": "Voltaire a écrit « Candide ou l'Optimisme » en 1759."
    },
    {
        "question": "Quel fleuve est le plus long d'Europe ?",
        "options": ["A) Danube", "B) Rhin", "C) Volga", "D) Loire"],
        "answer": "C",
        "explanation": "La Volga est le plus long fleuve d'Europe (environ 3 530 km)."
    },
    {
        "question": "En quelle année le Sénégal a-t-il accédé à l'indépendance ?",
        "options": ["A) 1958", "B) 1960", "C) 1962", "D) 1963"],
        "answer": "B",
        "explanation": "Le Sénégal a proclamé son indépendance le 4 avril 1960."
    },
    {
        "question": "Quelle est la principale base de lancement d'engins spatiaux aux États-Unis ?",
        "options": ["A) Houston", "B) Cap Canaveral", "C) Los Angeles", "D) Washington"],
        "answer": "B",
        "explanation": "Cap Canaveral (Kennedy Space Center) est la principale base spatiale américaine."
    },
    {
        "question": "Depuis 2020, quel territoire pourrait devenir le 51ème État des États-Unis ?",
        "options": ["A) Porto Rico", "B) Guam", "C) Washington D.C.", "D) Samoa américaines"],
        "answer": "A",
        "explanation": "Porto Rico a voté en 2020 en faveur de son intégration comme 51ème État."
    },
    {
        "question": "Combien de districts administratifs compte la Côte d'Ivoire ?",
        "options": ["A) 10", "B) 12", "C) 14", "D) 31"],
        "answer": "C",
        "explanation": "La Côte d'Ivoire compte 14 districts, dont 2 districts autonomes (Abidjan et Yamoussoukro)."
    },
    {
        "question": "Quel est le symbole chimique du fer ?",
        "options": ["A) Fr", "B) Fe", "C) Fa", "D) Fi"],
        "answer": "B",
        "explanation": "Le symbole du fer est Fe (du latin 'ferrum')."
    },
    {
        "question": "Quel est le cri de l'éléphant ?",
        "options": ["A) Barrit", "B) Rugit", "C) Mugit", "D) Brame"],
        "answer": "A",
        "explanation": "L'éléphant barrit."
    },
    {
        "question": "Quel est le cri du cheval ?",
        "options": ["A) Brait", "B) Mugit", "C) Hennit", "D) Bêle"],
        "answer": "C",
        "explanation": "Le cheval hennit."
    },
    {
        "question": "Quel est le plus grand fleuve de Côte d'Ivoire ?",
        "options": ["A) Le Sassandra", "B) Le Bandama", "C) Le Comoé", "D) Le Cavally"],
        "answer": "B",
        "explanation": "Le Bandama est le plus grand fleuve de Côte d'Ivoire (environ 1 050 km)."
    },
    {
        "question": "Quel organe détient le pouvoir législatif en Côte d'Ivoire ?",
        "options": ["A) Le gouvernement", "B) Le Sénat seul", "C) L'Assemblée nationale et le Sénat", "D) La Cour suprême"],
        "answer": "C",
        "explanation": "Le Parlement ivoirien est bicaméral : Assemblée nationale et Sénat."
    },
    {
        "question": "Quelle est la religion la plus pratiquée dans le monde ?",
        "options": ["A) L'islam", "B) Le christianisme", "C) L'hindouisme", "D) Le bouddhisme"],
        "answer": "B",
        "explanation": "Le christianisme est la religion la plus pratiquée avec environ 2,4 milliards de fidèles."
    },
    {
        "question": "Quel pays africain a accueilli la CAN 2023 ?",
        "options": ["A) Cameroun", "B) Côte d'Ivoire", "C) Sénégal", "D) Nigeria"],
        "answer": "B",
        "explanation": "La Côte d'Ivoire a accueilli la CAN 2023 (jouée en janvier-février 2024)."
    },
    {
        "question": "Qui a remporté la CAN 2023 ?",
        "options": ["A) Le Nigeria", "B) Le Sénégal", "C) La Côte d'Ivoire", "D) La RDC"],
        "answer": "C",
        "explanation": "La Côte d'Ivoire a remporté la CAN 2023 en battant le Nigeria en finale."
    },
    {
        "question": "Quel est le symbole chimique du cuivre ?",
        "options": ["A) Cr", "B) Cu", "C) Co", "D) Ci"],
        "answer": "B",
        "explanation": "Le symbole du cuivre est Cu (du latin 'cuprum')."
    },
    {
        "question": "Quel organe du corps humain produit l'insuline ?",
        "options": ["A) Le foie", "B) Le rein", "C) Le pancréas", "D) La rate"],
        "answer": "C",
        "explanation": "Le pancréas produit l'insuline qui régule le taux de glucose dans le sang."
    },
    {
        "question": "Quel est le plus grand pays d'Afrique en superficie ?",
        "options": ["A) RDC", "B) Soudan", "C) Algérie", "D) Libye"],
        "answer": "C",
        "explanation": "L'Algérie est le plus grand pays d'Afrique avec environ 2,38 millions de km²."
    },
    {
        "question": "Qui a écrit « Une vie de boy » ?",
        "options": ["A) Mongo Béti", "B) Ferdinand Oyono", "C) Camara Laye", "D) Cheikh Hamidou Kane"],
        "answer": "B",
        "explanation": "Ferdinand Oyono, écrivain camerounais, a publié « Une vie de boy » en 1956."
    },
    {
        "question": "Qui a écrit « L'aventure ambiguë » ?",
        "options": ["A) Birago Diop", "B) Cheikh Hamidou Kane", "C) Ousmane Sembène", "D) Léopold Sédar Senghor"],
        "answer": "B",
        "explanation": "Cheikh Hamidou Kane, écrivain sénégalais, a publié ce roman en 1961."
    },
    {
        "question": "Quelle est la capitale de la Guinée équatoriale ?",
        "options": ["A) Bata", "B) Malabo", "C) Libreville", "D) Douala"],
        "answer": "B",
        "explanation": "Malabo est la capitale de la Guinée équatoriale."
    },
    {
        "question": "Quelle est la capitale du Soudan ?",
        "options": ["A) Khartoum", "B) Djouba", "C) Le Caire", "D) Asmara"],
        "answer": "A",
        "explanation": "Khartoum est la capitale du Soudan."
    },
    {
        "question": "Quelle est la capitale du Soudan du Sud ?",
        "options": ["A) Khartoum", "B) Djouba", "C) Kampala", "D) Nairobi"],
        "answer": "B",
        "explanation": "Djouba (Juba) est la capitale du Soudan du Sud."
    },
    {
        "question": "Quel pays a pour monnaie le Yen ?",
        "options": ["A) Chine", "B) Corée du Sud", "C) Japon", "D) Thaïlande"],
        "answer": "C",
        "explanation": "Le Yen est la monnaie du Japon."
    },
    {
        "question": "Quel est le plus petit continent ?",
        "options": ["A) Antarctique", "B) Europe", "C) Océanie", "D) Amérique du Sud"],
        "answer": "C",
        "explanation": "L'Océanie est le plus petit continent."
    },
    {
        "question": "Combien d'arrondissements compte la ville d'Abidjan ?",
        "options": ["A) 10", "B) 13", "C) 15", "D) 20"],
        "answer": "A",
        "explanation": "La ville d'Abidjan compte 10 communes (arrondissements)."
    },
    {
        "question": "Quel est le sigle de la monnaie utilisée en Côte d'Ivoire ?",
        "options": ["A) CDF", "B) XOF", "C) EUR", "D) GHS"],
        "answer": "B",
        "explanation": "XOF est le code ISO du franc CFA de l'Afrique de l'Ouest (BCEAO)."
    },
    {
        "question": "Quel savant grec est considéré comme le père de la médecine ?",
        "options": ["A) Aristote", "B) Hippocrate", "C) Galien", "D) Archimède"],
        "answer": "B",
        "explanation": "Hippocrate (460-370 av. J.-C.) est considéré comme le père de la médecine."
    },
    {
        "question": "Quel pays africain n'a jamais été colonisé ?",
        "options": ["A) Ghana", "B) Liberia", "C) Éthiopie", "D) Liberia et Éthiopie"],
        "answer": "D",
        "explanation": "L'Éthiopie et le Liberia sont les deux seuls pays africains n'ayant jamais été colonisés."
    },
    {
        "question": "Qui a découvert la pénicilline ?",
        "options": ["A) Louis Pasteur", "B) Alexander Fleming", "C) Robert Koch", "D) Jonas Salk"],
        "answer": "B",
        "explanation": "Alexander Fleming a découvert la pénicilline (antibiotique) en 1928."
    },
    {
        "question": "Quel est le fleuve le plus long du monde ?",
        "options": ["A) Amazone", "B) Nil", "C) Mississippi", "D) Yangzi Jiang"],
        "answer": "B",
        "explanation": "Le Nil est le fleuve le plus long du monde avec environ 6 650 km."
    },
    {
        "question": "En quelle année les attentats du 11 septembre ont-ils eu lieu ?",
        "options": ["A) 2000", "B) 2001", "C) 2002", "D) 2003"],
        "answer": "B",
        "explanation": "Les attentats du World Trade Center ont eu lieu le 11 septembre 2001."
    },
    {
        "question": "Quel philosophe grec est l'auteur de « La République » ?",
        "options": ["A) Aristote", "B) Socrate", "C) Platon", "D) Épicure"],
        "answer": "C",
        "explanation": "Platon a écrit « La République » où il développe sa vision de la cité idéale."
    },
    {
        "question": "Quelle est la capitale de Madagascar ?",
        "options": ["A) Moroni", "B) Antananarivo", "C) Maputo", "D) Victoria"],
        "answer": "B",
        "explanation": "Antananarivo est la capitale de Madagascar."
    },
    {
        "question": "Quel organe du corps humain filtre le sang ?",
        "options": ["A) Le cœur", "B) Le foie", "C) Le rein", "D) Le poumon"],
        "answer": "C",
        "explanation": "Les reins filtrent le sang pour éliminer les déchets sous forme d'urine."
    },
    {
        "question": "Dans quelle articulation du corps se situe la rotule ?",
        "options": ["A) La hanche", "B) L'epaule", "C) Le genou", "D) Le coude"],
        "answer": "C",
        "explanation": "La rotule est l'os qui protege l'articulation du genou."
    },
    {
        "question": "Si je suis la bru de Michelle, qui est Michelle pour moi ?",
        "options": ["A) Ma soeur", "B) Ma tante", "C) Ma belle-mere", "D) Ma belle-soeur"],
        "answer": "C",
        "explanation": "La bru est l'epouse du fils : Michelle est donc la belle-mere."
    },
    {
        "question": "Quel nom d'oiseau designe un auteur de lettres anonymes ?",
        "options": ["A) Aigle", "B) Perroquet", "C) Corbeau", "D) Hibou"],
        "answer": "C",
        "explanation": "Un corbeau est familierement une personne qui envoie des lettres anonymes."
    },
    {
        "question": "Quelle est la capitale du Maroc ?",
        "options": ["A) Casablanca", "B) Marrakech", "C) Fes", "D) Rabat"],
        "answer": "D",
        "explanation": "Rabat est la capitale officielle du Maroc."
    },
    {
        "question": "Quelle est la capitale de la C?te d'Ivoire ?",
        "options": ["A) Abidjan", "B) Yamoussoukro", "C) Bouake", "D) San-Pedro"],
        "answer": "B",
        "explanation": "Yamoussoukro est la capitale politique de la C?te d'Ivoire depuis 1983."
    },
    {
        "question": "Quel est le plus grand pays du monde ?",
        "options": ["A) La Russie", "B) Le Canada", "C) Les ?tats-Unis", "D) La Chine"],
        "answer": "A",
        "explanation": "La Russie est le plus grand pays du monde avec environ 17,1 millions de km2."
    },
    {
        "question": "Quel pays a pour monnaie le Shekel ?",
        "options": ["A) Israel", "B) Jordanie", "C) Liban", "D) Syrie"],
        "answer": "A",
        "explanation": "Le nouveau Shekel est la monnaie officielle d'Israel."
    },
    {
        "question": "Quelle traversee Louis Bleriot a-t-il reussie en avion le 25 juillet 1909 ?",
        "options": ["A) La Mediterranee", "B) La Manche", "C) Le Rhin", "D) Le detroit de Gibraltar"],
        "answer": "B",
        "explanation": "Louis Bleriot a traverse la Manche en avion pour la premiere fois le 25 juillet 1909."
    },
    {
        "question": "Quel est le nom de la maladie qui entraine un battement trop rapide du coeur ?",
        "options": ["A) Tachycardie", "B) Bradycardie", "C) Arythmie", "D) Angine"],
        "answer": "A",
        "explanation": "La tachycardie est une frequence cardiaque anormalement elevee (plus de 100 battements par minute)."
    },
    {
        "question": "Dans quelle ville siege l'OPEP ?",
        "options": ["A) Ryad", "B) Dubai", "C) Vienne", "D) Geneve"],
        "answer": "C",
        "explanation": "Le siege de l'OPEP est a Vienne, en Autriche, depuis 1965."
    },
    {
        "question": "Qui est l'auteur de Le malade imaginaire ?",
        "options": ["A) Moliere", "B) Racine", "C) Corneille", "D) La Fontaine"],
        "answer": "A",
        "explanation": "Le malade imaginaire est une comedie-ballet de Moliere (1673)."
    },
    {
        "question": "De quelle region Bouna est-il le chef-lieu ?",
        "options": ["A) Le Poro", "B) Le Bounkani", "C) Le Hambol", "D) Le Moronou"],
        "answer": "B",
        "explanation": "Bouna est le chef-lieu de la region du Bounkani dans le Nord-Est de la C?te d'Ivoire."
    },
    {
        "question": "Quelle est la capitale de l'Egypte ?",
        "options": ["A) Alexandrie", "B) Louxor", "C) Le Caire", "D) Assouan"],
        "answer": "C",
        "explanation": "Le Caire est la capitale de l'Egypte et la ville la plus peuplee d'Afrique."
    },
    {
        "question": "Sur quoi reposent principalement les travaux de Pierre et Marie Curie ?",
        "options": ["A) La physique quantique", "B) La theorie de la relativite", "C) La radioactivite", "D) L'electromagnetisme"],
        "answer": "C",
        "explanation": "Pierre et Marie Curie ont consacre leurs recherches a la radioactivite."
    },
    {
        "question": "Dans quel ocean navigue-t-on au large de New York ?",
        "options": ["A) Oceean Indien", "B) Ocean Atlantique", "C) Ocean Pacifique", "D) Ocean Arctique"],
        "answer": "B",
        "explanation": "New York est situee sur la cote est des ?tats-Unis, au bord de l'Ocean Atlantique."
    }
]

# THÈME 4 : Organisations internationales
THEME_4 = [
    {
        "question": "En quelle année l'ONU a-t-elle été officiellement créée ?",
        "options": ["A) 1945", "B) 1946", "C) 1944", "D) 1950"],
        "answer": "A",
        "explanation": "L'ONU a été créée le 24 octobre 1945."
    },
    {
        "question": "Combien de membres permanents compte le Conseil de Sécurité de l'ONU ?",
        "options": ["A) 3", "B) 5", "C) 7", "D) 10"],
        "answer": "B",
        "explanation": "Il y a 5 membres permanents : USA, Russie, Chine, France, Royaume-Uni."
    },
    {
        "question": "Où siège la Cour internationale de Justice ?",
        "options": ["A) New York", "B) La Haye", "C) Genève", "D) Paris"],
        "answer": "B",
        "explanation": "La CIJ siège à La Haye aux Pays-Bas."
    },
    {
        "question": "Quel Secrétaire Général de l'ONU a obtenu le prix Nobel de la paix en 2001 ?",
        "options": ["A) Ban Ki-moon", "B) Kofi Annan", "C) Boutros Boutros-Ghali", "D) António Guterres"],
        "answer": "B",
        "explanation": "Kofi Annan, Secrétaire Général ghanéen, a reçu le prix Nobel en 2001."
    },
    {
        "question": "En quelle année a été créée l'OTAN ?",
        "options": ["A) 1949", "B) 1945", "C) 1955", "D) 1960"],
        "answer": "A",
        "explanation": "L'OTAN a été créée le 4 avril 1949."
    },
    {
        "question": "Où siège le Parlement européen ?",
        "options": ["A) Bruxelles", "B) Luxembourg", "C) Strasbourg", "D) Paris"],
        "answer": "C",
        "explanation": "Le Parlement européen siège principalement à Strasbourg."
    },
    {
        "question": "Combien d'États membres compte l'Union Européenne actuellement ?",
        "options": ["A) 25", "B) 27", "C) 28", "D) 30"],
        "answer": "B",
        "explanation": "L'UE compte 27 États membres depuis le Brexit."
    },
    {
        "question": "Le Mercosur est une organisation de quel continent ?",
        "options": ["A) Afrique", "B) Asie", "C) Amérique du Sud", "D) Europe"],
        "answer": "C",
        "explanation": "Le Mercosur est une organisation sud-américaine."
    },
    {
        "question": "Où se trouve le siège de l'Union africaine ?",
        "options": ["A) Accra", "B) Addis-Abeba", "C) Abidjan", "D) Le Caire"],
        "answer": "B",
        "explanation": "Le siège de l'UA est à Addis-Abeba en Éthiopie."
    },
    {
        "question": "L'Union africaine a succédé à quelle organisation ?",
        "options": ["A) ONU", "B) OUA", "C) CEDEAO", "D) UEMOA"],
        "answer": "B",
        "explanation": "L'UA a remplacé l'Organisation de l'Unité Africaine (OUA) en 2002."
    },
    {
        "question": "En quelle année a été créée la CEDEAO ?",
        "options": ["A) 1970", "B) 1975", "C) 1980", "D) 1985"],
        "answer": "B",
        "explanation": "La CEDEAO a été créée en 1975."
    },
    {
        "question": "Combien d'États membres compte actuellement l'UEMOA ?",
        "options": ["A) 6", "B) 8", "C) 10", "D) 12"],
        "answer": "B",
        "explanation": "L'UEMOA compte 8 États membres."
    },
    {
        "question": "Où se trouve le siège de l'UEMOA ?",
        "options": ["A) Dakar", "B) Ouagadougou", "C) Abidjan", "D) Lomé"],
        "answer": "B",
        "explanation": "Le siège de l'UEMOA est à Ouagadougou au Burkina Faso."
    },
    {
        "question": "Où se trouve le siège de la Banque africaine de développement ?",
        "options": ["A) Abidjan", "B) Lagos", "C) Accra", "D) Dakar"],
        "answer": "A",
        "explanation": "La BAD a son siège à Abidjan en Côte d'Ivoire."
    },
    {
        "question": "Quel organisme a reçu le prix Nobel de la Paix en 2012 ?",
        "options": ["A) L'ONU", "B) L'Union Européenne", "C) La CEDEAO", "D) L'UA"],
        "answer": "B",
        "explanation": "L'Union Européenne a reçu le prix Nobel de la Paix en 2012."
    },
    {
        "question": "Combien de membres compte l'Assemblée générale de l'ONU ?",
        "options": ["A) 173", "B) 183", "C) 193", "D) 203"],
        "answer": "C",
        "explanation": "L'Assemblée générale compte 193 États membres."
    },
    {
        "question": "Où se trouve le siège principal de l'ONU ?",
        "options": ["A) Washington", "B) Genève", "C) New York", "D) Paris"],
        "answer": "C",
        "explanation": "Le siège principal de l'ONU est à New York."
    },
    {
        "question": "Qui est le Secrétaire Général actuel de l'ONU ?",
        "options": ["A) Ban Ki-moon", "B) Kofi Annan", "C) António Guterres", "D) Boutros Boutros-Ghali"],
        "answer": "C",
        "explanation": "António Guterres est Secrétaire Général depuis 2017."
    },
    {
        "question": "Quel organe de l'ONU peut imposer des sanctions ?",
        "options": ["A) L'Assemblée générale", "B) Le Conseil de Sécurité", "C) La CIJ", "D) Le Secrétariat"],
        "answer": "B",
        "explanation": "Le Conseil de Sécurité a le pouvoir d'imposer des sanctions."
    },
    {
        "question": "Combien de membres non permanents siègent au Conseil de Sécurité ?",
        "options": ["A) 5", "B) 8", "C) 10", "D) 15"],
        "answer": "C",
        "explanation": "Il y a 10 membres non permanents élus pour 2 ans."
    },
    {
        "question": "Quelle est la durée du mandat des membres non permanents du Conseil de Sécurité ?",
        "options": ["A) 1 an", "B) 2 ans", "C) 3 ans", "D) 4 ans"],
        "answer": "B",
        "explanation": "Les membres non permanents sont élus pour un mandat de 2 ans."
    },
    {
        "question": "Quel est le siège de l'Organisation mondiale de la Santé (OMS) ?",
        "options": ["A) Paris", "B) Genève", "C) New York", "D) Londres"],
        "answer": "B",
        "explanation": "L'OMS a son siège à Genève en Suisse."
    },
    {
        "question": "En quelle année a été créée l'OUA (Organisation de l'Unité Africaine) ?",
        "options": ["A) 1960", "B) 1963", "C) 1965", "D) 1970"],
        "answer": "B",
        "explanation": "L'OUA a été créée le 25 mai 1963 à Addis-Abeba."
    },
    {
        "question": "En quelle année l'UA a-t-elle remplacé l'OUA ?",
        "options": ["A) 1999", "B) 2000", "C) 2001", "D) 2002"],
        "answer": "D",
        "explanation": "L'Union africaine a été créée en 2002."
    },
    {
        "question": "Combien d'États membres compte l'Union africaine ?",
        "options": ["A) 50", "B) 53", "C) 54", "D) 55"],
        "answer": "D",
        "explanation": "L'UA compte 55 États membres africains."
    },
    {
        "question": "Quel pays africain n'est pas membre de l'Union africaine ?",
        "options": ["A) Somalie", "B) Soudan du Sud", "C) Maroc (suspendu)", "D) Aucun, tous sont membres"],
        "answer": "D",
        "explanation": "Tous les 55 pays africains sont membres de l'UA."
    },
    {
        "question": "Où se trouve le siège de l'OTAN ?",
        "options": ["A) Washington", "B) Bruxelles", "C) Paris", "D) Londres"],
        "answer": "B",
        "explanation": "Le siège de l'OTAN est à Bruxelles en Belgique."
    },
    {
        "question": "Combien de pays sont membres de l'OTAN actuellement ?",
        "options": ["A) 28", "B) 30", "C) 31", "D) 32"],
        "answer": "D",
        "explanation": "L'OTAN compte 32 pays membres depuis l'adhésion de la Suède en 2024."
    },
    {
        "question": "Quel article du traité de l'OTAN définit la défense collective ?",
        "options": ["A) Article 3", "B) Article 5", "C) Article 7", "D) Article 10"],
        "answer": "B",
        "explanation": "L'article 5 stipule qu'une attaque contre un membre est une attaque contre tous."
    },
    {
        "question": "Où se trouve le siège de la Commission européenne ?",
        "options": ["A) Strasbourg", "B) Luxembourg", "C) Bruxelles", "D) Paris"],
        "answer": "C",
        "explanation": "La Commission européenne siège à Bruxelles."
    },
    {
        "question": "Quelle monnaie est utilisée par l'UEMOA ?",
        "options": ["A) Le dollar", "B) L'euro", "C) Le franc CFA", "D) Le cedi"],
        "answer": "C",
        "explanation": "Les pays de l'UEMOA utilisent le franc CFA."
    },
    {
        "question": "Combien d'États membres compte la CEDEAO ?",
        "options": ["A) 12", "B) 13", "C) 14", "D) 15"],
        "answer": "D",
        "explanation": "La CEDEAO compte 15 États membres."
    },
    {
        "question": "Où se trouve le siège de la CEDEAO ?",
        "options": ["A) Dakar", "B) Abuja", "C) Accra", "D) Abidjan"],
        "answer": "B",
        "explanation": "Le siège de la CEDEAO est à Abuja au Nigeria."
    },
    {
        "question": "Quelle organisation africaine est dédiée à l'intégration économique et monétaire ?",
        "options": ["A) L'UA", "B) La CEDEAO", "C) L'UEMOA", "D) La BAD"],
        "answer": "C",
        "explanation": "L'UEMOA vise l'intégration économique et monétaire de ses membres."
    },
    {
        "question": "En quelle année a été créée l'Organisation mondiale du Commerce (OMC) ?",
        "options": ["A) 1985", "B) 1990", "C) 1995", "D) 2000"],
        "answer": "C",
        "explanation": "L'OMC a été créée en 1995, succédant au GATT."
    },
    {
        "question": "Où se trouve le siège de l'OMC ?",
        "options": ["A) New York", "B) Genève", "C) Bruxelles", "D) Paris"],
        "answer": "B",
        "explanation": "L'OMC a son siège à Genève en Suisse."
    },
    {
        "question": "Quel organe de l'ONU s'occupe de l'éducation, la science et la culture ?",
        "options": ["A) UNICEF", "B) UNESCO", "C) OMS", "D) FAO"],
        "answer": "B",
        "explanation": "L'UNESCO est dédiée à l'éducation, la science et la culture."
    },
    {
        "question": "Où se trouve le siège de l'UNESCO ?",
        "options": ["A) Londres", "B) Rome", "C) Paris", "D) Genève"],
        "answer": "C",
        "explanation": "L'UNESCO a son siège à Paris en France."
    },
    {
        "question": "Quel organe de l'ONU s'occupe des réfugiés ?",
        "options": ["A) UNICEF", "B) HCR", "C) OIM", "D) PNUD"],
        "answer": "B",
        "explanation": "Le HCR (Haut-Commissariat aux Réfugiés) protège les réfugiés."
    },
    {
        "question": "Quel organe de l'ONU s'occupe des enfants ?",
        "options": ["A) UNICEF", "B) UNESCO", "C) OMS", "D) PAM"],
        "answer": "A",
        "explanation": "L'UNICEF (Fonds des Nations Unies pour l'Enfance) protège les enfants."
    },
    {
        "question": "En quelle année a été créé le FMI (Fonds Monétaire International) ?",
        "options": ["A) 1944", "B) 1945", "C) 1946", "D) 1950"],
        "answer": "A",
        "explanation": "Le FMI a été créé en 1944 lors de la conférence de Bretton Woods."
    },
    {
        "question": "Où se trouve le siège du FMI ?",
        "options": ["A) New York", "B) Washington", "C) Genève", "D) Londres"],
        "answer": "B",
        "explanation": "Le FMI a son siège à Washington D.C. aux États-Unis."
    },
    {
        "question": "Où se trouve le siège de la Banque mondiale ?",
        "options": ["A) New York", "B) Washington", "C) Londres", "D) Genève"],
        "answer": "B",
        "explanation": "La Banque mondiale a son siège à Washington D.C."
    },
    {
        "question": "Quel traité a créé l'Union européenne ?",
        "options": ["A) Traité de Rome", "B) Traité de Maastricht", "C) Traité de Lisbonne", "D) Traité de Paris"],
        "answer": "B",
        "explanation": "Le traité de Maastricht (1992) a créé l'Union européenne."
    },
    {
        "question": "En quelle année le traité de Maastricht a-t-il été signé ?",
        "options": ["A) 1990", "B) 1992", "C) 1995", "D) 2000"],
        "answer": "B",
        "explanation": "Le traité de Maastricht a été signé le 7 février 1992."
    },
    {
        "question": "Quelle organisation régionale réunit les pays d'Asie du Sud-Est ?",
        "options": ["A) APEC", "B) ASEAN", "C) SAARC", "D) BRICS"],
        "answer": "B",
        "explanation": "L'ASEAN (Association des Nations de l'Asie du Sud-Est) réunit 10 pays."
    },
    {
        "question": "Combien de pays composent le G7 ?",
        "options": ["A) 5", "B) 7", "C) 8", "D) 10"],
        "answer": "B",
        "explanation": "Le G7 comprend 7 pays industrialisés : USA, Canada, Japon, Allemagne, France, Royaume-Uni, Italie."
    },
    {
        "question": "Quel pays a été exclu du G8 en 2014 ?",
        "options": ["A) La Chine", "B) La Russie", "C) L'Inde", "D) Le Brésil"],
        "answer": "B",
        "explanation": "La Russie a été exclue du G8 en 2014 suite à l'annexion de la Crimée."
    },
    {
        "question": "Que signifie BRICS ?",
        "options": ["A) Brésil, Russie, Inde, Chine, Suisse", "B) Brésil, Russie, Inde, Chine, Afrique du Sud", "C) Belgique, Russie, Iran, Chine, Sénégal", "D) Brésil, Roumanie, Inde, Canada, Suède"],
        "answer": "B",
        "explanation": "BRICS = Brésil, Russie, Inde, Chine, South Africa (Afrique du Sud)."
    },
    {
        "question": "Quelle charte, proclamée en 1941 par Roosevelt et Churchill, annonça la création de l'ONU ?",
        "options": ["A) La Charte de San Francisco", "B) La Charte de l'Atlantique", "C) La Charte de Genève", "D) La Charte de Yalta"],
        "answer": "B",
        "explanation": "La Charte de l'Atlantique, signée en août 1941, posa les bases de l'ONU."
    },
    {
        "question": "Lors de la conférence de Yalta (1945), quel dirigeant tenait le plus à la création de l'ONU ?",
        "options": ["A) Roosevelt", "B) Churchill", "C) Staline", "D) De Gaulle"],
        "answer": "A",
        "explanation": "Le président américain Roosevelt fut le plus grand défenseur de la création de l'ONU."
    },
    {
        "question": "Quel est le dernier pays à avoir intégré l'ONU ?",
        "options": ["A) Le Monténégro", "B) Le Soudan du Sud", "C) Le Kosovo", "D) Le Timor oriental"],
        "answer": "B",
        "explanation": "Le Soudan du Sud a rejoint l'ONU en 2011."
    },
    {
        "question": "Quelles sont les langues de travail au Secrétariat Général de l'ONU ?",
        "options": ["A) Français et Anglais", "B) Anglais et Espagnol", "C) Anglais et Chinois", "D) Français et Espagnol"],
        "answer": "A",
        "explanation": "Les deux langues de travail du Secrétariat de l'ONU sont l'anglais et le français."
    },
    {
        "question": "Que représente la sculpture « Non-violence » devant le siège de l'ONU ?",
        "options": ["A) Une colombe", "B) Un revolver noué", "C) Un globe terrestre", "D) Des mains jointes"],
        "answer": "B",
        "explanation": "La sculpture de Carl Fredrik Reuterswärd représente un revolver au canon noué."
    },
    {
        "question": "Quel est le statut de la Palestine à l'ONU ?",
        "options": ["A) Membre à part entière", "B) Membre associé", "C) Observateur", "D) Aucun statut"],
        "answer": "C",
        "explanation": "La Palestine a un statut d'État observateur non membre à l'ONU."
    },
    {
        "question": "L'ONU dispose-t-elle d'une armée propre ?",
        "options": ["A) Oui, avec des soldats permanents", "B) Non, elle utilise les forces des États membres", "C) Oui, basée à Genève"],
        "answer": "B",
        "explanation": "L'ONU n'a pas d'armée propre. Les casques bleus sont fournis par les États membres."
    },
    {
        "question": "Qui est l'actuel Secrétaire Général de l'OTAN ?",
        "options": ["A) Jens Stoltenberg", "B) Anders Rasmussen", "C) Mark Rutte", "D) Ursula von der Leyen"],
        "answer": "C",
        "explanation": "Mark Rutte est devenu Secrétaire Général de l'OTAN en 2024."
    },
    {
        "question": "Quel est le dernier pays à avoir rejoint l'OTAN ?",
        "options": ["A) La Finlande", "B) L'Ukraine", "C) La Suède", "D) La Géorgie"],
        "answer": "C",
        "explanation": "La Suède a rejoint l'OTAN le 7 mars 2024."
    },
    {
        "question": "Qui est le président en exercice de l'Union africaine ?",
        "options": ["A) Macky Sall", "B) Évariste N'dayishimiye", "C) Félix Tshisekedi", "D) William Ruto"],
        "answer": "B",
        "explanation": "Évariste N'dayishimiye, président du Burundi, est président en exercice de l'UA."
    },
    {
        "question": "Combien de membres élus composent le Conseil de Paix et de Sécurité (CPS) de l'UA ?",
        "options": ["A) 10", "B) 15", "C) 20", "D) 25"],
        "answer": "B",
        "explanation": "Le CPS de l'UA est composé de 15 membres élus."
    },
    {
        "question": "Combien de pays compte actuellement la CEDEAO ?",
        "options": ["A) 10", "B) 12", "C) 15", "D) 16"],
        "answer": "B",
        "explanation": "La CEDEAO compte actuellement 12 pays après le retrait du Mali, du Burkina Faso et du Niger."
    },
    {
        "question": "Quel pays a été réintégré à la CEDEAO après sa suspension en 2021 ?",
        "options": ["A) Le Mali", "B) La Guinée", "C) Le Niger", "D) Le Burkina Faso"],
        "answer": "B",
        "explanation": "La Guinée a été réintégrée à la CEDEAO après sa suspension suite au coup d'État de 2021."
    },
    {
        "question": "Quel est le statut juridique de l'AES (Alliance des États du Sahel) ?",
        "options": ["A) Une fédération d'États", "B) Une confédération d'États", "C) Une organisation régionale", "D) Une union économique"],
        "answer": "B",
        "explanation": "L'AES (Mali, Burkina Faso, Niger) est une confédération d'États."
    },
    {
        "question": "La ZLECAF (Zone de Libre-Échange Continentale Africaine) relève de :",
        "options": ["A) La CEDEAO", "B) Un accord sous l'égide de l'UA", "C) L'ONU", "D) L'OMC"],
        "answer": "B",
        "explanation": "La ZLECAF est un accord commercial continental sous l'égide de l'Union africaine."
    },
    {
        "question": "Où se trouve le siège de la SADC (Communauté de développement de l'Afrique australe) ?",
        "options": ["A) Gaborone", "B) Pretoria", "C) Lusaka", "D) Harare"],
        "answer": "A",
        "explanation": "Le siège de la SADC est à Gaborone au Botswana."
    },
    {
        "question": "Combien de pays composent actuellement les BRICS ?",
        "options": ["A) 8", "B) 10", "C) 11", "D) 12"],
        "answer": "B",
        "explanation": "Les BRICS comptent actuellement 10 pays : Brésil, Russie, Inde, Chine, Afrique du Sud, Égypte, Éthiopie, Indonésie, Iran et Émirats arabes unis."
    },
    {
        "question": "Quel pays a été suspendu du Mercosur ?",
        "options": ["A) L'Argentine", "B) Le Venezuela", "C) Le Paraguay", "D) L'Uruguay"],
        "answer": "B",
        "explanation": "Le Venezuela a été suspendu du Mercosur pour rupture de l'ordre démocratique."
    },
    {
        "question": "Combien de membres de plein droit compte le Mercosur ?",
        "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
        "answer": "B",
        "explanation": "Le Mercosur compte 5 membres de plein droit : Argentine, Bolivie, Brésil, Paraguay et Uruguay. Le Venezuela est suspendu."
    },
    {
        "question": "En quelle année la Côte d'Ivoire a-t-elle pris la présidence de la CEDEAO ?",
        "options": ["A) 2012", "B) 2015", "C) 2018", "D) 2020"],
        "answer": "A",
        "explanation": "La Côte d'Ivoire a présidé la CEDEAO en 2012."
    },
    {
        "question": "Qui est le président actuel de la BAD (Banque africaine de développement) ?",
        "options": ["A) Sidi Ould Tah", "B) Akinwumi Adesina", "C) Donald Kaberuka", "D) Cristina Duarte"],
        "answer": "A",
        "explanation": "Sidi Ould Tah est le président actuel de la BAD."
    },
    {
        "question": "Où a été signée en 1992 la Convention-cadre de l'ONU sur les changements climatiques ?",
        "options": ["A) Sommet de Kyoto", "B) Sommet de Paris", "C) Sommet de la Terre à Rio de Janeiro", "D) Sommet de Copenhague"],
        "answer": "C",
        "explanation": "La Convention-cadre a été signée au Sommet de la Terre à Rio de Janeiro en 1992."
    },
    {
        "question": "Le mécanisme africain d'évaluation par les pairs relève de :",
        "options": ["A) La CEDEAO", "B) L'Union africaine", "C) L'ONU", "D) La BAD"],
        "answer": "B",
        "explanation": "Le MAEP est un instrument de l'Union africaine pour promouvoir la bonne gouvernance."
    },
    {
        "question": "La Banque mondiale et le FMI sont-ils associés à l'ONU ?",
        "options": ["A) Oui, ce sont des institutions spécialisées", "B) Non, ils sont totalement indépendants", "C) Seulement la Banque mondiale"],
        "answer": "A",
        "explanation": "La Banque mondiale et le FMI sont des institutions spécialisées du système des Nations Unies."
    },
    {
        "question": "Quelle est la deuxième puissance économique mondiale ?",
        "options": ["A) Le Japon", "B) L'Union européenne", "C) La Chine", "D) L'Inde"],
        "answer": "C",
        "explanation": "La Chine est la deuxième puissance économique mondiale derrière les États-Unis."
    },
    {
        "question": "Qui est l'actuel président de la Commission de la CEDEAO ?",
        "options": ["A) Omar Alieu Touray", "B) Jean-Claude Brou", "C) Julius Maada Bio", "D) Nana Akufo-Addo"],
        "answer": "A",
        "explanation": "Omar Alieu Touray est le président de la Commission de la CEDEAO depuis 2022."
    },
    {
        "question": "Qui est le président actuel de la Commission de l'UEMOA ?",
        "options": ["A) Abdoulaye Diop", "B) Cheickna Seydi Ahamadi Diawara", "C) Boureima Badini", "D) Soumaïla Cissé"],
        "answer": "A",
        "explanation": "Abdoulaye Diop est le président actuel de la Commission de l'UEMOA."
    },
    {
        "question": "Où se trouve le siège de l'Organisation internationale de la Francophonie (OIF) ?",
        "options": ["A) Genève", "B) Bruxelles", "C) Paris", "D) Montréal"],
        "answer": "C",
        "explanation": "Le siège de l'OIF est à Paris."
    },
    {
        "question": "Combien de pays membres compte l'Organisation internationale de la Francophonie ?",
        "options": ["A) 54", "B) 68", "C) 88", "D) 93"],
        "answer": "C",
        "explanation": "L'OIF compte 88 États et gouvernements membres, observateurs et associés."
    },
    {
        "question": "Où se trouve le siège de la Cour pénale internationale (CPI) ?",
        "options": ["A) New York", "B) La Haye", "C) Genève", "D) Bruxelles"],
        "answer": "B",
        "explanation": "La CPI siège à La Haye, aux Pays-Bas."
    },
    {
        "question": "En quelle année la CPI a-t-elle été créée par le Statut de Rome ?",
        "options": ["A) 1998", "B) 2000", "C) 2002", "D) 2005"],
        "answer": "C",
        "explanation": "La CPI est entrée en vigueur le 1er juillet 2002, le Statut de Rome ayant été adopté en 1998."
    },
    {
        "question": "Qu'est-ce que la CEMAC ?",
        "options": ["A) Communauté Économique des États de l'Afrique de l'Ouest", "B) Communauté Économique et Monétaire de l'Afrique Centrale", "C) Commission Européenne des Marchés de Capitaux", "D) Comité Économique des Marchés Africains"],
        "answer": "B",
        "explanation": "La CEMAC est la Communauté Économique et Monétaire de l'Afrique Centrale."
    },
    {
        "question": "Combien de pays composent la CEMAC ?",
        "options": ["A) 4", "B) 6", "C) 8", "D) 10"],
        "answer": "B",
        "explanation": "La CEMAC compte 6 pays : Cameroun, Centrafrique, Congo, Gabon, Guinée équatoriale et Tchad."
    },
    {
        "question": "Où se trouve le siège de la Ligue arabe ?",
        "options": ["A) Riyad", "B) Le Caire", "C) Beyrouth", "D) Tunis"],
        "answer": "B",
        "explanation": "Le siège de la Ligue arabe est au Caire, en Égypte."
    },
    {
        "question": "Combien de pays composent le G20 ?",
        "options": ["A) 19 pays + l'UE", "B) 20 pays exactement", "C) 18 pays + 2 organisations", "D) 20 pays + l'ONU"],
        "answer": "A",
        "explanation": "Le G20 comprend 19 pays + l'Union européenne."
    },
    {
        "question": "Quelle est la différence entre le Conseil de l'Europe et le Conseil européen ?",
        "options": ["A) Aucune, c'est la même chose", "B) Le Conseil de l'Europe est une organisation distincte de l'UE", "C) Le Conseil européen est plus ancien", "D) Le Conseil de l'Europe fait partie de l'ONU"],
        "answer": "B",
        "explanation": "Le Conseil de l'Europe (46 membres, siège à Strasbourg) est indépendant de l'UE. Le Conseil européen est un organe de l'UE."
    },
    {
        "question": "En quelle année ont été signés les Accords de Paris sur le climat ?",
        "options": ["A) 2012", "B) 2015", "C) 2018", "D) 2020"],
        "answer": "B",
        "explanation": "L'Accord de Paris sur le climat a été adopté le 12 décembre 2015 lors de la COP21."
    },
    {
        "question": "Combien de langues officielles compte l'ONU ?",
        "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
        "answer": "C",
        "explanation": "L'ONU a 6 langues officielles : anglais, arabe, chinois, espagnol, français et russe."
    },
    {
        "question": "Quel organe de l'ONU s'occupe de l'alimentation et l'agriculture ?",
        "options": ["A) PAM", "B) FAO", "C) FIDA", "D) UNICEF"],
        "answer": "B",
        "explanation": "La FAO (Organisation des Nations Unies pour l'Alimentation et l'Agriculture) a son siège à Rome."
    },
    {
        "question": "Où se trouve le siège de la FAO ?",
        "options": ["A) Paris", "B) Rome", "C) Genève", "D) New York"],
        "answer": "B",
        "explanation": "Le siège de la FAO est à Rome, en Italie."
    },
    {
        "question": "Quel est le rôle principal du PAM (Programme Alimentaire Mondial) ?",
        "options": ["A) Financer les pays pauvres", "B) Lutter contre la faim dans le monde", "C) Protéger les réfugiés", "D) Promouvoir l'éducation"],
        "answer": "B",
        "explanation": "Le PAM est l'organisme d'aide alimentaire de l'ONU, luttant contre la faim."
    },
    {
        "question": "Quel pays membre fondateur a quitté l'Union européenne ?",
        "options": ["A) La Suisse", "B) La Norvège", "C) Le Royaume-Uni", "D) L'Islande"],
        "answer": "C",
        "explanation": "Le Royaume-Uni a quitté l'UE le 31 janvier 2020 (Brexit)."
    },
    {
        "question": "En quelle année le Brexit a-t-il été effectif ?",
        "options": ["A) 2016", "B) 2018", "C) 2020", "D) 2021"],
        "answer": "C",
        "explanation": "Le Brexit est devenu effectif le 31 janvier 2020 (le référendum avait eu lieu en 2016)."
    },
    {
        "question": "Combien de pays membres l'OPEP compte-t-elle actuellement ?",
        "options": ["A) 10", "B) 11", "C) 12", "D) 15"],
        "answer": "B",
        "explanation": "L'OPEP compte 11 pays membres."
    },
    {
        "question": "Quel organisme de l'ONU est chargé du maintien de la paix ?",
        "options": ["A) L'Assemblée générale", "B) Le Conseil de Sécurité", "C) La CIJ", "D) Le Conseil économique et social"],
        "answer": "B",
        "explanation": "Le Conseil de Sécurité est l'organe principal chargé du maintien de la paix et de la sécurité internationales."
    },
    {
        "question": "Quel est le nombre total de membres du Conseil de Sécurité (permanents + non permanents) ?",
        "options": ["A) 10", "B) 12", "C) 15", "D) 20"],
        "answer": "C",
        "explanation": "Le Conseil de Sécurité compte 15 membres : 5 permanents + 10 non permanents."
    },
    {
        "question": "Quelle convention internationale protège les droits de l'Homme ?",
        "options": ["A) Convention de Genève", "B) Déclaration universelle des droits de l'homme", "C) Traité de Versailles", "D) Charte de l'Atlantique"],
        "answer": "B",
        "explanation": "La DUDH a été adoptée le 10 décembre 1948 par l'Assemblée générale de l'ONU."
    },
    {
        "question": "En quelle année la Déclaration universelle des droits de l'homme a-t-elle été adoptée ?",
        "options": ["A) 1945", "B) 1948", "C) 1950", "D) 1955"],
        "answer": "B",
        "explanation": "La DUDH a été adoptée le 10 décembre 1948 à Paris."
    },
    {
        "question": "Où se trouve le siège de l'Organisation Internationale du Travail (OIT) ?",
        "options": ["A) New York", "B) Genève", "C) Paris", "D) Bruxelles"],
        "answer": "B",
        "explanation": "L'OIT a son siège à Genève, en Suisse."
    },
    {
        "question": "Quel accord de libre-échange lie les États-Unis, le Mexique et le Canada ?",
        "options": ["A) ALENA", "B) ACEUM (USMCA)", "C) MERCOSUR", "D) APEC"],
        "answer": "B",
        "explanation": "L'ACEUM (ou USMCA en anglais) a remplacé l'ALENA en 2020."
    },
    {
        "question": "En quelle ann?e l'ONU a-t-elle ete creee ?",
        "options": ["A) 24 octobre 1945", "B) 8 mai 1945", "C) 26 juin 1945", "D) 1er janvier 1946"],
        "answer": "A",
        "explanation": "L'ONU a officiellement ete creee le 24 octobre 1945, date d'entree en vigueur de la Charte des Nations Unies."
    },
    {
        "question": "Combien d'?tats membres compte l'ONU ?",
        "options": ["A) 185", "B) 193", "C) 197", "D) 200"],
        "answer": "B",
        "explanation": "L'ONU compte actuellement 193 ?tats membres."
    },
    {
        "question": "Quel est le dernier pays a avoir integre l'ONU ?",
        "options": ["A) Kosovo", "B) Soudan du Sud", "C) Timor oriental", "D) Montenegro"],
        "answer": "B",
        "explanation": "Le Soudan du Sud est le 193e et dernier ?tat a integrer l'ONU, en juillet 2011."
    },
    {
        "question": "Quelle est la nationalit? de l'actuel Secretaire General des Nations Unies ?",
        "options": ["A) Ghaneenne", "B) Portugaise", "C) Bresilienne", "D) Canadienne"],
        "answer": "B",
        "explanation": "Antonio Guterres, Secretaire General de l'ONU depuis janvier 2017, est Portugais."
    },
    {
        "question": "Quel Secretaire General de l'ONU a obtenu le prix Nobel de la Paix en 2001 ?",
        "options": ["A) Boutros Boutros-Ghali", "B) Kofi Annan", "C) Ban Ki-moon", "D) Javier Perez de Cuellar"],
        "answer": "B",
        "explanation": "Kofi Annan et l'ONU ont conjointement recu le prix Nobel de la Paix le 10 decembre 2001."
    },
    {
        "question": "En quelle ann?e l'OTAN a-t-elle ete creee ?",
        "options": ["A) 4 avril 1949", "B) 5 mai 1950", "C) 24 octobre 1945", "D) 14 aout 1941"],
        "answer": "A",
        "explanation": "L'OTAN a ete creee le 4 avril 1949 par le traite de Washington."
    },
    {
        "question": "Ou se trouve le siege de l'OTAN ?",
        "options": ["A) Bruxelles", "B) Paris", "C) Londres", "D) Geneve"],
        "answer": "A",
        "explanation": "Le siege de l'OTAN est a Bruxelles, en Belgique."
    },
    {
        "question": "Quel est l'actuel Secretaire General de l'OTAN ?",
        "options": ["A) Jens Stoltenberg", "B) Anders Fogh Rasmussen", "C) Mark Rutte", "D) George Robertson"],
        "answer": "C",
        "explanation": "Mark Rutte est l'actuel Secretaire General de l'OTAN depuis octobre 2024."
    },
    {
        "question": "Quel est le dernier ?tat a avoir adhre a l'OTAN ?",
        "options": ["A) La Finlande", "B) La Suede", "C) L'Ukraine", "D) La Georgie"],
        "answer": "B",
        "explanation": "La Suede a rejoint l'OTAN le 7 mars 2024, devenant le 32e ?tat membre."
    },
    {
        "question": "Combien d'?tats membres compte l'Union Europeenne ?",
        "options": ["A) 25", "B) 27", "C) 28", "D) 30"],
        "answer": "B",
        "explanation": "L'UE compte 27 ?tats membres depuis le Brexit en 2020."
    },
    {
        "question": "Ou siege principalement le Parlement europeen ?",
        "options": ["A) Bruxelles", "B) Luxembourg", "C) Strasbourg", "D) Paris"],
        "answer": "C",
        "explanation": "Le Parlement europeen siege principalement a Strasbourg."
    },
    {
        "question": "La CEDEAO a ete creee en :",
        "options": ["A) 1960", "B) 1975", "C) 1980", "D) 1990"],
        "answer": "B",
        "explanation": "La CEDEAO a ete creee en 1975 par le traite de Lagos."
    },
    {
        "question": "Combien de pays membres compte la CEDEAO aujourd'hui ?",
        "options": ["A) 15", "B) 12", "C) 16", "D) 10"],
        "answer": "B",
        "explanation": "Suite aux suspensions et retraits (Mali, Burkina Faso, Niger), la CEDEAO compte actuellement 12 membres."
    },
    {
        "question": "Ou se trouve le siege de l'UEMOA ?",
        "options": ["A) Abidjan", "B) Ouagadougou", "C) Dakar", "D) Lome"],
        "answer": "B",
        "explanation": "Le siege de l'UEMOA est a Ouagadougou, au Burkina Faso."
    },
    {
        "question": "La Banque africaine de developpement (BAD) a son siege a :",
        "options": ["A) Abidjan", "B) Addis-Abeba", "C) Le Caire", "D) Nairobi"],
        "answer": "A",
        "explanation": "Le siege permanent de la BAD est a Abidjan, en C?te d'Ivoire."
    },
    {
        "question": "Quel organisme a obtenu le prix Nobel de la Paix en 2012 ?",
        "options": ["A) L'ONU", "B) L'Union Europeenne", "C) L'OTAN", "D) L'OMS"],
        "answer": "B",
        "explanation": "L'Union Europeenne a ete couronnee du prix Nobel de la Paix en 2012."
    },
    {
        "question": "L'Union africaine a succede a :",
        "options": ["A) La CEDEAO", "B) L'OUA", "C) La CEMAC", "D) L'UEMOA"],
        "answer": "B",
        "explanation": "L'UA a succede a l'Organisation de l'Unite Africaine (OUA) en 2002."
    },
    {
        "question": "Quel est le statut juridique de l'AES (Alliance des ?tats du Sahel) ?",
        "options": ["A) Une federation", "B) Une confederation d'?tats", "C) Une communaute ?conomique", "D) Une alliance militaire"],
        "answer": "B",
        "explanation": "L'AES regroupe le Mali, le Burkina Faso et le Niger sous forme de confederation d'?tats."
    },
    {
        "question": "La ZLECAF releve de :",
        "options": ["A) La CEDEAO", "B) L'Union Africaine", "C) L'ONU", "D) La Banque mondiale"],
        "answer": "B",
        "explanation": "La Zone de Libre-Echange Continentale Africaine (ZLECAF) est un accord sous l'egide de l'Union Africaine."
    },
    {
        "question": "Combien d'?tats membres compte l'UEMOA ?",
        "options": ["A) 5", "B) 8", "C) 10", "D) 12"],
        "answer": "B",
        "explanation": "L'UEMOA compte 8 ?tats membres partageant le franc CFA."
    }
]

# THÈME 5 : Anglais (English Grammar)
THEME_5 = [
    {
        "question": "Complete: 'If I ___ you, I would apologize.'",
        "options": ["A) am", "B) was", "C) were", "D) be"],
        "answer": "C",
        "explanation": "Type 2 conditional uses 'were' for all persons with the verb 'to be'."
    },
    {
        "question": "Which sentence is correct?",
        "options": ["A) If it will rain, I stay home", "B) If it rains, I will stay home", "C) If it rains, I would stay home"],
        "answer": "B",
        "explanation": "Type 1 conditional: never use 'will' immediately after 'if'. Structure: If + Present, will + verb."
    },
    {
        "question": "'You ___ park here. It's forbidden.'",
        "options": ["A) mustn't", "B) needn't", "C) shouldn't", "D) can't"],
        "answer": "A",
        "explanation": "'Mustn't' expresses prohibition (interdiction). 'Needn't' means no obligation."
    },
    {
        "question": "Choose the correct article: 'She is ___ honest woman.'",
        "options": ["A) a", "B) an", "C) the", "D) Ø"],
        "answer": "B",
        "explanation": "Use 'an' before words starting with a vowel SOUND. 'Honest' starts with a silent 'h'."
    },
    {
        "question": "'I travel ___ bus every day.'",
        "options": ["A) by", "B) on the", "C) in a", "D) with"],
        "answer": "A",
        "explanation": "'By' + means of transport (without article) is used for general transport."
    },
    {
        "question": "'If I had known, I ___ differently.'",
        "options": ["A) would act", "B) would have acted", "C) will act", "D) acted"],
        "answer": "B",
        "explanation": "Type 3 conditional (past regret): If + Past Perfect → Would have + Past Participle."
    },
    {
        "question": "'You ___ come if you don't want to.'",
        "options": ["A) mustn't", "B) don't have to", "C) can't", "D) shouldn't"],
        "answer": "B",
        "explanation": "'Don't have to' expresses absence of obligation. 'Mustn't' is prohibition."
    },
    {
        "question": "Which preposition? 'The meeting is ___ Monday.'",
        "options": ["A) at", "B) in", "C) on", "D) by"],
        "answer": "C",
        "explanation": "Use 'on' for specific days: on Monday, on Tuesday, on my birthday."
    },
    {
        "question": "'She ___ speak three languages.' (Present ability)",
        "options": ["A) can", "B) could", "C) may", "D) might"],
        "answer": "A",
        "explanation": "'Can' expresses ability in the present. 'Could' is past or politeness."
    },
    {
        "question": "'___ water boils at 100°C.'",
        "options": ["A) A", "B) The", "C) Ø (no article)", "D) An"],
        "answer": "C",
        "explanation": "No article for general truths with uncountable nouns like 'water'."
    },
    {
        "question": "'If water reaches 0°C, it ___.'",
        "options": ["A) freezes", "B) will freeze", "C) would freeze", "D) freeze"],
        "answer": "A",
        "explanation": "Type Zero conditional (general truth): If + Present → Present."
    },
    {
        "question": "'He ___ be at home. His car is in the driveway.' (Deduction)",
        "options": ["A) might", "B) must", "C) should", "D) can"],
        "answer": "B",
        "explanation": "'Must' expresses strong deduction/logical certainty (quasi-certitude)."
    },
    {
        "question": "'I was sitting ___ the train when I saw him.'",
        "options": ["A) by", "B) in", "C) on", "D) at"],
        "answer": "C",
        "explanation": "'On' is used for public transport: on the bus, on the train, on the plane."
    },
    {
        "question": "'You ___ to see a doctor. You look ill.' (Advice)",
        "options": ["A) ought", "B) must", "C) might", "D) need"],
        "answer": "A",
        "explanation": "'Ought to' expresses advice/recommendation (conseil)."
    },
    {
        "question": "'___ dogs are loyal animals.'",
        "options": ["A) A", "B) The", "C) Ø (no article)", "D) An"],
        "answer": "C",
        "explanation": "No article for general statements with plural nouns."
    },
    {
        "question": "'The concert is ___ 8 PM.'",
        "options": ["A) at", "B) in", "C) on", "D) by"],
        "answer": "A",
        "explanation": "Use 'at' for precise times: at 8 PM, at noon, at midnight."
    },
    {
        "question": "'If she ___ harder, she would pass the exam.'",
        "options": ["A) studies", "B) studied", "C) will study", "D) study"],
        "answer": "B",
        "explanation": "Type 2 conditional (imaginary present): If + Past Simple → Would + verb."
    },
    {
        "question": "'He travels to work ___ car.'",
        "options": ["A) by", "B) in", "C) on", "D) with"],
        "answer": "A",
        "explanation": "'By car' (no article) for general transport method. 'In a car' for specific vehicle."
    },
    {
        "question": "'It ___ rain later. Take an umbrella.' (Possibility ~50%)",
        "options": ["A) must", "B) may", "C) should", "D) will"],
        "answer": "B",
        "explanation": "'May' expresses possibility (~50% probability)."
    },
    {
        "question": "'My birthday is ___ July 15th.'",
        "options": ["A) at", "B) in", "C) on", "D) by"],
        "answer": "C",
        "explanation": "Use 'on' for specific dates: on July 15th, on December 25th."
    },
    {
        "question": "'She has lived here ___ 2010.'",
        "options": ["A) since", "B) for", "C) during", "D) from"],
        "answer": "A",
        "explanation": "'Since' is used with a specific point in time (depuis 2010)."
    },
    {
        "question": "'I have studied English ___ five years.'",
        "options": ["A) since", "B) for", "C) during", "D) ago"],
        "answer": "B",
        "explanation": "'For' is used with a duration (pendant 5 ans)."
    },
    {
        "question": "'I visited Paris three years ___.'",
        "options": ["A) since", "B) for", "C) ago", "D) before"],
        "answer": "C",
        "explanation": "'Ago' is used with past simple for a point in the past (il y a 3 ans)."
    },
    {
        "question": "'He ___ finished his homework yet.'",
        "options": ["A) hasn't", "B) didn't", "C) doesn't", "D) wasn't"],
        "answer": "A",
        "explanation": "'Yet' with present perfect negative: hasn't/haven't + past participle."
    },
    {
        "question": "'Have you ___ been to Japan?'",
        "options": ["A) yet", "B) ever", "C) already", "D) never"],
        "answer": "B",
        "explanation": "'Ever' is used in questions with present perfect (déjà dans ta vie)."
    },
    {
        "question": "'I have ___ finished my work.'",
        "options": ["A) yet", "B) ever", "C) already", "D) ago"],
        "answer": "C",
        "explanation": "'Already' with present perfect affirmative: have already + past participle."
    },
    {
        "question": "'Neither John ___ Mary came to the party.'",
        "options": ["A) or", "B) nor", "C) and", "D) but"],
        "answer": "B",
        "explanation": "'Neither...nor' is the correct correlative conjunction."
    },
    {
        "question": "'Either you apologize, ___ I will leave.'",
        "options": ["A) and", "B) but", "C) or", "D) nor"],
        "answer": "C",
        "explanation": "'Either...or' expresses a choice/alternative."
    },
    {
        "question": "'She is not only intelligent ___ also kind.'",
        "options": ["A) and", "B) but", "C) or", "D) yet"],
        "answer": "B",
        "explanation": "'Not only...but also' is the correct correlative conjunction."
    },
    {
        "question": "'I would rather ___ at home today.'",
        "options": ["A) stay", "B) to stay", "C) staying", "D) stayed"],
        "answer": "A",
        "explanation": "'Would rather' is followed by base form (infinitive without 'to')."
    },
    {
        "question": "'She made me ___ my homework.'",
        "options": ["A) do", "B) to do", "C) doing", "D) did"],
        "answer": "A",
        "explanation": "'Make' is followed by object + base form (without 'to')."
    },
    {
        "question": "'He let me ___ his car.'",
        "options": ["A) use", "B) to use", "C) using", "D) used"],
        "answer": "A",
        "explanation": "'Let' is followed by object + base form (without 'to')."
    },
    {
        "question": "'She wants me ___ her.'",
        "options": ["A) help", "B) to help", "C) helping", "D) helped"],
        "answer": "B",
        "explanation": "'Want' is followed by object + to-infinitive."
    },
    {
        "question": "'I'm looking forward ___ you.'",
        "options": ["A) see", "B) to see", "C) to seeing", "D) seeing"],
        "answer": "C",
        "explanation": "'Look forward to' is followed by gerund (verb + -ing)."
    },
    {
        "question": "'He is used ___ early.'",
        "options": ["A) wake up", "B) to wake up", "C) to waking up", "D) waking up"],
        "answer": "C",
        "explanation": "'Be used to' (être habitué à) is followed by gerund."
    },
    {
        "question": "'He used ___ in London.'",
        "options": ["A) live", "B) to live", "C) living", "D) lived"],
        "answer": "B",
        "explanation": "'Used to' (habitude passée) is followed by base form."
    },
    {
        "question": "'The book ___ by millions of people.'",
        "options": ["A) was read", "B) read", "C) is reading", "D) reads"],
        "answer": "A",
        "explanation": "Passive voice (past): was/were + past participle."
    },
    {
        "question": "'The house ___ built in 1990.'",
        "options": ["A) is", "B) was", "C) has", "D) had"],
        "answer": "B",
        "explanation": "Passive voice with specific past date uses 'was/were'."
    },
    {
        "question": "'English ___ all over the world.'",
        "options": ["A) speaks", "B) is spoken", "C) is speaking", "D) has spoken"],
        "answer": "B",
        "explanation": "Passive voice (present): is/are + past participle."
    },
    {
        "question": "'I wish I ___ rich.'",
        "options": ["A) am", "B) was", "C) were", "D) be"],
        "answer": "C",
        "explanation": "'I wish' + past tense for present unreal situation. Use 'were' for 'to be'."
    },
    {
        "question": "'I wish I ___ studied harder.' (Past regret)",
        "options": ["A) have", "B) had", "C) would", "D) could"],
        "answer": "B",
        "explanation": "'I wish' + past perfect for past regret."
    },
    {
        "question": "'If only I ___ more time!'",
        "options": ["A) have", "B) had", "C) will have", "D) would have"],
        "answer": "B",
        "explanation": "'If only' + past tense for present wish/regret."
    },
    {
        "question": "'He asked me where I ___.'",
        "options": ["A) live", "B) lived", "C) am living", "D) lives"],
        "answer": "B",
        "explanation": "Reported speech: present → past (backshift)."
    },
    {
        "question": "'She said she ___ come tomorrow.'",
        "options": ["A) will", "B) would", "C) can", "D) may"],
        "answer": "B",
        "explanation": "Reported speech: 'will' becomes 'would'."
    },
    {
        "question": "'There ___ many people at the party yesterday.'",
        "options": ["A) was", "B) were", "C) is", "D) are"],
        "answer": "B",
        "explanation": "'There were' for plural subjects in the past."
    },
    {
        "question": "'There ___ a problem with the system.'",
        "options": ["A) is", "B) are", "C) was", "D) were"],
        "answer": "A",
        "explanation": "'There is' for singular subjects in the present."
    },
    {
        "question": "'Few people ___ the answer.'",
        "options": ["A) knows", "B) know", "C) knowing", "D) knew"],
        "answer": "B",
        "explanation": "'Few people' is plural, so use 'know' (no -s)."
    },
    {
        "question": "'Each student ___ a book.'",
        "options": ["A) have", "B) has", "C) having", "D) are having"],
        "answer": "B",
        "explanation": "'Each' is singular, so use 'has'."
    },
    {
        "question": "'Neither of the answers ___ correct.'",
        "options": ["A) is", "B) are", "C) were", "D) being"],
        "answer": "A",
        "explanation": "'Neither' is singular, so use 'is'."
    },
    {
        "question": "'The team ___ playing well.' (as a unit)",
        "options": ["A) is", "B) are", "C) was", "D) were"],
        "answer": "A",
        "explanation": "Collective nouns can be singular (unit) or plural (individuals). Here, 'is' for unit."
    },
    {
        "question": "'She is ___ than her sister.' (intelligent)",
        "options": ["A) more intelligent", "B) most intelligent", "C) intelligenter", "D) more intelligenter"],
        "answer": "A",
        "explanation": "Long adjectives use 'more' for comparatives: more intelligent."
    },
    {
        "question": "'He is the ___ student in the class.'",
        "options": ["A) most tallest", "B) tallest", "C) more tall", "D) taller"],
        "answer": "B",
        "explanation": "Short adjectives use '-est' for superlatives: the tallest."
    },
    {
        "question": "'You like coffee, ___?'",
        "options": ["A) don't you", "B) do you", "C) isn't it", "D) aren't you"],
        "answer": "A",
        "explanation": "Question tags: positive statement → negative tag. 'You like' → 'don't you?'"
    },
    {
        "question": "'She can't swim, ___?'",
        "options": ["A) can't she", "B) can she", "C) could she", "D) does she"],
        "answer": "B",
        "explanation": "Question tags: negative statement → positive tag. 'Can't swim' → 'can she?'"
    },
    {
        "question": "'The man ___ lives next door is a doctor.'",
        "options": ["A) which", "B) who", "C) whom", "D) whose"],
        "answer": "B",
        "explanation": "'Who' is used for people as subject in relative clauses."
    },
    {
        "question": "'The book ___ I read was fascinating.'",
        "options": ["A) who", "B) which", "C) whose", "D) whom"],
        "answer": "B",
        "explanation": "'Which' (or 'that') is used for things in relative clauses."
    },
    {
        "question": "'The girl ___ father is a pilot studies here.'",
        "options": ["A) who", "B) which", "C) whose", "D) whom"],
        "answer": "C",
        "explanation": "'Whose' indicates possession in relative clauses."
    },
    {
        "question": "'If I ___ about the meeting, I would have attended.'" ,
        "options": ["A) know", "B) knew", "C) had known", "D) have known"],
        "answer": "C",
        "explanation": "Type 3 conditional: If + Past Perfect → Would have + Past Participle."
    },
    {
        "question": "'She asked me ___ I was going.'",
        "options": ["A) where", "B) that", "C) what", "D) if"],
        "answer": "A",
        "explanation": "Reported questions with 'wh-' words keep the question word: 'Where are you going?' → 'where I was going.'"
    },
    {
        "question": "'He told me ___ he would come.'" ,
        "options": ["A) what", "B) that", "C) if", "D) where"],
        "answer": "B",
        "explanation": "Reported statements use 'that' (optional): He said, 'I will come' → He told me that he would come."
    },
    {
        "question": "Choose the correct sentence:",
        "options": ["A) He suggested to go out", "B) He suggested going out", "C) He suggested go out", "D) He suggested that going out"],
        "answer": "B",
        "explanation": "'Suggest' is followed by gerund (verb + -ing) or 'that + subject + base form'."
    },
    {
        "question": "'I ___ up at 6 AM every day.' (habitual action)",
        "options": ["A) wake", "B) woke", "C) waken", "D) waking"],
        "answer": "A",
        "explanation": "Present simple for habitual actions: I wake up every day."
    },
    {
        "question": "'By next year, I ___ here for ten years.'",
        "options": ["A) will work", "B) will have worked", "C) will be working", "D) work"],
        "answer": "B",
        "explanation": "Future perfect: 'will have + past participle' for actions completed before a future point."
    },
    {
        "question": "'She enjoys ___ books in her free time.'",
        "options": ["A) read", "B) to read", "C) reading", "D) reads"],
        "answer": "C",
        "explanation": "'Enjoy' is always followed by gerund (verb + -ing)."
    },
    {
        "question": "'He avoided ___ the question.'",
        "options": ["A) answer", "B) to answer", "C) answering", "D) answered"],
        "answer": "C",
        "explanation": "'Avoid' is followed by gerund. Some verbs require -ing form."
    },
    {
        "question": "'Despite ___ hard, he failed the exam.'",
        "options": ["A) study", "B) to study", "C) studying", "D) studied"],
        "answer": "C",
        "explanation": "'Despite' is followed by a noun or gerund: despite studying hard."
    },
    {
        "question": "'I'm not ___ tall ___ my brother.'",
        "options": ["A) so...than", "B) as...as", "C) more...than", "D) so...so"],
        "answer": "B",
        "explanation": "'As...as' is used for comparisons of equality (or inequality with 'not')."
    },
    {
        "question": "'The more you study, the ___ you learn.'",
        "options": ["A) much", "B) more", "C) most", "D) many"],
        "answer": "B",
        "explanation": "'The more...the more' is a correlative comparative structure."
    },
    {
        "question": "'He ___ to the gym three times a week.' (regular habit)",
        "options": ["A) is going", "B) goes", "C) go", "D) going"],
        "answer": "B",
        "explanation": "Present simple for regular habits: He goes (third person -s)."
    },
    {
        "question": "'We arrived ___ the airport ___ time.'",
        "options": ["A) at / on", "B) in / on", "C) at / in", "D) to / at"],
        "answer": "A",
        "explanation": "'Arrive at' + specific place, 'on time' = à l'heure."
    },
    {
        "question": "'I have been living here ___ January.'",
        "options": ["A) for", "B) since", "C) during", "D) from"],
        "answer": "B",
        "explanation": "'Since' + specific point in time (since January). 'For' + duration."
    },
    {
        "question": "Choose the correct article: '___ university is a place of learning.'",
        "options": ["A) An", "B) A", "C) The", "D) Ø"],
        "answer": "B",
        "explanation": "'A' before 'university' because the first sound is /juː/ (consonant sound), not a vowel sound."
    },
    {
        "question": "'He ___ be tired. He has been working all day.' (logical deduction)",
        "options": ["A) can", "B) may", "C) must", "D) should"],
        "answer": "C",
        "explanation": "'Must' for strong logical deduction based on evidence."
    },
    {
        "question": "'They ___ have left already. The lights are off.' (deduction about past)",
        "options": ["A) can", "B) must", "C) should", "D) would"],
        "answer": "B",
        "explanation": "'Must have + past participle' for deductions about the past."
    },
    {
        "question": "'I ___ dinner when the phone rang.'",
        "options": ["A) cooked", "B) was cooking", "C) have cooked", "D) cook"],
        "answer": "B",
        "explanation": "Past continuous for an ongoing action interrupted by another event."
    },
    {
        "question": "'She ___ for two hours when he arrived.'",
        "options": ["A) waited", "B) was waiting", "C) had been waiting", "D) has waited"],
        "answer": "C",
        "explanation": "Past perfect continuous for a duration before a past event: had been + -ing."
    },
    {
        "question": "'How ___ sugar do you need?'",
        "options": ["A) many", "B) much", "C) few", "D) several"],
        "answer": "B",
        "explanation": "'Much' for uncountable nouns. 'Many' for countable nouns."
    },
    {
        "question": "'There are ___ apples in the basket.'",
        "options": ["A) much", "B) a few", "C) a little", "D) less"],
        "answer": "B",
        "explanation": "'A few' for countable nouns (positive sense). 'A little' for uncountable."
    },
    {
        "question": "Which noun is uncountable?",
        "options": ["A) Book", "B) Chair", "C) Information", "D) Apple"],
        "answer": "C",
        "explanation": "'Information' is uncountable: 'some information' (never 'informations' in English)."
    },
    {
        "question": "Which noun is uncountable?",
        "options": ["A) Advice", "B) Student", "C) Table", "D) Question"],
        "answer": "A",
        "explanation": "'Advice' is uncountable: 'a piece of advice' (never 'an advice')."
    },
    {
        "question": "'She ___ here for three years.' (and still works here)",
        "options": ["A) worked", "B) works", "C) has been working", "D) was working"],
        "answer": "C",
        "explanation": "Present perfect continuous for an action that started in the past and continues."
    },
    {
        "question": "'He ___ while I ___ .' (read / study)",
        "options": ["A) was reading / was studying", "B) read / studied", "C) was reading / studied", "D) read / was studying"],
        "answer": "A",
        "explanation": "Two simultaneous ongoing past actions: both in past continuous."
    },
    {
        "question": "'Although it was raining, ___'",
        "options": ["A) but they went out", "B) they went out", "C) so they stayed", "D) however they left"],
        "answer": "B",
        "explanation": "'Although' introduces a concession — no need for 'but'. Avoid double conjunction."
    },
    {
        "question": "'___ the rain, they went out.'",
        "options": ["A) Although", "B) Despite", "C) However", "D) Because of"],
        "answer": "B",
        "explanation": "'Despite' + noun/gerund for concession. 'Although' needs a clause."
    },
    {
        "question": "'He is good ___ mathematics.'",
        "options": ["A) in", "B) at", "C) on", "D) for"],
        "answer": "B",
        "explanation": "'Good at' is the correct preposition for skills/subjects."
    },
    {
        "question": "'She is interested ___ history.'",
        "options": ["A) about", "B) at", "C) in", "D) for"],
        "answer": "C",
        "explanation": "'Interested in' is the correct preposition."
    },
    {
        "question": "'He depends ___ his parents financially.'",
        "options": ["A) of", "B) on", "C) from", "D) in"],
        "answer": "B",
        "explanation": "'Depend on' is the correct preposition (not 'depend of')."
    },
    {
        "question": "'Could you look ___ my cat while I'm away?' (take care of)",
        "options": ["A) at", "B) for", "C) after", "D) up"],
        "answer": "C",
        "explanation": "'Look after' means to take care of someone/something."
    },
    {
        "question": "'I need to look ___ a word in the dictionary.' (search for)",
        "options": ["A) at", "B) for", "C) up", "D) after"],
        "answer": "C",
        "explanation": "'Look up' means to search for information in a reference."
    },
    {
        "question": "'He ___ up smoking last year.' (stop)",
        "options": ["A) gave", "B) put", "C) took", "D) got"],
        "answer": "A",
        "explanation": "'Give up' means to stop/quit a habit."
    },
    {
        "question": "'___ you study hard, you won't pass the exam.'",
        "options": ["A) If", "B) Unless", "C) Although", "D) Despite"],
        "answer": "B",
        "explanation": "'Unless' = 'if not'. Unless you study hard = if you don't study hard."
    },
    {
        "question": "'He ran fast ___ he could catch the bus.'",
        "options": ["A) so that", "B) because", "C) although", "D) unless"],
        "answer": "A",
        "explanation": "'So that' expresses purpose (pour que/afin que)."
    },
    {
        "question": "'___ I finish this report, I will call you.'",
        "options": ["A) While", "B) During", "C) As soon as", "D) Until"],
        "answer": "C",
        "explanation": "'As soon as' = dès que. Followed by present tense for future meaning."
    },
    {
        "question": "'This is the city ___ I was born.'",
        "options": ["A) which", "B) who", "C) where", "D) that"],
        "answer": "C",
        "explanation": "'Where' for places in relative clauses."
    },
    {
        "question": "'I don't know ___ he is coming or not.'",
        "options": ["A) if", "B) whether", "C) that", "D) Both A and B"],
        "answer": "D",
        "explanation": "Both 'if' and 'whether' can introduce indirect yes/no questions. 'Whether' is more formal."
    },
    {
        "question": "'He speaks English ___ fluently ___ French.' (comparison of equality)",
        "options": ["A) so / than", "B) as / as", "C) more / than", "D) less / as"],
        "answer": "B",
        "explanation": "'As...as' for comparisons of equality: He speaks English as fluently as French."
    },
    {
        "question": "'___ having a headache, she went to work.'",
        "options": ["A) Although", "B) In spite of", "C) Because", "D) Due to"],
        "answer": "B",
        "explanation": "'In spite of' + gerund/noun for concession (synonym of 'despite')."
    },
    {
        "question": "'He ___ to London twice this year.' (experience up to now)",
        "options": ["A) went", "B) has been", "C) was going", "D) goes"],
        "answer": "B",
        "explanation": "Present perfect for experiences within an unfinished time period ('this year')."
    },
    {
        "question": "'The exam was ___ than I expected.'",
        "options": ["A) more easier", "B) easier", "C) most easy", "D) easy"],
        "answer": "B",
        "explanation": "Short adjectives: comparative = adjective + '-er'. Never 'more + -er'."
    },
    {
        "question": "'You ___ to see a doctor. You look ill.' (conseil)",
        "options": ["A) ought", "B) must", "C) might", "D) can"],
        "answer": "A",
        "explanation": "'Ought to' expresses advice, similar to 'should'."
    },
    {
        "question": "'___ dogs are loyal animals.' (generalite)",
        "options": ["A) A", "B) The", "C) An", "D) No article"],
        "answer": "D",
        "explanation": "No article for generalities with plural countable nouns."
    },
    {
        "question": "'If water reaches 0 degrees, it ___.'",
        "options": ["A) freezes", "B) will freeze", "C) would freeze", "D) froze"],
        "answer": "A",
        "explanation": "Type Zero conditional for scientific truths: If + Present, Present."
    },
    {
        "question": "'He ___ be at home. His car is in the driveway.' (deduction forte)",
        "options": ["A) might", "B) must", "C) should", "D) could"],
        "answer": "B",
        "explanation": "'Must' expresses strong logical deduction based on evidence."
    },
    {
        "question": "'I was sitting ___ the train when I saw him.'",
        "options": ["A) by", "B) in", "C) on", "D) at"],
        "answer": "C",
        "explanation": "Use 'on' for public/collective transport: on the train, on the bus."
    },
    {
        "question": "'You ___ park here. It is forbidden.'",
        "options": ["A) mustn't", "B) needn't", "C) don't have to", "D) shouldn't"],
        "answer": "A",
        "explanation": "'Mustn't' expresses prohibition. 'Needn't/don't have to' express absence of obligation."
    },
    {
        "question": "Complete: 'If I had studied harder, I ___ the exam.'",
        "options": ["A) would pass", "B) will have passed", "C) would have passed", "D) passed"],
        "answer": "C",
        "explanation": "Type 3 conditional: If + Past Perfect, Would have + Past Participle."
    },
    {
        "question": "Which sentence uses the correct article?",
        "options": ["A) She plays the tennis every morning.", "B) She plays tennis every morning.", "C) She plays a tennis every morning.", "D) She plays an tennis every morning."],
        "answer": "B",
        "explanation": "No article before sports: she plays tennis."
    },
    {
        "question": "Complete: 'By next year, she ___ her degree.'",
        "options": ["A) will finish", "B) will have finished", "C) finishes", "D) would finish"],
        "answer": "B",
        "explanation": "Future perfect: actions completed before a future point in time."
    },
    {
        "question": "Complete: '___ honest man always tells the truth.'",
        "options": ["A) A", "B) An", "C) The", "D) No article"],
        "answer": "B",
        "explanation": "Use 'an' before vowel sounds. 'Honest' starts with a silent h."
    },
    {
        "question": "Which sentence is grammatically correct?",
        "options": ["A) He doesn't know nothing.", "B) He knows nothing.", "C) He don't know nothing.", "D) He knows not nothing."],
        "answer": "B",
        "explanation": "In standard English, double negatives are incorrect. Use 'He knows nothing.'"
    },
    {
        "question": "'She ___ speak three languages.' (capacite presente)",
        "options": ["A) can", "B) could", "C) may", "D) might"],
        "answer": "A",
        "explanation": "'Can' expresses present ability. 'Could' is for past ability or polite requests."
    }
]

# THÈME 6 : Institutions, droit et citoyenneté
THEME_6 = [
    {
        "question": "Quelle est la différence entre une loi et un règlement ?",
        "options": ["A) Une loi est générale et abstraite, le règlement précise son application", "B) Le règlement est supérieur à la loi", "C) Une loi ne s'applique qu'aux entreprises", "D) Il n'y a pas de différence"],
        "answer": "A",
        "explanation": "La loi fixe les principes généraux, tandis que les règlements les appliquent au niveau technique et administratif."
    },
    {
        "question": "Quel est le rôle principal du Conseil constitutionnel en France ?",
        "options": ["A) Gérer le budget", "B) Contrôler la constitutionnalité des lois", "C) Diriger les administrations", "D) Nommer les juges"],
        "answer": "B",
        "explanation": "Le Conseil constitutionnel veille à la conformité des lois à la Constitution."
    },
    {
        "question": "Que signifie le principe de laïcité ?",
        "options": ["A) L'État impose une religion", "B) La séparation des Églises et de l'État", "C) L'abolition des droits fondamentaux", "D) L'État ne protège que les croyants"],
        "answer": "B",
        "explanation": "La laïcité garantit la neutralité religieuse de l'État et la liberté de conscience."
    },
    {
        "question": "Quel est le devoir citoyen le plus directement lié au vote ?",
        "options": ["A) Le respect des horaires", "B) La participation politique", "C) Le paiement des impôts", "D) Le port de l'uniforme"],
        "answer": "B",
        "explanation": "Le vote est un acte central de participation à la vie politique et de citoyenneté."
    },
    {
        "question": "Qui est titulaire du pouvoir exécutif en France ?",
        "options": ["A) Le Parlement", "B) Le Président de la République et le Gouvernement", "C) Le Conseil d'État", "D) Le Tribunal administratif"],
        "answer": "B",
        "explanation": "Le pouvoir exécutif est exercé par le Président et le Gouvernement, dans le cadre de la Constitution."
    },
    {
        "question": "Qu'est-ce qu'un citoyen ?",
        "options": ["A) Un individu soumis uniquement aux règles fiscales", "B) Un membre d'une communauté politique jouissant de droits et devoirs", "C) Une personne ayant un passeport", "D) Un fonctionnaire"],
        "answer": "B",
        "explanation": "Le citoyen est inscrit dans une communauté politique et bénéficie de droits, avec des devoirs corrélatifs."
    },
    {
        "question": "Quel document fonde les droits fondamentaux en France ?",
        "options": ["A) Le Code civil", "B) La Constitution", "C) Le règlement intérieur", "D) Le code du travail"],
        "answer": "B",
        "explanation": "La Constitution et la Déclaration des droits de l'homme placent les droits fondamentaux au cœur de l'ordre juridique."
    },
    {
        "question": "Que garantit le principe d'égalité ?",
        "options": ["A) Une égalité totale de fortune", "B) Une égalité devant la loi et l'accès aux droits", "C) L'absence de différences sociales", "D) Une égalité des compétences"],
        "answer": "B",
        "explanation": "L'égalité juridique ne signifie pas l'uniformité des situations, mais une même protection devant la loi."
    },
    {
        "question": "Qu'est-ce qu'une institution ?",
        "options": ["A) Un objet de décoration", "B) Une organisation dotée d'un rôle public", "C) Un simple document administratif", "D) Une loi fiscale"],
        "answer": "B",
        "explanation": "Une institution est une structure organisée qui assure un rôle au sein de la société et de l'État."
    },
    {
        "question": "Quel est le rôle du Parlement ?",
        "options": ["A) Dire le droit en dernier ressort", "B) Élaborer et voter les lois", "C) Nommer les maires", "D) Gérer la police"],
        "answer": "B",
        "explanation": "Le Parlement a pour fonction principale la préparation, le vote et le contrôle des lois."
    },
    {
        "question": "Qu'est-ce que la séparation des pouvoirs ?",
        "options": ["A) Un régime où une seule personne détient tous les pouvoirs", "B) Le principe selon lequel le pouvoir exécutif, législatif et judiciaire sont distincts", "C) Un mode d'organisation des partis politiques", "D) La séparation de l'Église et de l'État"],
        "answer": "B",
        "explanation": "La séparation des pouvoirs (Montesquieu) garantit que les pouvoirs législatif, exécutif et judiciaire sont exercés par des organes distincts."
    },
    {
        "question": "Qu'est-ce que le suffrage universel ?",
        "options": ["A) Le droit de vote réservé aux propriétaires", "B) Le droit de vote accordé à tous les citoyens sans condition de fortune", "C) Le droit de vote réservé aux hommes", "D) Le vote au sein des parlements"],
        "answer": "B",
        "explanation": "Le suffrage universel accorde le droit de vote à tous les citoyens majeurs, sans distinction."
    },
    {
        "question": "Qu'est-ce que la présomption d'innocence ?",
        "options": ["A) Toute personne est coupable jusqu'à preuve du contraire", "B) Toute personne est présumée innocente jusqu'à preuve de sa culpabilité", "C) Les accusés n'ont pas droit à un avocat", "D) Les condamnations ne peuvent pas être contestées"],
        "answer": "B",
        "explanation": "La présomption d'innocence est un droit fondamental : nul n'est coupable sans jugement."
    },
    {
        "question": "Qu'est-ce qu'une constitution ?",
        "options": ["A) Un règlement interne d'une entreprise", "B) Un code pénal", "C) La loi fondamentale qui organise l'État et protège les droits fondamentaux", "D) Un traité international"],
        "answer": "C",
        "explanation": "La constitution est la norme suprême d'un État organisant les pouvoirs publics et garantissant les droits fondamentaux."
    },
    {
        "question": "Qu'est-ce que le droit de grève ?",
        "options": ["A) Le droit de refuser de payer des impôts", "B) Le droit pour les travailleurs de cesser le travail pour défendre leurs intérêts", "C) Le droit de manifester contre le gouvernement", "D) Le droit de quitter son emploi"],
        "answer": "B",
        "explanation": "Le droit de grève est un droit constitutionnel permettant aux travailleurs de cesser le travail collectivement."
    },
    {
        "question": "Quel organe détient le pouvoir législatif en Côte d'Ivoire ?",
        "options": ["A) Le gouvernement", "B) L'Assemblée nationale et le Sénat", "C) La Cour suprême", "D) Le Conseil des ministres"],
        "answer": "B",
        "explanation": "Le Parlement ivoirien est bicaméral : il comprend l'Assemblée nationale et le Sénat."
    },
    {
        "question": "Quelle institution ivoirienne contrôle la constitutionnalité des lois ?",
        "options": ["A) Le Tribunal de Première Instance", "B) La Cour d'Appel", "C) Le Conseil constitutionnel", "D) La Cour des Comptes"],
        "answer": "C",
        "explanation": "Le Conseil constitutionnel ivoirien veille à la conformité des lois à la Constitution."
    },
    {
        "question": "Combien de districts compte la Côte d'Ivoire ?",
        "options": ["A) 10", "B) 12", "C) 14", "D) 33"],
        "answer": "C",
        "explanation": "La Côte d'Ivoire compte 14 districts, dont 2 districts autonomes (Abidjan et Yamoussoukro)."
    },
    {
        "question": "Qu'est-ce qu'un référendum ?",
        "options": ["A) Un vote réservé au Parlement", "B) Une procédure par laquelle les citoyens se prononcent directement sur une question", "C) L'élection du Président de la République", "D) Un vote de confiance au gouvernement"],
        "answer": "B",
        "explanation": "Le référendum est un mécanisme de démocratie directe."
    },
    {
        "question": "Qu'est-ce que le Défenseur des droits en France ?",
        "options": ["A) Il défend la France devant les juridictions internationales", "B) Il protège les droits fondamentaux des citoyens face aux administrations", "C) Il gère le budget de l'État", "D) Il nomme les juges"],
        "answer": "B",
        "explanation": "Le Défenseur des droits veille au respect des droits et libertés des citoyens."
    },
    {
        "question": "Qu'est-ce que la séparation des pouvoirs ?",
        "options": ["A) Un régime où une seule personne détient tous les pouvoirs", "B) Le principe selon lequel exécutif, législatif et judiciaire sont distincts", "C) Un mode d'organisation des partis politiques", "D) La séparation de l'Église et de l'État"],
        "answer": "B",
        "explanation": "La séparation des pouvoirs (Montesquieu) garantit que les trois pouvoirs sont exercés par des organes distincts."
    },
    {
        "question": "Qu'est-ce que le suffrage universel ?",
        "options": ["A) Le droit de vote réservé aux propriétaires", "B) Le droit de vote accordé à tous les citoyens sans condition de fortune", "C) Le droit de vote réservé aux hommes", "D) Le vote au sein des parlements"],
        "answer": "B",
        "explanation": "Le suffrage universel accorde le droit de vote à tous les citoyens majeurs, sans distinction."
    },
    {
        "question": "Qu'est-ce que la présomption d'innocence ?",
        "options": ["A) Toute personne est coupable jusqu'à preuve du contraire", "B) Toute personne est présumée innocente jusqu'à preuve de sa culpabilité", "C) Les accusés n'ont pas droit à un avocat", "D) Les condamnations ne peuvent pas être contestées"],
        "answer": "B",
        "explanation": "La présomption d'innocence : nul n'est coupable sans jugement."
    },
    {
        "question": "Qu'est-ce qu'une constitution ?",
        "options": ["A) Un règlement interne d'une entreprise", "B) Un code pénal", "C) La loi fondamentale qui organise l'État et protège les droits fondamentaux", "D) Un traité international"],
        "answer": "C",
        "explanation": "La constitution est la norme suprême d'un État organisant les pouvoirs publics."
    },
    {
        "question": "Qu'est-ce que le droit de grève ?",
        "options": ["A) Le droit de refuser de payer des impôts", "B) Le droit pour les travailleurs de cesser le travail pour défendre leurs intérêts", "C) Le droit de manifester contre le gouvernement", "D) Le droit de quitter son emploi"],
        "answer": "B",
        "explanation": "Le droit de grève est un droit constitutionnel permettant aux travailleurs de cesser le travail collectivement."
    },
    {
        "question": "Quel organe détient le pouvoir législatif en Côte d'Ivoire ?",
        "options": ["A) Le gouvernement", "B) L'Assemblée nationale et le Sénat", "C) La Cour suprême", "D) Le Conseil des ministres"],
        "answer": "B",
        "explanation": "Le Parlement ivoirien est bicaméral : Assemblée nationale et Sénat."
    },
    {
        "question": "Quelle institution ivoirienne contrôle la constitutionnalité des lois ?",
        "options": ["A) Le Tribunal de Première Instance", "B) La Cour d'Appel", "C) Le Conseil constitutionnel", "D) La Cour des Comptes"],
        "answer": "C",
        "explanation": "Le Conseil constitutionnel ivoirien veille à la conformité des lois à la Constitution."
    },
    {
        "question": "Combien de districts compte la Côte d'Ivoire ?",
        "options": ["A) 10", "B) 12", "C) 14", "D) 33"],
        "answer": "C",
        "explanation": "La Côte d'Ivoire compte 14 districts, dont 2 districts autonomes."
    },
    {
        "question": "Qu'est-ce qu'un référendum ?",
        "options": ["A) Un vote réservé au Parlement", "B) Une procédure par laquelle les citoyens se prononcent directement sur une question", "C) L'élection du Président de la République", "D) Un vote de confiance au gouvernement"],
        "answer": "B",
        "explanation": "Le référendum est un mécanisme de démocratie directe."
    },
    {
        "question": "Quel est le rôle du Défenseur des droits ?",
        "options": ["A) Il défend la France devant les juridictions internationales", "B) Il protège les droits fondamentaux des citoyens face aux administrations", "C) Il gère le budget de l'État", "D) Il nomme les juges"],
        "answer": "B",
        "explanation": "Le Défenseur des droits veille au respect des droits et libertés des citoyens face aux administrations."
    },
    {
        "question": "Quelle est la capitale administrative de la Côte d'Ivoire ?",
        "options": ["A) Abidjan", "B) Yamoussoukro", "C) Bouake", "D) San-Pedro"],
        "answer": "B",
        "explanation": "Yamoussoukro est la capitale politique depuis 1983. Abidjan reste la capitale économique."
    },
    {
        "question": "En quelle année la CI a-t-elle accédé à l'indépendance ?",
        "options": ["A) 1958", "B) 1960", "C) 1962", "D) 1956"],
        "answer": "B",
        "explanation": "La CI a proclamé son indépendance le 7 août 1960."
    },
    {
        "question": "Quel est le premier président de la CI ?",
        "options": ["A) Henri Konan Bédié", "B) Laurent Gbagbo", "C) Félix Houphouët-Boigny", "D) Alassane Ouattara"],
        "answer": "C",
        "explanation": "Félix Houphouët-Boigny est le père fondateur et premier président (1960-1993)."
    },
    {
        "question": "Quel organe exerce le contrôle de constitutionnalité en CI ?",
        "options": ["A) La Cour Supr?me", "B) Le Conseil constitutionnel", "C) L'Assemblée nationale", "D) Le Sénat"],
        "answer": "B",
        "explanation": "Le Conseil constitutionnel ivoirien veille à la conformité des lois à la Constitution."
    },
    {
        "question": "Combien de régions compte la CI ?",
        "options": ["A) 19", "B) 26", "C) 31", "D) 33"],
        "answer": "C",
        "explanation": "La CI compte 31 régions et 2 districts autonomes."
    },
    {
        "question": "Quel est le mandat du Président ivoirien ?",
        "options": ["A) 4 ans renouvelable une fois", "B) 5 ans renouvelable une fois", "C) 6 ans renouvelable une fois", "D) 7 ans non renouvelable"],
        "answer": "B",
        "explanation": "La Constitution de 2016 fixe le mandat présidentiel à 5 ans renouvelable une seule fois."
    },
    {
        "question": "Quelle institution vérifie les comptes de l'État en CI ?",
        "options": ["A) Le Ministère des Finances", "B) La Cour des Comptes", "C) L'Assemblée nationale", "D) La BCEAO"],
        "answer": "B",
        "explanation": "La Cour des Comptes vérifie la régularité des comptes publics."
    },
    {
        "question": "Quel est le rôle du CESEC en CI ?",
        "options": ["A) Voter les lois", "B) Conseiller le gouvernement sur les questions économiques et sociales", "C) Contrôler le gouvernement", "D) Administrer les régions"],
        "answer": "B",
        "explanation": "Le Conseil Économique, Social, Environnemental et Culturel est une assemblée consultative."
    },
    {
        "question": "Piège : la CI a-t-elle un régime présidentialiste ou semi-présidentiel ?",
        "options": ["A) Présidentialiste pur", "B) Semi-présidentiel avec cohabitation possible", "C) Présidentiel fort : le Président est chef de l'État et du gouvernement", "D) Parlementaire"],
        "answer": "C",
        "explanation": "La Constitution de 2016 instaure un régime présidentiel fort sans cohabitation."
    },
    {
        "question": "Combien de membres compte le Conseil constitutionnel ivoirien ?",
        "options": ["A) 7", "B) 9", "C) 11", "D) 13"],
        "answer": "B",
        "explanation": "Le Conseil constitutionnel est composé de 9 membres nommés par le Président."
    },
    {
        "question": "La hiérarchie des normes en CI est ?",
        "options": ["A) La loi prévaut sur la Constitution", "B) Les traités sont toujours supérieurs à la Constitution", "C) Constitution > lois organiques > lois ordinaires > règlements", "D) Les arrêtés priment sur les décrets"],
        "answer": "C",
        "explanation": "Hiérarchie : Constitution (2016) > lois organiques > lois ordinaires > décrets > arrêtés."
    },
    {
        "question": "Piège : combien de constitutions la CI a-t-elle eues depuis 1960 ?",
        "options": ["A) 1", "B) 2", "C) 3 : 1960, 2000 et 2016", "D) 4"],
        "answer": "C",
        "explanation": "Trois constitutions : 1960 (indépendance), 2000 (Gbagbo) et 2016 (Ouattara)."
    },
    {
        "question": "Piège : le Sénat de CI peut-il renverser le gouvernement ?",
        "options": ["A) Oui par une motion de censure", "B) Oui en refusant le budget", "C) Non, seule l'Assemblée nationale peut voter une motion de censure", "D) Oui avec l'accord du Conseil constitutionnel"],
        "answer": "C",
        "explanation": "Seule l'Assemblée nationale peut engager la responsabilité du gouvernement."
    },
    {
        "question": "Quelle est la différence entre décret et ordonnance en droit ivoirien ?",
        "options": ["A) Ce sont des synonymes", "B) Le décret est réglementaire ; l'ordonnance est un acte législatif pris après habilitation parlementaire", "C) L'ordonnance est supérieure au décret", "D) Le décret est pris par le Premier ministre"],
        "answer": "B",
        "explanation": "L'ordonnance a valeur législative (habilitation) ; le décret est réglementaire."
    },
    {
        "question": "Quelle est la condition de nationalité pour candidater à la présidentielle ivoirienne ?",
        "options": ["A) Être né en CI", "B) Être ivoirien de naissance sans autre nationalité", "C) Être ivoirien de naissance de père et de mère ivoiriens sans autre nationalité", "D) Être naturalisé depuis 10 ans"],
        "answer": "C",
        "explanation": "Article 55 : nationalité ivoirienne de naissance de père et de mère ivoiriens sans autre nationalité."
    },
    {
        "question": "Piège : un Ivoirien naturalisé étranger peut-il se présenter à la présidentielle ?",
        "options": ["A) Oui s'il renonce avant la candidature", "B) Oui, la double nationalité est tolérée", "C) Non, la Constitution exige de n'avoir jamais eu une autre nationalité", "D) Oui après 10 ans de retour"],
        "answer": "C",
        "explanation": "Article 55 : n'avoir jamais acquis d'autre nationalité. L'acquisition antérieure est rédhibitoire."
    },
    {
        "question": "Qu'est-ce que la CEI en CI ?",
        "options": ["A) Un tribunal électoral", "B) L'organe indépendant chargé d'organiser et superviser les élections", "C) Un parti politique", "D) Un organe de l'ONU"],
        "answer": "B",
        "explanation": "La Commission Électorale Indépendante organise et supervise les élections ivoiriennes."
    },
    {
        "question": "Combien de mandats peut effectuer un président ivoirien ?",
        "options": ["A) Un seul de 7 ans", "B) Deux mandats de 5 ans", "C) Trois mandats de 5 ans", "D) Sans limitation"],
        "answer": "B",
        "explanation": "La Constitution de 2016 limite à deux mandats de 5 ans."
    },
    {
        "question": "Les étrangers résidents peuvent-ils voter en CI ?",
        "options": ["A) Oui pour les élections locales", "B) Oui après 5 ans de résidence", "C) Non, seuls les citoyens ivoiriens peuvent voter", "D) Oui pour les référendums"],
        "answer": "C",
        "explanation": "Le droit de vote est réservé aux seuls citoyens ivoiriens."
    },
    {
        "question": "Quel est le principal produit d'exportation de la CI ?",
        "options": ["A) Le pétrole", "B) Le cacao", "C) Le diamant", "D) Le café"],
        "answer": "B",
        "explanation": "La CI est le premier producteur mondial de cacao (environ 40 % de la production mondiale)."
    },
    {
        "question": "Quelle monnaie est utilisée en CI ?",
        "options": ["A) Le franc ivoirien", "B) Le franc CFA de l'UEMOA (XOF)", "C) L'euro", "D) Le dollar CEDEAO"],
        "answer": "B",
        "explanation": "Le franc CFA de l'Afrique de l'Ouest (XOF) est géré par la BCEAO."
    },
    {
        "question": "Quelle organisation gère le franc CFA des pays de l'UEMOA ?",
        "options": ["A) La Banque mondiale", "B) La BCEAO", "C) La BAD", "D) La Banque de France"],
        "answer": "B",
        "explanation": "La BCEAO (Banque Centrale des États de l'Afrique de l'Ouest) siège à Dakar."
    },
    {
        "question": "En quelle année la Constitution actuelle de la CI a-t-elle été adoptée ?",
        "options": ["A) 2000", "B) 2011", "C) 2016", "D) 2020"],
        "answer": "C",
        "explanation": "La Constitution de 2016 a été adoptée par référendum le 30 octobre 2016."
    },
    {
        "question": "Qu'est-ce que le principe de spécialité d'un établissement public ?",
        "options": ["A) Il peut agir dans n'importe quel domaine", "B) Il est limité à la mission précise pour laquelle il a été créé", "C) Il dépend uniquement du ministre", "D) Il peut voter des lois"],
        "answer": "B",
        "explanation": "Le principe de spécialité limite l'action de l'établissement public à l'objet fixé par ses textes."
    },
    {
        "question": "Piège : qui préside le Conseil supérieur de la magistrature en CI ?",
        "options": ["A) Le Ministre de la Justice", "B) Le Premier Président de la Cour Suprême", "C) Le Président de la République", "D) Le Procureur général"],
        "answer": "C",
        "explanation": "En CI, le CSM est présidé par le Président de la République."
    },
    {
        "question": "Qu'est-ce que le Médiateur de la République en CI ?",
        "options": ["A) Un juge civil", "B) Une autorité indépendante qui reçoit les réclamations des citoyens contre l'administration", "C) Le président de l'Assemblée nationale", "D) Un représentant du gouvernement"],
        "answer": "B",
        "explanation": "Le Médiateur de la République traite les réclamations des citoyens contre les administrations."
    },
    {
        "question": "Qu'est-ce que la distinction SPA et SPIC ?",
        "options": ["A) Aucune différence", "B) SPA = droit administratif ; SPIC = principalement droit privé", "C) SPIC géré par l'État SPA par des privés", "D) SPA génère des profits SPIC non"],
        "answer": "B",
        "explanation": "SPA = droit public. SPIC (eau, électricité) = droit privé pour usagers et personnel."
    },
    {
        "question": "Qu'est-ce que la déconcentration administrative en CI ?",
        "options": ["A) Transfert de compétences à des collectivités autonomes", "B) Déplacement de l'autorité de l'État vers ses représentants locaux (préfets, sous-préfets)", "C) Privatisation des services publics", "D) Suppression des ministères régionaux"],
        "answer": "B",
        "explanation": "La déconcentration déplace des pouvoirs au sein de l'État vers ses agents sur le terrain."
    },
    {
        "question": "Quelle institution forme les hauts fonctionnaires en CI ?",
        "options": ["A) L'ENA", "B) L'Université Félix Houphouët-Boigny", "C) Le Centre de Formation Administrative", "D) La BCEAO"],
        "answer": "A",
        "explanation": "L'ENA de CI forme les hauts fonctionnaires pour les corps préfectoraux, diplomatiques et administratifs."
    },
    {
        "question": "Qu'est-ce qu'un établissement public national (EPN) en CI ?",
        "options": ["A) Une entreprise privée sous contrôle de l'État", "B) Une personne morale de droit public autonome chargée d'une mission de service public", "C) Un ministère", "D) Une collectivité territoriale"],
        "answer": "B",
        "explanation": "Les EPN (ex. CNPS, SODEXAM) sont des personnes morales de droit public autonomes."
    },
    {
        "question": "Qu'est-ce que la LOLF en CI ?",
        "options": ["A) Loi organique relative aux lois de finances", "B) Loi sur les libertés fondamentales", "C) Loi sur le livre foncier", "D) Loi contre la fraude"],
        "answer": "A",
        "explanation": "La LOLF est le cadre juridique de la gestion budgétaire moderne orientée vers la performance."
    },
    {
        "question": "Qu'est-ce que le principe de séparation entre ordonnateur et comptable public ?",
        "options": ["A) Aucun principe en CI", "B) L'agent qui autorise une dépense ne peut pas être celui qui la paie : garantie contre les détournements", "C) Le comptable est supérieur à l'ordonnateur", "D) Ce principe ne s'applique qu'aux grandes villes"],
        "answer": "B",
        "explanation": "Ce principe empêche une même personne d'autoriser et de réaliser une dépense."
    },
    {
        "question": "Combien de langues et dialectes compte la CI ?",
        "options": ["A) 20-30", "B) 60-70", "C) Plus de 60", "D) 10-15"],
        "answer": "C",
        "explanation": "La CI compte plus de 60 langues et dialectes en 4 grands groupes."
    },
    {
        "question": "Quel est le plus grand groupe ethnique en CI ?",
        "options": ["A) Les Baoulé", "B) Les Dioula", "C) Les Bété", "D) Les Sénoufo"],
        "answer": "A",
        "explanation": "Les Baoulé du groupe Akan sont le groupe ethnique le plus important."
    },
    {
        "question": "Qu'est-ce que l'initiative PPTE pour la CI en 2012 ?",
        "options": ["A) Programme de planification économique", "B) Initiative Pays Pauvres Très Endettés : allègement de la dette", "C) Plan de promotion du tourisme", "D) Programme de protection des terres"],
        "answer": "B",
        "explanation": "En 2012, la CI a bénéficié de l'initiative PPTE, obtenant un allègement substantiel de sa dette."
    },
    {
        "question": "Piège : un acte administratif illégalement signé peut-il être validé ?",
        "options": ["A) Oui par ratification expresse de l'autorité compétente", "B) Non, jamais", "C) Oui automatiquement après 3 mois", "D) Non sauf si le Conseil constitutionnel l'approuve"],
        "answer": "A",
        "explanation": "Certains actes irréguliers peuvent être régularisés par ratification expresse."
    },
    {
        "question": "Qu'est-ce que l'ARTCI en CI ?",
        "options": ["A) Un ministère", "B) Une autorité administrative indépendante qui régule les télécommunications et les TIC", "C) Une entreprise publique", "D) Un tribunal spécialisé"],
        "answer": "B",
        "explanation": "L'ARTCI est l'autorité administrative indépendante de régulation du marché des télécommunications."
    },
    {
        "question": "Quel est le nom du processus de décentralisation en CI qui transfère des compétences aux communes ?",
        "options": ["A) La d?concentration", "B) La d?centralisation", "C) La privatisation", "D) La d?l?gation"],
        "answer": "B",
        "explanation": "La décentralisation transfère des compétences et des ressources à des collectivités territoriales autonomes (communes, régions, districts)."
    },
    {
        "question": "Quel est le role d un conseil municipal en CI ?",
        "options": ["A) Gerer les affaires de l'?tat central", "B) Deliberer sur les affaires d interet communal et voter le budget de la commune", "C) Nomrme les prefets", "D) Adopter les lois nationales"],
        "answer": "B",
        "explanation": "Le conseil municipal est l assembl?e deliberante de la commune. Il vote le budget et prend les decisions d interet local."
    },
    {
        "question": "Qu'est-ce que le principe de libre administration des collectivites territoriales en CI ?",
        "options": ["A) Les collectivites peuvent ignorer les lois nationales", "B) Les collectivites gerent librement leurs affaires dans le cadre de la loi sous le controle de l'?tat", "C) Les collectivites peuvent creer leurs propres lois", "D) Les collectivites sont independantes de l'?tat"],
        "answer": "B",
        "explanation": "Le principe de libre administration permet aux collectivites de gerer leurs affaires dans les limites fixees par la loi et sous controle de l'?tat."
    },
    {
        "question": "Quelle est la diff?rence entre un maire et un pr?fet en CI ?",
        "options": ["A) Aucune diff?rence", "B) Le maire est ?lu par les habitants pour g?rer la commune ; le pr?fet est nomm? par l'?tat pour le repr?senter dans le d?partement", "C) Le prefet est superieur au maire en tout", "D) Le maire est nomme par le gouvernement"],
        "answer": "B",
        "explanation": "Le maire est ?lu local ; le pr?fet est agent de l'?tat nomm? par d?cret. Leurs r?les et l?gitimit?s diff?rent."
    },
    {
        "question": "Qu'est-ce qu'un service d?concentr? de l'?tat ?",
        "options": ["A) Un service prive", "B) Un service de l'?tat implant? localement sous l'autorit? d'un repr?sentant de l'?tat (pr?fet, sous-pr?fet)", "C) Un etablissement public", "D) Une collectivit? territoriale"],
        "answer": "B",
        "explanation": "Les services d?concentr?s (DRE, DRSP, etc.) repr?sentent les minist?res au niveau local sous l'autorit? du pr?fet."
    },
    {
        "question": "Qu'est-ce que le contr?le de l?gitimit? dans le cadre de la d?centralisation ?",
        "options": ["A) Le controle exerce par les citoyens sur les elus locaux", "B) Le contr?le exerc? par le repr?sentant de l'?tat sur la l?galit? des actes des collectivit?s locales", "C) Le controle financier des collectivites", "D) L audit annuel des collectivites"],
        "answer": "B",
        "explanation": "Le repr?sentant de l'?tat contr?le que les actes des collectivit?s sont conformes ? la loi."
    },
    {
        "question": "Qu'est-ce que le budget communal en CI ?",
        "options": ["A) Le budget de l'?tat central", "B) Le document financier qui pr?voit les recettes et d?penses de la commune pour l'ann?e", "C) Le budget du departement", "D) Le budget alloue aux fonctionnaires communaux"],
        "answer": "B",
        "explanation": "Le budget communal est vot? par le conseil municipal. Il pr?voit les ressources et les d?penses de la commune."
    },
    {
        "question": "Quel est le financement des collectivites locales en CI ?",
        "options": ["A) Uniquement par l'?tat central", "B) Par les imp?ts locaux, dotations de l'?tat, fonds de d?centralisation et emprunts", "C) Uniquement par les impots locaux", "D) Par les dons internationaux uniquement"],
        "answer": "B",
        "explanation": "Les collectivit?s sont financ?es par une combinaison de ressources propres (imp?ts locaux) et de transferts de l'?tat."
    },
    {
        "question": "Qu'est-ce que l'?tat civil en CI ?",
        "options": ["A) Le registre des entreprises", "B) L'enregistrement des faits d'?tat civil (naissances, mariages, d?c?s) qui ?tablit l'identit? juridique des personnes", "C) Le registre des fonctionnaires", "D) La liste electorale"],
        "answer": "B",
        "explanation": "L'?tat civil enregistre les ?v?nements majeurs de la vie (naissances, mariages, d?c?s) et ?tablit l'identit? juridique."
    },
    {
        "question": "Qu'est-ce que le Tr?sor public en CI ?",
        "options": ["A) La banque centrale", "B) Le service de l'?tat qui g?re les finances publiques : encaissement des recettes et paiement des d?penses", "C) Un organisme prive", "D) La banque du gouvernement"],
        "answer": "B",
        "explanation": "Le Tr?sor public g?re les flux financiers de l'?tat : recettes fiscales, paiement des salaires, remboursement de la dette."
    },
    {
        "question": "Pi?ge : la Constitution de 2016 a-t-elle supprim? le poste de Premier ministre en CI ?",
        "options": ["A) Oui d?finitivement", "B) Non le poste existe toujours mais ses attributions sont encadr?es par l'organisation institutionnelle", "C) Oui mais il peut etre r?tabli par loi organique", "D) Non le Premier ministre reste chef du gouvernement"],
        "answer": "B",
        "explanation": "La Constitution de 2016 n'a pas supprimé le poste de Premier ministre ; elle a réorganisé l'exécutif et ses équilibres."
    },
    {
        "question": "Qu'est-ce que la responsabilit? politique du gouvernement en CI ?",
        "options": ["A) Le gouvernement est responsable devant le Pr?sident uniquement", "B) Le gouvernement est responsable devant l'Assembl?e nationale qui peut le renverser par une motion de censure", "C) Le gouvernement est irresponsable", "D) Le gouvernement est responsable devant le Senat"],
        "answer": "B",
        "explanation": "L'Assembl?e nationale peut engager la responsabilit? du gouvernement par une motion de censure."
    },
    {
        "question": "Pi?ge : le contr?le parlementaire s'exerce-t-il sur les actes du Pr?sident en CI ?",
        "options": ["A) Oui pleinement comme en r?gime semi-pr?sidentiel", "B) Non en r?gime pr?sidentiel le Pr?sident n est pas responsable devant le Parlement", "C) Oui uniquement sur les questions budg?taires", "D) Non le Parlement ne peut pas questionner le gouvernement"],
        "answer": "B",
        "explanation": "En r?gime pr?sidentiel ivoirien le Pr?sident n est pas responsable devant le Parlement. Seul le gouvernement l est."
    },
    {
        "question": "Qu'est-ce que le principe de l inamovibilite des magistrats en CI ?",
        "options": ["A) Les magistrats ne peuvent pas etre mutes", "B) Les magistrats du siege ne peuvent pas etre deplactes sanctionnes ou destitues sans leur consentement ou une procedure disciplinaire", "C) Les magistrats ne peuvent pas demissionner", "D) Les magistrats sont nommes a vie"],
        "answer": "B",
        "explanation": "L inamovibilite protege les magistrats du siege contre toute pression : ils ne peuvent etre mutas ou sanctionnes que par procedure disciplinaire."
    },
    {
        "question": "Qu'est-ce que la citoyennete ivoirienne confere comme droits politiques ?",
        "options": ["A) Uniquement le droit de vote", "B) Le droit de vote d eligibilite de petition d acces aux fonctions publiques et d exercice des libert?s civiques", "C) Uniquement le droit d acces aux fonctions publiques", "D) Aucun droit politique pour les citoyens ordinaires"],
        "answer": "B",
        "explanation": "La citoyennete ivoirienne confere l ensemble des droits politiques : vote eligibilite libert?s civiques acces aux fonctions publiques."
    },
    {
        "question": "Qu'est-ce que le droit d asile en CI ?",
        "options": ["A) Le droit pour un Ivoirien de quitter le pays", "B) La protection accordee a un ?tranger persecute dans son pays qui en fait la demande", "C) Le droit de refugier des biens a l ?tranger", "D) L exemption d impots pour les diplomates"],
        "answer": "B",
        "explanation": "Le droit d asile accorde une protection a tout ?tranger qui fuit des persecutions dans son pays d origine."
    },
    {
        "question": "Pi?ge : la peine de mort est-elle abolie en CI ?",
        "options": ["A) Oui depuis la Constitution de 2016", "B) Non elle est toujours en vigueur pour les crimes les plus graves", "C) Oui depuis 2000", "D) Oui depuis 1960"],
        "answer": "A",
        "explanation": "La Constitution de 2016 a aboli la peine de mort en CI. C est une avancee majeure des droits fondamentaux."
    },
    {
        "question": "Qu'est-ce que le Parlement ivoirien en mati?re de contr?le du gouvernement ?",
        "options": ["A) Il ne dispose d'aucun pouvoir de contr?le", "B) Il exerce un contr?le par les questions orales et ?crites, commissions d'enqu?te et motion de censure", "C) Il peut dissoudre le gouvernement ? tout moment", "D) Il peut refuser d appliquer les lois pr?sidentielles"],
        "answer": "B",
        "explanation": "Le Parlement ivoirien contr?le le gouvernement par les questions, les commissions et la motion de censure."
    },
    {
        "question": "Quel est le principe de la neutralite du service public ?",
        "options": ["A) Le service public doit etre gratuit", "B) Le service public ne doit pas etre influence par des considerations politiques religieuses ou ideologiques", "C) Le service public ne peut pas sous-traiter", "D) Le service public doit etre gere par des fonctionnaires uniquement"],
        "answer": "B",
        "explanation": "La neutralite du service public garantit que les agents traitent tous les usagers de facon egale sans discrimination."
    },
    {
        "question": "Pi?ge : un fonctionnaire peut-il militer pour un parti politique en CI ?",
        "options": ["A) Oui totalement sans restriction", "B) Non un fonctionnaire doit se garder de tout engagement politique ostensible dans l exercice de ses fonctions", "C) Oui mais uniquement apres les heures de service", "D) Non aucun fonctionnaire ne peut voter"],
        "answer": "B",
        "explanation": "Le devoir de reserve interdit au fonctionnaire de manifester ostensiblement ses opinions politiques dans l exercice de ses fonctions."
    },
    {
        "question": "Qu'est-ce que la notion d autorite de l'?tat ?",
        "options": ["A) La capacite de l'?tat a emettre des billets de banque", "B) La capacite de l'?tat a imposer le respect de l ordre juridique et a faire executer ses decisions en recourant si necessaire a la contrainte", "C) La capacite de l'?tat a conclure des traites", "D) La capacite de l'?tat a lever des impots"],
        "answer": "B",
        "explanation": "L autorite de l'?tat est sa capacite a maintenir l ordre et a faire respecter la loi en utilisant si necessaire la force legitime."
    },
    {
        "question": "Qu'est-ce que la nationalit? ivoirienne par naissance ?",
        "options": ["A) ?tre n? en CI", "B) ?tre n? de p?re ou de m?re ivoirien(ne)", "C) ?tre n? en CI ou d'un parent ivoirien sous conditions", "D) Uniquement ?tre n? de deux parents ivoiriens"],
        "answer": "C",
        "explanation": "La nationalit? ivoirienne par naissance est attribu?e ? ceux n?s en CI dans certaines conditions ou n?s d'un parent ivoirien."
    },
    {
        "question": "Pi?ge : une personne doublement nationale peut-elle obtenir le statut de refugie en CI ?",
        "options": ["A) Non un national CI ne peut pas etre refugie en CI", "B) Oui si elle prouve la persecution dans son autre pays", "C) Non les doubles nationaux n ont aucun droit au refuge", "D) Oui automatiquement"],
        "answer": "A",
        "explanation": "Un citoyen ivoirien ne peut pas demander le statut de refugie en CI. Le droit d asile protege les ?trangers dans un pays dont ils ne sont pas ressortissants."
    },
    {
        "question": "Quelle est la duree de la session parlementaire ordinaire en CI ?",
        "options": ["A) 3 mois par an", "B) 6 mois par an en deux sessions", "C) Permanente", "D) 9 mois par an"],
        "answer": "B",
        "explanation": "Le Parlement ivoirien se reunit en deux sessions ordinaires de 3 mois chacune soit 6 mois au total."
    },
    {
        "question": "Pi?ge : les actes du Pr?sident de la R?publique sont-ils soumis au contr?le du juge administratif ?",
        "options": ["A) Oui pleinement", "B) Non les actes de gouvernement (li?s ? la politique) ?chappent au contr?le juridictionnel mais les actes r?glementaires peuvent ?tre contr?l?s", "C) Non aucun acte pr?sidentiel n'est contr?lable", "D) Oui mais uniquement par le Conseil constitutionnel"],
        "answer": "B",
        "explanation": "Les actes de gouvernement (ex. trait?s, relations diplomatiques) ?chappent au juge administratif. Seuls les actes r?glementaires peuvent ?tre attaqu?s."
    },
    {
        "question": "Qu'est-ce que le principe d egalite devant le service public ?",
        "options": ["A) Tout le monde paye le meme prix", "B) Tous les usagers dans la meme situation doivent etre traites identiquement par le service public", "C) Tous les services publics sont gratuits", "D) Les fonctionnaires et les usagers ont les memes droits"],
        "answer": "B",
        "explanation": "L egalite devant le service public est une application du principe general d egalite : meme traitement pour les usagers dans des situations identiques."
    },
    {
        "question": "Quelle est la difference entre une commune de plein exercice et une commune de moyen exercice en CI ?",
        "options": ["A) La taille de la population", "B) Le niveau d autonomie et de competences : une commune de plein exercice dispose d une autonomie plus grande", "C) La localisation geographique", "D) Le montant du budget"],
        "answer": "B",
        "explanation": "En CI les communes sont classees selon leur niveau d autonomie. Les communes de plein exercice ont plus de competences et de ressources."
    },
    {
        "question": "Qu'est-ce que le principe de neutralite religieuse dans la fonction publique ivoirienne ?",
        "options": ["A) Les fonctionnaires ne peuvent pas pratiquer une religion", "B) Les fonctionnaires ne peuvent pas manifester leurs convictions religieuses dans l exercice de leurs fonctions", "C) Les fonctionnaires doivent etre atheistes", "D) La religion est interdite dans les locaux administratifs"],
        "answer": "B",
        "explanation": "La neutralite religieuse interdit aux fonctionnaires d exprimer leurs convictions religieuses dans l exercice de leurs fonctions."
    },
    {
        "question": "Qu'est-ce que le principe de gratuite du service public ?",
        "options": ["A) Tous les services publics sont gratuits", "B) Ce principe signifie que le financement du service public ne doit pas reposer uniquement sur les usagers : il peut etre finance par les impots", "C) Les usagers ne paient jamais pour les services publics", "D) Les fonctionnaires travaillent benevoles"],
        "answer": "B",
        "explanation": "La gratuite du service public ne signifie pas absence de paiement mais que le service est accessible sans que le prix soit un obstacle dirimant."
    },
    {
        "question": "Quelle est la distinction entre le prefet et le gouverneur en CI ?",
        "options": ["A) Aucune diff?rence", "B) En CI depuis 2011 le gouverneur dirige le district autonome (Abidjan Yamoussoukro) tandis que le prefet dirige le departement", "C) Le gouverneur est un role historique supprime", "D) Le gouverneur est elu le prefet nomme"],
        "answer": "B",
        "explanation": "La Constitution de 2011-2016 a cree des districts autonomes diriges par des gouverneurs nommes par le Pr?sident pour les grandes agglomerations."
    },
    {
        "question": "Qu'est-ce que la delegation de signature ?",
        "options": ["A) Un fonctionnaire signe a la place d un autre sans habilitation", "B) Une autorite administrative autorise un de ses subordonnes a signer en son nom certains actes", "C) Le Pr?sident deleguant ses pouvoirs au Premier ministre", "D) L Assemblee nationale delegant ses pouvoirs au gouvernement"],
        "answer": "B",
        "explanation": "La d?l?gation de signature permet a un chef de service d autoriser son subordonné a signer certains actes en son nom. Le deleguant reste responsable."
    },
    {
        "question": "Pi?ge : la delegation de pouvoirs est-elle differente de la delegation de signature ?",
        "options": ["A) Non ce sont des synonymes", "B) Oui : dans la delegation de pouvoirs le delegataire exerce le pouvoir en son nom propre et le delegant ne peut plus l exercer ; dans la delegation de signature le delegant reste responsable", "C) Oui : la delegation de pouvoirs est illegale", "D) Non elles ont les memes effets juridiques"],
        "answer": "B",
        "explanation": "Delegation de pouvoirs : transfert du pouvoir lui-meme (le delegant ne peut plus exercer). Delegation de signature : seule la signature est transferee le delegant reste responsable."
    }
]

# THÈME 7 : Droit administratif
THEME_7 = [
    {
        "question": "Quelle est la source historique du droit administratif français ?",
        "options": ["A) L'arrêt Blanco", "B) Le droit civil", "C) Le Code pénal", "D) La Constitution de 1848"],
        "answer": "A",
        "explanation": "L'arrêt Blanco (1873) fonde la spécificité du droit administratif français et la responsabilité de l'État."
    },
    {
        "question": "Quelle juridiction est la plus haute dans l'ordre administratif français ?",
        "options": ["A) Le tribunal judiciaire", "B) Le Conseil d'État", "C) La Cour de cassation", "D) Le tribunal de commerce"],
        "answer": "B",
        "explanation": "Le Conseil d'État est la juridiction suprême de l'ordre administratif en France."
    },
    {
        "question": "Quel principe signifie que l'administration doit agir dans le cadre de la loi ?",
        "options": ["A) Le principe de légalité", "B) Le principe de gratuité", "C) Le principe de hiérarchie", "D) Le principe d'efficacité"],
        "answer": "A",
        "explanation": "Le principe de légalité impose à l'administration d'agir conformément à la loi et à la Constitution."
    },
    {
        "question": "Qu'est-ce qu'une personne publique ?",
        "options": ["A) Un individu privé", "B) Un organisme de droit public exerçant une mission d'intérêt général", "C) Une entreprise commerciale", "D) Une association de loisirs"],
        "answer": "B",
        "explanation": "Les personnes publiques (État, collectivités, établissements publics) sont à la base de l'organisation administrative."
    },
    {
        "question": "Quel est le rôle du préfet ?",
        "options": ["A) Représenter le gouvernement dans le département", "B) Gérer uniquement les impôts", "C) Juger les litiges privés", "D) Diriger les tribunaux administratifs"],
        "answer": "A",
        "explanation": "Le préfet représente l'État au niveau départemental et assure le contrôle administratif."
    },
    {
        "question": "Que signifie le principe de non-rétroactivité de la loi pénale ?",
        "options": ["A) Une loi nouvelle ne peut pas s'appliquer rétroactivement", "B) Une loi ne s'applique qu'après son vote", "C) Une loi peut toujours être appliquée avec effet immédiat", "D) Une loi ne s'applique jamais aux personnes publiques"],
        "answer": "A",
        "explanation": "Le principe de non-rétroactivité est un principe fondamental du droit, surtout en matière pénale."
    },
    {
        "question": "Quel acte administratif est généralement pris par le pouvoir exécutif pour un cas particulier ?",
        "options": ["A) La norme générale", "B) L'acte individuel", "C) Le contrat privé", "D) Le code civil"],
        "answer": "B",
        "explanation": "Un acte individuel vise un cas particulier, par exemple une nomination, une autorisation ou une sanction."
    },
    {
        "question": "Qu'est-ce que le contrôle de légalité ?",
        "options": ["A) Le contrôle de la moralité des agents", "B) Le contrôle de la conformité d'un acte à la loi", "C) Le contrôle de la qualité des produits", "D) Le contrôle du budget privé"],
        "answer": "B",
        "explanation": "Le contrôle de légalité consiste à vérifier si un acte administratif est conforme aux normes supérieures."
    },
    {
        "question": "Qui est le gardien du droit administratif en France ?",
        "options": ["A) La Cour de cassation", "B) Le Conseil d'État", "C) Le ministère de la Justice", "D) Le Tribunal de grande instance"],
        "answer": "B",
        "explanation": "Le Conseil d'État a une place centrale dans l'interprétation et le développement du droit administratif."
    },
    {
        "question": "Que signifie le principe de sécurité juridique ?",
        "options": ["A) L'État peut agir sans limites", "B) Les citoyens doivent pouvoir connaître les règles et leurs conséquences", "C) La loi ne s'applique qu'aux entreprises", "D) L'administration ne doit jamais expliquer ses décisions"],
        "answer": "B",
        "explanation": "La sécurité juridique garantit la prévisibilité du droit et la protection contre l'arbitraire."
    },
    {
        "question": "Qu'est-ce que le service public selon le droit administratif ?",
        "options": ["A) Toute entreprise commerciale", "B) Une activite d interet general assuree ou controlee par la puissance publique", "C) Un service rendu uniquement aux fonctionnaires", "D) Un tribunal administratif"],
        "answer": "B",
        "explanation": "Le service public est une activite d interet general prise en charge par une personne publique."
    },
    {
        "question": "Quel principe du service public signifie qu il doit fonctionner sans interruption ?",
        "options": ["A) Le principe de mutabilite", "B) Le principe de continuite", "C) Le principe d egalite", "D) Le principe de neutralite"],
        "answer": "B",
        "explanation": "La continuite du service public impose que le service ne soit pas interrompu."
    },
    {
        "question": "Quel principe du service public impose son adaptation aux besoins de la societe ?",
        "options": ["A) La neutralite", "B) L egalite", "C) La mutabilite", "D) La gratuite"],
        "answer": "C",
        "explanation": "Le principe de mutabilite oblige le service public a evoluer en fonction des besoins."
    },
    {
        "question": "Qu'est-ce qu un etablissement public ?",
        "options": ["A) Une entreprise privee", "B) Une personne morale de droit public chargee d une mission de service public", "C) Un tribunal administratif", "D) Un service deconcentre"],
        "answer": "B",
        "explanation": "Un etablissement public est une personne morale de droit public gerant une mission de service public."
    },
    {
        "question": "Quelle est la difference entre d?concentration et d?centralisation ?",
        "options": ["A) Aucune", "B) La d?concentration transfere des pouvoirs a des agents de l'?tat, la d?centralisation a des collectivites autonomes", "C) La d?centralisation est au profit des agents de l'?tat", "D) La d?concentration concerne uniquement les communes"],
        "answer": "B",
        "explanation": "La d?concentration deplace des competences au sein de l'?tat, la d?centralisation les transfere a des entites distinctes."
    },
    {
        "question": "Qu'est-ce qu un recours pour exces de pouvoir ?",
        "options": ["A) Un recours visant a obtenir une indemnite", "B) Un recours en annulation d un acte administratif illegal", "C) Un recours contre les decisions judiciaires", "D) Un recours en interpr?tation"],
        "answer": "B",
        "explanation": "Le recours pour exces de pouvoir permet l annulation d un acte administratif illegal."
    },
    {
        "question": "Qu'est-ce que la hi?rarchie des normes ?",
        "options": ["A) L organisation des minist?res", "B) L organisation pyramidale des regles juridiques, avec la Constitution au sommet", "C) Le classement des juges par anciennete", "D) L ordre alphabetique des lois"],
        "answer": "B",
        "explanation": "La hi?rarchie des normes place la Constitution au sommet, suivie des traites, des lois et des r?glements."
    },
    {
        "question": "Qu'est-ce que la responsabilite sans faute de l'?tat ?",
        "options": ["A) L ?tat ne peut jamais etre condamne", "B) L ?tat peut etre condamne a indemniser meme sans avoir commis de faute", "C) La responsabilite personnelle des fonctionnaires", "D) L ?tat est responsable uniquement des accidents"],
        "answer": "B",
        "explanation": "La responsabilite sans faute repose sur le principe d egalite devant les charges publiques."
    },
    {
        "question": "Qu'est-ce qu un acte unilateral de l administration ?",
        "options": ["A) Un acte signe par deux parties", "B) Un acte par lequel l administration cree des obligations sans le consentement du destinataire", "C) Un contrat administratif", "D) Une loi votee par le Parlement"],
        "answer": "B",
        "explanation": "L acte unilateral est pris par l administration seule et s impose aux administres sans leur consentement."
    },
    {
        "question": "Qu'est-ce qu un contrat administratif ?",
        "options": ["A) Un contrat entre deux entreprises privees", "B) Un contrat conclu par une personne publique dans le cadre d une mission de service public", "C) Un acte unilateral de l administration", "D) Un accord entre deux ?tats"],
        "answer": "B",
        "explanation": "Le contrat administratif implique au moins une personne publique et presente des clauses exorbitantes du droit commun."
    },
    {
        "question": "Quelle est la procedure de revision constitutionnelle en CI ?",
        "options": ["A) Uniquement par r?f?rendum", "B) Par le Parlement seul a la majorite simple", "C) Par le Parlement a la majorite des 3/5 ou par r?f?rendum a l initiative du Pr?sident", "D) Par le Conseil constitutionnel"],
        "answer": "C",
        "explanation": "La revision peut etre adoptee par le Parlement (3/5) ou soumise a r?f?rendum."
    },
    {
        "question": "Qu'est-ce qu une loi organique en droit ivoirien ?",
        "options": ["A) Une loi votee par r?f?rendum", "B) Une loi qui precise la Constitution dans les domaines qu elle designe expressement", "C) Une loi adoptee a l unanimite", "D) Un decret du Pr?sident"],
        "answer": "B",
        "explanation": "Les lois organiques completent la Constitution et sont superieures aux lois ordinaires."
    },
    {
        "question": "Pi?ge : le preambule de la Constitution de 2016 a-t-il une valeur juridique ?",
        "options": ["A) Non c est un simple texte declaratoire", "B) Oui il fait partie du bloc de constitutionnalit?", "C) Non seul le corps de la Constitution a force contraignante", "D) Oui mais uniquement pour les lois penales"],
        "answer": "B",
        "explanation": "Le preambule est integre au bloc de constitutionnalit? et peut servir de base a la censure d une loi."
    },
    {
        "question": "Qu'est-ce que le principe de non-retroactivite des actes administratifs ?",
        "options": ["A) Un acte ne peut pas etre abroge", "B) Un acte administratif ne peut produire d effets que pour l avenir pas pour le passe", "C) Les actes s appliquent uniquement aux ?trangers", "D) Les r?glements ne s appliquent qu au moment de leur signature"],
        "answer": "B",
        "explanation": "L acte administratif prend effet a sa publication. Il ne peut pas s appliquer retroactivement."
    },
    {
        "question": "Qu'est-ce que le principe du contradictoire en procedure administrative ?",
        "options": ["A) L administration peut decider sans informer l administre", "B) Avant toute decision defavorable l administre doit pouvoir presenter ses observations", "C) L administre peut contredire toutes les decisions", "D) Les fonctionnaires peuvent refuser les ordres"],
        "answer": "B",
        "explanation": "Garantie fondamentale : avant toute decision qui lui fait grief l administre doit pouvoir s expliquer."
    },
    {
        "question": "Quelle est la difference entre recours gracieux et recours hierarchique ?",
        "options": ["A) Ce sont des synonymes", "B) Recours gracieux adresse a l auteur de l acte ; recours hierarchique adresse au superieur", "C) Le recours gracieux va devant un juge", "D) Le hierarchique est plus rapide"],
        "answer": "B",
        "explanation": "Gracieux : on demande a l auteur de retirer son acte. Hierarchique : on demande a son superieur de l annuler."
    },
    {
        "question": "Qu'est-ce que l exception d illegalite en droit administratif ?",
        "options": ["A) Impossibilite d attaquer un acte apres 2 mois", "B) La possibilite de soulever l illegalite d un acte r?glementaire de facon incidente lors d un litige meme hors delai de recours", "C) L annulation automatique de tout acte illegal", "D) Un recours special devant le Conseil constitutionnel"],
        "answer": "B",
        "explanation": "L exception d illegalite est imprescriptible pour les actes r?glementaires."
    },
    {
        "question": "Qu'est-ce que le pouvoir discrecionnaire de l administration ?",
        "options": ["A) Le droit d agir en dehors de la loi", "B) La liberte de choix dont dispose l administration dans les limites fixees par la loi", "C) Le droit de ne pas repondre aux requetes", "D) La possibilite d ignorer les jugements"],
        "answer": "B",
        "explanation": "Le pouvoir discrecionnaire permet de choisir comment agir dans un cadre legal."
    },
    {
        "question": "Quelles sont les trois lois de Rolland du service public ?",
        "options": ["A) Gratuite impartialite efficacite", "B) Continuite egalite mutabilite", "C) Rapidite transparence accessibilite", "D) Neutralite gratuite universalite"],
        "answer": "B",
        "explanation": "Lois de Rolland : continuite (pas d interruption) egalite (traitement egaux) mutabilite (adaptation aux besoins)."
    },
    {
        "question": "Pi?ge : le service public peut-il etre gere par une personne privee ?",
        "options": ["A) Non seul l'?tat peut gerer un service public", "B) Oui via la delegation de service public (concession affermage)", "C) Oui mais uniquement les services industriels", "D) Non c est inconstitutionnel"],
        "answer": "B",
        "explanation": "La d?l?gation de service public permet de confier la gestion a un prive."
    },
    {
        "question": "Qu'est-ce qu un contrat de concession de service public ?",
        "options": ["A) Un contrat de travail d un fonctionnaire", "B) Un contrat par lequel une personne publique confie a un prive la gestion d un service public a ses risques et perils", "C) Un accord international", "D) Un marche public de fournitures"],
        "answer": "B",
        "explanation": "Le concessionnaire est remunere par les usagers et assume le risque d exploitation."
    },
    {
        "question": "Quelle est la distinction fondamentale entre marche public et delegation de service public ?",
        "options": ["A) Aucune distinction", "B) Marche public : remuneration par l administration ; delegation : remuneration par les usagers ou les resultats", "C) Marche public = travaux delegation = services", "D) La d?l?gation s applique uniquement aux communes"],
        "answer": "B",
        "explanation": "La difference : le mode de remuneration et le transfert du risque d exploitation."
    },
    {
        "question": "Qu'est-ce que l IGE en CI ?",
        "options": ["A) Un tribunal administratif", "B) Un corps de controle charge d inspecter les services de l'?tat et de lutter contre la corruption", "C) Le service de securite de la presidence", "D) Un organe de l Assemblee nationale"],
        "answer": "B",
        "explanation": "L Inspection Generale d ?tat placee aupres du Pr?sident controle l utilisation des ressources publiques."
    },
    {
        "question": "Qu'est-ce que la titularisation dans la fonction publique ivoirienne ?",
        "options": ["A) Le recrutement initial", "B) La confirmation definitive du statut de fonctionnaire apres la periode de stage", "C) La promotion a un grade superieur", "D) La mutation vers une autre administration"],
        "answer": "B",
        "explanation": "La titularisation met fin au statut de stagiaire et confere le statut definitif de fonctionnaire."
    },
    {
        "question": "Pi?ge : un fonctionnaire peut-il refuser d obeir a un ordre manifestement illegal ?",
        "options": ["A) Non l obeissance hierarchique est absolue", "B) Oui il peut et doit refuser un ordre manifestement illegal comprometant serieusement un interet public", "C) Oui mais uniquement avec accord du syndicat", "D) Non il doit obeir et signaler apres"],
        "answer": "B",
        "explanation": "Le devoir de refuser un ordre manifestement illegal est un principe fondamental de la deontologie fonctionnaire."
    },
    {
        "question": "Qu'est-ce que la disponibilite dans la fonction publique ivoirienne ?",
        "options": ["A) La periode de conge annuel", "B) La position ou un fonctionnaire cesse temporairement ses fonctions sans perdre son statut", "C) Le droit au teletravail", "D) Une sanction disciplinaire"],
        "answer": "B",
        "explanation": "La disponibilite est une position administrative temporaire sans remuneration de l'?tat."
    },
    {
        "question": "Qu'est-ce que le detachement dans la fonction publique ?",
        "options": ["A) La mise a la retraite anticipee", "B) La position du fonctionnaire qui exerce dans une autre administration en conservant ses droits dans son corps d origine", "C) Une mutation definitive", "D) Un conge pour raisons personnelles"],
        "answer": "B",
        "explanation": "Le detachement : exercice temporaire ailleurs avec conservation des droits dans le corps d origine."
    },
    {
        "question": "Pi?ge tres difficile : un acte nul et un acte inexistant sont-ils identiques ?",
        "options": ["A) Oui synonymes", "B) Non : l acte nul a une apparence juridique et doit etre annule ; l acte inexistant n a aucune valeur et peut etre ignore", "C) Oui memes effets juridiques", "D) Non l acte inexistant entraine des sanctions penales"],
        "answer": "B",
        "explanation": "Acte nul : existe juridiquement mais vicie doit etre annule. Acte inexistant : aucune realite juridique."
    },
    {
        "question": "Qu'est-ce que le recours en cassation devant la chambre administrative de la Cour Supr?me ?",
        "options": ["A) Un appel qui rejuge les faits", "B) Un recours qui controle uniquement la legalite de la decision sans reexaminer les faits", "C) Un recours reserve aux ?trangers", "D) Un recours en responsabilite de l'?tat"],
        "answer": "B",
        "explanation": "La cassation verifie que la loi a ete correctement appliquee sans rejuger les faits."
    },
    {
        "question": "Qu'est-ce que le principe de proportionnalite dans l action administrative ?",
        "options": ["A) L administration traite les fonctionnaires proportionnellement a leur salaire", "B) Les mesures de l administration doivent etre adaptees et proportionnees a l objectif poursuivi", "C) Les taxes sont proportionnelles aux revenus", "D) Les sanctions sont proportionnelles au grade"],
        "answer": "B",
        "explanation": "La proportionnalite empeche les mesures excessives par rapport au but recherche."
    },
    {
        "question": "Qu'est-ce que le detournement de pouvoir en droit administratif ?",
        "options": ["A) Utiliser un droit dans un but autre que celui pour lequel il a ete accorde", "B) Refuser d appliquer la loi", "C) Depasser son budget", "D) Utiliser un droit legal de facon financierement abusive"],
        "answer": "A",
        "explanation": "Detournement de pouvoir : une autorite utilise un pouvoir legal a des fins autres que celles prevues."
    },
    {
        "question": "Pi?ge : la force majeure exonere-t-elle toujours l'?tat de sa responsabilite ?",
        "options": ["A) Oui toujours et totalement", "B) Non l'?tat reste responsable pour certains services dangereux meme en cas de force majeure", "C) Oui si l evenement est imprevisible et irresistible", "D) Non la force majeure n existe pas en droit administratif"],
        "answer": "B",
        "explanation": "Pour les activites dangereuses la responsabilite sans faute peut subsister meme en cas de force majeure."
    },
    {
        "question": "Qu'est-ce que le principe de continuite de l'?tat ?",
        "options": ["A) L ?tat dure indefiniment et ses engagements subsistent au-dela des gouvernements successifs", "B) Le Pr?sident ne peut pas demissionner", "C) Les lois ne peuvent pas etre abrogees", "D) Les fonctionnaires restent en poste independamment des ?lections"],
        "answer": "A",
        "explanation": "La continuite de l'?tat : ses engagements juridiques et financiers subsistent malgre les changements de gouvernement."
    },
    {
        "question": "Qu'est-ce que la faute personnelle detachable du service ?",
        "options": ["A) Un fonctionnaire ne peut jamais etre poursuivi penalement", "B) La faute grave qui revele un comportement incompatible avec les obligations du service exposant le fonctionnaire a des poursuites", "C) Seul le ministre peut etre poursuivi", "D) La faute personnelle engage l'?tat"],
        "answer": "B",
        "explanation": "La faute personnelle detachable engage la responsabilite personnelle du fonctionnaire (ex corruption violence deliberee)."
    },
    {
        "question": "Pi?ge : l annulation d un acte administratif par le juge a-t-elle un effet retroactif ?",
        "options": ["A) Non l annulation ne vaut que pour l avenir", "B) Oui l annulation a un effet retroactif : l acte est cense n avoir jamais existe", "C) Oui mais seulement pour les actes individuels", "D) Non sauf si le juge le decide expressement"],
        "answer": "B",
        "explanation": "L annulation par le juge administratif a un effet retroactif (ex tunc) : l acte est cense n avoir jamais produit d effets."
    },
    {
        "question": "Qu'est-ce que le principe d egalite de traitement dans la fonction publique ?",
        "options": ["A) Tous les fonctionnaires ont le meme salaire", "B) Des agents dans des situations identiques doivent etre traites de maniere identique sans discrimination", "C) Le meme travail est effectue par le meme nombre d agents", "D) Tous les grades sont equivalents"],
        "answer": "B",
        "explanation": "Le principe d egalite de traitement interdit toute discrimination dans la gestion des carrieres."
    },
    {
        "question": "Qu'est-ce que le controle de legalite interne d un acte administratif ?",
        "options": ["A) Verifier la signature", "B) Verifier le fond : le but les motifs de droit et de fait et l objet de l acte", "C) Verifier si l acte a ete publie", "D) Verifier la competence de l auteur"],
        "answer": "B",
        "explanation": "Le controle interne porte sur le fond : but motifs de droit motifs de fait contenu."
    },
    {
        "question": "Qu'est-ce que le pouvoir de tutelle administrative en CI ?",
        "options": ["A) La supervision des orphelins", "B) Le controle exerce par l'?tat sur les collectivites locales et EPN pour garantir la legalite", "C) La supervision des entreprises ?trangeres", "D) Le controle du Pr?sident sur les ministres"],
        "answer": "B",
        "explanation": "La tutelle administrative permet a l'?tat de controler les actes des collectivites locales et EPN."
    },
    {
        "question": "Pi?ge : un fonctionnaire detache peut-il etre discipline par son administration d accueil ET son corps d origine ?",
        "options": ["A) Non seule l administration d accueil est competente", "B) Non seul le corps d origine l est", "C) Oui : administration d accueil pour fautes liees au poste ; corps d origine pour manquements au statut", "D) Oui les deux peuvent sanctionner pour les memes faits"],
        "answer": "C",
        "explanation": "La discipline en detachement est partagee selon la nature de la faute."
    },
    {
        "question": "Qu'est-ce que la responsabilite de l'?tat du fait des lois ?",
        "options": ["A) L ?tat ne peut jamais etre condamne pour une loi", "B) Une loi ne peut pas engager la responsabilite de l'?tat", "C) L ?tat peut etre condamne si une loi cause un prejudice anormal et special meme si elle est legale", "D) Seul le Parlement est responsable des lois"],
        "answer": "C",
        "explanation": "Responsabilite sans faute du legislateur : meme une loi valide peut creer une rupture d egalite devant les charges publiques."
    },
    {
        "question": "Qu'est-ce que le principe de bonne foi dans l administration publique ?",
        "options": ["A) Les agents doivent etre de confession chretienne", "B) L administration doit agir avec loyaute et sincerite dans ses relations avec les administres", "C) Les contrats administratifs n engagent pas l administration", "D) Les agents doivent croire en leur mission"],
        "answer": "B",
        "explanation": "La bonne foi implique que l administration agit loyalement et respecte les expectatives legitimes creees."
    },
    {
        "question": "Qu'est-ce que le principe d accessibilite du service public ?",
        "options": ["A) Le service doit etre gratuit pour tous", "B) Le service doit etre physiquement et financierement accessible a tous les usagers de maniere egale", "C) Le service doit etre disponible 24h/24", "D) Le service doit etre numerique"],
        "answer": "B",
        "explanation": "L accessibilite est une expression du principe d egalite : le service public doit etre accessible a tous sans discrimination."
    },
    {
        "question": "Qu'est-ce qu un acte r?glementaire en droit administratif ?",
        "options": ["A) Un acte individuel visant une personne nommement designee", "B) Un acte a portee generale et impersonnelle qui s applique a tous", "C) Un acte du Parlement", "D) Un acte des collectivites locales uniquement"],
        "answer": "B",
        "explanation": "L acte r?glementaire a une portee generale : il s applique a toutes les personnes dans la situation qu il definit."
    },
    {
        "question": "Quelle est la difference entre un acte administratif unilateral et un contrat administratif ?",
        "options": ["A) Aucune diff?rence", "B) L acte unilateral est impose sans consentement du destinataire ; le contrat implique un accord de volontes entre les parties", "C) Le contrat est superieur a l acte unilateral", "D) L acte unilateral est reserved au Pr?sident"],
        "answer": "B",
        "explanation": "L acte unilateral s impose sans accord ; le contrat resulte d un accord de volontes entre personne publique et cocontractant."
    },
    {
        "question": "Qu'est-ce que la prescription quadriennale des creances contre l'?tat ?",
        "options": ["A) L ?tat doit payer ses dettes en 4 mois", "B) Les creances non reclamees contre l'?tat se prescrivent (s eteignent) apres 4 ans", "C) Les impots non payes se prescrivent apres 4 ans", "D) Les contrats administratifs expirent apres 4 ans"],
        "answer": "B",
        "explanation": "La prescription quadriennale (4 ans en droit francais inspire le droit ivoirien) eteint les creances non reclamees contre l'?tat."
    },
    {
        "question": "Qu'est-ce qu un acte administratif declaratif ?",
        "options": ["A) Un acte qui cree des droits nouveaux", "B) Un acte qui constate l existence d une situation juridique prexistante sans creer de droits nouveaux", "C) Un acte qui punit un administre", "D) Un acte qui nomme un fonctionnaire"],
        "answer": "B",
        "explanation": "Un acte declaratif (ex diplome reconnaissance de nationalit?) constate ; il ne cree pas de droits nouveaux contrairement a l acte constitutif."
    },
    {
        "question": "Qu'est-ce que le droit de retrait d un acte administratif ?",
        "options": ["A) L administre peut retirer son dossier", "B) L administration peut supprimer retroactivement un acte illegal dans un delai limite", "C) L administre peut ignorer un acte avec lequel il n est pas d accord", "D) L annulation par un juge"],
        "answer": "B",
        "explanation": "Le droit de retrait permet a l autorite administrative de supprimer retroactivement un acte illegal. Le delai est en general de 4 mois."
    },
    {
        "question": "Qu'est-ce que l abrogation d un acte administratif ?",
        "options": ["A) L annulation retroactive par un juge", "B) La suppression de l acte pour l avenir seulement sans retroactivite", "C) La modification de l acte", "D) Le remplacement de l acte par un autre"],
        "answer": "B",
        "explanation": "L abrogation supprime l acte pour l avenir (ex nunc), contrairement au retrait qui est retroactif (ex tunc)."
    },
    {
        "question": "Pi?ge : retrait et abrogation d un acte administratif ont-ils les memes effets ?",
        "options": ["A) Oui identiques", "B) Non : retrait = effet retroactif (l acte est cense n avoir jamais existe) ; abrogation = effet seulement pour l avenir", "C) Le retrait est plus favorable a l administre", "D) L abrogation est plus grave que le retrait"],
        "answer": "B",
        "explanation": "Retrait = retroactif (ex tunc). Abrogation = pour l avenir (ex nunc)."
    },
    {
        "question": "Qu'est-ce que le principe de la securite des relations juridiques ?",
        "options": ["A) L ?tat garantit la securite physique des citoyens", "B) Les relations juridiques etablies ne peuvent pas etre remises en cause indefiniment ; il faut des delais de stabilisation", "C) Les contrats ne peuvent pas etre modifies", "D) Les lois ne peuvent pas etre changees"],
        "answer": "B",
        "explanation": "La securite juridique exige que les relations et les actes acquierent une certaine stabilite apres expiration des delais de recours."
    },
    {
        "question": "Qu'est-ce que l erreur manifeste d appreciation en droit administratif ?",
        "options": ["A) Une erreur de calcul dans un acte administratif", "B) Une erreur grossiere dans l appreciation des faits par l administration qui entraine l illegalite de l acte", "C) Une faute professionnelle d un fonctionnaire", "D) Un acte redige avec des erreurs de forme"],
        "answer": "B",
        "explanation": "L erreur manifeste d appreciation est un controle restreint du juge : il censure les erreurs grossieres dans l appreciation des faits par l administration."
    },
    {
        "question": "Qu'est-ce que le pouvoir de substitution d action en droit administratif ?",
        "options": ["A) Remplacer un agent par un autre", "B) Le pouvoir du superieur de se substituer a l autorite inferieure defaillante pour agir a sa place", "C) Le droit de l administre de faire appel", "D) La d?l?gation de signature"],
        "answer": "B",
        "explanation": "La substitution d action permet au superieur (ex prefet) d agir a la place d une autorite locale defaillante pour garantir l execution des obligations legales."
    },
    {
        "question": "Qu'est-ce que le principe de la responsabilite pour risque en droit administratif ?",
        "options": ["A) L ?tat est responsable uniquement si ses agents ont commis une faute", "B) L ?tat est responsable du simple fait de la creation d une situation dangereuse meme sans faute", "C) L ?tat n est jamais responsable pour risque", "D) La responsabilite pour risque n existe qu en droit priv?"],
        "answer": "B",
        "explanation": "La responsabilite pour risque engage l'?tat du fait d activites dangereuses (armes explosifs) meme en l absence de faute."
    },
    {
        "question": "Qu'est-ce que la Commission Administrative Paritaire (CAP) dans la fonction publique ivoirienne ?",
        "options": ["A) Un tribunal pour fonctionnaires", "B) Un organisme consultatif paritaire (autant d elus du personnel que de representants de l administration) consulte sur les decisions individuelles (mutations avancement sanctions)", "C) Un syndicat de fonctionnaires", "D) Une instance de controle budg?taire"],
        "answer": "B",
        "explanation": "La CAP est consultee sur les decisions individuelles concernant la carriere des fonctionnaires."
    },
    {
        "question": "Qu'est-ce que le droit disciplinaire dans la fonction publique ?",
        "options": ["A) Le droit du fonctionnaire de refuser des sanctions", "B) L ensemble des regles relatives aux sanctions pouvant etre infligees a un fonctionnaire qui a manque a ses obligations professionnelles", "C) Le droit de retraite des fonctionnaires", "D) Le droit de greve des fonctionnaires"],
        "answer": "B",
        "explanation": "Le droit disciplinaire fixe les fautes professionnelles et les sanctions applicables (avertissement bleme suspension revocation)."
    },
    {
        "question": "Pi?ge : un fonctionnaire condamne penalement peut-il etre aussi sanctionne disciplinairement pour les memes faits ?",
        "options": ["A) Non le principe non bis in idem l interdit", "B) Oui les deux procedures sont independantes", "C) Non il faut choisir l une ou l autre", "D) Oui mais uniquement si la peine est superieure a 6 mois"],
        "answer": "B",
        "explanation": "Les procedures penale et disciplinaire sont independantes. Un meme fait peut donner lieu a une sanction penale et a une sanction disciplinaire."
    },
    {
        "question": "Qu'est-ce que l avancement a l anciennete dans la fonction publique ivoirienne ?",
        "options": ["A) La promotion automatique basee uniquement sur la duree de service", "B) L avancement qui tient compte du temps de service et parfois des notes mais sans selection rigoureuse", "C) La promotion uniquement au merite", "D) L avancement accorde par le Parlement"],
        "answer": "B",
        "explanation": "L avancement a l anciennete (increments) est automatique ou semi-automatique en fonction du temps de service."
    },
    {
        "question": "Qu'est-ce que l avancement au choix (ou au merite) dans la fonction publique ivoirienne ?",
        "options": ["A) L avancement automatique annuel", "B) L avancement decide par l administration apres evaluation des performances et choix parmi les agents eligibles", "C) L avancement par concours interne", "D) L avancement accorde au plus anciens"],
        "answer": "B",
        "explanation": "L avancement au choix est decide par l administration parmi les agents eligibles en tenant compte de leurs merites et de leurs notes."
    },
    {
        "question": "Qu'est-ce que la mise en non-activite d un fonctionnaire ivoirien ?",
        "options": ["A) Le conge annuel", "B) La position administrative ou le fonctionnaire est suspendu temporairement de ses fonctions en attendant une decision (ex enquete disciplinaire)", "C) La retraite", "D) Le detachement"],
        "answer": "B",
        "explanation": "La mise en non-activite est une suspension temporaire des fonctions dans l attente d une decision disciplinaire ou judiciaire."
    },
    {
        "question": "Pi?ge : un fonctionnaire suspendu pendant une enquete disciplinaire a-t-il droit a son salaire ?",
        "options": ["A) Non il perd tout droit a remuneration", "B) Oui il conserve sa remuneration pendant la periode de suspension dans l attente de la decision", "C) Il recoit 50% de son salaire", "D) Cela depend de la gravite des faits"],
        "answer": "B",
        "explanation": "Pendant la suspension provisoire en attente de decision disciplinaire le fonctionnaire conserve generalement sa remuneration."
    },
    {
        "question": "Qu'est-ce que le principe d impartialite de l administration ?",
        "options": ["A) L administration n a aucune opinion", "B) L administration traite toutes les situations similaires de la meme maniere sans favoritisme ni discrimination", "C) L administration ne peut pas donner d avis", "D) L administration doit toujours donner raison au citoyen"],
        "answer": "B",
        "explanation": "L impartialite garantit l absence de favoritisme : les agents de l administration ne peuvent pas avantager ou penaliser arbitrairement les administres."
    },
    {
        "question": "Qu'est-ce que la notion de service public en reseau ?",
        "options": ["A) Un service gere via internet", "B) Un service public organise en infrastructure nationale (eau electricite transport rail) qui necessite des investissements lourds et un acces universel", "C) Un service public gerant les reseaux sociaux", "D) Un service prive de telecommunications"],
        "answer": "B",
        "explanation": "Les services en reseau (eau electricite routes ferrees) sont des services publics a acces universel necessitant des infrastructures nationales."
    },
    {
        "question": "Qu'est-ce que le pouvoir de police administrative ?",
        "options": ["A) Le pouvoir de la police judiciaire de poursuivre les criminels", "B) Le pouvoir des autorites administratives de restreindre les libert?s individuelles pour maintenir l ordre public", "C) Le pouvoir du Parlement de voter des lois securitaires", "D) Le pouvoir des communes de creer des services de securite"],
        "answer": "B",
        "explanation": "La police administrative permet a l administration de prevenir les troubles a l ordre public en imposant des restrictions aux libert?s."
    },
    {
        "question": "Quels sont les trois elements de l ordre public en police administrative ?",
        "options": ["A) Surete tranquillite salubrité", "B) Surete securite efficacite", "C) Egalite liberte fraternite", "D) Ordre paix justice"],
        "answer": "A",
        "explanation": "L ordre public en police administrative comprend la surete (securite des personnes et biens) la tranquillite (absence de troubles) et la salubrite (hygiene publique)."
    },
    {
        "question": "Pi?ge : la police administrative peut-elle etre exercee par une personne privee ?",
        "options": ["A) Non, c'est une prerogative de puissance publique", "B) Oui dans le cadre de la delegation de service public", "C) Oui toujours", "D) Non meme en cas de delegation"],
        "answer": "A",
        "explanation": "La police administrative est une prerogative de puissance publique et ne se delegate pas a une personne privee."
    },
    {
        "question": "Qu'est-ce que le domaine public en droit administratif ivoirien ?",
        "options": ["A) L ensemble des biens prives de l'?tat", "B) L ensemble des biens affectes a l usage direct du public ou a un service public et soumis a un r?gime de protection special", "C) Les terres agricoles de l'?tat", "D) Les immeubles des minist?res uniquement"],
        "answer": "B",
        "explanation": "Le domaine public est insaisissable inalienable et imprescriptible. Il comprend les routes les ponts les cours d eau navigables etc."
    },
    {
        "question": "Pi?ge : l'?tat peut-il vendre un bien du domaine public ivoirien ?",
        "options": ["A) Oui librement", "B) Non le domaine public est inalienable ; il faut d abord le desaffecter du domaine public pour le vendre", "C) Oui avec l accord du Parlement", "D) Oui mais uniquement a une personne publique"],
        "answer": "B",
        "explanation": "L inalienabilite du domaine public interdit sa vente directe. La desaffectation prealable est obligatoire avant toute cession."
    },
    {
        "question": "Qu'est-ce que le droit de preemption de l'?tat en CI ?",
        "options": ["A) Le droit de l'?tat d acheter en priorite certains biens mis en vente", "B) Le droit de l'?tat de prendre les biens sans indemnisation", "C) Le droit de l'?tat de louer des proprietes privees", "D) Le droit de l'?tat de reclamer des impots en priorite"],
        "answer": "A",
        "explanation": "Le droit de preemption permet a l'?tat d acquerir en priorite certains biens mis en vente notamment dans le cadre de l amenagement du territoire."
    },
    {
        "question": "Qu'est-ce que l expropriation pour cause d utilite publique ?",
        "options": ["A) La confiscation des biens des criminels", "B) La procedure permettant a l'?tat de prendre propriete d un bien prive contre une indemnisation juste et prealable pour un projet d interet general", "C) La saisie des biens en cas de dettes fiscales", "D) La nationalisation d une entreprise"],
        "answer": "B",
        "explanation": "L expropriation est encadree : elle necessite une utilite publique reconnue une procedure legale et une indemnisation juste et prealable."
    },
    {
        "question": "Pi?ge : l expropriation sans indemnisation est-elle possible en CI ?",
        "options": ["A) Oui en cas d urgence nationale", "B) Non elle est inconstitutionnelle : l indemnisation juste et prealable est une garantie constitutionnelle", "C) Oui avec l accord du Conseil constitutionnel", "D) Oui uniquement pour les ?trangers"],
        "answer": "B",
        "explanation": "La Constitution garantit le droit de propriete. L expropriation n est possible qu avec une juste et prealable indemnisation."
    },
    {
        "question": "Qu'est-ce que le principe de continuite de l activite administrative ?",
        "options": ["A) L administration ne ferme jamais", "B) Les services administratifs essentiels doivent fonctionner de maniere continue sans interruption injustifiee", "C) Les fonctionnaires travaillent 24h/24", "D) Les lois ne peuvent pas suspendre les services"],
        "answer": "B",
        "explanation": "La continuite administrative garantit que les services publics essentiels (sante securite eau) ne s interrompent pas meme lors de greves."
    },
    {
        "question": "Qu'est-ce que le recours de plein contentieux (ou recours de pleine juridiction) ?",
        "options": ["A) Un recours qui ne peut annuler un acte", "B) Un recours ou le juge peut annuler reformer ou condamner l administration a payer des dommages et interets", "C) Un recours reserve aux ?trangers", "D) Un recours devant le Conseil constitutionnel"],
        "answer": "B",
        "explanation": "Le recours de plein contentieux va au-dela de la simple annulation : le juge peut reformer l acte et accorder des dommages et interets."
    },
    {
        "question": "Qu'est-ce qu un arrete ministeriel ?",
        "options": ["A) Un arrete pris par le Premier ministre", "B) Un acte r?glementaire ou individuel pris par un ministre dans le cadre de ses attributions", "C) Une loi adoptee par le Parlement", "D) Un decret pr?sidentiel"],
        "answer": "B",
        "explanation": "L arrete ministeriel est un acte de l executif pris par un ministre. Il a une portee inferieure aux decrets."
    },
    {
        "question": "Qu'est-ce que la hi?rarchie des actes administratifs en CI ?",
        "options": ["A) Les decrets > les arretes ministeriels > les arretes prefectoraux > les arretes municipaux", "B) Les arretes municipaux > les arretes prefectoraux", "C) Les arretes ministeriels > les decrets", "D) Tous les actes administratifs ont la meme valeur"],
        "answer": "A",
        "explanation": "La hi?rarchie : decrets presidetiels > decrets en conseil des ministres > arretes ministeriels > arretes prefectoraux > arretes municipaux."
    },
    {
        "question": "Qu'est-ce que la competence liee de l administration ?",
        "options": ["A) L administration a une totale liberte de choix", "B) L administration n a pas de liberte de choix : la loi definit precisement ce qu elle doit faire et comment", "C) La competence exclusive d un minist?re", "D) La competence partagee entre deux autorites"],
        "answer": "B",
        "explanation": "La competence liee s oppose au pouvoir discrecionnaire : l administration doit agir d une certaine maniere sans avoir le choix."
    },
    {
        "question": "Pi?ge : l administration peut-elle abroger un r?glement en vigueur a tout moment ?",
        "options": ["A) Non elle doit maintenir les r?glements en vigueur indefiniment", "B) Oui l administration peut abroger ses propres r?glements a tout moment sauf si l abrogation porte atteinte aux droits acquis", "C) Oui mais uniquement avec l accord du Parlement", "D) Non seul le juge peut abroger un r?glement"],
        "answer": "B",
        "explanation": "L administration a le droit et parfois l obligation d abroger ses r?glements illegaux. Cependant l abrogation ne peut pas porter atteinte a des droits acquis legitimes."
    },
    {
        "question": "Qu'est-ce que le principe de la hi?rarchie administrative ?",
        "options": ["A) Les fonctionnaires sont ordonnes par salaire", "B) Le superieur hierarchique peut donner des instructions a ses subordonnes et exercer sur eux un pouvoir de controle et de sanction", "C) Tous les agents ont la meme autorite", "D) Le plus ancien commande toujours"],
        "answer": "B",
        "explanation": "La hi?rarchie administrative implique que le superieur peut donner des instructions des ordres et exercer un pouvoir disciplinaire sur ses subordonnes."
    },
    {
        "question": "Qu'est-ce qu une autorite administrative independante (AAI) ?",
        "options": ["A) Un tribunal administratif", "B) Une structure administrative dotee d une independance vis-a-vis du gouvernement creee pour reguler des secteurs sensibles", "C) Un minist?re autonome", "D) Une collectivit? territoriale"],
        "answer": "B",
        "explanation": "Les AAI (ex ARTCI HACA CMI) sont des structures administratives independantes du gouvernement chargees de reguler des secteurs qui necessitent une neutralite politique."
    },
    {
        "question": "Qu'est-ce que la HACA en CI ?",
        "options": ["A) Haute Autorite des Collectivites Administratives", "B) Haute Autorite de la Communication Audiovisuelle : autorite qui regule les medias audiovisuels en CI", "C) Haute Assemblee des Citoyens Africains", "D) Haute Administration des Charges et Achats"],
        "answer": "B",
        "explanation": "La HACA est l autorite administrative independante chargee de reguler la communication audiovisuelle (television radio) en C?te d'Ivoire."
    },
    {
        "question": "Pi?ge : les AAI (autorites administratives independantes) font-elles partie de l'?tat ?",
        "options": ["A) Non elles sont totalement independantes", "B) Oui elles font partie de l'?tat mais disposent d une independance organique et fonctionnelle vis-a-vis du gouvernement", "C) Non elles sont des organismes prives", "D) Oui elles sont sous l autorite directe du Pr?sident"],
        "answer": "B",
        "explanation": "Les AAI font partie de l'?tat mais avec une independance institutionnelle garantissant leur neutralite par rapport au gouvernement du jour."
    },
    {
        "question": "Qu'est-ce que le contentieux de la responsabilite administrative ?",
        "options": ["A) La responsabilite penale des fonctionnaires", "B) Le litige devant le juge administratif tendant a obtenir la reparation d un dommage cause par une personne publique", "C) Le contentieux fiscal entre l'?tat et les entreprises", "D) Les litiges entre fonctionnaires"],
        "answer": "B",
        "explanation": "Le contentieux de la responsabilite administrative permet aux victimes d actes ou de comportements fautifs de l administration d obtenir une indemnisation."
    },
    {
        "question": "Qu'est-ce que la rupture d egalite devant les charges publiques ?",
        "options": ["A) Une inegalite de traitement entre fonctionnaires", "B) Le fait qu une decision ou une action de l administration fait supporter a un particulier un prejudice anormal et special que les autres citoyens ne supportent pas", "C) Une inegalite fiscale", "D) Une discrimination a l embauche dans la fonction publique"],
        "answer": "B",
        "explanation": "La rupture d egalite fonde la responsabilite sans faute : si l action de l'?tat cree un prejudice anormal et special l'?tat doit indemniser meme sans avoir commis de faute."
    },
    {
        "question": "Qu'est-ce que le recours indemnitaire en droit administratif ?",
        "options": ["A) Un recours pour annuler un acte", "B) Un recours tendant a obtenir une compensation financiere pour un prejudice subi du fait de l administration", "C) Un recours pour obtenir un logement social", "D) Un recours contre les impots"],
        "answer": "B",
        "explanation": "Le recours indemnitaire (ou de plein contentieux) permet d obtenir la condamnation de l administration a payer des dommages et interets."
    },
    {
        "question": "Qu'est-ce que la mise en demeure de l administration ?",
        "options": ["A) Une sanction administrative", "B) Un acte par lequel l administre ou le juge somme l administration d executer ses obligations dans un delai determine", "C) Une convocation disciplinaire", "D) Un ordre de paiement"],
        "answer": "B",
        "explanation": "La mise en demeure invite l administration a remplir ses obligations. Si elle ne s execute pas le juge peut prononcer des astreintes."
    },
    {
        "question": "Qu'est-ce que l astreinte en droit administratif ?",
        "options": ["A) Une peine privative de liberte pour un fonctionnaire", "B) Une sanction financiere prononcee par le juge pour contraindre l administration a executer une decision de justice", "C) Une amende fiscale", "D) Une retenue sur salaire"],
        "answer": "B",
        "explanation": "L astreinte est une condamnation financiere par jour de retard : elle vise a contraindre l administration a executer les decisions de justice."
    },
    {
        "question": "Pi?ge : le juge administratif peut-il adresser des injonctions a l administration en CI ?",
        "options": ["A) Non le juge ne peut qu annuler les actes", "B) Oui depuis les reformes recentes le juge administratif peut adresser des injonctions et prononcer des astreintes pour assurer l execution de ses decisions", "C) Non le juge administratif n a aucun pouvoir d execution", "D) Oui mais uniquement en matiere financiere"],
        "answer": "B",
        "explanation": "Les reformes du droit administratif modeme reconnaissent au juge le pouvoir d injonction et d astreinte pour faire executer ses decisions."
    },
    {
        "question": "Qu'est-ce que le principe de publicite des actes administratifs ?",
        "options": ["A) Tous les actes doivent passer a la television", "B) Pour etre opposables les actes administratifs doivent etre portes a la connaissance de leurs destinataires par publication ou notification", "C) Les actes administratifs sont confidentiels", "D) Seuls les decrets pr?sidentiels doivent etre publies"],
        "answer": "B",
        "explanation": "La publicite des actes administratifs est une condition de leur opposabilite : les r?glements doivent etre publies les actes individuels notifies."
    },
    {
        "question": "Qu'est-ce que le principe du service minimum en cas de greve dans les services publics essentiels ?",
        "options": ["A) Les greves sont interdites dans les services publics", "B) En cas de greve dans les services essentiels (hopitaux transports) un service minimum doit etre maintenu pour proteger la continuite", "C) Les fonctionnaires greves doivent assurer 100% du service", "D) Le service minimum n existe pas en CI"],
        "answer": "B",
        "explanation": "Le service minimum concilie le droit de greve et la continuite des services essentiels. Des agents doivent maintenir un service de base."
    },
    {
        "question": "Qu'est-ce que le principe de l autorite de la chose jugee en droit administratif ?",
        "options": ["A) Un acte administratif ne peut jamais etre modifie", "B) Une decision de justice devient definitive et lie les parties une fois les voies de recours epuisees", "C) L administration doit obeir aux jugements uniquement si elle le souhaite", "D) Seul le Conseil constitutionnel peut rendre des decisions definitives"],
        "answer": "B",
        "explanation": "L autorite de la chose jugee signifie qu une decision definitive s impose a tous y compris a l administration."
    },
    {
        "question": "Qu'est-ce que le pouvoir r?glementaire autonome en CI ?",
        "options": ["A) Le pouvoir du Parlement de prendre des r?glements", "B) Le pouvoir du Pr?sident et du gouvernement de prendre des r?glements dans des matieres non reservees a la loi", "C) Le pouvoir des communes de voter leurs propres lois", "D) Le pouvoir du Conseil constitutionnel de reguler les lois"],
        "answer": "B",
        "explanation": "Le pouvoir r?glementaire autonome permet a l executif de regler les matieres qui ne sont pas du domaine de la loi defini par la Constitution."
    }
]

# Catalogue des thèmes disponibles
THEME_CATALOG = [
    ("Culture Générale — Langue française", THEME_1),
    ("Aptitude Verbale — Phénomènes lexicaux", THEME_2),
    ("Culture Générale — Géographie et connaissances", THEME_3),
    ("Organisations Internationales", THEME_4),
    ("English Grammar", THEME_5),
    ("Culture Générale — Institutions et citoyenneté", THEME_6),
    ("Droit administratif", THEME_7),
]

def get_quiz_questions(num_questions=20, min_themes=7, selected_themes=None):
    """
    Génère un ensemble de questions pour le quiz.
    Les questions sont aléatoires et ne se répètent jamais dans un même quiz.
    
    Args:
        num_questions: Nombre total de questions (10, 20, 30, 50 ou 100)
        min_themes: Nombre minimum de thèmes à couvrir (défaut: 7 = tous)
        selected_themes: Liste optionnelle de thèmes à inclure. Si fournie,
            le quiz est limité à ces thèmes.
    
    Returns:
        Liste de questions mélangées sans doublons
    """
    themes = THEME_CATALOG

    if selected_themes:
        selected = {str(theme).strip() for theme in selected_themes if str(theme).strip()}
        themes = [item for item in THEME_CATALOG if item[0] in selected]
        if not themes:
            raise ValueError("Aucun thème valide sélectionné.")

    if not themes:
        raise ValueError("Aucun thème disponible.")
    
    # Couvrir les thèmes sélectionnés
    num_themes = len(themes)
    
    # Calculer le nombre de questions par thème (répartition équitable)
    questions_per_theme = num_questions // num_themes
    remaining = num_questions % num_themes
    
    selected_questions = []
    used_indices = set()  # Pour garantir la non-répétition
    
    for i, (theme_name, theme_questions) in enumerate(themes):
        # Nombre de questions pour ce thème
        n = questions_per_theme + (1 if i < remaining else 0)
        n = min(n, len(theme_questions))  # Ne pas dépasser le nombre disponible
        
        # Sélectionner aléatoirement n questions de ce thème (sans répétition)
        theme_sample = random.sample(theme_questions, n)
        
        # Ajouter le nom du thème à chaque question
        for q in theme_sample:
            q_copy = q.copy()
            q_copy["theme"] = theme_name
            selected_questions.append(q_copy)
    
    # Mélanger toutes les questions
    random.shuffle(selected_questions)
    
    return selected_questions[:num_questions]
