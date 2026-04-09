#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lecture du fichier bilan.docx
Affiche le contenu du document Word bilan.docx
"""

import os
from docx import Document


def read_bilan(filepath="bilan.docx"):
    """
    Lit et affiche le contenu d'un fichier Word (.docx).

    Args:
        filepath: Chemin vers le fichier .docx (défaut : bilan.docx)
    """
    if not os.path.exists(filepath):
        print(f"❌ Fichier introuvable : {filepath}")
        return

    try:
        doc = Document(filepath)
    except Exception as e:
        print(f"❌ Impossible de lire le fichier : {e}")
        return

    print("=" * 70)
    print(f"📄 Contenu de : {os.path.basename(filepath)}")
    print("=" * 70)
    print()

    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            print(text)
            print()

    print("=" * 70)


if __name__ == "__main__":
    import sys
    filepath = sys.argv[1] if len(sys.argv) > 1 else "bilan.docx"
    read_bilan(filepath)
