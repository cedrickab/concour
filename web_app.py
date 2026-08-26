#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quiz ENA - Application Web
Interface web pour le quiz de préparation au concours ENA

Auteur: Assistant IA
Date: Mars 2026
"""

import sys
import secrets

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from flask import Flask, render_template, request, jsonify, session
from quiz_data import get_quiz_questions, THEME_CATALOG

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
AVAILABLE_THEMES = [name for name, _ in THEME_CATALOG]

@app.route('/')
def index():
    """Page d'accueil"""
    return render_template('index.html')

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    """Démarre un nouveau quiz"""
    data = request.get_json(silent=True) or {}

    try:
        num_questions = int(data.get('num_questions', 10))
    except (TypeError, ValueError):
        return jsonify({'status': 'error', 'message': 'Le nombre de questions doit être un entier valide.'}), 400

    if num_questions < 1 or num_questions > 60:
        return jsonify({'status': 'error', 'message': 'Le nombre de questions doit être compris entre 1 et 60.'}), 400

    mode = str(data.get('mode', 'random') or 'random').strip().lower()
    selected_themes = data.get('selected_themes', [])
    if isinstance(selected_themes, str):
        selected_themes = [selected_themes]
    elif not isinstance(selected_themes, list):
        return jsonify({'status': 'error', 'message': 'La sélection des thèmes est invalide.'}), 400

    if mode not in ['random', 'selected']:
        return jsonify({'status': 'error', 'message': 'Le mode de quiz est invalide.'}), 400

    if mode == 'selected':
        cleaned_themes = [str(theme).strip() for theme in selected_themes if str(theme).strip()]
        if not cleaned_themes:
            return jsonify({'status': 'error', 'message': 'Choisissez au moins un thème.'}), 400

        invalid_themes = [theme for theme in cleaned_themes if theme not in AVAILABLE_THEMES]
        if invalid_themes:
            return jsonify({'status': 'error', 'message': 'Un ou plusieurs thèmes sélectionnés sont invalides.'}), 400

        questions = get_quiz_questions(num_questions=num_questions, selected_themes=cleaned_themes)
    else:
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
    """Soumet une réponse."""
    data = request.get_json(silent=True) or {}
    user_answer = str(data.get('answer', '') or '').upper()

    questions = session.get('questions', [])
    current = session.get('current_question', 0)
    score = session.get('score', 0)
    answers_history = session.get('answers_history', [])

    if current >= len(questions):
        return jsonify({'status': 'error', 'message': 'Quiz terminé'}), 400

    question = questions[current]
    correct_answer = question['answer']
    skipped = user_answer == ''

    if skipped:
        is_correct = None
    else:
        is_correct = user_answer == correct_answer
        if is_correct:
            score += 1
        else:
            score -= 1

    session['score'] = score

    answers_history.append({
        'question': question['question'],
        'theme': question['theme'],
        'user_answer': user_answer if user_answer else ' ',
        'correct_answer': correct_answer,
        'is_correct': is_correct,
        'skipped': skipped
    })
    session['answers_history'] = answers_history

    session['current_question'] = current + 1

    return jsonify({
        'status': 'success',
        'is_correct': is_correct,
        'skipped': skipped,
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
