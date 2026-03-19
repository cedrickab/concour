# 🎓 Application Quiz ENA - Guide d'Utilisation

## 📋 Description

Application Python interactive de quiz à choix multiples (QCM) pour la préparation au concours de l'**École Nationale d'Administration (ENA)** de Côte d'Ivoire.

Cette application génère des quiz de 10 questions (personnalisable) couvrant 5 thèmes principaux :

1. **Culture Générale — Langue française et vocabulaire**
2. **Aptitude Verbale — Phénomènes lexicaux**
3. **Culture Générale — Géographie et connaissances diverses**
4. **Organisations Internationales**
5. **English Grammar** (Grammaire anglaise)

---

## ✨ Fonctionnalités

- ✅ Quiz interactif avec 10 questions (personnalisable)
- ✅ Questions variées couvrant au minimum 3 thèmes différents
- ✅ Correction immédiate après chaque question
- ✅ Explications pédagogiques pour chaque réponse
- ✅ Score final avec pourcentage de réussite
- ✅ Récapitulatif détaillé de toutes les réponses
- ✅ Statistiques par thème
- ✅ Possibilité de refaire un quiz
- ✅ Interface en français avec emojis pour une meilleure expérience

---

## 🔧 Prérequis

- **Python 3.7 ou supérieur**

Vérifiez votre version de Python :

```bash
python --version
```

ou

```bash
python3 --version
```

---

## 📦 Installation

### Option 1 : Téléchargement direct

1. Téléchargez tous les fichiers du projet
2. Placez-les dans un même dossier
3. Aucune installation de dépendances n'est nécessaire (l'application utilise uniquement les bibliothèques standard de Python)

### Option 2 : Installation via Git (si disponible)

```bash
git clone <url-du-repository>
cd concour
```

---

## 🚀 Utilisation

### Lancement du quiz

**Sous Windows :**

```bash
python quiz_app.py
```

**Sous macOS/Linux :**

```bash
python3 quiz_app.py
```

### Déroulement du quiz

1. **Sélection du nombre de questions**
   - À l'ouverture, le programme vous demande combien de questions vous souhaitez (défaut : 10)
   - Vous pouvez choisir entre 1 et 60 questions

2. **Répondre aux questions**
   - Lisez chaque question attentivement
   - Tapez la lettre correspondant à votre réponse (A, B, C ou D)
   - Appuyez sur Entrée

3. **Correction immédiate**
   - Après chaque réponse, le programme affiche :
     - ✅ Si votre réponse est correcte
     - ❌ Si votre réponse est incorrecte (avec la bonne réponse)
     - 💡 Une explication pédagogique

4. **Résultats finaux**
   - À la fin du quiz, vous verrez :
     - Votre score total
     - Un message d'encouragement
     - Un récapitulatif détaillé de toutes vos réponses
     - Des statistiques par thème

5. **Refaire un quiz**
   - Vous pouvez choisir de refaire un nouveau quiz ou quitter l'application

---

## 📊 Exemple d'utilisation

```
======================================================================
🎓 QUIZ INTERACTIF — PRÉPARATION CONCOURS ENA
   École Nationale d'Administration — Côte d'Ivoire
======================================================================

Bienvenue dans le système de préparation au concours de l'ENA
(École Nationale d'Administration — Côte d'Ivoire)

Combien de questions souhaitez-vous (défaut: 10) ? 10

======================================================================
🎓 QUIZ INTERACTIF — PRÉPARATION CONCOURS ENA
   École Nationale d'Administration — Côte d'Ivoire
======================================================================

📊 Progression : 0/10 (0%)
🎯 Score actuel : 0/0

📝 Question 1/10
[Thème : Culture Générale — Langue française]

Quel est le synonyme du mot « fugace » ?

   A) Permanent
   B) Éphémère
   C) Rapide
   D) Durable

👉 Votre réponse (A/B/C/D) : B

----------------------------------------------------------------------
✅ Bonne réponse !
💡 Explication : « Fugace » signifie éphémère, qui dure peu de temps.
----------------------------------------------------------------------

Appuyez sur Entrée pour passer à la question suivante...
```

---

## 📂 Structure du projet

```
concour/
├── quiz_app.py           # Application principale (lanceur)
├── quiz_data.py          # Base de données des questions
├── requirements.txt      # Dépendances Python (vide - bibliothèques standard uniquement)
├── QUIZ_GUIDE.md        # Ce guide d'utilisation
└── README.md            # Documentation originale du projet
```

---

## 🎯 Conseils pour la préparation

1. **Faites plusieurs quiz** - La répétition aide à mémoriser
2. **Lisez attentivement les explications** - Elles enrichissent vos connaissances
3. **Variez le nombre de questions** - Commencez par des quiz courts, puis augmentez progressivement
4. **Notez vos points faibles** - Identifiez les thèmes où vous avez besoin de plus de révision
5. **Révisez les fiches originales** - Consultez le README.md pour approfondir vos connaissances

---

## 🔧 Personnalisation

### Modifier le nombre de questions par défaut

Éditez [quiz_app.py](quiz_app.py) et modifiez la ligne :

```python
num_questions = 10  # Changez cette valeur
```

### Ajouter de nouvelles questions

Éditez [quiz_data.py](quiz_data.py) et ajoutez vos questions dans le thème approprié :

```python
THEME_X.append({
    "question": "Votre question ?",
    "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
    "answer": "A",
    "explanation": "Explication de la réponse"
})
```

---

## ❓ Dépannage

### Le programme ne démarre pas

- Vérifiez que Python est installé : `python --version`
- Vérifiez que vous êtes dans le bon dossier
- Essayez `python3 quiz_app.py` au lieu de `python quiz_app.py`

### Erreur d'encodage des caractères

- Assurez-vous que votre terminal supporte l'UTF-8
- Sous Windows, utilisez PowerShell ou Windows Terminal (au lieu de CMD)

### Les emojis ne s'affichent pas

- Utilisez un terminal moderne (Windows Terminal, PowerShell 7+, ou un terminal Unix moderne)
- Les emojis ne sont pas essentiels au fonctionnement de l'application

---

## 📄 Licence

Ce projet est développé à des fins pédagogiques pour la préparation au concours ENA de Côte d'Ivoire.

---

## 🤝 Contribution

Pour améliorer l'application :

1. Ajoutez de nouvelles questions dans `quiz_data.py`
2. Proposez de nouvelles fonctionnalités
3. Signalez les erreurs dans les questions existantes

---

## 📞 Support

En cas de problème ou de question, consultez :

- Le fichier [README.md](README.md) pour le contenu pédagogique complet
- Les fiches de cours originales dans les dossiers du workspace

---

**Bonne chance pour votre préparation au concours ENA ! 🍀**
