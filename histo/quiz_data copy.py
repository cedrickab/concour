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
    }
]

def get_quiz_questions(num_questions=10, min_themes=3):
    """
    Génère un ensemble de questions pour le quiz
    
    Args:
        num_questions: Nombre total de questions (défaut: 10)
        min_themes: Nombre minimum de thèmes à couvrir (défaut: 3)
    
    Returns:
        Liste de questions mélangées
    """
    themes = [
        ("Culture Générale — Langue française", THEME_1),
        ("Aptitude Verbale — Phénomènes lexicaux", THEME_2),
        ("Culture Générale — Géographie et connaissances", THEME_3),
        ("Organisations Internationales", THEME_4),
        ("English Grammar", THEME_5)
    ]
    
    # Sélectionner au moins min_themes thèmes
    selected_themes = random.sample(themes, min(min_themes, len(themes)))
    
    # Calculer le nombre de questions par thème
    questions_per_theme = num_questions // len(selected_themes)
    remaining = num_questions % len(selected_themes)
    
    selected_questions = []
    
    for i, (theme_name, theme_questions) in enumerate(selected_themes):
        # Nombre de questions pour ce thème
        n = questions_per_theme + (1 if i < remaining else 0)
        
        # Sélectionner aléatoirement n questions de ce thème
        theme_sample = random.sample(theme_questions, min(n, len(theme_questions)))
        
        # Ajouter le nom du thème à chaque question
        for q in theme_sample:
            q_copy = q.copy()
            q_copy["theme"] = theme_name
            selected_questions.append(q_copy)
    
    # Mélanger toutes les questions
    random.shuffle(selected_questions)
    
    return selected_questions[:num_questions]
