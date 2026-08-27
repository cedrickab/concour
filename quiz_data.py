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
        "question": "Question 11",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "A",
        "explanation": "Exp 11"
    },
    {
        "question": "Question 12",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "B",
        "explanation": "Exp 12"
    },
    {
        "question": "Question 13",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "C",
        "explanation": "Exp 13"
    },
    {
        "question": "Question 14",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "D",
        "explanation": "Exp 14"
    },
    {
        "question": "Question 15",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "A",
        "explanation": "Exp 15"
    },
    {
        "question": "Question 16",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "B",
        "explanation": "Exp 16"
    },
    {
        "question": "Question 17",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "C",
        "explanation": "Exp 17"
    },
    {
        "question": "Question 18",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "D",
        "explanation": "Exp 18"
    },
    {
        "question": "Question 19",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "A",
        "explanation": "Exp 19"
    },
    {
        "question": "Question 20",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "B",
        "explanation": "Exp 20"
    },
    {
        "question": "Question 21",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "A",
        "explanation": "Exp"
    },
    {
        "question": "Question 22",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "B",
        "explanation": "Exp"
    },
    {
        "question": "Question 23",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "C",
        "explanation": "Exp"
    },
    {
        "question": "Question 24",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "D",
        "explanation": "Exp"
    },
    {
        "question": "Question 25",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "A",
        "explanation": "Exp"
    },
    {
        "question": "Question 26",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "B",
        "explanation": "Exp"
    },
    {
        "question": "Question 27",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "C",
        "explanation": "Exp"
    },
    {
        "question": "Question 28",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "D",
        "explanation": "Exp"
    },
    {
        "question": "Question 29",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "A",
        "explanation": "Exp"
    },
    {
        "question": "Question 30",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "B",
        "explanation": "Exp"
    },
    {
        "question": "Question 31",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "C",
        "explanation": "Exp"
    },
    {
        "question": "Question 32",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "D",
        "explanation": "Exp"
    },
    {
        "question": "Question 33",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "A",
        "explanation": "Exp"
    },
    {
        "question": "Question 34",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "B",
        "explanation": "Exp"
    },
    {
        "question": "Question 35",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "C",
        "explanation": "Exp"
    },
    {
        "question": "Question 36",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "D",
        "explanation": "Exp"
    },
    {
        "question": "Question 37",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "A",
        "explanation": "Exp"
    },
    {
        "question": "Question 38",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "B",
        "explanation": "Exp"
    },
    {
        "question": "Question 39",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "C",
        "explanation": "Exp"
    },
    {
        "question": "Question 40",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "D",
        "explanation": "Exp"
    },
    {
        "question": "Question 41",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "A",
        "explanation": "Exp"
    },
    {
        "question": "Question 42",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "B",
        "explanation": "Exp"
    },
    {
        "question": "Question 43",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "C",
        "explanation": "Exp"
    },
    {
        "question": "Question 44",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "D",
        "explanation": "Exp"
    },
    {
        "question": "Question 45",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "A",
        "explanation": "Exp"
    },
    {
        "question": "Question 46",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "B",
        "explanation": "Exp"
    },
    {
        "question": "Question 47",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "C",
        "explanation": "Exp"
    },
    {
        "question": "Question 48",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "D",
        "explanation": "Exp"
    },
    {
        "question": "Question 49",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "A",
        "explanation": "Exp"
    },
    {
        "question": "Question 50",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "B",
        "explanation": "Exp"
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
        "options": ["A) L’oxygène", "B) Le carbone", "C) Le diazote"],
        "answer": "C",
        "explanation": "Le diazote constitue 78% de l'atmosphère."
    },
    {
        "question": "Le Pakistan a pour capitale :",
        "options": ["A) Kuala Lumpur", "B) Bangkok", "C) Islamabad"],
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
        "options": ["A) Usain Bolt", "B) Michael Phelps", "C) Larissa Latynina"],
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
        "options": ["A) Istanbul", "B) Ankara", "C) Izmir"],
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
        "options": ["A) INSP", "B) ENAMF", "C) APF"],
        "answer": "A",
        "explanation": "L'ENA en France a été remplacée par l'Institut national du service public (INSP)."
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
        "question": "Avec quel pourcentage a été élu le président gabonais Brice Clotaire Oligui N’Guema ?",
        "options": ["A) 87 %", "B) 90,35 %", "C) 98,85 %"],
        "answer": "C",
        "explanation": "Il a été élu avec ce score."
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
        "options": ["A) Usain Bolt", "B) Noah Lyles", "C) Justin Gatlin"],
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
        "options": ["A) Chine", "B) Japon", "C) Vietnam"],
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
        "question": "En rugby, combien de points vaut un essai ?",
        "options": ["A) 3", "B) 5", "C) 6", "D) 7"],
        "answer": "B",
        "explanation": "Un essai au rugby vaut 5 points."
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
        "question": "Combien de points vaut un essai au rugby ?",
        "options": ["A) 3 points", "B) 4 points", "C) 5 points", "D) 7 points"],
        "answer": "C",
        "explanation": "Un essai vaut 5 points au rugby."
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
        "question": "Dans le sport du rugby (à XV), combien de points rapporte un essai marqué (avant transformation) ?",
        "options": ["A) 3 points", "B) 5 points", "C) 7 points", "D) 2 points"],
        "answer": "B",
        "explanation": "Un essai vaut 5 points, la transformation 2 points, le drop et la pénalité 3 points."
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
        "question": "Piège : qui préside le Conseil supérieur de la magistrature en CI ?",
        "options": ["A) Le Ministre de la Justice", "B) Une personnalité nommée par le Président de la République parmi les hauts magistrats", "C) Le Président de la République", "D) Le Procureur général"],
        "answer": "B",
        "explanation": "En CI, selon la Constitution de 2016, le CSM est présidé par une personnalité nommée par le Président parmi les hauts magistrats."
    },
    {
        "question": "Qu'est-ce que le Conseil d'État en Côte d'Ivoire ?",
        "options": ["A) La juridiction suprême de l'ordre administratif", "B) Une assemblée politique", "C) Une juridiction de l'ordre judiciaire", "D) Le conseil des ministres"],
        "answer": "A",
        "explanation": "Le Conseil d'État est la juridiction suprême de l'ordre administratif en Côte d'Ivoire (Constitution 2016)."
    },
    {
        "question": "La Cour de Cassation en Côte d'Ivoire est la juridiction suprême de quel ordre ?",
        "options": ["A) L'ordre administratif", "B) L'ordre judiciaire", "C) L'ordre constitutionnel", "D) L'ordre financier"],
        "answer": "B",
        "explanation": "La Cour de Cassation est la plus haute juridiction de l'ordre judiciaire ivoirien."
    },
]

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
        "question": "Que consacre l'arrêt Tomaso Grecco en droit administratif ?",
        "options": ["A) L'irresponsabilité de l'État pour les services de police", "B) La responsabilité de l'administration pour les services de police", "C) L'interdiction du droit de grève", "D) Le pouvoir réglementaire des maires"],
        "answer": "B",
        "explanation": "L'arrêt Tomaso Grecco (1905) admet le principe de la responsabilité de l'État pour faute dans les services de police."
    },
    {
        "question": "L'arrêt Benjamin du Conseil d'État concerne principalement :",
        "options": ["A) Les contrats administratifs", "B) Le contrôle de proportionnalité des mesures de police administrative", "C) L'expropriation pour cause d'utilité publique", "D) La responsabilité médicale"],
        "answer": "B",
        "explanation": "L'arrêt Benjamin (1933) impose que les restrictions aux libertés (mesures de police) soient proportionnées à la menace."
    },
    {
        "question": "L'arrêt Monpeurt (1942) a établi que :",
        "options": ["A) Les personnes privées peuvent gérer un service public et édicter des actes administratifs", "B) Seul l'État peut gérer un service public", "C) Les communes n'ont pas de pouvoir réglementaire", "D) Les traités priment sur les lois"],
        "answer": "A",
        "explanation": "L'arrêt Monpeurt reconnaît qu'un organisme privé gérant un service public peut prendre des actes administratifs."
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
