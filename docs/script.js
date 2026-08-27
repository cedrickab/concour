// Quiz ENA - JavaScript (static client-side version)
// Scoring: correct = +1, wrong = -1, skip = 0

// ===== QUIZ ENGINE =====

const THEME_SPECS = [
    { name: "Culture Générale — Langue française", count: 150 },
    { name: "Aptitude Verbale — Phénomènes lexicaux", count: 146 },
    { name: "Culture Générale — Géographie et connaissances", count: 187 },
    { name: "Organisations Internationales", count: 163 },
    { name: "English Grammar", count: 156 },
    { name: "Culture Générale — Institutions et citoyenneté", count: 129 },
    { name: "Droit administratif", count: 145 }
];

function getThemeCatalog() {
    if (typeof THEME_CATALOG !== 'undefined' && Array.isArray(THEME_CATALOG) && THEME_CATALOG.length > 0) {
        return THEME_CATALOG;
    }

    if (!Array.isArray(QUIZ_QUESTIONS)) {
        throw new Error('Quiz data is unavailable.');
    }

    let start = 0;
    return THEME_SPECS.map(spec => {
        const questions = QUIZ_QUESTIONS.slice(start, start + spec.count);
        start += spec.count;
        return { name: spec.name, questions };
    });
}

function getQuizQuestions(numQuestions, selectedThemeNames) {
    let themes = getThemeCatalog();

    if (selectedThemeNames && selectedThemeNames.length > 0) {
        themes = themes.filter(t => selectedThemeNames.includes(t.name));
    }

    if (themes.length === 0) return [];

    const numThemes = themes.length;
    const perTheme = Math.floor(numQuestions / numThemes);
    const remaining = numQuestions % numThemes;

    let selected = [];

    themes.forEach((theme, i) => {
        const n = Math.min(perTheme + (i < remaining ? 1 : 0), theme.questions.length);
        const shuffled = [...theme.questions].sort(() => Math.random() - 0.5);
        const picked = shuffled.slice(0, n);
        picked.forEach(q => selected.push({ ...q, theme: theme.name }));
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
const homePage     = document.getElementById('home-page');
const quizPage     = document.getElementById('quiz-page');
const resultsPage  = document.getElementById('results-page');
const startBtn     = document.getElementById('start-btn');
const retryBtn     = document.getElementById('retry-btn');
const nextBtn      = document.getElementById('next-btn');
const skipBtn      = document.getElementById('skip-btn');
const modeRandom   = document.getElementById('mode-random');
const modeSelected = document.getElementById('mode-selected');
const themeSelBox  = document.getElementById('theme-selection');
const themeCheckboxes = document.querySelectorAll('.theme-checkbox');

// ===== QUESTION COUNT SELECTOR =====
let selectedNumQuestions = 10;
let selectedQuizMode = 'random';
const countButtons = document.querySelectorAll('.count-btn');
const countInfo    = document.getElementById('count-info');

function getSelectedThemes() {
    const out = [];
    themeCheckboxes.forEach(cb => { if (cb.checked) out.push(cb.value); });
    return out;
}

function updateCountInfo() {
    if (selectedQuizMode === 'selected') {
        const n = getSelectedThemes().length;
        countInfo.textContent = n === 0
            ? `📋 ${selectedNumQuestions} questions sur un ou plusieurs thèmes choisis`
            : `📋 ${selectedNumQuestions} questions sur ${n} thème(s) choisi(s)`;
    } else {
        countInfo.textContent = `📋 ${selectedNumQuestions} questions aléatoires sur les 7 thèmes`;
    }
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
    themeSelBox.classList.add('hidden');
    updateCountInfo();
});

modeSelected.addEventListener('change', () => {
    selectedQuizMode = 'selected';
    themeSelBox.classList.remove('hidden');
    updateCountInfo();
});

themeCheckboxes.forEach(cb => cb.addEventListener('change', updateCountInfo));

// ===== START QUIZ =====
function startQuiz() {
    const selectedThemes = selectedQuizMode === 'selected' ? getSelectedThemes() : [];

    if (selectedQuizMode === 'selected' && selectedThemes.length === 0) {
        alert('Veuillez choisir au moins un thème.');
        return;
    }

    questions = getQuizQuestions(selectedNumQuestions, selectedThemes.length ? selectedThemes : null);
    currentIndex = 0;
    score = 0;
    answersHistory = [];
    document.getElementById('current-score').textContent = 'Score : 0';
    showPage('quiz');
    loadQuestion();
}

startBtn.addEventListener('click', startQuiz);

// ===== SKIP BUTTON =====
skipBtn.addEventListener('click', () => submitAnswer('', null));

// ===== LOAD QUESTION =====
function loadQuestion() {
    if (currentIndex >= questions.length) {
        showResults();
        return;
    }

    const q = questions[currentIndex];
    updateProgress();

    document.getElementById('theme-badge').textContent = q.theme;
    document.getElementById('question-text').textContent = q.question;

    const container = document.getElementById('options-container');
    container.innerHTML = '';

    q.options.forEach(option => {
        const letter = option.split(')')[0].trim();
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        btn.textContent = option;
        btn.dataset.answer = letter;
        btn.addEventListener('click', () => submitAnswer(letter, btn));
        container.appendChild(btn);
    });

    document.getElementById('feedback-box').classList.add('hidden');
    skipBtn.disabled = false;
    skipBtn.style.display = '';
}

// ===== SUBMIT ANSWER =====
function submitAnswer(answer, clickedBtn) {
    const allBtns = document.querySelectorAll('.option-btn');
    allBtns.forEach(b => b.disabled = true);
    skipBtn.disabled = true;

    const q = questions[currentIndex];
    const skipped = answer === '';
    let isCorrect = null;

    if (!skipped) {
        isCorrect = answer === q.answer;
        if (isCorrect) score++;
        else score--;
    }

    document.getElementById('current-score').textContent = `Score : ${score}/${currentIndex + 1}`;

    const feedbackBox = document.getElementById('feedback-box');
    const feedbackContent = document.getElementById('feedback-content');

    if (skipped) {
        feedbackBox.className = 'feedback-box neutral';
        feedbackContent.innerHTML = `
            <div class="feedback-title">⏭️ Question sautée</div>
            <div class="feedback-text">Vous n'avez pas répondu. Vous ne gagnez ni ne perdez de point.</div>
            <div class="feedback-text">💡 <strong>Explication :</strong> ${q.explanation}</div>`;
    } else if (isCorrect) {
        if (clickedBtn) clickedBtn.classList.add('correct');
        feedbackBox.className = 'feedback-box correct';
        feedbackContent.innerHTML = `
            <div class="feedback-title">✅ Bonne réponse !</div>
            <div class="feedback-text">💡 <strong>Explication :</strong> ${q.explanation}</div>`;
    } else {
        if (clickedBtn) clickedBtn.classList.add('incorrect');
        feedbackBox.className = 'feedback-box incorrect';
        allBtns.forEach(b => { if (b.dataset.answer === q.answer) b.classList.add('correct'); });
        feedbackContent.innerHTML = `
            <div class="feedback-title">❌ Mauvaise réponse</div>
            <div class="feedback-text"><strong>La bonne réponse est : ${q.answer}</strong></div>
            <div class="feedback-text">💡 <strong>Explication :</strong> ${q.explanation}</div>`;
    }

    answersHistory.push({
        question: q.question,
        theme: q.theme,
        user_answer: answer || '—',
        correct_answer: q.answer,
        is_correct: isCorrect,
        skipped
    });

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

// ===== PROGRESS =====
function updateProgress() {
    const pct = (currentIndex / questions.length) * 100;
    document.getElementById('progress-fill').style.width = pct + '%';
    document.getElementById('progress-text').textContent = `Question ${currentIndex + 1}/${questions.length}`;
}

// ===== SHOW RESULTS =====
function showResults() {
    const total = questions.length;
    const pct = total > 0 ? Math.round((score / total) * 100 * 10) / 10 : 0;

    document.getElementById('final-score').textContent = `${score}/${total}`;
    document.getElementById('final-percentage').textContent = `${pct}%`;

    let msg = '';
    if (pct >= 80) msg = '🌟 Excellent ! Vous êtes bien préparé(e) pour le concours ENA !';
    else if (pct >= 60) msg = '👍 Bon travail ! Continuez à vous entraîner pour progresser.';
    else if (pct >= 40) msg = '💪 Pas mal, mais il faut encore réviser certains thèmes.';
    else msg = '📚 Continuez à réviser ! La persévérance est la clé de la réussite.';
    document.getElementById('encouragement-message').textContent = msg;

    // Stats by theme
    const themeStats = {};
    answersHistory.forEach(h => {
        if (!themeStats[h.theme]) themeStats[h.theme] = { correct: 0, total: 0 };
        themeStats[h.theme].total++;
        if (h.is_correct) themeStats[h.theme].correct++;
    });

    const statsContainer = document.getElementById('themes-stats');
    statsContainer.innerHTML = '';
    Object.entries(themeStats).forEach(([theme, st]) => {
        const tPct = st.total > 0 ? Math.round(st.correct / st.total * 100) : 0;
        const div = document.createElement('div');
        div.className = 'theme-stat';
        div.innerHTML = `<span class="theme-name">${theme}</span><span class="theme-score">${st.correct}/${st.total} (${tPct}%)</span>`;
        statsContainer.appendChild(div);
    });

    // Recap
    const recapContainer = document.getElementById('answers-recap');
    recapContainer.innerHTML = '';
    answersHistory.forEach((h, i) => {
        const status = h.skipped ? '⏭️' : (h.is_correct ? '✅' : '❌');
        const cls = h.skipped ? 'neutral' : (h.is_correct ? 'correct' : 'incorrect');
        const userResp = h.skipped ? 'Question sautée' : h.user_answer;
        const div = document.createElement('div');
        div.className = `answer-item ${cls}`;
        div.innerHTML = `
            <div class="answer-header">
                <span class="answer-status">${status}</span>
                <small>[${h.theme}]</small>
            </div>
            <div class="answer-question">Q${i + 1}: ${h.question}</div>
            <div class="answer-detail">
                Votre réponse : <strong>${userResp}</strong> |
                Réponse correcte : <strong>${h.correct_answer}</strong>
            </div>`;
        recapContainer.appendChild(div);
    });

    showPage('results');
}

// ===== PAGE NAVIGATION =====
retryBtn.addEventListener('click', () => { showPage('home'); });

function showPage(page) {
    homePage.classList.remove('active');
    quizPage.classList.remove('active');
    resultsPage.classList.remove('active');
    if (page === 'home') homePage.classList.add('active');
    else if (page === 'quiz') quizPage.classList.add('active');
    else if (page === 'results') resultsPage.classList.add('active');
}
