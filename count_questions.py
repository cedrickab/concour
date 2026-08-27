#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour compter le nombre de questions par thème (Généré dynamiquement)
"""

import quiz_data

print("=" * 60)
print("📊 STATISTIQUES DES QUESTIONS PAR THÈME")
print("=" * 60)
print()

# Discover all themes dynamically
themes_data = []
for attr in sorted(dir(quiz_data)):
    if attr.startswith('THEME_') and attr != 'THEME_CATALOG':
        theme_list = getattr(quiz_data, attr)
        # Try to find a human-readable name in THEME_CATALOG if it exists
        name = attr
        if hasattr(quiz_data, 'THEME_CATALOG'):
            for cat_id, cat_name in getattr(quiz_data, 'THEME_CATALOG'):
                if cat_id == attr:
                    name = cat_name
                    break
        themes_data.append((name, theme_list))

total_questions = 0

for theme_name, theme_questions in themes_data:
    count = len(theme_questions)
    total_questions += count
    print(f"✅ {theme_name}")
    print(f"   → {count} questions\n")

print("=" * 60)
print(f"📚 TOTAL : {total_questions} questions dans toute la base")
print("=" * 60)
