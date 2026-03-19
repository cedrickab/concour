@echo off
REM Lanceur pour l'application web Quiz ENA
REM Ce script installe les dépendances et lance le serveur web

echo ======================================================================
echo                 QUIZ ENA - APPLICATION WEB
echo ======================================================================
echo.

REM Vérifier si Flask est installé
python -c "import flask" 2>nul
if %errorlevel% neq 0 (
    echo Flask n'est pas installe. Installation en cours...
    echo.
    pip install -r requirements.txt
    echo.
    if %errorlevel% neq 0 (
        echo ERREUR: L'installation a echoue.
        echo Verifiez que Python et pip sont correctement installes.
        pause
        exit /b 1
    )
)

echo Demarrage du serveur web...
echo.
echo Une fois le serveur demarre, ouvrez votre navigateur a l'adresse:
echo    http://localhost:5000
echo.
echo Pour arreter le serveur, appuyez sur Ctrl+C
echo ======================================================================
echo.

python web_app.py

pause
