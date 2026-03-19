#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quiz ENA - Application Web
Interface web pour le quiz de préparation au concours ENA

Auteur: Assistant IA
Date: Mars 2026
"""

from flask import Flask, render_template, request, jsonify, session
import secrets
from quiz_data import get_quiz_questions

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    """Page d'accueil"""
    return render_template('index.html')

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    """Démarre un nouveau quiz"""
    data = request.json
    num_questions = int(data.get('num_questions', 10))
    
    # Générer les questions
    questions = get_quiz_questions(num_questions=num_questions)
    
    # Stocker dans la session
    session['questions'] = questions
    session['current_question'] = 0
    session['score'] = 0
    session['answers_history'] = []
    
    return jsonify({'status': 'success', 'total_questions': len(questions)})

@app.route('/get_question', methods=['GET'])
def get_question():
    """Récupère la question actuelle"""
    questions = session.get('questions', [])
    current = session.get('current_question', 0)
    
    if current >= len(questions):
        return jsonify({'status': 'finished'})
    
    question = questions[current]
    
    return jsonify({
        'status': 'success',
        'question_num': current + 1,
        'total_questions': len(questions),
        'theme': question['theme'],
        'question': question['question'],
        'options': question['options']
    })

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    """Soumet une réponse"""
    data = request.json
    user_answer = data.get('answer', '').upper()
    
    questions = session.get('questions', [])
    current = session.get('current_question', 0)
    score = session.get('score', 0)
    answers_history = session.get('answers_history', [])
    
    if current >= len(questions):
        return jsonify({'status': 'error', 'message': 'Quiz terminé'})
    
    question = questions[current]
    correct_answer = question['answer']
    is_correct = user_answer == correct_answer
    
    if is_correct:
        score += 1
        session['score'] = score
    
    # Enregistrer l'historique
    answers_history.append({
        'question': question['question'],
        'theme': question['theme'],
        'user_answer': user_answer,
        'correct_answer': correct_answer,
        'is_correct': is_correct
    })
    session['answers_history'] = answers_history
    
    # Passer à la question suivante
    session['current_question'] = current + 1
    
    return jsonify({
        'status': 'success',
        'is_correct': is_correct,
        'correct_answer': correct_answer,
        'explanation': question['explanation'],
        'current_score': score,
        'next_question': current + 2 <= len(questions)
    })

@app.route('/get_results', methods=['GET'])
def get_results():
    """Récupère les résultats finaux"""
    questions = session.get('questions', [])
    score = session.get('score', 0)
    answers_history = session.get('answers_history', [])
    
    total_questions = len(questions)
    percentage = (score / total_questions * 100) if total_questions > 0 else 0
    
    # Calculer les statistiques par thème
    themes_stats = {}
    for history in answers_history:
        theme = history['theme']
        if theme not in themes_stats:
            themes_stats[theme] = {'correct': 0, 'total': 0}
        
        themes_stats[theme]['total'] += 1
        if history['is_correct']:
            themes_stats[theme]['correct'] += 1
    
    # Convertir en liste pour JSON
    themes_list = []
    for theme, stats in themes_stats.items():
        theme_percentage = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
        themes_list.append({
            'theme': theme,
            'correct': stats['correct'],
            'total': stats['total'],
            'percentage': round(theme_percentage, 1)
        })
    
    # Message d'encouragement
    if percentage >= 80:
        message = "🌟 Excellent ! Vous êtes bien préparé(e) pour le concours ENA !"
    elif percentage >= 60:
        message = "👍 Bon travail ! Continuez à vous entraîner pour progresser."
    elif percentage >= 40:
        message = "💪 Pas mal, mais il faut encore réviser certains thèmes."
    else:
        message = "📚 Continuez à réviser ! La persévérance est la clé de la réussite."
    
    return jsonify({
        'status': 'success',
        'score': score,
        'total_questions': total_questions,
        'percentage': round(percentage, 1),
        'message': message,
        'answers_history': answers_history,
        'themes_stats': themes_list
    })

if __name__ == '__main__':
    print("=" * 70)
    print("🎓 QUIZ ENA - APPLICATION WEB")
    print("=" * 70)
    print()
    print("✅ Serveur démarré avec succès !")
    print()
    print("🌐 Ouvrez votre navigateur et allez à l'adresse :")
    print("   👉 http://localhost:5000")
    print()
    print("💡 Pour arrêter le serveur, appuyez sur Ctrl+C")
    print("=" * 70)
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)
