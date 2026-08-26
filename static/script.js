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
const skipBtn = document.getElementById('skip-btn');
const modeRandom = document.getElementById('mode-random');
const modeSelected = document.getElementById('mode-selected');
const themeSelection = document.getElementById('theme-selection');
const themeCheckboxes = document.querySelectorAll('.theme-checkbox');

// Gestion du choix du nombre de questions
let selectedNumQuestions = 10;
let selectedQuizMode = 'random';
const countButtons = document.querySelectorAll('.count-btn');
const countInfo = document.getElementById('count-info');

function updateCountInfo() {
    if (selectedQuizMode === 'selected') {
        const selectedThemes = getSelectedThemes();
        if (selectedThemes.length === 0) {
            countInfo.textContent = `📋 ${selectedNumQuestions} questions sur un ou plusieurs thèmes choisis`;
        } else {
            countInfo.textContent = `📋 ${selectedNumQuestions} questions sur ${selectedThemes.length} thème(s) choisi(s)`;
        }
        return;
    }

    countInfo.textContent = `📋 ${selectedNumQuestions} questions aléatoires sur les 7 thèmes`;
}

function getSelectedThemes() {
    const themes = [];
    themeCheckboxes.forEach(cb => {
        if (cb.checked) {
            themes.push(cb.value);
        }
    });
    return themes;
}

countButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        countButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        selectedNumQuestions = parseInt(btn.dataset.count);
        updateCountInfo();
    });
});

modeRandom.addEventListener('change', () => {
    selectedQuizMode = 'random';
    themeSelection.classList.add('hidden');
    updateCountInfo();
});

modeSelected.addEventListener('change', () => {
    selectedQuizMode = 'selected';
    themeSelection.classList.remove('hidden');
    updateCountInfo();
});

themeCheckboxes.forEach(cb => {
    cb.addEventListener('change', updateCountInfo);
});

// Démarrer le quiz
async function startQuiz() {
    const numQuestions = selectedNumQuestions;
    const selectedThemes = getSelectedThemes();
    const mode = selectedQuizMode;

    if (mode === 'selected' && selectedThemes.length === 0) {
        alert('Veuillez choisir au moins un thème.');
        return;
    }
    
    try {
        const response = await fetch('/start_quiz', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                num_questions: numQuestions,
                mode: mode,
                selected_themes: selectedThemes
            })
        });

        const data = await response.json();

        if (data.status === 'success') {
            totalQuestions = data.total_questions;
            currentScore = 0;
            showPage('quiz');
            loadQuestion();
        } else {
            alert(data.message || 'Erreur lors du démarrage du quiz');
        }
    } catch (error) {
        console.error('Erreur:', error);
        alert('Erreur lors du démarrage du quiz');
    }
}

startBtn.addEventListener('click', startQuiz);

skipBtn.addEventListener('click', async () => {
    await submitAnswer('', null);
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
            skipBtn.disabled = false;
        }
    } catch (error) {
        console.error('Erreur:', error);
        alert('Erreur lors du chargement de la question');
    }
}

// Soumettre une réponse
async function submitAnswer(answer, clickedButton) {
    const allButtons = document.querySelectorAll('.option-btn');
    allButtons.forEach(btn => btn.disabled = true);
    skipBtn.disabled = true;

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

            document.getElementById('current-score').textContent = `Score : ${currentScore}/${currentQuestionNum}`;

            const feedbackBox = document.getElementById('feedback-box');
            const feedbackContent = document.getElementById('feedback-content');

            if (data.skipped) {
                feedbackBox.className = 'feedback-box neutral';
                feedbackContent.innerHTML = `
                    <div class="feedback-title">⏭️ Question sautée</div>
                    <div class="feedback-text">Vous n'avez pas répondu. Vous ne gagnez ni ne perdez de point.</div>
                    <div class="feedback-text">💡 <strong>Explication :</strong> ${data.explanation}</div>
                `;
            } else if (data.is_correct) {
                if (clickedButton) clickedButton.classList.add('correct');
                feedbackBox.className = 'feedback-box correct';
                feedbackContent.innerHTML = `
                    <div class="feedback-title">✅ Bonne réponse !</div>
                    <div class="feedback-text">💡 <strong>Explication :</strong> ${data.explanation}</div>
                `;
            } else {
                if (clickedButton) clickedButton.classList.add('incorrect');
                feedbackBox.className = 'feedback-box incorrect';

                allButtons.forEach(btn => {
                    if (btn.dataset.answer === data.correct_answer) {
                        btn.classList.add('correct');
                    }
                });

                feedbackContent.innerHTML = `
                    <div class="feedback-title">❌ Mauvaise réponse</div>
                    <div class="feedback-text"><strong>La bonne réponse est : ${data.correct_answer}</strong></div>
                    <div class="feedback-text">💡 <strong>Explication :</strong> ${data.explanation}</div>
                `;
            }

            feedbackBox.classList.remove('hidden');

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
                const status = answer.skipped ? '⏭️' : (answer.is_correct ? '✅' : '❌');
                const answerClass = answer.skipped ? 'neutral' : (answer.is_correct ? 'correct' : 'incorrect');
                const userResponse = answer.skipped ? 'Question sautée' : answer.user_answer;

                answerDiv.className = `answer-item ${answerClass}`;
                answerDiv.innerHTML = `
                    <div class="answer-header">
                        <span class="answer-status">${status}</span>
                        <small>[${answer.theme}]</small>
                    </div>
                    <div class="answer-question">Q${index + 1}: ${answer.question}</div>
                    <div class="answer-detail">
                        Votre réponse : <strong>${userResponse}</strong> | 
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
    startQuiz();
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
