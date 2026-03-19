# 🌐 Quiz ENA - Interface Web

## 🚀 Démarrage Rapide

### Option 1 : Utiliser le script de lancement (Recommandé)

Double-cliquez sur le fichier **`start_web_quiz.bat`** (Windows)

Le script va :
1. Vérifier et installer Flask si nécessaire
2. Démarrer automatiquement le serveur web
3. Vous indiquer l'adresse à ouvrir dans votre navigateur

### Option 2 : Ligne de commande

#### 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

#### 2. Lancer le serveur

```bash
python web_app.py
```

#### 3. Ouvrir dans votre navigateur

Allez à l'adresse : **http://localhost:5000**

---

## ✨ Fonctionnalités de l'interface web

- ✅ Interface moderne et responsive
- ✅ Design coloré avec dégradés
- ✅ Choix du nombre de questions (5, 10, 15, 20, 30)
- ✅ Barre de progression animée
- ✅ Feedback immédiat avec animations
- ✅ Score en temps réel
- ✅ Résultats détaillés avec statistiques visuelles
- ✅ Compatible mobile et desktop

---

## 🎨 Aperçu des pages

### Page d'accueil
- Présentation du quiz
- Liste des 5 thèmes (dont English Grammar)
- Sélection du nombre de questions
- Bouton de démarrage

### Page du quiz
- Barre de progression
- Question avec thème
- Options de réponse cliquables
- Feedback coloré (vert pour correct, rouge pour incorrect)
- Explications détaillées
- Score actuel

### Page des résultats
- Score final avec pourcentage
- Message d'encouragement personnalisé
- Statistiques par thème
- Récapitulatif complet de toutes les réponses
- Bouton pour recommencer

---

## 🔧 Configuration

### Modifier le port

Par défaut, le serveur s'exécute sur le port **5000**. Pour changer :

Éditez `web_app.py`, ligne finale :
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Changez 5000
```

### Personnaliser les couleurs

Éditez `static/style.css`, section `:root` :
```css
:root {
    --primary-color: #2c3e50;      /* Couleur principale */
    --secondary-color: #3498db;    /* Couleur secondaire */
    --success-color: #27ae60;      /* Vert (correct) */
    --error-color: #e74c3c;        /* Rouge (incorrect) */
}
```

---

## 📂 Structure des fichiers

```
concour/
├── web_app.py              # Application Flask (serveur)
├── quiz_data.py            # Base de données des questions
├── start_web_quiz.bat      # Script de lancement Windows
├── requirements.txt        # Dépendances Python
├── templates/
│   └── index.html         # Page HTML principale
└── static/
    ├── style.css          # Feuille de style CSS
    └── script.js          # Code JavaScript
```

---

## ❓ Dépannage

### Le serveur ne démarre pas

**Problème** : `ModuleNotFoundError: No module named 'flask'`

**Solution** :
```bash
pip install Flask
```

### La page ne s'affiche pas

**Vérifiez que** :
1. Le serveur est bien démarré (vous devez voir le message de confirmation)
2. Vous utilisez la bonne adresse : `http://localhost:5000`
3. Aucun autre programme n'utilise le port 5000

### Erreur de port déjà utilisé

**Problème** : `Address already in use`

**Solutions** :
1. Fermez l'autre application utilisant le port 5000
2. Ou changez le port dans `web_app.py`

---

## 🌐 Accès depuis un autre appareil

Pour accéder au quiz depuis un autre appareil sur le même réseau :

1. Trouvez votre adresse IP locale :
   ```bash
   ipconfig
   ```
   Cherchez "Adresse IPv4" (ex: 192.168.1.100)

2. Sur l'autre appareil, ouvrez :
   ```
   http://[VOTRE_IP]:5000
   ```
   Exemple : `http://192.168.1.100:5000`

---

## 🛑 Arrêter le serveur

Appuyez sur **Ctrl + C** dans le terminal où le serveur tourne

---

## 📱 Compatibilité

- ✅ Chrome, Firefox, Edge, Safari (dernières versions)
- ✅ Responsive : fonctionne sur mobile, tablette et desktop
- ✅ Windows, macOS, Linux

---

## 🎯 Différences avec la version console

| Fonctionnalité | Version Console | Version Web |
|----------------|----------------|-------------|
| Interface | Ligne de commande | Navigateur web |
| Design | Texte simple | Graphique coloré |
| Navigation | Entrée clavier | Clic souris |
| Multi-appareils | Non | Oui (réseau local) |
| Animations | Non | Oui |
| Installation | Aucune | Flask requis |

---

**Bon quiz et bonne préparation pour le concours ENA ! 🎓**
