#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour compter le nombre de questions par thème
"""

from quiz_data import THEME_1, THEME_2, THEME_3, THEME_4, THEME_5

print("=" * 60)
print("📊 STATISTIQUES DES QUESTIONS PAR THÈME")
print("=" * 60)
print()

themes_data = [
    ("THÈME 1 - Culture Générale — Langue française", THEME_1),
    ("THÈME 2 - Aptitude Verbale — Phénomènes lexicaux", THEME_2),
    ("THÈME 3 - Culture Générale — Géographie et connaissances", THEME_3),
    ("THÈME 4 - Organisations Internationales", THEME_4),
    ("THÈME 5 - English Grammar", THEME_5)
]

total_questions = 0

for theme_name, theme_questions in themes_data:
    count = len(theme_questions)
    total_questions += count
    print(f"✅ {theme_name}")
    print(f"   → {count} questions")
    print()

print("=" * 60)
print(f"📚 TOTAL : {total_questions} questions dans toute la base")
print("=" * 60)
