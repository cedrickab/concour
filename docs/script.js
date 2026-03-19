// Quiz ENA - JavaScript (version statique, 100% client-side)

// ===== QUIZ ENGINE =====

/**
 * Génère les questions du quiz (aléatoires, sans doublons, 5 thèmes couverts)
 */
function getQuizQuestions(numQuestions) {
    const themes = [
        { name: "Culture Générale — Langue française", questions: THEME_1 },
        { name: "Aptitude Verbale — Phénomènes lexicaux", questions: THEME_2 },
        { name: "Culture Générale — Géographie et connaissances", questions: THEME_3 },
        { name: "Organisations Internationales", questions: THEME_4 },
        { name: "English Grammar", questions: THEME_5 }
    ];

    const numThemes = themes.length;
    const perTheme = Math.floor(numQuestions / numThemes);
    const remaining = numQuestions % numThemes;

    let selected = [];

    themes.forEach((theme, i) => {
        const n = Math.min(perTheme + (i < remaining ? 1 : 0), theme.questions.length);
        const shuffled = [...theme.questions].sort(() => Math.random() - 0.5);
        const picked = shuffled.slice(0, n);
        picked.forEach(q => {
            selected.push({ ...q, theme: theme.name });
        });
    });

    // Fisher-Yates shuffle
    for (let i = selected.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [selected[i], selected[j]] = [selected[j], selected[i]];
    }

    return selected.slice(0, numQuestions);
}

// ===== STATE =====
let questions = [];
let currentIndex = 0;
let score = 0;
let answersHistory = [];

// ===== DOM =====
const homePage = document.getElementById('home-page');
const quizPage = document.getElementById('quiz-page');
const resultsPage = document.getElementById('results-page');
const startBtn = document.getElementById('start-btn');
const retryBtn = document.getElementById('retry-btn');
const nextBtn = document.getElementById('next-btn');

// ===== QUESTION COUNT SELECTOR =====
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

// ===== START QUIZ =====
startBtn.addEventListener('click', () => {
    questions = getQuizQuestions(selectedNumQuestions);
    currentIndex = 0;
    score = 0;
    answersHistory = [];
    document.getElementById('current-score').textContent = 'Score : 0';
    showPage('quiz');
    loadQuestion();
});

// ===== LOAD QUESTION =====
function loadQuestion() {
    if (currentIndex >= questions.length) {
        showResults();
        return;
    }

    const q = questions[currentIndex];

    // Update progress
    const pct = (currentIndex / questions.length) * 100;
    document.getElementById('progress-fill').style.width = pct + '%';
    document.getElementById('progress-text').textContent = `Question ${currentIndex + 1}/${questions.length}`;

    // Theme badge
    document.getElementById('theme-badge').textContent = q.theme;

    // Question text
    document.getElementById('question-text').textContent = q.question;

    // Options
    const optionsContainer = document.getElementById('options-container');
    optionsContainer.innerHTML = '';

    q.options.forEach(option => {
        const letter = option.split(')')[0].trim();
        const button = document.createElement('button');
        button.className = 'option-btn';
        button.textContent = option;
        button.dataset.answer = letter;
        button.addEventListener('click', () => submitAnswer(letter, button));
        optionsContainer.appendChild(button);
    });

    // Hide feedback
    document.getElementById('feedback-box').classList.add('hidden');
}

// ===== SUBMIT ANSWER =====
function submitAnswer(answer, clickedButton) {
    const allButtons = document.querySelectorAll('.option-btn');
    allButtons.forEach(btn => btn.disabled = true);

    const q = questions[currentIndex];
    const isCorrect = answer === q.answer;

    if (isCorrect) score++;

    answersHistory.push({
        question: q.question,
        theme: q.theme,
        user_answer: answer,
        correct_answer: q.answer,
        is_correct: isCorrect
    });

    document.getElementById('current-score').textContent = `Score : ${score}/${currentIndex + 1}`;

    const feedbackBox = document.getElementById('feedback-box');
    const feedbackContent = document.getElementById('feedback-content');

    if (isCorrect) {
        clickedButton.classList.add('correct');
        feedbackBox.className = 'feedback-box correct';
    } else {
        clickedButton.classList.add('incorrect');
        feedbackBox.className = 'feedback-box incorrect';
        allButtons.forEach(btn => {
            if (btn.dataset.answer === q.answer) {
                btn.classList.add('correct');
            }
        });
    }

    feedbackContent.innerHTML = `
        <div class="feedback-title">
            ${isCorrect ? '✅ Bonne réponse !' : '❌ Mauvaise réponse'}
        </div>
        ${!isCorrect ? `<div class="feedback-text"><strong>La bonne réponse est : ${q.answer}</strong></div>` : ''}
        <div class="feedback-text">💡 <strong>Explication :</strong> ${q.explanation}</div>
    `;

    feedbackBox.classList.remove('hidden');

    currentIndex++;

    if (currentIndex < questions.length) {
        nextBtn.textContent = 'Question suivante →';
        nextBtn.onclick = () => loadQuestion();
    } else {
        nextBtn.textContent = 'Voir les résultats →';
        nextBtn.onclick = () => showResults();
    }
}

// ===== SHOW RESULTS =====
function showResults() {
    const total = questions.length;
    const percentage = total > 0 ? Math.round((score / total) * 1000) / 10 : 0;

    document.getElementById('final-score').textContent = `${score}/${total}`;
    document.getElementById('final-percentage').textContent = `${percentage}%`;

    let message;
    if (percentage >= 80) {
        message = "🌟 Excellent ! Vous êtes bien préparé(e) pour le concours !";
    } else if (percentage >= 60) {
        message = "👍 Bon travail ! Continuez à vous entraîner pour progresser.";
    } else if (percentage >= 40) {
        message = "💪 Pas mal, mais il faut encore réviser certains thèmes.";
    } else {
        message = "📚 Continuez à réviser ! La persévérance est la clé de la réussite.";
    }
    document.getElementById('encouragement-message').textContent = message;

    // Theme stats
    const themesMap = {};
    answersHistory.forEach(a => {
        if (!themesMap[a.theme]) themesMap[a.theme] = { correct: 0, total: 0 };
        themesMap[a.theme].total++;
        if (a.is_correct) themesMap[a.theme].correct++;
    });

    const themesStatsContainer = document.getElementById('themes-stats');
    themesStatsContainer.innerHTML = '';
    for (const [theme, stats] of Object.entries(themesMap)) {
        const pct = stats.total > 0 ? Math.round((stats.correct / stats.total) * 1000) / 10 : 0;
        const statDiv = document.createElement('div');
        statDiv.className = 'theme-stat';
        statDiv.innerHTML = `
            <span class="theme-name">${theme}</span>
            <span class="theme-score">${stats.correct}/${stats.total} (${pct}%)</span>
        `;
        themesStatsContainer.appendChild(statDiv);
    }

    // Answers recap
    const answersRecapContainer = document.getElementById('answers-recap');
    answersRecapContainer.innerHTML = '';
    answersHistory.forEach((answer, index) => {
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

// ===== RETRY =====
retryBtn.addEventListener('click', () => {
    showPage('home');
});

// ===== PAGE NAVIGATION =====
function showPage(page) {
    homePage.classList.remove('active');
    quizPage.classList.remove('active');
    resultsPage.classList.remove('active');

    if (page === 'home') homePage.classList.add('active');
    else if (page === 'quiz') quizPage.classList.add('active');
    else if (page === 'results') resultsPage.classList.add('active');

    window.scrollTo(0, 0);
}
