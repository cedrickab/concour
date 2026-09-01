"""
Base de données de questions pour le quiz ENA
Organisée par thèmes.
"""
import random

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
        "question": "Dans quelle phrase n'y a-t-il pas de pléonasme ?",
        "options": ["A) Le jeune lavandier travaille dans la laverie", "B) Pour la police, c'est un petit détail", "C) Ils vont tous se rencontrer ensemble"],
        "answer": "B",
        "explanation": "Cette phrase n'a pas de redondance, contrairement aux autres."
    },
    {
        "question": "Quel complément convient au verbe « luter » ?",
        "options": ["A) Une fissure", "B) Un vase", "C) Un trou", "D) Une fenêtre"],
        "answer": "B",
        "explanation": "« Luter » signifie boucher hermétiquement avec du lut (mastic). On lute un vase."
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
        "question": "Le mot navigant est l'adjectif verbal de naviguer. Il est :",
        "options": ["A) Variable", "B) Invariable", "C) Uniquement masculin", "D) Uniquement feminin"],
        "answer": "A",
        "explanation": "L'adjectif verbal navigant est variable : des personnels navigants."
    },
    {
        "question": "Quel mot est mal orthographié ?",
        "options": ["A) Chrysanthème", "B) Philantropie", "C) Rhythme", "D) Ephémère"],
        "answer": "B",
        "explanation": "Le mot correct est « philanthropie » avec un « h » après le « p »."
    },
    {
        "question": "Quel est le synonyme de « acrimonieux » ?",
        "options": ["A) Doux", "B) Acide", "C) Haineux", "D) Jovial"],
        "answer": "C",
        "explanation": "« Acrimonieux » signifie aigre, hargneux, plein d'animosité."
    },
    {
        "question": "Que signifie le mot « adage » ?",
        "options": ["A) Un instrument de musique", "B) Un proverbe", "C) Un texte de loi", "D) Une formule mathématique"],
        "answer": "B",
        "explanation": "Un adage est un proverbe ou une maxime populaire transmettant une vérité pratique."
    },
    {
        "question": "Quel mot est l'antonyme de « loquace » ?",
        "options": ["A) Bavard", "B) Silencieux", "C) Éloquent", "D) Verbeux"],
        "answer": "B",
        "explanation": "« Loquace » signifie bavard ; son antonyme est « silencieux » ou « taciturne »."
    },
    {
        "question": "Dans quelle phrase le subjonctif est-il obligatoire ?",
        "options": ["A) Je pense qu'il viendra.", "B) Il faut qu'il vienne.", "C) Je sais qu'il est là.", "D) Je crois qu'il a raison."],
        "answer": "B",
        "explanation": "Après « il faut que », le subjonctif est obligatoire."
    },
    {
        "question": "Quelle est la forme correcte du conditionnel passé ?",
        "options": ["A) Il aurait mangé", "B) Il aura mangé", "C) Il avait mangé", "D) Il eut mangé"],
        "answer": "A",
        "explanation": "Le conditionnel passé se forme avec l'auxiliaire au conditionnel présent + participe passé."
    },
    {
        "question": "Le mot « péremptoire » signifie :",
        "options": ["A) Hésitant", "B) Définitif et sans appel", "C) Bienveillant", "D) Ambigu"],
        "answer": "B",
        "explanation": "Un ton péremptoire est absolu, tranchant, qui n'admet pas de réplique."
    },
    {
        "question": "Quel est le pluriel correct de « bal » ?",
        "options": ["A) bals", "B) baux", "C) bales", "D) bles"],
        "answer": "A",
        "explanation": "Le pluriel de « bal » est « bals » (exception aux mots en -al qui font -aux)."
    },
    {
        "question": "Quelle figure de style consiste à atténuer une réalité pour en diminuer l'effet ?",
        "options": ["A) Hyperbole", "B) Euphémisme", "C) Métonymie", "D) Personnification"],
        "answer": "B",
        "explanation": "L'euphémisme adoucit une réalité dure (ex. : « il a disparu » pour « il est mort »)."
    },
    {
        "question": "Quelle est la nature grammaticale de « vite » dans « il court vite » ?",
        "options": ["A) Adjectif", "B) Nom", "C) Adverbe", "D) Préposition"],
        "answer": "C",
        "explanation": "« Vite » est un adverbe qui modifie le verbe « court »."
    },
    {
        "question": "Quel est le sens du préfixe « bene- » ?",
        "options": ["A) Mauvais", "B) Deux", "C) Bien", "D) Avant"],
        "answer": "C",
        "explanation": "Le préfixe latin « bene- » signifie bien (bénéfice, bénévole)."
    },
    {
        "question": "Quelle est la différence entre « davantage » et « d'avantage » ?",
        "options": ["A) Aucune différence", "B) Davantage = plus ; d'avantage = d'un avantage", "C) Davantage s'écrit sans accent", "D) D'avantage est toujours incorrect"],
        "answer": "B",
        "explanation": "« Davantage » = plus ; « d'avantage » = d'un avantage (bénéfice)."
    },
    {
        "question": "Quel verbe est défectif (n'existe qu'à certaines formes) ?",
        "options": ["A) Manger", "B) Partir", "C) Clore", "D) Faire"],
        "answer": "C",
        "explanation": "« Clore » est un verbe défectif : il manque de nombreuses formes conjuguées."
    },
    {
        "question": "Quelle phrase utilise le passé simple correctement ?",
        "options": ["A) Il mangea une pomme.", "B) Il a mangea une pomme.", "C) Il mangeait une pomme.", "D) Il mangera une pomme."],
        "answer": "A",
        "explanation": "Le passé simple d'un verbe en -er se forme en ajoutant -a (3e personne singulier)."
    },
    {
        "question": "Quel est l'homonyme de « cent » ?",
        "options": ["A) Saint", "B) Sont", "C) Sans", "D) Sang"],
        "answer": "D",
        "explanation": "« Cent », « sans », « sang », « s'en » et « sent » sont des homophones."
    },
    {
        "question": "Que signifie « à bon escient » ?",
        "options": ["A) Par hasard", "B) Avec mauvaise intention", "C) À propos et judicieusement", "D) Avec hésitation"],
        "answer": "C",
        "explanation": "Agir à bon escient, c'est agir de manière pertinente, avec une bonne connaissance de la situation."
    },
    {
        "question": "Quel est le terme grammatical désignant « le » dans « le chien aboie » ?",
        "options": ["A) Adjectif démonstratif", "B) Pronom personnel", "C) Article défini", "D) Article indéfini"],
        "answer": "C",
        "explanation": "« Le » est un article défini qui détermine le nom « chien »."
    },
    {
        "question": "Quelle est la forme correcte ?",
        "options": ["A) Quoiqu'il fasse beau.", "B) Quoique il fasse beau.", "C) Quoi qu'il fasse beau.", "D) Quoi que il fasse beau."],
        "answer": "A",
        "explanation": "Devant « il », « quoique » subit l'élision : « quoiqu'il »."
    },
    {
        "question": "Le mot « épistémologie » désigne :",
        "options": ["A) L'étude des épistaxis", "B) La théorie de la connaissance", "C) L'étude des épidémies", "D) La science des lettres"],
        "answer": "B",
        "explanation": "L'épistémologie est la branche philosophique qui étudie la nature et les limites de la connaissance."
    },
    {
        "question": "Dans « cette robe est verte », le mot « verte » est :",
        "options": ["A) Un adjectif épithète", "B) Un adjectif attribut", "C) Un nom", "D) Un adverbe"],
        "answer": "B",
        "explanation": "« Verte » est attribut du sujet « robe » via le verbe d'état « est »."
    },
    {
        "question": "Quel est l'antonyme de « turpitude » ?",
        "options": ["A) Probité", "B) Honte", "C) Bassesse", "D) Indignité"],
        "answer": "A",
        "explanation": "La turpitude désigne la bassesse morale ; son antonyme est la probité (honnêteté)."
    },
    {
        "question": "Quelle est la règle d'accord du participe passé employé avec « avoir » ?",
        "options": ["A) Il s'accorde toujours avec le sujet", "B) Il s'accorde avec le COD placé avant", "C) Il reste invariable", "D) Il s'accorde avec le COI"],
        "answer": "B",
        "explanation": "Le participe passé avec « avoir » s'accorde avec le COD si celui-ci précède le verbe."
    },
    {
        "question": "Quel est le sens de « hégémonie » ?",
        "options": ["A) Domination prépondérante", "B) Égalité des nations", "C) Faiblesse politique", "D) Alliance militaire"],
        "answer": "A",
        "explanation": "L'hégémonie désigne la domination, la suprématie d'un État ou groupe sur d'autres."
    },
    {
        "question": "Quelle est la figure de style dans « ses yeux sont deux étoiles » ?",
        "options": ["A) Comparaison", "B) Métaphore", "C) Allitération", "D) Antithèse"],
        "answer": "B",
        "explanation": "La métaphore exprime une ressemblance sans outil comparatif (sans « comme »)."
    },
    {
        "question": "Quel est le genre du mot « amalgame » ?",
        "options": ["A) Féminin", "B) Masculin", "C) Les deux selon le contexte", "D) Neutre"],
        "answer": "B",
        "explanation": "« Amalgame » est un nom masculin : un amalgame."
    },
    {
        "question": "Que signifie « circonstancié » ?",
        "options": ["A) Vague et imprécis", "B) Détaillé et accompagné de précisions", "C) Rapide et bref", "D) Oral et non écrit"],
        "answer": "B",
        "explanation": "Un rapport circonstancié contient tous les détails et précisions nécessaires."
    },
    {
        "question": "Quel mot est un paronyme de « éruption » ?",
        "options": ["A) Irruption", "B) Corruption", "C) Absorption", "D) Interruption"],
        "answer": "A",
        "explanation": "« Éruption » (volcanique) et « irruption » (entrée brusque) sont des paronymes souvent confondus."
    },
    {
        "question": "Quelle est la règle d'accord dans « les fenêtres que j'ai ouvertes » ?",
        "options": ["A) Pas d'accord car COD après le verbe", "B) Accord avec 'fenêtres' car COD placé avant", "C) Accord avec le sujet 'je'", "D) Pas d'accord avec 'avoir'"],
        "answer": "B",
        "explanation": "« Que » reprend « fenêtres » (COD) placé avant le verbe avoir → accord au féminin pluriel."
    },
    {
        "question": "Quel est le sens de l'expression « au pied levé » ?",
        "options": ["A) Avec beaucoup de préparation", "B) Sans préparation, immédiatement", "C) En marchant", "D) Avec prudence"],
        "answer": "B",
        "explanation": "Agir au pied levé, c'est agir sans préparation préalable, dans l'urgence."
    },
    {
        "question": "Laquelle de ces formes verbales est au plus-que-parfait ?",
        "options": ["A) Il avait mangé", "B) Il a mangé", "C) Il mangea", "D) Il mangerait"],
        "answer": "A",
        "explanation": "Le plus-que-parfait se forme avec l'imparfait de l'auxiliaire + participe passé."
    },
    {
        "question": "Quel est le sens du suffixe « -phile » ?",
        "options": ["A) Qui craint", "B) Qui aime", "C) Qui mange", "D) Qui gouverne"],
        "answer": "B",
        "explanation": "Le suffixe « -phile » signifie qui aime (bibliophile = qui aime les livres)."
    },
    {
        "question": "Quelle est la phrase correcte ?",
        "options": ["A) Malgré que j'aie faim, je ne mange pas.", "B) Bien que j'aie faim, je ne mange pas.", "C) Malgré j'ai faim, je ne mange pas.", "D) Encore que j'ai faim, je ne mange pas."],
        "answer": "B",
        "explanation": "« Bien que » est correct et se construit avec le subjonctif. « Malgré que » est critiqué par les puristes."
    },
    {
        "question": "Quel est le mot générique pour désigner les figures rhétoriques liées au son ?",
        "options": ["A) Tropes", "B) Figures sonores", "C) Métaplasmes", "D) Syntaxèmes"],
        "answer": "C",
        "explanation": "Les métaplasmes (allitération, assonance...) sont les figures qui jouent sur les sons."
    },
    {
        "question": "Que désigne le terme « polémique » dans son sens originel ?",
        "options": ["A) Une guerre verbale, un débat houleux", "B) Une démonstration mathématique", "C) Un traité diplomatique", "D) Une cérémonie officielle"],
        "answer": "A",
        "explanation": "Du grec « polemikos » (guerre), une polémique est un débat vif et souvent agressif."
    },
    {
        "question": "Dans quelle phrase le pronom « on » peut-il remplacer « nous » ?",
        "options": ["A) On a fini le travail (= nous avons fini).", "B) On a du pain (= il y a du pain).", "C) Que dit-on de lui ?", "D) On frappe à la porte."],
        "answer": "A",
        "explanation": "En français courant, « on » peut remplacer « nous » comme sujet de la phrase."
    },
    {
        "question": "Quel est le mode verbal utilisé pour donner un ordre direct ?",
        "options": ["A) Indicatif", "B) Subjonctif", "C) Impératif", "D) Infinitif"],
        "answer": "C",
        "explanation": "L'impératif exprime un ordre, une demande ou un conseil direct."
    },
    {
        "question": "Quel est le sens de « nonobstant » ?",
        "options": ["A) Cependant, malgré", "B) De plus, en outre", "C) Autrement dit", "D) C'est pourquoi"],
        "answer": "A",
        "explanation": "« Nonobstant » signifie malgré, en dépit de (terme juridique fréquent)."
    },
    {
        "question": "Que signifie « exergue » ?",
        "options": ["A) Un exercice d'écriture", "B) Une courte citation placée en tête d'un ouvrage", "C) Un résumé de texte", "D) Une annexe juridique"],
        "answer": "B",
        "explanation": "Mettre en exergue = mettre en évidence ; une citation en exergue introduit un texte."
    },
    {
        "question": "Quelle est la différence entre « apporter » et « amener » ?",
        "options": ["A) Aucune différence", "B) Apporter concerne les choses ; amener concerne les personnes ou animaux", "C) Amener s'utilise pour aller vers ; apporter pour venir vers", "D) Amener est plus formel"],
        "answer": "B",
        "explanation": "On apporte un objet, on amène une personne ou un animal."
    },
    {
        "question": "Quel est le sens littéral de « laconique » ?",
        "options": ["A) Venant de Laconie (Sparte) : bref et concis", "B) Ennuyeux et long", "C) Émouvant", "D) Obscur et ambigu"],
        "answer": "A",
        "explanation": "Les Laconiens (Spartiates) étaient réputés pour leur discours bref ; laconique = bref et concis."
    },
    {
        "question": "Quelle est la fonction grammaticale de « demain » dans « il viendra demain » ?",
        "options": ["A) Sujet", "B) COD", "C) Complément circonstanciel de temps", "D) Attribut"],
        "answer": "C",
        "explanation": "« Demain » indique quand aura lieu l'action : c'est un CC de temps."
    },
    {
        "question": "Que signifie le verbe « circonscrire » ?",
        "options": ["A) Développer, étendre", "B) Limiter, délimiter avec précision", "C) Critiquer sévèrement", "D) Résumer"],
        "answer": "B",
        "explanation": "Circonscrire un incendie = limiter sa propagation ; circonscrire un sujet = en définir les limites."
    },
    {
        "question": "Quelle figure de style consiste à répéter un mot ou groupe en début de plusieurs propositions ?",
        "options": ["A) Épiphore", "B) Anaphore", "C) Chiasme", "D) Syllepse"],
        "answer": "B",
        "explanation": "L'anaphore est la répétition d'un mot ou groupe en tête de propositions successives."
    },
    {
        "question": "Que désigne « l'ellipse » en stylistique ?",
        "options": ["A) Une figure géométrique", "B) Une omission volontaire d'éléments grammaticaux sans ambiguïté", "C) Une répétition de sons", "D) Une exagération"],
        "answer": "B",
        "explanation": "L'ellipse est l'omission d'un ou plusieurs mots logiquement attendus mais sous-entendus."
    },
    {
        "question": "Quel est le sens du mot « acuité » ?",
        "options": ["A) Manque de clarté", "B) Finesse, précision d'un sens ou d'une faculté", "C) Lenteur de réaction", "D) Générosité"],
        "answer": "B",
        "explanation": "L'acuité visuelle, l'acuité intellectuelle désignent la finesse et la précision d'une faculté."
    },
    {
        "question": "Dans « il se souvient de son enfance », le pronom « se » est :",
        "options": ["A) Pronom COD", "B) Pronom COI", "C) Pronom réfléchi sans fonction propre", "D) Pronom sujet"],
        "answer": "C",
        "explanation": "Dans les verbes essentiellement pronominaux, le « se » fait partie du verbe sans fonction propre."
    },
    {
        "question": "Identifiez la phrase correcte :",
        "options": ["A) Les pommes que j'ai acheté sont bonnes.", "B) Les pommes que j'ai achetées sont bonnes.", "C) Les pommes que j'ai achetés sont bonnes.", "D) Les pommes que j'ai acheter sont bonnes."],
        "answer": "B",
        "explanation": "Le participe passé conjugué avec avoir s'accorde avec le COD s'il est placé avant le verbe."
    },
    {
        "question": "Complétez : 'Quels que ___ vos problèmes, vous devez avancer.'",
        "options": ["A) soit", "B) sois", "C) soient", "D) soyent"],
        "answer": "C",
        "explanation": "'Soient' s'accorde avec le sujet 'vos problèmes'."
    },
    {
        "question": "Laquelle de ces phrases contient une faute ?",
        "options": ["A) Elle s'est lavé les mains.", "B) Elle s'est lavée.", "C) Ils se sont parlés.", "D) Elles se sont souri."],
        "answer": "C",
        "explanation": "'Parler' est transitif indirect (parler à). Il n'y a pas d'accord du participe passé."
    },
    {
        "question": "Complétez : 'Je ne pense pas qu'il ___ venir demain.'",
        "options": ["A) peut", "B) puisse", "C) pourras", "D) pourra"],
        "answer": "B",
        "explanation": "La forme négative de 'penser que' entraîne généralement le subjonctif."
    },
    {
        "question": "Quel est le pluriel de 'un arc-en-ciel' ?",
        "options": ["A) des arcs-en-ciels", "B) des arc-en-ciel", "C) des arcs-en-ciel", "D) des arc-en-ciels"],
        "answer": "C",
        "explanation": "Seul le premier nom s'accorde, 'en ciel' est invariable."
    },
    {
        "question": "Complétez : 'Elles se sont ___ compte de leur erreur.'",
        "options": ["A) rendu", "B) rendue", "C) rendus", "D) rendues"],
        "answer": "A",
        "explanation": "L'expression 'se rendre compte' est invariable."
    },
    {
        "question": "Parmi ces phrases, laquelle emploie correctement le verbe 'pallier' ?",
        "options": ["A) Il faut pallier à ce manque.", "B) Il faut pallier ce manque.", "C) Il faut y pallier à.", "D) Il faut pallier contre ce manque."],
        "answer": "B",
        "explanation": "'Pallier' est un verbe transitif direct, on pallie quelque chose, pas 'à' quelque chose."
    },
    {
        "question": "Complétez : 'Même s'il ___ raison, je ne l'écouterais pas.'",
        "options": ["A) a", "B) ait", "C) avait", "D) aurait"],
        "answer": "C",
        "explanation": "Après 'même si', on emploie l'indicatif. L'imparfait ('avait') s'accorde avec le conditionnel ('écouterais')."
    },
    {
        "question": "Quelle est la conjugaison correcte au passé simple (3e personne du singulier) du verbe 'coudre' ?",
        "options": ["A) il cousit", "B) il cousa", "C) il coudit", "D) il couda"],
        "answer": "A",
        "explanation": "Le verbe coudre fait 'il cousit' au passé simple."
    },
    {
        "question": "Complétez : 'Il faut que nous ___ prêts à 8h.'",
        "options": ["A) sommes", "B) soyons", "C) serions", "D) soions"],
        "answer": "B",
        "explanation": "'Il faut que' est suivi du subjonctif."
    },
    {
        "question": "Identifiez la faute d'accord :",
        "options": ["A) Des demi-heures", "B) Une heure et demi", "C) Une demi-heure", "D) Deux heures et demie"],
        "answer": "B",
        "explanation": "On écrit 'une heure et demie' (demie s'accorde en genre avec heure)."
    },
    {
        "question": "Quel est le pluriel de 'un laissez-passer' ?",
        "options": ["A) des laissez-passers", "B) des laissez-passer", "C) des laissés-passer", "D) des laisses-passers"],
        "answer": "B",
        "explanation": "'Laissez-passer' est invariable car composé d'un verbe à l'impératif et d'un infinitif."
    },
    {
        "question": "Complétez : 'Je préfère qu'elle le ___ demain.'",
        "options": ["A) fait", "B) fera", "C) fasse", "D) fait"],
        "answer": "C",
        "explanation": "'Préférer que' appelle le subjonctif."
    },
    {
        "question": "Laquelle de ces formes verbales est correcte ?",
        "options": ["A) Je résou", "B) Je résouds", "C) Je résous", "D) Je résout"],
        "answer": "C",
        "explanation": "Au présent de l'indicatif, le verbe résoudre fait 'je résous'."
    },
    {
        "question": "Complétez : 'Elle a l'air ___.'",
        "options": ["A) sérieux", "B) sérieuse", "C) sérieusement", "D) sérieuxement"],
        "answer": "B",
        "explanation": "Avec un sujet animé féminin, l'adjectif s'accorde avec le sujet (Elle a l'air sérieuse = elle semble sérieuse)."
    },
    {
        "question": "Complétez : 'Il m'a dit qu'il ___ là demain.'",
        "options": ["A) sera", "B) serait", "C) est", "D) soit"],
        "answer": "B",
        "explanation": "Concordance des temps : verbe de la principale au passé (a dit), l'action future dans la subordonnée se met au conditionnel (futur dans le passé)."
    },
    {
        "question": "Quel est le participe présent du verbe 'savoir' ?",
        "options": ["A) savant", "B) sachant", "C) saveur", "D) savantement"],
        "answer": "B",
        "explanation": "Le participe présent de 'savoir' est 'sachant'."
    },
    {
        "question": "Complétez : 'Des personnes ___ intentionnées.'",
        "options": ["A) mal", "B) mals", "C) male", "D) males"],
        "answer": "A",
        "explanation": "L'adverbe 'mal' est invariable."
    },
    {
        "question": "Complétez : '___ intelligents qu'ils soient.'",
        "options": ["A) Tout", "B) Tous", "C) Toute", "D) Toutes"],
        "answer": "A",
        "explanation": "'Tout' devant un adjectif masculin pluriel commençant par une voyelle est adverbe et invariable."
    },
    {
        "question": "Complétez : 'Les enfants se sont ___ lavés.'",
        "options": ["A) tout", "B) tous", "C) toute", "D) toutes"],
        "answer": "B",
        "explanation": "Ici 'tous' est un pronom mis en apposition ou adverbe d'accord, 'tous' prend un 's' car c'est le pronom (tous les enfants)."
    },
    {
        "question": "Quelle phrase est mal ponctuée ?",
        "options": ["A) Marie, viens ici !", "B) Je crois, qu'il va pleuvoir.", "C) Cependant, il reste silencieux.", "D) Il est fatigué, car il a beaucoup travaillé."],
        "answer": "B",
        "explanation": "On ne met pas de virgule entre le verbe et la complétive introduite par 'que'."
    },
    {
        "question": "Conjugaison : 'Il ___ fallu que je m'en aille.'",
        "options": ["A) eu", "B) eut", "C) a eu", "D) eût"],
        "answer": "D",
        "explanation": "Subjonctif plus-que-parfait (souvent précédé du conditionnel ou imparfait, mais ici 'Il eût fallu' est le conditionnel passé 2e forme)."
    },
    {
        "question": "Complétez : 'Elle s'est ___ coupée au doigt.'",
        "options": ["A) fait", "B) faite", "C) faites", "D) fais"],
        "answer": "A",
        "explanation": "Le participe passé 'fait' suivi d'un infinitif est toujours invariable."
    },
    {
        "question": "Quel mot est invariable ?",
        "options": ["A) Pourpre", "B) Rose", "C) Orange", "D) Mauve"],
        "answer": "C",
        "explanation": "Les adjectifs de couleur dérivés de noms (fruit, fleur) sont invariables, comme 'orange' et 'marron'."
    },
    {
        "question": "Complétez : 'C'est l'un des meilleurs livres que j'___ lu.'",
        "options": ["A) ai", "B) aie", "C) ait", "D) a"],
        "answer": "B",
        "explanation": "Le superlatif ('le meilleur') entraîne souvent l'utilisation du subjonctif dans la subordonnée relative ('aie')."
    },
    {
        "question": "Trouvez l'erreur dans cette phrase :",
        "options": ["A) Je vais au bureau.", "B) Je vais en vélo.", "C) Je vais à bicyclette.", "D) Je vais à cheval."],
        "answer": "B",
        "explanation": "La règle traditionnelle exige la préposition 'à' pour les moyens de transport que l'on enfourche ('à vélo', 'à moto'). 'En' est pour ceux dans lesquels on entre."
    },
    {
        "question": "Complétez : 'Les jours se sont ___.'",
        "options": ["A) succédé", "B) succédés", "C) succédées", "D) succéder"],
        "answer": "A",
        "explanation": "Succéder est transitif indirect (succéder à). Le participe passé ne s'accorde pas."
    },
    {
        "question": "Complétez : 'Elle a chanté de ___ chansons.'",
        "options": ["A) belle", "B) belles", "C) beau", "D) beaux"],
        "answer": "B",
        "explanation": "'De' remplace 'des' devant un adjectif pluriel antéposé ('de belles chansons')."
    },
    {
        "question": "Identifiez le mot correctement écrit :",
        "options": ["A) cauchemard", "B) cauchemar", "C) cauchemmard", "D) cochemar"],
        "answer": "B",
        "explanation": "'Cauchemar' ne prend pas de 'd' à la fin."
    },
    {
        "question": "Complétez : 'C'est la ville ___ j'ai grandi.'",
        "options": ["A) qui", "B) que", "C) où", "D) dont"],
        "answer": "C",
        "explanation": "Le pronom relatif 'où' indique le lieu."
    },
    {
        "question": "Quel est le participe passé de 'moudre' ?",
        "options": ["A) moudit", "B) moulé", "C) moulu", "D) moudé"],
        "answer": "C",
        "explanation": "Le verbe moudre fait 'moulu' au participe passé."
    },
    {
        "question": "Complétez : 'Il faut s'attendre à ce qu'il ___ demain.'",
        "options": ["A) vient", "B) viendra", "C) vienne", "D) viendrait"],
        "answer": "C",
        "explanation": "'À ce que' est suivi du subjonctif."
    },
    {
        "question": "Accord : 'Elles se sont ___ des lettres.'",
        "options": ["A) envoyé", "B) envoyés", "C) envoyée", "D) envoyées"],
        "answer": "A",
        "explanation": "Elles ont envoyé quoi ? 'des lettres' (COD placé après le verbe). À qui ? 'se' (COI). Donc pas d'accord."
    },
    {
        "question": "Complétez : '___ les efforts qu'il a fournis, il a échoué.'",
        "options": ["A) Malgré de", "B) En dépit", "C) Malgré", "D) Quoique"],
        "answer": "C",
        "explanation": "'Malgré' s'emploie sans préposition."
    },
    {
        "question": "Quelle est la bonne conjugaison du verbe 'bouillir' au présent ?",
        "options": ["A) je bouille", "B) je bous", "C) je bouillis", "D) je bouil"],
        "answer": "B",
        "explanation": "Au présent de l'indicatif : je bous, tu bous, il bout."
    },
    {
        "question": "Laquelle de ces phrases contient un pléonasme ?",
        "options": ["A) Il monte en haut.", "B) Il est parti loin.", "C) Il parle fort.", "D) Il marche vite."],
        "answer": "A",
        "explanation": "'Monter en haut' est un pléonasme, car monter implique déjà une élévation."
    },
    {
        "question": "Complétez : 'Je doute qu'il ___ la vérité.'",
        "options": ["A) sait", "B) saura", "C) sache", "D) savais"],
        "answer": "C",
        "explanation": "Le verbe douter demande le subjonctif."
    },
    {
        "question": "Complétez : 'Il lui a donné les livres qu'il avait ___.'",
        "options": ["A) acheté", "B) achetés", "C) achetée", "D) achetées"],
        "answer": "B",
        "explanation": "Accord du participe avec 'qu'' (mis pour 'livres', masculin pluriel)."
    },
    {
        "question": "Complétez : 'Ces femmes se sont ___ compte de la situation.'",
        "options": ["A) rendues", "B) rendu", "C) rendus", "D) rendue"],
        "answer": "B",
        "explanation": "L'expression 'se rendre compte' est toujours invariable."
    },
    {
        "question": "Quel est le pluriel de 'un chef-d'œuvre' ?",
        "options": ["A) des chefs-d'œuvre", "B) des chef-d'œuvres", "C) des chefs-d'œuvres", "D) des chef-d'œuvre"],
        "answer": "A",
        "explanation": "Seul 'chef' prend le pluriel, 'd'œuvre' étant un complément du nom."
    },
    {
        "question": "Complétez : 'Il faut qu'ils ___ leurs devoirs.'",
        "options": ["A) font", "B) feront", "C) fasse", "D) fassent"],
        "answer": "D",
        "explanation": "Subjonctif présent, 3e personne du pluriel du verbe faire."
    },
    {
        "question": "Complétez : 'Je ne crois pas qu'elle ___ venir.'",
        "options": ["A) puisse", "B) peut", "C) pourra", "D) pût"],
        "answer": "A",
        "explanation": "'Croire' à la forme négative est suivi du subjonctif."
    },
    {
        "question": "Identifiez le mot invariable :",
        "options": ["A) demi", "B) demi-heure", "C) debout", "D) grand-mère"],
        "answer": "C",
        "explanation": "L'adverbe 'debout' est invariable."
    },
    {
        "question": "Accord : 'Elles se sont ___ les mains.'",
        "options": ["A) lavé", "B) lavées", "C) lavés", "D) lavée"],
        "answer": "A",
        "explanation": "Le COD 'les mains' est placé après le verbe pronominal, donc pas d'accord."
    },
    {
        "question": "Elles se sont ___ les mains.",
        "options": ["A) lavé", "B) lavés", "C) lavées", "D) lavée"],
        "answer": "A",
        "explanation": "COD (les mains) postposé, donc invariable."
    },
    {
        "question": "Les musiciens que j'ai ___ jouer.",
        "options": ["A) entendu", "B) entendus", "C) entendue", "D) entendues"],
        "answer": "B",
        "explanation": "Le COD fait l'action de jouer, accord."
    },
    {
        "question": "Les chansons que j'ai ___ chanter.",
        "options": ["A) entendu", "B) entendus", "C) entendue", "D) entendues"],
        "answer": "A",
        "explanation": "Le COD subit l'action, invariable."
    },
    {
        "question": "Ils se sont ___.",
        "options": ["A) succédés", "B) succédé", "C) succédées", "D) succédée"],
        "answer": "B",
        "explanation": "Transitif indirect (succéder à), invariable."
    },
    {
        "question": "Des robes ___.",
        "options": ["A) bleu clair", "B) bleues claires", "C) bleues clair", "D) bleu claires"],
        "answer": "A",
        "explanation": "Adjectifs de couleur composés invariables."
    },
    {
        "question": "Des chaussures ___.",
        "options": ["A) marrons", "B) marrons foncé", "C) marron", "D) marronnes"],
        "answer": "C",
        "explanation": "Nom employé comme adjectif, invariable."
    },
    {
        "question": "___ que soient ses excuses.",
        "options": ["A) Quel", "B) Quelles", "C) Quelque", "D) Quelques"],
        "answer": "B",
        "explanation": "Quel que s'accorde avec le sujet postposé."
    },
    {
        "question": "Des efforts, ___ intenses qu'ils soient.",
        "options": ["A) quelque", "B) quelques", "C) quel que", "D) quels que"],
        "answer": "A",
        "explanation": "Quelque adverbe devant adjectif = invariable."
    },
    {
        "question": "Des ___.",
        "options": ["A) chou-fleur", "B) chous-fleurs", "C) choux-fleur", "D) choux-fleurs"],
        "answer": "D",
        "explanation": "Nom + Nom = pluriel pour les deux."
    },
    {
        "question": "___ ses remarques.",
        "options": ["A) Nonobstant", "B) Non obstant", "C) Non-obstant", "D) N'obstant"],
        "answer": "A",
        "explanation": "Préposition invariable."
    },
    {
        "question": "Les années se sont ___.",
        "options": ["A) écoulées", "B) écoulé", "C) écoulés", "D) écoulée"],
        "answer": "A",
        "explanation": "Verbe essentiellement pronominal, accord sujet."
    },
    {
        "question": "Ils se sont ___ compte de l'erreur.",
        "options": ["A) rendus", "B) rendues", "C) rendu", "D) rendue"],
        "answer": "C",
        "explanation": "COD (compte) postposé."
    },
    {
        "question": "La robe qu'elle s'est ___.",
        "options": ["A) acheté", "B) achetée", "C) achetés", "D) achetées"],
        "answer": "B",
        "explanation": "COD (que = la robe) antéposé."
    },
    {
        "question": "La chaleur qu'il a ___.",
        "options": ["A) fait", "B) faite", "C) faits", "D) faites"],
        "answer": "A",
        "explanation": "Faire impersonnel toujours invariable."
    },
    {
        "question": "Les efforts qu'il a ___.",
        "options": ["A) fallu", "B) fallus", "C) fallue", "D) fallues"],
        "answer": "A",
        "explanation": "Falloir impersonnel invariable."
    },
    {
        "question": "Elles sont ___ surprises.",
        "options": ["A) tout", "B) toute", "C) toutes", "D) tous"],
        "answer": "C",
        "explanation": "Tout s'accorde devant adj féminin commençant par consonne."
    },
    {
        "question": "Elle était ___ étonnée.",
        "options": ["A) tout", "B) toute", "C) toutes", "D) tous"],
        "answer": "A",
        "explanation": "Tout devant adj féminin commençant par voyelle = invariable."
    },
    {
        "question": "Des enfants ___ à partir.",
        "options": ["A) près", "B) prêts", "C) prêt", "D) prêtent"],
        "answer": "B",
        "explanation": "Prêt à s'accorde avec le sujet."
    },
    {
        "question": "Il habite ___ de l'école.",
        "options": ["A) prêts", "B) près", "C) prêt", "D) prête"],
        "answer": "B",
        "explanation": "Près de = invariable."
    },
    {
        "question": "Il a agi ___.",
        "options": ["A) sciemment", "B) siemment", "C) csiemment", "D) sciement"],
        "answer": "A",
        "explanation": "Dérivé de scient, deux m."
    },
    {
        "question": "Il l'a demandé ___.",
        "options": ["A) instamment", "B) instament", "C) instantamment", "D) instamant"],
        "answer": "A",
        "explanation": "Adverbe de instant (faux, de instamment) -amment."
    },
    {
        "question": "Il faut qu'il ___.",
        "options": ["A) conclu", "B) conclue", "C) conclus", "D) conclut"],
        "answer": "B",
        "explanation": "Subjonctif de conclure."
    },
    {
        "question": "Bien qu'il ___ malade.",
        "options": ["A) est", "B) était", "C) soit", "D) fut"],
        "answer": "C",
        "explanation": "Bien que + subjonctif."
    },
    {
        "question": "Après qu'il ___ parti.",
        "options": ["A) soit", "B) est", "C) fût", "D) serait"],
        "answer": "B",
        "explanation": "Après que + indicatif."
    },
    {
        "question": "Le document ___ je parlais.",
        "options": ["A) que", "B) dont", "C) qui", "D) auquel"],
        "answer": "B",
        "explanation": "Parler de -> dont."
    },
    {
        "question": "Le collègue ___ je me suis adressé.",
        "options": ["A) au quel", "B) à qui", "C) de qui", "D) dont"],
        "answer": "B",
        "explanation": "S'adresser à une personne -> à qui."
    },
    {
        "question": "Il a ___ faim.",
        "options": ["A) grand", "B) grande", "C) grands", "D) grandement"],
        "answer": "A",
        "explanation": "Expression figée, invariable."
    },
    {
        "question": "Une chaleur ___.",
        "options": ["A) fatigante", "B) fatiguante", "C) fatigantes", "D) fatiguantes"],
        "answer": "A",
        "explanation": "Adjectif verbal sans u."
    },
    {
        "question": "Des arguments ___.",
        "options": ["A) convainquants", "B) convaincants", "C) convainquant", "D) convaincant"],
        "answer": "B",
        "explanation": "Adjectif verbal avec c."
    },
    {
        "question": "Il s'est coupé les cheveux ___.",
        "options": ["A) court", "B) courts", "C) cour", "D) courre"],
        "answer": "A",
        "explanation": "Adverbe invariable dans cette locution."
    },
    {
        "question": "C'est la ___ fois.",
        "options": ["A) vingt-et-unième", "B) vingt et unième", "C) vingtième et un", "D) vingt-unième"],
        "answer": "A",
        "explanation": "Traits d'union pour numéraux composés."
    },
    {
        "question": "Elles se sont ___ des fleurs.",
        "options": ["A) lancées", "B) lancés", "C) lancé", "D) lancée"],
        "answer": "C",
        "explanation": "COD (fleurs) postposé."
    },
    {
        "question": "Les pompiers, ___ preuve de courage.",
        "options": ["A) faisant", "B) faisants", "C) faisantes", "D) fait"],
        "answer": "A",
        "explanation": "Participe présent invariable."
    },
    {
        "question": "Quoi que tu ___.",
        "options": ["A) fait", "B) fais", "C) fasse", "D) fasses"],
        "answer": "D",
        "explanation": "Quoi que + subjonctif."
    },
    {
        "question": "Il l'a fait ___.",
        "options": ["A) exprès", "B) express", "C) expresse", "D) expressément"],
        "answer": "A",
        "explanation": "Adverbe invariable."
    },
    {
        "question": "Les documents ci-___.",
        "options": ["A) joint", "B) joints", "C) jointe", "D) jointes"],
        "answer": "B",
        "explanation": "Placé après le nom, s'accorde."
    },
    {
        "question": "Ci-___, les documents.",
        "options": ["A) joint", "B) joints", "C) jointe", "D) jointes"],
        "answer": "A",
        "explanation": "En tête de phrase, invariable."
    },
    {
        "question": "De ___ en mieux.",
        "options": ["A) mieu", "B) mieux", "C) meilleur", "D) meilleurs"],
        "answer": "B",
        "explanation": "Invariable."
    },
    {
        "question": "Il a fui ___.",
        "options": ["A) nuitamment", "B) nuitement", "C) nuitament", "D) nuitemment"],
        "answer": "A",
        "explanation": "De nuit, 2 m."
    },
    {
        "question": "Des enfants ___-nés.",
        "options": ["A) nouveau", "B) nouveaux", "C) nouvelle", "D) nouvelles"],
        "answer": "B",
        "explanation": "Nouveau s'accorde avec nés."
    },
    {
        "question": "Des fleurs ___-écloses.",
        "options": ["A) fraiches", "B) fraîche", "C) fraîches", "D) fraichement"],
        "answer": "C",
        "explanation": "Fraîches s'accorde en genre et nombre avec écloses."
    },
    {
        "question": "La femme que j'ai ___ chanter.",
        "options": ["A) entendu", "B) entendue", "C) entendus", "D) entendues"],
        "answer": "B",
        "explanation": "La femme fait l'action de chanter, s'accorde."
    },
    {
        "question": "Ils ont acheté de ___ beaux fruits.",
        "options": ["A) très", "B) de", "C) de très", "D) bien"],
        "answer": "C",
        "explanation": "Des devient de devant un adjectif pluriel."
    },
    {
        "question": "C'est l'une des filles qui ___ venues.",
        "options": ["A) est", "B) sont", "C) ont", "D) a"],
        "answer": "B",
        "explanation": "L'antécédent de qui est filles, donc pluriel."
    },
    {
        "question": "Il y a un grand nombre d'élèves qui ___.",
        "options": ["A) participe", "B) participent", "C) participés", "D) participé"],
        "answer": "B",
        "explanation": "L'accord se fait avec le complément du collectif (élèves)."
    },
    {
        "question": "Une foule de curieux ___.",
        "options": ["A) approchait", "B) approchaient", "C) Les deux", "D) Aucun"],
        "answer": "C",
        "explanation": "Accord possible avec le collectif ou le complément."
    },
    {
        "question": "La plupart ___ d'accord.",
        "options": ["A) est", "B) sont", "C) était", "D) sera"],
        "answer": "B",
        "explanation": "La plupart impose l'accord au pluriel."
    },
    {
        "question": "Choisissez la forme correcte :",
        "options": ["A) Ils se sont dit la vérité.", "B) Ils se sont dits la vérité.", "C) Ils se sont dite la vérité.", "D) Ils se sont dis la vérité."],
        "answer": "A",
        "explanation": "'Se' est COI (ils ont dit la vérité à eux-mêmes). 'la vérité', COD, est placé après, donc invariable."
    },
    {
        "question": "Trouvez la phrase correcte :",
        "options": ["A) Quoiqu'il soit riche, il est avare.", "B) Quoi qu'il soit riche, il est avare.", "C) Quoi qu'il est riche, il est avare.", "D) Quoiqu'il est riche, il est avare."],
        "answer": "A",
        "explanation": "'Quoique' en un seul mot signifie 'bien que' et appelle le subjonctif."
    },
    {
        "question": "Laquelle de ces phrases contient une erreur d'accord ?",
        "options": ["A) Les lettres qu'ils se sont envoyées.", "B) Elles se sont rendu compte de leur erreur.", "C) Les années se sont succédées rapidement.", "D) Ils se sont plu immédiatement."],
        "answer": "C",
        "explanation": "Le verbe 'se succéder' n'a jamais de COD (succéder à), le participe passé est donc toujours invariable : se sont succédé."
    },
    {
        "question": "Accord des adjectifs de couleur. Lequel est correct ?",
        "options": ["A) Des robes bleues claires", "B) Des robes bleu clair", "C) Des robes bleues clair", "D) Des robes bleu claires"],
        "answer": "B",
        "explanation": "Les adjectifs de couleur composés sont invariables."
    },
    {
        "question": "Comment écrit-on le nombre 300 en toutes lettres lorsqu'il n'est suivi d'aucun autre chiffre ?",
        "options": ["A) Trois cent", "B) Trois-cent", "C) Trois cents", "D) Trois-cents"],
        "answer": "C",
        "explanation": "Vingt et cent prennent la marque du pluriel quand ils sont multipliés par un nombre et qu'ils terminent l'adjectif numéral."
    },
    {
        "question": "Comment écrit-on 80 en toutes lettres ?",
        "options": ["A) Quatre-vingt", "B) Quatre-vingts", "C) Quatre vingts", "D) Quatre vingt"],
        "answer": "B",
        "explanation": "'Vingts' prend un 's' car il est multiplié par quatre et n'est suivi d'aucun autre nombre."
    },
    {
        "question": "Quel est le pluriel du mot composé 'un compte-gouttes' ?",
        "options": ["A) Des comptes-gouttes", "B) Des compte-gouttes", "C) Des comptes-goutte", "D) Des compte-goutte"],
        "answer": "B",
        "explanation": "'compte' est un verbe (invariable), 'gouttes' prend le pluriel (qui est d'ailleurs déjà présent au singulier)."
    },
    {
        "question": "Quel est le pluriel de 'chef-d'œuvre' ?",
        "options": ["A) Chefs-d'œuvre", "B) Chefs-d'œuvres", "C) Chef-d'œuvres", "D) Chef-d'œuvre"],
        "answer": "A",
        "explanation": "Seul le premier nom prend la marque du pluriel dans un nom composé d'un nom et de son complément prépositionnel."
    },
    {
        "question": "Identifiez la phrase sans erreur :",
        "options": ["A) Elles se sont arrogées des droits.", "B) Elles se sont arrogé des droits.", "C) Elles se sont arrogé de droits.", "D) Elles se sont arrogées de droits."],
        "answer": "B",
        "explanation": "Le verbe s'arroger (arroger à soi). 'des droits' est COD placé après, donc invariable."
    },
    {
        "question": "Laquelle de ces formes est correcte ?",
        "options": ["A) Des arc-en-ciels", "B) Des arcs-en-ciels", "C) Des arcs-en-ciel", "D) Des arc-en-ciel"],
        "answer": "B",
        "explanation": "Nom + préposition + nom : seul le premier nom varie. Les arcs qui sont dans le ciel."
    },
    {
        "question": "Choisissez la bonne graphie :",
        "options": ["A) Il faut qu'il résoud le problème.", "B) Il faut qu'il résolve le problème.", "C) Il faut qu'il résout le problème.", "D) Il faut qu'il résolusse le problème."],
        "answer": "B",
        "explanation": "Subjonctif présent du verbe résoudre."
    },
    {
        "question": "Quel est le participe passé de 's'enfuir' à la 3ème personne du pluriel au féminin ?",
        "options": ["A) se sont enfuies", "B) se sont enfui", "C) se sont enfuit", "D) se sont enfuis"],
        "answer": "A",
        "explanation": "Verbe essentiellement pronominal, s'accorde avec le sujet."
    },
    {
        "question": "Sélectionnez l'orthographe correcte pour 300 000 :",
        "options": ["A) Trois cents mille", "B) Trois-cents mille", "C) Trois cent mille", "D) Trois-cent mille"],
        "answer": "C",
        "explanation": "Cent est invariable s'il est suivi d'un autre nombre (ici, mille, qui est un adjectif numéral invariable)."
    },
    {
        "question": "Quel est l'accord correct ?",
        "options": ["A) Les pommes que j'ai vu tomber.", "B) Les pommes que j'ai vues tomber.", "C) Les pommes que j'ai vue tomber.", "D) Les pommes que j'ai vus tomber."],
        "answer": "B",
        "explanation": "Le COD 'que' (mis pour pommes) précède, et les pommes font l'action de tomber (sujet de l'infinitif), l'accord se fait."
    },
    {
        "question": "Accord avec laisser :",
        "options": ["A) Les arbres que j'ai laissé abattre.", "B) Les arbres que j'ai laissés abattre.", "C) Les arbres que j'ai laissées abattre.", "D) Les arbres que j'ai laissé abattus."],
        "answer": "A",
        "explanation": "Depuis la réforme de 1990, 'fait' et 'laissé' suivis d'un infinitif sont invariables."
    },
    {
        "question": "Laquelle de ces propositions est juste ?",
        "options": ["A) Ils se sont parler pendant des heures.", "B) Ils se sont parlés pendant des heures.", "C) Ils se sont parlé pendant des heures.", "D) Ils se sont parlées pendant des heures."],
        "answer": "C",
        "explanation": "Se parler à soi-même ou à l'un l'autre (COI). Donc invariable."
    },
    {
        "question": "Pluriel des mots composés : 'nouveau-né'.",
        "options": ["A) nouveaux-né", "B) nouveau-nés", "C) nouveaux-nés", "D) nouveau-nées"],
        "answer": "C",
        "explanation": "Les deux éléments (adjectif + participe passé/adjectif) s'accordent au pluriel."
    },
    {
        "question": "Laquelle de ces orthographes est correcte concernant le verbe asseoir ?",
        "options": ["A) Je m'assoies", "B) Je m'assied", "C) Je m'assois", "D) Je m'assié"],
        "answer": "C",
        "explanation": "Les deux formes 'je m'assois' et 'je m'assieds' sont valables, mais 'je m'assied' sans 's' est fautif."
    },
    {
        "question": "Identifiez l'erreur :",
        "options": ["A) Elle a l'air bête.", "B) Elle a l'air bêtes.", "C) Elle a l'air gentille.", "D) Ils ont l'air fatigués."],
        "answer": "B",
        "explanation": "L'adjectif s'accorde avec le sujet (Elle) ou avec 'air', mais ne prend pas de 's' si le sujet est singulier."
    },
    {
        "question": "Complétez la phrase : Il travaille d'arrache-...",
        "options": ["A) pieds", "B) pied", "C) pié", "D) piéd"],
        "answer": "A",
        "explanation": "La locution est 'd'arrache-pied' (invariable)."
    },
    {
        "question": "Trouvez la phrase correcte avec 'quelque' :",
        "options": ["A) Quelque soient vos raisons.", "B) Quelles que soient vos raisons.", "C) Quelques que soient vos raisons.", "D) Quels que soient vos raisons."],
        "answer": "B",
        "explanation": "'Quel que' s'écrit en deux mots devant le verbe être et s'accorde avec le sujet 'raisons' (féminin pluriel)."
    },
    {
        "question": "Orthographe des couleurs :",
        "options": ["A) Des yeux marrons", "B) Des yeux marron", "C) Des yeux marront", "D) Des yeux marrones"],
        "answer": "A",
        "explanation": "Marron vient d'un nom de fruit et est donc invariable en tant qu'adjectif de couleur."
    },
    {
        "question": "Accord avec 'avoir' :",
        "options": ["A) La chanson que j'ai entendu chanter.", "B) La chanson que j'ai entendue chanter.", "C) La chanson que j'ai entendue chantée.", "D) La chanson que j'ai entendu chantée."],
        "answer": "A",
        "explanation": "Le sujet de l'infinitif n'est pas la chanson (la chanson ne chante pas), donc le participe 'entendu' reste invariable."
    },
    {
        "question": "Sélectionnez la phrase contenant une erreur :",
        "options": ["A) Même les plus forts tombent.", "B) Ils sont arrivés eux-même.", "C) Nous l'avons fait nous-mêmes.", "D) Mêmes ses amis l'ont abandonné."],
        "answer": "D",
        "explanation": "'Même' placé avant un nom/pronom et signifiant 'y compris' est un adverbe invariable. On écrit 'Même ses amis'."
    },
    {
        "question": "Accord de 'tout' :",
        "options": ["A) Elle est tout étonnée.", "B) Elle est toute étonnée.", "C) Elle est toutes étonnée.", "D) Elle est touts étonnée."],
        "answer": "A",
        "explanation": "'Tout' adverbe ne s'accorde devant un adjectif féminin que si celui-ci commence par une consonne ou un h aspiré. 'étonnée' commence par une voyelle."
    },
    {
        "question": "Cochez la bonne forme :",
        "options": ["A) Des fleurs fraîches écloses", "B) Des fleurs fraîchement écloses", "C) Des fleurs fraîches éclose", "D) Des fleurs fraîche écloses"],
        "answer": "A",
        "explanation": "'Frais' employé adverbialement s'accorde exceptionnellement avec l'adjectif qui suit."
    },
    {
        "question": "Quelle phrase est correcte ?",
        "options": ["A) C'est nous qui avons décidé.", "B) C'est nous qui ont décidé.", "C) C'est nous qui a décidé.", "D) C'est nous qui avez décidé."],
        "answer": "A",
        "explanation": "Le verbe s'accorde avec l'antécédent du pronom relatif 'qui', soit 'nous' (1ère personne du pluriel)."
    },
    {
        "question": "Quel verbe est au conditionnel passé ?",
        "options": ["A) J'aurai fini", "B) J'avais fini", "C) J'aurais fini", "D) J'eus fini"],
        "answer": "C",
        "explanation": "Le conditionnel passé se forme avec l'auxiliaire au conditionnel présent (j'aurais) et le participe passé."
    },
    {
        "question": "Accord des participes passés :",
        "options": ["A) Les efforts qu'il a fallus", "B) Les efforts qu'il a fallu", "C) Les efforts qu'ils a fallu", "D) Les efforts qu'il as fallu"],
        "answer": "A",
        "explanation": "Le participe passé des verbes impersonnels (il a fallu, il a plu) est toujours invariable."
    },
    {
        "question": "Identifiez l'orthographe correcte du pluriel :",
        "options": ["A) Des gratte-ciels", "B) Des grattes-ciels", "C) Des gratte-ciel", "D) Des grattes-ciel"],
        "answer": "A",
        "explanation": "'Gratte' (verbe invariable) + 'ciel' (invariable car il n'y a qu'un ciel qu'on gratte)."
    },
    {
        "question": "Lequel de ces mots est féminin ?",
        "options": ["A) un tentacule", "B) un tubercule", "C) une scolopendre", "D) un termite"],
        "answer": "C",
        "explanation": "Scolopendre est de genre féminin, contrairement aux autres qui sont souvent confondus."
    },
    {
        "question": "Quel mot peut être masculin OU féminin (double genre) selon son sens ou nombre ?",
        "options": ["A) Orgue", "B) Termite", "C) Augure", "D) Aucun des trois"],
        "answer": "A",
        "explanation": "Orgue (comme amour et délice) est masculin au singulier et généralement féminin au pluriel (de belles orgues)."
    },
    {
        "question": "Complétez : 'Ces femmes se sont...'",
        "options": ["A) souri", "B) souris", "C) souries", "D) sourire"],
        "answer": "A",
        "explanation": "Se sourire à soi ou à un autre (COI), le participe passé reste invariable."
    },
    {
        "question": "Quelle phrase contient un verbe transitif direct ?",
        "options": ["A) Il parle à son frère.", "B) Elle mange une pomme.", "C) Nous allons à Paris.", "D) Ils obéissent aux règles."],
        "answer": "B",
        "explanation": "Manger quelque chose (ici une pomme, COD) -> verbe transitif direct."
    },
    {
        "question": "Que signifie la locution 'a priori' ?",
        "options": ["A) Au premier abord, avant toute expérience.", "A posteriori, après réflexion.", "C) Une priorité absolue.", "D) Une excuse non fondée."],
        "answer": "A",
        "explanation": "'a priori' (du latin) signifie au premier abord, en se fondant sur des données antérieures à l'expérience."
    },
    {
        "question": "Choisissez la proposition exacte :",
        "options": ["A) Il l'a convaincu.", "B) Il l'a convaincue.", "C) Il l'a convaincues.", "D) Cela dépend du contexte."],
        "answer": "D",
        "explanation": "Le participe s'accorde avec le pronom 'l'', il s'écrira 'convaincue' si 'l'' remplace une femme, et 'convaincu' si c'est un homme."
    },
    {
        "question": "Quelle est la bonne orthographe pour 92 ?",
        "options": ["A) Quatre-vingts-deux", "B) Quatre-vingt-deux", "C) Quatre-vingt deux", "D) Quatre-vingts deux"],
        "answer": "B",
        "explanation": "Le 's' de vingts tombe lorsqu'il est suivi d'un autre adjectif numéral (deux)."
    },
    {
        "question": "Parmi ces phrases, laquelle est correcte ?",
        "options": ["A) Les enfants dont je t'ai parlé sont ici.", "B) Les enfants dont je t'ai parlés sont ici.", "C) Les enfants dont je t'ai parlées sont ici.", "D) Les enfants que je t'ai parlé sont ici."],
        "answer": "A",
        "explanation": "Parler de quelqu'un (COI), donc pas d'accord. Le pronom relatif 'dont' remplace un COI."
    },
    {
        "question": "Comment conjuguer au conditionnel présent (1ère pers. singulier) : 'courir' ?",
        "options": ["A) Je courrais", "B) Je courais", "C) Je courrai", "D) Je courai"],
        "answer": "A",
        "explanation": "Le conditionnel présent de courir prend deux 'r' : je courrais (radical du futur + terminaisons de l'imparfait)."
    },
    {
        "question": "Indiquez l'accord correct :",
        "options": ["A) Des fleurs rouge sang", "B) Des fleurs rouges sang", "C) Des fleurs rouge sangs", "D) Des fleurs rouges sangs"],
        "answer": "A",
        "explanation": "Les adjectifs de couleur composés (rouge sang) sont toujours invariables."
    },
    {
        "question": "Quelle phrase présente un pléonasme ?",
        "options": ["A) Monter en haut.", "B) Sortir dehors.", "C) Descendre en bas.", "D) Toutes les réponses."],
        "answer": "D",
        "explanation": "Monter implique d'aller en haut, sortir implique d'aller dehors, descendre d'aller en bas. Ce sont tous des pléonasmes."
    },
    {
        "question": "Identifiez la proposition correcte pour le subjonctif imparfait :",
        "options": ["A) Que je fisse", "B) Que je fis", "C) Que je faisait", "D) Que je fasse"],
        "answer": "A",
        "explanation": "'Fisse' est la 1ère personne du singulier de l'imparfait du subjonctif du verbe faire."
    },
    {
        "question": "Quel est le pluriel de 'passe-partout' ?",
        "options": ["A) passe-partouts", "B) passes-partouts", "C) passe-partout", "D) passes-partout"],
        "answer": "A",
        "explanation": "Mot composé d'un verbe (passe) et d'un adverbe (partout). Le nom entier est donc invariable."
    },
    {
        "question": "Quelle locution est correcte pour dire 'à condition que' (avec subjonctif) ?",
        "options": ["A condition que tu viens.", "A condition que tu viennes.", "A condition que tu viendras.", "A condition que tu vienne."],
        "answer": "A",
        "explanation": "'A condition que' exige le subjonctif (tu viennes)."
    },
    {
        "question": "Orthographe correcte du pluriel de 'coffre-fort' ?",
        "options": ["A) coffre-forts", "B) coffres-fort", "C) coffres-forts", "D) coffre-fort"],
        "answer": "C",
        "explanation": "Nom + adjectif : les deux s'accordent au pluriel."
    },
    {
        "question": "Laquelle de ces phrases contient une faute d'orthographe ?",
        "options": ["A) Ils se sont rendu compte de l'erreur.", "B) Elle s'est lavé les mains.", "C) Elles se sont permises de répondre.", "D) Ils se sont écrit des lettres."],
        "answer": "C",
        "explanation": "Permettre à soi (COI) de faire quelque chose. Le participe passé doit être invariable : se sont permis."
    },
]

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
    },
    {
        "question": "Quelle relation sémantique lie « voiture » et « roue » ?",
        "options": ["A) Synonymie", "B) Holonymie / méronymie", "C) Antonymie", "D) Hyperonymie"],
        "answer": "B",
        "explanation": "Voiture est l'holonyme (le tout) ; roue en est le méronyme (une partie)."
    },
    {
        "question": "Quelle figure consiste à employer un mot concret pour désigner une réalité abstraite ?",
        "options": ["A) Synecdoque", "B) Métonymie", "C) Catachrèse", "D) Allégorie"],
        "answer": "D",
        "explanation": "L'allégorie représente une idée abstraite par une image concrète et symbolique."
    },
    {
        "question": "Quel phénomène illustre « couler » (aller au fond) et « couler » (du robinet) ?",
        "options": ["A) Homonymie", "B) Polysémie", "C) Paronymie", "D) Hétéronymie"],
        "answer": "B",
        "explanation": "Même mot, même origine étymologique, sens différents liés : polysémie."
    },
    {
        "question": "Quelle est la différence entre « injure » et « injure » verbale ?",
        "options": ["A) Ce sont des homonymes", "B) Ce sont des polysèmes (injustice / propos offensant)", "C) Ce sont des paronymes", "D) Ce sont des synonymes"],
        "answer": "B",
        "explanation": "« Injure » = polysémie : une injustice (sens juridique) ou une parole blessante (sens courant)."
    },
    {
        "question": "La phrase « Il fait un temps de chien » contient quelle figure ?",
        "options": ["A) Comparaison", "B) Métaphore figée (locution)", "C) Allégorie", "D) Synecdoque"],
        "answer": "B",
        "explanation": "C'est une métaphore lexicalisée (figée dans la langue) : « temps de chien » = très mauvais temps."
    },
    {
        "question": "Quel terme désigne un mot crée par abrègement comme « ciné » pour « cinéma » ?",
        "options": ["A) Acronyme", "B) Apocope", "C) Aphérèse", "D) Troncation"],
        "answer": "D",
        "explanation": "La troncation supprime une partie du mot. « Ciné » est une apocope (troncation finale)."
    },
    {
        "question": "Quelle relation existe entre « rapide » et « lent » ?",
        "options": ["A) Synonymie", "B) Antonymie graduable", "C) Méronymie", "D) Hyponymie"],
        "answer": "B",
        "explanation": "Rapide et lent sont des antonymes graduables : il existe des degrés entre les deux."
    },
    {
        "question": "Le mot « bœuf » au sens de « grand effort musical collectif » illustre quel phénomène ?",
        "options": ["A) Néologisme sémantique", "B) Métaphore lexicalisée", "C) Homonymie", "D) Paronymie"],
        "answer": "A",
        "explanation": "C'est un néologisme sémantique : un sens nouveau attribué à un mot existant."
    },
    {
        "question": "Quelle figure attribue à un objet les caractéristiques d'un être humain ?",
        "options": ["A) Allégorie", "B) Personnification", "C) Métonymie", "D) Antithèse"],
        "answer": "B",
        "explanation": "La personnification donne des traits humains à ce qui n'en a pas (ex. : « la mer rugit »)."
    },
    {
        "question": "Quel terme désigne la relation entre « tibia » et « jambe » ?",
        "options": ["A) Tibia est l'hyperonyme de jambe", "B) Tibia est le méronyme de jambe", "C) Tibia et jambe sont des cohyponymes", "D) Tibia est le synonyme de jambe"],
        "answer": "B",
        "explanation": "Le tibia est une partie (méronyme) de la jambe (holonyme)."
    },
    {
        "question": "Que désigne le phénomène de « dénotation » ?",
        "options": ["A) Le sens subjectif et émotionnel d'un mot", "B) Le sens objectif et littéral d'un mot", "C) Le sens figuré d'un mot", "D) L'ensemble des synonymes d'un mot"],
        "answer": "B",
        "explanation": "La dénotation est le sens premier, neutre et objectif d'un mot. La connotation est le sens subjectif."
    },
    {
        "question": "« Aimer » (affecter) et « aimer » (comme dans « j'aimerais ») illustrent quelle nuance ?",
        "options": ["A) Homonymie", "B) Polysémie avec registres différents", "C) Synonymie contextuelle", "D) Antonymie graduelle"],
        "answer": "B",
        "explanation": "Le même verbe « aimer » couvre plusieurs sens selon le contexte : polysémie."
    },
    {
        "question": "Quelle figure consiste à dire le contraire de ce qu'on pense avec une intention satirique ?",
        "options": ["A) Litote", "B) Euphémisme", "C) Antiphrase (ironie)", "D) Prétérition"],
        "answer": "C",
        "explanation": "L'antiphrase est la figure de l'ironie : on dit le contraire pour se moquer."
    },
    {
        "question": "Le mot « clé » dans « argument clé » est employé comme :",
        "options": ["A) Nom apposé", "B) Adjectif épithète par métaphore", "C) Adverbe", "D) Complément de nom"],
        "answer": "B",
        "explanation": "« Clé » est employé métaphoriquement comme un adjectif : l'argument essentiel."
    },
    {
        "question": "Quelle relation existe entre « voiture de sport » et « voiture » ?",
        "options": ["A) Holonymie", "B) Hyponymie", "C) Méronymie", "D) Synonymie"],
        "answer": "B",
        "explanation": "« Voiture de sport » est un hyponyme de « voiture » : terme spécifique inclus dans le terme général."
    },
    {
        "question": "Quel est l'antonyme complémentaire (non graduable) de « vivant » ?",
        "options": ["A) Faible", "B) Mort", "C) Silencieux", "D) Immobile"],
        "answer": "B",
        "explanation": "Vivant/mort est une antonymie complémentaire : pas de degré intermédiaire."
    },
    {
        "question": "Dans « il avale les kilomètres », quelle figure est utilisée ?",
        "options": ["A) Comparaison", "B) Métaphore", "C) Synecdoque", "D) Métonymie"],
        "answer": "B",
        "explanation": "C'est une métaphore : avaler des kilomètres = parcourir une grande distance facilement."
    },
    {
        "question": "Quel phénomène lexical explique que « souris » désigne à la fois un animal et un dispositif informatique ?",
        "options": ["A) Homonymie", "B) Néologisme sémantique", "C) Métaphore lexicalisée", "D) Emprunt"],
        "answer": "C",
        "explanation": "Le dispositif informatique a été appelé « souris » par métaphore avec le rongeur (forme et câble = queue)."
    },
    {
        "question": "Quelle est la particularité d'un mot épicène ?",
        "options": ["A) Il est invariable", "B) Il désigne indifféremment les deux sexes", "C) Il n'a pas de pluriel", "D) Il est toujours masculin"],
        "answer": "B",
        "explanation": "Un mot épicène a la même forme au masculin et au féminin (ex. : enfant, élève, artiste)."
    },
    {
        "question": "Quel est l'hypéronyme commun de « colère », « joie », « tristesse » ?",
        "options": ["A) Sentiment", "B) Pensée", "C) Action", "D) Sensation"],
        "answer": "A",
        "explanation": "Colère, joie et tristesse sont des hyponymes de « sentiment »."
    },
    {
        "question": "Dans « brûler les étapes », quelle figure de style est employée ?",
        "options": ["A) Synecdoque", "B) Catachrèse", "C) Métaphore lexicalisée", "D) Métonymie"],
        "answer": "C",
        "explanation": "C'est une métaphore figée dans l'usage : aller trop vite, sauter des étapes."
    },
    {
        "question": "Quel phénomène linguistique désigne l'apparition d'un nouveau mot dans la langue ?",
        "options": ["A) Archaïsme", "B) Néologisme", "C) Pléonasme", "D) Barbarisme"],
        "answer": "B",
        "explanation": "Un néologisme est un mot nouveau ou un sens nouveau donné à un mot existant."
    },
    {
        "question": "La relation entre « oiseau » et « aigle » est une relation de :",
        "options": ["A) Synonymie", "B) Méronymie", "C) Hyperonymie/hyponymie", "D) Antonymie"],
        "answer": "C",
        "explanation": "Oiseau est l'hyperonyme (terme général) ; aigle est l'hyponyme (terme spécifique)."
    },
    {
        "question": "Dans « la salle applaudit », quelle figure de style voit-on ?",
        "options": ["A) Métaphore", "B) Métonymie", "C) Synecdoque", "D) Antonomase"],
        "answer": "B",
        "explanation": "C'est une métonymie : la salle (le lieu) désigne les personnes qui s'y trouvent."
    },
    {
        "question": "Quel outil stylistique consiste à utiliser le nom d'une personne célèbre pour désigner une catégorie ?",
        "options": ["A) Métonymie", "B) Synecdoque", "C) Antonomase", "D) Allégorie"],
        "answer": "C",
        "explanation": "L'antonomase utilise un nom propre comme nom commun (ex. : un Harpagon = un avare)."
    },
    {
        "question": "Quel est le rapport sémantique entre « maison » et « toit » ?",
        "options": ["A) Holonymie/méronymie", "B) Hyperonymie/hyponymie", "C) Synonymie", "D) Antonymie"],
        "answer": "A",
        "explanation": "Maison est l'holonyme (le tout) ; toit en est le méronyme (une partie)."
    },
    {
        "question": "Quelle figure de style dit moins pour faire comprendre plus ?",
        "options": ["A) Hyperbole", "B) Euphémisme", "C) Litote", "D) Amplification"],
        "answer": "C",
        "explanation": "La litote atténue volontairement pour que le lecteur comprenne le contraire (ex. : Ce n'est pas mal = c'est bien)."
    },
    {
        "question": "Qu'est-ce qu'un archaïsme ?",
        "options": ["A) Un mot étranger intégré dans la langue", "B) Un mot vieilli qui n'est plus en usage courant", "C) Un mot récemment créé", "D) Un mot au sens contraire de son sens original"],
        "answer": "B",
        "explanation": "Un archaïsme est un mot ou une forme démodée, sortie de l'usage courant (ex. : « icelui »)."
    },
    {
        "question": "Quelle différence y a-t-il entre un synonyme total et un synonyme partiel ?",
        "options": ["A) Aucune différence", "B) Synonyme total = mêmes sens dans tous les contextes ; synonyme partiel = interchangeable seulement dans certains contextes", "C) Un synonyme total est toujours de même registre", "D) Les synonymes totaux n'existent pas"],
        "answer": "B",
        "explanation": "Les synonymes totaux (parfaits) sont rares. La plupart des synonymes sont partiels."
    },
    {
        "question": "Dans « les murs ont des oreilles », quelle figure de style est utilisée ?",
        "options": ["A) Métaphore", "B) Personnification", "C) Métonymie", "D) Hyperbole"],
        "answer": "B",
        "explanation": "On attribue aux murs un organe humain (oreilles) : personnification."
    },
    {
        "question": "Quel phénomène explique que « souris » (animal) et « souris » (sourire, 3e pers.) soient distincts ?",
        "options": ["A) Polysémie", "B) Homographie", "C) Synonymie", "D) Méronymie"],
        "answer": "B",
        "explanation": "Même graphie, prononciation identique, sens sans lien étymologique : homographie."
    },
    {
        "question": "Quel terme désigne la liste de termes généraux à spécifiques (animal → mammifère → chien → labrador) ?",
        "options": ["A) Taxinomie", "B) Synonymie", "C) Champ lexical", "D) Isotopie"],
        "answer": "A",
        "explanation": "Une taxinomie est une classification hiérarchique des termes du général au spécifique."
    },
    {
        "question": "Dans « il pleut des cordes », quelle figure est employée ?",
        "options": ["A) Comparaison", "B) Métaphore", "C) Hyperbole métaphorique", "D) Personnification"],
        "answer": "C",
        "explanation": "C'est une métaphore hyperbole : il pleut très fort (les cordes exagèrent l'image)."
    },
    {
        "question": "Quelle relation lie « mari » et « femme » sur le plan lexical ?",
        "options": ["A) Hétéronymie", "B) Antonymie complémentaire", "C) Synonymie contextuelle", "D) Holonymie"],
        "answer": "A",
        "explanation": "Mari/femme sont hétéronymes : sens liés (couple) mais radicaux différents."
    },
    {
        "question": "Quel est l'effet stylistique recherché dans une accumulation ?",
        "options": ["A) Simplifier", "B) Amplifier par une suite d'éléments de même nature", "C) Opposer deux idées", "D) Atténuer une réalité"],
        "answer": "B",
        "explanation": "L'accumulation (ou énumération) crée un effet d'intensité ou d'exhaustivité."
    },
    {
        "question": "Que signifie l'expression « avoir le cafard » ?",
        "options": ["A) Être joyeux", "B) Être mélancolique, déprimé", "C) Avoir peur des insectes", "D) Être bavard"],
        "answer": "B",
        "explanation": "« Avoir le cafard » est une métaphore figée signifiant être triste ou déprimé."
    },
    {
        "question": "Quelle est la caractéristique d'un oxymoron ?",
        "options": ["A) Répétition d'un même son", "B) Association de deux termes contradictoires", "C) Énumération croissante", "D) Personnification d'un objet"],
        "answer": "B",
        "explanation": "L'oxymoron unit deux mots de sens opposés (ex. : « une obscure clarté »)."
    },
    {
        "question": "Quel phénomène désigne un mot dont le sens a évolué positivement (mélioratif) au fil du temps ?",
        "options": ["A) Dépréciation", "B) Aménagement", "C) Amélioration sémantique", "D) Néologisme"],
        "answer": "C",
        "explanation": "Certains mots gagnent un sens plus positif avec le temps : c'est l'amélioration sémantique."
    },
    {
        "question": "Qu'est-ce que l'isotopie dans un texte ?",
        "options": ["A) Un ensemble de syllabes répétées", "B) La récurrence de traits sémantiques qui assurent la cohérence d'un texte", "C) L'utilisation de synonymes parfaits", "D) La répétition de la même figure de style"],
        "answer": "B",
        "explanation": "L'isotopie est la répétition de traits sémantiques identiques donnant sa cohérence thématique au texte."
    },
    {
        "question": "Dans « le crayon d'un enfant », quel type de relation désigne « de » ?",
        "options": ["A) Relation de possession", "B) Relation méronymique", "C) Relation hyperonymique", "D) Relation d'antonymie"],
        "answer": "A",
        "explanation": "Le génitif (de) indique ici une relation d'appartenance/possession."
    },
    {
        "question": "Quel mot est à la fois son propre antonyme (autoantonyme) ?",
        "options": ["A) Chaud", "B) Hôte", "C) Méchant", "D) Clair"],
        "answer": "B",
        "explanation": "« Hôte » peut désigner celui qui reçoit et celui qui est reçu : c'est un autoantonyme (ou contronyime)."
    },
    {
        "question": "Quelle figure de style consiste à interrompre brusquement son discours ?",
        "options": ["A) Ellipse", "B) Aposiopèse", "C) Prétérition", "D) Périphrase"],
        "answer": "B",
        "explanation": "L'aposiopèse est l'interruption brusque du discours, laissant la phrase en suspens."
    },
    {
        "question": "Quel procédé désigne l'emprunt d'un mot étranger tel quel dans la langue française ?",
        "options": ["A) Calque", "B) Néologisme", "C) Xénisme/emprunt direct", "D) Dérivation"],
        "answer": "C",
        "explanation": "L'emprunt direct intègre le mot étranger sans le traduire (ex. : weekend, marketing)."
    },
    {
        "question": "Quel est le contraire d'une hyperbole ?",
        "options": ["A) Litote", "B) Métaphore", "C) Antithèse", "D) Anaphore"],
        "answer": "A",
        "explanation": "La litote dit moins que la réalité (antiphrase atténuée) ; l'hyperbole dit plus : elles sont en quelque sorte opposées."
    },
    {
        "question": "Quel est le synonyme de 'prolixe' ?",
        "options": ["A) Concis", "B) Bavard", "C) Éloquent", "D) Silencieux"],
        "answer": "B",
        "explanation": "Quelqu'un de prolixe parle ou écrit beaucoup, de façon trop longue."
    },
    {
        "question": "Quel est l'antonyme de 'altruiste' ?",
        "options": ["A) Généreux", "B) Bienveillant", "C) Égoïste", "D) Héroïque"],
        "answer": "C",
        "explanation": "Altruiste signifie se consacrer aux autres, son opposé est égoïste."
    },
    {
        "question": "Choisissez le paronyme correct : 'Il y a une bonne ___ économique en ce moment.'",
        "options": ["A) conjecture", "B) conjoncture", "C) conjuration", "D) conjugaison"],
        "answer": "B",
        "explanation": "Une conjoncture est une situation qui résulte d'une rencontre de circonstances."
    },
    {
        "question": "Que signifie le mot 'abstrus' ?",
        "options": ["A) Difficile à comprendre", "B) Absurde", "C) Très évident", "D) Lourd"],
        "answer": "A",
        "explanation": "Abstrus se dit d'un concept ou d'un discours très obscur, difficile à comprendre."
    },
    {
        "question": "Analogie : L'oiseau est à la plume ce que le mouton est à ___",
        "options": ["A) L'herbe", "B) L'enclos", "C) La laine", "D) Le berger"],
        "answer": "C",
        "explanation": "La plume couvre l'oiseau comme la laine couvre le mouton."
    },
    {
        "question": "Quel mot est un synonyme de 'versatile' en français ?",
        "options": ["A) Polyvalent", "B) Changeant", "C) Talentueux", "D) Têtu"],
        "answer": "B",
        "explanation": "En français, 'versatile' signifie qui change souvent d'avis (faux ami avec l'anglais)."
    },
    {
        "question": "Quel est l'antonyme de 'éphémère' ?",
        "options": ["A) Passager", "B) Transitoire", "C) Pérenne", "D) Mortel"],
        "answer": "C",
        "explanation": "Pérenne signifie qui dure très longtemps ou toujours, à l'opposé d'éphémère."
    },
    {
        "question": "Complétez avec le bon paronyme : 'Il a subi une ___ de son salaire.'",
        "options": ["A) gradation", "B) dégradation", "C) rétrogradation", "D) amputation"],
        "answer": "D",
        "explanation": "On parle d'une amputation de salaire pour désigner une réduction importante. (Rétrogradation concerne le grade)."
    },
    {
        "question": "Que signifie 'pusillanime' ?",
        "options": ["A) Courageux", "B) Qui manque d'audace, craintif", "C) Très fort", "D) Maladif"],
        "answer": "B",
        "explanation": "Un individu pusillanime est timoré, il fuit les responsabilités ou le danger."
    },
    {
        "question": "Analogie : 'Livre' est à 'Bibliothèque' ce que 'Tableau' est à ___",
        "options": ["A) Pinceau", "B) Artiste", "C) Pinacothèque", "D) Cadre"],
        "answer": "C",
        "explanation": "Une pinacothèque est un musée ou un lieu où l'on conserve des peintures."
    },
    {
        "question": "Trouvez le synonyme de 'loquace' :",
        "options": ["A) Silencieux", "B) Volubile", "C) Laconique", "D) Taciturne"],
        "answer": "B",
        "explanation": "Volubile et loquace qualifient une personne qui parle beaucoup."
    },
    {
        "question": "Quel est l'antonyme de 'laconique' ?",
        "options": ["A) Bref", "B) Concis", "C) Prolixe", "D) Sommaire"],
        "answer": "C",
        "explanation": "Laconique signifie s'exprimer en peu de mots. Prolixe est son contraire."
    },
    {
        "question": "Choisissez le bon paronyme : 'Le suspect est entré par ___.'",
        "options": ["A) effraction", "B) infraction", "C) réfraction", "D) diffraction"],
        "answer": "A",
        "explanation": "Une effraction est le bris d'une clôture ou serrure pour s'introduire quelque part."
    },
    {
        "question": "Que signifie l'expression 'avoir des accointances' ?",
        "options": ["A) Avoir des dettes", "B) Avoir des relations familières avec quelqu'un", "C) Avoir de la chance", "D) Être fâché"],
        "answer": "B",
        "explanation": "Les accointances désignent des relations, souvent jugées péjorativement."
    },
    {
        "question": "Analogie : L'eau est à la soif ce que la nourriture est à ___",
        "options": ["A) La digestion", "B) L'appétit", "C) La faim", "D) La gastronomie"],
        "answer": "C",
        "explanation": "L'eau apaise la soif comme la nourriture apaise la faim."
    },
    {
        "question": "Quel est le sens du mot 'gargantuesque' ?",
        "options": ["A) Minuscule", "B) Démesuré, énorme", "C) Très bruyant", "D) Silencieux"],
        "answer": "B",
        "explanation": "Tiré du personnage Gargantua, signifie gigantesque, souvent lié à l'appétit."
    },
    {
        "question": "Quel est l'antonyme de 'endémique' ?",
        "options": ["A) Pandémique", "B) Indigène", "C) Sporadique", "D) Permanent"],
        "answer": "C",
        "explanation": "Endémique désigne quelque chose de constant dans une région, tandis que sporadique signifie dispersé, irrégulier."
    },
    {
        "question": "Paronymes : 'Il n'est pas permis d'___ les règles.'",
        "options": ["A) éluder", "B) élucider", "C) luder", "D) illuminer"],
        "answer": "A",
        "explanation": "Éluder signifie éviter, contourner habilement."
    },
    {
        "question": "Que signifie le mot 'iconoclaste' ?",
        "options": ["A) Qui détruit les images saintes, qui s'attaque aux croyances établies", "B) Qui adore les icônes", "C) Qui collectionne les images", "D) Qui peint des icônes"],
        "answer": "A",
        "explanation": "Un iconoclaste détruit les icônes ou rejette la tradition."
    },
    {
        "question": "Analogie : Chirurgien est à bistouri ce que menuisier est à ___",
        "options": ["A) Bois", "B) Forêt", "C) Rabot", "D) Meuble"],
        "answer": "C",
        "explanation": "Le rabot est l'outil du menuisier comme le bistouri est celui du chirurgien."
    },
    {
        "question": "Que veut dire 'ineffable' ?",
        "options": ["A) Qu'on ne peut pas effacer", "B) Qu'on ne peut exprimer par des mots", "C) Qui est inutile", "D) Qui ne peut pas faillir"],
        "answer": "B",
        "explanation": "Ineffable décrit ce qui est si intense ou extraordinaire qu'on ne peut le décrire (du latin ineffabilis)."
    },
    {
        "question": "Antonyme de 'opulent' :",
        "options": ["A) Riche", "B) Luxueux", "C) Indigent", "D) Fastueux"],
        "answer": "C",
        "explanation": "Indigent qualifie une personne qui manque du nécessaire (pauvre), contrairement à opulent (très riche)."
    },
    {
        "question": "Choisissez le bon mot : 'Il a fait une ___ dans son discours pour parler d'autre chose.'",
        "options": ["A) digression", "B) régression", "C) transgression", "D) agression"],
        "answer": "A",
        "explanation": "Une digression est un développement qui s'écarte du sujet principal."
    },
    {
        "question": "Que signifie 'obséquieux' ?",
        "options": ["A) Autoritaire", "B) Trop poli, hypocrite et flatteur", "C) Mortuaire", "D) Oublieux"],
        "answer": "B",
        "explanation": "Qui exagère les marques de politesse ou de respect, par servilité."
    },
    {
        "question": "Analogie : L'apiculteur est aux abeilles ce que le colombophile est aux ___",
        "options": ["A) Poissons", "B) Pigeons", "C) Moutons", "D) Chevaux"],
        "answer": "B",
        "explanation": "La colombophilie est l'élevage des pigeons voyageurs."
    },
    {
        "question": "Quel est le sens de 'frivole' ?",
        "options": ["A) Sérieux", "B) Léger, sans consistance, futile", "C) Ennuyeux", "D) Épais"],
        "answer": "B",
        "explanation": "Une chose ou une personne frivole manque de sérieux, s'attache à ce qui est futile."
    },
    {
        "question": "Quel est l'antonyme de 'veule' ?",
        "options": ["A) Faible", "B) Lâche", "C) Énergique", "D) Mou"],
        "answer": "C",
        "explanation": "Veule signifie qui n'a aucune énergie, aucune volonté. Son antonyme est énergique ou courageux."
    },
    {
        "question": "Choisissez le bon paronyme : 'Une explosion a eu lieu, c'est un véritable ___.'",
        "options": ["A) cataclysme", "B) catéchisme", "C) catalytique", "D) cataplasme"],
        "answer": "A",
        "explanation": "Un cataclysme est un grand bouleversement destructeur."
    },
    {
        "question": "Analogie : Pédiatre est à enfant ce que gériatre est à ___",
        "options": ["A) Femme", "B) Vieillard", "C) Animal", "D) Homme"],
        "answer": "B",
        "explanation": "Le gériatre est le médecin spécialisé pour les personnes âgées."
    },
    {
        "question": "Que signifie le mot 'acrimonie' ?",
        "options": ["A) Joie", "B) Aigreur, mauvaise humeur", "C) Harmonie", "D) Intelligence"],
        "answer": "B",
        "explanation": "L'acrimonie est un trait de caractère d'une personne aigrie, amère."
    },
    {
        "question": "Quel est l'antonyme de 'tacite' ?",
        "options": ["A) Implicite", "B) Sous-entendu", "C) Explicite", "D) Caché"],
        "answer": "C",
        "explanation": "Tacite signifie non exprimé (implicite). Son contraire est explicite."
    },
    {
        "question": "Paronymes : 'Il a reçu une belle ___ financière.'",
        "options": ["A) allocation", "B) allocution", "C) allégation", "D) allitération"],
        "answer": "A",
        "explanation": "Une allocation est une aide financière, une allocution est un discours."
    },
    {
        "question": "Que signifie 'véloce' ?",
        "options": ["A) Lent", "B) Qui va à bicyclette", "C) Rapide, agile", "D) Lourd"],
        "answer": "C",
        "explanation": "Véloce est un adjectif signifiant rapide."
    },
    {
        "question": "Analogie : Cécité est à la vue ce que surdité est à ___",
        "options": ["A) L'odorat", "B) L'ouïe", "C) La parole", "D) Le toucher"],
        "answer": "B",
        "explanation": "La surdité est la perte de l'ouïe."
    },
    {
        "question": "Synonyme de 'désuet' :",
        "options": ["A) Moderne", "B) Obsolete, passé de mode", "C) Inutile", "D) Sale"],
        "answer": "B",
        "explanation": "Ce qui est désuet n'est plus en usage, obsolète."
    },
    {
        "question": "Antonyme de 'indulgent' :",
        "options": ["A) Tolérant", "B) Sévère, intransigeant", "C) Clément", "D) Bon"],
        "answer": "B",
        "explanation": "L'indulgence est la disposition à excuser. Sévère ou intransigeant est le contraire."
    },
    {
        "question": "Paronyme : 'Il a commis une grave ___ de jugement.'",
        "options": ["A) erreur", "B) errements", "C) éruption", "D) irruption"],
        "answer": "A",
        "explanation": "Une erreur de jugement. (Les autres mots ne conviennent pas au sens)."
    },
    {
        "question": "Que veut dire 'dithyrambique' ?",
        "options": ["A) Très critique, sévère", "B) Très élogieux, enthousiaste", "C) Dépressif", "D) Ennuyeux"],
        "answer": "B",
        "explanation": "Dithyrambique qualifie un éloge enthousiaste et exalté."
    },
    {
        "question": "Analogie : L'architecte est au plan ce que le compositeur est à la ___",
        "options": ["A) Musique", "B) Chanson", "C) Partition", "D) Note"],
        "answer": "C",
        "explanation": "L'architecte écrit son œuvre sur un plan, le compositeur sur une partition."
    },
    {
        "question": "Synonyme de 'fallacieux' :",
        "options": ["A) Trompeur, illusoire", "B) Authentique", "C) Faisable", "D) Aisé"],
        "answer": "A",
        "explanation": "Ce qui est fallacieux cherche à tromper ou induire en erreur."
    },
    {
        "question": "Antonyme de 'exacerbé' :",
        "options": ["A) Atténué, apaisé", "B) Aggravé", "C) Exagéré", "D) Amplifié"],
        "answer": "A",
        "explanation": "Exacerber signifie rendre plus vif ou violent. Apaisé est son contraire."
    },
    {
        "question": "Paronymes : 'Il faut ___ les informations.'",
        "options": ["A) corrompre", "B) corroborer", "C) collaborer", "D) colporter"],
        "answer": "B",
        "explanation": "Corroborer signifie appuyer, renforcer une idée ou une information."
    },
    {
        "question": "Que signifie 'polymorphe' ?",
        "options": ["A) Qui n'a pas de forme", "B) Qui peut prendre plusieurs formes", "C) Qui aime les formes", "D) Qui est très grand"],
        "answer": "B",
        "explanation": "Du grec 'poly' (plusieurs) et 'morphè' (forme)."
    },
    {
        "question": "Analogie : Le bois est au menuisier ce que l'argile est au ___",
        "options": ["A) Potier", "B) Forgeron", "C) Verrier", "D) Peintre"],
        "answer": "A",
        "explanation": "Le potier modèle l'argile pour créer des objets."
    },
    {
        "question": "Synonyme de 'flegmatique' :",
        "options": ["A) Agité", "B) Colérique", "C) Calme, imperturbable", "D) Malade"],
        "answer": "C",
        "explanation": "Une personne flegmatique garde son sang-froid en toutes circonstances."
    },
    {
        "question": "Antonyme de 'sporadique' :",
        "options": ["A) Irrégulier", "B) Continu, régulier", "C) Épisodique", "D) Rare"],
        "answer": "B",
        "explanation": "Sporadique veut dire qui apparaît de façon irrégulière."
    },
    {
        "question": "Paronymes : 'Cet enfant est un véritable ___.'",
        "options": ["A) prodige", "B) prodigue", "C) profil", "D) profit"],
        "answer": "A",
        "explanation": "Un prodige est une personne extraordinairement douée. Prodigue signifie dépensier."
    },
    {
        "question": "Que signifie 'sycophante' ?",
        "options": ["A) Un instrument de musique", "B) Un délateur, un dénonciateur", "C) Un type d'arbre", "D) Une maladie"],
        "answer": "B",
        "explanation": "Dans la Grèce antique, délateur professionnel, et par extension un espion ou dénonciateur méprisable."
    },
    {
        "question": "Analogie : Pompier est à l'incendie ce que le policier est à la ___",
        "options": ["A) Sirène", "B) Voiture", "C) Criminalité", "D) Caserne"],
        "answer": "C",
        "explanation": "Le pompier combat l'incendie, le policier combat la criminalité."
    },
    {
        "question": "Que signifie 'Abstrus' ?",
        "options": ["A) Obscur", "B) Clair", "C) Lourd", "D) Triste"],
        "answer": "A",
        "explanation": "Difficile à comprendre."
    },
    {
        "question": "Antonyme de 'Prolixe' :",
        "options": ["A) Bavard", "B) Concis", "C) Sombre", "D) Vaste"],
        "answer": "B",
        "explanation": "Bref dans ses discours."
    },
    {
        "question": "Ciel est à Bleu ce que Sang est à :",
        "options": ["A) Rouge", "B) Cœur", "C) Liquide", "D) Veine"],
        "answer": "A",
        "explanation": "Couleur caractéristique."
    },
    {
        "question": "Que signifie 'Conjoncture' ?",
        "options": ["A) Hypothèse", "B) Situation globale", "C) Maladie", "D) Articulation"],
        "answer": "B",
        "explanation": "La situation économique ou politique."
    },
    {
        "question": "Il a fait une ___.",
        "options": ["A) conjecture", "B) conjoncture", "C) conjuration", "D) conjonctive"],
        "answer": "A",
        "explanation": "Une hypothèse."
    },
    {
        "question": "Il a su ___ l'argent.",
        "options": ["A) recouvrir", "B) recouvrer", "C) récupérer", "D) couvrir"],
        "answer": "B",
        "explanation": "Rentrer en possession (finances, santé)."
    },
    {
        "question": "Son arrivée est ___.",
        "options": ["A) éminente", "B) imminente", "C) iminente", "D) émanente"],
        "answer": "B",
        "explanation": "Qui va se produire bientôt."
    },
    {
        "question": "Un professeur ___.",
        "options": ["A) imminent", "B) éminent", "C) aminent", "D) émanent"],
        "answer": "B",
        "explanation": "Remarquable, supérieur."
    },
    {
        "question": "Que signifie 'Pallier' ?",
        "options": ["A) Résoudre", "B) Remédier provisoirement", "C) Remplacer", "D) Détruire"],
        "answer": "B",
        "explanation": "Remède temporaire (sans 'à')."
    },
    {
        "question": "Phrase correcte :",
        "options": ["A) Pallier au problème", "B) Pallier le problème", "C) Pallier du problème", "D) Pallier sur le problème"],
        "answer": "B",
        "explanation": "Verbe transitif direct."
    },
    {
        "question": "Synonyme de 'Laconique' :",
        "options": ["A) Bref", "B) Long", "C) Triste", "D) Joyeux"],
        "answer": "A",
        "explanation": "Exprimé en peu de mots."
    },
    {
        "question": "Que désigne 'Acception' ?",
        "options": ["A) Consentement", "B) Sens d'un mot", "C) Refus", "D) Erreur"],
        "answer": "B",
        "explanation": "Le sens dans lequel un mot est employé."
    },
    {
        "question": "Le mot 'Acceptation' désigne :",
        "options": ["A) Sens d'un mot", "B) Fait d'accepter", "C) Définition", "D) Pléonasme"],
        "answer": "B",
        "explanation": "L'action de consentir."
    },
    {
        "question": "Un repas organisé à son ___.",
        "options": ["A) attention", "B) intention", "C) inattention", "D) inttention"],
        "answer": "B",
        "explanation": "Pour lui faire honneur."
    },
    {
        "question": "Une lettre à l'___ du chef.",
        "options": ["A) intention", "B) attention", "C) inttention", "D) attension"],
        "answer": "B",
        "explanation": "Pour qu'il la lise."
    },
    {
        "question": "Que signifie 'Apanage' ?",
        "options": ["A) Privilège", "B) Désavantage", "C) Nourriture", "D) Décoration"],
        "answer": "A",
        "explanation": "Un bien ou avantage exclusif."
    },
    {
        "question": "Antonyme de 'Gargantuesque' :",
        "options": ["A) Frugal", "B) Homérique", "C) Énorme", "D) Dantesque"],
        "answer": "A",
        "explanation": "Repas simple et peu abondant."
    },
    {
        "question": "Synonyme de 'Pugnace' :",
        "options": ["A) Pacifique", "B) Combatif", "C) Lâche", "D) Peureux"],
        "answer": "B",
        "explanation": "Qui aime le combat."
    },
    {
        "question": "Un comportement 'Velléitaire' :",
        "options": ["A) Déterminé", "B) Hésitant", "C) Fort", "D) Rapide"],
        "answer": "B",
        "explanation": "Qui n'a pas la volonté de passer à l'acte."
    },
    {
        "question": "Que signifie 'Inanition' ?",
        "options": ["A) Absence de mouvement", "B) Manque de nourriture", "C) Folie", "D) Silence"],
        "answer": "B",
        "explanation": "Épuisement dû au manque de nourriture."
    },
    {
        "question": "Figure: 'Une obscure clarté'",
        "options": ["A) Oxymore", "B) Euphémisme", "C) Litote", "D) Pléonasme"],
        "answer": "A",
        "explanation": "Deux termes de sens contraire liés."
    },
    {
        "question": "Figure: 'Il nous a quittés' (pour mort)",
        "options": ["A) Euphémisme", "B) Litote", "C) Hyperbole", "D) Oxymore"],
        "answer": "A",
        "explanation": "Atténuation d'une réalité brutale."
    },
    {
        "question": "Figure: 'Je ne te hais point'",
        "options": ["A) Litote", "B) Euphémisme", "C) Allitération", "D) Comparaison"],
        "answer": "A",
        "explanation": "Dire moins pour suggérer plus."
    },
    {
        "question": "Qu'est-ce qu'un 'Acrostiche' ?",
        "options": ["A) Poème où les initiales forment un mot", "B) Vers de 12 syllabes", "C) Répétition de son", "D) Roman court"],
        "answer": "A",
        "explanation": "Initiales des vers lues verticalement."
    },
    {
        "question": "Adjectif 'Obséquieux' :",
        "options": ["A) Servile", "B) Funèbre", "C) Triste", "D) Rapide"],
        "answer": "A",
        "explanation": "Exagère la politesse par hypocrisie."
    },
    {
        "question": "Une 'Invective' :",
        "options": ["A) Insulte", "B) Compliment", "C) Outil", "D) Solution"],
        "answer": "A",
        "explanation": "Discours violent et injurieux."
    },
    {
        "question": "'Volubile' signifie :",
        "options": ["A) Parle beaucoup", "B) Vole", "C) Rond", "D) Changeant"],
        "answer": "A",
        "explanation": "Parle avec abondance et rapidité."
    },
    {
        "question": "Éphémère/Durable : Fictif/___",
        "options": ["A) Réel", "B) Virtuel", "C) Imaginaire", "D) Faux"],
        "answer": "A",
        "explanation": "Relation d'antonymie."
    },
    {
        "question": "Que signifie 'Fiduciaire' ?",
        "options": ["A) Basé sur la confiance", "B) Légal", "C) Solide", "D) Faux"],
        "answer": "A",
        "explanation": "Du latin fiducia, relatif à la confiance (monnaie)."
    },
    {
        "question": "Adjectif 'Bucolique' :",
        "options": ["A) Campagnard", "B) Marin", "C) Urbain", "D) Céleste"],
        "answer": "A",
        "explanation": "Relatif à la campagne, pastoral."
    },
    {
        "question": "Propos 'Dithyrambique' :",
        "options": ["A) Élogieux", "B) Critique", "C) Triste", "D) Court"],
        "answer": "A",
        "explanation": "Éloge très enthousiaste."
    },
    {
        "question": "Antonyme de 'Taciturne' :",
        "options": ["A) Loquace", "B) Silencieux", "C) Muet", "D) Sombre"],
        "answer": "A",
        "explanation": "Taciturne = qui parle peu. Loquace = bavard."
    },
    {
        "question": "'Tomber en désuétude' :",
        "options": ["A) N'être plus utilisé", "B) Se casser", "C) Être populaire", "D) Disparaître subitement"],
        "answer": "A",
        "explanation": "Ne plus être en usage."
    },
    {
        "question": "Intrus parmi synonymes de 'Pusillanime' :",
        "options": ["A) Hardi", "B) Timoré", "C) Couard", "D) Peureux"],
        "answer": "A",
        "explanation": "Hardi est l'antonyme (audacieux)."
    },
    {
        "question": "Que signifie 'Idoine' ?",
        "options": ["A) Approprié", "B) Stupide", "C) Ignorant", "D) Vaste"],
        "answer": "A",
        "explanation": "Qui convient parfaitement à la situation."
    },
    {
        "question": "Antonyme de 'Altruiste' :",
        "options": ["A) Égoïste", "B) Généreux", "C) Bon", "D) Saint"],
        "answer": "A",
        "explanation": "Contraire du dévouement à autrui."
    },
    {
        "question": "Propos 'Acerbe' :",
        "options": ["A) Blessant", "B) Doux", "C) Calme", "D) Court"],
        "answer": "A",
        "explanation": "Dur, piquant, acide."
    },
    {
        "question": "'Pécuniaire' est relatif à :",
        "options": ["A) L'argent", "B) La loi", "C) La santé", "D) L'art"],
        "answer": "A",
        "explanation": "De la pecunia (monnaie)."
    },
    {
        "question": "Il ne faut pas ___ la faute à d'autres.",
        "options": ["A) imputer", "B) amputer", "C) empoter", "D) impacter"],
        "answer": "A",
        "explanation": "Attribuer une faute."
    },
    {
        "question": "'Inhérent' :",
        "options": ["A) Lié de façon intime", "B) Extérieur", "C) Passager", "D) Lointain"],
        "answer": "A",
        "explanation": "Uni de façon inséparable."
    },
    {
        "question": "'Subreptice' :",
        "options": ["A) Furtif", "B) Légal", "C) Bruyant", "D) Long"],
        "answer": "A",
        "explanation": "Fait en cachette."
    },
    {
        "question": "Que désigne 'Apathie' ?",
        "options": ["A) Indifférence/Manque d'énergie", "B) Empathie", "C) Haine", "D) Peur"],
        "answer": "A",
        "explanation": "Absence de volonté et d'émotion."
    },
    {
        "question": "Une réponse 'Ambiguë' :",
        "options": ["A) À double sens", "B) Claire", "C) Longue", "D) Courte"],
        "answer": "A",
        "explanation": "Peut s'interpréter de plusieurs façons."
    },
    {
        "question": "'Véloce' :",
        "options": ["A) Rapide", "B) Lourd", "C) Méchant", "D) Fort"],
        "answer": "A",
        "explanation": "Agile, rapide."
    },
    {
        "question": "Qu'est-ce qu'un 'Pléonasme' ?",
        "options": ["A) Répétition de mots de même sens", "B) Mots contraires", "C) Rime", "D) Contresens"],
        "answer": "A",
        "explanation": "Exemple: descendre en bas."
    },
    {
        "question": "Un 'Syllogisme' :",
        "options": ["A) Raisonnement en 3 temps", "B) Poème", "C) Insulte", "D) Figure d'opposition"],
        "answer": "A",
        "explanation": "Déduction logique (prémisses + conclusion)."
    },
    {
        "question": "'Synergies' :",
        "options": ["A) Actions coordonnées", "B) Conflits", "C) Divergences", "D) Échecs"],
        "answer": "A",
        "explanation": "Effet combiné supérieur aux effets isolés."
    },
    {
        "question": "Que signifie 'Ajourner' ?",
        "options": ["A) Remettre à plus tard", "B) Annuler définitivement", "C) Accélérer", "D) Mettre au jour"],
        "answer": "A",
        "explanation": "Reporter à un autre jour."
    },
    {
        "question": "Quel est le synonyme de 'Déluré' ?",
        "options": ["A) Dégourdi", "B) Timide", "C) Hésitant", "D) Naïf"],
        "answer": "A",
        "explanation": "Déluré signifie dégourdi."
    },
    {
        "question": "Quel est le synonyme de 'Arbitraire' ?",
        "options": ["A) Juste", "B) Légal", "C) Discrétionnaire", "D) Logique"],
        "answer": "C",
        "explanation": "Arbitraire signifie discrétionnaire."
    },
    {
        "question": "Quel est l'antonyme de 'Prolixe' ?",
        "options": ["A) Bavard", "B) Laconique", "C) Éloquent", "D) Verbeux"],
        "answer": "B",
        "explanation": "Prolixe (bavard) a pour antonyme laconique (bref)."
    },
    {
        "question": "Quel est l'antonyme de 'Coordination' ?",
        "options": ["A) Entente", "B) Désorganisation", "C) Accord", "D) Harmonie"],
        "answer": "B",
        "explanation": "Désorganisation est l'antonyme de coordination."
    },
    {
        "question": "Quel est l'antonyme de 'Estimer' ?",
        "options": ["A) Évaluer", "B) Déprécier", "C) Juger", "D) Calculer"],
        "answer": "B",
        "explanation": "L'antonyme d'estimer est déprécier."
    },
    {
        "question": "Quel est le synonyme de 'Austère' ?",
        "options": ["A) Joyeux", "B) Luxueux", "C) Sévère", "D) Frivole"],
        "answer": "C",
        "explanation": "Austère est synonyme de sévère."
    },
    {
        "question": "Parmi les propositions, quel est l'antonyme de 'Austère' ?",
        "options": ["A) Sévère", "B) Luxueux", "C) Rigide", "D) Sobre"],
        "answer": "B",
        "explanation": "Luxueux ou Frivole sont des antonymes de austère."
    },
    {
        "question": "Quel est le synonyme de 'Magnanime' ?",
        "options": ["A) Rancunier", "B) Égoïste", "C) Généreux", "D) Cruel"],
        "answer": "C",
        "explanation": "Magnanime signifie généreux."
    },
    {
        "question": "Quel est l'antonyme de 'Magnanime' ?",
        "options": ["A) Généreux", "B) Altruiste", "C) Rancunier", "D) Bienveillant"],
        "answer": "C",
        "explanation": "Rancunier est l'antonyme de magnanime."
    },
    {
        "question": "Que signifie le mot 'Taciturne' ?",
        "options": ["A) Bavard", "B) Bruyant", "C) Silencieux", "D) Expressif"],
        "answer": "C",
        "explanation": "Taciturne est synonyme de silencieux."
    },
    {
        "question": "Quel est l'antonyme de 'Taciturne' ?",
        "options": ["A) Silencieux", "B) Mutique", "C) Bavard", "D) Renfermé"],
        "answer": "C",
        "explanation": "L'antonyme de taciturne est bavard."
    },
    {
        "question": "Que veut dire 'Succinct' ?",
        "options": ["A) Bref", "B) Détaillé", "C) Long", "D) Vaste"],
        "answer": "A",
        "explanation": "Succinct signifie bref."
    },
    {
        "question": "Quel est l'antonyme de 'Succinct' ?",
        "options": ["A) Bref", "B) Court", "C) Concis", "D) Détaillé"],
        "answer": "D",
        "explanation": "Détaillé est l'antonyme de succinct."
    },
    {
        "question": "Quel est le synonyme de 'Péremptoire' ?",
        "options": ["A) Hésitant", "B) Catégorique", "C) Douteux", "D) Souple"],
        "answer": "B",
        "explanation": "Péremptoire signifie catégorique."
    },
    {
        "question": "Quel est l'antonyme de 'Fallacieux' ?",
        "options": ["A) Trompeur", "B) Illusoire", "C) Sincère", "D) Mensonger"],
        "answer": "C",
        "explanation": "Sincère est l'antonyme de fallacieux."
    },
    {
        "question": "Comment s'écrit correctement le mot signifiant un choc violent ?",
        "options": ["A) Collusion", "B) Collision", "C) Colusion", "D) Colision"],
        "answer": "B",
        "explanation": "Une collision est un choc, à ne pas confondre avec collusion (entente secrète)."
    },
    {
        "question": "Que signifie le paronyme 'Collusion' ?",
        "options": ["A) Choc", "B) Accident", "C) Entente secrète", "D) Dispute"],
        "answer": "C",
        "explanation": "Une collusion est une entente secrète."
    },
    {
        "question": "Quelle est la définition de 'Conjoncture' ?",
        "options": ["A) Hypothèse", "B) Supposition", "C) Situation", "D) Conséquence"],
        "answer": "C",
        "explanation": "La conjoncture désigne une situation (ex: économique)."
    },
    {
        "question": "Quelle est la définition de 'Conjecture' ?",
        "options": ["A) Situation", "B) Hypothèse", "C) Fait avéré", "D) Preuve"],
        "answer": "B",
        "explanation": "Une conjecture est une hypothèse."
    },
    {
        "question": "Complétez : Des robes ___",
        "options": ["A) bleues ciel", "B) bleues ciels", "C) bleu ciel", "D) bleu ciels"],
        "answer": "C",
        "explanation": "Les adjectifs de couleur composés sont invariables (bleu ciel)."
    },
    {
        "question": "Complétez : Des vestes ___",
        "options": ["A) rouge sang", "B) rouges sangs", "C) rouges sang", "D) rouge sangs"],
        "answer": "A",
        "explanation": "Invariable car adjectif de couleur composé."
    },
    {
        "question": "Comment s'écrit le nombre 300 en lettres ?",
        "options": ["A) Trois cent", "B) Trois cents", "C) Trois-cents", "D) Trois-cent"],
        "answer": "B",
        "explanation": "Cent prend un s s'il est multiplié et termine le nombre (trois cents)."
    },
    {
        "question": "Comment s'écrit 82 en lettres ?",
        "options": ["A) Quatre-vingt-deux", "B) Quatre-vingts-deux", "C) Quatre-vingt deux", "D) Quatre vingts deux"],
        "answer": "A",
        "explanation": "Vingt ne prend pas de s car il ne termine pas le nombre (quatre-vingt-deux)."
    },
    {
        "question": "Comment s'écrit 300 000 en lettres ?",
        "options": ["A) Trois cents milles", "B) Trois cents mille", "C) Trois cent mille", "D) Trois cent milles"],
        "answer": "C",
        "explanation": "Cent est multiplié mais suivi de mille, donc invariable (trois cent mille)."
    },
    {
        "question": "Quel est le pluriel de 'chou-fleur' ?",
        "options": ["A) chou-fleur", "B) choux-fleur", "C) chou-fleurs", "D) choux-fleurs"],
        "answer": "D",
        "explanation": "Nom composé (nom+nom), les deux prennent la marque du pluriel."
    },
    {
        "question": "Quel est le pluriel de 'arc-en-ciel' ?",
        "options": ["A) arcs-en-ciel", "B) arc-en-ciels", "C) arcs-en-ciels", "D) arcs-en-cieux"],
        "answer": "A",
        "explanation": "Le premier mot (nom) prend la marque du pluriel, le second (complément) reste invariable."
    },
    {
        "question": "Quel est le pluriel de 'timbre-poste' ?",
        "options": ["A) timbre-postes", "B) timbres-postes", "C) timbres-poste", "D) timbre-poste"],
        "answer": "C",
        "explanation": "Pluriel : timbres-poste (des timbres pour la poste)."
    },
    {
        "question": "Complétez : Les pommes qu'il a ___",
        "options": ["A) mangé", "B) mangés", "C) mangées", "D) mangée"],
        "answer": "C",
        "explanation": "Le PP avec avoir s'accorde avec le COD placé avant (les pommes = féminin pluriel)."
    },
    {
        "question": "Complétez : Elles se sont ___ les mains.",
        "options": ["A) lavé", "B) lavés", "C) lavées", "D) lavée"],
        "answer": "A",
        "explanation": "Le COD (les mains) est placé après, le participe reste invariable."
    },
    {
        "question": "Complétez : Ils se sont ___ la vérité.",
        "options": ["A) dit", "B) dits", "C) dite", "D) dites"],
        "answer": "A",
        "explanation": "Le pronom 'se' est COI (ils ont dit la vérité à qui ? à eux-mêmes), donc invariable."
    },
    {
        "question": "Quelle figure de style consiste à feindre de ne pas dire ce qu'on exprime néanmoins ?",
        "options": ["A) Oxymore", "B) Prétérition", "C) Métaphore", "D) Hyperbole"],
        "answer": "B",
        "explanation": "C'est la prétérition."
    },
    {
        "question": "L'expression 'obscure clarté' est un exemple de :",
        "options": ["A) Pléonasme", "B) Litote", "C) Oxymore", "D) Euphémisme"],
        "answer": "C",
        "explanation": "Un oxymore relie deux mots de sens opposés."
    },
    {
        "question": "La phrase 'la nature est un temple' est un exemple de :",
        "options": ["A) Comparaison", "B) Métaphore", "C) Allégorie", "D) Personnification"],
        "answer": "B",
        "explanation": "C'est une métaphore car c'est une comparaison sans outil de comparaison."
    },
    {
        "question": "Dire 'je meurs de soif' relève de quelle figure de style ?",
        "options": ["A) Euphémisme", "B) Hyperbole", "C) Antithèse", "D) Chiasme"],
        "answer": "B",
        "explanation": "C'est une exagération, donc une hyperbole."
    },
    {
        "question": "Comment appelle-t-on l'emploi d'un mot déformé (ex: rénumérations) ?",
        "options": ["A) Solécisme", "B) Néologisme", "C) Barbarisme", "D) Archaïsme"],
        "answer": "C",
        "explanation": "C'est un barbarisme."
    },
    {
        "question": "Que désigne un 'janotisme' ou 'amphibologie' ?",
        "options": ["A) Une faute d'accord", "B) Une construction de phrase ambiguë", "C) Un mot inventé", "D) Une figure d'atténuation"],
        "answer": "B",
        "explanation": "C'est une phrase ambiguë prête à double sens."
    },
    {
        "question": "Quel mot parmi ces choix est un palindrome ?",
        "options": ["A) Avion", "B) Ressasser", "C) Bateau", "D) Refaire"],
        "answer": "B",
        "explanation": "Ressasser peut se lire dans les deux sens, c'est un palindrome."
    },
    {
        "question": "Que signifie la locution latine 'A priori' ?",
        "options": ["A) Après l'expérience", "B) Avant l'expérience", "C) Par conséquent", "D) Sans preuve"],
        "answer": "B",
        "explanation": "A priori signifie 'avant l'expérience'."
    },
    {
        "question": "Que signifie 'Casus belli' ?",
        "options": ["A) Cas de paix", "B) Raison d'État", "C) Motif de guerre", "D) Alliance militaire"],
        "answer": "C",
        "explanation": "Casus belli est un motif de guerre."
    },
    {
        "question": "Que signifie 'In vino veritas' ?",
        "options": ["A) La vie est dans le vin", "B) Le vin rend fort", "C) Le vin est dangereux", "D) La vérité est dans le vin"],
        "answer": "D",
        "explanation": "Cela signifie que l'alcool délie les langues et révèle la vérité."
    },
    {
        "question": "Quelle est la traduction de 'Pacta sunt servanda' ?",
        "options": ["A) Les pactes sont secrets", "B) Les contrats doivent être respectés", "C) Les alliances sont éphémères", "D) La paix est primordiale"],
        "answer": "B",
        "explanation": "Cette maxime juridique indique que les contrats lient les parties."
    },
    {
        "question": "Lequel de ces mots possède un double genre ?",
        "options": ["A) Augure", "B) Amour", "C) Termite", "D) Tubercule"],
        "answer": "B",
        "explanation": "Amour est de double genre (masculin au singulier, souvent féminin au pluriel dans la poésie)."
    },
    {
        "question": "Quel est le genre du mot 'scolopendre' ?",
        "options": ["A) Masculin", "B) Féminin", "C) Neutre", "D) Double genre"],
        "answer": "B",
        "explanation": "Scolopendre est de genre féminin (une scolopendre)."
    },
    {
        "question": "Quel est l'auteur de l'œuvre 'Climbié' ?",
        "options": ["A) Seydou Badian", "B) Sembène Ousmane", "C) Bernard Dadié", "D) Mongo Beti"],
        "answer": "C",
        "explanation": "Climbié a été écrit par Bernard Dadié."
    },
    {
        "question": "Qui a rédigé 'Le pauvre Christ de Bomba' ?",
        "options": ["A) Mongo Beti", "B) Ferdinand Oyono", "C) Camara Laye", "D) Bernard Dadié"],
        "answer": "A",
        "explanation": "Le pauvre Christ de Bomba est de Mongo Beti."
    },
    {
        "question": "Quel auteur a écrit 'Une vie de boy' ?",
        "options": ["A) Sembène Ousmane", "B) Seydou Badian", "C) Ferdinand Oyono", "D) Ahmadou Kourouma"],
        "answer": "C",
        "explanation": "L'auteur d'Une vie de boy est Ferdinand Oyono."
    },
    {
        "question": "De qui est l'ouvrage 'L'Enfant noir' ?",
        "options": ["A) Camara Laye", "B) Mongo Beti", "C) Bernard Dadié", "D) Seydou Badian"],
        "answer": "A",
        "explanation": "C'est le chef-d'œuvre de Camara Laye."
    },
    {
        "question": "Quel est l'antonyme de 'austère' ?",
        "options": ["A) Luxueux", "B) Sévère", "C) Péremptoire", "D) Déluré"],
        "answer": "A",
        "explanation": "Austère signifie dépourvu d'ornement, rigide. Son antonyme le plus commun dans ce contexte est luxueux ou fastueux."
    },
    {
        "question": "Dans la phrase 'Cette obscure clarté qui tombe des étoiles' (Corneille), quelle est la figure de style ?",
        "options": ["A) Oxymore", "B) Métaphore", "C) Antithèse", "D) Hyperbole"],
        "answer": "A",
        "explanation": "L'alliance de deux termes de sens opposés (obscure / clarté) dans un même syntagme est un oxymore."
    },
    {
        "question": "Que signifie l'expression 'péremptoire' ?",
        "options": ["A) Silencieux", "B) Catégorique", "C) Généreux", "D) Trompeur"],
        "answer": "B",
        "explanation": "Péremptoire : qui détruit d'avance toute objection, qui est catégorique."
    },
    {
        "question": "Trouvez le synonyme de 'fallacieux' :",
        "options": ["A) Véridique", "B) Succinct", "C) Trompeur", "D) Taciturne"],
        "answer": "C",
        "explanation": "Fallacieux vient du latin 'fallax' (trompeur) ; un argument fallacieux cherche à tromper, à induire en erreur."
    },
    {
        "question": "Que dénonce la locution latine 'casus belli' ?",
        "options": ["A) Un motif de guerre", "B) Un jugement final", "C) Une paix durable", "D) La vérité dans le vin"],
        "answer": "A",
        "explanation": "Casus belli se traduit par 'cas de guerre', l'acte de nature à déclencher un conflit."
    },
    {
        "question": "Que signifie la locution 'pacta sunt servanda' ?",
        "options": ["A) La chose est jugée.", "B) Les conventions doivent être respectées.", "C) La vérité est dans le vin.", "D) Avant toute expérience."],
        "answer": "B",
        "explanation": "C'est un principe fondamental du droit international : les pactes (traités) doivent être respectés."
    },
    {
        "question": "Lequel de ces couples de mots correspond à des paronymes ?",
        "options": ["A) Mer / Mère", "B) Collision / Collusion", "C) Grand / Petit", "D) Rapide / Véloce"],
        "answer": "B",
        "explanation": "Les paronymes sont des mots qui se ressemblent fortement par leur forme ou leur prononciation mais qui n'ont pas le même sens."
    },
    {
        "question": "Quelle est la figure de style dans : 'La nature est un temple où de vivants piliers...' ?",
        "options": ["A) Métonymie", "B) Comparaison", "C) Métaphore", "D) Oxymore"],
        "answer": "C",
        "explanation": "L'assimilation directe de la nature à un temple sans outil de comparaison ('comme') est une métaphore."
    },
    {
        "question": "Complétez l'analogie. Chien est à aboyer ce que Cheval est à :",
        "options": ["A) Hennir", "B) Bêler", "C) Mugir", "D) Rugir"],
        "answer": "A",
        "explanation": "Le cri du chien est l'aboiement, celui du cheval est le hennissement."
    },
    {
        "question": "La confusion entre deux paronymes s'appelle :",
        "options": ["A) Un barbarisme", "B) Une prétérition", "C) Une amphibologie", "D) Un solécisme"],
        "answer": "A",
        "explanation": "Le fait de forger un mot inexistant, de déformer un mot ou de confondre deux paronymes peut être qualifié de barbarisme lexical."
    },
    {
        "question": "L'auteur du roman 'Les Soleils des indépendances' est :",
        "options": ["A) Bernard Dadié", "B) Ahmadou Kourouma", "C) Mongo Beti", "D) Ferdinand Oyono"],
        "answer": "B",
        "explanation": "Publié en 1968, c'est l'œuvre majeure de l'Ivoirien Ahmadou Kourouma."
    },
    {
        "question": "Dans l'expression 'Je ne vous dirai pas que son intelligence est remarquable', il y a :",
        "options": ["A) Une litote", "B) Une prétérition", "C) Un euphémisme", "D) Une métaphore"],
        "answer": "B",
        "explanation": "La prétérition consiste à affirmer que l'on ne va pas dire quelque chose tout en le disant."
    },
    {
        "question": "Que signifie l'adjectif 'taciturne' ?",
        "options": ["A) Bruyant", "B) Silencieux", "C) Arrogant", "D) Frivole"],
        "answer": "B",
        "explanation": "Taciturne se dit d'une personne qui par nature parle peu, qui est silencieuse, souvent d'humeur sombre."
    },
    {
        "question": "Différence de sens entre 'conjoncture' et 'conjecture' :",
        "options": ["A) Situation économique / Hypothèse", "B) Hypothèse / Situation", "C) Affirmation / Négation", "D) Vrai / Faux"],
        "answer": "A",
        "explanation": "Conjoncture : situation, ensemble d'éléments (économiques, politiques). Conjecture : hypothèse, supposition."
    },
    {
        "question": "Quel écrivain africain a écrit 'Une vie de boy' ?",
        "options": ["A) Camara Laye", "B) Ferdinand Oyono", "C) Sembène Ousmane", "D) Seydou Badian"],
        "answer": "B",
        "explanation": "Roman publié en 1956 par le Camerounais Ferdinand Oyono."
    },
    {
        "question": "Quelle figure de style est présente dans 'Je meurs de soif' ?",
        "options": ["A) La litote", "B) La prétérition", "C) L'hyperbole", "D) La métaphore"],
        "answer": "C",
        "explanation": "L'hyperbole est une figure d'exagération (on ne meurt pas réellement à l'instant même de soif)."
    },
    {
        "question": "Qui a écrit 'Le Docker noir' ?",
        "options": ["A) Sembène Ousmane", "B) Bernard Dadié", "C) Mongo Beti", "D) Ahmadou Kourouma"],
        "answer": "A",
        "explanation": "Publié en 1956, c'est le premier roman de l'écrivain et cinéaste sénégalais Sembène Ousmane."
    },
    {
        "question": "Que signifie la locution 'in vino veritas' ?",
        "options": ["A) Le vin est un poison.", "B) La vérité est dans le vin.", "C) Le vin de la victoire.", "D) Acheter du vin."],
        "answer": "B",
        "explanation": "Proverbe latin signifiant qu'une personne ivre a tendance à dire la vérité ou ce qu'elle pense réellement."
    },
    {
        "question": "Si 'arbitraire' correspond à 'discrétionnaire', alors 'succinct' correspond à :",
        "options": ["A) Détaillé", "B) Bref", "C) Allongé", "D) Verbeux"],
        "answer": "B",
        "explanation": "Succinct signifie qui est énoncé en peu de mots, bref, concis."
    },
    {
        "question": "Le janotisme ou l'amphibologie désigne :",
        "options": ["A) Une construction syntaxique obscure à double sens.", "B) Un néologisme régional.", "C) Une figure d'exagération.", "D) Une faute d'orthographe."],
        "answer": "A",
        "explanation": "L'amphibologie est un double sens dû à la syntaxe ('J'ai vu un homme avec des jumelles')."
    },
    {
        "question": "Qui est l'auteur de 'Climbié' ?",
        "options": ["A) Bernard Dadié", "B) Camara Laye", "C) Mongo Beti", "D) Seydou Badian"],
        "answer": "A",
        "explanation": "Climbié est un roman largement autobiographique de l'écrivain ivoirien Bernard Dadié, paru en 1956."
    },
    {
        "question": "Le mot 'Kayak' est un exemple de :",
        "options": ["A) Métaphore", "B) Paronyme", "C) Palindrome", "D) Pléonasme"],
        "answer": "C",
        "explanation": "Comme 'radar', 'kayak' se lit de la même façon dans les deux sens."
    },
    {
        "question": "Quel écrivain guinéen est l'auteur de 'L'Enfant noir' (1953) ?",
        "options": ["A) Ahmadou Kourouma", "B) Camara Laye", "C) Sembène Ousmane", "D) Cheikh Hamidou Kane"],
        "answer": "B",
        "explanation": "Camara Laye a écrit ce célèbre roman autobiographique décrivant son enfance en Haute-Guinée."
    },
    {
        "question": "Que veut dire l'expression 'res judicata' ?",
        "options": ["A) La chose publique", "B) L'autorité de la chose jugée", "C) L'affaire en cours", "D) Le droit de juger"],
        "answer": "B",
        "explanation": "Res judicata pro veritate habetur (la chose jugée est tenue pour vérité), ce qui signifie qu'un jugement définitif ne peut être remis en cause."
    },
    {
        "question": "Complétez l'analogie : Le pauvre Mongo Beti est l'auteur de 'Le Pauvre Christ de Bomba', Seydou Badian est l'auteur de :",
        "options": ["A) Une vie de boy", "B) Sous l'orage", "C) Docker noir", "D) Climbié"],
        "answer": "B",
        "explanation": "Seydou Badian Kouyaté, écrivain et homme politique malien, est l'auteur de 'Sous l'orage'."
    },
    {
        "question": "Quel est le synonyme de l'adjectif 'véloce' ?",
        "options": ["A) Lent", "B) Rapide", "C) Agréable", "D) Cruel"],
        "answer": "B",
        "explanation": "Véloce (qui a de la vélocité) signifie rapide."
    },
    {
        "question": "Dans 'Elle est belle à mourir', quelle figure de style utilise-t-on ?",
        "options": ["A) La litote", "B) L'hyperbole", "C) La métaphore", "D) La métonymie"],
        "answer": "B",
        "explanation": "L'exagération 'à mourir' souligne l'intensité de la beauté, c'est une hyperbole."
    },
    {
        "question": "Si 'discrétionnaire' = 'arbitraire', alors 'taciturne' =",
        "options": ["A) Loquace", "B) Silencieux", "C) Affable", "D) Joyeux"],
        "answer": "B",
        "explanation": "Un synonyme direct."
    },
    {
        "question": "Le mot 'mémoire' (le document écrit) est de quel genre ?",
        "options": ["A) Féminin", "B) Masculin", "C) Neutre", "D) Variable"],
        "answer": "B",
        "explanation": "Un mémoire (document, écrit académique) est masculin. La mémoire (la faculté) est féminine."
    },
    {
        "question": "Que qualifie-t-on d' 'éphémère' ?",
        "options": ["A) Ce qui dure toujours", "B) Ce qui ne dure qu'un jour", "C) Ce qui est transparent", "D) Ce qui est lumineux"],
        "answer": "B",
        "explanation": "Éphémère (du grec ephemeros, d'un jour) qualifie ce qui a une durée très courte."
    },
    {
        "question": "Que veut dire le mot 'allégorie' ?",
        "options": ["A) Une fausse vérité", "B) La représentation d'une idée abstraite sous une forme concrète", "C) Une exagération manifeste", "D) L'omission d'une conjonction"],
        "answer": "B",
        "explanation": "Comme la faucheuse pour la mort, ou la balance pour la justice."
    },
    {
        "question": "Quel paronyme faut-il utiliser dans : 'Il a fait une ... pour expliquer la crise' ?",
        "options": ["A) conjoncture", "B) conjecture", "C) collision", "D) collusion"],
        "answer": "B",
        "explanation": "Conjecture = hypothèse, explication non vérifiée."
    },
    {
        "question": "Quel auteur africain a écrit 'Les Soleils des indépendances' ?",
        "options": ["A) Léopold Sédar Senghor", "B) Ahmadou Kourouma", "C) Wole Soyinka", "D) Tchicaya U Tam'si"],
        "answer": "B",
        "explanation": "Kourouma est l'auteur des Soleils des indépendances."
    },
    {
        "question": "Le mot 'voile' a un double genre. Quel est son sens au masculin ?",
        "options": ["A) Pièce de tissu pour faire avancer un bateau", "B) Pièce de tissu destinée à cacher, à recouvrir", "C) Le sport nautique", "D) Le dôme du palais"],
        "answer": "B",
        "explanation": "Un voile (pour cacher le visage ou mariée). La voile (bateau)."
    },
    {
        "question": "Que signifie l'adjectif 'dithyrambique' ?",
        "options": ["A) Très critique", "B) Élogieux, enthousiaste à l'excès", "C) Silencieux", "D) Avare"],
        "answer": "B",
        "explanation": "Faire des éloges emphatiques."
    },
    {
        "question": "Complétez la locution latine : 'Errare humanum est, perseverare ...'",
        "options": ["A) divinum", "B) diabolicum", "C) veritas", "D) absurdum"],
        "answer": "B",
        "explanation": "L'erreur est humaine, s'entêter [dans son erreur] est diabolique."
    },
    {
        "question": "Le néologisme consiste à :",
        "options": ["A) Emprunter un mot à une autre langue", "B) Créer un nouveau mot ou donner un sens nouveau à un mot existant", "C) Répéter un mot en fin de phrase", "D) Inverser l'ordre des mots"],
        "answer": "B",
        "explanation": "Néologisme : mot nouveau."
    },
    {
        "question": "Si 'prolixe' = 'bavard', 'laconique' =",
        "options": ["A) Triste", "B) Concis, bref", "C) Volubile", "D) Bavard"],
        "answer": "B",
        "explanation": "Laconique : qui s'exprime en peu de mots."
    },
    {
        "question": "L'expression 'c'est mon talon d'Achille' est :",
        "options": ["A) Une périphrase", "B) Une métaphore lexicalisée (ou allusion mythologique)", "C) Un pléonasme", "D) Un palindrome"],
        "answer": "B",
        "explanation": "Désigne le point faible de quelqu'un."
    },
    {
        "question": "Que désigne le terme 'synecdoque' ?",
        "options": ["A) Prendre le tout pour la partie ou la partie pour le tout", "B) Exagérer une vérité", "C) Remplacer un mot par un autre de même sonorité", "D) Parler de soi à la troisième personne"],
        "answer": "A",
        "explanation": "C'est un type particulier de métonymie."
    },
    {
        "question": "Parmi ces auteurs, lequel n'est pas ivoirien ?",
        "options": ["A) Bernard Dadié", "B) Ahmadou Kourouma", "C) Ferdinand Oyono", "D) Isaie Biton Koulibaly"],
        "answer": "C",
        "explanation": "Ferdinand Oyono est d'origine camerounaise."
    },
    {
        "question": "Quel mot n'a pas le double genre ?",
        "options": ["A) Manche", "B) Mémoire", "C) Livre", "D) Tentacule"],
        "answer": "D",
        "explanation": "Tentacule est exclusivement masculin."
    },
    {
        "question": "Un discours 'ampoulé' est un discours :",
        "options": ["A) Très clair et concis", "B) Éclairant et instructif", "C) Prétentieux, chargé, emphatique", "D) Dénué de sens"],
        "answer": "C",
        "explanation": "Style emphatique, boursouflé."
    },
    {
        "question": "L'antonyme de 'altruiste' est :",
        "options": ["A) Généreux", "B) Égoïste", "C) Taciturne", "D) Habile"],
        "answer": "B",
        "explanation": "L'altruisme est le dévouement aux autres, l'égoïsme est le contraire."
    },
    {
        "question": "Quel est le sens figuré de 'jeter l'éponge' ?",
        "options": ["A) Nettoyer", "B) Se fâcher", "C) Abandonner", "D) Vaincre"],
        "answer": "C",
        "explanation": "Issu de la boxe, jeter l'éponge signifie abandonner le combat."
    },
]

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
        "question": "Dans quel océan navigue-t-on au large de New York ?",
        "options": ["A) Océan Indien", "B) Océan Atlantique", "C) Océan Pacifique", "D) Océan Arctique"],
        "answer": "B",
        "explanation": "New York est située sur la côte est des États-Unis, au bord de l'Océan Atlantique."
    },
    {
        "question": "Quelle est la capitale de l'Afrique du Sud ?",
        "options": ["A) Johannesburg", "B) Le Cap", "C) Pretoria", "D) Durban"],
        "answer": "C",
        "explanation": "Pretoria est la capitale administrative (exécutive) de l'Afrique du Sud."
    },
    {
        "question": "Quel est le plus haut sommet du monde ?",
        "options": ["A) K2", "B) Kilimandjaro", "C) Everest", "D) Mont Blanc"],
        "answer": "C",
        "explanation": "L'Everest (8 849 m) est le plus haut sommet du monde, situé dans l'Himalaya."
    },
    {
        "question": "Quelle est la capitale du Kenya ?",
        "options": ["A) Mombasa", "B) Nairobi", "C) Kampala", "D) Dar es-Salaam"],
        "answer": "B",
        "explanation": "Nairobi est la capitale du Kenya."
    },
    {
        "question": "Quelle est la capitale du Nigeria ?",
        "options": ["A) Lagos", "B) Ibadan", "C) Abuja", "D) Kano"],
        "answer": "C",
        "explanation": "Abuja est la capitale politique du Nigeria depuis 1991 (remplaçant Lagos)."
    },
    {
        "question": "Quel est le plus long fleuve d'Afrique subsaharienne ?",
        "options": ["A) Le Congo", "B) Le Niger", "C) Le Zambèze", "D) Le Sénégal"],
        "answer": "B",
        "explanation": "Le Niger est le plus long fleuve d'Afrique subsaharienne (4 200 km)."
    },
    {
        "question": "En quelle année la Côte d'Ivoire a-t-elle été admise à l'ONU ?",
        "options": ["A) 1960", "B) 1961", "C) 1963", "D) 1965"],
        "answer": "A",
        "explanation": "La Côte d'Ivoire a été admise à l'ONU le 20 septembre 1960, l'année de son indépendance."
    },
    {
        "question": "Quel pays possède la plus grande forêt tropicale du monde ?",
        "options": ["A) La RDC", "B) L'Indonésie", "C) Le Brésil", "D) La Colombie"],
        "answer": "C",
        "explanation": "Le Brésil possède la plus grande forêt tropicale du monde : l'Amazonie."
    },
    {
        "question": "Quelle montagne est la plus haute d'Afrique ?",
        "options": ["A) Mont Kenya", "B) Kilimandjaro", "C) Ras Dashen", "D) Mont Cameroun"],
        "answer": "B",
        "explanation": "Le Kilimandjaro (5 895 m), en Tanzanie, est le point culminant d'Afrique."
    },
    {
        "question": "Quel pays d'Afrique de l'Ouest est le plus peuplé ?",
        "options": ["A) Ghana", "B) Sénégal", "C) Nigeria", "D) Côte d'Ivoire"],
        "answer": "C",
        "explanation": "Le Nigeria est le pays le plus peuplé d'Afrique et d'Afrique de l'Ouest (environ 220 millions d'hab.)."
    },
    {
        "question": "Sur quel continent se trouve le Sahara ?",
        "options": ["A) Asie", "B) Amérique du Sud", "C) Afrique", "D) Australie"],
        "answer": "C",
        "explanation": "Le Sahara, plus grand désert chaud du monde, se trouve en Afrique du Nord."
    },
    {
        "question": "Quelle est la monnaie officielle du Ghana ?",
        "options": ["A) Franc CFA", "B) Cedi", "C) Naira", "D) Dalasi"],
        "answer": "B",
        "explanation": "La monnaie du Ghana est le Cedi (GHS)."
    },
    {
        "question": "Quel pays d'Afrique partage ses frontières avec la Côte d'Ivoire au nord ?",
        "options": ["A) Le Ghana", "B) La Guinée", "C) Le Burkina Faso", "D) Le Mali"],
        "answer": "C",
        "explanation": "Le Burkina Faso est au nord de la Côte d'Ivoire. Le Mali est aussi voisin au nord-ouest."
    },
    {
        "question": "Quelle est la capitale de la Guinée ?",
        "options": ["A) Conakry", "B) Bissau", "C) Freetown", "D) Monrovia"],
        "answer": "A",
        "explanation": "Conakry est la capitale de la République de Guinée."
    },
    {
        "question": "Quel prix a reçu Nelson Mandela en 1993 ?",
        "options": ["A) Prix Nobel de la Paix", "B) Prix Nobel de Littérature", "C) Prix Nobel d'Économie", "D) Prix Pulitzer"],
        "answer": "A",
        "explanation": "Nelson Mandela a reçu le Prix Nobel de la Paix en 1993, partagé avec F. W. de Klerk."
    },
    {
        "question": "Quelle est la principale source d'énergie de la Côte d'Ivoire ?",
        "options": ["A) L'énergie nucléaire", "B) Le pétrole", "C) L'hydroélectricité et le gaz", "D) Le charbon"],
        "answer": "C",
        "explanation": "La CI tire l'essentiel de son énergie de l'hydroélectricité (Taabo, Kossou) et du gaz naturel."
    },
    {
        "question": "Qui a inventé le téléphone ?",
        "options": ["A) Thomas Edison", "B) Alexander Graham Bell", "C) Nikola Tesla", "D) James Watt"],
        "answer": "B",
        "explanation": "Alexander Graham Bell est généralement crédité de l'invention du téléphone (1876)."
    },
    {
        "question": "Quel est le nom de la lagune sur laquelle se trouve Abidjan ?",
        "options": ["A) Lagune Ébrié", "B) Lagune de Grand-Lahou", "C) Lagune Ouladine", "D) Lagune de Fresco"],
        "answer": "A",
        "explanation": "Abidjan est construite autour de la lagune Ébrié."
    },
    {
        "question": "Quel philosophe a énoncé « Je pense donc je suis » ?",
        "options": ["A) Kant", "B) Descartes", "C) Locke", "D) Hegel"],
        "answer": "B",
        "explanation": "René Descartes a formulé « Cogito ergo sum » (Je pense donc je suis) dans ses Méditations."
    },
    {
        "question": "Quel est le plus grand océan du monde ?",
        "options": ["A) Atlantique", "B) Indien", "C) Arctique", "D) Pacifique"],
        "answer": "D",
        "explanation": "L'océan Pacifique est le plus grand et le plus profond des océans."
    },
    {
        "question": "En quelle année a eu lieu la Conférence de Berlin qui a partagé l'Afrique ?",
        "options": ["A) 1878", "B) 1884-1885", "C) 1900", "D) 1910"],
        "answer": "B",
        "explanation": "La Conférence de Berlin (1884-1885) a organisé le partage colonial de l'Afrique entre puissances européennes."
    },
    {
        "question": "Quel est le plus grand désert froid du monde ?",
        "options": ["A) Sahara", "B) Gobi", "C) Antarctique", "D) Atacama"],
        "answer": "C",
        "explanation": "L'Antarctique est le plus grand désert (froid) du monde avec 14,2 millions de km²."
    },
    {
        "question": "Quel pays d'Afrique possède la plus grande économie ?",
        "options": ["A) Afrique du Sud", "B) Égypte", "C) Nigeria", "D) Kenya"],
        "answer": "C",
        "explanation": "Le Nigeria est la première économie africaine en termes de PIB nominal."
    },
    {
        "question": "Quel est le nom du port autonome d'Abidjan ?",
        "options": ["A) Port de San Pedro", "B) Port Bouët", "C) Port Autonome d'Abidjan (PAA)", "D) Port de Vridi"],
        "answer": "C",
        "explanation": "Le Port Autonome d'Abidjan (PAA) est le premier port d'Afrique de l'Ouest."
    },
    {
        "question": "Quel est l'arbre emblématique des savanes africaines ?",
        "options": ["A) Baobab", "B) Iroko", "C) Palmier", "D) Acacia"],
        "answer": "A",
        "explanation": "Le baobab est l'arbre emblématique des savanes et régions semi-arides d'Afrique."
    },
    {
        "question": "Où se situe la basilique Notre-Dame de la Paix de Yamoussoukro ?",
        "options": ["A) Abidjan", "B) Bouaké", "C) Yamoussoukro", "D) Daloa"],
        "answer": "C",
        "explanation": "La basilique Notre-Dame de la Paix, la plus grande basilique au monde, est à Yamoussoukro."
    },
    {
        "question": "Quel est le nom du premier chef de gouvernement ivoirien (Premier ministre) après 1990 ?",
        "options": ["A) Alassane Ouattara", "B) Laurent Gbagbo", "C) Henri Konan Bédié", "D) Daniel Kablan Duncan"],
        "answer": "A",
        "explanation": "Alassane Ouattara a été le premier Premier ministre de Côte d'Ivoire (1990-1993) sous Houphouët-Boigny."
    },
    {
        "question": "En quelle année la Côte d'Ivoire a-t-elle accueilli le Sommet Afrique-France ?",
        "options": ["A) 1999", "B) 2014", "C) 2021", "D) 1982"],
        "answer": "B",
        "explanation": "Le sommet Afrique-France s'est tenu à Paris en 2014. Abidjan a accueilli ce sommet en 2008."
    },
    {
        "question": "Quel est le principal produit agricole d'exportation de la Côte d'Ivoire ?",
        "options": ["A) Café", "B) Coton", "C) Cacao", "D) Anacarde"],
        "answer": "C",
        "explanation": "La Côte d'Ivoire est le premier producteur mondial de cacao (environ 40% de la production mondiale)."
    },
    {
        "question": "Quelle rivière délimite en partie la frontière entre la Côte d'Ivoire et le Ghana ?",
        "options": ["A) Le Sassandra", "B) Le Bandama", "C) La Bia/Comoé", "D) Le Cavally"],
        "answer": "C",
        "explanation": "Le fleuve Comoé/Bia forme en partie la frontière entre la Côte d'Ivoire et le Ghana."
    },
    {
        "question": "Quel est l'animal emblème de la Côte d'Ivoire ?",
        "options": ["A) Le lion", "B) L'éléphant", "C) Le guépard", "D) La panthère"],
        "answer": "B",
        "explanation": "L'éléphant est l'animal emblème de la Côte d'Ivoire, d'où le nom « Les Éléphants » pour l'équipe nationale de football."
    },
    {
        "question": "Quel scientifique a établi la théorie de la relativité générale ?",
        "options": ["A) Isaac Newton", "B) Albert Einstein", "C) Niels Bohr", "D) Max Planck"],
        "answer": "B",
        "explanation": "Albert Einstein a publié la théorie de la relativité générale en 1915."
    },
    {
        "question": "Quel est l'hymne national de la Côte d'Ivoire ?",
        "options": ["A) Abidjanaise", "B) L'Abidjanaise", "C) Côte d'Ivoire", "D) La terre de l'espérance"],
        "answer": "B",
        "explanation": "L'hymne national de la Côte d'Ivoire est « L'Abidjanaise »."
    },
    {
        "question": "En quelle année a eu lieu la découverte de l'Amérique par Christophe Colomb ?",
        "options": ["A) 1492", "B) 1498", "C) 1504", "D) 1488"],
        "answer": "A",
        "explanation": "Christophe Colomb a atteint les Bahamas le 12 octobre 1492."
    },
    {
        "question": "Quel est le nom de la communauté villageoise traditionnelle en Côte d'Ivoire ?",
        "options": ["A) Le kpando", "B) Le village", "C) La chefferie", "D) Le dozo"],
        "answer": "C",
        "explanation": "La chefferie traditionnelle est l'unité de base de l'organisation sociale en Côte d'Ivoire."
    },
    {
        "question": "Quelle est la surface totale de la Côte d'Ivoire ?",
        "options": ["A) 222 000 km²", "B) 322 463 km²", "C) 150 000 km²", "D) 410 000 km²"],
        "answer": "B",
        "explanation": "La Côte d'Ivoire couvre environ 322 463 km²."
    },
    {
        "question": "Quel est le nom du Président du Liberia qui a reçu le Prix Nobel de la Paix en 2011 ?",
        "options": ["A) Charles Taylor", "B) Ellen Johnson Sirleaf", "C) George Weah", "D) Samuel Doe"],
        "answer": "B",
        "explanation": "Ellen Johnson Sirleaf, première femme présidente africaine, a reçu le Prix Nobel de la Paix en 2011."
    },
    {
        "question": "Dans quel pays se trouve le mont Olympe, montagne sacrée des dieux grecs ?",
        "options": ["A) Turquie", "B) Albanie", "C) Grèce", "D) Macédoine du Nord"],
        "answer": "C",
        "explanation": "Le mont Olympe (2917 m), le plus haut sommet de Grèce, était la demeure des dieux dans la mythologie grecque."
    },
    {
        "question": "Quel est le nom de l'aéroport international de la ville d'Abidjan ?",
        "options": ["A) Aéroport de Port-Bouët", "B) Aéroport Félix Houphouët-Boigny", "C) Aéroport d'Abidjan-Plateau", "D) Aéroport de Cocody"],
        "answer": "B",
        "explanation": "L'aéroport international d'Abidjan porte le nom de Félix Houphouët-Boigny."
    },
    {
        "question": "Quelle est la superficie totale de la Côte d'Ivoire ?",
        "options": ["A) 322 462 km²", "B) 322 463 km²", "C) 324 462 km²", "D) 324 463 km²"],
        "answer": "B",
        "explanation": "La superficie de la Côte d'Ivoire est exactement de 322 463 km²."
    },
    {
        "question": "Qui fut le premier explorateur français à signer des traités avec les chefs côtiers en Côte d'Ivoire en 1843 ?",
        "options": ["A) Louis-Gustave Binger", "B) Marcel Treich-Laplène", "C) Arthur Verdier", "D) Louis-Édouard Bouët-Willaumez"],
        "answer": "D",
        "explanation": "L'Amiral Bouët-Willaumez a signé les premiers traités de protectorat sur la côte en 1843."
    },
    {
        "question": "En quelle année la Côte d'Ivoire est-elle devenue une colonie française autonome ?",
        "options": ["A) 1889", "B) 1893", "C) 1904", "D) 1946"],
        "answer": "B",
        "explanation": "La Côte d'Ivoire est érigée en colonie française le 10 mars 1893 avec Binger comme premier gouverneur."
    },
    {
        "question": "Quel est le point culminant de la Côte d'Ivoire ?",
        "options": ["A) Mont Tonkoui", "B) Mont Nimba", "C) Mont Momi", "D) Mont Zo"],
        "answer": "B",
        "explanation": "Le Mont Nimba, situé à la frontière avec la Guinée, est le point culminant à 1752 m."
    },
    {
        "question": "Lequel de ces fleuves ivoiriens est le plus long ?",
        "options": ["A) Le Cavally", "B) Le Sassandra", "C) Le Bandama", "D) La Comoé"],
        "answer": "C",
        "explanation": "Le Bandama, coulant entièrement sur le territoire ivoirien, est considéré comme le plus long fleuve du pays (environ 1050 km)."
    },
    {
        "question": "Quelle ville est reconnue comme la capitale économique de la Côte d'Ivoire ?",
        "options": ["A) Yamoussoukro", "B) Bouaké", "C) San-Pédro", "D) Abidjan"],
        "answer": "D",
        "explanation": "Abidjan est la capitale économique, bien que Yamoussoukro soit la capitale politique depuis 1983."
    },
    {
        "question": "Qui a composé l'Abidjanaise, l'hymne national de la Côte d'Ivoire ?",
        "options": ["A) Pierre-Michel Pango", "B) Mathieu Ekra", "C) Joachim Bony", "D) L'Abbé Pierre-Michel Pango et le révérend père Michel Coty"],
        "answer": "D",
        "explanation": "L'hymne a été composé par l'Abbé Pierre-Michel Pango (musique) et l'Abbé Michel Coty, avec des paroles co-écrites par Mathieu Ekra, Joachim Bony."
    },
    {
        "question": "Quelle est la devise de la Côte d'Ivoire ?",
        "options": ["A) Union, Discipline, Travail", "B) Fraternité, Travail, Progrès", "C) Paix, Travail, Patrie", "D) Union, Travail, Justice"],
        "answer": "A",
        "explanation": "La devise officielle de la République de Côte d'Ivoire est 'Union, Discipline, Travail'."
    },
    {
        "question": "En quelle année Félix Houphouët-Boigny est-il décédé ?",
        "options": ["A) 1990", "B) 1993", "C) 1995", "D) 1999"],
        "answer": "B",
        "explanation": "Félix Houphouët-Boigny, le premier président de la Côte d'Ivoire, est décédé le 7 décembre 1993."
    },
    {
        "question": "Quel traité de 1919 a redéfini les frontières de la Côte d'Ivoire en créant la Haute-Volta ?",
        "options": ["A) Décret du 1er mars 1919", "B) Traité de Versailles", "C) Accords de Brazzaville", "D) Conférence de Berlin"],
        "answer": "A",
        "explanation": "Le décret de 1919 a séparé des territoires de la Côte d'Ivoire et du Haut-Sénégal-Niger pour créer la colonie de la Haute-Volta."
    },
    {
        "question": "Quel sommet ivoirien culmine à 1752 m ?",
        "options": ["A) Mont Tonkoui", "B) Mont Nimba", "C) Mont Momi", "D) Mont Zo"],
        "answer": "B",
        "explanation": "Le Mont Nimba est le point culminant du pays."
    },
    {
        "question": "Quel fleuve naît exclusivement en CI ?",
        "options": ["A) Cavally", "B) Bandama", "C) Comoé", "D) Sassandra"],
        "answer": "B",
        "explanation": "Le Bandama prend sa source au nord de la CI."
    },
    {
        "question": "Yamoussoukro est devenue capitale en :",
        "options": ["A) 1983", "B) 1990", "C) 1978", "D) 1980"],
        "answer": "A",
        "explanation": "Loi du 21 mars 1983."
    },
    {
        "question": "Plus grande forêt d'Abidjan ?",
        "options": ["A) Banco", "B) Azagny", "C) Taï", "D) Sangoué"],
        "answer": "A",
        "explanation": "Parc National du Banco."
    },
    {
        "question": "Groupe ethnique Gour inclut :",
        "options": ["A) Baoulé", "B) Sénoufo", "C) Dan", "D) Bété"],
        "answer": "B",
        "explanation": "Les Sénoufo font partie du groupe Gour."
    },
    {
        "question": "Ville non chef-lieu de district autonome ?",
        "options": ["A) San Pédro", "B) Korhogo", "C) Man", "D) Bouaflé"],
        "answer": "D",
        "explanation": "Bouaflé est chef-lieu de région (Marahoué) mais pas de district autonome."
    },
    {
        "question": "Explorateur ayant signé traités en 1887 ?",
        "options": ["A) Binger", "B) Verdier", "C) Treich-Laplène", "D) Caillié"],
        "answer": "C",
        "explanation": "Marcel Treich-Laplène."
    },
    {
        "question": "Inauguration canal de Vridi ?",
        "options": ["A) 1950", "B) 1960", "C) 1934", "D) 1948"],
        "answer": "A",
        "explanation": "Ouvert en 1950."
    },
    {
        "question": "Premier PM en 1990 ?",
        "options": ["A) Bédié", "B) Ouattara", "C) Duncan", "D) Diarra"],
        "answer": "B",
        "explanation": "Alassane Ouattara fut nommé PM en 1990."
    },
    {
        "question": "Objectif majeur PND 2021-2025 ?",
        "options": ["A) Écologie", "B) Transformation par industrialisation", "C) Autosuffisance", "D) Dette 0"],
        "answer": "B",
        "explanation": "Transformation structurelle par l'industrialisation."
    },
    {
        "question": "Gisement gazier majeur 2021 ?",
        "options": ["A) Baleine", "B) Espoir", "C) Baobab", "D) Bélier"],
        "answer": "A",
        "explanation": "Gisement Baleine."
    },
    {
        "question": "Successeur de Binger (1896) ?",
        "options": ["A) Clozel", "B) Mouttet", "C) Roberdeau", "D) Angoulvant"],
        "answer": "B",
        "explanation": "Eugène Mouttet."
    },
    {
        "question": "Réserve de faune d'Abokouamékro dans quelle région ?",
        "options": ["A) Bélier", "B) Gbêkê", "C) Agnéby", "D) Iffou"],
        "answer": "A",
        "explanation": "Région du Bélier, près de Yamoussoukro."
    },
    {
        "question": "Part de la CI en prod mondiale de cajou (2023) ?",
        "options": ["A) 15%", "B) 25%", "C) 40%", "D) 60%"],
        "answer": "C",
        "explanation": "Environ 40%, 1er producteur mondial."
    },
    {
        "question": "Fondateur royaume Sanwi ?",
        "options": ["A) Amon N'Douffou Ier", "B) Aka Essoh", "C) Mian Amou", "D) Amalaman Anoh"],
        "answer": "D",
        "explanation": "Amalaman Anoh (XVIIIe)."
    },
    {
        "question": "Ethnie du groupe Krou ?",
        "options": ["A) Abouré", "B) Dida", "C) Gouro", "D) Lobi"],
        "answer": "B",
        "explanation": "Les Dida."
    },
    {
        "question": "Miracle ivoirien ?",
        "options": ["A) 1950-1960", "B) 1960-1980", "C) 1980-1990", "D) 1990-2000"],
        "answer": "B",
        "explanation": "Période de forte croissance 1960-1980."
    },
    {
        "question": "Barrage inauguré en 2017 ?",
        "options": ["A) Kossou", "B) Soubré", "C) Taabo", "D) Buyo"],
        "answer": "B",
        "explanation": "Barrage de Soubré."
    },
    {
        "question": "Origine du nom 'Côte d'Ivoire' ?",
        "options": ["A) Mammouths", "B) Commerce ivoire", "C) Binger", "D) Tribu Ivori"],
        "answer": "B",
        "explanation": "Nommé par les marins pour le commerce de l'ivoire."
    },
    {
        "question": "Colonie rattachée à la CI en 1932 ?",
        "options": ["A) Soudan", "B) Haute-Volta", "C) Guinée", "D) Dahomey"],
        "answer": "B",
        "explanation": "Haute-Volta (jusqu'en 1947)."
    },
    {
        "question": "Nombre de parcs nationaux en CI ?",
        "options": ["A) 5", "B) 8", "C) 12", "D) 15"],
        "answer": "B",
        "explanation": "8 Parcs Nationaux."
    },
    {
        "question": "San Pédro 1er port mondial pour :",
        "options": ["A) Café", "B) Cacao", "C) Bois", "D) Hévéa"],
        "answer": "B",
        "explanation": "Exportation de fèves de cacao."
    },
    {
        "question": "Ville ivoirienne UNESCO (2012) ?",
        "options": ["A) Abidjan", "B) Yamoussoukro", "C) Grand-Bassam", "D) Kong"],
        "answer": "C",
        "explanation": "Ville historique de Grand-Bassam."
    },
    {
        "question": "Fondateur royaume de Bouna ?",
        "options": ["A) Bounkani", "B) Samory", "C) Tutu", "D) Pokou"],
        "answer": "A",
        "explanation": "Roi Bounkani."
    },
    {
        "question": "Création du PDCI ?",
        "options": ["A) 1944", "B) 1946", "C) 1958", "D) 1960"],
        "answer": "B",
        "explanation": "9 avril 1946."
    },
    {
        "question": "Loi Houphouët (abolition travail forcé) ?",
        "options": ["A) 1944", "B) 1946", "C) 1950", "D) 1956"],
        "answer": "B",
        "explanation": "11 avril 1946."
    },
    {
        "question": "Consécration Basilique ND de la Paix ?",
        "options": ["A) 1989", "B) 1990", "C) 1992", "D) 1994"],
        "answer": "B",
        "explanation": "Septembre 1990 par Jean-Paul II."
    },
    {
        "question": "Plus long fleuve s'écoulant entièrement en CI ?",
        "options": ["A) Bandama", "B) Comoé", "C) Sassandra", "D) Cavally"],
        "answer": "A",
        "explanation": "Le Bandama (1050 km)."
    },
    {
        "question": "Part investissements privé dans PND 2021-2025 ?",
        "options": ["A) 50%", "B) 60%", "C) 74%", "D) 85%"],
        "answer": "C",
        "explanation": "74% du financement attendu."
    },
    {
        "question": "Altitude Mont Tonkoui ?",
        "options": ["A) 1073 m", "B) 1189 m", "C) 1223 m", "D) 1752 m"],
        "answer": "B",
        "explanation": "Environ 1189 m."
    },
    {
        "question": "Jour de l'indépendance CI ?",
        "options": ["A) 7 Août", "B) 4 Décembre", "C) 15 Août", "D) 1er Juillet"],
        "answer": "A",
        "explanation": "7 août 1960."
    },
    {
        "question": "Premier chef du Conseil de gouvernement (1958) ?",
        "options": ["A) Denise", "B) Houphouët", "C) Mockey", "D) Coulibaly"],
        "answer": "A",
        "explanation": "Auguste Denise."
    },
    {
        "question": "Fête du nouvel an Nzima ?",
        "options": ["A) Dipri", "B) Abissa", "C) Popo", "D) Goly"],
        "answer": "B",
        "explanation": "Fête de l'Abissa."
    },
    {
        "question": "Prix Ahmadou Kourouma 2021 ?",
        "options": ["A) Tadjo", "B) Gauz", "C) Abouet", "D) Diallo"],
        "answer": "B",
        "explanation": "Armand Gauz."
    },
    {
        "question": "Accord de paix 2007 ?",
        "options": ["A) Marcoussis", "B) Pretoria", "C) Ouagadougou", "D) Accra"],
        "answer": "C",
        "explanation": "Accord de Ouagadougou."
    },
    {
        "question": "Promulgation Constitution 3e République ?",
        "options": ["A) 8 Nov 2016", "B) 30 Oct 2016", "C) 1 Aou 2000", "D) 15 Mai 2020"],
        "answer": "A",
        "explanation": "8 novembre 2016."
    },
    {
        "question": "Plus grand lac artificiel de CI ?",
        "options": ["A) Kossou", "B) Soubré", "C) Buyo", "D) Taabo"],
        "answer": "A",
        "explanation": "Lac de Kossou."
    },
    {
        "question": "Signification BNETD ?",
        "options": ["A) Bureau National d'Études Techniques et de Développement", "B) Bureau National de l'Économie...", "C) Base Nationale...", "D) Bureau National d'Équipement..."],
        "answer": "A",
        "explanation": "Bureau National d'Études Techniques et de Développement."
    },
    {
        "question": "Mont Nimba classé UNESCO en :",
        "options": ["A) 1981", "B) 1990", "C) 2001", "D) 1974"],
        "answer": "A",
        "explanation": "Inscrit en 1981/1982."
    },
    {
        "question": "Stade finale CAN 2023 ?",
        "options": ["A) 2021", "B) 2023", "C) 2019", "D) 2025"],
        "answer": "B",
        "explanation": "La question était sur l'année de la CAN (2023)."
    },
    {
        "question": "Gouverneur 'pacification' (1908-1916) ?",
        "options": ["A) Angoulvant", "B) Binger", "C) Ponty", "D) Eboué"],
        "answer": "A",
        "explanation": "Gabriel Angoulvant."
    },
    {
        "question": "Hymne de la CI ?",
        "options": ["A) L'Abidjanaise", "B) La Concorde", "C) Le Ditanyè", "D) La Renaissance"],
        "answer": "A",
        "explanation": "L'Abidjanaise."
    },
    {
        "question": "Chef-lieu du Gôh ?",
        "options": ["A) Daloa", "B) Gagnoa", "C) Soubré", "D) Issia"],
        "answer": "B",
        "explanation": "Gagnoa."
    },
    {
        "question": "Mosquées inscrites à l'UNESCO (2021) ?",
        "options": ["A) Kong", "B) Style soudanais du nord", "C) Samatiguila", "D) Mankono"],
        "answer": "B",
        "explanation": "Ensemble de 8 mosquées de style soudanais."
    },
    {
        "question": "Communes du Grand Abidjan ?",
        "options": ["A) 10", "B) 13", "C) 14", "D) 15"],
        "answer": "B",
        "explanation": "13 entités communales (10 urbaines + 3 sous-préfectures)."
    },
    {
        "question": "Création de la RTI ?",
        "options": ["A) 1960", "B) 1963", "C) 1970", "D) 1973"],
        "answer": "B",
        "explanation": "1963."
    },
    {
        "question": "Zone forestière actuelle CI estimée à :",
        "options": ["A) <3M ha", "B) 8M ha", "C) 12M ha", "D) 16M ha"],
        "answer": "A",
        "explanation": "Moins de 3 millions d'hectares."
    },
    {
        "question": "Port historiquement bois ?",
        "options": ["A) Abidjan", "B) San Pédro", "C) Sassandra", "D) Tabou"],
        "answer": "B",
        "explanation": "San Pédro a été créé pour le bois."
    },
    {
        "question": "Ethnie Lobi connue pour :",
        "options": ["A) Zaouli", "B) Soukalas", "C) Poids à or", "D) Kita"],
        "answer": "B",
        "explanation": "Habitats fortifiés en banco appelés soukalas."
    },
    {
        "question": "Monnaie précoloniale Akan ?",
        "options": ["A) Cauri", "B) Manille", "C) Sel", "D) Poudre d'or"],
        "answer": "D",
        "explanation": "La poudre d'or et les poids à peser."
    },
    {
        "question": "Lequel de ces pays est actuellement dirigé par une femme ?",
        "options": ["A) Libéria", "B) Sierra Léone", "C) Tanzanie", "D) Éthiopie"],
        "answer": "C",
        "explanation": "La Tanzanie est dirigée par Samia Suluhu Hassan."
    },
    {
        "question": "Quelle école Aristote a-t-il créée ?",
        "options": ["A) Le Jardin des Plantes", "B) L'Académie", "C) Le Lycée", "D) L’Université d’Athènes"],
        "answer": "C",
        "explanation": "Aristote a fondé le Lycée à Athènes."
    },
    {
        "question": "Qui fut le premier Directeur Général de l'ENA-CI ?",
        "options": ["A) Laurent Dona Fologo", "B) Ropion Robert", "C) Zadi Zaourou", "D) Alassane Ouattara"],
        "answer": "B",
        "explanation": "Ropion Robert a été le premier DG de l'ENA."
    },
    {
        "question": "Quel acte a permis l’indépendance du Soudan du Sud en 2011 ?",
        "options": ["A) L’Accord de paix global", "B) Les Accords de Naivasha", "C) Les Accords de Khartoum", "D) Le Référendum d’autodétermination"],
        "answer": "D",
        "explanation": "C'est le référendum d'autodétermination de 2011 qui a conduit à l'indépendance."
    },
    {
        "question": "Un savoir ésotérique est un savoir :",
        "options": ["A) Populaire et accessible", "B) Réservé à un cercle initié", "C) Pratique", "D) Public"],
        "answer": "B",
        "explanation": "L'ésotérisme désigne un enseignement réservé à des initiés."
    },
    {
        "question": "Quelle est la capitale de la Tanzanie ?",
        "options": ["A) Freetown", "B) Banjul", "C) Bissau", "D) Dodoma"],
        "answer": "D",
        "explanation": "Dodoma est la capitale politique de la Tanzanie."
    },
    {
        "question": "Les députés ivoiriens sont :",
        "options": ["A) Nommés", "B) Élus", "C) Élus pour certains, nommés pour d’autres", "D) Nommés par le président"],
        "answer": "B",
        "explanation": "Les députés de l'Assemblée nationale sont élus au suffrage universel direct."
    },
    {
        "question": "Lequel de ces personnalités n’a jamais été président de l’Assemblée Nationale ?",
        "options": ["A) Henri Konan Bédié", "B) Mamadou Koulibaly", "C) Soro Guillaume", "D) Kandia Camara"],
        "answer": "D",
        "explanation": "Kandia Camara a été présidente du Sénat, mais pas de l'Assemblée nationale."
    },
    {
        "question": "En CI, le président de la République est membre du gouvernement.",
        "options": ["A) Vrai", "B) Faux"],
        "answer": "B",
        "explanation": "Le Président de la République n'est pas formellement membre du gouvernement, bien qu'il le préside."
    },
    {
        "question": "L’Assemblée Nationale ivoirienne comprend désormais des sénateurs :",
        "options": ["A) Vrai", "B) Faux"],
        "answer": "B",
        "explanation": "L'Assemblée Nationale et le Sénat sont deux chambres distinctes du Parlement."
    },
    {
        "question": "En quelle année le Printemps arabe a-t-il débuté ?",
        "options": ["A) 2008", "B) 2012", "C) 2010", "D) 2005"],
        "answer": "C",
        "explanation": "Le Printemps arabe a commencé fin 2010 en Tunisie."
    },
    {
        "question": "En quelle année le FEMUA a-t-il débuté ?",
        "options": ["A) 2006", "B) 2008", "C) 2009", "D) 2010"],
        "answer": "B",
        "explanation": "Le FEMUA a été lancé en 2008."
    },
    {
        "question": "Qui est l’actuel Directeur Général de la Fonction Publique ivoirienne ?",
        "options": ["A) Aka Kacou", "B) Yéo Nahoua", "C) Kouakou Edouard", "D) SORO Gninagafol"],
        "answer": "D",
        "explanation": "Soro Gninagafol a été nommé DG de la Fonction Publique."
    },
    {
        "question": "En quelle année Yamoussoukro devint-elle la capitale politique ivoirienne ?",
        "options": ["A) 1980", "B) 1983", "C) 1990", "D) 1995"],
        "answer": "B",
        "explanation": "Le transfert de la capitale à Yamoussoukro a été décidé en 1983."
    },
    {
        "question": "Qui est l'actuel Premier ministre du Canada ?",
        "options": ["A) Justin Trudeau", "B) Chrystia Freeland", "C) Jagmeet Singh", "D) Mark Carney"],
        "answer": "A",
        "explanation": "Justin Trudeau est le Premier ministre du Canada."
    },
    {
        "question": "Quel est le rang de la Côte d’Ivoire dans le classement mondial des producteurs de café ?",
        "options": ["A) 3e", "B) 5e", "C) 14e", "D) 15e"],
        "answer": "C",
        "explanation": "La Côte d'Ivoire se situe autour du 14e rang mondial."
    },
    {
        "question": "Quelle science étudie les insectes ?",
        "options": ["A) Ornithologie", "B) Mycologie", "C) Entomologie", "D) Arachnologie"],
        "answer": "C",
        "explanation": "L'entomologie est la science qui étudie les insectes."
    },
    {
        "question": "Quelle femme a été la première à arbitrer un match de football professionnel ?",
        "options": ["A) Wendie Renard", "B) Stéphanie Frappart", "C) Bibiana Steinhaus", "D) Salima Mukansanga"],
        "answer": "C",
        "explanation": "Bibiana Steinhaus a été la première femme à arbitrer un match masculin de haut niveau."
    },
    {
        "question": "En quelle année les accords de Bretton Woods ont-ils été signés ?",
        "options": ["A) 1940", "B) 1944", "C) 1945", "D) 1939"],
        "answer": "B",
        "explanation": "Les accords de Bretton Woods ont été signés en 1944."
    },
    {
        "question": "Qui est l'actuel président du Conseil constitutionnel ivoirien ?",
        "options": ["A) Mamadou Koné", "B) Chantal Nanaba Camara", "C) Francis Wodié", "D) Tia Koné"],
        "answer": "B",
        "explanation": "Chantal Nanaba Camara a été nommée présidente du Conseil constitutionnel."
    },
    {
        "question": "Quel peintre espagnol est connu pour avoir cofondé le cubisme ?",
        "options": ["A) Salvador Dalí", "B) Pablo Picasso", "C) Juan Gris"],
        "answer": "B",
        "explanation": "Pablo Picasso est l'un des fondateurs du cubisme."
    },
    {
        "question": "Qui a été couronné empereur français le 2 décembre 1804 ?",
        "options": ["A) Napoléon Bonaparte", "B) Charlemagne", "C) Louis XIV"],
        "answer": "A",
        "explanation": "Napoléon Bonaparte a été sacré empereur en 1804."
    },
    {
        "question": "Quel est le nom de la science qui étudie les fossiles ?",
        "options": ["A) Paléontologie", "B) Botanique", "C) Archéologie"],
        "answer": "A",
        "explanation": "La paléontologie est l'étude des fossiles."
    },
    {
        "question": "Qui est l’actuel Secrétaire Général de l’ENA ?",
        "options": ["A) Narcisse Sepy Yessoh", "B) Koné Aline", "C) François Kouma"],
        "answer": "A",
        "explanation": "Narcisse Sepy Yessoh est le SG actuel de l'ENA."
    },
    {
        "question": "Combien de pattes possède une araignée ?",
        "options": ["A) 6", "B) 8", "C) 12"],
        "answer": "B",
        "explanation": "Les araignées sont des arachnides et possèdent 8 pattes."
    },
    {
        "question": "Quel gaz représente environ 78 % de l’atmosphère terrestre ?",
        "options": ["A) L’oxygène", "B) Le carbone", "C) Le diazote", "D) L'argon"],
        "answer": "C",
        "explanation": "Le diazote constitue 78% de l'atmosphère."
    },
    {
        "question": "Le Pakistan a pour capitale :",
        "options": ["A) Kuala Lumpur", "B) Bangkok", "C) Islamabad", "D) Kaboul"],
        "answer": "C",
        "explanation": "Islamabad est la capitale du Pakistan."
    },
    {
        "question": "Quel éminent diplomate et Ministre des Affaires Etrangères de Cote d’Ivoire a tiré sa révérence le 8 avril 2025 ?",
        "options": ["A) Essy Amara", "B) Charles Koffi Diby", "C) Siméon Aké"],
        "answer": "A",
        "explanation": "Essy Amara est un diplomate ivoirien."
    },
    {
        "question": "Quelle maison a pour emblème un loup dans la série Game of Thrones ?",
        "options": ["A) La maison Stark", "B) La maison Baratheon", "C) La maison Lannister"],
        "answer": "A",
        "explanation": "L'emblème de la Maison Stark est un loup-garou."
    },
    {
        "question": "Qui a écrit « Les bouts de bois de Dieu » ?",
        "options": ["A) Aimé Césaire", "B) Sembene Ousmane", "C) Soro Guéfala"],
        "answer": "B",
        "explanation": "Ousmane Sembène a écrit Les Bouts de bois de Dieu."
    },
    {
        "question": "Quelle planète est surnommée « l’étoile du berger » ?",
        "options": ["A) Mars", "B) Terre", "C) Vénus"],
        "answer": "C",
        "explanation": "Vénus est souvent appelée l'étoile du berger."
    },
    {
        "question": "Quel personnage mythologique a été condamné à pousser éternellement un rocher en haut d’une montagne ?",
        "options": ["A) Sisyphe", "B) Prométhée", "C) Tantale"],
        "answer": "A",
        "explanation": "C'est le mythe de Sisyphe."
    },
    {
        "question": "Quel traité a mis fin à la première guerre mondiale en 1919 ?",
        "options": ["A) Le traité de Versailles", "B) Les accords d’Evian", "C) Le traité de Rome"],
        "answer": "A",
        "explanation": "Le Traité de Versailles a mis fin à la Première Guerre mondiale."
    },
    {
        "question": "Qui était le président américain pendant la seconde guerre mondiale ?",
        "options": ["A) Richard Nixon", "B) Delano Roosevelt", "C) John Kennedy"],
        "answer": "B",
        "explanation": "Franklin Delano Roosevelt était président pendant la majeure partie de la guerre."
    },
    {
        "question": "Qui est le plus médaillé aux Jeux Olympiques ?",
        "options": ["A) Usain Bolt", "B) Michael Phelps", "C) Larissa Latynina", "D) Mark Spitz"],
        "answer": "B",
        "explanation": "Michael Phelps détient le record du nombre de médailles olympiques."
    },
    {
        "question": "Quel stade a accueilli la confrontation entre la Cote d’Ivoire et le Sénégal lors des huitièmes de finale de la 34e édition de la CAN ?",
        "options": ["A) Le Stade Laurent Pokou", "B) Le Stade de la paix", "C) Le Stade Charles Konan Banny"],
        "answer": "C",
        "explanation": "Le match a eu lieu au stade Charles Konan Banny de Yamoussoukro."
    },
    {
        "question": "Combien d’Océans il y a-t-il ?",
        "options": ["A) 4", "B) 5", "C) 6"],
        "answer": "B",
        "explanation": "Il y a 5 océans : Atlantique, Pacifique, Indien, Arctique, Antarctique."
    },
    {
        "question": "Quel est le nom à l’état civil de l’artiste zouglou Pat Sacko ?",
        "options": ["A) Hughes-Patrick Ossohou", "B) Blaise-Patrick Daté", "C) Patrick Yao"],
        "answer": "A",
        "explanation": "Son nom à l'état civil est Ossohou Patrick."
    },
    {
        "question": "Quel est le chef-lieu de la région de l’Agnéby -Tiassa ?",
        "options": ["A) Dabou", "B) Adzopé", "C) Agboville"],
        "answer": "C",
        "explanation": "Agboville est le chef-lieu de l'Agnéby-Tiassa."
    },
    {
        "question": "Quelle mer sépare l’Europe de l’Afrique ?",
        "options": ["A) Mer Rouge", "B) Mer Noire", "C) Mer Méditerranée"],
        "answer": "C",
        "explanation": "La mer Méditerranée sépare l'Europe de l'Afrique."
    },
    {
        "question": "Quel est le seul continent à ne pas avoir de pays ?",
        "options": ["A) Océanie", "B) Arctique", "C) Antarctique"],
        "answer": "C",
        "explanation": "L'Antarctique ne compte aucun pays."
    },
    {
        "question": "Quelle est la capitale de la Turquie ?",
        "options": ["A) Istanbul", "B) Ankara", "C) Izmir", "D) Antalya"],
        "answer": "B",
        "explanation": "Ankara est la capitale de la Turquie."
    },
    {
        "question": "A quelles dates se sont déroulées la 3e édition des Journées Portes Ouvertes de l’ENA ?",
        "options": ["A) Du 25 au 26 février 2025", "B) Du 13 au 15 février 2025", "C) Du 23 au 24 février 2025"],
        "answer": "B",
        "explanation": "C'est généralement autour de ces dates."
    },
    {
        "question": "Quelle est la nouvelle dénomination de l’ENA France ?",
        "options": ["A) INSP", "B) ENAMF", "C) APF", "D) ENA-Paris"],
        "answer": "A",
        "explanation": "L'École nationale d'administration a été remplacée par l'Institut national du service public (INSP)."
    },
    {
        "question": "En quelle année a eu lieu la prise de la Bastille ?",
        "options": ["A) 1789", "B) 1791", "C) 1793"],
        "answer": "A",
        "explanation": "La prise de la Bastille a eu lieu en 1789."
    },
    {
        "question": "Combien de langues officielles compte l’Union Européenne ?",
        "options": ["A) 20", "B) 24", "C) 3"],
        "answer": "B",
        "explanation": "L'UE compte 24 langues officielles."
    },
    {
        "question": "Quel est le pourcentage de suffrages obtenu par Brice Clotaire Oligui N’Guema selon les résultats provisoires de l'élection présidentielle d'avril 2025 au Gabon ?",
        "options": ["A) 87,50 %", "B) 90,35 %", "C) 94,85 %", "D) 98,85 %"],
        "answer": "B",
        "explanation": "Selon les résultats provisoires annoncés le 13 avril 2025 par le ministère de l'Intérieur, Brice Clotaire Oligui N'Guema a obtenu 90,35 % des voix (proclamation définitive le 25 avril 2025 à 94,85 % par la Cour constitutionnelle)."
    },
    {
        "question": "Qui est l’actuel secrétaire général de la francophonie ?",
        "options": ["A) Louise Mushikiwabo", "B) Michael Jean", "C) Abdou Diouf"],
        "answer": "A",
        "explanation": "Louise Mushikiwabo est l'actuelle Secrétaire générale."
    },
    {
        "question": "Où a eu lieu la COP 29 ?",
        "options": ["A) Bakou", "B) Paris", "C) Belém"],
        "answer": "A",
        "explanation": "La COP 29 a eu lieu à Bakou, en Azerbaïdjan."
    },
    {
        "question": "Sous quel thème est placé le FEMUA 18 ?",
        "options": ["A) La santé mentale", "B) Intelligence artificielle : menace ou opportunité pour l'Afrique ?", "C) Civisme et sécurité Routière"],
        "answer": "B",
        "explanation": "L'IA est le thème du FEMUA 18."
    },
    {
        "question": "En quelle année furent signés les accords de Maastricht ?",
        "options": ["A) 1962", "B) 1981", "C) 1992"],
        "answer": "C",
        "explanation": "Le traité de Maastricht a été signé en 1992."
    },
    {
        "question": "Quelle est la monnaie utilisée en Russie ?",
        "options": ["A) l’euro", "B) le rouble", "C) l’hryvnia"],
        "answer": "B",
        "explanation": "Le rouble est la monnaie russe."
    },
    {
        "question": "A combien est estimée la population ivoirienne à l’issu du dernier recensement général de la population et de l’habitat ?",
        "options": ["A) 29 389 150 hbts", "B) 32 167 255 hbts", "C) autre"],
        "answer": "A",
        "explanation": "La population est estimée à environ 29,4 millions d'habitants."
    },
    {
        "question": "Comment appelle-t-on les habitants de Gaza ?",
        "options": ["A) Les Gazaouis", "B) Les Gazavites", "C) Les Gazawites"],
        "answer": "A",
        "explanation": "Les habitants de Gaza sont les Gazaouis."
    },
    {
        "question": "En mathématiques, quelle est la valeur arrondie de pi ?",
        "options": ["A) 3,14028", "B) 3,14159", "C) 3,14217"],
        "answer": "B",
        "explanation": "La valeur de Pi commence par 3,14159."
    },
    {
        "question": "Quelle est la langue principale parlée en Iran ?",
        "options": ["A) Persan", "B) Kurde", "C) Iranien"],
        "answer": "A",
        "explanation": "Le persan est la langue officielle de l'Iran."
    },
    {
        "question": "Quel est le seul pays au monde à posséder une capitale qui commence par la lettre Z ?",
        "options": ["A) Suisse", "B) Croatie", "C) Ouganda"],
        "answer": "B",
        "explanation": "Zagreb est la capitale de la Croatie."
    },
    {
        "question": "Quel verbe est utilisé pour désigner le cri des dauphins ?",
        "options": ["A) Gazouiller", "B) Glapir", "C) Siffler"],
        "answer": "C",
        "explanation": "Les dauphins sifflent."
    },
    {
        "question": "Qui est le coréalisateur du film Marabout chéri au côté de Luis Marquès ?",
        "options": ["A) Cheick Yvhane", "B) Michel Bohiri", "C) Kadhy Touré"],
        "answer": "C",
        "explanation": "Kadhy Touré est co-réalisatrice de Marabout Chéri."
    },
    {
        "question": "“Je punirai les serviteurs, les fils et leurs pères” est une :",
        "options": ["A) Méthaphore", "B) Allégorie", "C) Gradation"],
        "answer": "C",
        "explanation": "Il s'agit d'une gradation."
    },
    {
        "question": "Qui détient le record du monde du 100 m masculin ?",
        "options": ["A) Usain Bolt", "B) Noah Lyles", "C) Justin Gatlin", "D) Asafa Powell"],
        "answer": "A",
        "explanation": "Usain Bolt détient le record du monde du 100 m."
    },
    {
        "question": "Qui est considéré comme le meilleur joueur de basketball de tous les temps ?",
        "options": ["A) Lebron James", "B) Michael Jordan", "C) Kobe Bryant"],
        "answer": "B",
        "explanation": "Michael Jordan est généralement considéré comme le meilleur joueur de basketball."
    },
    {
        "question": "Qui a été le premier pays à remporter la coupe du monde de football ?",
        "options": ["A) Urugay", "B) Grande Bretagne", "C) Italie"],
        "answer": "A",
        "explanation": "L'Uruguay a remporté la première Coupe du monde en 1930."
    },
    {
        "question": "Qui a remporté le ballon d’or France football en 2022 ?",
        "options": ["A) Lionnel Messi", "B) Karim Benzema", "C) Luka Modric"],
        "answer": "B",
        "explanation": "Karim Benzema a remporté le Ballon d'or 2022."
    },
    {
        "question": "Quel boxeur nommé « the greatest » est considéré comme l’un des plus grands boxeurs de tous les temps ?",
        "options": ["A) Floyd Mayweather Jr", "B) Mike Tyson", "C) Mohamed Ali"],
        "answer": "C",
        "explanation": "Mohamed Ali était surnommé The Greatest."
    },
    {
        "question": "Qui est le joueur de tennis espagnol qui est considéré comme l’un des meilleurs joueurs sur terre battue de tous les temps ?",
        "options": ["A) Rafael Nadal", "B) Carlos Alcaraz", "C) Manuel Alonzo"],
        "answer": "A",
        "explanation": "Rafael Nadal est le roi de la terre battue."
    },
    {
        "question": "Qui est le joueur de golf américain qui est considéré comme l’un des plus grands golfeurs de tous les temps ?",
        "options": ["A) Jack Nicklaus", "B) Tiger Woods", "C) Arnold Palmer"],
        "answer": "B",
        "explanation": "Tiger Woods est l'un des plus grands golfeurs."
    },
    {
        "question": "Qui est le premier joueur ivoirien à avoir marqué en finale d’une CAN ?",
        "options": ["A) Laurent Pokou", "B) Didier Drogba", "C) Franck Kessié"],
        "answer": "A",
        "explanation": "Laurent Pokou."
    },
    {
        "question": "Combien de buts ont été marqués à la Coupe d’Afrique des Nations 2023 organisé en Côte d’ivoire ?",
        "options": ["A) 109 buts", "B) 119 buts", "C) 135 buts"],
        "answer": "B",
        "explanation": "119 buts ont été marqués lors de la CAN 2023."
    },
    {
        "question": "Qui est le meilleur buteur de l’histoire de la CAN ?",
        "options": ["A) Didier Drogba", "B) Roger Mila", "C) Samuel Eto’o"],
        "answer": "C",
        "explanation": "Samuel Eto'o est le meilleur buteur de l'histoire de la CAN avec 18 buts."
    },
    {
        "question": "Lors du tour de France, qui est récompensé d’un maillot blanc à pois rouges ?",
        "options": ["A) Le meilleur grimpeur", "B) Le meilleur coureur", "C) Le meilleur cycliste"],
        "answer": "A",
        "explanation": "Le maillot à pois récompense le meilleur grimpeur."
    },
    {
        "question": "Où se dérouleront les prochains jeux olympiques ?",
        "options": ["A) Paris", "B) Mexico", "C) Los Angeles"],
        "answer": "C",
        "explanation": "Les prochains Jeux Olympiques d'été après 2024 auront lieu à Los Angeles en 2028."
    },
    {
        "question": "Depuis quelle année le badminton est devenu une discipline olympique ?",
        "options": ["A) 1992", "B) 2010", "C) 2023"],
        "answer": "A",
        "explanation": "Le badminton est sport olympique depuis 1992."
    },
    {
        "question": "Les IXème jeux de la francophonie se sont déroulés du ……. Au ……….. 2023 à Kinshasa :",
        "options": ["A) Du 28 juillet au 6 aout", "B) Du 28 février au 7 mars 2023", "C) Du 28 juin au 6 juillet"],
        "answer": "A",
        "explanation": "Les Jeux de la Francophonie 2023 se sont tenus fin juillet - début août."
    },
    {
        "question": "Comment appelle-t-on le tournoi de tennis joué à Paris ?",
        "options": ["A) Roland-Garros", "B) Wimbledon", "C) Us Open"],
        "answer": "A",
        "explanation": "Le tournoi de Paris est Roland-Garros."
    },
    {
        "question": "Qui a remporté le ballon d’or africain quatre fois consécutives ?",
        "options": ["A) Georges Weah", "B) Yaya Touré", "C) Samuel Eto’o"],
        "answer": "B",
        "explanation": "Yaya Touré a gagné le Ballon d'Or africain quatre fois de suite (2011-2014)."
    },
    {
        "question": "Qui a été le meilleur buteur de la coupe du monde 2014 ?",
        "options": ["A) James Rodriguez", "B) Thomas Muller", "C) Lionnel Messi"],
        "answer": "A",
        "explanation": "James Rodriguez a été le meilleur buteur (6 buts)."
    },
    {
        "question": "Qui est le dernier vainqueur français de Roland Garros ?",
        "options": ["A) Tsonga", "B) Monfils", "C) Noah"],
        "answer": "C",
        "explanation": "Yannick Noah en 1983."
    },
    {
        "question": "Dans quel pays est né le judo ?",
        "options": ["A) Chine", "B) Japon", "C) Vietnam", "D) Corée du Sud"],
        "answer": "B",
        "explanation": "Le judo a été créé au Japon par Jigoro Kano."
    },
    {
        "question": "Quel pays a remporté la Coupe du Monde FIFA 2022 ?",
        "options": ["A) France", "B) Brésil", "C) Argentine", "D) Allemagne"],
        "answer": "C",
        "explanation": "L'Argentine a remporté la Coupe du Monde 2022."
    },
    {
        "question": "Quelle ville a accueilli les Jeux Olympiques d’été 2024 ?",
        "options": ["A) Tokyo", "B) Paris", "C) Los Angelès", "D) Londres"],
        "answer": "B",
        "explanation": "Paris a accueilli les JO en 2024."
    },
    {
        "question": "Combien de joueurs composent une équipe de basketball sur le terrain ?",
        "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
        "answer": "B",
        "explanation": "Il y a 5 joueurs par équipe sur le terrain."
    },
    {
        "question": "Dans quel sport évolue Novak Djokovic ?",
        "options": ["A) Golf", "B) Tennis", "C) Handball", "D) Boxe"],
        "answer": "B",
        "explanation": "Djokovic est un joueur de tennis."
    },
    {
        "question": "Quel pays domine historiquement les Jeux Olympiques d’hiver ?",
        "options": ["A) Norvège", "B) Canada", "C) Russie", "D) USA"],
        "answer": "A",
        "explanation": "La Norvège est le pays le plus titré aux JO d'hiver."
    },
    {
        "question": "Qui a remporté le Ballon d’Or 2020 ?",
        "options": ["A) Erling Halland", "B) Lionnel Messi", "C) Cristiano R", "D) Modric"],
        "answer": "B",
        "explanation": "Le Ballon d'Or 2020 n'a pas été attribué. Il s'agit peut-être d'une erreur dans les options. En l'absence de meilleur choix, on retient Messi."
    },
    {
        "question": "Combien de sets gagnants faut-il pour remporter un match masculin en Grand Chelem ?",
        "options": ["A) 2", "B) 3", "C) 4", "D) 5"],
        "answer": "B",
        "explanation": "Il faut 3 sets gagnants pour remporter un match masculin en Grand Chelem."
    },
    {
        "question": "Quel sport utilise les termes “birdie” et “eagle” ?",
        "options": ["A) Tennis", "B) Golf", "C) Badminton", "D) Baseball"],
        "answer": "B",
        "explanation": "Ce sont des termes de golf."
    },
    {
        "question": "Quelle nation a remporté la CAN 2023 (jouée en 2024) ?",
        "options": ["A) Sénégal", "B) Maroc", "C) Côte d’Ivoire", "D) Nigéria"],
        "answer": "C",
        "explanation": "La Côte d'Ivoire a remporté la CAN 2023."
    },
    {
        "question": "Combien de kilomètres mesure un marathon ?",
        "options": ["A) 40", "B) 41", "C) 41, 195", "D) 43 km"],
        "answer": "C",
        "explanation": "Un marathon mesure 42,195 km, l'option C (bien que 41,195 y soit écrite) est l'option la plus proche visée ou une coquille du document original."
    },
    {
        "question": "Dans quel sport retrouve-t-on la NBA ?",
        "options": ["A) Hockey", "B) Baseball", "C) Football", "D) Basketball"],
        "answer": "D",
        "explanation": "La NBA est la ligue américaine de basketball."
    },
    {
        "question": "Quel joueur est associé au club d’Al Nassr depuis 2023 ?",
        "options": ["A) Neymar", "B) Benzema", "C) Cristiano R", "D) Messi"],
        "answer": "C",
        "explanation": "Cristiano Ronaldo joue pour Al Nassr."
    },
    {
        "question": "Quel pays a organisé la Coupe du Monde 2022 ?",
        "options": ["A) Qatar", "B) Russie", "C) France", "D) Mexique"],
        "answer": "A",
        "explanation": "Le Qatar a organisé la Coupe du monde 2022."
    },
    {
        "question": "Dans le sport du rugby (à XV), combien de points rapporte un essai marqué (avant transformation) ?",
        "options": ["A) 3 points", "B) 5 points", "C) 7 points", "D) 2 points"],
        "answer": "B",
        "explanation": "Un essai au rugby vaut 5 points (la transformation rapporte 2 points supplémentaires, une pénalité ou un drop vaut 3 points)."
    },
    {
        "question": "Quel club est le plus titré en Ligue des Champions CAF ?",
        "options": ["A) Al ahly sc", "B) TP Mazembe", "C) Zamalek", "D) Pyramids fc"],
        "answer": "A",
        "explanation": "Al Ahly SC est le club le plus titré."
    },
    {
        "question": "Dans quel sport évolue Francis Ngannou ?",
        "options": ["A) Boxe MMA", "B) Football", "C) Athlétisme", "D) Lutte"],
        "answer": "A",
        "explanation": "Francis Ngannou évolue en MMA et Boxe."
    },
    {
        "question": "Quelle est la nature du pouvoir exécutif ivoirien ?",
        "options": ["A) Monocéphale", "B) Bicéphale", "C) Tricéphale"],
        "answer": "B",
        "explanation": "Le pouvoir exécutif ivoirien est bicéphale (Président et Premier Ministre)."
    },
    {
        "question": "Qui est le Vice-président de la République de Côte d’Ivoire ?",
        "options": ["A) Tiemoko Meyliet Koné", "B) Yua Koffi", "C) Beugré Mambé"],
        "answer": "A",
        "explanation": "Tiémoko Meyliet Koné est le Vice-président."
    },
    {
        "question": "Le médiateur de la République est nommé pour ?",
        "options": ["A) 4 ans", "B) 5 ans", "C) 6 ans"],
        "answer": "C",
        "explanation": "Le Médiateur de la République est nommé pour un mandat de 6 ans non renouvelable."
    },
    {
        "question": "Qui est l’actuel médiateur de la République de Côte d’Ivoire ?",
        "options": ["A) Adama Toungara", "B) Eugène Aka Aouelé", "C) Gaoussou Touré"],
        "answer": "A",
        "explanation": "Adama Toungara est le Médiateur de la République."
    },
    {
        "question": "En quelle année a été nommé le Haut représentant du Président de la république ?",
        "options": ["A) 2024", "B) 2023", "C) 2022"],
        "answer": "B",
        "explanation": "Le Haut représentant a été nommé en 2023."
    },
    {
        "question": "Le parlement ivoirien est ?",
        "options": ["A) Monocamérale", "B) Bicamérale", "C) aucune réponse n’est correcte"],
        "answer": "B",
        "explanation": "Le parlement ivoirien est bicaméral (Assemblée nationale et Sénat)."
    },
    {
        "question": "Qui a été le premier président du Sénat ivoirien ?",
        "options": ["A) Kandia Camara", "B) Jeannot Ahoussou Kouadio", "C) Dagri Diabaté"],
        "answer": "B",
        "explanation": "Jeannot Ahoussou-Kouadio fut le premier président du Sénat."
    },
    {
        "question": "Comment s’appelle l’actuel président du Conseil Constitutionnel ivoirien ?",
        "options": ["A) Chantal Naneba Camara", "B) Chantal Nanaba Camara", "C) Chantal Massereba Camara"],
        "answer": "B",
        "explanation": "Chantal Nanaba Camara est la présidente du Conseil constitutionnel."
    },
    {
        "question": "Le président du Conseil Régional est élu pour ?",
        "options": ["A) 6 ans", "B) 5 ans", "C) 4 ans"],
        "answer": "B",
        "explanation": "Il est élu pour 5 ans."
    },
    {
        "question": "Qui est le ministre de la fonction publique et de la modernisation de l’administration ?",
        "options": ["A) Mathieu Ekra", "B) Ally Coulibaly", "C) Anne Ouloto"],
        "answer": "C",
        "explanation": "Anne Ouloto est la ministre de la fonction publique."
    },
    {
        "question": "L’ordre juridictionnel ivoirien est ?",
        "options": ["A) Moniste", "B) Dualiste", "C) Atypique"],
        "answer": "B",
        "explanation": "L'ordre est dualiste, avec un ordre judiciaire et un ordre administratif."
    },
    {
        "question": "Qui est le président du Conseil d’Etat ivoirien ?",
        "options": ["A) Patrice Yao Kouakou", "B) Yua Koffi", "C) Lamine Ouattara"],
        "answer": "A",
        "explanation": "Patrice Yao Kouakou préside le Conseil d'Etat."
    },
    {
        "question": "Qui est le président de la Cour de Cassation ivoirienne ?",
        "options": ["A) Yua Koffi", "B) Patrice Yao Kouakou", "C) Théophile Ahoua N’dol"],
        "answer": "A",
        "explanation": "Yua Koffi préside la Cour de Cassation."
    },
    {
        "question": "Qui est le président de la Haute Autorité à la Bonne gouvernance ?",
        "options": ["A) Mamadou Sangafowa", "B) Epiphane Zoro BI", "C) Patrick Achi"],
        "answer": "B",
        "explanation": "Epiphane Zoro BI Ballo est le président de la HABG."
    },
    {
        "question": "Le général Apalo Touré est issu de ?",
        "options": ["A) La Police", "B) L’armée de l’air", "C) La Gendarmerie"],
        "answer": "C",
        "explanation": "Alexandre Apalo Touré est Commandant Supérieur de la Gendarmerie."
    },
    {
        "question": "Quelle est la dénomination exacte du Ministère de l’éducation ?",
        "options": ["A) Ministère d’Etat, Ministère de l’Education Nationale et de l’Alphabétisation", "B) Ministère de l’Education Nationale, de l’Alphabétisation et de l’Enseignement technique", "C) Ministère de l’Education Nationale et de l’Enseignement Supérieur"],
        "answer": "A",
        "explanation": "C'est le Ministère de l'Éducation Nationale et de l'Alphabétisation."
    },
    {
        "question": "Kanvaly Diomandé est le président de laquelle de ces institutions ?",
        "options": ["A) Commission Electorale Indépendante", "B) Cour des Comptes", "C) Grande Chancellerie de l’ordre national"],
        "answer": "B",
        "explanation": "Kanvaly Diomandé est président de la Cour des Comptes."
    },
    {
        "question": "Qui est le président de la Chambre des Rois et chefs traditionnels de Cote d’ivoire ?",
        "options": ["A) Sa majesté Nanan Desire Amon-Tanoe", "B) Sa majesté Nanan Desire Amoi-Tano", "C) Sa majesté Nanan Desire Amani-Tanoe"],
        "answer": "A",
        "explanation": "Nanan Amon Tanoé Désiré préside la Chambre."
    },
    {
        "question": "Parmi ces personnalités, laquelle n’a jamais été président de l’Assemblée Nationale en CI ?",
        "options": ["A) Mamadou Koulibaly", "B) Soro Guillaume", "C) Coulibaly Kuibiert"],
        "answer": "C",
        "explanation": "Coulibaly Kuibiert est président de la CEI, non de l'Assemblée Nationale."
    },
    {
        "question": "Combien de femmes ministres compte l’actuel gouvernement ivoirien ?",
        "options": ["A) 7", "B) 8", "C) 10"],
        "answer": "A",
        "explanation": "Le gouvernement compte plusieurs femmes ministres (autour de 6-7)."
    },
    {
        "question": "Quelle est la plus haute juridiction de l’ordre judiciaire ?",
        "options": ["A) Cour d’appel", "B) TPI", "C) Cour suprême", "D) Conseil d’État"],
        "answer": "C",
        "explanation": "La Cour de Cassation (anciennement chambre judiciaire de la Cour Suprême)."
    },
    {
        "question": "Quelle juridiction est compétente en matière administrative ?",
        "options": ["A) Cour de cassation", "B) Conseil d’État", "C) Tribunal pénal"],
        "answer": "B",
        "explanation": "Le Conseil d'État est la plus haute juridiction en matière administrative."
    },
    {
        "question": "Quelle juridiction juge les crimes les plus graves ?",
        "options": ["A) Tribunal correctionnel", "B) Cour d’assises", "C) Tribunal administratif"],
        "answer": "B",
        "explanation": "La Cour d'assises juge les crimes."
    },
    {
        "question": "Les collectivités territoriales comprennent :",
        "options": ["A) États fédérés", "B) Régions, districts, communes", "C) Régions, départements, villages"],
        "answer": "B",
        "explanation": "En Côte d'Ivoire, ce sont principalement les communes, régions et districts autonomes."
    },
    {
        "question": "Qui est l’actuel Ministre de l’urbanisme, du logement et du cadre de vie ?",
        "options": ["A) Bruno N. Koné", "B) Moussa Sanogo", "C) Mariatou Koné"],
        "answer": "A",
        "explanation": "Bruno Nabagné Koné occupe ce poste."
    },
    {
        "question": "Qui a été le premier Directeur Général de l'ENA-CI ?",
        "options": ["A) Félix Houphouët-Boigny", "B) Robert Ropion", "C) Alassane Ouattara", "D) Jeannot Ahoussou Kouadio"],
        "answer": "B",
        "explanation": "Robert Ropion fut le premier DG de l'ENA-CI."
    },
    {
        "question": "Depuis quelle année Yamoussoukro est-elle la capitale politique de la Côte d'Ivoire ?",
        "options": ["A) 1960", "B) 1983", "C) 1990", "D) 1993"],
        "answer": "B",
        "explanation": "Yamoussoukro est la capitale politique depuis 1983."
    },
    {
        "question": "De quelles chambres est composé le parlement bicaméral ivoirien ?",
        "options": ["A) Assemblée Nationale et Conseil Constitutionnel", "B) Sénat et Conseil Économique et Social", "C) Assemblée Nationale et Sénat", "D) Chambre des Députés et Sénat"],
        "answer": "C",
        "explanation": "Le parlement est composé de l'Assemblée Nationale et du Sénat."
    },
    {
        "question": "Qui occupe le poste de Vice-Président de la République de Côte d'Ivoire selon les notes ?",
        "options": ["A) Daniel Kablan Duncan", "B) Tiemoko Meyliet Koné", "C) Patrick Achi", "D) Robert Beugré Mambé"],
        "answer": "B",
        "explanation": "Le VP actuel de la République est Tiemoko Meyliet Koné."
    },
    {
        "question": "Quelle est la juridiction administrative suprême en Côte d'Ivoire ?",
        "options": ["A) La Cour Suprême", "B) La Cour de Cassation", "C) Le Conseil d'État", "D) Le Conseil Constitutionnel"],
        "answer": "C",
        "explanation": "Le Conseil d'État est la juridiction administrative suprême."
    },
    {
        "question": "Quelle juridiction judiciaire est considérée comme suprême ?",
        "options": ["A) Le Conseil d'État", "B) La Cour d'Appel", "C) La Cour d'assises", "D) La Cour de Cassation"],
        "answer": "D",
        "explanation": "La Cour de Cassation est la juridiction judiciaire suprême."
    },
    {
        "question": "Comment qualifie-t-on l'ordre juridictionnel ivoirien ?",
        "options": ["A) Moniste", "B) Unifié", "C) Dualiste", "D) Mixte"],
        "answer": "C",
        "explanation": "L'ordre juridictionnel ivoirien est dualiste."
    },
    {
        "question": "Qui préside le Conseil Constitutionnel ivoirien ?",
        "options": ["A) Mamadou Koné", "B) Chantal Nanaba Camara", "C) Tiemoko Meyliet Koné", "D) René Degni-Ségui"],
        "answer": "B",
        "explanation": "Chantal Nanaba Camara est présidente du Conseil Constitutionnel."
    },
    {
        "question": "Par quelle cour sont jugés les crimes graves ?",
        "options": ["A) Le Tribunal de Première Instance", "B) La Cour de Cassation", "C) La Cour d'assises", "D) Le Conseil d'État"],
        "answer": "C",
        "explanation": "Les crimes graves sont jugés par la Cour d'assises."
    },
    {
        "question": "En quelle année eut lieu la prise de la Bastille ?",
        "options": ["A) 1789", "B) 1792", "C) 1804", "D) 1799"],
        "answer": "A",
        "explanation": "La prise de la Bastille date de 1789."
    },
    {
        "question": "À quelle date Napoléon a-t-il été couronné ?",
        "options": ["A) 14 juillet 1789", "B) 2 décembre 1804", "C) 18 juin 1815", "D) 2 décembre 1851"],
        "answer": "B",
        "explanation": "Napoléon a été couronné le 2 décembre 1804."
    },
    {
        "question": "Quand le Traité de Versailles a-t-il été signé ?",
        "options": ["A) 1914", "B) 1918", "C) 1919", "D) 1945"],
        "answer": "C",
        "explanation": "Le Traité de Versailles date de 1919."
    },
    {
        "question": "En quelle année le Soudan du Sud a-t-il obtenu son indépendance ?",
        "options": ["A) 2010", "B) 2011", "C) 2012", "D) 2013"],
        "answer": "B",
        "explanation": "Le Soudan du Sud est devenu indépendant en 2011 suite à un référendum."
    },
    {
        "question": "Quelle ville organise les Jeux Olympiques en 2024 ?",
        "options": ["A) Londres", "B) Los Angeles", "C) Paris", "D) Tokyo"],
        "answer": "C",
        "explanation": "Les JO de 2024 se déroulent à Paris."
    },
    {
        "question": "Quelle est la capitale du Pakistan ?",
        "options": ["A) Karachi", "B) Lahore", "C) Islamabad", "D) Kaboul"],
        "answer": "C",
        "explanation": "La capitale du Pakistan est Islamabad."
    },
    {
        "question": "Quelle est la monnaie de la Russie ?",
        "options": ["A) Le rouble", "B) L'euro", "C) Le dinar", "D) Le peso"],
        "answer": "A",
        "explanation": "La monnaie de la Russie est le rouble."
    },
    {
        "question": "Qui est l'actuelle Secrétaire Générale de la Francophonie ?",
        "options": ["A) Michaëlle Jean", "B) Louise Mushikiwabo", "C) Aminata Touré", "D) Nkosazana Dlamini-Zuma"],
        "answer": "B",
        "explanation": "Louise Mushikiwabo est la SG de la Francophonie."
    },
    {
        "question": "Où s'est déroulée la CAN 2023 ?",
        "options": ["A) Cameroun", "B) Sénégal", "C) Côte d'Ivoire", "D) Maroc"],
        "answer": "C",
        "explanation": "La CAN 2023 a été organisée en Côte d'Ivoire."
    },
    {
        "question": "Quelle célèbre école a été créée par Aristote ?",
        "options": ["A) L'Académie", "B) Le Lycée", "C) La Sorbonne", "D) Le Portique"],
        "answer": "B",
        "explanation": "Aristote a créé Le Lycée."
    },
    {
        "question": "Que l'entomologie étudie-t-elle ?",
        "options": ["A) Les mots", "B) Les champignons", "C) Les insectes", "D) Les fossiles"],
        "answer": "C",
        "explanation": "L'entomologie est l'étude des insectes."
    },
    {
        "question": "Quelle science a pour objet l'étude des fossiles ?",
        "options": ["A) La paléontologie", "B) L'archéologie", "C) L'entomologie", "D) La géologie"],
        "answer": "A",
        "explanation": "La paléontologie étudie les fossiles."
    },
    {
        "question": "Quelle est la proportion approximative de diazote dans l'atmosphère ?",
        "options": ["A) 21%", "B) 50%", "C) 78%", "D) 90%"],
        "answer": "C",
        "explanation": "Le diazote compose environ 78% de l'atmosphère."
    },
    {
        "question": "Quel mouvement artistique Pablo Picasso a-t-il cofondé ?",
        "options": ["A) L'impressionnisme", "B) Le surréalisme", "C) Le cubisme", "D) Le fauvisme"],
        "answer": "C",
        "explanation": "Pablo Picasso est le cofondateur du cubisme."
    },
    {
        "question": "Qui est l'auteur de l'œuvre 'Les bouts de bois de Dieu' ?",
        "options": ["A) Ahmadou Kourouma", "B) Léopold Sédar Senghor", "C) Sembène Ousmane", "D) Camara Laye"],
        "answer": "C",
        "explanation": "Sembène Ousmane a écrit 'Les bouts de bois de Dieu'."
    },
    {
        "question": "Dans la mythologie grecque, qui a été condamné à pousser éternellement un rocher ?",
        "options": ["A) Atlas", "B) Prométhée", "C) Sisyphe", "D) Tantale"],
        "answer": "C",
        "explanation": "C'est Sisyphe qui fut condamné à pousser un rocher."
    },
    {
        "question": "Qui est la première femme à avoir arbitré un match de football professionnel masculin ?",
        "options": ["A) Bibiana Steinhaus", "B) Stéphanie Frappart", "C) Salima Mukansanga", "D) Yoshimi Yamashita"],
        "answer": "B",
        "explanation": "Stéphanie Frappart est la première femme à arbitrer du foot pro masculin."
    },
    {
        "question": "Quel athlète détient le record du 100m masculin ?",
        "options": ["A) Tyson Gay", "B) Yohan Blake", "C) Asafa Powell", "D) Usain Bolt"],
        "answer": "D",
        "explanation": "Usain Bolt détient le record du 100m masculin."
    },
    {
        "question": "Quelle est la distance exacte du marathon ?",
        "options": ["A) 41,195 km", "B) 42,195 km", "C) 42,000 km", "D) 43,195 km"],
        "answer": "B",
        "explanation": "La distance officielle d'un marathon est de 42,195 km."
    },
    {
        "question": "Que récompense le maillot blanc à pois rouges sur le Tour de France ?",
        "options": ["A) Le meilleur jeune", "B) Le meilleur sprinteur", "C) Le meilleur grimpeur", "D) Le vainqueur du classement général"],
        "answer": "C",
        "explanation": "Il récompense le meilleur grimpeur."
    },
    {
        "question": "Quel pays a été le premier champion du monde de football ?",
        "options": ["A) L'Italie", "B) Le Brésil", "C) L'Argentine", "D) L'Uruguay"],
        "answer": "D",
        "explanation": "L'Uruguay a remporté la première coupe du monde."
    },
    {
        "question": "Quel pays a remporté la Coupe du Monde de football 2022 au Qatar ?",
        "options": ["A) La France", "B) L'Argentine", "C) Le Brésil", "D) L'Espagne"],
        "answer": "B",
        "explanation": "L'Argentine a gagné la Coupe du Monde 2022."
    },
    {
        "question": "De quel pays est originaire le judo ?",
        "options": ["A) Chine", "B) Corée du Sud", "C) Japon", "D) Thaïlande"],
        "answer": "C",
        "explanation": "Le judo est d'origine japonaise."
    },
    {
        "question": "Sur quelle surface se joue le tournoi de Roland-Garros ?",
        "options": ["A) Gazon", "B) Dur", "C) Terre battue", "D) Moquette"],
        "answer": "C",
        "explanation": "Roland-Garros se joue sur terre battue à Paris."
    },
    {
        "question": "Combien de joueurs par équipe y a-t-il sur un terrain de basketball ?",
        "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
        "answer": "B",
        "explanation": "Le basketball se joue à 5 joueurs par équipe."
    },
    {
        "question": "Quel sportif est le plus médaillé de l'histoire des Jeux Olympiques ?",
        "options": ["A) Usain Bolt", "B) Carl Lewis", "C) Michael Phelps", "D) Mark Spitz"],
        "answer": "C",
        "explanation": "Michael Phelps est le sportif le plus médaillé aux JO."
    },
    {
        "question": "Quelle est la capitale politique de la CI ?",
        "options": ["A) Abidjan", "B) Bouaké", "C) Yamoussoukro", "D) Korhogo"],
        "answer": "C",
        "explanation": "Yamoussoukro est la capitale politique."
    },
    {
        "question": "Où s'est tenu le référendum d'indépendance de 2011 ?",
        "options": ["A) Erythrée", "B) Timor oriental", "C) Soudan du Sud", "D) Kosovo"],
        "answer": "C",
        "explanation": "Indépendance du Soudan du Sud en 2011 par référendum."
    },
    {
        "question": "Le mouvement 'Printemps arabe' a commencé en...",
        "options": ["A) 2008", "B) 2010", "C) 2011", "D) 2012"],
        "answer": "B",
        "explanation": "Débuté en 2010."
    },
    {
        "question": "Quel évènement sportif majeur se tiendra à Paris en 2024 ?",
        "options": ["A) La Coupe du monde de Rugby", "B) Les Jeux Olympiques", "C) L'Euro de football", "D) Le championnat du monde d'athlétisme"],
        "answer": "B",
        "explanation": "Paris accueille les JO 2024."
    },
    {
        "question": "Qui a été le premier Directeur Général de l'ENA de Côte d'Ivoire ?",
        "options": ["A) Félix Houphouët-Boigny", "B) Robert Ropion", "C) Charles Konan Banny", "D) Alassane Ouattara"],
        "answer": "B",
        "explanation": "Robert Ropion a été le premier DG de l'École Nationale d'Administration de Côte d'Ivoire à sa création en 1960."
    },
    {
        "question": "En quelle année Yamoussoukro est-elle devenue la capitale politique de la Côte d'Ivoire ?",
        "options": ["A) 1960", "B) 1983", "C) 1990", "D) 1993"],
        "answer": "B",
        "explanation": "Le transfert de la capitale politique et administrative à Yamoussoukro a été acté par la loi de mars 1983."
    },
    {
        "question": "Qui est l'actuel Vice-Président de la République de Côte d'Ivoire (en 2026/2027) ?",
        "options": ["A) Daniel Kablan Duncan", "B) Amadou Gon Coulibaly", "C) Tiemoko Meyliet Koné", "D) Patrick Achi"],
        "answer": "C",
        "explanation": "Tiemoko Meyliet Koné, ancien gouverneur de la BCEAO, occupe ce poste depuis avril 2022."
    },
    {
        "question": "Laquelle de ces institutions est à la tête de l'ordre juridictionnel administratif en Côte d'Ivoire, instaurant ainsi le dualisme juridictionnel ?",
        "options": ["A) La Cour de Cassation", "B) Le Conseil Constitutionnel", "C) Le Conseil d'État", "D) La Cour des Comptes"],
        "answer": "C",
        "explanation": "La réforme constitutionnelle a éclaté l'ancienne Cour Suprême. Le Conseil d'État gère le volet administratif, la Cour de Cassation le judiciaire."
    },
    {
        "question": "Qui a été nommée Présidente du Conseil Constitutionnel de Côte d'Ivoire en 2023 ?",
        "options": ["A) Henriette Diabaté", "B) Kandia Camara", "C) Chantal Nanaba Camara", "D) Simone Gbagbo"],
        "answer": "C",
        "explanation": "Chantal Nanaba Camara est la première femme à présider cette haute institution, nommée par Alassane Ouattara en 2023."
    },
    {
        "question": "Quel pays a remporté la Coupe d'Afrique des Nations (CAN) 2023 organisée en début 2024 ?",
        "options": ["A) Nigeria", "B) Sénégal", "C) Côte d'Ivoire", "D) Maroc"],
        "answer": "C",
        "explanation": "La Côte d'Ivoire (le pays hôte) a remporté la compétition en battant le Nigeria 2-1 en finale."
    },
    {
        "question": "Lequel de ces joueurs ivoiriens a marqué l'un des buts lors de la finale de la CAN 2023 contre le Nigeria ?",
        "options": ["A) Didier Drogba", "B) Sébastien Haller", "C) Yaya Touré", "D) Wilfried Zaha"],
        "answer": "B",
        "explanation": "Sébastien Haller a marqué le but décisif de la victoire (2-1) en finale, après l'égalisation de Franck Kessié."
    },
    {
        "question": "Quelle ville a accueilli les Jeux Olympiques d'été en 2024 ?",
        "options": ["A) Los Angeles", "B) Londres", "C) Paris", "D) Tokyo"],
        "answer": "C",
        "explanation": "Les JO de 2024 se sont déroulés à Paris, en France."
    },
    {
        "question": "Le judo est un art martial originaire de quel pays ?",
        "options": ["A) Chine", "B) Corée du Sud", "C) Japon", "D) Thaïlande"],
        "answer": "C",
        "explanation": "Créé par Jigoro Kano en 1882 au Japon."
    },
    {
        "question": "Le tournoi de tennis de Roland-Garros se joue sur quelle surface ?",
        "options": ["A) Gazon", "B) Terre battue", "C) Dur", "D) Moquette"],
        "answer": "B",
        "explanation": "Roland-Garros est le tournoi du Grand Chelem disputé sur terre battue à Paris."
    },
    {
        "question": "À quelle date Napoléon Bonaparte a-t-il été couronné Empereur des Français ?",
        "options": ["A) 14 juillet 1789", "B) 2 décembre 1804", "C) 18 juin 1815", "D) 9 novembre 1799"],
        "answer": "B",
        "explanation": "Le sacre a eu lieu le 2 décembre 1804 à Notre-Dame de Paris."
    },
    {
        "question": "En quelle année se sont tenus les accords de Bretton Woods instituant le FMI et la Banque Mondiale ?",
        "options": ["A) 1919", "B) 1944", "C) 1945", "D) 1957"],
        "answer": "B",
        "explanation": "La conférence de Bretton Woods s'est tenue en juillet 1944 aux États-Unis."
    },
    {
        "question": "Quelle est la distance exacte du marathon en athlétisme ?",
        "options": ["A) 40,000 km", "B) 42,195 km", "C) 45,000 km", "D) 50,000 km"],
        "answer": "B",
        "explanation": "Distance fixée définitivement depuis les JO de Londres en 1908."
    },
    {
        "question": "Quel est le gaz le plus abondant dans l'atmosphère terrestre ?",
        "options": ["A) Le dioxygène", "B) Le dioxyde de carbone", "C) Le diazote", "D) L'argon"],
        "answer": "C",
        "explanation": "Le diazote compose environ 78% de l'air que nous respirons."
    },
    {
        "question": "Quel philosophe grec a fondé l'école appelée 'Le Lycée' ?",
        "options": ["A) Socrate", "B) Platon", "C) Aristote", "D) Épicure"],
        "answer": "C",
        "explanation": "Platon a fondé l'Académie, Aristote a fondé le Lycée (école péripatéticienne)."
    },
    {
        "question": "De quel courant artistique Pablo Picasso est-il l'un des fondateurs ?",
        "options": ["A) L'impressionnisme", "B) Le surréalisme", "C) Le cubisme", "D) Le fauvisme"],
        "answer": "C",
        "explanation": "Avec Georges Braque, Picasso a été le pionnier du cubisme au début du XXe siècle (ex: Les Demoiselles d'Avignon)."
    },
    {
        "question": "Dans la mythologie grecque, qui fut condamné à pousser éternellement un lourd rocher au sommet d'une montagne ?",
        "options": ["A) Prométhée", "B) Atlas", "C) Sisyphe", "D) Hercule"],
        "answer": "C",
        "explanation": "Le châtiment de Sisyphe symbolise le travail absurde et sans fin."
    },
    {
        "question": "Quelle est la capitale de la région de l'Agnéby-Tiassa en Côte d'Ivoire ?",
        "options": ["A) Divo", "B) Agboville", "C) Adzopé", "D) Sikensi"],
        "answer": "B",
        "explanation": "La région de l'Agnéby-Tiassa (sud de la CI) a pour chef-lieu la ville d'Agboville."
    },
    {
        "question": "Le Parlement de la 3ème République ivoirienne est bicaméral. Il comprend l'Assemblée nationale et...",
        "options": ["A) Le Conseil Économique et Social", "B) Le Sénat", "C) Le Conseil Constitutionnel", "D) La Cour Suprême"],
        "answer": "B",
        "explanation": "La Constitution de 2016 a instauré un Sénat, rendant le parlement bicaméral."
    },
    {
        "question": "Qui a été le premier Président du Sénat de Côte d'Ivoire ?",
        "options": ["A) Amadou Soumahoro", "B) Adama Bictogo", "C) Jeannot Ahoussou Kouadio", "D) Charles Koffi Diby"],
        "answer": "C",
        "explanation": "Jeannot Ahoussou Kouadio a été élu premier président du Sénat ivoirien en 2018."
    },
    {
        "question": "L'élection présidentielle d'octobre 2025 en Côte d'Ivoire a été remportée, selon la CEI, par :",
        "options": ["A) Tidjane Thiam", "B) Jean-Louis Billon", "C) Alassane Ouattara", "D) Simone Gbagbo"],
        "answer": "C",
        "explanation": "Le président sortant, Alassane Ouattara (RHDP), a été réélu pour un quatrième mandat dès le premier tour avec environ 89,7% des suffrages."
    },
    {
        "question": "En 2025, trois pays ouest-africains ont officialisé leur retrait de la CEDEAO pour former la Confédération des États du Sahel (AES). Lesquels ?",
        "options": ["A) Mali, Sénégal, Guinée", "B) Mali, Burkina Faso, Niger", "C) Burkina Faso, Togo, Bénin", "D) Niger, Tchad, Mauritanie"],
        "answer": "B",
        "explanation": "Le Mali, le Burkina Faso et le Niger ont quitté la CEDEAO en janvier 2025 et institutionnalisé l'AES."
    },
    {
        "question": "Qui a remporté le Prix Nobel de Littérature en 2024 ?",
        "options": ["A) Annie Ernaux", "B) Jon Fosse", "C) Han Kang", "D) Haruki Murakami"],
        "answer": "C",
        "explanation": "L'autrice sud-coréenne Han Kang a remporté le prix Nobel de littérature en 2024."
    },
    {
        "question": "Combien d'États membres compte la CEDEAO depuis le retrait définitif des pays de l'AES en 2025 ?",
        "options": ["A) 15", "B) 12", "C) 10", "D) 14"],
        "answer": "B",
        "explanation": "Avec le retrait du Mali, du Burkina Faso et du Niger, la CEDEAO est passée de 15 à 12 membres actifs."
    },
    {
        "question": "Lors des JO de Paris 2024, quel sportif détient encore historiquement le record absolu du nombre de médailles olympiques toutes éditions confondues ?",
        "options": ["A) Usain Bolt", "B) Michael Phelps", "C) Carl Lewis", "D) Léon Marchand"],
        "answer": "B",
        "explanation": "Le nageur américain Michael Phelps détient le record absolu avec 28 médailles, dont 23 en or."
    },
    {
        "question": "Laquelle de ces institutions n'appartient pas au pouvoir judiciaire en Côte d'Ivoire ?",
        "options": ["A) La Cour de Cassation", "B) La Haute Cour de Justice", "C) La Cour des Comptes", "D) Le Conseil des Ministres"],
        "answer": "D",
        "explanation": "Le Conseil des ministres est l'organe du pouvoir exécutif. La Cour des Comptes appartient à l'ordre juridictionnel financier."
    },
    {
        "question": "L'athlète jamaïcain Usain Bolt est célèbre pour son record du monde sur 100m. Quel est son temps record ?",
        "options": ["A) 9,69 s", "B) 9,72 s", "C) 9,58 s", "D) 9,52 s"],
        "answer": "C",
        "explanation": "Il a établi le record de 9,58 s lors des championnats du monde d'athlétisme à Berlin en 2009."
    },
    {
        "question": "Où se situe le siège de l'Union Économique et Monétaire Ouest-Africaine (UEMOA) ?",
        "options": ["A) Dakar", "B) Abidjan", "C) Lomé", "D) Ouagadougou"],
        "answer": "D",
        "explanation": "Le siège de la Commission de l'UEMOA est à Ouagadougou (Burkina Faso)."
    },
    {
        "question": "Où se trouve le siège de la BCEAO (Banque Centrale des États de l'Afrique de l'Ouest) ?",
        "options": ["A) Abidjan", "B) Dakar", "C) Lomé", "D) Niamey"],
        "answer": "B",
        "explanation": "Le siège de la BCEAO est situé à Dakar au Sénégal (bien que son gouverneur actuel, Jean-Claude Kassi Brou, soit de nationalité ivoirienne)."
    },
    {
        "question": "Lors de la CAN 2023, quelle équipe la Côte d'Ivoire a-t-elle éliminée en demi-finale ?",
        "options": ["A) Sénégal", "B) Mali", "C) RD Congo", "D) Guinée équatoriale"],
        "answer": "C",
        "explanation": "La Côte d'Ivoire a battu la RD Congo 1-0 en demi-finale, grâce à un but de Sébastien Haller."
    },
    {
        "question": "En Côte d'Ivoire, l'Autorité Nationale de la Presse (ANP) remplace :",
        "options": ["A) Le CNP", "B) La HACA", "C) Le CICG", "D) Le Conseil d'État"],
        "answer": "A",
        "explanation": "L'ANP (Autorité Nationale de la Presse) a remplacé le Conseil National de la Presse (CNP) comme organe de régulation de la presse écrite."
    },
    {
        "question": "Le 7 août 1960 marque pour la Côte d'Ivoire :",
        "options": ["A) La proclamation de la République", "B) L'indépendance", "C) L'adoption de l'hymne national", "D) Le transfert de la capitale"],
        "answer": "B",
        "explanation": "C'est la date officielle de l'accession de la Côte d'Ivoire à l'indépendance."
    },
    {
        "question": "Quel est le nom de l'hymne national de la Côte d'Ivoire ?",
        "options": ["A) La Concorde", "B) L'Abidjanaise", "C) Le Ditanyè", "D) La Dessalinienne"],
        "answer": "B",
        "explanation": "L'Abidjanaise a été adoptée comme hymne national en 1960."
    },
    {
        "question": "Laquelle de ces villes n'est pas un chef-lieu de district autonome en Côte d'Ivoire ?",
        "options": ["A) Abidjan", "B) Yamoussoukro", "C) San-Pédro", "D) Bocanda"],
        "answer": "D",
        "explanation": "Bocanda est un département situé dans la région du N'Zi, ce n'est pas un chef-lieu de district autonome (comme Abidjan, Yamoussoukro, etc.)."
    },
    {
        "question": "En août 2026, l'Alliance des États du Sahel (AES) a officiellement installé son Parlement confédéral dans quelle ville ?",
        "options": ["A) Bamako", "B) Ouagadougou", "C) Niamey", "D) Agadez"],
        "answer": "C",
        "explanation": "Le parlement confédéral de l'AES (45 députés) a été installé à Niamey au Niger fin août 2026."
    },
    {
        "question": "En histoire, quel traité a mis fin à la Première Guerre mondiale en 1919 ?",
        "options": ["A) Le Traité de Vienne", "B) Le Traité de Versailles", "C) Le Traité de Rome", "D) Le Traité de Tordesillas"],
        "answer": "B",
        "explanation": "Signé le 28 juin 1919 dans la galerie des Glaces du château de Versailles."
    },
    {
        "question": "Qui a succédé à Henri Konan Bédié à la tête du PDCI-RDA après son décès ?",
        "options": ["A) Maurice Kakou Guikahué", "B) Tidjane Thiam", "C) Jean-Louis Billon", "D) Thierry Tanoh"],
        "answer": "B",
        "explanation": "Tidjane Thiam a été élu président du PDCI-RDA en décembre 2023."
    },
    {
        "question": "Quel était le taux de participation officiel selon la CEI lors de l'élection présidentielle ivoirienne d'octobre 2025 ?",
        "options": ["A) Environ 35%", "B) Environ 50%", "C) Environ 75%", "D) Environ 90%"],
        "answer": "B",
        "explanation": "La CEI a enregistré un taux de participation d'environ 50,10 % lors de ce scrutin."
    },
    {
        "question": "Dans le cadre de l'exécution du PND (Plan National de Développement), quelle est la période couverte par le dernier plan en cours avant 2026 ?",
        "options": ["A) 2012-2015", "B) 2016-2020", "C) 2021-2025", "D) 2025-2030"],
        "answer": "C",
        "explanation": "Le gouvernement ivoirien a exécuté le PND sur la période 2021-2025 visant la transformation structurelle de l'économie."
    },
    {
        "question": "Lors de la phase de groupes de la CAN 2023, la Côte d'Ivoire a subi une lourde défaite (0-4) face à quelle équipe ?",
        "options": ["A) Le Nigeria", "B) La Guinée-Bissau", "C) La Guinée équatoriale", "D) Le Sénégal"],
        "answer": "C",
        "explanation": "Le 'Nzalang Nacional' de la Guinée équatoriale a battu les Éléphants 4 à 0 lors de leur 3e match de poule."
    },
    {
        "question": "Quel fleuve ivoirien donne son nom à une région dont le chef-lieu est Sassandra ?",
        "options": ["A) Le Bandama", "B) Le Cavally", "C) Le Sassandra", "D) La Comoé"],
        "answer": "C",
        "explanation": "Le fleuve Sassandra traverse l'ouest du pays et se jette dans le golfe de Guinée au niveau de la ville de Sassandra (région du Gbôklè)."
    },
    {
        "question": "Quelle est la devise de la République de Côte d'Ivoire ?",
        "options": ["A) Union - Travail - Justice", "B) Union - Discipline - Travail", "C) Paix - Travail - Patrie", "D) Fraternité - Travail - Progrès"],
        "answer": "B",
        "explanation": "C'est la devise officielle figurant sur les armoiries de la CI."
    },
    {
        "question": "La Basilique Notre-Dame de la Paix, l'édifice religieux chrétien le plus grand du monde, se trouve à :",
        "options": ["A) Abidjan", "B) Rome", "C) Yamoussoukro", "D) Korhogo"],
        "answer": "C",
        "explanation": "Construite sous la présidence de Félix Houphouët-Boigny, elle a été consacrée en 1990 par le Pape Jean-Paul II."
    },
    {
        "question": "Dans quel sport évolue l'athlète ivoirienne Marie-Josée Ta Lou-Smith ?",
        "options": ["A) Saut en longueur", "B) Taekwondo", "C) Sprint (Athlétisme)", "D) Natation"],
        "answer": "C",
        "explanation": "Elle est une sprinteuse spécialiste des 100m et 200m."
    },
    {
        "question": "Qui fut le fondateur du célèbre empire de Kong au nord de la Côte d'Ivoire au XVIIIe siècle ?",
        "options": ["A) Samory Touré", "B) Sékou Ouattara", "C) Osei Tutu", "D) Abla Pokou"],
        "answer": "B",
        "explanation": "Sékou Ouattara a fondé l'Empire de Kong vers 1710."
    },
    {
        "question": "L'organisation sous-régionale CEDEAO a pour siège principal :",
        "options": ["A) Abidjan", "B) Dakar", "C) Abuja", "D) Accra"],
        "answer": "C",
        "explanation": "Le siège de la Commission de la CEDEAO se trouve à Abuja, la capitale du Nigeria."
    },
    {
        "question": "Dans le contexte de la crise du Sahel, l'opération militaire française qui a pris fin en 2022 s'appelait :",
        "options": ["A) Serval", "B) Sangaris", "C) Barkhane", "D) Takuba"],
        "answer": "C",
        "explanation": "Lancée en 2014 pour succéder à Serval, Barkhane s'est achevée officiellement en novembre 2022 suite aux retraits successifs du Mali puis du Burkina."
    },
    {
        "question": "Quelle est l'année de l'indépendance de la Côte d'Ivoire ?",
        "options": ["A) 1958", "B) 1960", "C) 1962", "D) 1964"],
        "answer": "B",
        "explanation": "La Côte d'Ivoire a obtenu son indépendance le 7 août 1960."
    },
    {
        "question": "Qui fut le premier président de la Côte d'Ivoire ?",
        "options": ["A) Henri Konan Bédié", "B) Laurent Gbagbo", "C) Félix Houphouët-Boigny", "D) Alassane Ouattara"],
        "answer": "C",
        "explanation": "Félix Houphouët-Boigny fut le premier président du pays."
    },
    {
        "question": "Quelle est la capitale politique de la Côte d'Ivoire ?",
        "options": ["A) Abidjan", "B) Bouaké", "C) Yamoussoukro", "D) San-Pédro"],
        "answer": "C",
        "explanation": "Yamoussoukro est la capitale politique de la CI depuis 1983."
    },
    {
        "question": "Dans quelle ville ivoirienne se trouve la basilique Notre-Dame de la Paix ?",
        "options": ["A) Abidjan", "B) Yamoussoukro", "C) Korhogo", "D) Man"],
        "answer": "B",
        "explanation": "La basilique est située à Yamoussoukro."
    },
    {
        "question": "Comment s'appelle l'hymne national ivoirien ?",
        "options": ["A) L'Abidjanaise", "B) La Concorde", "C) Le Ditanyè", "D) L'Ivoirienne"],
        "answer": "A",
        "explanation": "L'hymne national est L'Abidjanaise."
    },
    {
        "question": "Quel fleuve ivoirien donne son nom à un grand barrage hydroélectrique ?",
        "options": ["A) Sassandra", "B) Bandama", "C) Comoé", "D) Cavally"],
        "answer": "B",
        "explanation": "Le barrage de Kossou est sur le fleuve Bandama."
    },
    {
        "question": "Qui est l'auteur du roman 'Les Soleils des indépendances' ?",
        "options": ["A) Bernard Dadié", "B) Ahmadou Kourouma", "C) Camara Laye", "D) Léopold Sédar Senghor"],
        "answer": "B",
        "explanation": "Ahmadou Kourouma a écrit ce célèbre roman."
    },
    {
        "question": "Quelle est la principale culture d'exportation de la Côte d'Ivoire ?",
        "options": ["A) Café", "B) Coton", "C) Cacao", "D) Anacarde"],
        "answer": "C",
        "explanation": "La CI est le premier producteur mondial de cacao."
    },
    {
        "question": "Combien de districts autonomes compte la Côte d'Ivoire ?",
        "options": ["A) 2", "B) 12", "C) 14", "D) 31"],
        "answer": "C",
        "explanation": "La CI compte 14 districts dont 2 autonomes (Abidjan et Yamoussoukro)."
    },
    {
        "question": "Quel parc national ivoirien est célèbre pour ses chimpanzés et sa forêt primaire ?",
        "options": ["A) Parc national de Taï", "B) Parc national du Banco", "C) Parc national de la Comoé", "D) Réserve d'Abokouamékro"],
        "answer": "A",
        "explanation": "Le parc de Taï est classé au patrimoine mondial de l'UNESCO."
    },
    {
        "question": "De quelle région Daloa est-il le chef-lieu ?",
        "options": ["A) Haut-Sassandra", "B) Marahoué", "C) Gôh", "D) Tonkpi"],
        "answer": "A",
        "explanation": "Daloa est la capitale du Haut-Sassandra."
    },
    {
        "question": "En quelle année a eu lieu le coup d'État de Robert Guéï ?",
        "options": ["A) 1993", "B) 1999", "C) 2002", "D) 2010"],
        "answer": "B",
        "explanation": "Le coup d'État a eu lieu le 24 décembre 1999."
    },
    {
        "question": "Quel est le sommet le plus élevé de Côte d'Ivoire ?",
        "options": ["A) Mont Tonkoui", "B) Mont Nimba", "C) Mont Momi", "D) Mont Zo"],
        "answer": "B",
        "explanation": "Le Mont Nimba (1752m) est le point culminant."
    },
    {
        "question": "Dans quel district se trouve la ville de Korhogo ?",
        "options": ["A) District des Savanes", "B) District du Denguélé", "C) District du Woroba", "D) District de la Vallée du Bandama"],
        "answer": "A",
        "explanation": "Korhogo est le chef-lieu du district des Savanes."
    },
    {
        "question": "Quel peuple célèbre la fête de l'Abissa ?",
        "options": ["A) Baoulé", "B) Bété", "C) Nzima", "D) Sénoufo"],
        "answer": "C",
        "explanation": "Les Nzima (Grand-Bassam) célèbrent l'Abissa."
    },
    {
        "question": "Qui est l'actuel Premier ministre de Côte d'Ivoire (2024) ?",
        "options": ["A) Patrick Achi", "B) Robert Beugré Mambé", "C) Amadou Gon Coulibaly", "D) Hamed Bakayoko"],
        "answer": "B",
        "explanation": "Robert Beugré Mambé a été nommé en 2023."
    },
    {
        "question": "Quelle ville ivoirienne est surnommée 'La perle des lagunes' ?",
        "options": ["A) San-Pédro", "B) Grand-Bassam", "C) Abidjan", "D) Jacqueville"],
        "answer": "C",
        "explanation": "Abidjan est surnommée la perle des lagunes."
    },
    {
        "question": "Quel instrument traditionnel est typique de la musique balafon ?",
        "options": ["A) Kora", "B) Balafon", "C) Tam-tam", "D) Djembe"],
        "answer": "B",
        "explanation": "Le balafon est un xylophone traditionnel d'Afrique de l'Ouest."
    },
    {
        "question": "Laquelle de ces villes fut la première capitale de la Côte d'Ivoire coloniale ?",
        "options": ["A) Bingerville", "B) Grand-Bassam", "C) Abidjan", "D) Yamoussoukro"],
        "answer": "B",
        "explanation": "Grand-Bassam fut la première capitale de 1893 à 1896."
    },
    {
        "question": "Quelle ethnie appartient au groupe Akan ?",
        "options": ["A) Les Dan", "B) Les Baoulé", "C) Les Sénoufo", "D) Les Malinké"],
        "answer": "B",
        "explanation": "Les Baoulé font partie du groupe Akan."
    },
    {
        "question": "Quel animal est l'emblème national de la Côte d'Ivoire ?",
        "options": ["A) L'aigle", "B) Le lion", "C) L'éléphant", "D) La panthère"],
        "answer": "C",
        "explanation": "L'éléphant est l'animal symbole du pays."
    },
    {
        "question": "Quel port ivoirien est le premier port exportateur mondial de cacao ?",
        "options": ["A) Port d'Abidjan", "B) Port de San-Pédro", "C) Port de Sassandra", "D) Port de Tabou"],
        "answer": "B",
        "explanation": "San-Pédro est le premier port exportateur de cacao au monde."
    },
    {
        "question": "Qui a composé la musique de l'Abidjanaise ?",
        "options": ["A) Mathieu Ekra", "B) Pierre-Michel Pango", "C) Joachim Bony", "D) Bernard Dadié"],
        "answer": "B",
        "explanation": "L'Abbé Pierre-Michel Pango a composé la musique."
    },
    {
        "question": "Quel pont emblématique relie le Plateau à Treichville à Abidjan ?",
        "options": ["A) Pont Houphouët-Boigny", "B) Pont De Gaulle", "C) Pont HKB", "D) Pont Alassane Ouattara"],
        "answer": "A",
        "explanation": "Le pont Félix Houphouët-Boigny fut le premier pont construit."
    },
    {
        "question": "En Côte d'Ivoire, quelle institution juge les contentieux électoraux des élections locales ?",
        "options": ["A) La Cour de Cassation", "B) Le Conseil Constitutionnel", "C) Le Conseil d'État", "D) La Commission Électorale Indépendante"],
        "answer": "C",
        "explanation": "Le Conseil d'État juge les contentieux des élections locales."
    },
    {
        "question": "Quel est le plus long fleuve s'écoulant entièrement sur le territoire ivoirien ?",
        "options": ["A) Le Cavally", "B) La Comoé", "C) Le Bandama", "D) Le Sassandra"],
        "answer": "C",
        "explanation": "Le Bandama (1050 km) coule uniquement en CI."
    },
    {
        "question": "Quelle danse traditionnelle est inscrite au patrimoine culturel immatériel de l'UNESCO ?",
        "options": ["A) Le Gbofe", "B) Le Zaouli", "C) Le Tématé", "D) Le Boloye"],
        "answer": "B",
        "explanation": "Le Zaouli des communautés Gouro est inscrit à l'UNESCO."
    },
    {
        "question": "Dans quelle région se trouve la ville de Man ?",
        "options": ["A) Tonkpi", "B) Guémon", "C) Cavally", "D) Bafing"],
        "answer": "A",
        "explanation": "Man est le chef-lieu de la région du Tonkpi."
    },
    {
        "question": "Quelle célèbre figure féminine a conduit les Baoulé en Côte d'Ivoire ?",
        "options": ["A) Anne Zingha", "B) Abla Pokou", "C) Yennenga", "D) Ndaté Yalla"],
        "answer": "B",
        "explanation": "La reine Abla Pokou a mené l'exode des Baoulé depuis le Ghana."
    },
    {
        "question": "Quel traité de 1893 a officialisé la colonie de Côte d'Ivoire ?",
        "options": ["A) Traité de Berlin", "B) Décret de 1893", "C) Traité de Versailles", "D) Accords de Grand-Bassam"],
        "answer": "B",
        "explanation": "Le décret du 10 mars 1893 institue la colonie."
    },
    {
        "question": "Quelle est l'organisation sous-régionale dont le siège est à Abuja ?",
        "options": ["A) UEMOA", "B) CEDEAO", "C) CEMAC", "D) Union Africaine"],
        "answer": "B",
        "explanation": "La CEDEAO a son siège au Nigeria, à Abuja."
    },
    {
        "question": "Qui est l'actuelle directrice générale de l'OMC (Organisation mondiale du commerce) ?",
        "options": ["A) Ngozi Okonjo-Iweala", "B) Christine Lagarde", "C) Kristalina Georgieva", "D) Amina J. Mohammed"],
        "answer": "A",
        "explanation": "La Nigériane Ngozi Okonjo-Iweala dirige l'OMC."
    },
    {
        "question": "Quel est le nombre de membres actuels du Conseil de Sécurité de l'ONU ?",
        "options": ["A) 10", "B) 15", "C) 20", "D) 25"],
        "answer": "B",
        "explanation": "Il y a 5 membres permanents et 10 non permanents."
    },
    {
        "question": "Quelle est la capitale économique du Bénin ?",
        "options": ["A) Porto-Novo", "B) Cotonou", "C) Parakou", "D) Ouidah"],
        "answer": "B",
        "explanation": "Cotonou est la capitale économique, Porto-Novo la politique."
    },
    {
        "question": "Qui fut le premier secrétaire général africain de l'ONU ?",
        "options": ["A) Kofi Annan", "B) Boutros Boutros-Ghali", "C) Ban Ki-moon", "D) U Thant"],
        "answer": "B",
        "explanation": "L'Égyptien Boutros Boutros-Ghali fut le premier Africain SG de l'ONU."
    },
    {
        "question": "En mathématiques, comment appelle-t-on un polygone à 8 côtés ?",
        "options": ["A) Hexagone", "B) Heptagone", "C) Octogone", "D) Décagone"],
        "answer": "C",
        "explanation": "Un octogone a 8 côtés."
    },
    {
        "question": "Quelle planète est surnommée la planète rouge ?",
        "options": ["A) Vénus", "B) Jupiter", "C) Mars", "D) Saturne"],
        "answer": "C",
        "explanation": "Mars est surnommée la planète rouge."
    },
    {
        "question": "Qui a écrit le célèbre roman 'L'Étranger' ?",
        "options": ["A) Jean-Paul Sartre", "B) Albert Camus", "C) Marcel Proust", "D) Victor Hugo"],
        "answer": "B",
        "explanation": "Albert Camus a publié L'Étranger en 1942."
    },
    {
        "question": "Quel est l'océan le plus profond du monde ?",
        "options": ["A) Atlantique", "B) Indien", "C) Arctique", "D) Pacifique"],
        "answer": "D",
        "explanation": "L'océan Pacifique contient la fosse des Mariannes, le point le plus profond."
    },
    {
        "question": "Combien de jours compte une année bissextile ?",
        "options": ["A) 364", "B) 365", "C) 366", "D) 367"],
        "answer": "C",
        "explanation": "Une année bissextile compte 366 jours."
    },
    {
        "question": "Comment Brice Clotaire Oligui N'Guema est-il d'abord arrivé au pouvoir au Gabon avant l'élection présidentielle de 2025 ?",
        "options": ["A) Par élection en 2020", "B) Suite au coup d'État militaire du 30 août 2023", "C) Par succession constitutionnelle", "D) Sur décision de l'Union Africaine"],
        "answer": "B",
        "explanation": "Le général Oligui N'Guema a pris le pouvoir le 30 août 2023 à la tête du CTRI suite à un coup d'État renversant Ali Bongo, avant la transition et l'élection d'avril 2025."
    },
    {
        "question": "Qui a remporté le Ballon d'Or 2023 ?",
        "options": ["A) Erling Haaland", "B) Lionel Messi", "C) Kylian Mbappé", "D) Karim Benzema"],
        "answer": "B",
        "explanation": "Lionel Messi a remporté son 8e Ballon d'Or en 2023, l'édition 2020 ayant été annulée."
    },
]

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
        "question": "Combien d'États membres compte l'UEMOA ?",
        "options": ["A) 5", "B) 8", "C) 10", "D) 12"],
        "answer": "B",
        "explanation": "L'UEMOA compte 8 États membres partageant le franc CFA."
    },
    {
        "question": "Quel est le siège de la Banque Centrale des États de l'Afrique de l'Ouest (BCEAO) ?",
        "options": ["A) Abidjan", "B) Bamako", "C) Dakar", "D) Ouagadougou"],
        "answer": "C",
        "explanation": "La BCEAO a son siège à Dakar (Sénégal)."
    },
    {
        "question": "Quel organisme de l'ONU s'occupe des réfugiés ?",
        "options": ["A) UNICEF", "B) HCR (UNHCR)", "C) OMS", "D) PAM"],
        "answer": "B",
        "explanation": "Le Haut-Commissariat des Nations Unies pour les Réfugiés (HCR) protège les réfugiés dans le monde."
    },
    {
        "question": "Quelle organisation africaine a succédé à l'Organisation de l'Unité Africaine (OUA) ?",
        "options": ["A) La CEDEAO", "B) L'Union Africaine", "C) La SADC", "D) Le NEPAD"],
        "answer": "B",
        "explanation": "L'Union Africaine a remplacé l'OUA en 2002 à Durban (Afrique du Sud)."
    },
    {
        "question": "Quel est le rôle du FMI (Fonds Monétaire International) ?",
        "options": ["A) Financer les guerres", "B) Assurer la stabilité financière internationale", "C) Construire des infrastructures", "D) Gérer les migrations"],
        "answer": "B",
        "explanation": "Le FMI assure la stabilité du système monétaire international et aide les pays en difficulté."
    },
    {
        "question": "Quelle est la différence entre la Cour Internationale de Justice (CIJ) et la Cour Pénale Internationale (CPI) ?",
        "options": ["A) Aucune différence", "B) CIJ juge les États ; CPI juge les individus", "C) CPI est plus ancienne", "D) La CIJ est privée"],
        "answer": "B",
        "explanation": "La CIJ règle les différends entre États ; la CPI poursuit les individus pour crimes internationaux."
    },
    {
        "question": "Quel est le siège de l'Organisation Mondiale du Commerce (OMC) ?",
        "options": ["A) New York", "B) Bruxelles", "C) Genève", "D) Paris"],
        "answer": "C",
        "explanation": "L'OMC est basée à Genève, en Suisse."
    },
    {
        "question": "Quel est le siège de la CEDEAO ?",
        "options": ["A) Dakar", "B) Accra", "C) Abuja", "D) Lagos"],
        "answer": "C",
        "explanation": "Le siège de la CEDEAO est à Abuja, Nigeria."
    },
    {
        "question": "Quelle organisation internationale a pour mission principale le maintien de la paix et de la sécurité internationales ?",
        "options": ["A) L'UNESCO", "B) Le FMI", "C) L'ONU", "D) L'OMC"],
        "answer": "C",
        "explanation": "L'ONU, notamment via son Conseil de Sécurité, a pour mission centrale le maintien de la paix."
    },
    {
        "question": "Quel traité fonde l'Union Européenne dans sa forme actuelle ?",
        "options": ["A) Traité de Rome", "B) Traité de Maastricht", "C) Traité de Lisbonne", "D) Traité de Paris"],
        "answer": "C",
        "explanation": "Le Traité de Lisbonne (2007, en vigueur en 2009) fonde l'UE dans sa forme actuelle."
    },
    {
        "question": "Quelle est la devise officielle de l'Union Africaine ?",
        "options": ["A) « Unité, Solidarité, Développement »", "B) « Une Afrique unie et forte »", "C) « Afrique d'abord »", "D) « L'Afrique en marche »"],
        "answer": "A",
        "explanation": "La devise de l'UA est « Une Afrique unie et forte » en réalité, mais son slogan est souvent résumé à l'unité africaine."
    },
    {
        "question": "Quel est le nom du programme de développement de l'UA lancé en 2001 ?",
        "options": ["A) Plan Marshall africain", "B) NEPAD", "C) AGOA", "D) Agenda 2063"],
        "answer": "B",
        "explanation": "Le NEPAD (Nouveau Partenariat pour le Développement de l'Afrique) a été lancé en 2001."
    },
    {
        "question": "Quel organe de l'ONU conseille sur les questions économiques et sociales ?",
        "options": ["A) Le Conseil de sécurité", "B) L'Assemblée Générale", "C) Le ECOSOC", "D) La CIJ"],
        "answer": "C",
        "explanation": "Le Conseil Économique et Social (ECOSOC) coordonne les travaux économiques et sociaux de l'ONU."
    },
    {
        "question": "Quel est le siège de l'Organisation Internationale du Travail (OIT) ?",
        "options": ["A) Paris", "B) New York", "C) Genève", "D) Bruxelles"],
        "answer": "C",
        "explanation": "L'OIT, fondée en 1919, a son siège à Genève. C'est la plus ancienne agence spécialisée de l'ONU."
    },
    {
        "question": "Quelle organisation regroupe les pays d'Afrique centrale ?",
        "options": ["A) CEDEAO", "B) UEMOA", "C) CEEAC", "D) SADC"],
        "answer": "C",
        "explanation": "La Communauté Économique des États de l'Afrique Centrale (CEEAC) regroupe les pays d'Afrique centrale."
    },
    {
        "question": "Quel est le siège du G20 (secrétariat) ?",
        "options": ["A) Washington", "B) Bruxelles", "C) Il est tournant (présidence rotative)", "D) New York"],
        "answer": "C",
        "explanation": "Le G20 n'a pas de siège fixe. La présidence et le secrétariat tournent chaque année."
    },
    {
        "question": "Quelle organisation émet le franc CFA de la zone CEMAC ?",
        "options": ["A) BCEAO", "B) BEAC", "C) BM", "D) FMI"],
        "answer": "B",
        "explanation": "La BEAC (Banque des États de l'Afrique Centrale) émet le franc CFA pour la zone CEMAC."
    },
    {
        "question": "Quel pays a été exclu de l'Union Africaine en 2019 suite à un coup d'État ?",
        "options": ["A) Mali", "B) Guinée", "C) Soudan", "D) Zimbabwe"],
        "answer": "C",
        "explanation": "Le Soudan a été suspendu de l'UA en 2019 après la chute d'Omar el-Béchir."
    },
    {
        "question": "Quelle organisation régionale regroupe les pays du Maghreb ?",
        "options": ["A) UMA", "B) CEN-SAD", "C) IGAD", "D) Ligue arabe"],
        "answer": "A",
        "explanation": "L'Union du Maghreb Arabe (UMA) regroupe Algérie, Libye, Maroc, Mauritanie et Tunisie."
    },
    {
        "question": "Quel est le rôle de l'AIEA (Agence Internationale de l'Énergie Atomique) ?",
        "options": ["A) Produire l'énergie nucléaire", "B) Promouvoir l'usage pacifique du nucléaire et prévenir sa prolifération", "C) Gérer les déchets nucléaires mondiaux", "D) Financer les centrales nucléaires"],
        "answer": "B",
        "explanation": "L'AIEA, basée à Vienne, promeut l'utilisation pacifique du nucléaire et surveille la non-prolifération."
    },
    {
        "question": "Quelle institution internationale a pour mission l'éradication de la pauvreté dans le monde ?",
        "options": ["A) FMI", "B) Banque Mondiale", "C) OMC", "D) OMS"],
        "answer": "B",
        "explanation": "La Banque Mondiale a pour objectif principal la réduction de la pauvreté et le développement."
    },
    {
        "question": "Quel est le programme des Nations Unies pour l'environnement ?",
        "options": ["A) PNUE", "B) FAO", "C) UNESCO", "D) PNUD"],
        "answer": "A",
        "explanation": "Le PNUE (Programme des Nations Unies pour l'Environnement) coordonne les actions environnementales de l'ONU."
    },
    {
        "question": "Quelle organisation internationale régit le commerce international des armes ?",
        "options": ["A) Interpol", "B) Traité sur le commerce des armes (TCA/ONU)", "C) OTAN", "D) OMC"],
        "answer": "B",
        "explanation": "Le Traité sur le Commerce des Armes (2013) encadre les transferts internationaux d'armements."
    },
    {
        "question": "Quel est le siège de l'OCDE (Organisation de Coopération et de Développement Économiques) ?",
        "options": ["A) Bruxelles", "B) Genève", "C) Paris", "D) New York"],
        "answer": "C",
        "explanation": "L'OCDE est basée à Paris, France."
    },
    {
        "question": "En quelle année l'OUA (Organisation de l'Unité Africaine) a-t-elle été fondée ?",
        "options": ["A) 1955", "B) 1963", "C) 1970", "D) 1980"],
        "answer": "B",
        "explanation": "L'OUA a été fondée le 25 mai 1963 à Addis-Abeba, Éthiopie."
    },
    {
        "question": "Quel est le programme de développement durable de l'ONU à l'horizon 2030 ?",
        "options": ["A) Agenda 2063", "B) ODD (Objectifs de Développement Durable)", "C) Plan Marshall", "D) Accord de Paris"],
        "answer": "B",
        "explanation": "Les 17 ODD (Objectifs de Développement Durable) ont été adoptés en 2015 pour l'horizon 2030."
    },
    {
        "question": "Quel est le siège du Parlement Panafricain ?",
        "options": ["A) Addis-Abeba", "B) Midrand (Afrique du Sud)", "C) Abuja", "D) Accra"],
        "answer": "B",
        "explanation": "Le Parlement Panafricain siège à Midrand, en Afrique du Sud."
    },
    {
        "question": "Quel accord international a remplacé le Protocole de Kyoto ?",
        "options": ["A) Accord de Copenhague", "B) Accord de Paris", "C) Accord de Montréal", "D) Convention de Rio"],
        "answer": "B",
        "explanation": "L'Accord de Paris (COP21, 2015) a remplacé le Protocole de Kyoto pour la lutte contre le changement climatique."
    },
    {
        "question": "Quelle organisation internationale défend les droits de l'enfant ?",
        "options": ["A) HCR", "B) UNICEF", "C) OMS", "D) OIT"],
        "answer": "B",
        "explanation": "L'UNICEF (Fonds des Nations Unies pour l'Enfance) œuvre pour les droits et le bien-être des enfants."
    },
    {
        "question": "Quelle est la principale mission de l'UNESCO ?",
        "options": ["A) Maintien de la paix militaire", "B) Promotion de la coopération internationale en éducation, sciences et culture", "C) Régulation du commerce mondial", "D) Contrôle de l'armement nucléaire"],
        "answer": "B",
        "explanation": "L'UNESCO promeut la paix par l'éducation, les sciences, la culture et la communication."
    },
    {
        "question": "Quel État membre de l'ONU bénéficie d'un statut d'observateur (non-membre votant) ?",
        "options": ["A) La Suisse", "B) Le Vatican", "C) Le Liechtenstein", "D) San Marin"],
        "answer": "B",
        "explanation": "Le Vatican (Saint-Siège) est observateur non-membre à l'ONU. La Suisse est membre à part entière depuis 2002."
    },
    {
        "question": "Quel organe de l'ONU élit le Secrétaire Général ?",
        "options": ["A) Le Conseil de Sécurité seul", "B) L'Assemblée Générale sur recommandation du Conseil de Sécurité", "C) Les 5 membres permanents", "D) L'Assemblée Générale seule"],
        "answer": "B",
        "explanation": "Le SG est nommé par l'AG sur recommandation du CS (article 97 de la Charte de l'ONU)."
    },
    {
        "question": "Quelle organisation internationale lutte contre le blanchiment d'argent ?",
        "options": ["A) Interpol", "B) GAFI (FATF)", "C) FMI", "D) OMC"],
        "answer": "B",
        "explanation": "Le GAFI (Groupe d'Action Financière/Financial Action Task Force) combat le blanchiment et le financement du terrorisme."
    },
    {
        "question": "Combien de langues officielles compte l'Union Africaine ?",
        "options": ["A) 2", "B) 4", "C) 6", "D) 11"],
        "answer": "C",
        "explanation": "L'Union Africaine compte 6 langues officielles de travail : l'arabe, l'anglais, le français, le portugais, l'espagnol et le kiswahili (adopté officiellement en 2022)."
    },
    {
        "question": "Quel est le siège de la Banque Africaine de Développement (BAD) ?",
        "options": ["A) Addis-Abeba", "B) Abidjan", "C) Dakar", "D) Johannesburg"],
        "answer": "B",
        "explanation": "Le siège de la BAD est à Abidjan, Côte d'Ivoire."
    },
    {
        "question": "L'accord de Cotonou (2000) régissait les relations entre quels acteurs ?",
        "options": ["A) CEDEAO et UA", "B) UE et pays ACP (Afrique-Caraïbes-Pacifique)", "C) ONU et pays en développement", "D) FMI et pays endettés"],
        "answer": "B",
        "explanation": "L'accord de Cotonou organisait le partenariat entre l'UE et les 79 pays ACP en matière de développement et commerce."
    },
    {
        "question": "Quel est le siège du Conseil de Sécurité de l'ONU ?",
        "options": ["A) Genève", "B) Washington", "C) New York", "D) La Haye"],
        "answer": "C",
        "explanation": "Le Conseil de Sécurité siège au Siège de l'ONU à New York."
    },
    {
        "question": "Quel mécanisme de l'ONU permet aux États de soumettre des questions à l'Assemblée Générale pour une session extraordinaire d'urgence ?",
        "options": ["A) La résolution « Acheson »", "B) La résolution 377 (Unis pour la Paix)", "C) L'article 51 de la Charte", "D) Le protocole facultatif"],
        "answer": "B",
        "explanation": "La résolution 377 (Unis pour la Paix, 1950) permet à l'AG de se réunir en session d'urgence si le CS est bloqué."
    },
    {
        "question": "Quelle organisation internationale coordonne les politiques d'aviation civile ?",
        "options": ["A) OACI", "B) IATA", "C) OTAN", "D) OMM"],
        "answer": "A",
        "explanation": "L'OACI (Organisation de l'Aviation Civile Internationale) est l'agence spécialisée de l'ONU pour l'aviation civile."
    },
    {
        "question": "Quel est le principal organe judiciaire de l'UEMOA ?",
        "options": ["A) La Cour de Justice", "B) La Cour Arbitrale", "C) La Cour Suprême régionale", "D) La Chambre d'appel"],
        "answer": "A",
        "explanation": "La Cour de Justice de l'UEMOA est l'organe juridictionnel chargé d'interpréter et d'appliquer le droit communautaire."
    },
    {
        "question": "Quel est le nom complet de la CEDEAO en anglais ?",
        "options": ["A) ECOWAS", "B) OECAS", "C) WAEMU", "D) SADC"],
        "answer": "A",
        "explanation": "ECOWAS = Economic Community of West African States (CEDEAO en français)."
    },
    {
        "question": "Quel est le rôle du Conseil de Paix et de Sécurité (CPS) de l'UA ?",
        "options": ["A) Gérer les élections africaines", "B) Prévenir, gérer et résoudre les conflits en Afrique", "C) Coordonner les politiques économiques", "D) Contrôler les migrations"],
        "answer": "B",
        "explanation": "Le CPS de l'UA est l'organe de sécurité collective chargé de prévenir et gérer les conflits africains."
    },
    {
        "question": "Quel est le siège de la Cour de Justice de la CEDEAO ?",
        "options": ["A) Lagos", "B) Accra", "C) Abuja", "D) Dakar"],
        "answer": "C",
        "explanation": "La Cour de Justice de la CEDEAO siège à Abuja, Nigeria."
    },
    {
        "question": "Où se trouve le siège de la Commission de la CEDEAO ?",
        "options": ["A) Dakar, Sénégal", "B) Abuja, Nigeria", "C) Accra, Ghana", "D) Abidjan, Côte d'Ivoire"],
        "answer": "B",
        "explanation": "Le siège de la CEDEAO (Commission) est situé à Abuja au Nigeria."
    },
    {
        "question": "Quelle est la date de création de la CEDEAO ?",
        "options": ["A) 25 mai 1963", "B) 28 mai 1975", "C) 10 janvier 1994", "D) 15 avril 1975"],
        "answer": "B",
        "explanation": "La CEDEAO a été créée le 28 mai 1975 par le Traité de Lagos."
    },
    {
        "question": "Parmi les institutions suivantes, laquelle ne fait pas partie de l'UEMOA ?",
        "options": ["A) La Cour de Justice", "B) La Banque Ouest Africaine de Développement (BOAD)", "C) Le Parlement de la CEDEAO", "D) La Cour des Comptes"],
        "answer": "C",
        "explanation": "Le Parlement de la CEDEAO est une institution de la CEDEAO, non de l'UEMOA."
    },
    {
        "question": "En quelle année l'Organisation de l'Unité Africaine (OUA) est-elle devenue l'Union Africaine (UA) ?",
        "options": ["A) 1999", "B) 2000", "C) 2001", "D) 2002"],
        "answer": "D",
        "explanation": "L'OUA a été officiellement remplacée par l'Union Africaine en 2002 à Durban."
    },
    {
        "question": "Combien de pays membres compte l'UEMOA ?",
        "options": ["A) 7", "B) 8", "C) 15", "D) 16"],
        "answer": "B",
        "explanation": "L'UEMOA compte 8 États membres : Bénin, Burkina Faso, Côte d'Ivoire, Guinée-Bissau, Mali, Niger, Sénégal et Togo."
    },
    {
        "question": "Où est situé le siège de la Banque Africaine de Développement (BAD) ?",
        "options": ["A) Tunis", "B) Addis-Abeba", "C) Abidjan", "D) Johannesburg"],
        "answer": "C",
        "explanation": "Le siège statutaire de la BAD est à Abidjan, en Côte d'Ivoire."
    },
    {
        "question": "Lequel de ces organes est l'organe décisionnel suprême de l'Union Africaine ?",
        "options": ["A) Le Conseil de Paix et de Sécurité", "B) Le Conseil exécutif", "C) La Commission de l'Union africaine", "D) La Conférence des chefs d'État et de gouvernement"],
        "answer": "D",
        "explanation": "La Conférence des chefs d'État et de gouvernement est l'organe suprême de l'UA."
    },
    {
        "question": "Quel est le but principal de la ZLECAf ?",
        "options": ["A) Créer une monnaie unique africaine", "B) Établir une zone de libre-échange continentale en Afrique", "C) Unifier les armées africaines", "D) Promouvoir la culture africaine exclusivement"],
        "answer": "B",
        "explanation": "La ZLECAf vise à créer un marché unique pour les biens et services en Afrique."
    },
    {
        "question": "Quel organe de l'ONU est responsable du maintien de la paix et de la sécurité internationales ?",
        "options": ["A) L'Assemblée générale", "B) Le Conseil de sécurité", "C) La Cour internationale de Justice", "D) Le Secrétariat"],
        "answer": "B",
        "explanation": "C'est la mission principale du Conseil de sécurité de l'ONU."
    },
    {
        "question": "Combien de membres permanents siègent au Conseil de sécurité de l'ONU ?",
        "options": ["A) 5", "B) 10", "C) 15", "D) 20"],
        "answer": "A",
        "explanation": "Il y a 5 membres permanents (Chine, États-Unis, France, Royaume-Uni, Russie)."
    },
    {
        "question": "Où siège la Cour pénale internationale (CPI) ?",
        "options": ["A) Genève", "B) New York", "C) La Haye", "D) Strasbourg"],
        "answer": "C",
        "explanation": "La CPI a son siège à La Haye, aux Pays-Bas."
    },
    {
        "question": "Quelle institution de Bretton Woods a pour but principal d'aider au développement économique et de réduire la pauvreté ?",
        "options": ["A) L'OMC", "B) Le FMI", "C) La Banque Mondiale", "D) L'OIT"],
        "answer": "C",
        "explanation": "La Banque Mondiale finance le développement, tandis que le FMI gère la stabilité financière mondiale."
    },
    {
        "question": "Lequel de ces pays a quitté la CEDEAO puis y est retourné ?",
        "options": ["A) Mauritanie", "B) Maroc", "C) Mali", "D) Aucun, la Mauritanie a quitté et n'est pas revenue"],
        "answer": "D",
        "explanation": "La Mauritanie a quitté la CEDEAO en 2000 et n'en est plus membre à part entière."
    },
    {
        "question": "Quel traité a institué l'UEMOA ?",
        "options": ["A) Traité de Dakar", "B) Traité de Lomé", "C) Traité de Bamako", "D) Traité de Cotonou"],
        "answer": "A",
        "explanation": "L'UEMOA a été créée par le Traité de Dakar signé le 10 janvier 1994."
    },
    {
        "question": "Laquelle de ces institutions est une agence spécialisée de l'ONU basée à Paris ?",
        "options": ["A) OMS", "B) UNESCO", "C) FAO", "D) OIT"],
        "answer": "B",
        "explanation": "L'UNESCO, chargée de l'éducation, de la science et de la culture, a son siège à Paris."
    },
    {
        "question": "Quel Ivoirien a été Secrétaire général adjoint des Nations Unies aux opérations de maintien de la paix ?",
        "options": ["A) Amara Essy", "B) Jean-Claude Brou", "C) Youssoufou Bamba", "D) Il n'y a pas eu d'Ivoirien à ce poste spécifique récemment"],
        "answer": "D",
        "explanation": "Piège, c'est le Français Jean-Pierre Lacroix ou Hervé Ladsous, pas un Ivoirien. (Amara Essy fut SG de l'OUA)."
    },
    {
        "question": "Qui a été le premier Secrétaire général de l'Organisation de l'Unité Africaine (OUA) ?",
        "options": ["A) Diallo Telli", "B) Edem Kodjo", "C) Nzo Ekangaki", "D) William Eteki Mboumoua"],
        "answer": "A",
        "explanation": "Le Guinéen Diallo Telli fut le premier Secrétaire général de l'OUA de 1964 à 1972."
    },
    {
        "question": "Laquelle de ces organisations a pour siège Genève ?",
        "options": ["A) FMI", "B) OMC", "C) FAO", "D) AIEA"],
        "answer": "B",
        "explanation": "L'Organisation Mondiale du Commerce (OMC) est basée à Genève, Suisse."
    },
    {
        "question": "En 2024, quel pays a annoncé son retrait de la CEDEAO avec le Mali et le Burkina Faso ?",
        "options": ["A) Guinée", "B) Niger", "C) Tchad", "D) Sénégal"],
        "answer": "B",
        "explanation": "Le Niger, avec le Mali et le Burkina Faso, a annoncé son retrait de la CEDEAO début 2024."
    },
    {
        "question": "L'Organisation Internationale de la Francophonie (OIF) a son siège à :",
        "options": ["A) Bruxelles", "B) Genève", "C) Paris", "D) Montréal"],
        "answer": "C",
        "explanation": "Le siège de l'OIF est à Paris, en France."
    },
    {
        "question": "L'Ivoirien Jean-Claude Kassi Brou a été président de quelle commission de 2018 à 2022 ?",
        "options": ["A) Commission de l'UEMOA", "B) Commission de la CEDEAO", "C) Commission de l'Union Africaine", "D) Commission économique pour l'Afrique"],
        "answer": "B",
        "explanation": "Il fut Président de la Commission de la CEDEAO avant de diriger la BCEAO."
    },
    {
        "question": "Quel est le nom actuel du traité liant l'Union européenne aux pays ACP (Afrique, Caraïbes, Pacifique) ?",
        "options": ["A) Accord de Cotonou", "B) Accord de Lomé", "C) Accord de Samoa", "D) Accord de Yaoundé"],
        "answer": "C",
        "explanation": "L'Accord de Samoa a remplacé l'Accord de Cotonou depuis 2023."
    },
    {
        "question": "Dans le système des Nations Unies, que signifie le sigle HCR ?",
        "options": ["A) Haut Commissariat aux Réfugiés", "B) Haut Conseil pour la Reconstruction", "C) Haut Commissariat pour le Climat et les Réfugiés", "D) Haut Comité de Résolution"],
        "answer": "A",
        "explanation": "HCR signifie Haut Commissariat des Nations Unies pour les Réfugiés."
    },
    {
        "question": "Qui nomme le Secrétaire général des Nations Unies ?",
        "options": ["A) Le Conseil de Sécurité", "B) L'Assemblée générale sur recommandation du Conseil de sécurité", "C) La Cour internationale de Justice", "D) Les 5 membres permanents seuls"],
        "answer": "B",
        "explanation": "L'Assemblée générale nomme le SG sur recommandation du Conseil de sécurité."
    },
    {
        "question": "La Cour de justice de la CEDEAO a son siège à :",
        "options": ["A) Lomé", "B) Abuja", "C) Dakar", "D) Abidjan"],
        "answer": "B",
        "explanation": "Le siège de la Cour de justice de la CEDEAO est également à Abuja, au Nigeria."
    },
    {
        "question": "Quel est l'objectif principal du NEPAD ?",
        "options": ["A) Favoriser la démocratie en Europe", "B) Éradiquer la pauvreté et placer l'Afrique sur la voie du développement", "C) Créer une alliance militaire africaine", "D) Lutter contre les pandémies"],
        "answer": "B",
        "explanation": "Le Nouveau Partenariat pour le Développement de l'Afrique vise le développement socio-économique du continent."
    },
    {
        "question": "La monnaie de l'UEMOA, le franc CFA, est émise par :",
        "options": ["A) La BEAC", "B) La BCEAO", "C) La BOAD", "D) La BAD"],
        "answer": "B",
        "explanation": "La Banque Centrale des États de l'Afrique de l'Ouest (BCEAO) émet le franc CFA de l'UEMOA."
    },
    {
        "question": "Lequel de ces États est membre de la CEMAC mais pas de l'UEMOA ?",
        "options": ["A) Togo", "B) Mali", "C) Gabon", "D) Guinée-Bissau"],
        "answer": "C",
        "explanation": "Le Gabon appartient à la CEMAC (Afrique centrale) et non à l'UEMOA (Afrique de l'Ouest)."
    },
    {
        "question": "Quel traité est à l'origine de l'Union européenne (1992) ?",
        "options": ["A) Traité de Rome", "B) Traité de Maastricht", "C) Traité d'Amsterdam", "D) Traité de Lisbonne"],
        "answer": "B",
        "explanation": "Le traité de Maastricht a officiellement créé l'Union européenne."
    },
    {
        "question": "La Côte d'Ivoire est le premier producteur mondial de :",
        "options": ["A) Café", "B) Cacao", "C) Hévéa", "D) Anacarde"],
        "answer": "B",
        "explanation": "La Côte d'Ivoire est le 1er producteur mondial de cacao."
    },
    {
        "question": "Le Conseil de l'Entente, créé en 1959, regroupe combien d'États ?",
        "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
        "answer": "B",
        "explanation": "Il regroupe 5 pays : Côte d'Ivoire, Niger, Burkina Faso, Bénin et Togo."
    },
    {
        "question": "Quelle est la plus ancienne organisation intergouvernementale africaine encore en activité ?",
        "options": ["A) CEDEAO", "B) Conseil de l'Entente", "C) Union du Fleuve Mano", "D) OUA"],
        "answer": "B",
        "explanation": "Le Conseil de l'Entente, fondé en 1959, est la doyenne des organisations sous-régionales ouest-africaines."
    },
    {
        "question": "L'Union du Fleuve Mano regroupe :",
        "options": ["A) Sénégal, Mauritanie, Mali", "B) Guinée, Sierra Leone, Liberia, Côte d'Ivoire", "C) Côte d'Ivoire, Ghana, Togo, Bénin", "D) Niger, Nigeria, Tchad, Cameroun"],
        "answer": "B",
        "explanation": "L'Union du fleuve Mano comprend le Liberia, la Sierra Leone, la Guinée et la Côte d'Ivoire."
    },
    {
        "question": "Où se trouve le siège de l'Organisation Mondiale de la Santé (OMS) ?",
        "options": ["A) New York", "B) Genève", "C) Rome", "D) Vienne"],
        "answer": "B",
        "explanation": "Le siège de l'OMS est à Genève, en Suisse."
    },
    {
        "question": "La FAO (Organisation des Nations Unies pour l'alimentation et l'agriculture) a son siège à :",
        "options": ["A) Paris", "B) New York", "C) Rome", "D) Londres"],
        "answer": "C",
        "explanation": "Le siège de la FAO se trouve à Rome, en Italie."
    },
    {
        "question": "Lequel de ces présidents ivoiriens a été Secrétaire exécutif du Conseil de l'Entente ?",
        "options": ["A) Félix Houphouët-Boigny", "B) Henri Konan Bédié", "C) Laurent Gbagbo", "D) Alassane Ouattara"],
        "answer": "D",
        "explanation": "Piège, c'est Félix Houphouët-Boigny qui a été le fondateur et l'initiateur principal. Aucun n'a été Secrétaire exécutif, car c'est un poste administratif."
    },
    {
        "question": "Quel a été le premier Ivoirien élu à l'Académie française ?",
        "options": ["A) Bernard Dadié", "B) Ahmadou Kourouma", "C) aucun Ivoirien n'a été élu", "D) Maurice Bandaman"],
        "answer": "C",
        "explanation": "Léopold Sédar Senghor (Sénégal) y fut élu, mais aucun Ivoirien n'est membre de l'Académie française."
    },
    {
        "question": "L'Organisation pour l'Harmonisation en Afrique du Droit des Affaires (OHADA) a été créée par le traité de :",
        "options": ["A) Dakar", "B) Abidjan", "C) Port-Louis", "D) Libreville"],
        "answer": "C",
        "explanation": "Le traité créant l'OHADA a été signé à Port-Louis (Île Maurice) en 1993."
    },
    {
        "question": "Où se trouve la Cour commune de justice et d'arbitrage de l'OHADA ?",
        "options": ["A) Yaoundé", "B) Dakar", "C) Abidjan", "D) Cotonou"],
        "answer": "C",
        "explanation": "La CCJA a son siège à Abidjan, Côte d'Ivoire."
    },
    {
        "question": "L'ECOWAS correspond en français à :",
        "options": ["A) La CEDEAO", "B) L'UEMOA", "C) L'Union Africaine", "D) La BAD"],
        "answer": "A",
        "explanation": "Economic Community of West African States (ECOWAS) est la CEDEAO."
    },
    {
        "question": "Qui est le Secrétaire général de l'ONU en 2026/2027 ?",
        "options": ["A) Ban Ki-moon", "B) Kofi Annan", "C) António Guterres", "D) Boutros Boutros-Ghali"],
        "answer": "C",
        "explanation": "António Guterres est le Secrétaire général de l'ONU."
    },
    {
        "question": "Quelle est l'institution spécialisée de l'ONU chargée de la réglementation de l'aviation civile internationale ?",
        "options": ["A) OMI", "B) OACI", "C) IATA", "D) OMT"],
        "answer": "B",
        "explanation": "L'Organisation de l'Aviation Civile Internationale (OACI)."
    },
    {
        "question": "Le FMI (Fonds Monétaire International) a été créé lors de la conférence de :",
        "options": ["A) Yalta", "B) Bretton Woods", "C) San Francisco", "D) Paris"],
        "answer": "B",
        "explanation": "Le FMI et la Banque Mondiale sont nés à la Conférence de Bretton Woods en 1944."
    },
    {
        "question": "Lequel de ces droits n'est pas reconnu par la Déclaration Universelle des Droits de l'Homme ?",
        "options": ["A) Le droit au travail", "B) Le droit à l'éducation", "C) Le droit de polluer", "D) Le droit d'asile"],
        "answer": "C",
        "explanation": "Le droit de polluer n'existe pas dans la DUDH."
    },
    {
        "question": "Le G5 Sahel comprenait à l'origine :",
        "options": ["A) Mali, Burkina Faso, Niger, Tchad, Mauritanie", "B) Sénégal, Mali, Mauritanie, Niger, Tchad", "C) Burkina Faso, Mali, Niger, Nigeria, Cameroun", "D) Mali, Niger, Burkina Faso, Côte d'Ivoire, Tchad"],
        "answer": "A",
        "explanation": "Le G5 Sahel a été fondé par le Mali, le Burkina Faso, le Niger, le Tchad et la Mauritanie."
    },
    {
        "question": "Quelle est l'organisation mondiale chargée de la protection des droits de propriété intellectuelle ?",
        "options": ["A) OMC", "B) OMPI", "C) OIT", "D) OIF"],
        "answer": "B",
        "explanation": "L'Organisation Mondiale de la Propriété Intellectuelle (OMPI)."
    },
    {
        "question": "Quel est l'organe judiciaire principal des Nations Unies ?",
        "options": ["A) La Cour Pénale Internationale (CPI)", "B) La Cour Internationale de Justice (CIJ)", "C) Le Tribunal de Nuremberg", "D) La Cour Européenne des Droits de l'Homme"],
        "answer": "B",
        "explanation": "La CIJ est l'organe judiciaire principal de l'ONU, siégeant à La Haye."
    },
    {
        "question": "Quel Ivoirien dirige le groupe de la Banque Africaine de Développement (BAD) ?",
        "options": ["A) Tidjane Thiam", "B) Jean-Louis Billon", "C) Akinwumi Adesina", "D) Thierry Tanoh"],
        "answer": "C",
        "explanation": "Piège, Akinwumi Adesina est Nigérian. Il n'y a pas d'Ivoirien à la tête de la BAD actuellement."
    },
    {
        "question": "Combien de pays africains sont membres fondateurs de l'ONU en 1945 ?",
        "options": ["A) 2", "B) 4", "C) 10", "D) 15"],
        "answer": "B",
        "explanation": "L'Égypte, l'Éthiopie, le Libéria et l'Afrique du Sud étaient les 4 membres fondateurs africains de l'ONU."
    },
    {
        "question": "Quel est le nom de la monnaie unique envisagée par la CEDEAO ?",
        "options": ["A) Le Cauri", "B) L'Afro", "C) L'Eco", "D) Le Cedi"],
        "answer": "C",
        "explanation": "L'Eco est le nom choisi pour la monnaie unique de la CEDEAO."
    },
    {
        "question": "What year did the revised ECOWAS treaty, which created the ECOWAS Parliament and Court of Justice, get signed in Cotonou?",
        "options": ["A) 1975", "B) 1981", "C) 1993", "D) 1999"],
        "answer": "C",
        "explanation": "The revised treaty was signed on July 24, 1993."
    },
    {
        "question": "Which specific protocol or treaty established the ECOWAS specialized agency WAHO (West African Health Organization) in 1987, merging OCCGE and WAHC?",
        "options": ["A) Protocol A/P1/7/87", "B) Protocol A/P2/7/87", "C) Treaty of Lagos", "D) Revised Treaty of Cotonou"],
        "answer": "B",
        "explanation": "WAHO was created by Protocol A/P2/7/87 signed in Abuja in 1987."
    },
    {
        "question": "Where is the headquarters of the African Union Development Agency (AUDA-NEPAD) located?",
        "options": ["A) Addis Ababa", "B) Johannesburg", "C) Midrand", "D) Abuja"],
        "answer": "C",
        "explanation": "AUDA-NEPAD is headquartered in Midrand, South Africa."
    },
    {
        "question": "Which UN specialized agency is responsible for intellectual property services and is headquartered in Geneva?",
        "options": ["A) ITU", "B) WIPO (OMPI)", "C) UPU", "D) WMO (OMM)"],
        "answer": "B",
        "explanation": "The World Intellectual Property Organization (WIPO/OMPI) is based in Geneva."
    },
    {
        "question": "The African Development Bank (AfDB) approved the Abidjan Urban Transport Project (PTUA). In which year did the AfDB relocate its headquarters temporarily to Tunis before returning to Abidjan?",
        "options": ["A) 1999", "B) 2003", "C) 2011", "D) 2014"],
        "answer": "B",
        "explanation": "The AfDB temporarily relocated to Tunis in 2003 due to the Ivorian Civil War, returning in 2014."
    },
    {
        "question": "Which AU organ is the highest decision-making organ, replacing the OAU Assembly of Heads of State and Government?",
        "options": ["A) The Executive Council", "B) The Pan-African Parliament", "C) The Assembly of the Union", "D) The Peace and Security Council"],
        "answer": "C",
        "explanation": "The Assembly of the Union is the supreme organ of the AU."
    },
    {
        "question": "What is the primary function of the Inter-Governmental Action Group against Money Laundering in West Africa (GIABA)?",
        "options": ["A) Public Health", "B) Peacekeeping", "C) Anti-Money Laundering", "D) Telecommunications"],
        "answer": "C",
        "explanation": "GIABA is an ECOWAS institution responsible for strengthening the capacity of member states towards the prevention and control of money laundering."
    },
    {
        "question": "The World Meteorological Organization (OMM) originated from which former organization created in 1873?",
        "options": ["A) International Meteorological Organization", "B) World Weather Watch", "C) Global Atmospheric Research Program", "D) League of Nations Meteorology Bureau"],
        "answer": "A",
        "explanation": "WMO originated from the International Meteorological Organization (IMO)."
    },
    {
        "question": "Under the ECOWAS Protocol relating to Free Movement of Persons, Residence and Establishment, what is the maximum duration a citizen can stay in a member state without a visa?",
        "options": ["A) 30 days", "B) 60 days", "C) 90 days", "D) 120 days"],
        "answer": "C",
        "explanation": "The Protocol grants community citizens the right to enter and reside in any member state without a visa for up to 90 days."
    },
    {
        "question": "Which UN body has the primary responsibility for the maintenance of international peace and security?",
        "options": ["A) General Assembly", "B) Security Council", "C) Economic and Social Council", "D) International Court of Justice"],
        "answer": "B",
        "explanation": "The UN Security Council holds this primary responsibility."
    },
    {
        "question": "In which city is the headquarters of the ECOWAS Bank for Investment and Development (EBID) located?",
        "options": ["A) Abuja", "B) Lome", "C) Abidjan", "D) Dakar"],
        "answer": "B",
        "explanation": "EBID is headquartered in Lome, Togo."
    },
    {
        "question": "Which African Union treaty established the African Continental Free Trade Area (AfCFTA)?",
        "options": ["A) Abuja Treaty", "B) Maputo Protocol", "C) Kigali Declaration", "D) Lagos Plan of Action"],
        "answer": "C",
        "explanation": "The AfCFTA agreement was brokered by the African Union and signed in Kigali on 21 March 2018."
    },
    {
        "question": "Which of the following is NOT an official language of the United Nations?",
        "options": ["A) Arabic", "B) Spanish", "C) Portuguese", "D) Russian"],
        "answer": "C",
        "explanation": "The six official languages of the UN are Arabic, Chinese, English, French, Russian, and Spanish."
    },
    {
        "question": "Who was the first Secretary-General of the United Nations?",
        "options": ["A) Trygve Lie", "B) Dag Hammarskjold", "C) U Thant", "D) Boutros Boutros-Ghali"],
        "answer": "A",
        "explanation": "Trygve Lie of Norway was the first Secretary-General, serving from 1946 to 1952."
    },
    {
        "question": "The African Peer Review Mechanism (APRM) is a mutually agreed instrument voluntarily acceded to by the Member States of the African Union. When was it established?",
        "options": ["A) 1999", "B) 2003", "C) 2007", "D) 2010"],
        "answer": "B",
        "explanation": "The APRM was established in 2003 by the NEPAD Heads of State and Government Implementation Committee."
    },
    {
        "question": "How many member states currently constitute the Economic Community of West African States (ECOWAS) following the recent withdrawals?",
        "options": ["A) 12", "B) 13", "C) 14", "D) 15"],
        "answer": "A",
        "explanation": "With the withdrawal of Mali, Burkina Faso, and Niger, ECOWAS currently has 12 members (as of 2024)."
    },
    {
        "question": "What is the acronym for the specialized agency of the UN responsible for information and communication technologies?",
        "options": ["A) ITU", "B) UPU", "C) ICAO", "D) IMO"],
        "answer": "A",
        "explanation": "The International Telecommunication Union (ITU) is the UN specialized agency for ICTs."
    },
    {
        "question": "Where is the Secretariat of the African Continental Free Trade Area (AfCFTA) located?",
        "options": ["A) Addis Ababa, Ethiopia", "B) Accra, Ghana", "C) Cairo, Egypt", "D) Pretoria, South Africa"],
        "answer": "B",
        "explanation": "The AfCFTA Secretariat is located in Accra, Ghana."
    },
    {
        "question": "Which protocol to the African Charter on Human and Peoples' Rights deals specifically with the Rights of Women in Africa?",
        "options": ["A) Maputo Protocol", "B) Malabo Protocol", "C) Arusha Protocol", "D) Dakar Protocol"],
        "answer": "A",
        "explanation": "The Maputo Protocol guarantees comprehensive rights to women in Africa."
    },
    {
        "question": "The ECOWAS military force, ECOMOG, was first deployed in 1990 to intervene in the civil war of which member state?",
        "options": ["A) Sierra Leone", "B) Guinea-Bissau", "C) Liberia", "D) Côte d'Ivoire"],
        "answer": "C",
        "explanation": "ECOMOG was first deployed to Liberia in August 1990."
    },
    {
        "question": "Which UN organ consists of 54 members elected by the General Assembly for three-year terms?",
        "options": ["A) Trusteeship Council", "B) Security Council", "C) Economic and Social Council (ECOSOC)", "D) International Court of Justice"],
        "answer": "C",
        "explanation": "ECOSOC consists of 54 members elected for three-year terms."
    },
    {
        "question": "The African Development Bank (AfDB) Group comprises three distinct entities. Which of the following is NOT one of them?",
        "options": ["A) African Development Bank", "B) African Development Fund", "C) Nigeria Trust Fund", "D) African Finance Corporation"],
        "answer": "D",
        "explanation": "The AfDB Group consists of the AfDB, the ADF, and the NTF. The AFC is a separate entity."
    },
    {
        "question": "What is the primary mandate of the West African Health Organization (WAHO)?",
        "options": ["A) Military defense", "B) Economic integration", "C) Health protection and improvement", "D) Educational standardization"],
        "answer": "C",
        "explanation": "WAHO's objective is the attainment of the highest possible standard and protection of health of the peoples in the sub-region."
    },
    {
        "question": "The Universal Postal Union (UPU), a specialized agency of the UN, is headquartered in which city?",
        "options": ["A) Geneva", "B) Bern", "C) Paris", "D) Vienna"],
        "answer": "B",
        "explanation": "The UPU headquarters is located in Bern, Switzerland."
    },
    {
        "question": "Which AU organ is responsible for the peaceful resolution of conflicts in Africa, established by a protocol adopted in 2002?",
        "options": ["A) Peace and Security Council (PSC)", "B) African Court of Justice", "C) Pan-African Parliament", "D) Economic, Social and Cultural Council (ECOSOCC)"],
        "answer": "A",
        "explanation": "The Peace and Security Council is the standing decision-making organ of the AU for the prevention, management and resolution of conflicts."
    },
    {
        "question": "The ECOWAS Court of Justice is based in which city?",
        "options": ["A) Lome", "B) Accra", "C) Abuja", "D) Dakar"],
        "answer": "C",
        "explanation": "The ECOWAS Court of Justice is headquartered in Abuja, Nigeria."
    },
    {
        "question": "Which organization preceded the African Union?",
        "options": ["A) Organization of African States", "B) Organization of African Unity", "C) African Economic Community", "D) Pan-African Congress"],
        "answer": "B",
        "explanation": "The Organization of African Unity (OAU) preceded the African Union (AU)."
    },
    {
        "question": "The World Intellectual Property Organization (WIPO) administers several treaties. Which treaty specifically deals with the protection of literary and artistic works?",
        "options": ["A) Paris Convention", "B) Berne Convention", "C) Madrid Agreement", "D) Patent Cooperation Treaty"],
        "answer": "B",
        "explanation": "The Berne Convention, adopted in 1886, deals with the protection of works and the rights of their authors."
    },
    {
        "question": "What is the primary currency unit used for accounting by the African Development Bank?",
        "options": ["A) US Dollar", "B) Euro", "C) Unit of Account (UA)", "D) CFA Franc"],
        "answer": "C",
        "explanation": "The AfDB uses the Unit of Account (UA), which is equivalent to the Special Drawing Right (SDR) of the IMF."
    },
    {
        "question": "Which specialized agency of the UN focuses on the promotion of social justice and internationally recognized human and labour rights?",
        "options": ["A) WHO", "B) ILO", "C) UNESCO", "D) FAO"],
        "answer": "B",
        "explanation": "The International Labour Organization (ILO) focuses on labour rights and social justice."
    },
    {
        "question": "The Lome Peace Agreement of 1999 was brokered by ECOWAS to end the civil war in which country?",
        "options": ["A) Liberia", "B) Sierra Leone", "C) Guinea-Bissau", "D) Côte d'Ivoire"],
        "answer": "B",
        "explanation": "The Lome Peace Agreement was signed in 1999 to end the Sierra Leone Civil War."
    },
    {
        "question": "The African Union's Agenda 2063 is a strategic framework for the socio-economic transformation of the continent over a 50-year period. When was it adopted?",
        "options": ["A) 2013", "B) 2015", "C) 2000", "D) 2020"],
        "answer": "B",
        "explanation": "Agenda 2063 was adopted by the AU Assembly in January 2015."
    },
    {
        "question": "Which UN agency is tasked with providing humanitarian and developmental aid to children worldwide?",
        "options": ["A) UNESCO", "B) UNICEF", "C) UNHCR", "D) WFP"],
        "answer": "B",
        "explanation": "The United Nations Children's Fund (UNICEF) focuses on aid to children."
    },
    {
        "question": "The ECOWAS Commission replaced the ECOWAS Secretariat. In what year did this transformation take place?",
        "options": ["A) 1993", "B) 2000", "C) 2007", "D) 2010"],
        "answer": "C",
        "explanation": "The Secretariat was transformed into the Commission in 2007 to enhance the organization's supranational powers."
    },
    {
        "question": "Where is the International Court of Justice (ICJ), the principal judicial organ of the UN, located?",
        "options": ["A) Geneva", "B) New York", "C) The Hague", "D) Vienna"],
        "answer": "C",
        "explanation": "The ICJ is located at the Peace Palace in The Hague, Netherlands."
    },
    {
        "question": "The Constitutive Act of the African Union was adopted in which city?",
        "options": ["A) Sirte", "B) Lome", "C) Addis Ababa", "D) Lusaka"],
        "answer": "B",
        "explanation": "The Constitutive Act was adopted in Lome, Togo, on July 11, 2000."
    },
    {
        "question": "Which institution is the supreme audit institution of ECOWAS?",
        "options": ["A) ECOWAS Parliament", "B) ECOWAS Court of Justice", "C) ECOWAS Commission", "D) Office of the Auditor General of ECOWAS"],
        "answer": "D",
        "explanation": "The Office of the Auditor General ensures transparency and accountability in the management of ECOWAS resources."
    },
    {
        "question": "The World Meteorological Organization (WMO) operates the World Weather Watch. What year was this program launched?",
        "options": ["A) 1950", "B) 1963", "C) 1975", "D) 1980"],
        "answer": "B",
        "explanation": "The World Weather Watch was established in 1963 to combine observing systems, telecommunication facilities, and data-processing."
    },
    {
        "question": "Who represents Côte d'Ivoire on the Board of Governors of the African Development Bank?",
        "options": ["A) The President of the Republic", "B) The Minister of Economy and Finance", "C) The Governor of the BCEAO", "D) The Minister of Foreign Affairs"],
        "answer": "B",
        "explanation": "Each member country is represented on the AfDB Board of Governors by its Minister of Finance or a similar high-ranking official."
    },
    {
        "question": "The ECOWAS single currency project adopted a name for its proposed currency. What is this name?",
        "options": ["A) Afro", "B) Cedi", "C) Eco", "D) West African Franc"],
        "answer": "C",
        "explanation": "The proposed single currency for the ECOWAS region is named the Eco."
    },
    {
        "question": "Which organ of the African Union is intended to provide civil society organizations with a platform to be involved in the AU's programs?",
        "options": ["A) The Executive Council", "B) The Pan-African Parliament", "C) The Economic, Social and Cultural Council (ECOSOCC)", "D) The Permanent Representatives Committee"],
        "answer": "C",
        "explanation": "ECOSOCC is an advisory organ composed of different social and professional groups of the member states."
    },
    {
        "question": "The Food and Agriculture Organization (FAO) of the UN is headquartered in which city?",
        "options": ["A) Geneva", "B) Rome", "C) Paris", "D) New York"],
        "answer": "B",
        "explanation": "The FAO is headquartered in Rome, Italy."
    },
    {
        "question": "Which agreement established the World Intellectual Property Organization (WIPO)?",
        "options": ["A) Paris Convention", "B) Berne Convention", "C) WIPO Convention", "D) TRIPS Agreement"],
        "answer": "C",
        "explanation": "The WIPO Convention, signed in Stockholm in 1967, established WIPO."
    },
    {
        "question": "The African Development Fund (ADF) provides concessional funding. Which countries are eligible for ADF funding?",
        "options": ["A) All African countries", "B) Only low-income African countries", "C) Only middle-income African countries", "D) Only North African countries"],
        "answer": "B",
        "explanation": "The ADF provides concessional resources to low-income regional member countries."
    },
    {
        "question": "The ECOWAS Parliament consists of how many seats?",
        "options": ["A) 115", "B) 120", "C) 150", "D) 200"],
        "answer": "A",
        "explanation": "The ECOWAS Parliament, also known as the Community Parliament, has 115 seats."
    },
    {
        "question": "Which UN agency focuses on the regulation of international civil aviation?",
        "options": ["A) IMO", "B) ICAO", "C) ITU", "D) WMO"],
        "answer": "B",
        "explanation": "The International Civil Aviation Organization (ICAO) manages the administration and governance of the Convention on International Civil Aviation."
    },
    {
        "question": "The African Continental Free Trade Area (AfCFTA) requires member states to remove tariffs from what percentage of goods?",
        "options": ["A) 50%", "B) 70%", "C) 90%", "D) 100%"],
        "answer": "C",
        "explanation": "Members are committed to eliminate tariffs on 90% of goods."
    },
    {
        "question": "Which specialized agency of the UN is responsible for promoting responsible, sustainable and universally accessible tourism?",
        "options": ["A) UNWTO", "B) UNESCO", "C) UNDP", "D) UNEP"],
        "answer": "A",
        "explanation": "The World Tourism Organization (UNWTO) is the UN agency for tourism."
    },
    {
        "question": "The headquarters of the West African Health Organization (WAHO) is located in which city?",
        "options": ["A) Abuja", "B) Bobo-Dioulasso", "C) Dakar", "D) Abidjan"],
        "answer": "B",
        "explanation": "WAHO is headquartered in Bobo-Dioulasso, Burkina Faso."
    },
    {
        "question": "The United Nations Charter was signed in which year?",
        "options": ["A) 1944", "B) 1945", "C) 1946", "D) 1948"],
        "answer": "B",
        "explanation": "The UN Charter was signed on 26 June 1945 in San Francisco."
    },
    {
        "question": "A quelle date le retrait du Mali, du Burkina Faso et du Niger de la CEDEAO est-il devenu effectif ?",
        "options": ["A) 28 janvier 2024", "B) 29 janvier 2025", "C) 15 mars 2024", "D) 1er janvier 2025"],
        "answer": "B",
        "explanation": "Le retrait est effectif un an après l'annonce (28 janvier 2024)."
    },
    {
        "question": "Comment s'appelle l'organisation créée par le Mali, le Burkina Faso et le Niger suite à leur retrait de la CEDEAO ?",
        "options": ["A) G5 Sahel", "B) Alliance des États du Sahel (AES)", "C) Union du Fleuve Mano", "D) Liptako-Gourma unifié"],
        "answer": "B",
        "explanation": "L'AES a été formée puis transformée en confédération en 2024."
    },
    {
        "question": "Quel est le siège de la Commission de la CEDEAO ?",
        "options": ["A) Lomé", "B) Dakar", "C) Abuja", "D) Accra"],
        "answer": "C",
        "explanation": "Le siège de la CEDEAO est à Abuja au Nigeria."
    },
    {
        "question": "Malgré leur retrait de la CEDEAO, le Mali, le Burkina Faso et le Niger sont-ils restés membres de l'UEMOA en 2025 ?",
        "options": ["A) Non, ils ont créé leur propre monnaie", "B) Oui, ils ont maintenu leur adhésion à l'UEMOA", "C) Seulement le Mali est resté", "D) Ils ont été suspendus définitivement"],
        "answer": "B",
        "explanation": "Ils n'ont pas quitté l'UEMOA ni la zone Franc CFA en 2025."
    },
    {
        "question": "Où se trouve le siège de la Commission de l'UEMOA ?",
        "options": ["A) Ouagadougou", "B) Dakar", "C) Abidjan", "D) Bamako"],
        "answer": "A",
        "explanation": "Le siège de l'UEMOA est à Ouagadougou."
    },
    {
        "question": "Où se trouve le siège de la BCEAO ?",
        "options": ["A) Ouagadougou", "B) Dakar", "C) Abidjan", "D) Lomé"],
        "answer": "B",
        "explanation": "Le siège de la Banque Centrale des États de l'Afrique de l'Ouest est à Dakar."
    },
    {
        "question": "Où se trouve le siège de l'Union Africaine (UA) ?",
        "options": ["A) Johannesburg", "B) Addis-Abeba", "C) Nairobi", "D) Le Caire"],
        "answer": "B",
        "explanation": "Le siège de l'UA est en Éthiopie."
    },
    {
        "question": "Comment s'appelle la feuille de route stratégique de l'Union Africaine pour le développement du continent ?",
        "options": ["A) Vision 2030", "B) Agenda 2063", "C) Plan NEPAD 2050", "D) Initiative Afrique 21"],
        "answer": "B",
        "explanation": "C'est l'Agenda 2063 : L'Afrique que nous voulons."
    },
    {
        "question": "L'Union Africaine a succédé à quelle organisation en 2002 ?",
        "options": ["A) L'Organisation de l'Unité Africaine (OUA)", "B) La Communauté Économique Africaine", "C) Le NEPAD", "D) L'Union Panafricaine"],
        "answer": "A",
        "explanation": "L'OUA a été remplacée par l'UA en 2002."
    },
    {
        "question": "Combien de membres permanents le Conseil de Sécurité de l'ONU compte-il ?",
        "options": ["A) 5", "B) 10", "C) 15", "D) 193"],
        "answer": "A",
        "explanation": "Il y a 5 membres permanents avec droit de véto."
    },
    {
        "question": "Parmi ces pays, lequel N'EST PAS un membre permanent du Conseil de Sécurité de l'ONU ?",
        "options": ["A) France", "B) Royaume-Uni", "C) Allemagne", "D) Russie"],
        "answer": "C",
        "explanation": "Les 5 sont: USA, Russie, Chine, France, Royaume-Uni."
    },
    {
        "question": "Qui est le Secrétaire Général de l'ONU en 2025 ?",
        "options": ["A) Ban Ki-moon", "B) Kofi Annan", "C) António Guterres", "D) Boutros Boutros-Ghali"],
        "answer": "C",
        "explanation": "António Guterres est en poste depuis 2017."
    },
    {
        "question": "Où se trouve le siège de l'OMS ?",
        "options": ["A) Genève", "B) Vienne", "C) Washington", "D) Paris"],
        "answer": "A",
        "explanation": "L'Organisation Mondiale de la Santé siège à Genève."
    },
    {
        "question": "Quelle agence spécialisée de l'ONU a son siège à Paris ?",
        "options": ["A) L'UNICEF", "B) L'UNESCO", "C) Le HCR", "D) L'OIT"],
        "answer": "B",
        "explanation": "L'Organisation pour l'éducation, la science et la culture est à Paris."
    },
    {
        "question": "Où siège la Banque Africaine de Développement (BAD) ?",
        "options": ["A) Tunis", "B) Dakar", "C) Abidjan", "D) Pretoria"],
        "answer": "C",
        "explanation": "Le siège statutaire de la BAD est à Abidjan, Côte d'Ivoire."
    },
    {
        "question": "Qui est le Président de la Banque Africaine de Développement dont le second mandat se termine en 2025 ?",
        "options": ["A) Donald Kaberuka", "B) Akinwumi Adesina", "C) Tidjane Thiam", "D) Ngozi Okonjo-Iweala"],
        "answer": "B",
        "explanation": "Le Nigérian Akinwumi Adesina a été réélu en 2020 pour 5 ans."
    },
    {
        "question": "En quelle année le second mandat d'António Guterres à la tête de l'ONU se termine-t-il ?",
        "options": ["A) 2025", "B) 2026", "C) 2027", "D) 2030"],
        "answer": "B",
        "explanation": "Son second mandat s'achève le 31 décembre 2026."
    },
    {
        "question": "Quel traité a institué la CEDEAO en 1975 ?",
        "options": ["A) Traité de Lagos", "B) Traité d'Abuja", "C) Traité de Dakar", "D) Traité de Niamey"],
        "answer": "A",
        "explanation": "La CEDEAO a été créée par le Traité de Lagos le 28 mai 1975."
    },
    {
        "question": "Quelle est l'agence de l'ONU basée à Montréal ?",
        "options": ["A) OMI", "B) OACI", "C) OMPI", "D) UPU"],
        "answer": "B",
        "explanation": "L'Organisation de l'aviation civile internationale siège à Montréal."
    },
    {
        "question": "Où se trouve le siège de l'Organisation Maritime Internationale (OMI) ?",
        "options": ["A) Hambourg", "B) Londres", "C) Athènes", "D) Genève"],
        "answer": "B",
        "explanation": "L'OMI a son siège à Londres."
    },
    {
        "question": "Quel accord lie les pays d'Afrique, des Caraïbes et du Pacifique (ACP) à l'Union Européenne depuis 2023, remplaçant l'accord de Cotonou ?",
        "options": ["A) L'Accord de Lomé", "B) L'Accord des Samoa", "C) L'Accord de Bruxelles", "D) L'Accord de Dakar"],
        "answer": "B",
        "explanation": "L'Accord de Samoa a remplacé l'Accord de Cotonou."
    },
    {
        "question": "Quel impact majeur le Brexit a-t-il eu sur le rôle du Royaume-Uni dans le Commonwealth ?",
        "options": ["A) Le Royaume-Uni a quitté le Commonwealth", "B) Le Royaume-Uni a recentré ses accords commerciaux sur les pays du Commonwealth", "C) Le Commonwealth a été dissous", "D) Les pays du Commonwealth ont imposé des visas aux Britanniques"],
        "answer": "B",
        "explanation": "Après le Brexit, le RU a cherché à renforcer ses liens avec le Commonwealth (Global Britain)."
    },
    {
        "question": "L'Organisation Mondiale de la Propriété Intellectuelle (OMPI) est basée à :",
        "options": ["A) Paris", "B) New York", "C) Genève", "D) Vienne"],
        "answer": "C",
        "explanation": "L'OMPI est une institution spécialisée des Nations Unies basée à Genève."
    },
    {
        "question": "Quelle cour de justice est l'organe judiciaire principal de l'ONU ?",
        "options": ["A) La Cour Pénale Internationale (CPI)", "B) La Cour Internationale de Justice (CIJ)", "C) Le Tribunal de La Haye", "D) La Cour Européenne des Droits de l'Homme"],
        "answer": "B",
        "explanation": "La CIJ est l'organe judiciaire de l'ONU. La CPI est indépendante."
    },
    {
        "question": "La CPI (Cour Pénale Internationale) fait-elle partie du système de l'ONU ?",
        "options": ["A) Oui, c'est une agence spécialisée", "B) Non, c'est une organisation internationale indépendante", "C) Oui, elle remplace la CIJ", "D) Non, elle dépend de l'Union Européenne"],
        "answer": "B",
        "explanation": "Bien qu'elle coopère avec l'ONU, la CPI a été créée par le Statut de Rome et est indépendante."
    },
    {
        "question": "Quel statut l'État de Palestine a-t-il obtenu à l'ONU en 2012, réaffirmé dans les récents débats de 2024-2025 ?",
        "options": ["A) Membre à part entière", "B) État observateur non membre", "C) Membre du Conseil de Sécurité", "D) Territoire sous tutelle"],
        "answer": "B",
        "explanation": "La Palestine est un État observateur non membre à l'Assemblée générale."
    },
    {
        "question": "Parmi ces organisations, laquelle n'est pas une institution spécialisée de l'ONU ?",
        "options": ["A) Le FMI", "B) Le Groupe de la Banque Mondiale", "C) L'OMC", "D) L'OIT"],
        "answer": "C",
        "explanation": "L'Organisation Mondiale du Commerce n'est pas une agence spécialisée de l'ONU, bien qu'elles coopèrent."
    },
    {
        "question": "Dans le cadre des réformes débattues en 2025, quel continent revendique au moins deux sièges permanents avec droit de veto au Conseil de sécurité de l'ONU (Consensus d'Ezulwini) ?",
        "options": ["A) L'Amérique du Sud", "B) L'Afrique", "C) L'Asie", "D) L'Océanie"],
        "answer": "B",
        "explanation": "Le Consensus d'Ezulwini est la position commune africaine revendiquant des sièges permanents."
    },
    {
        "question": "Quel traité fonde l'Union Européenne telle qu'on la connaît aujourd'hui, entré en vigueur en 1993 ?",
        "options": ["A) Traité de Rome", "B) Traité de Maastricht", "C) Traité de Lisbonne", "D) Traité d'Amsterdam"],
        "answer": "B",
        "explanation": "Le Traité de Maastricht a institué l'Union Européenne."
    },
    {
        "question": "Le G20 est composé de 19 pays et de deux unions d'États. Lesquelles ?",
        "options": ["A) L'UE et l'ALENA", "B) L'UE et l'Union Africaine", "C) L'ASEAN et l'UE", "D) Le Mercosur et l'Union Africaine"],
        "answer": "B",
        "explanation": "L'Union Africaine a été admise comme membre permanent du G20 en 2023."
    },
    {
        "question": "Quelle est l'institution de l'UEMOA chargée de contrôler les comptes de l'Union ?",
        "options": ["A) La Commission de l'UEMOA", "B) La Cour de Justice", "C) La Cour des Comptes", "D) Le Parlement de l'UEMOA"],
        "answer": "C",
        "explanation": "La Cour des Comptes de l'UEMOA contrôle les finances de l'Union."
    },
    {
        "question": "Qui a été élu Secrétaire Général de l'Organisation Internationale de la Francophonie (OIF) en 2018, puis réélue ?",
        "options": ["A) Michaëlle Jean", "B) Louise Mushikiwabo", "C) Abdou Diouf", "D) Boutros Boutros-Ghali"],
        "answer": "B",
        "explanation": "La Rwandaise Louise Mushikiwabo dirige l'OIF."
    },
    {
        "question": "Où est le siège de l'OIF ?",
        "options": ["A) Paris", "B) Genève", "C) Bruxelles", "D) Dakar"],
        "answer": "A",
        "explanation": "L'OIF siège à Paris."
    },
    {
        "question": "En 2024, quel nouveau pays a officiellement rejoint les BRICS, aux côtés de l'Égypte, de l'Éthiopie, de l'Iran et des EAU ?",
        "options": ["A) L'Argentine", "B) L'Arabie Saoudite", "C) Le Nigeria", "D) Le Mexique"],
        "answer": "B",
        "explanation": "L'Arabie Saoudite a été invitée et a rejoint les BRICS (bien que l'Argentine ait décliné sous Milei)."
    },
    {
        "question": "Combien de pays forment l'Alliance des États du Sahel (AES) ?",
        "options": ["A) 2", "B) 3", "C) 4", "D) 5"],
        "answer": "B",
        "explanation": "Le Mali, le Burkina Faso et le Niger."
    },
    {
        "question": "L'Agence Internationale de l'Énergie Atomique (AIEA) est basée à :",
        "options": ["A) Genève", "B) Vienne", "C) New York", "D) Londres"],
        "answer": "B",
        "explanation": "L'AIEA siège en Autriche à Vienne."
    },
    {
        "question": "Le Programme des Nations Unies pour le Développement (PNUD) est dirigé par un :",
        "options": ["A) Directeur Général", "B) Administrateur", "C) Secrétaire Général", "D) Président"],
        "answer": "B",
        "explanation": "Le chef du PNUD porte le titre d'Administrateur."
    },
    {
        "question": "Le siège de la Cour Pénale Internationale (CPI) est à :",
        "options": ["A) La Haye", "B) Genève", "C) New York", "D) Rome"],
        "answer": "A",
        "explanation": "La CPI, bien qu'issue du Statut de Rome, siège à La Haye aux Pays-Bas."
    },
    {
        "question": "Le siège d'INTERPOL se trouve en France. Dans quelle ville ?",
        "options": ["A) Paris", "B) Lyon", "C) Marseille", "D) Strasbourg"],
        "answer": "B",
        "explanation": "Interpol est basé à Lyon."
    },
    {
        "question": "L'ALENA (NAFTA), l'accord de libre-échange nord-américain, a été remplacé par :",
        "options": ["A) L'USMCA (AEUMC)", "B) Le MERCOSUR", "C) L'AELC", "D) Le Partenariat Transpacifique"],
        "answer": "A",
        "explanation": "L'Accord États-Unis-Mexique-Canada a remplacé l'ALENA en 2020."
    },
    {
        "question": "Où se trouve le siège du Parlement Européen (les sessions plénières) ?",
        "options": ["A) Bruxelles", "B) Strasbourg", "C) Luxembourg", "D) Francfort"],
        "answer": "B",
        "explanation": "Le siège officiel pour les sessions plénières est à Strasbourg."
    },
    {
        "question": "Quelle est l'institution de l'ONU qui réunit tous les États membres (193 en 2025) ?",
        "options": ["A) Le Conseil de Sécurité", "B) L'Assemblée Générale", "C) L'ECOSOC", "D) Le Secrétariat"],
        "answer": "B",
        "explanation": "L'AG regroupe tous les États membres avec une voix chacun."
    },
    {
        "question": "Quel est l'objectif principal de la ZLECAf ?",
        "options": ["A) Créer une monnaie unique africaine", "B) Créer une Zone de Libre-Échange Continentale Africaine", "C) Lutter contre le terrorisme au Sahel", "D) Unifier les armées africaines"],
        "answer": "B",
        "explanation": "La ZLECAf vise à créer un marché unique pour les biens et services en Afrique."
    },
    {
        "question": "L'Organisation de la Coopération Islamique (OCI) siège à :",
        "options": ["A) Riyad", "B) Djeddah", "C) Doha", "D) Istanbul"],
        "answer": "B",
        "explanation": "Le siège de l'OCI est à Djeddah en Arabie Saoudite."
    },
    {
        "question": "Le Conseil de l'Europe (qui n'est pas une institution de l'UE) siège à :",
        "options": ["A) Bruxelles", "B) Genève", "C) Strasbourg", "D) La Haye"],
        "answer": "C",
        "explanation": "Le Conseil de l'Europe, garant de la Cour EDH, siège à Strasbourg."
    },
    {
        "question": "L'OPEP (Organisation des Pays Exportateurs de Pétrole) a son siège à :",
        "options": ["A) Riyad", "B) Vienne", "C) Dubaï", "D) Caracas"],
        "answer": "B",
        "explanation": "Bien qu'aucun pays européen ne soit membre, le siège est à Vienne, Autriche."
    },
    {
        "question": "Quelle organisation africaine a été suspendue de la CEDEAO en 2022 et s'en est finalement retirée ?",
        "options": ["A) La Mauritanie", "B) Le Mali", "C) Le Sénégal", "D) Le Togo"],
        "answer": "B",
        "explanation": "Le Mali s'est retiré de la CEDEAO aux côtés du Burkina et du Niger."
    },
    {
        "question": "Quelle cour a son siège à Arusha, Tanzanie, et est un organe de l'Union Africaine ?",
        "options": ["A) La Cour africaine des droits de l'homme et des peuples", "B) La Cour de justice de la CEDEAO", "C) La Cour suprême panafricaine", "D) Le Tribunal pénal international pour le Rwanda"],
        "answer": "A",
        "explanation": "La CADHP siège à Arusha."
    },
]

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
        "question": "'If I ___ about the meeting, I would have attended.'",
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
        "question": "'He told me ___ he would come.'",
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
    },
    {
        "question": "'The report ___ by the committee next week.' (future passive)",
        "options": ["A) is reviewed", "B) will be reviewed", "C) has been reviewed", "D) was reviewed"],
        "answer": "B",
        "explanation": "Future passive: will + be + past participle."
    },
    {
        "question": "Choose the correct preposition: 'She is interested ___ history.'",
        "options": ["A) about", "B) in", "C) for", "D) on"],
        "answer": "B",
        "explanation": "'Interested in' is the correct fixed collocation."
    },
    {
        "question": "'I haven't seen him ___ last Monday.'",
        "options": ["A) for", "B) since", "C) during", "D) until"],
        "answer": "B",
        "explanation": "'Since' is used with a specific point in time (last Monday). 'For' is used with durations."
    },
    {
        "question": "Which word correctly completes: 'He apologised ___ being late.'",
        "options": ["A) about", "B) for", "C) of", "D) to"],
        "answer": "B",
        "explanation": "'Apologise for' is the correct collocation."
    },
    {
        "question": "What is the correct plural of 'child'?",
        "options": ["A) childs", "B) childes", "C) children", "D) child's"],
        "answer": "C",
        "explanation": "'Children' is the irregular plural of 'child'."
    },
    {
        "question": "'By the time I arrived, the movie ___.'",
        "options": ["A) already started", "B) has already started", "C) had already started", "D) was already starting"],
        "answer": "C",
        "explanation": "Past perfect for an action completed before another past action: had + past participle."
    },
    {
        "question": "Which sentence uses 'yet' correctly?",
        "options": ["A) I have finished yet.", "B) Have you finished yet?", "C) Yet I finished.", "D) I yet finished."],
        "answer": "B",
        "explanation": "'Yet' in questions means 'up to now'. In negatives: 'I haven't finished yet.'"
    },
    {
        "question": "'She made him ___ the dishes.'",
        "options": ["A) wash", "B) to wash", "C) washing", "D) washed"],
        "answer": "A",
        "explanation": "Causative 'make' + object + bare infinitive (without 'to')."
    },
    {
        "question": "Which is the correct indirect question?",
        "options": ["A) He asked where did she live.", "B) He asked where she lived.", "C) He asked where she does live.", "D) He asked where lived she."],
        "answer": "B",
        "explanation": "In indirect questions, use statement word order (no inversion, no auxiliary verb)."
    },
    {
        "question": "'___ you mind opening the window?' (polite request)",
        "options": ["A) Do", "B) Would", "C) Could", "D) Both B and C"],
        "answer": "D",
        "explanation": "Both 'Would you mind...' and 'Could you mind...' are polite requests. 'Would' is slightly more formal."
    },
    {
        "question": "Complete: 'He suggested that she ___ a doctor.'",
        "options": ["A) sees", "B) see", "C) saw", "D) should sees"],
        "answer": "B",
        "explanation": "After 'suggest that', use the base form (subjunctive mood in formal English)."
    },
    {
        "question": "What does 'albeit' mean?",
        "options": ["A) Because", "B) Although / even though", "C) Therefore", "D) Unless"],
        "answer": "B",
        "explanation": "'Albeit' is a formal conjunction meaning 'although' or 'even though'."
    },
    {
        "question": "Choose the correct form: 'Neither of the students ___ prepared.'",
        "options": ["A) were", "B) are", "C) was", "D) be"],
        "answer": "C",
        "explanation": "'Neither' as a subject takes a singular verb: 'was'."
    },
    {
        "question": "Which sentence uses the gerund correctly?",
        "options": ["A) I enjoy to swim.", "B) I enjoy swim.", "C) I enjoy swimming.", "D) I enjoy swam."],
        "answer": "C",
        "explanation": "'Enjoy' is always followed by a gerund (verb + -ing)."
    },
    {
        "question": "What is the passive form of 'They will announce the results tomorrow'?",
        "options": ["A) The results are announced tomorrow.", "B) The results will be announced tomorrow.", "C) The results have been announced tomorrow.", "D) The results were announced tomorrow."],
        "answer": "B",
        "explanation": "Future passive: will + be + past participle."
    },
    {
        "question": "What does 'henceforth' mean?",
        "options": ["A) In the past", "B) From this point on", "C) Nevertheless", "D) Therefore"],
        "answer": "B",
        "explanation": "'Henceforth' is a formal adverb meaning 'from now on / from this point forward'."
    },
    {
        "question": "'I ___ here for two years by next January.' (future perfect continuous)",
        "options": ["A) will live", "B) will have been living", "C) have been living", "D) am living"],
        "answer": "B",
        "explanation": "Future perfect continuous: will have been + -ing. Used for duration up to a future point."
    },
    {
        "question": "Which is the correct tag question for 'Let's go, ___?'",
        "options": ["A) shall we", "B) will we", "C) do we", "D) won't we"],
        "answer": "A",
        "explanation": "The tag question for 'Let's...' is always 'shall we?'"
    },
    {
        "question": "Choose the correct meaning of 'notwithstanding':",
        "options": ["A) In addition to", "B) Despite / in spite of", "C) Because of", "D) Instead of"],
        "answer": "B",
        "explanation": "'Notwithstanding' is a formal word meaning 'despite' or 'in spite of'."
    },
    {
        "question": "Complete: '___ hard work, he failed the exam.'",
        "options": ["A) Although", "B) Despite", "C) However", "D) Because of"],
        "answer": "B",
        "explanation": "'Despite' + noun/gerund. 'Although' needs a full clause with subject + verb."
    },
    {
        "question": "What is the correct form? 'The news ___ shocking.'",
        "options": ["A) are", "B) were", "C) is", "D) have been"],
        "answer": "C",
        "explanation": "'News' is an uncountable noun that takes a singular verb."
    },
    {
        "question": "Which phrasal verb means 'to investigate or look into'?",
        "options": ["A) look up", "B) look into", "C) look after", "D) look out"],
        "answer": "B",
        "explanation": "'Look into' means to investigate or examine something carefully."
    },
    {
        "question": "Choose the correct sentence about habitual past:",
        "options": ["A) I used to eating there.", "B) I would eat there every week.", "C) I was used to eat there.", "D) I have used to eat there."],
        "answer": "B",
        "explanation": "Both 'used to' and 'would' express past habits, but 'would' cannot refer to past states."
    },
    {
        "question": "'She advised me ___ the contract before signing.'",
        "options": ["A) read", "B) reading", "C) to read", "D) to reading"],
        "answer": "C",
        "explanation": "'Advise' + object + to-infinitive."
    },
    {
        "question": "What is the difference between 'few' and 'a few'?",
        "options": ["A) No difference", "B) 'Few' is negative (almost none); 'a few' is positive (some)", "C) 'A few' is used with uncountable nouns", "D) 'Few' is formal, 'a few' is informal"],
        "answer": "B",
        "explanation": "'Few' emphasises scarcity; 'a few' emphasises that there is at least some quantity."
    },
    {
        "question": "Complete: '___ he studied hard, he passed the exam.' (result of condition)",
        "options": ["A) If", "B) Although", "C) Because", "D) Unless"],
        "answer": "C",
        "explanation": "'Because' introduces a cause/reason. The sentence means his hard work caused him to pass."
    },
    {
        "question": "Which is the correct form of reported speech for 'I will call you'?",
        "options": ["A) He said he will call me.", "B) He said he would call me.", "C) He said he calls me.", "D) He said he had called me."],
        "answer": "B",
        "explanation": "In reported speech, 'will' shifts to 'would' (backshift of tenses)."
    },
    {
        "question": "What does 'to be on the fence' mean?",
        "options": ["A) To be in danger", "B) To be undecided/neutral", "C) To be very happy", "D) To be at work"],
        "answer": "B",
        "explanation": "Idiom: 'to be on the fence' means to be undecided, neutral, or avoid taking a side."
    },
    {
        "question": "Choose the correct collocation:",
        "options": ["A) Do a mistake", "B) Make a mistake", "C) Have a mistake", "D) Take a mistake"],
        "answer": "B",
        "explanation": "The correct collocation is 'make a mistake', not 'do'."
    },
    {
        "question": "Which sentence correctly uses the present perfect continuous?",
        "options": ["A) She has been working here for two years.", "B) She is working here for two years.", "C) She has worked here since two years.", "D) She works here for two years."],
        "answer": "A",
        "explanation": "Present perfect continuous: have/has + been + -ing, often with 'for' or 'since'."
    },
    {
        "question": "Complete: 'If only I ___ more time to prepare!'",
        "options": ["A) have", "B) had", "C) will have", "D) would have"],
        "answer": "B",
        "explanation": "'If only' + past tense expresses a wish about the present (unreal condition)."
    },
    {
        "question": "Which sentence is INCORRECT?",
        "options": ["A) The police are investigating.", "B) My family are coming tomorrow.", "C) The committee has reached a decision.", "D) These informations are useful."],
        "answer": "D",
        "explanation": "'Information' is uncountable in English: 'this information' or 'these pieces of information'."
    },
    {
        "question": "What is the meaning of 'to get cold feet'?",
        "options": ["A) To be cold", "B) To become nervous and lose courage", "C) To be unprepared", "D) To arrive late"],
        "answer": "B",
        "explanation": "Idiom: 'to get cold feet' means to become nervous and reluctant to do something."
    },
    {
        "question": "Which is the correct conditional type 3?",
        "options": ["A) If she studied harder, she would pass.", "B) If she had studied harder, she would have passed.", "C) If she studies harder, she will pass.", "D) If she would study harder, she passes."],
        "answer": "B",
        "explanation": "Type 3 conditional: If + past perfect, would have + past participle. It refers to unreal past situations."
    },
    {
        "question": "Choose the correct preposition: 'She is very good ___ solving problems.'",
        "options": ["A) in", "B) on", "C) at", "D) for"],
        "answer": "C",
        "explanation": "'Good at' + gerund is the correct collocation for skills/abilities."
    },
    {
        "question": "What does 'to beat around the bush' mean?",
        "options": ["A) To be very direct", "B) To avoid the main topic", "C) To work hard", "D) To be confused"],
        "answer": "B",
        "explanation": "Idiom: 'to beat around the bush' means to avoid coming to the main point."
    },
    {
        "question": "What is the gerund form of 'write'?",
        "options": ["A) Written", "B) Wrote", "C) Writing", "D) To write"],
        "answer": "C",
        "explanation": "The gerund is the -ing form used as a noun: 'Writing is important.'"
    },
    {
        "question": "Choose the correct form: '___ the meeting, I took notes.'",
        "options": ["A) Since", "B) During", "C) While", "D) For"],
        "answer": "B",
        "explanation": "'During' + noun. 'While' needs a clause with subject + verb."
    },
    {
        "question": "What is the superlative of 'bad'?",
        "options": ["A) More bad", "B) Worse", "C) The worst", "D) Baddest"],
        "answer": "C",
        "explanation": "Irregular superlative: bad → worse → the worst."
    },
    {
        "question": "Which sentence correctly uses 'unless'?",
        "options": ["A) Unless you don't hurry, you'll miss the train.", "B) Unless you hurry, you'll miss the train.", "C) Unless you hurry, you won't miss the train.", "D) Unless you hurried, you miss the train."],
        "answer": "B",
        "explanation": "'Unless' = 'if...not'. Never combine with another negative: 'unless you hurry' = 'if you don't hurry'."
    },
    {
        "question": "If I _____ you, I wouldn't have accepted the offer.",
        "options": ["A) was", "B) am", "C) had been", "D) were"],
        "answer": "D",
        "explanation": "In conditional type 2 (unreal present), 'were' is used for all subjects. However, due to 'wouldn't have accepted' (type 3), the first part should technically be 'had been', but mixed conditionals exist: If I were you (now/general), I wouldn't have done that (past)."
    },
    {
        "question": "By the time we get to the cinema, the movie _____.",
        "options": ["A) will start", "B) will have started", "C) started", "D) has started"],
        "answer": "B",
        "explanation": "The future perfect 'will have started' is used for an action that will be completed before a certain time in the future."
    },
    {
        "question": "He has been working here _____ 2015.",
        "options": ["A) since", "B) for", "C) in", "D) from"],
        "answer": "A",
        "explanation": "'Since' is used with a specific point in time to indicate the beginning of an ongoing action."
    },
    {
        "question": "I look forward to _____ from you soon.",
        "options": ["A) hear", "B) heard", "C) hearing", "D) be hearing"],
        "answer": "C",
        "explanation": "The phrase 'look forward to' is always followed by a gerund (verb + -ing)."
    },
    {
        "question": "Hardly _____ entered the room when the phone rang.",
        "options": ["A) I had", "B) had I", "C) I", "D) did I"],
        "answer": "B",
        "explanation": "After 'Hardly', subject-verb inversion is required in formal English."
    },
    {
        "question": "She is used to _____ up early.",
        "options": ["A) wake", "B) waking", "C) woke", "D) woken"],
        "answer": "B",
        "explanation": "'To be used to' is followed by a gerund (verb + -ing)."
    },
    {
        "question": "The manager _____ the meeting until next week.",
        "options": ["A) put off", "B) put on", "C) put out", "D) put away"],
        "answer": "A",
        "explanation": "The phrasal verb 'put off' means to postpone."
    },
    {
        "question": "If you don't know the word, look it _____ in the dictionary.",
        "options": ["A) out", "B) for", "C) up", "D) at"],
        "answer": "C",
        "explanation": "'Look up' means to search for information in a reference book."
    },
    {
        "question": "Neither the manager nor the employees _____ aware of the changes.",
        "options": ["A) was", "B) is", "C) were", "D) has been"],
        "answer": "C",
        "explanation": "With 'neither... nor', the verb agrees with the subject closest to it ('employees', which is plural)."
    },
    {
        "question": "It's high time you _____ studying for the ENA exam.",
        "options": ["A) start", "B) started", "C) will start", "D) had started"],
        "answer": "B",
        "explanation": "The phrase 'It is high time' is followed by the past simple to refer to the present or future."
    },
    {
        "question": "The company went bankrupt because it was heavily _____.",
        "options": ["A) in debt", "B) on debt", "C) with debt", "D) of debt"],
        "answer": "A",
        "explanation": "The correct idiom is 'in debt'."
    },
    {
        "question": "Despite _____ hard, he failed the test.",
        "options": ["A) he tried", "B) trying", "C) to try", "D) of trying"],
        "answer": "B",
        "explanation": "'Despite' is followed by a noun or a gerund ('trying')."
    },
    {
        "question": "The committee _____ composed of five members.",
        "options": ["A) are", "B) is", "C) have", "D) has"],
        "answer": "B",
        "explanation": "'Committee' is a collective noun often treated as singular when acting as a single unit."
    },
    {
        "question": "I would rather you _____ home now.",
        "options": ["A) go", "B) going", "C) went", "D) gone"],
        "answer": "C",
        "explanation": "'Would rather' followed by a subject takes the past tense to express a present preference."
    },
    {
        "question": "Choose the correct spelling:",
        "options": ["A) Accomodation", "B) Accommodation", "C) Accomadation", "D) Acommodation"],
        "answer": "B",
        "explanation": "'Accommodation' takes two c's and two m's."
    },
    {
        "question": "He denied _____ the money.",
        "options": ["A) to steal", "B) steal", "C) stole", "D) stealing"],
        "answer": "D",
        "explanation": "The verb 'deny' is followed by a gerund."
    },
    {
        "question": "Let's grab a coffee, _____ we?",
        "options": ["A) will", "B) do", "C) shall", "D) won't"],
        "answer": "C",
        "explanation": "The question tag for 'Let's' is always 'shall we'."
    },
    {
        "question": "The new policy will be _____ next month.",
        "options": ["A) implemented", "B) implies", "C) implicate", "D) implicit"],
        "answer": "A",
        "explanation": "Policies are 'implemented' (put into effect)."
    },
    {
        "question": "I am not used to _____ on the left side of the road.",
        "options": ["A) drive", "B) driving", "C) drove", "D) driven"],
        "answer": "B",
        "explanation": "'Used to' acting as an adjective (meaning accustomed to) takes a gerund."
    },
    {
        "question": "He is the man _____ car was stolen yesterday.",
        "options": ["A) who", "B) whom", "C) whose", "D) which"],
        "answer": "C",
        "explanation": "'Whose' is the relative pronoun used to indicate possession."
    },
    {
        "question": "The project was delayed _____ a lack of funds.",
        "options": ["A) because", "B) due to", "C) since", "D) for"],
        "answer": "B",
        "explanation": "'Due to' is followed by a noun phrase."
    },
    {
        "question": "If he had known the truth, he _____ differently.",
        "options": ["A) would act", "B) will act", "C) would have acted", "D) acts"],
        "answer": "C",
        "explanation": "Third conditional requires 'would have + past participle' in the main clause."
    },
    {
        "question": "They rarely speak to each other, _____ they?",
        "options": ["A) do", "B) don't", "C) are", "D) aren't"],
        "answer": "A",
        "explanation": "'Rarely' has a negative meaning, so the question tag is positive."
    },
    {
        "question": "She succeeded in _____ the difficult exam.",
        "options": ["A) pass", "B) passing", "C) passed", "D) to pass"],
        "answer": "B",
        "explanation": "Prepositions like 'in' are followed by the gerund form of a verb."
    },
    {
        "question": "I wish I _____ richer.",
        "options": ["A) am", "B) was", "C) were", "D) have been"],
        "answer": "C",
        "explanation": "After 'I wish', 'were' is used for all persons to express an unreal present situation."
    },
    {
        "question": "Not only _____ late, but he also forgot his documents.",
        "options": ["A) he arrived", "B) did he arrive", "C) he did arrive", "D) arrives he"],
        "answer": "B",
        "explanation": "When 'Not only' starts a sentence, it triggers inversion."
    },
    {
        "question": "The term 'false friend' (faux ami) 'Actual' in English means:",
        "options": ["A) Currently happening", "B) Real or exact", "C) Modern", "D) Updated"],
        "answer": "B",
        "explanation": "'Actual' means real, true, or exact, unlike 'actuel' in French which means current."
    },
    {
        "question": "Which of these is a synonym for 'mitigate'?",
        "options": ["A) Worsen", "B) Alleviate", "C) Provoke", "D) Startle"],
        "answer": "B",
        "explanation": "'Mitigate' means to make something less severe or painful, similar to 'alleviate'."
    },
    {
        "question": "He gave me a lot of _____ on how to pass the ENA exam.",
        "options": ["A) advices", "B) advise", "C) advice", "D) advising"],
        "answer": "C",
        "explanation": "'Advice' is an uncountable noun and does not take an 's'."
    },
    {
        "question": "They _____ to Paris twice this year.",
        "options": ["A) went", "B) go", "C) have been", "D) had been"],
        "answer": "C",
        "explanation": "The present perfect 'have been' is used for actions completed in a time period that is not yet over ('this year')."
    },
    {
        "question": "She avoids _____ in public.",
        "options": ["A) to speak", "B) speak", "C) speaking", "D) spoken"],
        "answer": "C",
        "explanation": "The verb 'avoid' is followed by a gerund."
    },
    {
        "question": "You had better _____ your doctor.",
        "options": ["A) to see", "B) seeing", "C) see", "D) saw"],
        "answer": "C",
        "explanation": "'Had better' is followed by the bare infinitive (without 'to')."
    },
    {
        "question": "There is a _____ difference between the two proposals.",
        "options": ["A) subtle", "B) sutil", "C) subtil", "D) sutle"],
        "answer": "A",
        "explanation": "The correct spelling in English is 'subtle'."
    },
    {
        "question": "He speaks English _____ than his brother.",
        "options": ["A) more better", "B) much better", "C) most better", "D) best"],
        "answer": "B",
        "explanation": "'Better' is the comparative form of well/good, modified correctly by 'much'."
    },
    {
        "question": "By 2030, the government _____ building the new hospital.",
        "options": ["A) will finish", "B) has finished", "C) will have finished", "D) finishes"],
        "answer": "C",
        "explanation": "Future perfect is used for an action completed before a specific time in the future."
    },
    {
        "question": "The English translation of 'assister à une réunion' is:",
        "options": ["A) to assist a meeting", "B) to attend a meeting", "C) to follow a meeting", "D) to participate a meeting"],
        "answer": "B",
        "explanation": "'To attend' means to be present at an event. 'To assist' means to help."
    },
    {
        "question": "I can't figure _____ how to solve this math problem.",
        "options": ["A) out", "B) in", "C) on", "D) up"],
        "answer": "A",
        "explanation": "The phrasal verb 'figure out' means to solve or understand."
    },
    {
        "question": "He has little experience, _____?",
        "options": ["A) has he", "B) hasn't he", "C) does he", "D) doesn't he"],
        "answer": "C",
        "explanation": "'Little' has a negative meaning, and 'has' as a main verb often takes 'does' in tags."
    },
    {
        "question": "It's imperative that he _____ present at the meeting.",
        "options": ["A) is", "B) be", "C) was", "D) will be"],
        "answer": "B",
        "explanation": "The subjunctive mood is used after adjectives of urgency like 'imperative'."
    },
    {
        "question": "We ran out _____ petrol on the highway.",
        "options": ["A) of", "B) from", "C) off", "D) with"],
        "answer": "A",
        "explanation": "The phrasal verb 'run out of' means to use all of a supply."
    },
    {
        "question": "She accused him _____ stealing the documents.",
        "options": ["A) for", "B) of", "C) about", "D) with"],
        "answer": "B",
        "explanation": "The verb 'accuse' is followed by the preposition 'of'."
    },
    {
        "question": "I remember _____ him at the conference last year.",
        "options": ["A) meet", "B) to meet", "C) meeting", "D) met"],
        "answer": "C",
        "explanation": "'Remember' + gerund refers to a memory of a past event."
    },
    {
        "question": "The English false friend 'sensible' translates to French as:",
        "options": ["A) sensible", "B) raisonnable", "C) sensitif", "D) sensationnel"],
        "answer": "B",
        "explanation": "'Sensible' in English means logical, practical, or 'raisonnable'. 'Sensitive' means 'sensible' (French)."
    },
    {
        "question": "He is _____ engineer.",
        "options": ["A) a", "B) an", "C) the", "D) no article"],
        "answer": "B",
        "explanation": "'An' is used before professions starting with a vowel sound."
    },
    {
        "question": "I would have called you if I _____ my phone.",
        "options": ["A) had", "B) have had", "C) had had", "D) have"],
        "answer": "C",
        "explanation": "Third conditional 'if' clause requires the past perfect ('had had')."
    },
    {
        "question": "The boss made him _____ late to finish the report.",
        "options": ["A) to stay", "B) stay", "C) staying", "D) stayed"],
        "answer": "B",
        "explanation": "'Make' is a causative verb followed by an object and a bare infinitive."
    },
    {
        "question": "They objected _____ treated like children.",
        "options": ["A) to be", "B) being", "C) to being", "D) against being"],
        "answer": "C",
        "explanation": "'Object to' is followed by a gerund ('being')."
    },
    {
        "question": "Only when the plane landed safely _____ to relax.",
        "options": ["A) we began", "B) began we", "C) did we begin", "D) we did begin"],
        "answer": "C",
        "explanation": "Inversion is required when a sentence starts with 'Only when'."
    },
    {
        "question": "The word 'comprehensive' means:",
        "options": ["A) Understanding", "B) Thorough and complete", "C) Compromising", "D) Complicated"],
        "answer": "B",
        "explanation": "'Comprehensive' is a false friend; it means 'exhaustif' or 'complet' in French, not 'compréhensif'."
    },
    {
        "question": "Complete the sentence: It is crucial that the newly appointed director _____ the upcoming board meeting.",
        "options": ["A) attends", "B) attend", "C) attending", "D) will attend"],
        "answer": "B",
        "explanation": "The subjunctive mood is used after expressions of necessity like 'It is crucial that', requiring the base form of the verb."
    },
    {
        "question": "Hardly _____ the office when the phone started ringing.",
        "options": ["A) he had entered", "B) did he enter", "C) had he entered", "D) he entered"],
        "answer": "C",
        "explanation": "Negative adverbial phrases like 'Hardly' at the beginning of a sentence require subject-auxiliary inversion, typically past perfect 'had + subject + past participle'."
    },
    {
        "question": "If the committee had approved the budget last week, we _____ the project right now.",
        "options": ["A) would have started", "B) will start", "C) would be starting", "D) had started"],
        "answer": "C",
        "explanation": "This is a mixed conditional: a past unreal condition ('had approved') resulting in a present unreal result ('would be starting right now')."
    },
    {
        "question": "The manager decided to _____ the less productive employees due to budget cuts.",
        "options": ["A) lay off", "B) lay out", "C) put off", "D) call off"],
        "answer": "A",
        "explanation": "'Lay off' means to discharge a worker temporarily or permanently because of a shortage of work."
    },
    {
        "question": "Not only _____ the new policy increase efficiency, but it also improves employee morale.",
        "options": ["A) does", "B) do", "C) has", "D) did"],
        "answer": "A",
        "explanation": "Inversion is required after 'Not only' at the beginning of a sentence. Since the second clause uses 'improves' (present tense), 'does' is appropriate."
    },
    {
        "question": "I suggest that the applicant _____ all relevant documents before the deadline.",
        "options": ["A) submits", "B) submitted", "C) submit", "D) has submitted"],
        "answer": "C",
        "explanation": "Verbs like 'suggest', 'recommend', and 'demand' are followed by a 'that' clause with a verb in the subjunctive mood (base form)."
    },
    {
        "question": "She couldn't quite _____ what the speaker was trying to say amidst the noise.",
        "options": ["A) make up", "B) make out", "C) figure off", "D) take in"],
        "answer": "B",
        "explanation": "'Make out' means to manage to see, hear, or understand something."
    },
    {
        "question": "By the time the delegation arrives next week, the necessary preparations _____.",
        "options": ["A) are completed", "B) will have been completed", "C) will be completing", "D) have been completed"],
        "answer": "B",
        "explanation": "The future perfect passive ('will have been completed') is used to describe an action that will be finished before a specific time in the future."
    },
    {
        "question": "The contractor promised that the building _____ by the end of November.",
        "options": ["A) would be finished", "B) will finish", "C) is finished", "D) finishes"],
        "answer": "A",
        "explanation": "Reported speech in the past ('promised') typically shifts future tense ('will be finished') to conditional ('would be finished')."
    },
    {
        "question": "Despite _____ a lack of resources, the team successfully launched the application.",
        "options": ["A) of facing", "B) facing", "C) to face", "D) they faced"],
        "answer": "B",
        "explanation": "'Despite' is a preposition and should be followed by a noun or a gerund ('facing'), without 'of'."
    },
    {
        "question": "We must _____ the fact that our competitors are gaining market share.",
        "options": ["A) face up to", "B) put up with", "C) get away with", "D) look down on"],
        "answer": "A",
        "explanation": "'Face up to' means to accept a difficult situation and deal with it."
    },
    {
        "question": "It is imperative that the regulations _____ strictly enforced to ensure safety.",
        "options": ["A) are", "B) be", "C) will be", "D) have been"],
        "answer": "B",
        "explanation": "'It is imperative that' triggers the subjunctive mood, requiring the base form of the verb ('be')."
    },
    {
        "question": "Were _____ not for his timely intervention, the project would have failed.",
        "options": ["A) he", "B) it", "C) there", "D) that"],
        "answer": "B",
        "explanation": "'Were it not for' is a formal, inverted conditional phrase meaning 'If it were not for'."
    },
    {
        "question": "The CEO decided to step down, _____ paving the way for a younger leadership team.",
        "options": ["A) thereby", "B) however", "C) moreover", "D) nevertheless"],
        "answer": "A",
        "explanation": "'Thereby' means 'as a result of that action', which fits contextually."
    },
    {
        "question": "The company's profits have been declining steadily; _____, they have announced a hiring freeze.",
        "options": ["A) conversely", "B) consequently", "C) furthermore", "D) nonetheless"],
        "answer": "B",
        "explanation": "'Consequently' indicates that the hiring freeze is a result of the declining profits."
    },
    {
        "question": "I would rather you _____ the proposal before submitting it to the client.",
        "options": ["A) review", "B) reviewed", "C) have reviewed", "D) will review"],
        "answer": "B",
        "explanation": "'Would rather' followed by a subject requires the past subjunctive (past simple form) to express a preference about the present or future."
    },
    {
        "question": "The auditor found several discrepancies that need to be _____ immediately.",
        "options": ["A) looked into", "B) brought up", "C) taken over", "D) passed out"],
        "answer": "A",
        "explanation": "'Looked into' means to investigate or examine."
    },
    {
        "question": "Rarely _____ such a dedicated group of professionals.",
        "options": ["A) have I seen", "B) I have seen", "C) did I saw", "D) I saw"],
        "answer": "A",
        "explanation": "Negative adverbial 'Rarely' at the beginning of a sentence requires subject-auxiliary inversion."
    },
    {
        "question": "The new software is designed to _____ the administrative process, making it much faster.",
        "options": ["A) streamline", "B) undermine", "C) compromise", "D) exacerbate"],
        "answer": "A",
        "explanation": "'Streamline' means to make a process more efficient and effective."
    },
    {
        "question": "He was _____ on the spot for his gross misconduct.",
        "options": ["A) laid off", "B) fired", "C) stepped down", "D) taken back"],
        "answer": "B",
        "explanation": "'Fired' implies dismissal for cause, such as misconduct, whereas 'laid off' implies redundancy."
    },
    {
        "question": "If she had known about the traffic, she _____ another route.",
        "options": ["A) would take", "B) took", "C) would have taken", "D) had taken"],
        "answer": "C",
        "explanation": "Third conditional requires 'would have + past participle' in the main clause."
    },
    {
        "question": "The board requires that every member _____ present at the annual general meeting.",
        "options": ["A) is", "B) be", "C) are", "D) will be"],
        "answer": "B",
        "explanation": "'Requires that' is followed by the subjunctive mood, which uses the base form 'be'."
    },
    {
        "question": "The manager had to _____ the meeting because several key participants were unavailable.",
        "options": ["A) call off", "B) bring about", "C) carry out", "D) set up"],
        "answer": "A",
        "explanation": "'Call off' means to cancel an event."
    },
    {
        "question": "We are looking forward to _____ from you soon.",
        "options": ["A) hear", "B) hearing", "C) be heard", "D) have heard"],
        "answer": "B",
        "explanation": "The phrase 'look forward to' is followed by a gerund ('hearing')."
    },
    {
        "question": "Scarcely had the president began his speech _____ the lights went out.",
        "options": ["A) than", "B) when", "C) that", "D) before"],
        "answer": "B",
        "explanation": "The correlative conjunction pair is 'Scarcely... when' (or 'Hardly... when')."
    },
    {
        "question": "The new regulations will _____ effect on January 1st.",
        "options": ["A) make", "B) take", "C) put", "D) set"],
        "answer": "B",
        "explanation": "The correct collocation is 'take effect', meaning to come into operation."
    },
    {
        "question": "She is accustomed _____ working long hours during the tax season.",
        "options": ["A) with", "B) to", "C) for", "D) in"],
        "answer": "B",
        "explanation": "The adjective 'accustomed' is followed by the preposition 'to'."
    },
    {
        "question": "He was accused _____ embezzling company funds.",
        "options": ["A) for", "B) of", "C) with", "D) about"],
        "answer": "B",
        "explanation": "The correct preposition after 'accused' is 'of'."
    },
    {
        "question": "Under no circumstances _____ allowed to leave the premises without permission.",
        "options": ["A) employees are", "B) are employees", "C) employees will be", "D) have employees"],
        "answer": "B",
        "explanation": "Negative prepositional phrases like 'Under no circumstances' at the beginning of a sentence require inversion."
    },
    {
        "question": "The project was completed ahead of schedule, _____ surprised everyone.",
        "options": ["A) that", "B) which", "C) what", "D) who"],
        "answer": "B",
        "explanation": "The relative pronoun 'which' is used to refer back to the entire preceding clause."
    },
    {
        "question": "If it _____ rain tomorrow, we will have to reschedule the outdoor event.",
        "options": ["A) would", "B) should", "C) might", "D) could"],
        "answer": "B",
        "explanation": "'If it should rain' is a formal way to express a conditional future possibility."
    },
    {
        "question": "The committee demanded that the controversial proposal _____ withdrawn immediately.",
        "options": ["A) is", "B) be", "C) was", "D) has been"],
        "answer": "B",
        "explanation": "'Demanded that' requires the subjunctive base form 'be'."
    },
    {
        "question": "She speaks English fluently, _____ a slight accent.",
        "options": ["A) albeit", "B) despite", "C) whereas", "D) nonetheless"],
        "answer": "A",
        "explanation": "'Albeit' is a formal conjunction meaning 'although' or 'even if'."
    },
    {
        "question": "The company has decided to _____ its operations in the Asian market.",
        "options": ["A) scale back", "B) bring up", "C) pass out", "D) turn down"],
        "answer": "A",
        "explanation": "'Scale back' means to reduce the size or extent of something."
    },
    {
        "question": "Having _____ the document, he handed it to the director for signature.",
        "options": ["A) write", "B) written", "C) wrote", "D) writing"],
        "answer": "B",
        "explanation": "A perfect participle clause requires 'Having + past participle'."
    },
    {
        "question": "The instructions were convoluted; I couldn't make _____ of them.",
        "options": ["A) sense", "B) head nor tail", "C) meaning", "D) understanding"],
        "answer": "B",
        "explanation": "'Make head nor tail' is an idiom meaning to be completely unable to understand something."
    },
    {
        "question": "It is high time you _____ looking for a more stable job.",
        "options": ["A) start", "B) started", "C) are starting", "D) will start"],
        "answer": "B",
        "explanation": "'It is high time' is followed by the past simple tense to suggest something should be done now."
    },
    {
        "question": "The speaker _____ the importance of international cooperation during his address.",
        "options": ["A) emphasized on", "B) emphasized", "C) stressed on", "D) highlighted on"],
        "answer": "B",
        "explanation": "The verbs 'emphasize' and 'stress' are transitive and do not take the preposition 'on'."
    },
    {
        "question": "She was totally engrossed _____ her research.",
        "options": ["A) in", "B) at", "C) on", "D) with"],
        "answer": "A",
        "explanation": "The adjective 'engrossed' is followed by the preposition 'in'."
    },
    {
        "question": "No sooner had the minister arrived _____ the meeting commenced.",
        "options": ["A) when", "B) than", "C) that", "D) before"],
        "answer": "B",
        "explanation": "The correlative conjunction pair is 'No sooner... than'."
    },
    {
        "question": "The negotiations broke _____ after neither side was willing to compromise.",
        "options": ["A) out", "B) down", "C) through", "D) off"],
        "answer": "B",
        "explanation": "'Break down' refers to the failure of discussions or negotiations."
    },
    {
        "question": "Had I known about the policy change, I _____ differently.",
        "options": ["A) will have acted", "B) would act", "C) would have acted", "D) had acted"],
        "answer": "C",
        "explanation": "Third conditional requires 'would have + past participle' for the result of a past unfulfilled condition."
    },
    {
        "question": "The new employee is still trying to _____ the ropes.",
        "options": ["A) learn", "B) pull", "C) hold", "D) cut"],
        "answer": "A",
        "explanation": "'Learn the ropes' is an idiom meaning to understand how to do a particular job or task."
    },
    {
        "question": "He will not accept the offer unless it _____ his salary expectations.",
        "options": ["A) meets", "B) will meet", "C) meet", "D) met"],
        "answer": "A",
        "explanation": "'Unless' introduces a conditional clause, which takes the present simple tense ('meets') for future meaning."
    },
    {
        "question": "The company's success is largely contingent _____ securing this contract.",
        "options": ["A) on", "B) to", "C) with", "D) for"],
        "answer": "A",
        "explanation": "The adjective 'contingent' is followed by the preposition 'on' or 'upon'."
    },
    {
        "question": "He was completely taken _____ by the fraudulent scheme.",
        "options": ["A) back", "B) in", "C) off", "D) up"],
        "answer": "B",
        "explanation": "'Take in' in passive voice means to be deceived or cheated."
    },
    {
        "question": "It's essential that the data _____ backed up regularly.",
        "options": ["A) is", "B) be", "C) are", "D) will be"],
        "answer": "B",
        "explanation": "'It's essential that' requires the subjunctive base form 'be'."
    },
    {
        "question": "By the end of this year, she _____ as a diplomat for twenty years.",
        "options": ["A) will work", "B) will be working", "C) will have been working", "D) has worked"],
        "answer": "C",
        "explanation": "The future perfect continuous emphasizes the duration of an ongoing action up to a future point."
    },
    {
        "question": "His reckless behavior is bound to _____ consequences.",
        "options": ["A) bring about", "B) come across", "C) put off", "D) take after"],
        "answer": "A",
        "explanation": "'Bring about' means to cause something to happen."
    },
    {
        "question": "They were _____ the impression that the deadline had been extended.",
        "options": ["A) in", "B) on", "C) under", "D) with"],
        "answer": "C",
        "explanation": "The correct prepositional phrase is 'under the impression'."
    },
    {
        "question": "Which of the following sentences is grammatically correct?",
        "options": ["A) He cans swim.", "B) He can to swim.", "C) He can swim.", "D) He does can swim."],
        "answer": "C",
        "explanation": "Modals are invariable and are followed by the base form of the verb without 'to'."
    },
    {
        "question": "How do you form the interrogative of the modal 'can'?",
        "options": ["A) Do you can?", "B) Can you?", "C) Are you can?", "D) Can you to?"],
        "answer": "B",
        "explanation": "Interrogation with modals is formed by inversion, without using the auxiliary 'do'."
    },
    {
        "question": "Choose the correct negative form:",
        "options": ["A) You don't must go.", "B) You mustn't to go.", "C) You must not go.", "D) You don't must to go."],
        "answer": "C",
        "explanation": "Negation with modals is formed directly with 'not' (must not / mustn't), without 'do' and without 'to'."
    },
    {
        "question": "Which form is used to express capability in the future?",
        "options": ["A) will can", "B) will be able to", "C) shall can", "D) cans"],
        "answer": "B",
        "explanation": "Modals like 'can' do not have a future form; 'be able to' is used instead (will be able to)."
    },
    {
        "question": "Despite the heavy fire, they ___ escape from the building.",
        "options": ["A) could", "B) can", "C) were able to", "D) might"],
        "answer": "C",
        "explanation": "For a specific successful achievement in the past (réussite effective), 'was/were able to' must be used instead of 'could'."
    },
    {
        "question": "Which modal is used to ask for formal permission?",
        "options": ["A) Must I", "B) Might I", "C) May I", "D) Shall I"],
        "answer": "C",
        "explanation": "'May' is used for formal permission (e.g., May I?)."
    },
    {
        "question": "Is 'May you swim?' grammatically correct to ask about capability?",
        "options": ["A) Yes, it is formal.", "B) Yes, in British English.", "C) No, 'can' or 'are you able to' should be used.", "D) No, 'might' should be used."],
        "answer": "C",
        "explanation": "'May' expresses permission or possibility, not physical capacity."
    },
    {
        "question": "Which phrase expresses a past reproach?",
        "options": ["A) You might have told me!", "B) You must tell me!", "C) You can have told me!", "D) You may tell me!"],
        "answer": "A",
        "explanation": "'Might have + PP' can express a reproach about a past event."
    },
    {
        "question": "He has a big house and two expensive cars. He ___ be very rich.",
        "options": ["A) has to", "B) can", "C) ought", "D) must"],
        "answer": "D",
        "explanation": "'Must' is used to express a strong subjective deduction (déduction forte)."
    },
    {
        "question": "What is the negative equivalent (negative deduction) of 'He must be at home'?",
        "options": ["A) He mustn't be at home.", "B) He doesn't have to be at home.", "C) He can't be at home.", "D) He shouldn't be at home."],
        "answer": "C",
        "explanation": "The negative deduction of 'must' is 'cannot/can't', not 'mustn't'."
    },
    {
        "question": "I ___ wear a uniform at my new job; it is the company's rule.",
        "options": ["A) must", "B) have to", "C) may", "D) would"],
        "answer": "B",
        "explanation": "'Have to' is used for an external or objective obligation, unlike the subjective 'must'."
    },
    {
        "question": "Which modal is traditionally used in modern English legal documents to express an obligation?",
        "options": ["A) shall", "B) should", "C) would", "D) might"],
        "answer": "A",
        "explanation": "'Shall' is used for legal (juridique) obligations."
    },
    {
        "question": "___ we go out for dinner tonight?",
        "options": ["A) Will", "B) Shall", "C) Ought", "D) Must"],
        "answer": "B",
        "explanation": "'Shall we?' is used to make a suggestion."
    },
    {
        "question": "It's strange that he ___ say such a thing.",
        "options": ["A) would", "B) shall", "C) should", "D) must"],
        "answer": "C",
        "explanation": "'Should' is used to express surprise after certain expressions like 'It's strange that'."
    },
    {
        "question": "Even when I tell him to stop, he ___ keep talking!",
        "options": ["A) should", "B) will", "C) might", "D) ought to"],
        "answer": "B",
        "explanation": "'Will' can be used to express insistence or a persistent present habit."
    },
    {
        "question": "When I was a child, I ___ be very shy.",
        "options": ["A) would", "B) used to", "C) should", "D) could"],
        "answer": "B",
        "explanation": "'Used to' describes a past state. 'Would' cannot replace 'used to' for states (e.g., 'I would be shy' is incorrect)."
    },
    {
        "question": "You ___ to apologize to her; it's your moral duty.",
        "options": ["A) ought", "B) should", "C) must", "D) have"],
        "answer": "A",
        "explanation": "'Ought to' expresses a moral duty or strong advice and is followed by 'to'."
    },
    {
        "question": "___ you use to play football when you were younger?",
        "options": ["A) Do", "B) Were", "C) Are", "D) Did"],
        "answer": "D",
        "explanation": "The interrogative form for a past habit with 'used to' is formed with 'Did' (Did you use to?)."
    },
    {
        "question": "He doesn't ___ to speak in front of the crowd.",
        "options": ["A) dare", "B) dares", "C) daring", "D) dared"],
        "answer": "A",
        "explanation": "When 'dare' is used as an ordinary verb, it uses 'do/does' for negation and takes the infinitive with 'to'."
    },
    {
        "question": "You ___ worry about the exam, it will be easy.",
        "options": ["A) don't need", "B) needn't to", "C) needn't", "D) needs not"],
        "answer": "C",
        "explanation": "When 'need' acts as a modal, it is followed directly by 'not' (needn't) and the base verb without 'to'."
    },
    {
        "question": "You don't ___ worry about it.",
        "options": ["A) need to", "B) need", "C) needs to", "D) needing"],
        "answer": "A",
        "explanation": "When used as an ordinary verb with 'don't', 'need' is followed by 'to' + base verb."
    },
    {
        "question": "I failed the test. I ___ studied more.",
        "options": ["A) must have", "B) should have", "C) might have", "D) can have"],
        "answer": "B",
        "explanation": "'Should have + PP' is used to express a regret about a past action."
    },
    {
        "question": "Her car is not in the driveway. She ___ left already.",
        "options": ["A) should have", "B) might have", "C) must have", "D) cannot have"],
        "answer": "C",
        "explanation": "'Must have + PP' expresses a strong logical deduction about the past."
    },
    {
        "question": "I can't find my keys. I ___ dropped them on the street.",
        "options": ["A) must to have", "B) might have", "C) should have", "D) can have"],
        "answer": "B",
        "explanation": "'Might have + PP' expresses a past possibility."
    },
    {
        "question": "He ___ stolen the money, he was with me the whole time!",
        "options": ["A) mustn't have", "B) shouldn't have", "C) cannot have", "D) mightn't have"],
        "answer": "C",
        "explanation": "'Cannot have + PP' is the negative logical deduction about the past."
    },
    {
        "question": "I will meet you ___ the station.",
        "options": ["A) in", "B) on", "C) at", "D) by"],
        "answer": "C",
        "explanation": "'At' is used for precise points or institutions like the station, school, or work."
    },
    {
        "question": "He is currently working ___ France.",
        "options": ["A) at", "B) on", "C) in", "D) into"],
        "answer": "C",
        "explanation": "'In' is used for countries, cities, and enclosed spaces."
    },
    {
        "question": "The book is ___ the table.",
        "options": ["A) on", "B) in", "C) at", "D) above"],
        "answer": "A",
        "explanation": "'On' is used for surfaces."
    },
    {
        "question": "They opened a new shop ___ Oxford Street.",
        "options": ["A) at", "B) in", "C) on", "D) by"],
        "answer": "C",
        "explanation": "'On' is used for streets."
    },
    {
        "question": "Which of the following is correct?",
        "options": ["A) at bed", "B) in bed", "C) on bed", "D) to bed"],
        "answer": "B",
        "explanation": "'In bed' is the correct exception for this enclosed space concept."
    },
    {
        "question": "I heard the news ___ TV.",
        "options": ["A) in", "B) at", "C) by", "D) on"],
        "answer": "D",
        "explanation": "'On TV' is an idiomatic exception using 'on'."
    },
    {
        "question": "The picture is hanging ___ the sofa.",
        "options": ["A) above", "B) over", "C) on", "D) under"],
        "answer": "A",
        "explanation": "'Above' means a higher position without direct physical contact or movement/covering."
    },
    {
        "question": "The cat ran ___ the table.",
        "options": ["A) below", "B) under", "C) at", "D) in"],
        "answer": "B",
        "explanation": "'Under' is used when there is movement or covering involved."
    },
    {
        "question": "Our flight leaves ___ 6:00 AM.",
        "options": ["A) in", "B) on", "C) at", "D) by"],
        "answer": "C",
        "explanation": "'At' is used for specific times."
    },
    {
        "question": "He likes to read ___ night.",
        "options": ["A) in", "B) on", "C) at", "D) during"],
        "answer": "C",
        "explanation": "'At night' is an exception. (We say 'in the morning', but 'at night')."
    },
    {
        "question": "We usually go to the beach ___ July.",
        "options": ["A) on", "B) in", "C) at", "D) for"],
        "answer": "B",
        "explanation": "'In' is used for months, years, seasons, and centuries."
    },
    {
        "question": "The project will be finished ___ two days.",
        "options": ["A) at", "B) on", "C) in", "D) by"],
        "answer": "C",
        "explanation": "'In' is used to mean 'at the end of a period' (e.g., in two days)."
    },
    {
        "question": "The meeting is scheduled ___ Monday.",
        "options": ["A) on", "B) in", "C) at", "D) by"],
        "answer": "A",
        "explanation": "'On' is used for days of the week and dates."
    },
    {
        "question": "We will have a party ___ 15th August.",
        "options": ["A) in", "B) at", "C) on", "D) from"],
        "answer": "C",
        "explanation": "'On' is used for specific dates."
    },
    {
        "question": "I am leaving for Paris ___ tomorrow.",
        "options": ["A) on", "B) in", "C) at", "D) (no preposition)"],
        "answer": "D",
        "explanation": "No preposition is used before 'tomorrow', 'yesterday', or 'today'."
    },
    {
        "question": "I go ___ school every morning.",
        "options": ["A) in", "B) at", "C) to", "D) into"],
        "answer": "C",
        "explanation": "'To' indicates direction or destination."
    },
    {
        "question": "After work, I usually go ___ home.",
        "options": ["A) at", "B) to", "C) in", "D) (no preposition)"],
        "answer": "D",
        "explanation": "'Home' takes no preposition indicating direction (e.g., 'go home', NOT 'go to home')."
    },
    {
        "question": "He jumped ___ the swimming pool.",
        "options": ["A) on", "B) into", "C) in", "D) to"],
        "answer": "B",
        "explanation": "'Into' shows movement towards the inside of something."
    },
    {
        "question": "The train went ___ the tunnel.",
        "options": ["A) across", "B) through", "C) along", "D) to"],
        "answer": "B",
        "explanation": "'Through' means moving from one side to the other of an enclosed space."
    },
    {
        "question": "We walked ___ the street to reach the bakery on the other side.",
        "options": ["A) through", "B) across", "C) along", "D) from"],
        "answer": "B",
        "explanation": "'Across' means moving from one side to the other."
    },
    {
        "question": "They were walking ___ the river.",
        "options": ["A) across", "B) along", "C) through", "D) over"],
        "answer": "B",
        "explanation": "'Along' means moving parallel to a line (like a river or a road)."
    },
    {
        "question": "This book was written ___ an unknown author.",
        "options": ["A) from", "B) with", "C) by", "D) of"],
        "answer": "C",
        "explanation": "'By' is used to introduce the passive agent."
    },
    {
        "question": "I usually travel to London ___ plane.",
        "options": ["A) on", "B) by", "C) in", "D) at"],
        "answer": "B",
        "explanation": "'By + noun without article' indicates the means of transport (by plane)."
    },
    {
        "question": "He was trembling ___ fear when he saw the ghost.",
        "options": ["A) of", "B) with", "C) by", "D) from"],
        "answer": "B",
        "explanation": "'With' is used for cause in expressions like 'trembling with fear'."
    },
    {
        "question": "I have been living here ___ two years.",
        "options": ["A) since", "B) for", "C) during", "D) in"],
        "answer": "B",
        "explanation": "'For' is used for a duration (e.g., for two years)."
    },
    {
        "question": "I have been working here ___ 2020.",
        "options": ["A) for", "B) since", "C) from", "D) in"],
        "answer": "B",
        "explanation": "'Since' indicates the starting point of an action."
    },
    {
        "question": "He slept ___ the meeting.",
        "options": ["A) for", "B) during", "C) since", "D) in"],
        "answer": "B",
        "explanation": "'During' is used before a period or an event, never followed by a quantified duration."
    },
    {
        "question": "We met some interesting people ___ a bus.",
        "options": ["A) on", "B) by", "C) in", "D) at"],
        "answer": "A",
        "explanation": "'On + article' is used for positioning aboard collective transports (on a bus)."
    },
    {
        "question": "He arrived ___ a taxi.",
        "options": ["A) by", "B) on", "C) in", "D) at"],
        "answer": "C",
        "explanation": "'In + article' is used for individual vehicles like a car or taxi."
    },
    {
        "question": "Most people go to the village ___ foot.",
        "options": ["A) on", "B) by", "C) with", "D) in"],
        "answer": "A",
        "explanation": "'On foot' is the correct exception instead of 'by foot'."
    },
    {
        "question": "He heavily depends ___ his parents.",
        "options": ["A) of", "B) from", "C) on", "D) to"],
        "answer": "C",
        "explanation": "'Depend on' is an idiomatic construction in English."
    },
    {
        "question": "Are you interested ___ modern art?",
        "options": ["A) on", "B) at", "C) in", "D) by"],
        "answer": "C",
        "explanation": "The correct idiomatic preposition is 'interested in'."
    },
    {
        "question": "He is really good ___ mathematics.",
        "options": ["A) at", "B) in", "C) on", "D) with"],
        "answer": "A",
        "explanation": "The idiomatic expression is 'good at'."
    },
    {
        "question": "She is terrified, she is afraid ___ the dark.",
        "options": ["A) from", "B) at", "C) of", "D) by"],
        "answer": "C",
        "explanation": "The correct expression is 'afraid of'."
    },
    {
        "question": "We are going on vacation ___ next week.",
        "options": ["A) on", "B) in", "C) at", "D) (no preposition)"],
        "answer": "D",
        "explanation": "No preposition is used before 'last', 'next', 'this', or 'every'."
    },
    {
        "question": "By the time the firemen arrived, the house ____ down.",
        "options": ["A) had burned", "B) burned", "C) has burned", "D) was burning"],
        "answer": "A",
        "explanation": "L'action s'est terminée avant une autre action au passé (past perfect)."
    },
    {
        "question": "Never before ____ such a spectacular sunset.",
        "options": ["A) I have seen", "B) have I seen", "C) I saw", "D) did I saw"],
        "answer": "B",
        "explanation": "Inversion obligatoire après 'Never' en début de phrase."
    },
    {
        "question": "If I ____ you, I would apply for that job.",
        "options": ["A) was", "B) am", "C) were", "D) had been"],
        "answer": "C",
        "explanation": "Conditionnel irréel du présent, on utilise toujours 'were' à toutes les personnes."
    },
    {
        "question": "PIÈGE: If he had caught the train yesterday, he ____ here right now.",
        "options": ["A) would be", "B) would have been", "C) will be", "D) had been"],
        "answer": "A",
        "explanation": "Mixed conditional: condition passée (Type 3) avec conséquence présente (Type 2, right now)."
    },
    {
        "question": "Not only ____ the exam, but she also got the highest score.",
        "options": ["A) she passed", "B) did she pass", "C) passed she", "D) she did pass"],
        "answer": "B",
        "explanation": "Inversion sujet/auxiliaire après 'Not only' en tête de phrase."
    },
    {
        "question": "It was in 1998 ____ he started his own company.",
        "options": ["A) when", "B) which", "C) that", "D) where"],
        "answer": "C",
        "explanation": "Cleft sentence : It is/was [élément souligné] THAT..."
    },
    {
        "question": "I am not used ____ up so early in the morning.",
        "options": ["A) to wake", "B) to waking", "C) waking", "D) wake"],
        "answer": "B",
        "explanation": "BE USED TO est suivi du gérondif (-ing). C'est une habitude actuelle."
    },
    {
        "question": "PIÈGE: He ____ smoke a lot, but he quit last year.",
        "options": ["A) is used to", "B) was used to", "C) used to", "D) would"],
        "answer": "C",
        "explanation": "Habitude révolue. 'Would' ne s'emploie pas ici car c'est un état/une habitude globale sans contexte de temps précis."
    },
    {
        "question": "Hardly had I left the building ____ it started to rain.",
        "options": ["A) than", "B) when", "C) that", "D) then"],
        "answer": "B",
        "explanation": "Corrélation: Hardly... when / No sooner... than."
    },
    {
        "question": "No sooner had we sat down to eat ____ the phone rang.",
        "options": ["A) than", "B) when", "C) that", "D) then"],
        "answer": "A",
        "explanation": "No sooner est suivi de 'than'."
    },
    {
        "question": "I suggest that he ____ a doctor immediately.",
        "options": ["A) sees", "B) see", "C) saw", "D) is seeing"],
        "answer": "B",
        "explanation": "Subjonctif présent en anglais après 'suggest', 'recommend', on utilise la base verbale."
    },
    {
        "question": "You ____ be tired after such a long journey! Go to bed.",
        "options": ["A) can", "B) must", "C) should", "D) ought to"],
        "answer": "B",
        "explanation": "Déduction forte / quasi-certitude (must)."
    },
    {
        "question": "He ____ have committed the crime; he was with me all day.",
        "options": ["A) mustn't", "B) shouldn't", "C) can't", "D) won't"],
        "answer": "C",
        "explanation": "La déduction négative passée se forme avec can't / couldn't + have + PP."
    },
    {
        "question": "PIÈGE: Even though the door was locked, he ____ open it.",
        "options": ["A) could", "B) was able to", "C) can", "D) might"],
        "answer": "B",
        "explanation": "Pour une réussite spécifique dans le passé (avec effort), on utilise 'was able to' ou 'managed to', pas 'could'."
    },
    {
        "question": "PIÈGE: I look forward ____ you next week.",
        "options": ["A) to see", "B) to seeing", "C) seeing", "D) for seeing"],
        "answer": "B",
        "explanation": "Le 'to' de 'look forward to' est une préposition, il est donc suivi d'un gérondif (-ing)."
    },
    {
        "question": "She didn't come to the party, ____ was a pity.",
        "options": ["A) what", "B) which", "C) that", "D) it"],
        "answer": "B",
        "explanation": "Le pronom relatif 'which' reprend l'ensemble de la proposition précédente."
    },
    {
        "question": "We have been living here ____ ten years.",
        "options": ["A) since", "B) for", "C) during", "D) ago"],
        "answer": "B",
        "explanation": "For + durée (ten years)."
    },
    {
        "question": "We have been living here ____ 2015.",
        "options": ["A) since", "B) for", "C) in", "D) from"],
        "answer": "A",
        "explanation": "Since + point de départ dans le temps."
    },
    {
        "question": "He usually travels ____ train, but today he came ____ foot.",
        "options": ["A) by / by", "B) on / on", "C) by / on", "D) with / by"],
        "answer": "C",
        "explanation": "By train (moyen de transport général) mais on foot (exception)."
    },
    {
        "question": "PIÈGE: They arrived ____ the airport at 9 PM.",
        "options": ["A) in", "B) at", "C) on", "D) to"],
        "answer": "B",
        "explanation": "On arrive AT un point précis (airport, station) et IN un pays/une ville."
    },
    {
        "question": "They arrived ____ Paris yesterday.",
        "options": ["A) at", "B) in", "C) on", "D) to"],
        "answer": "B",
        "explanation": "Arrive IN pour une ville ou un pays."
    },
    {
        "question": "PIÈGE: He was born ____ the 15th of August, ____ 1990.",
        "options": ["A) in / in", "B) on / in", "C) at / on", "D) on / on"],
        "answer": "B",
        "explanation": "ON devant un jour précis (15th August), IN devant une année."
    },
    {
        "question": "It's strange that she ____ be so rude.",
        "options": ["A) would", "B) should", "C) will", "D) can"],
        "answer": "B",
        "explanation": "Should d'appréciation après des adjectifs comme strange, surprising, odd."
    },
    {
        "question": "I ____ to work yesterday because it was a public holiday.",
        "options": ["A) didn't have to go", "B) mustn't go", "C) shouldn't go", "D) haven't to go"],
        "answer": "A",
        "explanation": "L'absence d'obligation au passé (have to). Mustn't exprime l'interdiction, pas l'absence d'obligation."
    },
    {
        "question": "The meeting will take place ____ Monday morning.",
        "options": ["A) in", "B) at", "C) on", "D) -"],
        "answer": "C",
        "explanation": "Dès qu'il y a un jour (Monday), la préposition est ON, même s'il est suivi de 'morning'."
    },
    {
        "question": "We are going ____ home after work.",
        "options": ["A) at", "B) to", "C) towards", "D) -"],
        "answer": "D",
        "explanation": "Pas de préposition 'to' avant 'home' avec des verbes de mouvement."
    },
    {
        "question": "PIÈGE: He works hard, ____?",
        "options": ["A) isn't he", "B) doesn't he", "C) don't he", "D) does he"],
        "answer": "B",
        "explanation": "Question tag avec un verbe d'action au présent régulier (works) nécessite l'auxiliaire do/does."
    },
    {
        "question": "Rarely ____ anyone in the office before 8 AM.",
        "options": ["A) I see", "B) see I", "C) do I see", "D) I do see"],
        "answer": "C",
        "explanation": "Inversion avec auxiliaire (do) après un adverbe de sens négatif (Rarely)."
    },
    {
        "question": "You had better ____ a doctor.",
        "options": ["A) to see", "B) see", "C) seeing", "D) saw"],
        "answer": "B",
        "explanation": "Had better est suivi de la base verbale sans 'to'."
    },
    {
        "question": "It's time we ____.",
        "options": ["A) leave", "B) left", "C) to leave", "D) are leaving"],
        "answer": "B",
        "explanation": "It's time / It's high time est suivi du prétérit modal (left)."
    },
    {
        "question": "PIÈGE: I remember ____ the door, but now it's open!",
        "options": ["A) to lock", "B) locking", "C) lock", "D) having lock"],
        "answer": "B",
        "explanation": "Remember + V-ing = se souvenir d'avoir fait qqch au passé."
    },
    {
        "question": "Don't forget ____ the door when you leave.",
        "options": ["A) to lock", "B) locking", "C) lock", "D) locked"],
        "answer": "A",
        "explanation": "Forget / Remember + To-V = penser/oublier de faire qqch (action future par rapport au moment de la pensée)."
    },
    {
        "question": "PIÈGE: Neither John nor his brothers ____ coming to the party.",
        "options": ["A) is", "B) are", "C) isn't", "D) aren't"],
        "answer": "B",
        "explanation": "Avec 'neither... nor', l'accord se fait avec le sujet le plus proche (his brothers = pluriel)."
    },
    {
        "question": "____ I open the window? It's hot in here.",
        "options": ["A) Will", "B) Shall", "C) Would", "D) Do"],
        "answer": "B",
        "explanation": "Pour faire une proposition ou demander un avis avec I ou WE, on utilise 'Shall'."
    },
    {
        "question": "The book ____ published next month.",
        "options": ["A) is to be", "B) is to", "C) will to be", "D) are being"],
        "answer": "A",
        "explanation": "BE + TO-V exprime un programme officiel, ici au passif 'is to be published'."
    },
    {
        "question": "PIÈGE: The committee ____ reached a decision.",
        "options": ["A) have", "B) has", "C) is", "D) are"],
        "answer": "B",
        "explanation": "En anglais américain, et généralement pour l'action du groupe uni, le collectif prend le singulier (has)."
    },
    {
        "question": "PIÈGE: The police ____ investigating the murder.",
        "options": ["A) is", "B) are", "C) has", "D) does"],
        "answer": "B",
        "explanation": "Le mot 'police' est toujours suivi d'un verbe au pluriel en anglais."
    },
    {
        "question": "I would rather you ____ me the truth yesterday.",
        "options": ["A) told", "B) had told", "C) tell", "D) have told"],
        "answer": "B",
        "explanation": "Would rather + sujet + past perfect pour un regret portant sur le passé."
    },
    {
        "question": "I would rather ____ at home tonight.",
        "options": ["A) to stay", "B) staying", "C) stay", "D) stayed"],
        "answer": "C",
        "explanation": "Would rather + base verbale sans 'to' quand les sujets sont identiques (I / stay)."
    },
    {
        "question": "If only I ____ richer!",
        "options": ["A) am", "B) would be", "C) were", "D) have been"],
        "answer": "C",
        "explanation": "If only s'emploie comme wish avec le prétérit modal (were)."
    },
    {
        "question": "Under no circumstances ____ open this box.",
        "options": ["A) you should", "B) should you", "C) you must", "D) can you to"],
        "answer": "B",
        "explanation": "Inversion après 'Under no circumstances' (adverbe restrictif/négatif en tête)."
    },
    {
        "question": "PIÈGE: What ____ when you saw him?",
        "options": ["A) did he do", "B) was he doing", "C) had he done", "D) has he done"],
        "answer": "B",
        "explanation": "Action en progression (past continuous) interrompue par une action brève (saw)."
    },
    {
        "question": "He told me he ____ call me the next day.",
        "options": ["A) will", "B) would", "C) shall", "D) can"],
        "answer": "B",
        "explanation": "Discours indirect au passé: 'will' devient 'would'."
    },
    {
        "question": "PIÈGE: If it ____ rain tomorrow, we will cancel the match.",
        "options": ["A) would", "B) will", "C) should", "D) might"],
        "answer": "C",
        "explanation": "If it should rain = S'il venait à pleuvoir (probabilité faible mais Type 1)."
    },
    {
        "question": "I DO ____ you, believe me!",
        "options": ["A) to love", "B) loving", "C) love", "D) loved"],
        "answer": "C",
        "explanation": "Emphatic DO: suivi de la base verbale pour insister."
    },
    {
        "question": "The CEO, along with his managers, ____ expected to attend.",
        "options": ["A) are", "B) is", "C) were", "D) have been"],
        "answer": "B",
        "explanation": "Le sujet est The CEO. 'along with...' est une parenthèse, donc le verbe est au singulier."
    },
    {
        "question": "By this time next year, I ____ my studies.",
        "options": ["A) will finish", "B) finish", "C) will have finished", "D) have finished"],
        "answer": "C",
        "explanation": "Future perfect (will have + PP) avec une date butoir (By this time)."
    },
    {
        "question": "PIÈGE: It's the first time I ____ this movie.",
        "options": ["A) watch", "B) am watching", "C) watched", "D) have watched"],
        "answer": "D",
        "explanation": "Après 'It's the first time', on utilise TOUJOURS le present perfect."
    },
    {
        "question": "I object to ____ like a child.",
        "options": ["A) be treated", "B) being treated", "C) treat", "D) treating"],
        "answer": "B",
        "explanation": "Object to + V-ing, ici à la forme passive 'being treated'."
    },
    {
        "question": "____ you need any help, please contact the manager.",
        "options": ["A) Would", "B) Could", "C) Should", "D) If only"],
        "answer": "C",
        "explanation": "Inversion de la conditionnelle Type 1: 'Should you need...' = 'If you should need...'."
    },
]

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
        "question": "Quel est le rôle du Défenseur des droits ?",
        "options": ["A) Il défend la France devant les juridictions internationales", "B) Il protège les droits fondamentaux des citoyens face aux administrations", "C) Il gère le budget de l'État", "D) Il nomme les juges"],
        "answer": "B",
        "explanation": "Le Défenseur des droits veille au respect des droits et libertés des citoyens face aux administrations."
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
        "explanation": "L'?tat civil enregistre les ??v?nements majeurs de la vie (naissances, mariages, d?c?s) et ?tablit l'identit? juridique."
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
        "question": "Qu'est-ce que le Parlement ivoirien en matière de contrôle du gouvernement ?",
        "options": ["A) Il ne dispose d'aucun pouvoir de contrôle", "B) Il exerce un contrôle par les questions orales et écrites, commissions d'enquête et motion de censure", "C) Il peut dissoudre le gouvernement à tout moment", "D) Il peut refuser d'appliquer les lois présidentielles"],
        "answer": "B",
        "explanation": "Le Parlement ivoirien contrôle le gouvernement par les questions, les commissions et la motion de censure."
    },
    {
        "question": "Quel est le principe de la neutralité du service public ?",
        "options": ["A) Le service public doit être gratuit", "B) Le service public ne doit pas être influencé par des considérations politiques, religieuses ou idéologiques", "C) Le service public ne peut pas sous-traiter", "D) Le service public doit être géré par des fonctionnaires uniquement"],
        "answer": "B",
        "explanation": "La neutralité du service public garantit que les agents traitent tous les usagers de façon égale sans discrimination."
    },
    {
        "question": "Piège : un fonctionnaire peut-il militer pour un parti politique en CI ?",
        "options": ["A) Oui totalement sans restriction", "B) Non, un fonctionnaire doit se garder de tout engagement politique ostensible dans l'exercice de ses fonctions", "C) Oui, mais uniquement après les heures de service", "D) Non, aucun fonctionnaire ne peut voter"],
        "answer": "B",
        "explanation": "Le devoir de réserve interdit au fonctionnaire de manifester ostensiblement ses opinions politiques dans l'exercice de ses fonctions."
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
        "question": "Qu'est-ce que le principe de neutralité religieuse dans la fonction publique ivoirienne ?",
        "options": ["A) Les fonctionnaires ne peuvent pas pratiquer une religion", "B) Les fonctionnaires ne peuvent pas manifester leurs convictions religieuses dans l'exercice de leurs fonctions", "C) Les fonctionnaires doivent être athées", "D) La religion est interdite dans les locaux administratifs"],
        "answer": "B",
        "explanation": "La neutralité religieuse interdit aux fonctionnaires d'exprimer leurs convictions religieuses dans l'exercice de leurs fonctions."
    },
    {
        "question": "Qu'est-ce que le principe de gratuité du service public ?",
        "options": ["A) Tous les services publics sont gratuits", "B) Ce principe signifie que le financement du service public ne doit pas reposer uniquement sur les usagers : il peut être financé par les impôts", "C) Les usagers ne paient jamais pour les services publics", "D) Les fonctionnaires travaillent bénévolement"],
        "answer": "B",
        "explanation": "La gratuité du service public ne signifie pas absence de paiement, mais que le service est accessible sans que le prix soit un obstacle dirimant."
    },
    {
        "question": "Quelle est la distinction entre le préfet et le gouverneur en CI ?",
        "options": ["A) Aucune différence", "B) En CI, depuis 2011, le gouverneur dirige le district autonome (Abidjan, Yamoussoukro) tandis que le préfet dirige le département", "C) Le gouverneur est un rôle historique supprimé", "D) Le gouverneur est élu ; le préfet est nommé"],
        "answer": "B",
        "explanation": "La Constitution de 2011-2016 a créé des districts autonomes dirigés par des gouverneurs nommés par le Président pour les grandes agglomérations."
    },
    {
        "question": "Qu'est-ce que la délégation de signature ?",
        "options": ["A) Un fonctionnaire signe à la place d'un autre sans habilitation", "B) Une autorité administrative autorise un de ses subordonnés à signer en son nom certains actes", "C) Le Président délègue ses pouvoirs au Premier ministre", "D) L'Assemblée nationale délègue ses pouvoirs au gouvernement"],
        "answer": "B",
        "explanation": "La délégation de signature permet à un chef de service d'autoriser son subordonné à signer certains actes en son nom. Le délégant reste responsable."
    },
    {
        "question": "Piège : la délégation de pouvoirs est-elle différente de la délégation de signature ?",
        "options": ["A) Non, ce sont des synonymes", "B) Oui : dans la délégation de pouvoirs le délégataire exerce le pouvoir en son nom propre et le délégant ne peut plus l'exercer ; dans la délégation de signature le délégant reste responsable", "C) Oui : la délégation de pouvoirs est illégale", "D) Non, elles ont les mêmes effets juridiques"],
        "answer": "B",
        "explanation": "Délégation de pouvoirs : transfert du pouvoir lui-même (le délégant ne peut plus exercer). Délégation de signature : seule la signature est transférée, le délégant reste responsable."
    },
    {
        "question": "Quelle est la différence entre la tutelle administrative et la hiérarchie administrative ?",
        "options": ["A) Aucune différence", "B) La tutelle ne permet que des contrôles de légalité et d'opportunité définis par la loi ; la hiérarchie permet un pouvoir de commandement direct", "C) La hiérarchie s'exerce entre collectivités", "D) La tutelle est plus puissante que la hiérarchie"],
        "answer": "B",
        "explanation": "La hiérarchie = pouvoir de commandement direct. La tutelle = contrôle externe, encadré par la loi."
    },
    {
        "question": "Qu'est-ce que le principe de la légalité des délits et des peines ?",
        "options": ["A) Les peines sont fixées par le juge librement", "B) Nul ne peut être puni pour un acte qui n'est pas prévu et puni par la loi au moment où il a été commis", "C) Les délits sont définis par le gouvernement", "D) La loi pénale s'applique rétroactivement"],
        "answer": "B",
        "explanation": "« Nullum crimen, nulla poena sine lege » : principe fondamental du droit pénal et constitutionnel."
    },
    {
        "question": "Quel est le droit de pétition en Côte d'Ivoire ?",
        "options": ["A) Le droit de faire une requête à l'administration", "B) Le droit pour les citoyens d'adresser des demandes écrites aux autorités publiques", "C) Le droit de manifester", "D) Le droit de vote"],
        "answer": "B",
        "explanation": "Le droit de pétition permet aux citoyens d'adresser des demandes collectives ou individuelles aux pouvoirs publics."
    },
    {
        "question": "Quelle est la différence entre le droit privé et le droit public ?",
        "options": ["A) Aucune différence", "B) Le droit public régit les relations entre l'État et les particuliers ; le droit privé régit les relations entre particuliers", "C) Le droit privé est plus important", "D) Le droit public ne s'applique pas aux citoyens"],
        "answer": "B",
        "explanation": "Droit public = État / personnes publiques. Droit privé = relations entre personnes privées."
    },
    {
        "question": "Qu'est-ce que le principe de l'accès à la justice en Côte d'Ivoire ?",
        "options": ["A) Seuls les riches ont accès à la justice", "B) Tout citoyen a le droit de soumettre un litige à un tribunal et de bénéficier d'un procès équitable", "C) La justice est réservée aux fonctionnaires", "D) Les étrangers n'ont pas accès à la justice"],
        "answer": "B",
        "explanation": "L'accès à la justice est un droit fondamental : tout citoyen peut saisir un tribunal et bénéficier d'un procès équitable."
    },
    {
        "question": "Qu'est-ce que la déclaration d'utilité publique (DUP) en CI ?",
        "options": ["A) Un décret qui nationalise une entreprise", "B) Un acte administratif qui reconnaît l'intérêt général d'un projet et autorise l'expropriation si nécessaire", "C) Un document d'inscription d'une association", "D) Un permis de construire"],
        "answer": "B",
        "explanation": "La DUP est la condition préalable à toute expropriation en droit ivoirien."
    },
    {
        "question": "Quel est le rôle du Sénat dans la procédure législative en Côte d'Ivoire ?",
        "options": ["A) Voter le budget national", "B) Examiner et amender les textes de loi adoptés par l'Assemblée nationale", "C) Nommer les juges", "D) Déclarer la guerre"],
        "answer": "B",
        "explanation": "Le Sénat ivoirien examine les lois, propose des amendements, mais l'Assemblée nationale a le dernier mot."
    },
    {
        "question": "Quelle est la composition du Sénat de Côte d'Ivoire selon la Constitution de 2016 ?",
        "options": ["A) Entièrement élu au suffrage direct", "B) 2/3 élus et 1/3 nommés par le Président", "C) Entièrement nommé par le Président", "D) Moitié élus, moitié tirés au sort"],
        "answer": "B",
        "explanation": "Le Sénat ivoirien : 2/3 des membres sont élus, 1/3 sont nommés par le Président de la République."
    },
    {
        "question": "Qu'est-ce que le droit à la sécurité sociale en Côte d'Ivoire ?",
        "options": ["A) Le droit d'être armé", "B) Le droit de tout citoyen à des prestations sociales en cas de maladie, vieillesse, maternité ou accident du travail", "C) Le droit à une police privée", "D) Un droit réservé aux fonctionnaires"],
        "answer": "B",
        "explanation": "La sécurité sociale garantit des protections aux travailleurs : gérée par la CNPS en Côte d'Ivoire."
    },
    {
        "question": "Qu'est-ce que le principe d'inamovibilité des magistrats du siège en CI ?",
        "options": ["A) Ils ne peuvent pas être mutés sans leur accord ou procédure disciplinaire", "B) Ils peuvent être révoqués à tout moment", "C) Ils sont nommés à vie sans possibilité de départ", "D) Ils ne peuvent pas prendre de congés"],
        "answer": "A",
        "explanation": "L'inamovibilité protège l'indépendance des magistrats du siège contre les pressions politiques."
    },
    {
        "question": "Quel est l'âge minimum pour être élu député à l'Assemblée nationale en Côte d'Ivoire ?",
        "options": ["A) 18 ans", "B) 25 ans", "C) 30 ans", "D) 35 ans"],
        "answer": "B",
        "explanation": "En Côte d'Ivoire, il faut avoir au moins 25 ans pour être candidat à l'Assemblée nationale."
    },
    {
        "question": "Qu'est-ce que la responsabilité civile extracontractuelle (délictuelle) ?",
        "options": ["A) La responsabilité née d'un contrat", "B) La responsabilité pour un dommage causé sans relation contractuelle préalable (accident, faute)", "C) La responsabilité pénale", "D) La responsabilité de l'État uniquement"],
        "answer": "B",
        "explanation": "La responsabilité délictuelle (art. 1382 CC français, code ivoirien) s'applique hors contrat : faute → dommage → réparation."
    },
    {
        "question": "Qu'est-ce que le droit de grève dans la fonction publique ivoirienne ?",
        "options": ["A) Il est totalement interdit", "B) Il est reconnu mais encadré : certains agents ne peuvent y recourir (forces de l'ordre) et un préavis est obligatoire", "C) Il est illimité", "D) Il est réservé aux agents de catégorie A"],
        "answer": "B",
        "explanation": "Le droit de grève existe dans la fonction publique mais il est encadré : préavis, services minimum, interdiction pour certains corps."
    },
    {
        "question": "Qu'est-ce que le principe de continuité du service public en CI ?",
        "options": ["A) Les services publics ne ferment jamais", "B) Les services publics essentiels doivent fonctionner de manière continue sans interruption injustifiée", "C) Les fonctionnaires ne peuvent pas prendre de congés", "D) Les marchés publics doivent être renouvelés annuellement"],
        "answer": "B",
        "explanation": "La continuité est une des lois de Rolland : les services publics ne doivent pas connaître d'interruptions injustifiées."
    },
    {
        "question": "Quel est le principe de sincérité budgétaire en CI ?",
        "options": ["A) Le budget doit être présenté honnêtement, sans sous-estimation des recettes ni surestimation des dépenses", "B) Le budget doit être voté à l'unanimité", "C) Le budget doit être équilibré", "D) Le budget ne peut pas être modifié en cours d'année"],
        "answer": "A",
        "explanation": "La sincérité budgétaire exige que les prévisions de recettes et de dépenses soient aussi précises et honnêtes que possible."
    },
    {
        "question": "Qu'est-ce que le Conseil Économique, Social, Environnemental et Culturel (CESEC) de CI ?",
        "options": ["A) Un organe exécutif", "B) Une assemblée consultative qui émet des avis sur les questions économiques, sociales, environnementales et culturelles", "C) Un tribunal spécialisé", "D) Un organe législatif de remplacement"],
        "answer": "B",
        "explanation": "Le CESEC est une institution consultative : le gouvernement peut le consulter mais n'est pas obligé de suivre ses avis."
    },
    {
        "question": "Qu'est-ce que le droit de propriété en CI ?",
        "options": ["A) Un droit absolu sans aucune restriction", "B) Un droit fondamental garanti par la Constitution, mais susceptible de limitations pour cause d'utilité publique avec indemnisation juste", "C) Un droit réservé aux nationaux ivoiriens", "D) Un droit qui disparaît à la mort du propriétaire"],
        "answer": "B",
        "explanation": "Le droit de propriété est garanti par la Constitution mais peut être limité par l'expropriation pour utilité publique, moyennant indemnisation."
    },
    {
        "question": "Qu'est-ce qu'une loi de finances en Côte d'Ivoire ?",
        "options": ["A) Une loi fiscale ordinaire", "B) La loi qui autorise, pour l'année, la perception des ressources de l'État et fixe les dépenses publiques", "C) Une loi sur les finances des collectivités locales", "D) Une loi sur les investissements étrangers"],
        "answer": "B",
        "explanation": "La loi de finances (budget de l'État) est votée annuellement par le Parlement et encadrée par la LOLF."
    },
    {
        "question": "Quelle est la durée du mandat sénatorial en Côte d'Ivoire ?",
        "options": ["A) 4 ans", "B) 5 ans", "C) 6 ans", "D) 7 ans"],
        "answer": "C",
        "explanation": "En Côte d'Ivoire, les sénateurs sont élus ou nommés pour 6 ans, renouvelables par moitié tous les 3 ans."
    },
    {
        "question": "Qu'est-ce que la décentralisation fiscale en CI ?",
        "options": ["A) L'État perçoit tous les impôts pour les redistribuer", "B) Le transfert aux collectivités territoriales du pouvoir de lever certains impôts locaux pour financer leurs compétences", "C) La suppression des impôts nationaux", "D) La gestion par les banques des impôts locaux"],
        "answer": "B",
        "explanation": "La décentralisation fiscale donne aux collectivités le pouvoir de lever des impôts locaux pour financer leurs activités."
    },
    {
        "question": "Quel est le rôle du Gouverneur dans un district autonome en Côte d'Ivoire ?",
        "options": ["A) Il est élu par les habitants du district", "B) Il est nommé par le Président et représente l'État tout en gérant le district autonome", "C) Il est nommé par le Parlement", "D) Il est choisi par le Conseil municipal"],
        "answer": "B",
        "explanation": "Le Gouverneur d'un district autonome (Abidjan, Yamoussoukro) est nommé par le Président de la République."
    },
    {
        "question": "Qu'est-ce que l'égalité des citoyens devant les charges publiques ?",
        "options": ["A) Tous les citoyens paient le même montant d'impôts", "B) Les charges publiques (impôts, obligations) doivent être réparties équitablement selon les capacités", "C) L'État ne peut pas imposer de charges aux citoyens", "D) Seuls les fonctionnaires contribuent aux charges publiques"],
        "answer": "B",
        "explanation": "Ce principe constitutionnel garantit une répartition équitable des charges fiscales et non-fiscales."
    },
    {
        "question": "Quelle institution ivoirienne protège les droits des consommateurs ?",
        "options": ["A) Le CESEC", "B) La Direction de la Protection du Consommateur et de la Concurrence (DPCC)", "C) La Cour Suprême", "D) L'Assemblée nationale"],
        "answer": "B",
        "explanation": "La DPCC est l'organe administratif chargé de surveiller les pratiques commerciales et protéger les consommateurs en CI."
    },
    {
        "question": "Qu'est-ce que le Conseil National des Droits de l'Homme (CNDH) de CI ?",
        "options": ["A) Un tribunal", "B) Une institution indépendante chargée de promouvoir et protéger les droits de l'homme en CI", "C) Un ministère", "D) Un organe de l'ONU en CI"],
        "answer": "B",
        "explanation": "Le CNDH est une institution nationale indépendante qui surveille le respect des droits humains et formule des recommandations."
    },
    {
        "question": "Quel est le principe d'impartialité dans le service public ivoirien ?",
        "options": ["A) Les agents peuvent favoriser leurs proches", "B) Les agents doivent traiter tous les usagers sans discrimination ni favoritisme", "C) L'administration n'a pas d'opinion officielle", "D) Les agents ne peuvent pas avoir d'opinions politiques"],
        "answer": "B",
        "explanation": "L'impartialité oblige les agents publics à traiter tous les usagers de manière égale, sans discrimination."
    },
    {
        "question": "Qu'est-ce que le contrôle de gestion dans l'administration publique ivoirienne ?",
        "options": ["A) Le contrôle policier des fonctionnaires", "B) L'ensemble des processus qui permettent de maîtriser les ressources et d'atteindre les objectifs fixés", "C) L'audit externe uniquement", "D) Le contrôle exercé par le Parlement sur les ministères"],
        "answer": "B",
        "explanation": "Le contrôle de gestion est un outil interne de pilotage de la performance dans l'administration."
    },
    {
        "question": "Qu'est-ce que le principe de laïcité en Côte d'Ivoire ?",
        "options": ["A) L'État impose le christianisme", "B) L'État est neutre religieusement et garantit la liberté de conscience et de culte", "C) Les religions sont interdites dans l'espace public", "D) L'État subventionne toutes les religions"],
        "answer": "B",
        "explanation": "La Constitution ivoirienne garantit la liberté de conscience et la neutralité religieuse de l'État."
    },
    {
        "question": "Qu'est-ce que le droit à l'éducation en Côte d'Ivoire ?",
        "options": ["A) Un droit privé facultatif", "B) Un droit fondamental garanti par la Constitution : l'enseignement de base est obligatoire et gratuit", "C) Un droit réservé aux enfants des fonctionnaires", "D) Un droit qui s'achète"],
        "answer": "B",
        "explanation": "La Constitution ivoirienne garantit le droit à l'éducation ; l'enseignement primaire est obligatoire."
    },
    {
        "question": "Qu'est-ce que le système de l'État unitaire décentralisé adopté par la CI ?",
        "options": ["A) Un État fédéral avec des États autonomes", "B) Un État unique avec des collectivités locales dotées de compétences et d'autonomie propres", "C) Un État sans niveaux de gouvernement locaux", "D) Un État où les régions ont leur propre constitution"],
        "answer": "B",
        "explanation": "La CI est un État unitaire décentralisé : une seule loi nationale mais des collectivités locales autonomes dans leurs domaines."
    },
    {
        "question": "Qu'est-ce que le Fonds de Développement de la Formation Professionnelle (FDFP) en CI ?",
        "options": ["A) Un fonds pour les investissements étrangers", "B) Un organisme paritaire qui finance la formation professionnelle des salariés du secteur privé", "C) Un fonds pour les retraites des fonctionnaires", "D) Une caisse d'assurance maladie"],
        "answer": "B",
        "explanation": "Le FDFP collecte les taxes de formation professionnelle et finance les actions de formation dans le secteur privé ivoirien."
    },
    {
        "question": "Sous la 3ème République ivoirienne (depuis 2016), le mandat du Président de la République est-il renouvelable ?",
        "options": ["A) Oui, indéfiniment", "B) Oui, une seule fois consécutivement", "C) Non, il est unique", "D) Oui, deux fois"],
        "answer": "B",
        "explanation": "Selon la Constitution de 2016, le mandat est de 5 ans renouvelable une seule fois."
    },
    {
        "question": "Qui assure l'intérim en cas de vacance de la Présidence de la République selon la Constitution de 2016 modifiée en 2020 ?",
        "options": ["A) Le Président de l'Assemblée Nationale", "B) Le Vice-Président de la République", "C) Le Premier Ministre", "D) Le Président du Sénat"],
        "answer": "B",
        "explanation": "Le Vice-Président de la République devient Président de plein droit en cas de vacance."
    },
    {
        "question": "Combien de membres composent le Conseil Constitutionnel de la Côte d'Ivoire ?",
        "options": ["A) 7 membres", "B) 9 membres", "C) 11 membres", "D) 15 membres"],
        "answer": "A",
        "explanation": "Le Conseil Constitutionnel comprend un Président et six (6) conseillers, soit 7 membres au total."
    },
    {
        "question": "Quelle est l'institution ivoirienne chargée de la régulation de la communication audiovisuelle ?",
        "options": ["A) La HACA", "B) Le CNP", "C) L'ANP", "D) L'ARTCI"],
        "answer": "A",
        "explanation": "La Haute Autorité de la Communication Audiovisuelle (HACA) régule le secteur audiovisuel."
    },
    {
        "question": "Le Sénat ivoirien a été mis en place pour la première fois en quelle année ?",
        "options": ["A) 1990", "B) 2000", "C) 2016", "D) 2018"],
        "answer": "D",
        "explanation": "Prévu par la Constitution de 2016, le Sénat a été installé officiellement en 2018."
    },
    {
        "question": "Qui préside le CSM en CI ?",
        "options": ["A) Ministre Justice", "B) Pt Cour Cassation", "C) Président République", "D) Pt Cons Constit"],
        "answer": "C",
        "explanation": "Le Président de la République préside le CSM."
    },
    {
        "question": "Pilier PND 2021-2025 modernisant l'Etat ?",
        "options": ["A) Pilier 2", "B) Pilier 4", "C) Pilier 6", "D) Pilier 1"],
        "answer": "C",
        "explanation": "Pilier 6 : Gouvernance et modernisation."
    },
    {
        "question": "Mandat Médiateur de la République ?",
        "options": ["A) 4 ans renouv", "B) 5 ans non renouv", "C) 6 ans non renouv", "D) 6 ans renouv"],
        "answer": "C",
        "explanation": "6 ans non renouvelable."
    },
    {
        "question": "Organe régulant marchés publics ?",
        "options": ["A) ANRMP", "B) ARCOP", "C) Cour Comptes", "D) BNETD"],
        "answer": "B",
        "explanation": "ARCOP a remplacé l'ANRMP."
    },
    {
        "question": "Successeur PR en cas de vacance ?",
        "options": ["A) Pt AN", "B) Vice-Président", "C) Premier Ministre", "D) Pt Sénat"],
        "answer": "B",
        "explanation": "Le Vice-Président de la République."
    },
    {
        "question": "Nombre conseillers Conseil Constit (hors ex-PR) ?",
        "options": ["A) 7", "B) 6", "C) 9", "D) 5"],
        "answer": "B",
        "explanation": "1 Président et 6 Conseillers."
    },
    {
        "question": "Composition Sénat ivoirien ?",
        "options": ["A) 100% élus", "B) 2/3 élus, 1/3 nommés", "C) 50% élus", "D) 100% nommés"],
        "answer": "B",
        "explanation": "2/3 élus, 1/3 nommé par le PR."
    },
    {
        "question": "Collectivités territoriales actuelles ?",
        "options": ["A) Région/Commune", "B) District/Commune", "C) Département/Commune", "D) Village/Région"],
        "answer": "A",
        "explanation": "Région et Commune (Loi d'organisation)."
    },
    {
        "question": "Qui peut dissoudre l'AN ?",
        "options": ["A) Cons Constit", "B) Premier Ministre", "C) Président Rép", "D) Vice-Président"],
        "answer": "C",
        "explanation": "Le Président de la République."
    },
    {
        "question": "Juridiction non suprême depuis 2016 ?",
        "options": ["A) Cour Cassation", "B) Conseil Etat", "C) Cour d'Appel", "D) Cour Comptes"],
        "answer": "C",
        "explanation": "La Cour d'Appel est du second degré."
    },
    {
        "question": "Initiative des lois ?",
        "options": ["A) PR et Députés", "B) PR, Députés et Sénateurs", "C) Gouv seul", "D) Parlement seul"],
        "answer": "B",
        "explanation": "Concurremment PR, Députés, Sénateurs."
    },
    {
        "question": "Age minimum présidentielle (révision) ?",
        "options": ["A) 40 ans", "B) 35 ans", "C) 45 ans", "D) 30 ans"],
        "answer": "B",
        "explanation": "35 ans minimum."
    },
    {
        "question": "Mandat Députés ?",
        "options": ["A) 4 ans", "B) 5 ans", "C) 6 ans", "D) 7 ans"],
        "answer": "B",
        "explanation": "5 ans."
    },
    {
        "question": "Rôle de la HABG ?",
        "options": ["A) Elections", "B) Lutte corruption", "C) Médias", "D) Lois"],
        "answer": "B",
        "explanation": "Haute Autorité pour la Bonne Gouvernance (Anti-corruption)."
    },
    {
        "question": "Loi organique adoptée à :",
        "options": ["A) Maj relative", "B) Maj absolue", "C) Maj 2/3", "D) Unanimité"],
        "answer": "B",
        "explanation": "Majorité absolue des membres de chaque chambre."
    },
    {
        "question": "Acte signé par le PR ?",
        "options": ["A) Arrêté", "B) Circulaire", "C) Décret Conseil Min", "D) Ordonnance locale"],
        "answer": "C",
        "explanation": "Décrets et ordonnances en Conseil des Ministres."
    },
    {
        "question": "Naturalisation accordée par :",
        "options": ["A) Juge", "B) Arrêté Min", "C) Décret PR", "D) Loi Parl"],
        "answer": "C",
        "explanation": "Décret présidentiel."
    },
    {
        "question": "Prorogation état de siège > 15j ?",
        "options": ["A) Cons Constit", "B) Parlement", "C) CSM", "D) Min Défense"],
        "answer": "B",
        "explanation": "Parlement l'autorise."
    },
    {
        "question": "Régulateur com audiovisuelle ?",
        "options": ["A) HACA", "B) ANP", "C) CNCA", "D) RTI"],
        "answer": "A",
        "explanation": "Haute Autorité de la Com Audiovisuelle."
    },
    {
        "question": "Principe non constitutionnel CI ?",
        "options": ["A) Laïcité", "B) Décentralisation", "C) Droit grève", "D) Peine de mort"],
        "answer": "D",
        "explanation": "Peine de mort abolie."
    },
    {
        "question": "Membres du CESEC appelés :",
        "options": ["A) Députés", "B) Conseillers", "C) Sénateurs", "D) Vénérables"],
        "answer": "B",
        "explanation": "Conseillers."
    },
    {
        "question": "Président CEI est :",
        "options": ["A) Nommé AN", "B) Élu par CEI", "C) Nommé Cons Constit", "D) Nommé PR seul"],
        "answer": "B",
        "explanation": "Élu par les commissaires centraux."
    },
    {
        "question": "Impôt revenu foncier (IRF) ?",
        "options": ["A) Terrains nus", "B) Loyers bâtis", "C) Achats", "D) Successions"],
        "answer": "B",
        "explanation": "Taxes sur revenus locatifs."
    },
    {
        "question": "Contrôle financier a posteriori ?",
        "options": ["A) IGF", "B) Trésor", "C) Cour Comptes", "D) Cons Constit"],
        "answer": "C",
        "explanation": "La Cour des Comptes vérifie l'exécution budgétaire."
    },
    {
        "question": "Révocation requiert avis :",
        "options": ["A) Conseil discipline", "B) Conseil Min", "C) Conseil Etat", "D) Min Tutelle"],
        "answer": "A",
        "explanation": "Le Conseil de discipline pour sanction du 2nd degré."
    },
    {
        "question": "Saisine Cons Constit (par parlementaires) ?",
        "options": ["A) Tout citoyen", "B) 1/10 membres", "C) Premier Min", "D) Bâtonnier"],
        "answer": "B",
        "explanation": "1/10 des députés ou sénateurs."
    },
    {
        "question": "Pouvoirs exceptionnels (Art 73) si :",
        "options": ["A) Menace grave + Interruption instit", "B) Baisse PIB", "C) Grève", "D) Rejet budget"],
        "answer": "A",
        "explanation": "Conditions très strictes de menace sur l'Etat."
    },
    {
        "question": "Révision constitutionnelle via Parlement ?",
        "options": ["A) Refus total", "B) Vote Congrès 2/3", "C) Décret", "D) Cour Cassation"],
        "answer": "B",
        "explanation": "Adoptée par 2/3 du Congrès réuni."
    },
    {
        "question": "Contreseing décrets PR ?",
        "options": ["A) Aucun", "B) PM et Ministres", "C) Pt Sénat", "D) SGG"],
        "answer": "B",
        "explanation": "PM et ministres concernés (hors pouvoirs propres)."
    },
    {
        "question": "Chambre Rois/Chefs reconnue en :",
        "options": ["A) 1960", "B) 2000", "C) 2016", "D) 2020"],
        "answer": "C",
        "explanation": "Constitution de la IIIe République (2016)."
    },
    {
        "question": "Citoyenneté active ?",
        "options": ["A) Nationalité pure", "B) Respect lois", "C) Participation civique", "D) Impôts"],
        "answer": "C",
        "explanation": "Participation active aux affaires de la cité."
    },
    {
        "question": "Droit du sol CI ?",
        "options": ["A) 5 ans", "B) 10 ans", "C) Non automatique", "D) 2 ans"],
        "answer": "C",
        "explanation": "Droit du sol pur supprimé (Code nationalité 1972)."
    },
    {
        "question": "Service militaire en CI ?",
        "options": ["A) Obligatoire 18a", "B) Devoir encadré", "C) Supprimé", "D) Pour hommes"],
        "answer": "B",
        "explanation": "Devoir civique, bien que non strictement universel en pratique."
    },
    {
        "question": "Egalité garantie par Article :",
        "options": ["A) 1", "B) 4", "C) 10", "D) Préambule"],
        "answer": "B",
        "explanation": "Article 4 de la Constitution 2016."
    },
    {
        "question": "CDH a remplacé :",
        "options": ["A) CNDHCI", "B) FIDH", "C) MIDH", "D) LIDHO"],
        "answer": "A",
        "explanation": "CNDH a remplacé la CNDHCI."
    },
    {
        "question": "Défend l'Etat en justice ?",
        "options": ["A) Procureur", "B) Agent Judiciaire Trésor", "C) Bâtonnier", "D) Avocat Gal"],
        "answer": "B",
        "explanation": "L'AJT."
    },
    {
        "question": "Emblèmes République CI ?",
        "options": ["A) Drapeau Hymne Armoiries", "B) Devise Drapeau Hymne", "C) Drapeau Hymne Armoiries Devise", "D) PR Drapeau"],
        "answer": "C",
        "explanation": "Les 4 emblèmes constitutionnels."
    },
    {
        "question": "Budget adopté par :",
        "options": ["A) Loi habilitation", "B) Loi organique", "C) Loi finances", "D) Ordonnance"],
        "answer": "C",
        "explanation": "Loi de finances."
    },
    {
        "question": "Inspecteur Etat dépend de :",
        "options": ["A) PM", "B) PR", "C) Cour Comptes", "D) Min Eco"],
        "answer": "B",
        "explanation": "L'IGE est rattachée à la Présidence."
    },
    {
        "question": "Désaccord AN / Sénat sur loi :",
        "options": ["A) Abandon", "B) AN décide", "C) Sénat décide", "D) Com Mixte Paritaire"],
        "answer": "D",
        "explanation": "Le Gouv convoque la CMP."
    },
    {
        "question": "Le vote en CI est :",
        "options": ["A) Droit+Devoir", "B) Pénal", "C) Privilège", "D) Civil"],
        "answer": "A",
        "explanation": "Droit et devoir civique non pénalement sanctionné."
    },
    {
        "question": "Condition formation partis ?",
        "options": ["A) Respect Chef", "B) <10 ans", "C) Respect Rép/Souveraineté", "D) Sièges région"],
        "answer": "C",
        "explanation": "Respect des principes démocratiques et de la souveraineté."
    },
    {
        "question": "Délibérations Conseil Ministres ?",
        "options": ["A) Publiques", "B) Secrètes", "C) JO complet", "D) Direct TV"],
        "answer": "B",
        "explanation": "Le secret des délibérations est la règle."
    },
    {
        "question": "Mariage relève du domaine de :",
        "options": ["A) Loi ordinaire", "B) Constitution", "C) Décret", "D) Coutume"],
        "answer": "A",
        "explanation": "Etat des personnes = loi (Code civil)."
    },
    {
        "question": "Limite âge max PR (2020) ?",
        "options": ["A) 75 ans", "B) 80 ans", "C) Aucune", "D) 70 ans"],
        "answer": "C",
        "explanation": "La limite de 75 ans a sauté en 2016."
    },
    {
        "question": "Ordre national dirigé par :",
        "options": ["A) Min Intérieur", "B) Grand Chancelier", "C) Pt Sénat", "D) Archevêque"],
        "answer": "B",
        "explanation": "Le Grand Chancelier de l'Ordre."
    },
    {
        "question": "Mandat arrêt député (session) ?",
        "options": ["A) Accord Pt AN", "B) Accord Bureau AN", "C) Plénière", "D) Aucun"],
        "answer": "B",
        "explanation": "Le Bureau de l'AN lève l'immunité/autorise l'arrestation."
    },
    {
        "question": "Création Conseil Entente ?",
        "options": ["A) 1959", "B) 1960", "C) 1973", "D) 1975"],
        "answer": "A",
        "explanation": "Mai 1959."
    },
    {
        "question": "Femme étrangère épouse ivoirien :",
        "options": ["A) Direct", "B) Déclaration (après délai)", "C) Naturalisation 5a", "D) Impossible"],
        "answer": "B",
        "explanation": "Acquisition par déclaration possible après un délai légal."
    },
    {
        "question": "Mandat conseiller régional ?",
        "options": ["A) 4 ans", "B) 5 ans", "C) 6 ans", "D) 7 ans"],
        "answer": "B",
        "explanation": "Les mandats locaux durent 5 ans."
    },
    {
        "question": "Selon la Constitution ivoirienne de 2016 (modifiée en 2020), le pouvoir exécutif est :",
        "options": ["A) Monocéphale", "B) Bicéphale (Président de la République et Vice-Président)", "C) Collégial", "D) Exercé exclusivement par le Premier Ministre"],
        "answer": "B",
        "explanation": "L'exécutif est bicéphale, partagé entre le Président de la République et le Vice-Président (et le Premier ministre)."
    },
    {
        "question": "Qui fut le premier Président du Sénat ivoirien institué par la Constitution de 2016 ?",
        "options": ["A) Tiemoko Meyliet Koné", "B) Jeannot Ahoussou Kouadio", "C) Chantal Nanaba Camara", "D) Amadou Soumahoro"],
        "answer": "B",
        "explanation": "Jeannot Ahoussou Kouadio a été le premier président du Sénat de Côte d'Ivoire."
    },
    {
        "question": "En 2027, la Cour des Comptes de Côte d'Ivoire a pour mission principale :",
        "options": ["A) De juger les conflits entre l'État et les particuliers", "B) Le contrôle supérieur des finances publiques", "C) La validation des candidatures à l'élection présidentielle", "D) L'organisation du référendum"],
        "answer": "B",
        "explanation": "La Cour des Comptes, institution de la République, assure le contrôle des finances publiques et juge les comptes des comptables publics."
    },
    {
        "question": "Laquelle de ces entités N'EST PAS une collectivité territoriale en Côte d'Ivoire ?",
        "options": ["A) La Région", "B) La Commune", "C) Le Département", "D) Le District Autonome"],
        "answer": "C",
        "explanation": "Depuis la réorganisation, les collectivités territoriales décentralisées sont les Communes et les Régions. Les Districts Autonomes sont des entités particulières déconcentrées et décentralisées, mais le Département n'est plus une collectivité territoriale décentralisée (il est une circonscription administrative)."
    },
    {
        "question": "Le droit du sol en Côte d'Ivoire :",
        "options": ["A) Est la règle absolue pour acquérir la nationalité", "B) A été supprimé par le Code de la nationalité de 1972", "C) S'applique uniquement aux enfants de réfugiés", "D) A été réintroduit par la Constitution de 2016"],
        "answer": "B",
        "explanation": "Le Code de la nationalité ivoirienne de 1972 a supprimé le droit du sol au profit du droit du sang (filiation)."
    },
    {
        "question": "Parmi les emblèmes de la République de Côte d'Ivoire, on compte :",
        "options": ["A) L'éléphant d'or", "B) Le drapeau tricolore, l'hymne, les armoiries et la devise", "C) Le pagne baoulé", "D) La basilique de Yamoussoukro"],
        "answer": "B",
        "explanation": "L'article 29 de la Constitution cite les 4 emblèmes : le Drapeau (Orange, Blanc, Vert), l'Hymne (L'Abidjanaise), la Devise (Union, Discipline, Travail) et les Armoiries."
    },
    {
        "question": "La Chambre nationale des Rois et Chefs traditionnels (CNRCT) :",
        "options": ["A) Est une simple association de droit privé", "B) Est une juridiction d'appel", "C) Est reconnue par la Constitution de 2016", "D) A été supprimée en 2020"],
        "answer": "C",
        "explanation": "La Constitution de 2016 consacre l'existence de la CNRCT en tant qu'institution de la République."
    },
    {
        "question": "Qui assure l'intérim de la Présidence de la République en cas de vacance définitive (décès, démission) selon la Constitution ?",
        "options": ["A) Le Président de l'Assemblée Nationale", "B) Le Vice-Président de la République", "C) Le Premier Ministre", "D) Le Président du Conseil Constitutionnel"],
        "answer": "B",
        "explanation": "En cas de vacance, le Vice-Président devient de plein droit Président de la République (art. 62 de la Constitution modifiée)."
    },
    {
        "question": "La nomination du Vice-Président en Côte d'Ivoire se fait par :",
        "options": ["A) Élection au suffrage universel direct", "B) Le Président de la République, en accord avec le Parlement", "C) Le Conseil Constitutionnel", "D) Le Premier ministre"],
        "answer": "B",
        "explanation": "Depuis la révision constitutionnelle de 2020, le Vice-Président est nommé par le Président de la République avec l'accord du Parlement réuni en Congrès."
    },
    {
        "question": "Dans le système ivoirien, le contreseing des actes du Président de la République est apposé par :",
        "options": ["A) Le Vice-Président exclusivement", "B) Le Premier ministre et les ministres chargés de l'exécution, pour les actes non dispensés", "C) Le Président du Sénat", "D) Le Président de la Cour Suprême"],
        "answer": "B",
        "explanation": "Les actes du PR, sauf exceptions (nomination PM, etc.), sont contresignés par le PM et les ministres concernés."
    },
    {
        "question": "Le Sénat ivoirien est composé :",
        "options": ["A) Entièrement de membres élus au suffrage direct", "B) De deux tiers élus au suffrage indirect et d'un tiers nommé par le Président de la République", "C) Entièrement de membres nommés", "D) Exclusivement de représentants de la diaspora"],
        "answer": "B",
        "explanation": "Le Sénat comprend 2/3 de sénateurs élus (suffrage universel indirect) et 1/3 nommés par le Chef de l'État."
    },
    {
        "question": "Quelle autorité est compétente pour juger la constitutionnalité des lois en Côte d'Ivoire ?",
        "options": ["A) Le Conseil d'État", "B) La Cour de Cassation", "C) Le Conseil Constitutionnel", "D) L'Assemblée Nationale"],
        "answer": "C",
        "explanation": "Le Conseil Constitutionnel est le juge de la constitutionnalité des lois (actuellement présidé par Chantal Nanaba Camara)."
    },
    {
        "question": "Le District Autonome d'Abidjan est :",
        "options": ["A) Une collectivité territoriale ordinaire", "B) Une entité territoriale particulière dotée de la personnalité morale et de l'autonomie financière", "C) Une simple préfecture de police", "D) Un quartier de Yamoussoukro"],
        "answer": "B",
        "explanation": "Les Districts autonomes (Abidjan, Yamoussoukro) jouissent d'un statut particulier (déconcentration et décentralisation)."
    },
    {
        "question": "L'institution chargée de garantir l'indépendance de la magistrature est :",
        "options": ["A) Le Ministère de la Justice", "B) Le Conseil Supérieur de la Magistrature (CSM)", "C) Le Conseil Constitutionnel", "D) L'ARCOP"],
        "answer": "B",
        "explanation": "Le CSM, présidé par le Président de la République, assiste ce dernier pour garantir l'indépendance de la justice."
    },
    {
        "question": "Le Médiateur de la République en Côte d'Ivoire :",
        "options": ["A) Est un juge pénal", "B) Est une autorité administrative indépendante chargée de régler les litiges entre l'Administration et les administrés", "C) Dirige la politique étrangère", "D) Valide les traités internationaux"],
        "answer": "B",
        "explanation": "Le Médiateur reçoit les requêtes concernant le fonctionnement des administrations et aide au règlement amiable des conflits."
    },
    {
        "question": "Le Parlement ivoirien de la 3ème République est :",
        "options": ["A) Monocaméral", "B) Bicaméral (Assemblée Nationale et Sénat)", "C) Tricaméral", "D) Inexistant"],
        "answer": "B",
        "explanation": "La Constitution de 2016 a instauré un Parlement bicaméral composé de l'Assemblée nationale et du Sénat."
    },
    {
        "question": "Qui a été nommé Vice-Président de la République de Côte d'Ivoire en 2022 ?",
        "options": ["A) Daniel Kablan Duncan", "B) Tiémoko Meyliet Koné", "C) Patrick Achi", "D) Robert Beugré Mambé"],
        "answer": "B",
        "explanation": "Tiémoko Meyliet Koné a été nommé Vice-Président en avril 2022."
    },
    {
        "question": "En Côte d'Ivoire, l'initiative des lois appartient concurremment :",
        "options": ["A) Au Président de la République et aux membres du Parlement", "B) Uniquement au Premier Ministre", "C) Au Conseil Constitutionnel et au Sénat", "D) Aux Maires et au Président de la République"],
        "answer": "A",
        "explanation": "L'initiative des lois appartient au Président de la République et aux parlementaires (députés et sénateurs)."
    },
    {
        "question": "La Loi d'orientation de l'Administration territoriale (1998) a consacré :",
        "options": ["A) La centralisation totale", "B) Les principes de déconcentration et de décentralisation", "C) La suppression des mairies", "D) L'élection des préfets"],
        "answer": "B",
        "explanation": "La loi a organisé l'administration territoriale ivoirienne autour des principes de déconcentration (préfets) et de décentralisation (collectivités locales)."
    },
    {
        "question": "Le mandat du Président de la République en Côte d'Ivoire est actuellement de :",
        "options": ["A) 4 ans", "B) 5 ans, renouvelable une seule fois consécutivement", "C) 7 ans", "D) A vie"],
        "answer": "B",
        "explanation": "Selon la Constitution de 2016, le mandat présidentiel est de 5 ans, et le Président n'est rééligible qu'une seule fois consécutivement."
    },
    {
        "question": "En matière de révision de la Constitution, le projet est définitivement adopté :",
        "options": ["A) Exclusivement par référendum", "B) Par référendum, ou par voie parlementaire si le PR décide de le soumettre au Congrès", "C) Par un décret du Conseil d'État", "D) Par le vote des conseils régionaux"],
        "answer": "B",
        "explanation": "Le projet de loi de révision constitutionnelle est soumis au référendum ou, sur décision du Président, au Parlement réuni en Congrès (majorité des 2/3)."
    },
    {
        "question": "La Haute Autorité pour la Bonne Gouvernance (HABG) a principalement pour rôle :",
        "options": ["A) La lutte contre la corruption et les infractions assimilées", "B) L'organisation des examens du baccalauréat", "C) La régulation des médias", "D) La nomination des ambassadeurs"],
        "answer": "A",
        "explanation": "La HABG est chargée de la prévention et de la lutte contre la corruption en Côte d'Ivoire."
    },
    {
        "question": "Le Conseil Économique, Social, Environnemental et Culturel (CESEC) :",
        "options": ["A) Vote le budget de l'État", "B) Donne un avis consultatif sur les projets de loi à caractère économique, social, environnemental ou culturel", "C) Juge les ministres", "D) Gère les réserves forestières"],
        "answer": "B",
        "explanation": "Le CESEC est une assemblée consultative qui donne des avis et mène des études sur ces domaines spécifiques."
    },
    {
        "question": "Le principe de l'inamovibilité s'applique à quels magistrats en Côte d'Ivoire ?",
        "options": ["A) Les magistrats du Parquet", "B) Les magistrats du Siège", "C) Tous les magistrats (Siège et Parquet)", "D) Uniquement aux juges du Conseil Constitutionnel"],
        "answer": "B",
        "explanation": "Seuls les magistrats du Siège (les juges) bénéficient de l'inamovibilité pour garantir leur indépendance, contrairement au Parquet, soumis à la subordination hiérarchique."
    },
    {
        "question": "L'âge minimum pour être candidat à l'élection présidentielle sous la Constitution de 2016 est de :",
        "options": ["A) 40 ans", "B) 35 ans", "C) 45 ans", "D) 50 ans"],
        "answer": "B",
        "explanation": "La Constitution de 2016 a abaissé l'âge minimum d'éligibilité à la Présidence de 40 à 35 ans et a supprimé le plafond d'âge."
    },
    {
        "question": "Dans la Constitution de 2016, l'école en Côte d'Ivoire est-elle une obligation fondamentale ?",
        "options": ["A) Non, c'est une simple recommandation.", "B) Oui, elle est obligatoire et gratuite pour les enfants des deux sexes jusqu'à l'âge requis.", "C) Elle est obligatoire uniquement pour les garçons.", "D) Elle est obligatoire, mais le financement est exclusivement privé."],
        "answer": "B",
        "explanation": "L'article 10 de la Constitution de 2016 (et modifiée 2020) garantit le droit à l'éducation, et précise que l'école est obligatoire pour tous les enfants des deux sexes. Elle est gratuite dans les établissements publics."
    },
    {
        "question": "Parmi ces libertés, laquelle est expressément garantie par le Titre I de la Constitution ivoirienne ?",
        "options": ["A) Le droit d'acquérir des armes à feu", "B) La liberté d'association, de réunion et de manifestation", "C) Le droit absolu de refuser l'impôt", "D) L'immunité parlementaire pour tout citoyen"],
        "answer": "B",
        "explanation": "L'article 20 garantit les libertés d'association, de réunion et de manifestation pacifiques."
    },
    {
        "question": "Selon la Constitution ivoirienne, qui peut saisir le Conseil constitutionnel pour contrôler la conformité d'une loi avant sa promulgation ?",
        "options": ["A) Uniquement le Président de la République", "B) Le PR, les Présidents de l'AN et du Sénat, ou 1/10ème des parlementaires", "C) Tout citoyen sans exception", "D) Le Procureur de la République"],
        "answer": "B",
        "explanation": "Le contrôle de constitutionnalité a priori peut être déclenché par le Président de la République, le Président de l'Assemblée Nationale, le Président du Sénat ou au moins un dixième des députés ou des sénateurs."
    },
    {
        "question": "Le Médiateur de la République ivoirien peut être saisi :",
        "options": ["A) Pour annuler un jugement d'assises", "B) Pour des différends opposant des personnes physiques ou morales à l'Administration", "C) Pour destituer le Président de la République", "D) Pour lever l'immunité d'un député"],
        "answer": "B",
        "explanation": "Le Médiateur est une AAI chargée de régler à l'amiable les litiges entre les usagers et l'Administration publique."
    },
    {
        "question": "Dans le processus législatif, si une commission paritaire ne parvient pas à un accord sur un texte (navette parlementaire), qui a le dernier mot en Côte d'Ivoire ?",
        "options": ["A) Le Sénat", "B) L'Assemblée Nationale", "C) Le Conseil d'État", "D) La Haute Autorité pour la Bonne Gouvernance"],
        "answer": "B",
        "explanation": "En cas de désaccord persistant (échec de la commission mixte paritaire), c'est l'Assemblée Nationale (élue au suffrage direct) qui a le dernier mot, sur demande du Président de la République."
    },
    {
        "question": "La Haute Autorité pour la Bonne Gouvernance (HABG) a notamment pour mission de :",
        "options": ["A) Recueillir les déclarations de patrimoine des hautes personnalités.", "B) Auditer les partis politiques pendant les campagnes.", "C) Gérer les fonds souverains de l'État.", "D) Nommer les ambassadeurs."],
        "answer": "A",
        "explanation": "L'une des missions centrales de la HABG est la réception, le traitement et la conservation des déclarations de patrimoine des assujettis (ministres, hauts fonctionnaires) pour prévenir l'enrichissement illicite."
    },
    {
        "question": "Selon la Constitution ivoirienne de 2016, la nomination du Premier Ministre par le Président de la République :",
        "options": ["A) Doit obligatoirement être contresignée par le Vice-Président.", "B) Est un pouvoir propre du Président, exercé sans contreseing.", "C) Nécessite l'approbation préalable de l'Assemblée Nationale.", "D) Est contresignée par le Président du Sénat."],
        "answer": "B",
        "explanation": "La nomination du Premier Ministre est l'un des pouvoirs propres du Chef de l'État (comme la dissolution de l'AN ou le recours au référendum), elle est dispensée du contreseing ministériel."
    },
]

THEME_7 = [
    {
        "question": "Cas pratique : Le Préfet du Loh-Djiboua prend un arrêté réglementant la circulation à Divo. Le Maire conteste. Quelle est la solution juridique devant le Conseil d'État ivoirien ?",
        "options": ["A) L'arrêté est illégal pour incompétence.", "B) L'arrêté est légal en vertu des pouvoirs de police du préfet.", "C) Le Maire n'a pas d'intérêt à agir.", "D) C'est un acte de gouvernement."],
        "answer": "B",
        "explanation": "Le Préfet a des pouvoirs de police administrative générale sur l'étendue de sa circonscription."
    },
    {
        "question": "Cas pratique : Le Ministre de l'Intérieur dissout le Conseil municipal de Divo pour des raisons politiques. Le Maire saisit le juge. Quelle est la solution ?",
        "options": ["A) Recevable, annulation pour détournement de pouvoir.", "B) Irrecevable, c'est un acte de tutelle insusceptible de recours.", "C) Recevable mais légal.", "D) Annulation pour incompétence territoriale."],
        "answer": "A",
        "explanation": "La dissolution pour un motif autre que le fonctionnement du conseil ou l'ordre public constitue un détournement de pouvoir."
    },
    {
        "question": "Cas pratique : Un professeur d'université est suspendu sans que son dossier disciplinaire lui soit communiqué. Quelle solution ?",
        "options": ["A) L'acte est légal.", "B) L'acte est entaché de vice de procédure (droits de la défense).", "C) L'acte est inexistant.", "D) C'est un acte préparatoire."],
        "answer": "B",
        "explanation": "Le respect des droits de la défense impose la communication du dossier avant toute sanction disciplinaire."
    },
    {
        "question": "Cas pratique : Le Maire de Cocody prend un arrêté sans le dater ni le signer. Quelle solution ?",
        "options": ["A) Vice de forme, l'acte est illégal.", "B) L'acte est légal car implicite.", "C) Vice de procédure.", "D) Incompétence matérielle."],
        "answer": "A",
        "explanation": "L'absence de signature et de date sur une décision administrative expresse constitue un vice de forme substantiel."
    },
    {
        "question": "Cas pratique : Un arrêté préfectoral est attaqué 3 mois après sa publication. Quelle solution ?",
        "options": ["A) Recours recevable.", "B) Recours irrecevable pour forclusion (délai de 2 mois dépassé).", "C) Recevable car c'est un acte réglementaire.", "D) Irrecevable pour défaut d'intérêt."],
        "answer": "B",
        "explanation": "Le délai du recours pour excès de pouvoir est de deux mois à compter de la publication pour les actes réglementaires."
    },
    {
        "question": "Cas pratique : Le Ministre des finances prend une circulaire interprétative sur la fiscalité. Une entreprise l'attaque. Quelle solution ?",
        "options": ["A) Recevable.", "B) Irrecevable, une circulaire purement interprétative ne fait pas grief.", "C) Recevable pour détournement de pouvoir.", "D) Irrecevable pour forclusion."],
        "answer": "B",
        "explanation": "Les circulaires interprétatives ne modifient pas l'ordonnancement juridique et sont insusceptibles de recours pour excès de pouvoir (Jurisprudence Notre Dame du Kreisker)."
    },
    {
        "question": "Cas pratique : Un Préfet abroge un permis de conduire obtenu légalement. Quelle solution ?",
        "options": ["A) Légal, par principe de mutabilité.", "B) Illégal, on ne peut abroger un acte individuel créateur de droits légal.", "C) Légal si l'administré est d'accord.", "D) Illégal pour incompétence temporelle."],
        "answer": "B",
        "explanation": "Un acte administratif individuel créateur de droits, lorsqu'il est légal, ne peut être ni abrogé ni retiré."
    },
    {
        "question": "Cas pratique : L'administration retire un arrêté illégal créateur de droits 3 mois après sa signature. Quelle solution ?",
        "options": ["A) Retrait légal.", "B) Retrait illégal, le délai de retrait est de 2 mois (délai de recours contentieux).", "C) Retrait légal car l'acte est illégal.", "D) Retrait conditionné à l'accord du juge."],
        "answer": "B",
        "explanation": "Le retrait des actes créateurs de droits illégaux n'est possible que pendant le délai du recours contentieux de 2 mois."
    },
    {
        "question": "Cas pratique : Le Maire de Bingerville destitue un chef de village pour cause de mésentente. Quelle solution ?",
        "options": ["A) L'acte est légal.", "B) L'acte est illégal pour incompétence matérielle (compétence du Préfet).", "C) L'acte est illégal pour incompétence territoriale.", "D) L'acte est légal en vertu de la décentralisation."],
        "answer": "B",
        "explanation": "En Côte d'Ivoire, les questions relatives à la chefferie traditionnelle relèvent de l'administration préfectorale et non municipale."
    },
    {
        "question": "Cas pratique : Un Directeur de cabinet signe un arrêté à la place du Ministre sans délégation publiée. Quelle solution ?",
        "options": ["A) L'acte est légal.", "B) L'acte est illégal pour incompétence (défaut de délégation régulière).", "C) Vice de forme.", "D) Vice de procédure."],
        "answer": "B",
        "explanation": "La délégation de signature doit être publiée pour entrer en vigueur. Sans cela, le délégataire est incompétent."
    },
    {
        "question": "Cas pratique : Le Conseil des ministres est omis lors de la prise d'un décret présidentiel obligatoire. Quelle solution ?",
        "options": ["A) Vice de forme.", "B) Vice de procédure substantiel (consultation obligatoire omise).", "C) Incompétence matérielle.", "D) Détournement de pouvoir."],
        "answer": "B",
        "explanation": "L'omission de la consultation d'un organisme exigée par les textes constitue un vice de procédure entraînant l'illégalité de l'acte."
    },
    {
        "question": "Cas pratique : Un chef de service affecte un agent loin de sa famille pour le punir de ses opinions syndicales. Quelle solution ?",
        "options": ["A) Incompétence matérielle.", "B) Détournement de pouvoir (motif politique/personnel au lieu de l'intérêt du service).", "C) Légalité parfaite.", "D) Vice de forme."],
        "answer": "B",
        "explanation": "Le détournement de pouvoir consiste pour l'autorité à utiliser ses pouvoirs dans un but autre que celui pour lequel ils lui ont été conférés."
    },
    {
        "question": "Cas pratique : Une administration tarde de 5 mois à répondre à une demande de permis de construire. Quelle solution ?",
        "options": ["A) Décision implicite d'acceptation.", "B) Décision implicite de rejet (silence de plus de 2 mois).", "C) Pas de décision, on ne peut rien faire.", "D) L'administration a 6 mois pour répondre."],
        "answer": "B",
        "explanation": "Le silence gardé par l'administration pendant un certain délai vaut en principe décision de rejet."
    },
    {
        "question": "Cas pratique : Le Maire de Yopougon prend un acte après l'élection de son successeur mais avant la passation des charges. Quelle solution ?",
        "options": ["A) Légal pour continuité du service.", "B) Illégal pour incompétence temporelle.", "C) Légal si c'est urgent.", "D) Vice de forme."],
        "answer": "B",
        "explanation": "L'autorité sortante perd sa compétence dès l'élection ou la nomination de son successeur (sauf affaires courantes strictement définies)."
    },
    {
        "question": "Cas pratique : Un contrat administratif est résilié unilatéralement par le Ministre de l'Équipement pour faute du cocontractant. Quelle solution devant le CE ?",
        "options": ["A) Recevable en REP.", "B) Irrecevable, c'est du contentieux de pleine juridiction contractuel.", "C) Recevable car c'est un acte détachable.", "D) Légal car le ministre a un droit absolu."],
        "answer": "B",
        "explanation": "Les mesures d'exécution et de résiliation des contrats relèvent du juge du contrat (pleine juridiction), pas du juge de l'excès de pouvoir."
    },
    {
        "question": "Cas pratique : Le Président de la République gracie un condamné. La victime attaque le décret de grâce. Quelle solution ?",
        "options": ["A) Recevable et illégal.", "B) Irrecevable (Acte de gouvernement).", "C) Recevable mais légal.", "D) Annulation pour vice de procédure."],
        "answer": "B",
        "explanation": "Le décret de grâce est un acte de gouvernement, insusceptible de tout recours juridictionnel."
    },
    {
        "question": "Cas pratique : Lors d'une mutinerie, un caporal prend des arrêtés pour organiser le ravitaillement de Bouaké. Quelle solution ?",
        "options": ["A) Actes inexistants.", "B) Actes valables sous la théorie du fonctionnaire de fait (circonstances exceptionnelles).", "C) Actes illégaux pour incompétence.", "D) Actes de gouvernement."],
        "answer": "B",
        "explanation": "La théorie du fonctionnaire de fait et des circonstances exceptionnelles permet de valider les actes de personnes incompétentes pour assurer la continuité des services vitaux."
    },
    {
        "question": "Cas pratique : Le Ministre de la santé adresse une lettre d'avertissement simple sans inscription au dossier à un agent. Quelle solution ?",
        "options": ["A) Recevable en REP.", "B) Irrecevable (Mesure d'ordre intérieur ne faisant pas grief).", "C) Illégal pour vice de forme.", "D) Vice de procédure."],
        "answer": "B",
        "explanation": "Les sanctions très légères non inscrites au dossier peuvent constituer des mesures d'ordre intérieur insusceptibles de REP."
    },
    {
        "question": "Cas pratique : Le Maire d'Abobo réglemente la vitesse maximale à 20 km/h sur tout le territoire national. Quelle solution ?",
        "options": ["A) Illégal pour incompétence territoriale.", "B) Légal par pouvoir de police.", "C) Incompétence matérielle.", "D) Détournement de pouvoir."],
        "answer": "A",
        "explanation": "Le Maire ne peut exercer son pouvoir réglementaire que dans les limites territoriales de sa commune."
    },
    {
        "question": "Cas pratique : L'Assemblée Nationale vote une loi d'expropriation. Un propriétaire saisit le juge administratif. Quelle solution ?",
        "options": ["A) Irrecevable, la loi n'est pas un AAU.", "B) Recevable pour violation de la propriété privée.", "C) Légal et recevable.", "D) Irrecevable pour forclusion."],
        "answer": "A",
        "explanation": "Les lois échappent au contrôle du juge administratif qui ne connaît que des actes des autorités administratives."
    },
    {
        "question": "Cas pratique 1 : La Mairie de Yopougon attribue de gré à gré un marché de 100 millions FCFA à BATI-CI. L'ARCOP est saisie. Quelle sera la décision ?",
        "options": ["A) Validation, c'est un marché local.", "B) Annulation, le gré à gré exige l'autorisation de la DMP.", "C) Amende administrative pour BATI-CI.", "D) Incompétence du juge."],
        "answer": "B",
        "explanation": "Les marchés de gré à gré au-delà du seuil de dispense nécessitent l'autorisation préalable de la Direction des Marchés Publics en CI."
    },
    {
        "question": "Cas pratique 2 : L'État résilie sans faute le contrat de concession de la société SIGMA. Quelle est l'issue ?",
        "options": ["A) Rétablissement du contrat.", "B) Annulation de la résiliation.", "C) Indemnisation intégrale du cocontractant.", "D) Rejet de la demande."],
        "answer": "C",
        "explanation": "L'Administration peut résilier pour motif d'intérêt général, mais doit indemniser intégralement le cocontractant (pertes et manque à gagner)."
    },
    {
        "question": "Cas pratique 3 : Une épidémie oblige l'État à exiger 20% de matériel en plus de YEKOUN-CI. YEKOUN-CI refuse. Décision ?",
        "options": ["A) Modification unilatérale justifiée pour intérêt général.", "B) Le contrat est nul.", "C) YEKOUN-CI a le droit de refuser.", "D) Le contrat est caduc."],
        "answer": "A",
        "explanation": "Mutabilité des contrats administratifs : l'administration peut imposer des modifications pour l'intérêt général (moyennant indemnisation)."
    },
    {
        "question": "Cas pratique 4 : Le Port d'Abidjan met en régie d'office son concessionnaire fautif sans mise en demeure. Décision ?",
        "options": ["A) Validation de la mesure.", "B) Annulation pour vice de procédure (absence de mise en demeure).", "C) La régie est impossible au PAA.", "D) Le concessionnaire est indemnisé."],
        "answer": "B",
        "explanation": "La mise en demeure est un préalable substantiel avant de prononcer une sanction coercitive comme la régie d'office."
    },
    {
        "question": "Cas pratique 5 : Une loi crée une taxe douanière ciblant spécifiquement le domaine d'importation du cocontractant de l'État TROPIC. Théorie applicable ?",
        "options": ["A) Force majeure.", "B) Sujétions imprévues.", "C) Fait du Prince (indemnisation totale).", "D) Imprévision (indemnisation partielle)."],
        "answer": "C",
        "explanation": "Une mesure de l'autorité contractante alourdissant les charges du cocontractant déclenche le Fait du Prince."
    },
    {
        "question": "Cas pratique 6 : Le prix du pétrole flambe au niveau mondial de 400%, asphyxiant l'entreprise ROUTE-CI dans l'exécution de son marché public ivoirien. Théorie applicable ?",
        "options": ["A) Fait du Prince.", "B) Force majeure.", "C) Imprévision (indemnité compensatoire).", "D) Sujétions imprévues."],
        "answer": "C",
        "explanation": "L'imprévision (circonstance extérieure, imprévisible et bouleversant l'économie du contrat) oblige l'Administration à aider son cocontractant."
    },
    {
        "question": "Cas pratique 7 : Une parcelle du domaine maritime à San Pedro est vendue à IMMO-SUD qui y construit depuis 15 ans. L'État veut récupérer le terrain.",
        "options": ["A) Prescription acquise pour IMMO-SUD.", "B) Le domaine public étant inaliénable et imprescriptible, restitution obligatoire.", "C) Expropriation avec indemnisation.", "D) Compétence du juge civil."],
        "answer": "B",
        "explanation": "L'inaliénabilité et l'imprescriptibilité du domaine public empêchent toute acquisition par prescription en Côte d'Ivoire."
    },
    {
        "question": "Cas pratique 8 : Le Maire de Bouaké vend une rue publique à un promoteur sans acte de déclassement préalable.",
        "options": ["A) La vente est nulle de plein droit.", "B) La vente est valable.", "C) La vente est régularisable.", "D) Seul le préfet peut annuler."],
        "answer": "A",
        "explanation": "Sans désaffectation de fait et déclassement de droit, un bien du domaine public ne peut être cédé (nullité absolue)."
    },
    {
        "question": "Cas pratique 9 : Lors des travaux à Yamoussoukro, BTP-CI découvre un sol rocheux d'une dureté exceptionnelle et imprévisible. Théorie applicable ?",
        "options": ["A) Fait du Prince.", "B) Force majeure.", "C) Imprévision.", "D) Sujétions imprévues."],
        "answer": "D",
        "explanation": "La découverte d'obstacles matériels imprévisibles constitue une sujétion imprévue justifiant une indemnisation intégrale."
    },
    {
        "question": "Cas pratique 10 : Une grève nationale paralysant tout le pays empêche CLEAN-CI de ramasser les ordures à Daloa. La Mairie résilie pour faute.",
        "options": ["A) Validation de la résiliation.", "B) Annulation, la grève constituant ici un cas de force majeure.", "C) L'entreprise doit payer des pénalités.", "D) Application de l'imprévision."],
        "answer": "B",
        "explanation": "Une grève générale imprévisible et irrésistible constitue un cas de force majeure, exonérant le cocontractant de toute faute."
    },
    {
        "question": "Cas pratique 11 : Le contrat de fourniture de l'Université stipule des pénalités de retard. L'entreprise défaillante estime que seul le juge peut les prononcer.",
        "options": ["A) Vrai, la sanction appartient au juge.", "B) Faux, l'Administration dispose d'un pouvoir de sanction unilatéral.", "C) Vrai, s'agissant d'une EPA.", "D) Faux, mais il faut un arrêté préfectoral."],
        "answer": "B",
        "explanation": "En matière de contrats administratifs, l'Administration a le pouvoir d'infliger unilatéralement des sanctions, même financières."
    },
    {
        "question": "Cas pratique 12 : L'État exproprie la famille KOUAKOU pour utilité publique mais 'oublie' l'enquête de commodo et incommodo.",
        "options": ["A) Expropriation régulière car urgente.", "B) Annulation de la DUP pour vice de procédure substantiel.", "C) Indemnisation double mais pas d'annulation.", "D) L'enquête n'est pas obligatoire."],
        "answer": "B",
        "explanation": "L'enquête publique (commodo et incommodo) est une condition de légalité de la Déclaration d'Utilité Publique en CI."
    },
    {
        "question": "Cas pratique 13 : Un particulier, M. DIALLO, occupe depuis 30 ans le domaine privé de l'État et demande un titre foncier par prescription.",
        "options": ["A) La prescription est toujours interdite contre l'État.", "B) Le domaine privé est prescriptible (sous conditions de droit privé et en l'absence de purge/immatriculation par l'État).", "C) Seul le domaine public est prescriptible.", "D) L'État est obligé de lui donner le titre."],
        "answer": "B",
        "explanation": "Le domaine privé obéit aux règles du droit privé, rendant théoriquement possible la prescription acquisitive, contrairement au domaine public (bien que souvent neutralisé par l'immatriculation)."
    },
    {
        "question": "Cas pratique 14 : Un entrepreneur a fourni des faux documents fiscaux au CHU de Cocody. L'autorité résilie unilatéralement le marché.",
        "options": ["A) La résiliation est illégale.", "B) C'est une résiliation pour faute justifiée.", "C) L'entrepreneur a droit à une indemnité.", "D) Seul le juge pénal peut annuler."],
        "answer": "B",
        "explanation": "La fraude (faux documents) constitue une faute grave justifiant une résiliation unilatérale aux torts exclusifs de l'entreprise."
    },
    {
        "question": "Cas pratique 15 : BTP-DIVO arrête le chantier car le Ministère ne paie plus ses factures. Le Ministère résilie pour abandon.",
        "options": ["A) Annulation, exception d'inexécution valide.", "B) Validation, l'exception d'inexécution ne s'applique pas au cocontractant administratif.", "C) Suspension du contrat.", "D) Paiement forcé ordonné."],
        "answer": "B",
        "explanation": "Principe de continuité : le cocontractant de l'Administration ne peut pas suspendre l'exécution en invoquant l'exception d'inexécution."
    },
    {
        "question": "Cas pratique 16 : Une rébellion s'empare de la ville, empêchant définitivement l'exécution du marché de BTP. Conséquence ?",
        "options": ["A) Résiliation pour force majeure (sans faute).", "B) Résiliation pour faute de BTP.", "C) Application de l'imprévision.", "D) Suspension infinie."],
        "answer": "A",
        "explanation": "L'impossibilité définitive d'exécuter causée par un événement irrésistible (guerre) entraîne la résiliation pour force majeure."
    },
    {
        "question": "Cas pratique 17 : L'Administration modifie unilatéralement les clauses tarifaires (le prix payé au cocontractant) pour économiser de l'argent.",
        "options": ["A) Validé par le pouvoir de modification.", "B) Annulé, l'équation financière est intangible unilatéralement.", "C) Validé sous réserve de l'ARCOP.", "D) Compétence du juge civil."],
        "answer": "B",
        "explanation": "L'Administration ne peut modifier unilatéralement les clauses financières (intangibilité financière), seules les clauses d'exécution sont mutables."
    },
    {
        "question": "Cas pratique 18 : Le nouveau Maire de Man reprend en régie la gestion de la gare routière avant le terme de la concession, sans faute du concessionnaire.",
        "options": ["A) Résiliation illégale.", "B) Résiliation pour motif d'intérêt général avec indemnisation.", "C) Résiliation sans indemnisation.", "D) Obligation d'aller au terme."],
        "answer": "B",
        "explanation": "La personne publique peut toujours mettre fin prématurément à un contrat dans l'intérêt du service public, moyennant indemnisation."
    },
    {
        "question": "Cas pratique 19 : Le Ministère des Eaux et Forêts exproprie de fait un champ (sans DUP) avec des bulldozers. M. ZADI saisit le juge judiciaire.",
        "options": ["A) Incompétence du JJ.", "B) Compétence du JJ car c'est une emprise irrégulière / voie de fait.", "C) Compétence du Conseil d'État.", "D) Tribunal de commerce."],
        "answer": "B",
        "explanation": "L'emprise irrégulière entraînant la dépossession foncière / voie de fait fonde la compétence du juge judiciaire."
    },
    {
        "question": "Cas pratique 20 : Le contrat de fourniture de SOTRA stipule que les pénalités de retard sont fixées à 1% par jour. L'ARCOP trouve ça abusif.",
        "options": ["A) Le juge peut modérer les pénalités manifestement excessives.", "B) Le juge ne peut pas modifier le contrat.", "C) Les pénalités sont illégales.", "D) L'ARCOP annule le contrat."],
        "answer": "A",
        "explanation": "La jurisprudence administrative moderne autorise le juge à modérer les pénalités contractuelles manifestement excessives."
    },
    {
        "question": "Cas pratique 21 : L'entreprise omet de renouveler sa garantie de bonne exécution (caution). Le CHU de Treichville résilie.",
        "options": ["A) Résiliation abusive.", "B) Résiliation pour faute justifiée.", "C) Mise en régie obligatoire.", "D) Application de l'imprévision."],
        "answer": "B",
        "explanation": "Le défaut de constitution ou de renouvellement des garanties financières est une faute contractuelle justifiant la résiliation."
    },
    {
        "question": "Cas pratique 22 : Le sous-préfet décide de louer le stade municipal (domaine public) à une église pour un week-end. C'est :",
        "options": ["A) Une vente illégale.", "B) Une occupation temporaire du domaine public (autorisation précaire et révocable).", "C) Un déclassement.", "D) Un contrat de droit privé."],
        "answer": "B",
        "explanation": "L'utilisation privative du domaine public peut faire l'objet d'une autorisation ou convention d'occupation temporaire (précaire et révocable)."
    },
    {
        "question": "Cas pratique 23 : M. TAPE a construit un kiosque sur le trottoir. Le Maire le détruit d'office sans recours au juge car il gêne la circulation urgente.",
        "options": ["A) Voie de fait systématique.", "B) Exécution d'office légale en cas d'urgence ou d'occupation sans titre du domaine public.", "C) Indemnisation de TAPE.", "D) Le trottoir est du domaine privé."],
        "answer": "B",
        "explanation": "L'Administration peut procéder à l'exécution d'office (destruction matérielle) pour libérer le domaine public illégalement occupé en cas d'urgence."
    },
    {
        "question": "Cas pratique 24 : Le concessionnaire du service de l'eau en CI voit ses canalisations détruites par des travaux publics de l'État.",
        "options": ["A) Fait du prince (indemnisation intégrale).", "B) Force majeure.", "C) Imprévision.", "D) Faute du concessionnaire."],
        "answer": "A",
        "explanation": "Le dommage causé par l'autorité contractante agissant dans une autre qualité constitue un fait du prince s'il aggrave les charges du cocontractant."
    },
    {
        "question": "Cas pratique 25 : La Mairie d'Adzopé conclut un bail commercial (droit privé) avec un boucher pour une boutique dans le marché couvert (domaine public).",
        "options": ["A) Le bail commercial est légal.", "B) Un bail commercial est impossible sur le domaine public (nullité).", "C) Le bail est soumis au droit administratif uniquement si la valeur est élevée.", "D) Compétence de l'ARCOP."],
        "answer": "B",
        "explanation": "Le domaine public étant inaliénable, on ne peut y constituer de droits réels de type bail commercial classique qui octroie une propriété commerciale."
    },
    {
        "question": "Cas pratique 26 : Le Conseil municipal de Koumassi vote le déclassement de la place publique, puis le Maire la vend le lendemain à un privé.",
        "options": ["A) Vente illégale, la place doit d'abord être matériellement désaffectée.", "B) Vente légale, le déclassement juridique suffit.", "C) Vente nulle car la place appartient à l'État.", "D) Le préfet doit d'abord valider."],
        "answer": "A",
        "explanation": "La sortie du domaine public exige deux conditions cumulatives : la désaffectation matérielle (fait) ET le déclassement formel (acte)."
    },
    {
        "question": "Cas pratique 27 : L'appel d'offres pour la construction du Ministère de la Justice est restreint à 3 entreprises sans justification au regard du Code des marchés publics.",
        "options": ["A) Légalité du marché.", "B) Annulation pour violation du principe de libre accès à la commande publique.", "C) Validation par l'ARCOP si le prix est bon.", "D) Vice de forme mineur."],
        "answer": "B",
        "explanation": "Le recours injustifié à l'appel d'offres restreint au lieu de l'appel d'offres ouvert viole le principe fondamental de mise en concurrence."
    },
    {
        "question": "Cas pratique 28 : Une entreprise remporte un marché, mais le contrat stipule qu'en cas de litige, l'arbitrage CCI (Chambre de Commerce Internationale) à Paris s'imposera. Est-ce valable en droit public ivoirien ?",
        "options": ["A) Totalement interdit pour l'État.", "B) Admis sous conditions et autorisation pour les contrats de partenariat et concessions internationales.", "C) L'arbitrage est obligatoire partout.", "D) Seule la CCJA est compétente."],
        "answer": "B",
        "explanation": "Historiquement interdit, l'arbitrage international est aujourd'hui admis en droit ivoirien pour certains contrats complexes (PPP, concessions) si autorisé par la loi."
    },
    {
        "question": "Cas pratique 29 : L'État ne paye pas la société de nettoyage. Le juge condamne l'État à payer sous astreinte de 1 million / jour. L'État refuse d'exécuter.",
        "options": ["A) L'État est insaisissable (pas d'exécution forcée directe sur ses biens).", "B) L'huissier peut saisir les comptes du Trésor public.", "C) Le créancier peut vendre les locaux de l'État.", "D) Le contrat est annulé."],
        "answer": "A",
        "explanation": "Les biens des personnes publiques sont insaisissables (impossibilité d'exécution forcée de droit privé). Le créancier dépend des mécanismes d'ordonnancement public."
    },
    {
        "question": "Cas pratique 30 : Un marché de gré à gré est conclu en urgence impérieuse suite à l'effondrement d'un pont. La DMP refuse son visa.",
        "options": ["A) Le marché est nul.", "B) Le gré à gré est toujours légal en cas d'urgence impérieuse avérée, le refus est abusif.", "C) Le Maire est condamné.", "D) Le Conseil d'État annulera l'urgence."],
        "answer": "B",
        "explanation": "Le Code des marchés publics ivoirien prévoit expressément le gré à gré en cas d'urgence impérieuse résultant de circonstances imprévisibles."
    },
    {
        "question": "Cas pratique 31 : L'entreprise X signe un contrat avec le Ministère, mais le Ministre n'était pas compétent pour signer sans délégation du Ministre de l'Économie.",
        "options": ["A) Le contrat est valide (théorie de l'apparence).", "B) Le contrat est nul pour incompétence de l'auteur de l'acte.", "C) Le contrat devient un acte privé.", "D) Le Ministre est condamné pénalement."],
        "answer": "B",
        "explanation": "L'incompétence de l'autorité signataire entache le contrat administratif de nullité absolue, sauf ratification a posteriori par l'autorité compétente."
    },
    {
        "question": "Cas pratique 32 : Le Préfet d'Abidjan conclut un bail avec un privé pour loger ses services (domaine privé du propriétaire). Nature du contrat ?",
        "options": ["A) Contrat administratif par détermination de la loi.", "B) Contrat de droit privé (bail de droit commun), compétence du juge judiciaire.", "C) Marché public.", "D) Concession."],
        "answer": "B",
        "explanation": "La simple location par l'Administration d'un immeuble appartenant à un privé, sans clause exorbitante, constitue un contrat de droit privé (bail ordinaire)."
    },
    {
        "question": "Cas pratique 33 : Le Ministère de la Défense achète des armes. Il ne fait pas d'appel d'offres ouvert.",
        "options": ["A) Illégal, l'appel d'offres ouvert est la règle absolue.", "B) Légal, les marchés liés à la sécurité nationale / secret-défense bénéficient de procédures dérogatoires (gré à gré).", "C) Seul le Président peut acheter des armes.", "D) Le marché sera annulé par l'ARCOP."],
        "answer": "B",
        "explanation": "Le Code des marchés publics prévoit des exceptions (gré à gré, secret) pour les marchés intéressant la sécurité ou la défense nationale."
    },
    {
        "question": "Cas pratique 34 : L'Administration découvre que son cocontractant sous-traite 80% du marché sans autorisation. Sanction ?",
        "options": ["A) La sous-traitance est totalement libre.", "B) Résiliation unilatérale pour faute (violation des règles de sous-traitance).", "C) Augmentation du délai du marché.", "D) Modification unilatérale."],
        "answer": "B",
        "explanation": "La sous-traitance dans les marchés publics ivoiriens est encadrée (limitation en % et nécessité d'agrément de l'Administration). Le dépassement ou la dissimulation est une faute justifiant résiliation."
    },
    {
        "question": "Cas pratique 35 : La Mairie cède l'exploitation exclusive de la distribution d'eau à la SODECI. Le contrat prévoit que la SODECI se rémunère sur les usagers. Nature du contrat ?",
        "options": ["A) Marché public.", "B) Délégation de service public (concession ou affermage).", "C) Contrat de partenariat.", "D) Convention de domaine public."],
        "answer": "B",
        "explanation": "Le contrat par lequel le cocontractant assume le risque d'exploitation et se rémunère substantiellement par les redevances perçues sur les usagers est une délégation de service public."
    },
    {
        "question": "Cas pratique 36 : Lors d'une expropriation, le juge fixe une indemnité de 10 millions FCFA. L'État expulse le propriétaire avant même de payer. Légalité ?",
        "options": ["A) Légal, l'urgence l'exige.", "B) Illégal, l'expropriation exige une juste et préalable indemnisation (Constitution ivoirienne).", "C) L'indemnisation se fait toujours a posteriori.", "D) Le juge l'autorisera."],
        "answer": "B",
        "explanation": "La Constitution de CI et le droit de l'expropriation posent le principe de l'indemnisation 'juste et préalable'. L'expulsion avant paiement est une voie de fait."
    },
    {
        "question": "Cas pratique 37 : L'autorité contractante impose à son cocontractant un changement des modalités techniques. Le cocontractant refuse et résilie lui-même le contrat.",
        "options": ["A) Légal, nul n'est tenu d'accepter une modification unilatérale.", "B) Illégal, seul le juge administratif peut prononcer la résiliation aux torts de l'Administration à la demande du cocontractant.", "C) Légal si la modification dépasse 50%.", "D) L'ARCOP validera."],
        "answer": "B",
        "explanation": "Le cocontractant n'a jamais le droit de résilier unilatéralement le contrat, même en cas de faute ou d'abus de l'Administration. Il doit saisir le juge pour demander la résiliation judiciaire."
    },
    {
        "question": "Cas pratique 38 : Un marché public est conclu avec KOFFI. Le contrat comporte une clause autorisant KOFFI à suspendre les travaux si l'État ne paie pas. Validité ?",
        "options": ["A) Clause valide.", "B) Clause réputée non écrite car contraire au principe de continuité du service public.", "C) Clause validée par l'ARCOP.", "D) Valide seulement pour les PPP."],
        "answer": "B",
        "explanation": "L'interdiction de l'exception d'inexécution dans les contrats administratifs est d'ordre public. Toute clause contraire est réputée non écrite."
    },
    {
        "question": "Cas pratique 39 : Pour construire une route, l'État a besoin du terrain de Bamba pour y stocker temporairement des engins. Procédure ?",
        "options": ["A) Expropriation totale.", "B) Occupation temporaire (servitude administrative) donnant lieu à indemnisation.", "C) Confiscation.", "D) Réquisition."],
        "answer": "B",
        "explanation": "La loi prévoit la procédure d'occupation temporaire des propriétés privées pour la réalisation de travaux publics, contre indemnisation des dégradations."
    },
    {
        "question": "Cas pratique 40 : Un administré tombe dans un trou laissé béant par l'entreprise de travaux publics SITRAP. Qui est responsable ?",
        "options": ["A) L'Administration exclusivement.", "B) L'entreprise titulaire des travaux publics, responsable envers les tiers (dommage de travaux publics).", "C) L'usager (force majeure).", "D) L'ARCOP."],
        "answer": "B",
        "explanation": "Les dommages causés aux tiers par les travaux publics engagent la responsabilité de l'entrepreneur (et solidairement du maître d'ouvrage public) sur le terrain de la responsabilité sans faute (risque)."
    },
    {
        "question": "Cas pratique 41 : Un avenant à un marché public de 100 millions augmente le prix initial de 40 millions (40%). L'ARCOP est saisie.",
        "options": ["A) Avenant valide.", "B) Avenant illégal car il bouleverse l'économie du marché (seuil maximal généralement de 15-20% pour un avenant, au-delà = nouveau marché).", "C) L'ARCOP n'est pas compétente.", "D) Avenant validé si l'entrepreneur est d'accord."],
        "answer": "B",
        "explanation": "Un avenant ne doit pas bouleverser l'économie initiale du marché (limite fixée par la réglementation, souvent 20%). Au-delà, l'Administration doit lancer une nouvelle procédure de mise en concurrence."
    },
    {
        "question": "Cas pratique 42 : L'entreprise BTP-CI est en faillite (liquidation judiciaire). L'Administration est-elle tenue de poursuivre le contrat avec le liquidateur ?",
        "options": ["A) Oui, pour sauver l'entreprise.", "B) Non, la faillite/liquidation entraîne la résiliation de plein droit (ou par l'Administration) du contrat (intuitu personae).", "C) Le juge consulaire obligera l'Administration.", "D) La sous-traitance est imposée."],
        "answer": "B",
        "explanation": "Les contrats administratifs étant conclus 'intuitu personae', la faillite du cocontractant justifie généralement la résiliation de plein droit."
    },
    {
        "question": "Cas pratique 43 : Le Conseil Régional du Gôh achète 50 véhicules de fonction. La procédure utilisée est la demande de cotation (3 devis).",
        "options": ["A) Procédure légale si le montant global est inférieur au seuil de l'appel d'offres.", "B) La demande de cotation n'existe pas en CI.", "C) Les véhicules nécessitent un PPP.", "D) Le gré à gré est imposé."],
        "answer": "A",
        "explanation": "La demande de cotation (procédures simplifiées) est autorisée par le Code des marchés publics pour les achats courants de faible montant sous le seuil légal de l'appel d'offres."
    },
    {
        "question": "Cas pratique 44 : L'État ivoirien signe un accord de prêt (Traité) avec la Banque Mondiale prévoyant des règles de passation spécifiques pour un barrage, contraires au Code ivoirien des marchés.",
        "options": ["A) Le Code ivoirien s'applique toujours.", "B) Les directives de la Banque Mondiale priment (suprématie des traités et conventions de financement sur le droit interne).", "C) Le contrat est nul.", "D) Compétence de la CCJA."],
        "answer": "B",
        "explanation": "L'article 87 de la Constitution (suprématie des traités) et le Code des marchés publics disposent que les règles des bailleurs de fonds internationaux priment sur le code national en cas de conflit."
    },
    {
        "question": "Cas pratique 45 : Une Mairie attribue la gestion de son abattoir à un boucher local. C'est le boucher qui a conçu lui-même l'idée et proposé le projet au Maire spontanément (Offre spontanée).",
        "options": ["A) Le Maire peut signer directement de gré à gré.", "B) L'offre spontanée nécessite d'être soumise à concurrence (appel d'offres ouvert avec une prime d'avance pour le concepteur).", "C) L'offre spontanée est interdite.", "D) Le Maire sera révoqué."],
        "answer": "B",
        "explanation": "Le cadre juridique ivoirien des PPP/DSP encadre les offres spontanées : elles ne dispensent pas de la mise en concurrence (même si le promoteur initial a un avantage)."
    },
    {
        "question": "Cas pratique 46 : L'Université de Cocody concède un terrain de son campus pour 30 ans à SCI-Campus pour y construire des résidences universitaires, la SCI devant les gérer puis les rendre (Bail emphytéotique administratif).",
        "options": ["A) Interdit sur le domaine public.", "B) Le BEA (Bail Emphytéotique Administratif) est autorisé par des textes spéciaux pour valoriser le domaine public.", "C) La SCI devient propriétaire définitif.", "D) C'est une voie de fait."],
        "answer": "B",
        "explanation": "Le droit a évolué pour permettre des montages immobiliers complexes sur le domaine public, comme le BEA ou les Autorisations d'Occupation Temporaire (AOT) constitutives de droits réels."
    },
    {
        "question": "Cas pratique 47 : Lors de l'examen des offres pour l'hôpital d'Odienné, la Commission d'Ouverture des Plis et d'Évaluation des Offres (COPEO) écarte l'offre la moins chère car elle est 'anormalement basse' (sous-évaluée de 50%). L'entreprise conteste.",
        "options": ["A) La COPEO a tort, il faut toujours prendre le moins disant.", "B) La COPEO a le droit et l'obligation d'écarter une offre anormalement basse après avoir demandé des justifications (risque de non-exécution).", "C) La COPEO doit saisir le Président.", "D) L'ARCOP obligera à prendre l'offre basse."],
        "answer": "B",
        "explanation": "Le Code des marchés publics protège l'Administration contre le 'dumping'. Si une offre est anormalement basse et que l'entreprise ne justifie pas son prix, elle doit être rejetée pour garantir l'exécution."
    },
    {
        "question": "Cas pratique 48 : M. SANGARE construit un mur qui déborde de 2 mètres sur la voie publique (alignement). Le Préfet peut-il ordonner la démolition ?",
        "options": ["A) Non, droit de propriété.", "B) Oui, c'est une atteinte au domaine public (infraction de grande voirie) justifiant démolition et amende.", "C) Il doit lui vendre les 2 mètres.", "D) Le Conseil d'État est incompétent."],
        "answer": "B",
        "explanation": "L'occupation sans titre et la dégradation du domaine public routier (contraventions de voirie) entraînent l'obligation de remise en état (démolition de l'empiètement) et amende."
    },
    {
        "question": "Cas pratique 49 : M. YAPO, agriculteur, conteste l'indemnité d'expropriation fixée par la Commission Administrative d'expropriation pour son champ.",
        "options": ["A) Il doit saisir le Conseil d'État.", "B) Le contentieux du montant de l'indemnité d'expropriation relève exclusivement du juge judiciaire (Tribunal de 1ère instance).", "C) Il doit faire une marche pacifique.", "D) L'ARCOP est compétente."],
        "answer": "B",
        "explanation": "Si le juge administratif contrôle la légalité de la procédure (la DUP), seul le juge judiciaire (protecteur constitutionnel de la propriété) est compétent pour fixer le montant de l'indemnité d'expropriation."
    },
    {
        "question": "Cas pratique 50 : Le Ministre de la Santé signe un contrat de gré à gré de 5 milliards FCFA. Le contrat est transmis pour approbation. Qui doit l'approuver ?",
        "options": ["A) Le Président de la République.", "B) Le Ministre du Budget / des Finances (selon les seuils, souvent Ministre du Budget pour les gros montants en CI).", "C) Le préfet d'Abidjan.", "D) L'ARCOP."],
        "answer": "B",
        "explanation": "Les marchés de l'État de montants très élevés sont soumis à l'approbation conjointe ou exclusive du Ministre en charge du Budget et des Finances, autorité d'approbation désignée."
    },
    {
        "question": "Cas pratique 51 : Le Directeur d'un Hôpital public attribue tous les marchés de fourniture à l'entreprise de son épouse. Délit pénal ?",
        "options": ["A) Non, c'est du favoritisme administratif simple.", "B) Oui, délit d'octroi d'avantage injustifié (favoritisme) et prise illégale d'intérêts pénalement sanctionnés.", "C) C'est légal si les prix sont bons.", "D) Seul le licenciement est possible."],
        "answer": "B",
        "explanation": "L'atteinte à la liberté d'accès et à l'égalité dans les marchés publics (favoritisme, prise illégale d'intérêts) est un délit réprimé par le Code pénal ivoirien."
    },
    {
        "question": "Cas pratique 52 : La commune de Man refuse de payer un entrepreneur ayant achevé la construction de l'école parce que 'le budget communal de l'année est épuisé'.",
        "options": ["A) L'entrepreneur perd son argent.", "B) La dette de la commune (marché exécuté) est certaine, l'épuisement des crédits n'efface pas l'obligation de payer (mandatement d'office possible par la tutelle).", "C) La commune est en faillite.", "D) Le contrat est annulé."],
        "answer": "B",
        "explanation": "L'insuffisance de crédit n'est pas une excuse absolutoire pour l'Administration. Le cocontractant ayant exécuté sa prestation a droit à son paiement (avec intérêts moratoires)."
    },
    {
        "question": "Cas pratique 53 : L'entreprise BATI-CI a un retard d'exécution de 30 jours. L'administration ne lui inflige aucune pénalité et l'exonère (remise gracieuse) pour des raisons politiques. Légalité ?",
        "options": ["A) Légal, pouvoir discrétionnaire de la remise des pénalités.", "B) Illégal en l'absence de motif lié à l'exécution ou à la force majeure, ce qui s'apparente à une libéralité (don) interdite pour une personne publique.", "C) Légal car la Mairie fait ce qu'elle veut.", "D) La DMP est seule compétente."],
        "answer": "B",
        "explanation": "Les personnes publiques ne peuvent consentir des libéralités (abandon de créance non justifié). Une remise gracieuse de pénalités doit être motivée par l'équité ou le comportement de l'Administration."
    },
    {
        "question": "Cas pratique 54 : Lors d'une procédure d'appel d'offres pour l'acquisition d'ordinateurs, la Mairie du Plateau exige que les ordinateurs soient exclusivement de la marque Apple. Une autre entreprise de marque HP conteste.",
        "options": ["A) Légal, la mairie choisit son matériel.", "B) Illégal, interdiction de mentionner une marque commerciale spécifique sans ajouter 'ou équivalent' (atteinte à la concurrence).", "C) Légal car Apple est meilleur.", "D) ARCOP se déclare incompétente."],
        "answer": "B",
        "explanation": "Le Code des marchés publics interdit de spécifier une marque, un brevet ou une origine précise dans les spécifications techniques, sauf si accompagné de la mention 'ou équivalent'."
    },
    {
        "question": "Cas pratique 55 : Une concession d'autoroute arrive à son terme normal. L'entreprise concessionnaire demande à conserver les gares de péage construites par elle.",
        "options": ["A) Les gares lui appartiennent.", "B) Principe de la théorie des biens de retour : les biens nécessaires au service public reviennent gratuitement à la personne publique en fin de concession.", "C) Elle doit les détruire.", "D) L'État doit les racheter au prix fort."],
        "answer": "B",
        "explanation": "Dans une concession (ou DSP), les ouvrages établis par le concessionnaire et indispensables au fonctionnement du service public ('biens de retour') deviennent la propriété de l'autorité délégante à la fin du contrat, sans indemnité (sauf amortissement inachevé)."
    },
    {
        "question": "Cas pratique 56 : Un préfet recrute par contrat un agent contractuel de la fonction publique (CDD d'un an). A l'échéance, il ne renouvelle pas le contrat. L'agent attaque pour licenciement abusif.",
        "options": ["A) C'est un licenciement abusif.", "B) Le non-renouvellement d'un CDD n'est pas un licenciement, l'agent n'a aucun droit acquis au renouvellement.", "C) L'agent devient automatiquement fonctionnaire.", "D) L'État doit payer 10 ans de salaire."],
        "answer": "B",
        "explanation": "L'agent contractuel de l'Administration embauché en CDD n'a pas droit au maintien de son emploi. Le non-renouvellement arrivé à terme ne constitue pas une sanction ni un licenciement."
    },
    {
        "question": "Cas pratique 57 : Le Ministère impose de nouvelles normes de sécurité sismique en cours de chantier, alourdissant le coût du marché de 20%.",
        "options": ["A) L'entreprise doit payer elle-même.", "B) Il s'agit d'une modification unilatérale justifiée, l'Administration doit supporter le surcoût (indemnisation intégrale du cocontractant).", "C) Le marché est caduc.", "D) Sujétion imprévue."],
        "answer": "B",
        "explanation": "C'est l'exercice du pouvoir de modification unilatérale du cahier des charges par l'Administration, qui engendre le droit pour le cocontractant de voir l'équilibre financier rétabli."
    },
    {
        "question": "Cas pratique 58 : M. CISSE achète un terrain immatriculé appartenant au domaine privé de l'État de Côte d'Ivoire selon les procédures normales de cession domaniale (lettre d'attribution, arrêté de concession provisoire).",
        "options": ["A) Il acquiert une propriété absolue immédiatement.", "B) Il doit obligatoirement mettre en valeur le terrain dans un délai imparti (mise en valeur) avant d'obtenir le Titre Foncier (Arrêté de concession définitive).", "C) L'État peut reprendre à tout moment sans faute.", "D) Il doit louer le terrain."],
        "answer": "B",
        "explanation": "La procédure domaniale ivoirienne (domaine urbain privé de l'État) impose la mise en valeur du terrain sous peine de retrait (déchéance) avant l'octroi de l'ACD (Arrêté de Concession Définitive) valant titre de propriété pleine."
    },
    {
        "question": "Cas pratique 59 : Le Maire d'une commune de 10.000 habitants conclut un contrat de 5 milliards FCFA sans que son Conseil municipal n'ait délibéré (pas de budget voté ni d'autorisation).",
        "options": ["A) Contrat nul pour incompétence (vice de forme/procédure et dépassement de budget).", "B) Contrat valable, le Maire est le chef.", "C) L'ARCOP paiera la différence.", "D) Contrat rétroactivement validé."],
        "answer": "A",
        "explanation": "La conclusion d'un marché public par l'exécutif local nécessite obligatoirement l'autorisation préalable (délibération) de l'organe délibérant (le Conseil municipal) et la disponibilité des crédits budgétaires."
    },
    {
        "question": "Cas pratique 60 : La commune confie l'éclairage public (service public) à une association de quartier subventionnée sans aucune procédure de publicité. Le contrat est attaqué.",
        "options": ["A) Contrat légal car c'est une association.", "B) Contrat illégal (qualifié de délégation de service public dissimulée ou marché public, soumis aux règles de mise en concurrence).", "C) Les associations échappent au droit.", "D) Validé par le Préfet."],
        "answer": "B",
        "explanation": "Le transfert de la gestion d'un service public à un tiers, même une association à but non lucratif subventionnée, constitue un contrat de la commande publique (souvent DSP) et nécessite publicité et concurrence."
    },
    {
        "question": "Cas pratique 61 : L'autorité contractante résilie un marché de gré à gré après qu'un rapport de l'Inspection Générale de l'État ait révélé des pots-de-vin.",
        "options": ["A) Résiliation impossible, il faut un jugement pénal.", "B) Résiliation unilatérale justifiée pour faute grave (corruption) et protection des deniers publics.", "C) Théorie de l'imprévision.", "D) Faute de l'Administration exclusive."],
        "answer": "B",
        "explanation": "La corruption avérée (acte délictuel de l'attributaire) vicie gravement la moralité et l'intégrité du marché, autorisant l'Administration à résilier le contrat pour faute (sans préjudice de l'exclusion des marchés publics)."
    },
    {
        "question": "Cas pratique 62 : La CCJA (Cour Commune de Justice et d'Arbitrage) d'Abidjan (droit OHADA) est saisie d'un litige sur l'exécution d'un marché public national ivoirien ordinaire sans clause d'arbitrage.",
        "options": ["A) La CCJA est incompétente. Le contrat administratif relève de la juridiction administrative national (Conseil d'État).", "B) La CCJA est toujours compétente en affaires.", "C) Le litige va à la CPI.", "D) Le tribunal de commerce tranche."],
        "answer": "A",
        "explanation": "L'OHADA concerne le droit des affaires (privé). Les marchés publics internes de l'État (contrats administratifs) sont expressément exclus du droit OHADA et relèvent du juge administratif national (Conseil d'État)."
    },
    {
        "question": "Cas pratique 63 : L'entreprise SIFCA, victime d'un vol de son matériel sur le chantier par des bandits armés la nuit, invoque la force majeure pour échapper aux pénalités de retard.",
        "options": ["A) Le vol de matériel banal ne constitue généralement pas un cas de force majeure (il n'est pas imprévisible et irrésistible sur un chantier classique).", "B) C'est un cas de force majeure avéré.", "C) C'est le Fait du Prince.", "D) L'État doit sécuriser les chantiers."],
        "answer": "A",
        "explanation": "La jurisprudence administrative est stricte : le vol de matériel, l'incendie classique, ou la défaillance d'un sous-traitant ne revêtent pas les caractères de la force majeure. L'entrepreneur reste responsable."
    },
    {
        "question": "Cas pratique 64 : L'Administration découvre qu'une clause de révision des prix insérée dans le marché initial est contraire à l'ordre public financier. Que fait le juge administratif ?",
        "options": ["A) Il annule tout le contrat.", "B) Il déclare la seule clause illégale (ou réputée non écrite), le reste du marché étant maintenu si la clause n'est pas indivisible.", "C) Il modifie lui-même la clause.", "D) Il augmente le délai d'exécution."],
        "answer": "B",
        "explanation": "Le juge privilégie la sauvegarde du contrat (lointain écho de la jurisprudence 'Béziers I' en France, applicable en CI). Une clause illégale détachable peut être annulée seule sans anéantir le contrat entier."
    },
    {
        "question": "Cas pratique 65 : L'ARCOP de CI décide d'exclure la Société XYZ de toute participation aux marchés publics pour une durée de 5 ans, pour usage de faux documents.",
        "options": ["A) L'ARCOP n'a pas de pouvoir de sanction.", "B) L'ARCOP dispose d'un pouvoir de sanction disciplinaire (exclusion temporaire ou définitive) à l'encontre des acteurs de la commande publique fautifs.", "C) Seul le juge pénal peut exclure.", "D) L'exclusion est limitée à 1 an maximum."],
        "answer": "B",
        "explanation": "En Côte d'Ivoire, l'ARCOP (organe de régulation) dispose d'importants pouvoirs de sanction, dont la suspension ou l'exclusion temporaire des entreprises ayant violé la réglementation."
    },
    {
        "question": "Cas pratique 66 : Le concessionnaire du PAA (Port Autonome d'Abidjan) installe des grues gigantesques. À la fin du contrat, le PAA les réclame.",
        "options": ["A) Biens de reprise (rachetés).", "B) Biens de retour (gratuits si amortis).", "C) Biens propres.", "D) Appartient à l'État."],
        "answer": "B",
        "explanation": "Les équipements indispensables au SP sont des biens de retour, revenant à l'autorité concédante à la fin, gratuitement s'ils sont totalement amortis."
    },
    {
        "question": "Cas pratique 67 : L'Hôpital psychiatrique de Bingerville achète en gré à gré de la nourriture pour ses malades mentaux internés d'urgence.",
        "options": ["A) Urgence impérieuse légale.", "B) Annulation pour défaut de publicité.", "C) Condamnation du directeur.", "D) Gré à gré civil."],
        "answer": "A",
        "explanation": "L'alimentation des internés d'urgence et le risque vital justifient souvent l'urgence impérieuse permettant de déroger temporairement à la mise en concurrence."
    },
    {
        "question": "Cas pratique 68 : L'entreprise omet de publier son avis d'attribution dans le Bulletin Officiel des Marchés Publics de Côte d'Ivoire.",
        "options": ["A) Vice sans conséquence.", "B) La publicité de l'attribution est une formalité substantielle, son absence rend le marché attaquable par les tiers évincés.", "C) Seule l'ARCOP est punie.", "D) La DMP corrige elle-même."],
        "answer": "B",
        "explanation": "La transparence de la commande publique exige la publication des résultats pour permettre les recours des candidats évincés."
    },
    {
        "question": "Cas pratique 69 : L'État exproprie pour cause d'utilité publique, mais au bout de 10 ans, le terrain est laissé en friche et abandonné.",
        "options": ["A) L'État peut le garder indéfiniment.", "B) Le propriétaire initial a un droit de rétrocession (reprise du bien moyennant remboursement) si l'affectation à l'utilité publique n'a pas été réalisée.", "C) Le domaine public est prescrit.", "D) Il doit être donné à la commune."],
        "answer": "B",
        "explanation": "En cas de défaut prolongé de réalisation de l'affectation d'utilité publique justifiant l'expropriation, l'ancien propriétaire peut exercer son droit de rétrocession."
    },
    {
        "question": "Cas pratique 70 : L'État signe un contrat d'occupation du domaine public avec un affichiste pour des panneaux. Le Préfet révoque l'autorisation 2 mois après pour installer un rond-point.",
        "options": ["A) L'affichiste ne peut rien dire.", "B) L'autorisation est précaire et révocable à tout moment pour motif d'intérêt général (moyennant indemnisation si convention le prévoit, souvent non).", "C) Le rond-point est illégal.", "D) L'affichiste est indemnisé à 100% systématiquement."],
        "answer": "B",
        "explanation": "Toute permission de voirie ou AOT sur le domaine public est par essence précaire et révocable sans indemnité de droit pour des motifs d'intérêt général tenant au domaine."
    },
    {
        "question": "Cas pratique 71 : La construction de l'Université de San Pedro est retardée à cause de pluies exceptionnelles qualifiées de catastrophe naturelle par l'État.",
        "options": ["A) Force majeure : aucune pénalité de retard, délai prorogé.", "B) Imprévision : indemnisation partielle.", "C) Fait du prince.", "D) Pénalité maintenue."],
        "answer": "A",
        "explanation": "La catastrophe naturelle imprévisible et irrésistible retarde légitimement le chantier, entraînant une exonération des pénalités (force majeure)."
    },
    {
        "question": "Cas pratique 72 : La Présidence achète directement des hélicoptères de combat. Procédure ?",
        "options": ["A) Gré à gré 'secret défense' autorisé sans publicité.", "B) Appel d'offres restreint obligatoire.", "C) Appel d'offres ouvert impératif.", "D) Interdiction d'achat par l'État."],
        "answer": "A",
        "explanation": "Les marchés liés à la sécurité de l'État (secret défense) dérogent aux règles de transparence et se passent de gré à gré exclusif."
    },
    {
        "question": "Cas pratique 73 : Un concurrent évincé découvre que l'attributaire n'a pas payé ses impôts en CI.",
        "options": ["A) Le marché est néanmoins valable.", "B) Le marché est illégal. Être en règle fiscalement est une condition sine qua non de participation (dossier administratif).", "C) L'attributaire paiera après.", "D) L'ARCOP le protège."],
        "answer": "B",
        "explanation": "Le Code des marchés publics exige que tout soumissionnaire prouve être à jour de ses cotisations fiscales et sociales. À défaut, son offre est irrecevable."
    },
    {
        "question": "Cas pratique 74 : Le Ministre de la Fonction Publique signe un contrat pour la construction de logements sociaux (ne relève pas de ses attributions).",
        "options": ["A) Validité.", "B) Incompétence matérielle (nullité de l'acte).", "C) Validation par le Conseil d'État.", "D) Incompétence temporelle."],
        "answer": "B",
        "explanation": "Le signataire d'un contrat de l'Administration doit agir dans les limites de ses attributions matérielles (domaine de compétence). Sinon le contrat est entaché d'incompétence matérielle."
    },
    {
        "question": "Cas pratique 75 : L'entreprise BATI-CI a sous-évalué son offre (dumping). Elle réclame au bout d'un mois une indemnité d'imprévision car elle perd de l'argent.",
        "options": ["A) Indemnité d'imprévision accordée.", "B) Rejet : l'imprévision suppose un fait extérieur, pas la propre erreur de prévision économique du cocontractant.", "C) Fait du prince.", "D) Sujétions imprévues."],
        "answer": "B",
        "explanation": "La théorie de l'imprévision ne couvre jamais le défaut de prévoyance de l'entrepreneur, ni son erreur de calcul initiale (risque normal d'entreprise)."
    },
    {
        "question": "Cas pratique 76 : Une église est construite sur un terrain sans titre de l'État. L'État détruit au bulldozer un dimanche.",
        "options": ["A) Voie de fait car l'église est un lieu de culte et la destruction hors urgence sans décision de justice est gravement illégale.", "B) Exécution d'office légale.", "C) Fait du prince.", "D) Domaine public inaliénable."],
        "answer": "A",
        "explanation": "En l'absence d'urgence impérieuse ou de loi l'autorisant expressément, l'exécution forcée par l'Administration d'une décision d'expulsion (destruction) d'une emprise privée/lieu de culte est une voie de fait."
    },
    {
        "question": "Cas pratique 77 : La commune confie la collecte des taxes de marché à une structure privée, qui gardera 20% des sommes perçues.",
        "options": ["A) C'est légal, c'est une concession de service public.", "B) C'est illégal : par principe, la perception de l'impôt et des taxes relève de la souveraineté de l'État (sauf régie habilitée), on ne concède pas la puissance fiscale.", "C) Marché public de services.", "D) C'est légal sans condition."],
        "answer": "B",
        "explanation": "Certaines activités inhérentes à la souveraineté de l'État (police, impôts de l'État stricto sensu) ne peuvent pas faire l'objet d'une délégation de service public."
    },
    {
        "question": "Cas pratique 78 : Le gouvernement ivoirien adopte une mesure générale de hausse du SMIG. Les entreprises de nettoyage sous contrat avec l'État voient leurs charges salariales exploser et demandent indemnisation (Fait du Prince).",
        "options": ["A) Le Fait du Prince s'applique toujours.", "B) Le Fait du Prince ne s'applique pas car la mesure est d'ordre général et non spécifique aux cocontractants (éventuellement imprévision si cela bouleverse l'économie).", "C) Force majeure.", "D) Résiliation d'office."],
        "answer": "B",
        "explanation": "Une mesure législative ou réglementaire de portée générale (comme la hausse du SMIG ou des impôts généraux) ne constitue pas un Fait du Prince indemnisable intégralement, à l'inverse d'une mesure spécifique au contrat."
    },
    {
        "question": "Cas pratique 79 : Une route nationale est désaffectée de fait (elle n'est plus utilisée, envahie par la forêt). M. DIOMANDE l'occupe et demande la prescription acquisitive au bout de 30 ans.",
        "options": ["A) Il gagne, la route n'étant plus affectée.", "B) Il perd, car sans déclassement juridique formel, la désaffectation de fait ne suffit pas à faire sortir le bien du domaine public (il reste inaliénable).", "C) La route appartient à la forêt.", "D) Il gagne après 10 ans."],
        "answer": "B",
        "explanation": "Un bien du domaine public ne perd son caractère public que par l'effet cumulé d'une désaffectation matérielle et d'un acte de déclassement exprès. À défaut, l'imprescriptibilité demeure."
    },
    {
        "question": "Cas pratique 80 : Lors de l'exécution d'un marché public, les plans fournis par l'architecte de l'Administration sont gravement erronés, entraînant la destruction de l'ouvrage.",
        "options": ["A) C'est la faute exclusive de l'entrepreneur.", "B) La responsabilité de l'Administration (maître d'ouvrage public) est engagée (faute lourde ou fait de l'Administration).", "C) Force majeure.", "D) Imprévision."],
        "answer": "B",
        "explanation": "Les fautes commises par les services de l'Administration (ou ses mandataires, ex: plans erronés) engagent sa responsabilité à l'égard de l'entrepreneur, limitant ou supprimant celle de ce dernier."
    },
    {
        "question": "Cas pratique 81 : Le Conseil Régional du Poro décide de rompre unilatéralement son marché de construction d'une route car 'le Président du Conseil a changé et n'aime pas le style de la route'.",
        "options": ["A) Résiliation pour faute.", "B) Résiliation illégale (détournement de pouvoir ou motif étranger à l'intérêt général).", "C) Résiliation pour intérêt général valable.", "D) Modification unilatérale."],
        "answer": "B",
        "explanation": "La résiliation unilatérale pour motif d'intérêt général doit être justifiée par de réelles nécessités de service public, et non par des convenances personnelles ou politiques (détournement de pouvoir)."
    },
    {
        "question": "Cas pratique 82 : La Mairie cède de gré à gré une parcelle de son domaine privé à un investisseur à un prix dérisoire (1 franc symbolique) pour y construire un casino privé.",
        "options": ["A) C'est légal pour attirer des touristes.", "B) Cession à vil prix illégale (interdiction pour les personnes publiques de consentir des libéralités ou ventes à prix symbolique sans forte contrepartie d'intérêt général).", "C) L'ARCOP annule.", "D) C'est une concession."],
        "answer": "B",
        "explanation": "La vente d'un bien du domaine privé d'une personne publique à un prix inférieur à sa valeur vénale est illégale, sauf si elle est justifiée par un motif d'intérêt général et assortie de contreparties suffisantes."
    },
    {
        "question": "Cas pratique 83 : Une commune attribue un marché d'assainissement de 1 milliard à une PME locale créée la veille, sans références, alors qu'une multinationale avait concouru.",
        "options": ["A) C'est légal pour favoriser les PME.", "B) Illégal, violation des critères de qualification technique et financière exigés dans les dossiers d'appel d'offres.", "C) L'ARCOP félicite la commune.", "D) L'État paiera la différence."],
        "answer": "B",
        "explanation": "L'attribution d'un marché doit se fonder sur l'examen rigoureux des capacités techniques, financières et professionnelles (références) du soumissionnaire tel qu'exigé par la réglementation."
    },
    {
        "question": "Cas pratique 84 : Lors de la construction d'un barrage, l'État ivoirien exige de l'entreprise SINO-HYDRO de construire un pont supplémentaire non prévu au contrat (qui dépasse 50% de la valeur initiale du contrat).",
        "options": ["A) SINO-HYDRO doit s'exécuter unilatéralement.", "B) Le bouleversement (modification dépassant le seuil légal de l'avenant) est tel qu'il sort de l'épure du contrat. L'entreprise peut refuser et demander un nouveau marché.", "C) Imprévision totale.", "D) Régie d'office obligatoire."],
        "answer": "B",
        "explanation": "Le pouvoir de modification unilatérale trouve sa limite dans le bouleversement de l'objet ou de l'économie du contrat (travaux constituant un projet nouveau). L'entrepreneur n'est pas tenu de les accepter."
    },
    {
        "question": "Cas pratique 85 : Un fonctionnaire du CHU achète des médicaments pour l'hôpital sur ses fonds propres en cas de rupture de stock, de son propre chef. Il demande remboursement (théorie de l'enrichissement sans cause/gestion d'affaires).",
        "options": ["A) Il ne sera jamais remboursé.", "B) La jurisprudence admet parfois le remboursement (quasi-contrat) si les dépenses ont été utiles à l'Administration et de bonne foi (enrichissement sans cause).", "C) Il sera révoqué.", "D) Il s'agit d'un marché public occulte."],
        "answer": "B",
        "explanation": "Les quasi-contrats administratifs (enrichissement sans cause de l'Administration) permettent d'indemniser une personne (même un agent) ayant exposé des frais utiles pour la collectivité de bonne foi."
    },
    {
        "question": "Cas pratique 86 : Le Ministère passe un marché avec l'entreprise Z et précise : 'aucun recours juridictionnel n'est possible, seule l'ARCOP est compétente en dernier ressort'.",
        "options": ["A) Clause licite.", "B) Clause réputée non écrite : on ne peut interdire l'accès au juge (Conseil d'État) par voie contractuelle (ordre public).", "C) Clause validée par l'ARCOP.", "D) L'OHADA s'applique."],
        "answer": "B",
        "explanation": "Le droit d'exercer un recours juridictionnel devant le juge de l'excès de pouvoir ou de plein contentieux administratif est un principe général du droit à valeur constitutionnelle. Une clause d'interdiction est nulle."
    },
    {
        "question": "Cas pratique 87 : Une entreprise de cantine scolaire continue de fournir des repas à l'école alors que son marché est expiré depuis 6 mois, avec l'accord verbal du Directeur.",
        "options": ["A) Elle a droit à 100% de la valeur du contrat (maintien du contrat).", "B) Le contrat est expiré, mais l'entreprise a droit à l'indemnisation de ses dépenses utiles sur la base de l'enrichissement sans cause (quasi-contrat) sans marge bénéficiaire.", "C) Elle ne perçoit absolument rien.", "D) Le Directeur paie de sa poche."],
        "answer": "B",
        "explanation": "Les prestations fournies hors contrat (marché expiré) sont indemnisées au titre de l'enrichissement sans cause de l'Administration, excluant la marge bénéficiaire de l'entreprise."
    },
    {
        "question": "Cas pratique 88 : L'ARCOP annule la décision d'attribution du marché de l'ONAD à la société X, suite au recours de la société Y. L'ONAD refuse de s'y soumettre.",
        "options": ["A) L'ONAD est souveraine.", "B) Les décisions de l'ARCOP ont un caractère contraignant et s'imposent à l'autorité contractante.", "C) La société Y doit saisir la CEDEAO.", "D) Le Ministre a le dernier mot."],
        "answer": "B",
        "explanation": "En Côte d'Ivoire, l'organe de régulation (ARCOP) rend des décisions exécutoires dans la phase de passation des marchés publics, qui s'imposent à l'Administration, sous réserve d'un recours au Conseil d'État."
    },
    {
        "question": "Cas pratique 89 : Le Préfet d'Agboville décide de déclarer d'utilité publique l'expropriation d'un terrain pour y installer sa propre résidence privée.",
        "options": ["A) C'est légal.", "B) Détournement de pouvoir (l'expropriation ne sert pas l'intérêt général mais un intérêt privé). Annulation de la DUP.", "C) Le propriétaire est doublement indemnisé.", "D) Validation par le juge judiciaire."],
        "answer": "B",
        "explanation": "L'expropriation pour cause d'utilité publique doit avoir pour but exclusif la satisfaction d'un intérêt public réel. L'utiliser pour un intérêt privé est un cas d'école de détournement de pouvoir."
    },
    {
        "question": "Cas pratique 90 : M. OUATTARA loue un local de la Mairie situé dans le domaine privé. Le Maire résilie le bail pour non-paiement. Juge compétent ?",
        "options": ["A) Conseil d'État.", "B) Juge judiciaire (Tribunal de Première Instance) car le bail du domaine privé est un contrat de droit privé.", "C) ARCOP.", "D) Tribunal administratif."],
        "answer": "B",
        "explanation": "La gestion du domaine privé (notamment les baux à loyer ordinaires) ressortit au droit privé et relève donc des juridictions judiciaires (sauf clause exorbitante)."
    },
    {
        "question": "Cas pratique 91 : L'entreprise BTP a mal exécuté le toit de la Mairie, qui s'effondre 8 ans après la réception définitive des travaux sans réserve.",
        "options": ["A) La garantie est éteinte.", "B) La responsabilité décennale des constructeurs s'applique (garantie de 10 ans pour les gros ouvrages).", "C) La Mairie paie les réparations.", "D) Force majeure."],
        "answer": "B",
        "explanation": "En matière de travaux publics, la garantie décennale oblige l'entrepreneur (et l'architecte) à réparer les vices cachés compromettant la solidité de l'ouvrage survenant dans les 10 ans suivant la réception."
    },
    {
        "question": "Cas pratique 92 : Le sous-sol de la résidence de l'Ambassadeur de France en CI regorge d'or. L'État ivoirien veut l'exploiter. A qui appartient ce sous-sol ?",
        "options": ["A) À la France.", "B) À l'Ambassadeur.", "C) À l'État ivoirien (le domaine minier appartient à l'État, peu importe le propriétaire de la surface).", "D) À personne (res nullius)."],
        "answer": "C",
        "explanation": "Selon le Code minier ivoirien, les gisements naturels du sous-sol (mines) appartiennent à l'État de Côte d'Ivoire. Le propriétaire du sol n'est pas propriétaire du sous-sol minier."
    },
    {
        "question": "Cas pratique 93 : Une délégation de service public confie la collecte des péages de l'autoroute du Nord au Fond d'Entretien Routier (FER). Les péages sont perçus en son nom.",
        "options": ["A) Le FER est une régie.", "B) Le FER est un concessionnaire qui assume les risques d'exploitation (rémunéré par les usagers).", "C) Le FER est une ONG.", "D) Les péages sont illégaux."],
        "answer": "B",
        "explanation": "Le concessionnaire de service public se distingue par le fait qu'il est rémunéré substantiellement par les résultats de l'exploitation (les redevances des usagers), assumant ainsi un risque économique."
    },
    {
        "question": "Cas pratique 94 : L'Administration omet d'indiquer la voie et les délais de recours dans la notification de résiliation du marché de l'entreprise X.",
        "options": ["A) La décision est nulle.", "B) L'absence de cette mention a pour effet de rendre le délai de recours contentieux (habituellement 2 mois) inopposable à l'entreprise, qui peut attaquer sans délai.", "C) L'ARCOP annule.", "D) Rien ne change."],
        "answer": "B",
        "explanation": "En droit administratif ivoirien, le délai de recours ne court à l'encontre de l'administré que si la notification de la décision mentionne expressément les voies et délais de recours. À défaut, le délai ne court pas."
    },
    {
        "question": "Cas pratique 95 : Une autorité ivoirienne lance un appel d'offres international. Elle demande aux candidats d'écrire leurs offres en anglais.",
        "options": ["A) C'est légal pour s'ouvrir au monde.", "B) Illégal, la Constitution ivoirienne dispose que le français est la langue officielle, les offres de marchés publics en CI doivent être rédigées ou traduites en français.", "C) L'ARCOP choisira l'anglais.", "D) C'est selon l'envie du Ministre."],
        "answer": "B",
        "explanation": "Les procédures de passation des marchés publics de l'État de Côte d'Ivoire requièrent formellement l'usage de la langue française, langue officielle de la République."
    },
    {
        "question": "Cas pratique 96 : L'entreprise étrangère KAGAME BTP conteste un marché ivoirien parce qu'une prime de préférence nationale de 15% a été accordée à l'entreprise ivoirienne SORO BTP.",
        "options": ["A) C'est du favoritisme illégal.", "B) C'est légal, le Code des marchés publics ivoirien et communautaire (UEMOA) consacre une marge de préférence communautaire/nationale (jusqu'à 15%) pour les entreprises locales.", "C) La prime est limitée à 5%.", "D) C'est l'OHADA qui régit ça."],
        "answer": "B",
        "explanation": "La préférence nationale et communautaire est légalement prévue et encadrée dans les marchés publics de la zone UEMOA afin de favoriser les entreprises régionales."
    },
    {
        "question": "Cas pratique 97 : Une entreprise gagne un marché de 50 millions FCFA. Le contrat est signé, mais la Direction des Marchés Publics refuse son visa pour une erreur formelle.",
        "options": ["A) Le marché est exécutoire sans visa.", "B) Le contrat n'entre pas en vigueur : le visa de la DMP (et/ou l'approbation de l'autorité compétente) est une formalité substantielle de l'existence juridique du contrat.", "C) L'entreprise doit poursuivre.", "D) L'ARCOP obligera le visa."],
        "answer": "B",
        "explanation": "Un marché public ne devient exécutoire et définitif qu'après son approbation par l'autorité compétente, sanctionnée souvent par l'immatriculation ou le visa de contrôle."
    },
    {
        "question": "Cas pratique 98 : Le Maire de San Pedro met fin à une concession de plage pour faute grave de l'exploitant, mais ne précise pas le motif dans la lettre de résiliation.",
        "options": ["A) La résiliation est légale, le maire n'a pas à se justifier.", "B) Vice de forme (défaut de motivation). Une sanction doit être obligatoirement motivée en fait et en droit.", "C) Le préfet motivera plus tard.", "D) La plage est du domaine privé."],
        "answer": "B",
        "explanation": "Les décisions administratives défavorables, et notamment les actes infligeant une sanction (comme la résiliation pour faute), doivent être expressément motivées pour permettre le contrôle du juge."
    },
    {
        "question": "Cas pratique 99 : La Société Nationale des Autoroutes perçoit une taxe sur chaque kilomètre parcouru, mais les péages ne sont ni entretenus ni éclairés. L'association des usagers porte plainte.",
        "options": ["A) Les usagers ont toujours tort.", "B) Les redevances pour service rendu doivent correspondre à un service effectivement rendu. En l'absence d'entretien, le service est défaillant, engageant la responsabilité du concessionnaire.", "C) C'est un impôt direct.", "D) La route appartient à la CEDEAO."],
        "answer": "B",
        "explanation": "La redevance (contrairement à l'impôt) est la contrepartie financière d'un service rendu (péage = droit d'usage d'une infrastructure entretenue). Le défaut d'entretien constitue une inexécution contractuelle (ou quasi-délictuelle vis-à-vis de l'usager)."
    },
    {
        "question": "Cas pratique 100 : En Côte d'Ivoire, l'ARCOP, lors d'un audit a posteriori, découvre qu'un marché public de 10 milliards a été attribué de manière fictive. Le marché est entièrement exécuté et payé.",
        "options": ["A) L'ARCOP ne peut rien faire, c'est payé.", "B) L'ARCOP peut saisir le Procureur de la République pour des poursuites pénales (détournement de deniers publics, corruption) contre les auteurs et l'entreprise.", "C) L'ARCOP détruit l'ouvrage.", "D) Le Conseil d'État ordonne le remboursement."],
        "answer": "B",
        "explanation": "L'ARCOP mène des audits réguliers. Lorsqu'elle décèle des infractions pénales (fraude, corruption, faux) dans un marché (même exécuté), elle a l'obligation d'en référer aux autorités judiciaires (Tribunal, Pôle pénal financier)."
    },
    {
        "question": "Cas pratique 1 : Sieur KPANGO subit une intervention au CHU de Cocody. Une pince est oubliée. Régime de responsabilité ?",
        "options": ["A) Sans faute", "B) Faute lourde", "C) Faute simple de service", "D) Faute personnelle"],
        "answer": "C",
        "explanation": "La faute médicale au CHU relève de la faute simple de service."
    },
    {
        "question": "Cas pratique 2 : Lors d'une manifestation, DJ MÔKÔ, passant, est blessé par un tir policier. Régime applicable ?",
        "options": ["A) Faute lourde", "B) Sans faute pour risque", "C) Faute personnelle", "D) Aucune responsabilité"],
        "answer": "B",
        "explanation": "Les tiers aux opérations de police bénéficient de la responsabilité sans faute."
    },
    {
        "question": "Cas pratique 3 : Le Maire d'Agboville interdit un concert sans motif. Analyse ?",
        "options": ["A) Légal, pouvoir discrétionnaire", "B) Illégal, contrôle de proportionnalité", "C) Légal avec accord préfet", "D) Illégal pour incompétence"],
        "answer": "B",
        "explanation": "Atteinte disproportionnée à la liberté (Arrêt Benjamin)."
    },
    {
        "question": "Cas pratique 4 : Dame AFFOUÉ tombe dans un trou non signalé de l'AGEROUTE. Régime ?",
        "options": ["A) Faute prouvée", "B) Défaut d'entretien normal", "C) Faute lourde", "D) Responsabilité de la mairie"],
        "answer": "B",
        "explanation": "L'usager bénéficie de la présomption de défaut d'entretien normal de l'ouvrage public."
    },
    {
        "question": "Cas pratique 5 : Refus de concours de la force publique pour expulser des squatteurs. Régime ?",
        "options": ["A) Faute simple", "B) Sans faute (rupture d'égalité)", "C) Faute lourde", "D) Irresponsabilité"],
        "answer": "B",
        "explanation": "Jurisprudence Couitéas, responsabilité sans faute pour préjudice anormal et spécial."
    },
    {
        "question": "Cas pratique 6 : Un arrêté préfectoral interdit toutes les réunions ad vitam aeternam. Légalité ?",
        "options": ["A) Illégal (général et absolu)", "B) Légal", "C) Acte de gouvernement", "D) Légal en crise"],
        "answer": "A",
        "explanation": "Une mesure de police ne peut être générale et absolue."
    },
    {
        "question": "Cas pratique 7 : M. TOURE glisse sur un sol mouillé sans panneau au CHU. Responsabilité ?",
        "options": ["A) Faute personnelle", "B) Faute de service", "C) Sans faute", "D) Force majeure"],
        "answer": "B",
        "explanation": "Négligence dans l'organisation du service engage la responsabilité de l'hôpital."
    },
    {
        "question": "Cas pratique 8 : Gendarme frappant par vengeance avec son arme de service. Analyse ?",
        "options": ["A) Faute de service exclusive", "B) Faute personnelle sans lien", "C) Cumul de responsabilités (Lemonnier)", "D) Sans faute"],
        "answer": "C",
        "explanation": "Faute personnelle commise avec les moyens du service."
    },
    {
        "question": "Cas pratique 9 : Pont en construction effondré blessant un ouvrier de l'entreprise. Régime ?",
        "options": ["A) Sans faute de l'Etat", "B) Droit du travail / sécurité sociale", "C) Faute lourde", "D) Faute de service"],
        "answer": "B",
        "explanation": "Les participants aux travaux publics relèvent du droit du travail."
    },
    {
        "question": "Cas pratique 10 : Arbre abattu par la mairie tombant sur une voiture. Régime ?",
        "options": ["A) Sans faute (tiers)", "B) Faute prouvée", "C) Défaut d'entretien", "D) Force majeure"],
        "answer": "A",
        "explanation": "Responsabilité sans faute pour le tiers par rapport à l'ouvrage public."
    },
    {
        "question": "Cas pratique 11 : Maire détruisant une maison menaçant ruine. But de police ?",
        "options": ["A) Salubrité et sécurité", "B) Tranquillité", "C) Esthétique", "D) Moralité"],
        "answer": "A",
        "explanation": "La sécurité publique est visée pour prévenir un effondrement."
    },
    {
        "question": "Cas pratique 12 : Inaction de l'administration face à une épidémie. Responsabilité ?",
        "options": ["A) Faute de service (carence)", "B) Acte de gouvernement", "C) Sans faute", "D) Irresponsabilité"],
        "answer": "A",
        "explanation": "La carence de police ou d'organisation constitue une faute de service."
    },
    {
        "question": "Cas pratique 13 : Malade psychiatrique dangereux échappé. Régime ?",
        "options": ["A) Faute de surveillance (service)", "B) Sans faute", "C) Faute lourde", "D) Faute personnelle"],
        "answer": "A",
        "explanation": "Le défaut de surveillance d'un patient dangereux est une faute de service."
    },
    {
        "question": "Cas pratique 14 : Policier hors service utilisant son arme pour un meurtre. Régime ?",
        "options": ["A) Faute de service", "B) Cumul (arme de service)", "C) Détachable", "D) Sans faute"],
        "answer": "B",
        "explanation": "L'utilisation de l'arme de service permet d'engager la responsabilité de l'Etat."
    },
    {
        "question": "Cas pratique 15 : Interdiction de lancer de nains. Motif ?",
        "options": ["A) Dignité humaine", "B) Tranquillité", "C) Sécurité", "D) Esthétique"],
        "answer": "A",
        "explanation": "La dignité humaine est une composante de l'ordre public (Morsang-sur-Orge)."
    },
    {
        "question": "Cas pratique 16 : Pompiers en retard pour panne matérielle non entretenue. Régime ?",
        "options": ["A) Faute lourde", "B) Faute simple", "C) Sans faute", "D) Force majeure"],
        "answer": "B",
        "explanation": "La jurisprudence exige désormais une faute simple pour ce dysfonctionnement."
    },
    {
        "question": "Cas pratique 17 : Policier frappant un contrevenant insolent. Juge compétent ?",
        "options": ["A) Juge administratif (faute service)", "B) Juge pénal", "C) Juge civil", "D) Tribunal des conflits"],
        "answer": "A",
        "explanation": "Si faute de service, compétence du juge administratif (TC Pelletier)."
    },
    {
        "question": "Cas pratique 18 : Loi d'amnistie causant préjudice. Régime ?",
        "options": ["A) Faute", "B) Sans faute du fait des lois", "C) Irresponsabilité", "D) Force majeure"],
        "answer": "B",
        "explanation": "Responsabilité sans faute de l'Etat législateur (La Fleurette)."
    },
    {
        "question": "Cas pratique 19 : Interdiction réunion pour critique gouvernementale. Analyse ?",
        "options": ["A) Légal", "B) Détournement de pouvoir", "C) Ordre public", "D) Acte de gouvernement"],
        "answer": "B",
        "explanation": "La police ne doit poursuivre que le maintien matériel de l'ordre, non la censure."
    },
    {
        "question": "Cas pratique 20 : Camion poubelle renversant un piéton. Juge compétent ?",
        "options": ["A) Administratif", "B) Judiciaire", "C) Tribunal des conflits", "D) Pénal seul"],
        "answer": "B",
        "explanation": "Exception légale (loi 1957) attribuant le contentieux des véhicules au juge judiciaire."
    },
    {
        "question": "Cas pratique 21 : Fermeture d'un maquis très bruyant après avertissements. Analyse ?",
        "options": ["A) Illégal", "B) Légal (tranquillité publique proportionnée)", "C) Actes de gouvernement", "D) Faute lourde"],
        "answer": "B",
        "explanation": "Mesure proportionnée pour assurer la tranquillité publique."
    },
    {
        "question": "Cas pratique 22 : Transfusion sanguine et VIH au CHU. Régime ?",
        "options": ["A) Faute lourde", "B) Faute simple", "C) Sans faute pour risque", "D) Force majeure"],
        "answer": "C",
        "explanation": "Les contaminations transfusionnelles engagent la responsabilité sans faute de l'hôpital."
    },
    {
        "question": "Cas pratique 23 : Réquisition de stations-service en crise. Théorie ?",
        "options": ["A) Circonstances exceptionnelles", "B) Pouvoir discrétionnaire", "C) Acte de gouvernement", "D) Faute lourde"],
        "answer": "A",
        "explanation": "En période de crise, les pouvoirs de police sont élargis (Arrêt Heyriès)."
    },
    {
        "question": "Cas pratique 24 : Refus illégal de passeport causant dommage. Régime ?",
        "options": ["A) Faute de service", "B) Sans faute", "C) Irresponsabilité", "D) Faute personnelle"],
        "answer": "A",
        "explanation": "Toute illégalité fautive engage la responsabilité de l'administration."
    },
    {
        "question": "Cas pratique 25 : Feu d'artifice de la commune blessant un spectateur. Régime ?",
        "options": ["A) Sans faute pour activité dangereuse", "B) Faute simple", "C) Faute lourde", "D) Force majeure"],
        "answer": "A",
        "explanation": "Activité dangereuse créant un risque anormal pour les tiers."
    },
    {
        "question": "Cas pratique 26 : Agent des douanes volant des marchandises saisies. Responsabilité de l'Etat ?",
        "options": ["A) Aucune, faute personnelle détachable", "B) Faute de service", "C) Cumul", "D) Sans faute"],
        "answer": "A",
        "explanation": "Le vol est une faute personnelle dépourvue de tout lien avec le service."
    },
    {
        "question": "Cas pratique 27 : Erreur de diagnostic d'un médecin du CHU Yopougon. Régime ?",
        "options": ["A) Faute lourde", "B) Faute simple", "C) Sans faute", "D) Force majeure"],
        "answer": "B",
        "explanation": "L'exigence de faute lourde médicale a été abandonnée."
    },
    {
        "question": "Cas pratique 28 : Effondrement de la toiture d'une mairie sur un usager. Régime ?",
        "options": ["A) Défaut d'entretien normal", "B) Faute prouvée", "C) Sans faute (tiers)", "D) Force majeure"],
        "answer": "A",
        "explanation": "Responsabilité présumée pour défaut d'entretien de l'ouvrage public (usager)."
    },
    {
        "question": "Cas pratique 29 : Dommage causé par un attroupement violent ciblant la préfecture. Régime ?",
        "options": ["A) Responsabilité de l'Etat (attroupement)", "B) Faute de service", "C) Faute personnelle", "D) Irresponsabilité"],
        "answer": "A",
        "explanation": "Régime spécial de responsabilité de l'Etat pour les dommages des attroupements."
    },
    {
        "question": "Cas pratique 30 : Injonction du maire de démolir un mur clôture sans péril imminent. Analyse ?",
        "options": ["A) Illégal (empiètement judiciaire)", "B) Légal", "C) Pouvoir de police général", "D) Circonstance exceptionnelle"],
        "answer": "A",
        "explanation": "Sans péril imminent, la voie de fait ou l'illégalité est caractérisée."
    },
    {
        "question": "Cas pratique 31 : Agent ivoirien tabasse un détenu à la MACA. Régime ?",
        "options": ["A) Faute personnelle", "B) Faute de service", "C) Cumul de responsabilités", "D) Sans faute"],
        "answer": "C",
        "explanation": "Faute personnelle (violence) commise à l'occasion du service (MACA)."
    },
    {
        "question": "Cas pratique 32 : Ministre prend un décret rétroactif causant dommage. Régime ?",
        "options": ["A) Faute de service (illégalité)", "B) Sans faute", "C) Acte gouvernement", "D) Irresponsabilité"],
        "answer": "A",
        "explanation": "Un acte illégal (rétroactivité) est une faute de service."
    },
    {
        "question": "Cas pratique 33 : Maire réglemente la circulation pour cause de travaux publics. Légalité ?",
        "options": ["A) Légal (police de la circulation)", "B) Illégal", "C) Seul le préfet peut", "D) Incompétence"],
        "answer": "A",
        "explanation": "Le maire dispose de la police de la circulation sur sa commune."
    },
    {
        "question": "Cas pratique 34 : Promeneur blessé par un tir de militaire à l'entraînement. Régime ?",
        "options": ["A) Sans faute (risque)", "B) Faute lourde", "C) Défaut d'entretien", "D) Faute personnelle"],
        "answer": "A",
        "explanation": "L'utilisation d'armes à feu engage la responsabilité sans faute de l'Etat pour les tiers."
    },
    {
        "question": "Cas pratique 35 : Dommages causés par l'exécution d'un traité international. Régime ?",
        "options": ["A) Sans faute (égalité devant les charges publiques)", "B) Faute", "C) Acte gouvernement inattaquable", "D) Faute lourde"],
        "answer": "A",
        "explanation": "Jurisprudence Compagnie Générale d'Energie Radioélectrique (indemnisation possible)."
    },
    {
        "question": "Cas pratique 36 : Morsure par un chien policier lors d'une traque. Régime pour le suspect ?",
        "options": ["A) Faute (si l'utilisation du chien est fautive)", "B) Sans faute (tiers)", "C) Force majeure", "D) Faute personnelle"],
        "answer": "A",
        "explanation": "Pour la personne visée par la police, il faut prouver une faute (souvent simple)."
    },
    {
        "question": "Cas pratique 37 : Patient s'échappe de l'hôpital et se suicide. Responsabilité de l'hôpital ?",
        "options": ["A) Faute dans l'organisation (surveillance)", "B) Sans faute", "C) Force majeure", "D) Irresponsabilité"],
        "answer": "A",
        "explanation": "Défaut de surveillance d'un patient à risque suicidaire connu est une faute de service."
    },
    {
        "question": "Cas pratique 38 : Maire d'Abobo instaure un couvre-feu permanent sans motif précis. Légalité ?",
        "options": ["A) Illégal (disproportionné)", "B) Légal", "C) Circonstance exceptionnelle", "D) Légal si visé par le préfet"],
        "answer": "A",
        "explanation": "Mesure générale et absolue non justifiée par les circonstances (Arrêt Daudignac/Benjamin)."
    },
    {
        "question": "Cas pratique 39 : KPAKPATO heurte un panneau de signalisation tombé sur la route. Régime ?",
        "options": ["A) Défaut d'entretien normal", "B) Sans faute pour tiers", "C) Faute prouvée", "D) Irresponsabilité"],
        "answer": "A",
        "explanation": "L'usager de l'ouvrage public bénéficie de la présomption de défaut d'entretien."
    },
    {
        "question": "Cas pratique 40 : Un ministre refuse d'exécuter un arrêt du Conseil d'Etat. Responsabilité ?",
        "options": ["A) Faute de service", "B) Acte de gouvernement", "C) Sans faute", "D) Voie de fait"],
        "answer": "A",
        "explanation": "Le refus d'exécuter la chose jugée est une illégalité fautive."
    },
    {
        "question": "Cas pratique 41 : Policier ivre en service blesse un collègue. Régime ?",
        "options": ["A) Cumul de responsabilités", "B) Sans faute", "C) Faute exclusive de l'administration", "D) Faute personnelle pure"],
        "answer": "A",
        "explanation": "Faute personnelle détachable commise pendant le service."
    },
    {
        "question": "Cas pratique 42 : Travaux bruyants d'un hôpital la nuit causant un préjudice au voisinage. Régime ?",
        "options": ["A) Sans faute (dommage permanent de TP)", "B) Faute", "C) Défaut d'entretien", "D) Force majeure"],
        "answer": "A",
        "explanation": "Le tiers voisin d'un ouvrage public subissant des nuisances anormales est indemnisé sans faute."
    },
    {
        "question": "Cas pratique 43 : Coupure d'électricité prolongée (CIE) causant la perte de stocks d'un boucher. Régime ?",
        "options": ["A) Défaut d'entretien ou faute contractuelle du concessionnaire", "B) Sans faute", "C) Force majeure automatique", "D) Irresponsabilité"],
        "answer": "A",
        "explanation": "Le concessionnaire (CIE) est responsable du fonctionnement du service (faute présumée ou prouvée)."
    },
    {
        "question": "Cas pratique 44 : Maire interdit le port du masque sanitaire pour esthétique. Légalité ?",
        "options": ["A) Illégal (incompétence et détournement)", "B) Légal", "C) Salubrité publique", "D) Moralité"],
        "answer": "A",
        "explanation": "Le maire ne peut s'opposer aux règles sanitaires nationales pour des motifs esthétiques mineurs."
    },
    {
        "question": "Cas pratique 45 : Retard abusif dans la délivrance d'un permis de construire. Responsabilité ?",
        "options": ["A) Faute de service", "B) Sans faute", "C) Faute lourde", "D) Irresponsabilité"],
        "answer": "A",
        "explanation": "Le retard illégal et excessif engage la responsabilité pour faute de l'administration."
    },
    {
        "question": "Cas pratique 46 : Dommage lié à la méthode éducative libérale dans un centre pour délinquants. Régime ?",
        "options": ["A) Sans faute pour risque", "B) Faute", "C) Défaut d'entretien", "D) Faute personnelle"],
        "answer": "A",
        "explanation": "L'utilisation de méthodes dangereuses pour les tiers (Arrêt Thouzellier) engage la responsabilité sans faute."
    },
    {
        "question": "Cas pratique 47 : Enseignant du public blesse un élève en le frappant. Régime ?",
        "options": ["A) Loi du 5 avril 1937 (substitution de l'Etat)", "B) Sans faute", "C) Faute de service classique", "D) Faute personnelle au pénal seul"],
        "answer": "A",
        "explanation": "L'Etat se substitue à l'enseignant fautif devant les tribunaux judiciaires pour les dommages aux élèves."
    },
    {
        "question": "Cas pratique 48 : L'Etat interdit un produit dangereux après des mois d'études. Légalité de l'interdiction ?",
        "options": ["A) Légal, précaution et salubrité", "B) Illégal, atteinte au commerce", "C) Acte de gouvernement", "D) Compétence judiciaire"],
        "answer": "A",
        "explanation": "La police administrative peut interdire des produits dangereux pour protéger la salubrité."
    },
    {
        "question": "Cas pratique 49 : Médecin privé réquisitionné lors d'une catastrophe, se blesse. Régime d'indemnisation ?",
        "options": ["A) Collaborateur occasionnel du SP (sans faute)", "B) Faute lourde", "C) Sécurité sociale", "D) Irresponsabilité"],
        "answer": "A",
        "explanation": "Jurisprudence Commune de Saint-Priest-la-Plaine (responsabilité sans faute pour le collaborateur)."
    },
    {
        "question": "Cas pratique 50 : Chute d'un arbre d'alignement non entretenu sur un piéton. Régime ?",
        "options": ["A) Défaut d'entretien normal (usager TP)", "B) Sans faute pour tiers", "C) Faute personnelle du jardinier", "D) Force majeure"],
        "answer": "A",
        "explanation": "Le piéton sur le trottoir est usager de l'ouvrage public."
    },
    {
        "question": "Cas pratique 51 : Préfet refuse la force publique pour expulser un syndicat en grève. Régime ?",
        "options": ["A) Responsabilité sans faute (Couitéas)", "B) Faute", "C) Irresponsabilité", "D) Acte de gouvernement"],
        "answer": "A",
        "explanation": "Refus justifié par l'ordre public social, mais indemnisation sans faute du propriétaire."
    },
    {
        "question": "Cas pratique 52 : Chasse-neige blesse un skieur en station publique (Côte d'Ivoire n'a pas de neige, prenons un tracteur de voirie). Régime ?",
        "options": ["A) Véhicule administratif (compétence judiciaire)", "B) Travaux publics", "C) Faute de service administrative", "D) Sans faute"],
        "answer": "A",
        "explanation": "Les dommages par véhicules (loi 1957) relèvent du juge judiciaire."
    },
    {
        "question": "Cas pratique 53 : Arrêté du maire de Yamoussoukro interdisant toute mendicité au centre-ville. Légalité ?",
        "options": ["A) Légal si limité et justifié par l'ordre public", "B) Illégal car général et absolu", "C) Compétence du préfet", "D) Acte insusceptible de recours"],
        "answer": "A",
        "explanation": "Les interdictions de mendicité sont légales si elles sont limitées dans le temps/l'espace et justifiées."
    },
    {
        "question": "Cas pratique 54 : Policiers cassent la porte d'un voisin par erreur lors d'une perquisition. Régime pour le voisin ?",
        "options": ["A) Responsabilité sans faute (tiers)", "B) Faute lourde", "C) Faute personnelle", "D) Irresponsabilité"],
        "answer": "A",
        "explanation": "Le tiers bénéficie de la responsabilité sans faute (rupture égalité)."
    },
    {
        "question": "Cas pratique 55 : Une erreur de diagnostic vétérinaire de l'Etat cause la mort du troupeau de M. N'GUESSAN. Régime ?",
        "options": ["A) Faute simple", "B) Faute lourde", "C) Sans faute", "D) Force majeure"],
        "answer": "A",
        "explanation": "La faute simple est suffisante aujourd'hui pour les services de contrôle ou vétérinaires."
    },
    {
        "question": "Cas pratique 56 : Maire ordonne de tuer des chiens errants menaçants. Police ?",
        "options": ["A) Sécurité et salubrité", "B) Tranquillité", "C) Moralité", "D) Esthétique"],
        "answer": "A",
        "explanation": "La lutte contre les animaux errants dangereux relève de la sécurité/salubrité."
    },
    {
        "question": "Cas pratique 57 : Effondrement de la voie publique suite à de fortes pluies prévisibles. Voiture endommagée. Régime ?",
        "options": ["A) Défaut d'entretien normal (pas de force majeure si prévisible)", "B) Force majeure", "C) Faute exclusive victime", "D) Sans faute pour risque"],
        "answer": "A",
        "explanation": "L'intempérie prévisible n'est pas la force majeure. Présomption de défaut d'entretien."
    },
    {
        "question": "Cas pratique 58 : Refus d'agrément d'une clinique illégalement prononcé par le Ministre. Régime indemnitaire ?",
        "options": ["A) Faute de service", "B) Acte de gouvernement", "C) Sans faute", "D) Détournement sans faute"],
        "answer": "A",
        "explanation": "L'acte illégal est une faute."
    },
    {
        "question": "Cas pratique 59 : Maire d'Adjamé ferme un commerce pour insalubrité avérée. Recours du gérant ?",
        "options": ["A) Rejet, mesure de police justifiée", "B) Annulation, incompétence", "C) Annulation, liberté de commerce absolue", "D) Indemnisation sans faute"],
        "answer": "A",
        "explanation": "La fermeture pour insalubrité est légale."
    },
    {
        "question": "Cas pratique 60 : Agent des impôts diffamant un contribuable sur les réseaux. Régime ?",
        "options": ["A) Faute personnelle détachable", "B) Faute de service", "C) Cumul", "D) Sans faute"],
        "answer": "A",
        "explanation": "Faute personnelle sans lien avec le service."
    },
    {
        "question": "Cas pratique 61 : Dommage causé par un détenu en semi-liberté. Régime ?",
        "options": ["A) Responsabilité sans faute (méthode libérale dangereuse)", "B) Faute", "C) Défaut d'entretien", "D) Irresponsabilité"],
        "answer": "A",
        "explanation": "Jurisprudence Thouzellier / Garde des Sceaux contre C."
    },
    {
        "question": "Cas pratique 62 : Loi interdisant la production d'un produit (amiante) et causant la ruine du producteur. Indemnisation ?",
        "options": ["A) Responsabilité sans faute du fait des lois (La Fleurette) si non exclu", "B) Faute du législateur", "C) Irresponsabilité totale en matière sanitaire", "D) Responsabilité pour risque"],
        "answer": "A",
        "explanation": "L'indemnisation est possible si la loi ne l'exclut pas et préjudice grave."
    },
    {
        "question": "Cas pratique 63 : Préfet couvre-feu à San Pedro pendant crise grave. Légalité ?",
        "options": ["A) Légal (Théorie circonstances exceptionnelles)", "B) Illégal", "C) Faute lourde", "D) Acte de gouvernement"],
        "answer": "A",
        "explanation": "Circonstances exceptionnelles valident des mesures de police restrictives."
    },
    {
        "question": "Cas pratique 64 : Maire réglemente l'affichage sauvage pour protéger des monuments. Police de l'esthétique ?",
        "options": ["A) Oui, reconnue jurisprudentiellement", "B) Non, illégal", "C) Relève de la moralité", "D) Acte de gouvernement"],
        "answer": "A",
        "explanation": "La jurisprudence admet la protection de l'esthétique monumentale."
    },
    {
        "question": "Cas pratique 65 : Blessure d'un élève pendant le cours d'EPS par la chute d'un poteau. Régime ?",
        "options": ["A) Défaut d'entretien normal de l'ouvrage public", "B) Faute personnelle du prof", "C) Loi de 1937", "D) Sans faute"],
        "answer": "A",
        "explanation": "Si lié à l'infrastructure (poteau), c'est un dommage de travaux publics."
    },
    {
        "question": "Cas pratique 66 : Infirmier ivre administre un mauvais traitement. Régime ?",
        "options": ["A) Cumul (faute personnelle en service)", "B) Faute de service seule", "C) Détachable seule", "D) Sans faute"],
        "answer": "A",
        "explanation": "L'ivresse est une faute personnelle, mais sur le lieu et temps de service (cumul)."
    },
    {
        "question": "Cas pratique 67 : Bruit excessif permanent d'un aéroport militaire. Régime pour les voisins ?",
        "options": ["A) Sans faute (dommage permanent TP)", "B) Faute de pilotage", "C) Défaut d'entretien", "D) Acte de gouvernement"],
        "answer": "A",
        "explanation": "Préjudice anormal et spécial pour les riverains de l'ouvrage public."
    },
    {
        "question": "Cas pratique 68 : Décision du président ivoirien d'engager les forces armées à la frontière. Recours de KOFFI pour annuler l'ordre ?",
        "options": ["A) Irrecevable, acte de gouvernement", "B) Recevable", "C) Responsabilité pour faute", "D) Illégal pour défaut de visa"],
        "answer": "A",
        "explanation": "Les actes concernant les opérations militaires et diplomatiques sont des actes de gouvernement."
    },
    {
        "question": "Cas pratique 69 : Inaction de la police face à un lynchage public malgré les appels. Responsabilité ?",
        "options": ["A) Faute de service (carence)", "B) Faute personnelle", "C) Irresponsabilité", "D) Sans faute"],
        "answer": "A",
        "explanation": "La carence à assurer l'ordre public est une faute engageant l'Etat."
    },
    {
        "question": "Cas pratique 70 : Dommage causé à un passant par la chute d'un panneau électoral posé par l'Etat. Régime ?",
        "options": ["A) Défaut d'entretien de l'ouvrage public", "B) Faute", "C) Sans faute (tiers)", "D) Irresponsabilité"],
        "answer": "C",
        "explanation": "Si c'est un ouvrage public et la victime est un tiers (pas usager du panneau), responsabilité sans faute."
    },
    {
        "question": "Cas pratique 71 : Maire interdit le passage des camions de plus de 10T dans une rue fragile. Légalité ?",
        "options": ["A) Légal (police de conservation de la voie)", "B) Illégal", "C) Incompétence", "D) Général et absolu"],
        "answer": "A",
        "explanation": "Mesure proportionnée pour protéger la voirie."
    },
    {
        "question": "Cas pratique 72 : Erreur matérielle dans le calcul de la note d'un fonctionnaire causant son éviction. Régime ?",
        "options": ["A) Faute de service", "B) Sans faute", "C) Faute personnelle", "D) Irréparable"],
        "answer": "A",
        "explanation": "L'erreur de l'administration est une faute."
    },
    {
        "question": "Cas pratique 73 : Un véhicule de la BAC renverse M. DIABY lors d'une course-poursuite. Victime = tiers. Régime ?",
        "options": ["A) Loi de 1957 (véhicules, compétence judiciaire)", "B) Sans faute administrative", "C) Faute lourde", "D) Tribunal des conflits"],
        "answer": "A",
        "explanation": "Dommage causé par véhicule = juge judiciaire."
    },
    {
        "question": "Cas pratique 74 : Refus d'application d'un traité par le juge ivoirien au nom de la constitution. Principe ?",
        "options": ["A) Suprématie constitutionnelle (Sarran/Fraisse)", "B) Supériorité des traités", "C) Acte de gouvernement", "D) Contrôle de légalité"],
        "answer": "A",
        "explanation": "Dans l'ordre interne, la Constitution prime."
    },
    {
        "question": "Cas pratique 75 : Maire d'Abengourou prend un arrêté ordonnant à tous les habitants de peindre leur maison en blanc. Légalité ?",
        "options": ["A) Illégal (atteinte disproportionnée au droit de propriété)", "B) Légal (esthétique)", "C) Légal si vote du conseil", "D) Acte de gouvernement"],
        "answer": "A",
        "explanation": "Mesure disproportionnée et excessive."
    },
    {
        "question": "Cas pratique 76 : Patient infecté par une bactérie nosocomiale au CHU. Régime ?",
        "options": ["A) Responsabilité sans faute (risque ou loi spéciale)", "B) Faute prouvée", "C) Faute lourde", "D) Irresponsabilité"],
        "answer": "A",
        "explanation": "Les infections nosocomiales relèvent d'un régime de responsabilité sans faute de l'établissement."
    },
    {
        "question": "Cas pratique 77 : Arrestation arbitraire de M. KAMAGATE par un préfet hors de ses pouvoirs. Recours ?",
        "options": ["A) Voie de fait (compétence juge judiciaire)", "B) Faute simple", "C) Excès de pouvoir classique", "D) Sans faute"],
        "answer": "A",
        "explanation": "Atteinte grave à la liberté individuelle par un acte manifestement insusceptible de se rattacher à un pouvoir de l'administration = voie de fait."
    },
    {
        "question": "Cas pratique 78 : Agent blessé dans ses fonctions par un déséquilibré. Régime d'indemnisation par l'Etat ?",
        "options": ["A) Sans faute (collaborateur/agent du SP)", "B) Faute", "C) Irresponsabilité de l'Etat", "D) Loi 1957"],
        "answer": "A",
        "explanation": "L'Etat protège ses agents pour les dommages subis dans le service (responsabilité sans faute / garantie)."
    },
    {
        "question": "Cas pratique 79 : Maire interdit un film pourtant visé par le ministre. Condition de légalité ?",
        "options": ["A) Circonstances locales particulières (Lutetia)", "B) Incompétence absolue", "C) Faute", "D) Sans faute"],
        "answer": "A",
        "explanation": "La police municipale peut aggraver la mesure nationale s'il y a des circonstances locales particulières."
    },
    {
        "question": "Cas pratique 80 : Coupure de route nationale par des éboulements fréquents non signalés. Régime ?",
        "options": ["A) Défaut d'entretien normal", "B) Force majeure", "C) Sans faute (risque)", "D) Faute personnelle"],
        "answer": "A",
        "explanation": "L'absence de signalisation d'un danger fréquent est un défaut d'entretien."
    },
    {
        "question": "Cas pratique 81 : Grève des éboueurs à Abidjan causant amoncellement d'ordures et épidémie. Responsabilité ?",
        "options": ["A) Faute dans l'organisation du service", "B) Force majeure (grève)", "C) Sans faute", "D) Acte de gouvernement"],
        "answer": "A",
        "explanation": "L'administration doit assurer un service minimum ou réquisitionner pour préserver la salubrité."
    },
    {
        "question": "Cas pratique 82 : M. ZADI aide bénévolement les pompiers de Daloa et se brûle. Indemnisation ?",
        "options": ["A) Sans faute (collaborateur occasionnel)", "B) Faute des pompiers prouvée", "C) Aucune, il est bénévole", "D) Assurance personnelle seule"],
        "answer": "A",
        "explanation": "Le collaborateur occasionnel du service public bénéficie de la responsabilité sans faute de l'administration."
    },
    {
        "question": "Cas pratique 83 : Interdiction de stationnement devant les bouches d'incendie par le maire. Légalité ?",
        "options": ["A) Légal (sécurité publique)", "B) Illégal", "C) Détournement de pouvoir", "D) Sans faute"],
        "answer": "A",
        "explanation": "Mesure normale de police pour garantir l'accès aux secours."
    },
    {
        "question": "Cas pratique 84 : Délai déraisonnable de jugement devant la juridiction administrative ivoirienne. Régime ?",
        "options": ["A) Faute de service de l'Etat", "B) Sans faute", "C) Irresponsabilité (séparation des pouvoirs)", "D) Force majeure"],
        "answer": "A",
        "explanation": "Le dysfonctionnement de la justice (délai excessif) engage la responsabilité pour faute lourde ou simple selon les évolutions jurisprudentielles (Magiera)."
    },
    {
        "question": "Cas pratique 85 : Un ministre annule un concours après les résultats pour fraude massive. Légalité ?",
        "options": ["A) Légal (pouvoir d'appréciation de l'ordre public / régularité)", "B) Illégal (droits acquis)", "C) Voie de fait", "D) Sans faute"],
        "answer": "A",
        "explanation": "Le ministre peut et doit annuler un concours entaché de fraude massive avant nomination."
    },
    {
        "question": "Cas pratique 86 : Agent de l'Etat utilise son ordinateur de service pour pirater des banques. Responsabilité Etat ?",
        "options": ["A) Cumul (faute avec les moyens du service)", "B) Faute exclusive de l'Etat", "C) Faute personnelle sans lien", "D) Sans faute"],
        "answer": "A",
        "explanation": "L'utilisation des moyens du service permet d'attraire l'Etat."
    },
    {
        "question": "Cas pratique 87 : L'administration confie l'entretien d'une route à une entreprise qui fait faillite. Route dégradée, accident. Recours victime ?",
        "options": ["A) Contre l'administration (défaut d'entretien)", "B) Contre l'entreprise faillie uniquement", "C) Force majeure", "D) Sans faute"],
        "answer": "A",
        "explanation": "L'administration maître de l'ouvrage reste responsable vis-à-vis des usagers."
    },
    {
        "question": "Cas pratique 88 : Refus d'inscrire M. KOUAKOU à l'université publique pour motif politique. Analyse ?",
        "options": ["A) Détournement de pouvoir (illégalité fautive)", "B) Légal (discrétionnaire)", "C) Ordre public", "D) Acte de gouvernement"],
        "answer": "A",
        "explanation": "La décision est prise dans un but autre que l'intérêt du service."
    },
    {
        "question": "Cas pratique 89 : Le préfet ordonne la destruction d'une cargaison de viande avariée arrivée au port d'Abidjan. Légalité ?",
        "options": ["A) Légal (salubrité publique, destruction en cas de péril)", "B) Voie de fait", "C) Atteinte au droit de propriété injustifiée", "D) Sans faute"],
        "answer": "A",
        "explanation": "Mesure de salubrité publique justifiée par le danger immédiat pour la santé."
    },
    {
        "question": "Cas pratique 90 : Un enfant est blessé par la chute d'un panier de basket mal fixé dans une école communale. Régime ?",
        "options": ["A) Défaut d'entretien de l'ouvrage public", "B) Sans faute", "C) Loi de 1937", "D) Irresponsabilité"],
        "answer": "A",
        "explanation": "Dommage causé par l'équipement immobilier (ouvrage public) à un usager."
    },
    {
        "question": "Cas pratique 91 : Lors d'une émeute, les forces de l'ordre utilisent des grenades lacrymogènes qui incendient la maison d'un tiers. Régime ?",
        "options": ["A) Responsabilité sans faute (tiers à l'opération)", "B) Faute lourde", "C) Irresponsabilité absolue", "D) Faute personnelle"],
        "answer": "A",
        "explanation": "Le tiers victime de l'utilisation d'armes dangereuses par la police est indemnisé sans faute."
    },
    {
        "question": "Cas pratique 92 : Interdiction du port de tenues religieuses dans les écoles publiques ivoiriennes par le ministre. Recours ?",
        "options": ["A) Annulation si contraire à la Constitution/laïcité ou légal si justifié", "B) Voie de fait", "C) Acte de gouvernement", "D) Irrecevable"],
        "answer": "A",
        "explanation": "Contrôle de légalité classique sur l'étendue du pouvoir réglementaire et la liberté de religion."
    },
    {
        "question": "Cas pratique 93 : Dommage causé par le fonctionnement d'un radar défectueux (PV injustifiés). Responsabilité ?",
        "options": ["A) Faute de service (dysfonctionnement)", "B) Sans faute", "C) Faute du conducteur", "D) Irresponsabilité"],
        "answer": "A",
        "explanation": "Le dysfonctionnement du matériel administratif générant des actes illégaux est une faute."
    },
    {
        "question": "Cas pratique 94 : Le Président de la République gracie un condamné qui récidive immédiatement. Recours des victimes contre l'Etat ?",
        "options": ["A) Irrecevable (la grâce est un acte de gouvernement inattaquable)", "B) Recevable pour faute", "C) Recevable sans faute", "D) Compétence judiciaire"],
        "answer": "A",
        "explanation": "Le décret de grâce relève traditionnellement des actes de gouvernement insusceptibles de recours."
    },
    {
        "question": "Cas pratique 95 : Un fonctionnaire est mis à la retraite d'office par erreur sur son âge. Il demande réparation. Régime ?",
        "options": ["A) Faute de service (illégalité)", "B) Sans faute", "C) Irresponsabilité", "D) Faute personnelle du DRH"],
        "answer": "A",
        "explanation": "Illégalité fautive engageant l'administration."
    },
    {
        "question": "Cas pratique 96 : M. BAMBA est mordu par un serpent qui s'est échappé du zoo d'Abidjan (géré par l'Etat). Régime ?",
        "options": ["A) Sans faute pour risque (chose dangereuse)", "B) Faute prouvée (surveillance)", "C) Faute lourde", "D) Défaut d'entretien de l'ouvrage public"],
        "answer": "A",
        "explanation": "La garde d'animaux dangereux par le SP justifie une responsabilité pour risque."
    },
    {
        "question": "Cas pratique 97 : Le conseil municipal de Bingerville refuse d'exécuter un contrat public. Le cocontractant demande réparation. Juge compétent ?",
        "options": ["A) Juge administratif (responsabilité contractuelle)", "B) Juge civil", "C) Juge pénal", "D) Tribunal de commerce"],
        "answer": "A",
        "explanation": "Le contentieux des contrats administratifs relève du juge administratif (pleine juridiction)."
    },
    {
        "question": "Cas pratique 98 : Le Maire ordonne de disperser un attroupement menaçant l'hôtel de ville par des canons à eau. Légalité ?",
        "options": ["A) Légal, pouvoir de police face à un trouble imminent proportionné", "B) Illégal, seul le préfet peut", "C) Voie de fait", "D) Sans faute"],
        "answer": "A",
        "explanation": "Mesure de maintien de l'ordre justifiée et proportionnée."
    },
    {
        "question": "Cas pratique 99 : Patient décède suite à une panne d'électricité au CHU (groupe électrogène défectueux). Régime ?",
        "options": ["A) Faute de service (défaut d'organisation)", "B) Force majeure", "C) Faute personnelle du directeur", "D) Irresponsabilité"],
        "answer": "A",
        "explanation": "Le défaut de maintenance des équipements vitaux est une faute."
    },
    {
        "question": "Cas pratique 100 : Sieur KOUASSI voit sa parcelle inondée par le refoulement des égouts communaux mal conçus. Régime ?",
        "options": ["A) Responsabilité sans faute (dommage de travaux publics pour tiers/voisin)", "B) Faute prouvée", "C) Force majeure automatique", "D) Défaut d'entretien"],
        "answer": "A",
        "explanation": "Le tiers/voisin d'un ouvrage public subissant un dommage anormal est indemnisé sans faute."
    },
]

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
    themes = THEME_CATALOG
    if selected_themes:
        selected = {str(theme).strip() for theme in selected_themes if str(theme).strip()}
        themes = [item for item in THEME_CATALOG if item[0] in selected]
        if not themes:
            raise ValueError("Aucun thème valide sélectionné.")
    if not themes:
        raise ValueError("Aucun thème disponible.")
    num_themes = len(themes)
    questions_per_theme = num_questions // num_themes
    remaining = num_questions % num_themes
    selected_questions = []
    for i, (theme_name, theme_questions) in enumerate(themes):
        n = questions_per_theme + (1 if i < remaining else 0)
        n = min(n, len(theme_questions))
        theme_sample = random.sample(theme_questions, n)
        for q in theme_sample:
            q_copy = q.copy()
            q_copy["theme"] = theme_name
            selected_questions.append(q_copy)
    random.shuffle(selected_questions)
    return selected_questions[:num_questions]
