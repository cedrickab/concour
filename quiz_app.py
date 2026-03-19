#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quiz Interactif - Préparation Concours ENA (Côte d'Ivoire)
Application de quiz à choix multiples pour la préparation au concours ENA

Auteur: Assistant IA
Date: Mars 2026
"""

import sys
import time
from quiz_data import get_quiz_questions


class QuizENA:
    """Classe principale pour gérer le quiz interactif ENA"""
    
    def __init__(self, num_questions=10):
        """
        Initialise le quiz
        
        Args:
            num_questions: Nombre de questions du quiz (défaut: 10)
        """
        self.num_questions = num_questions
        self.questions = get_quiz_questions(num_questions=num_questions)
        self.score = 0
        self.answers_history = []
    
    def clear_screen(self):
        """Efface l'écran (compatible Windows et Unix)"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Affiche l'en-tête du quiz"""
        print("=" * 70)
        print("🎓 QUIZ INTERACTIF — PRÉPARATION CONCOURS ENA")
        print("   École Nationale d'Administration — Côte d'Ivoire")
        print("=" * 70)
        print()
    
    def display_question(self, question_num, question_data):
        """
        Affiche une question
        
        Args:
            question_num: Numéro de la question (1-indexed)
            question_data: Dictionnaire contenant les données de la question
        """
        print(f"📝 Question {question_num}/{self.num_questions}")
        print(f"[Thème : {question_data['theme']}]")
        print()
        print(question_data['question'])
        print()
        
        for option in question_data['options']:
            print(f"   {option}")
        print()
    
    def get_user_answer(self):
        """
        Récupère la réponse de l'utilisateur
        
        Returns:
            Réponse de l'utilisateur (A, B, C ou D)
        """
        while True:
            answer = input("👉 Votre réponse (A/B/C/D) : ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            else:
                print("❌ Réponse invalide. Veuillez entrer A, B, C ou D.")
    
    def check_answer(self, user_answer, correct_answer, explanation):
        """
        Vérifie la réponse et affiche le résultat
        
        Args:
            user_answer: Réponse de l'utilisateur
            correct_answer: Réponse correcte
            explanation: Explication de la réponse
        
        Returns:
            True si la réponse est correcte, False sinon
        """
        print()
        print("-" * 70)
        
        is_correct = user_answer == correct_answer
        
        if is_correct:
            print("✅ Bonne réponse !")
            self.score += 1
        else:
            print("❌ Mauvaise réponse.")
            print(f"La bonne réponse est : {correct_answer}")
        
        print(f"💡 Explication : {explanation}")
        print("-" * 70)
        print()
        
        return is_correct
    
    def display_progress(self, question_num):
        """
        Affiche la progression du quiz
        
        Args:
            question_num: Numéro de la question actuelle
        """
        progress = (question_num / self.num_questions) * 100
        print(f"📊 Progression : {question_num}/{self.num_questions} ({progress:.0f}%)")
        print(f"🎯 Score actuel : {self.score}/{question_num}")
        print()
    
    def run(self):
        """Lance le quiz interactif"""
        self.clear_screen()
        self.display_header()
        
        print("Bienvenue dans le quiz de préparation au concours ENA !")
        print(f"Ce quiz contient {self.num_questions} questions couvrant plusieurs thèmes.")
        print()
        input("Appuyez sur Entrée pour commencer... ")
        
        # Parcourir toutes les questions
        for i, question_data in enumerate(self.questions, 1):
            self.clear_screen()
            self.display_header()
            self.display_progress(i - 1)
            
            # Afficher la question
            self.display_question(i, question_data)
            
            # Obtenir la réponse de l'utilisateur
            user_answer = self.get_user_answer()
            
            # Vérifier la réponse
            is_correct = self.check_answer(
                user_answer,
                question_data['answer'],
                question_data['explanation']
            )
            
            # Enregistrer l'historique
            self.answers_history.append({
                'question': question_data['question'],
                'theme': question_data['theme'],
                'user_answer': user_answer,
                'correct_answer': question_data['answer'],
                'is_correct': is_correct
            })
            
            # Pause avant la question suivante
            if i < self.num_questions:
                input("Appuyez sur Entrée pour passer à la question suivante... ")
        
        # Afficher le résultat final
        self.display_final_results()
    
    def display_final_results(self):
        """Affiche les résultats finaux du quiz"""
        self.clear_screen()
        self.display_header()
        
        print("=" * 70)
        print("🎉 QUIZ TERMINÉ !")
        print("=" * 70)
        print()
        
        # Score final
        percentage = (self.score / self.num_questions) * 100
        print(f"📊 SCORE FINAL : {self.score}/{self.num_questions} ({percentage:.1f}%)")
        print()
        
        # Message d'encouragement basé sur le score
        if percentage >= 80:
            print("🌟 Excellent ! Vous êtes bien préparé(e) pour le concours ENA !")
        elif percentage >= 60:
            print("👍 Bon travail ! Continuez à vous entraîner pour progresser.")
        elif percentage >= 40:
            print("💪 Pas mal, mais il faut encore réviser certains thèmes.")
        else:
            print("📚 Continuez à réviser ! La persévérance est la clé de la réussite.")
        
        print()
        print("-" * 70)
        print("📋 RÉCAPITULATIF DES RÉPONSES")
        print("-" * 70)
        print()
        
        # Afficher le récapitulatif question par question
        for i, history in enumerate(self.answers_history, 1):
            status = "✅" if history['is_correct'] else "❌"
            print(f"{status} Question {i} [{history['theme']}]")
            print(f"   {history['question'][:60]}...")
            print(f"   Votre réponse : {history['user_answer']} | "
                  f"Réponse correcte : {history['correct_answer']}")
            print()
        
        print("=" * 70)
        print("Merci d'avoir participé au quiz de préparation ENA !")
        print("Bonne chance pour votre concours ! 🍀")
        print("=" * 70)
    
    def display_statistics_by_theme(self):
        """Affiche des statistiques par thème"""
        themes_stats = {}
        
        for history in self.answers_history:
            theme = history['theme']
            if theme not in themes_stats:
                themes_stats[theme] = {'correct': 0, 'total': 0}
            
            themes_stats[theme]['total'] += 1
            if history['is_correct']:
                themes_stats[theme]['correct'] += 1
        
        print()
        print("-" * 70)
        print("📈 STATISTIQUES PAR THÈME")
        print("-" * 70)
        
        for theme, stats in themes_stats.items():
            percentage = (stats['correct'] / stats['total']) * 100
            print(f"{theme} : {stats['correct']}/{stats['total']} ({percentage:.0f}%)")
        
        print("-" * 70)


def main():
    """Fonction principale"""
    print("=" * 70)
    print("🎓 QUIZ INTERACTIF — PRÉPARATION CONCOURS ENA")
    print("=" * 70)
    print()
    print("Bienvenue dans le système de préparation au concours de l'ENA")
    print("(École Nationale d'Administration — Côte d'Ivoire)")
    print()
    
    # Demander le nombre de questions
    while True:
        try:
            num_questions_input = input("Combien de questions souhaitez-vous (défaut: 10) ? ")
            if num_questions_input.strip() == "":
                num_questions = 10
            else:
                num_questions = int(num_questions_input)
                if num_questions < 1 or num_questions > 60:
                    print("❌ Veuillez entrer un nombre entre 1 et 60.")
                    continue
            break
        except ValueError:
            print("❌ Veuillez entrer un nombre valide.")
    
    print()
    
    # Créer et lancer le quiz
    quiz = QuizENA(num_questions=num_questions)
    quiz.run()
    
    # Afficher les statistiques par thème
    quiz.display_statistics_by_theme()
    
    print()
    
    # Demander si l'utilisateur veut refaire un quiz
    while True:
        retry = input("Voulez-vous refaire un autre quiz ? (O/N) : ").strip().upper()
        if retry == 'O':
            print()
            main()
            break
        elif retry == 'N':
            print()
            print("Au revoir et bonne chance pour votre concours ! 🍀")
            sys.exit(0)
        else:
            print("❌ Veuillez répondre par O (Oui) ou N (Non).")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🛑 Quiz interrompu par l'utilisateur.")
        print("Au revoir ! 👋")
        sys.exit(0)
