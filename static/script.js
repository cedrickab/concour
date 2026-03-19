// Quiz ENA - JavaScript

let currentQuestionNum = 0;
let totalQuestions = 0;
let currentScore = 0;

// Éléments DOM
const homePage = document.getElementById('home-page');
const quizPage = document.getElementById('quiz-page');
const resultsPage = document.getElementById('results-page');
const startBtn = document.getElementById('start-btn');
const retryBtn = document.getElementById('retry-btn');
const nextBtn = document.getElementById('next-btn');

// Gestion du choix du nombre de questions
let selectedNumQuestions = 20;
const countButtons = document.querySelectorAll('.count-btn');
const countInfo = document.getElementById('count-info');

countButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        countButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        selectedNumQuestions = parseInt(btn.dataset.count);
        countInfo.textContent = `📋 ${selectedNumQuestions} questions aléatoires sur les 5 thèmes`;
    });
});

// Démarrer le quiz
startBtn.addEventListener('click', async () => {
    const numQuestions = selectedNumQuestions;
    
    try {
        const response = await fetch('/start_quiz', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ num_questions: numQuestions })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            totalQuestions = data.total_questions;
            currentScore = 0;
            showPage('quiz');
            loadQuestion();
        }
    } catch (error) {
        console.error('Erreur:', error);
        alert('Erreur lors du démarrage du quiz');
    }
});

// Charger une question
async function loadQuestion() {
    try {
        const response = await fetch('/get_question');
        const data = await response.json();
        
        if (data.status === 'finished') {
            showResults();
            return;
        }
        
        if (data.status === 'success') {
            currentQuestionNum = data.question_num;
            
            // Mettre à jour la progression
            updateProgress();
            
            // Afficher le thème
            document.getElementById('theme-badge').textContent = data.theme;
            
            // Afficher la question
            document.getElementById('question-text').textContent = data.question;
            
            // Créer les options
            const optionsContainer = document.getElementById('options-container');
            optionsContainer.innerHTML = '';
            
            data.options.forEach((option, index) => {
                const letter = option.split(')')[0];
                const button = document.createElement('button');
                button.className = 'option-btn';
                button.textContent = option;
                button.dataset.answer = letter;
                button.addEventListener('click', () => submitAnswer(letter, button));
                optionsContainer.appendChild(button);
            });
            
            // Cacher le feedback
            document.getElementById('feedback-box').classList.add('hidden');
        }
    } catch (error) {
        console.error('Erreur:', error);
        alert('Erreur lors du chargement de la question');
    }
}

// Soumettre une réponse
async function submitAnswer(answer, clickedButton) {
    // Désactiver tous les boutons
    const allButtons = document.querySelectorAll('.option-btn');
    allButtons.forEach(btn => btn.disabled = true);
    
    try {
        const response = await fetch('/submit_answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ answer: answer })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            currentScore = data.current_score;
            
            // Mettre à jour le score affiché
            document.getElementById('current-score').textContent = `Score : ${currentScore}/${currentQuestionNum}`;
            
            // Afficher le feedback
            const feedbackBox = document.getElementById('feedback-box');
            const feedbackContent = document.getElementById('feedback-content');
            
            // Colorer le bouton
            if (data.is_correct) {
                clickedButton.classList.add('correct');
                feedbackBox.className = 'feedback-box correct';
            } else {
                clickedButton.classList.add('incorrect');
                feedbackBox.className = 'feedback-box incorrect';
                
                // Mettre en vert la bonne réponse
                allButtons.forEach(btn => {
                    if (btn.dataset.answer === data.correct_answer) {
                        btn.classList.add('correct');
                    }
                });
            }
            
            // Contenu du feedback
            feedbackContent.innerHTML = `
                <div class="feedback-title">
                    ${data.is_correct ? '✅ Bonne réponse !' : '❌ Mauvaise réponse'}
                </div>
                ${!data.is_correct ? `<div class="feedback-text"><strong>La bonne réponse est : ${data.correct_answer}</strong></div>` : ''}
                <div class="feedback-text">💡 <strong>Explication :</strong> ${data.explanation}</div>
            `;
            
            feedbackBox.classList.remove('hidden');
            
            // Gérer le bouton suivant
            if (data.next_question) {
                nextBtn.textContent = 'Question suivante →';
                nextBtn.onclick = () => {
                    loadQuestion();
                };
            } else {
                nextBtn.textContent = 'Voir les résultats →';
                nextBtn.onclick = () => {
                    showResults();
                };
            }
        }
    } catch (error) {
        console.error('Erreur:', error);
        alert('Erreur lors de la soumission de la réponse');
    }
}

// Mettre à jour la barre de progression
function updateProgress() {
    const percentage = ((currentQuestionNum - 1) / totalQuestions) * 100;
    document.getElementById('progress-fill').style.width = percentage + '%';
    document.getElementById('progress-text').textContent = `Question ${currentQuestionNum}/${totalQuestions}`;
}

// Afficher les résultats
async function showResults() {
    try {
        const response = await fetch('/get_results');
        const data = await response.json();
        
        if (data.status === 'success') {
            // Afficher le score
            document.getElementById('final-score').textContent = `${data.score}/${data.total_questions}`;
            document.getElementById('final-percentage').textContent = `${data.percentage}%`;
            document.getElementById('encouragement-message').textContent = data.message;
            
            // Afficher les statistiques par thème
            const themesStatsContainer = document.getElementById('themes-stats');
            themesStatsContainer.innerHTML = '';
            
            data.themes_stats.forEach(theme => {
                const statDiv = document.createElement('div');
                statDiv.className = 'theme-stat';
                statDiv.innerHTML = `
                    <span class="theme-name">${theme.theme}</span>
                    <span class="theme-score">${theme.correct}/${theme.total} (${theme.percentage}%)</span>
                `;
                themesStatsContainer.appendChild(statDiv);
            });
            
            // Afficher le récapitulatif
            const answersRecapContainer = document.getElementById('answers-recap');
            answersRecapContainer.innerHTML = '';
            
            data.answers_history.forEach((answer, index) => {
                const answerDiv = document.createElement('div');
                answerDiv.className = `answer-item ${answer.is_correct ? 'correct' : 'incorrect'}`;
                answerDiv.innerHTML = `
                    <div class="answer-header">
                        <span class="answer-status">${answer.is_correct ? '✅' : '❌'}</span>
                        <small>[${answer.theme}]</small>
                    </div>
                    <div class="answer-question">Q${index + 1}: ${answer.question}</div>
                    <div class="answer-detail">
                        Votre réponse : <strong>${answer.user_answer}</strong> | 
                        Réponse correcte : <strong>${answer.correct_answer}</strong>
                    </div>
                `;
                answersRecapContainer.appendChild(answerDiv);
            });
            
            showPage('results');
        }
    } catch (error) {
        console.error('Erreur:', error);
        alert('Erreur lors du chargement des résultats');
    }
}

// Refaire un quiz
retryBtn.addEventListener('click', () => {
    showPage('home');
});

// Afficher une page
function showPage(page) {
    homePage.classList.remove('active');
    quizPage.classList.remove('active');
    resultsPage.classList.remove('active');
    
    if (page === 'home') {
        homePage.classList.add('active');
    } else if (page === 'quiz') {
        quizPage.classList.add('active');
    } else if (page === 'results') {
        resultsPage.classList.add('active');
    }
}
