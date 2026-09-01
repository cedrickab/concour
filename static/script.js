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
    if (!Array.isArray(QUIZ_QUESTIONS)) {
        throw new Error('Quiz data is unavailable.');
    }

    const themeMap = new Map();
    QUIZ_QUESTIONS.forEach(q => {
        const themeName = q.theme || "Culture Générale — Langue française";
        if (!themeMap.has(themeName)) {
            themeMap.set(themeName, []);
        }
        themeMap.get(themeName).push(q);
    });

    const catalog = [];
    themeMap.forEach((questions, name) => {
        catalog.push({ name, questions });
    });

    return catalog;
}

const CAS_PRATIQUE_THEME = 'Droit administratif';
const BONUS_CAS_PRATIQUES = 2; // number of Cas Pratiques added as bonus on top

function getQuizQuestions(numQuestions, selectedThemeNames) {
    let allThemes = getThemeCatalog();

    // Separate Cas Pratiques pool from scored themes
    const casPratiquesTheme = allThemes.find(t => t.name === CAS_PRATIQUE_THEME);
    let scoredThemes = allThemes.filter(t => t.name !== CAS_PRATIQUE_THEME);

    if (selectedThemeNames && selectedThemeNames.length > 0) {
        scoredThemes = scoredThemes.filter(t => selectedThemeNames.includes(t.name));
    }

    if (scoredThemes.length === 0 && !casPratiquesTheme) return [];

    // --- Build scored questions pool ---
    let scored = [];
    if (scoredThemes.length > 0) {
        const numThemes = scoredThemes.length;
        const perTheme = Math.floor(numQuestions / numThemes);
        const remaining = numQuestions % numThemes;

        scoredThemes.forEach((theme, i) => {
            const n = Math.min(perTheme + (i < remaining ? 1 : 0), theme.questions.length);
            const shuffled = [...theme.questions].sort(() => Math.random() - 0.5);
            shuffled.slice(0, n).forEach(q => scored.push({ ...q, theme: theme.name }));
        });

        // Fisher-Yates shuffle on scored questions
        for (let i = scored.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [scored[i], scored[j]] = [scored[j], scored[i]];
        }
        scored = scored.slice(0, numQuestions);
    }

    // --- Build bonus Cas Pratiques ---
    let bonus = [];
    if (casPratiquesTheme) {
        // If user explicitly selected ONLY Droit Administratif, treat all as bonus (no scored)
        const onlyCasPratiques = selectedThemeNames &&
            selectedThemeNames.length === 1 &&
            selectedThemeNames[0] === CAS_PRATIQUE_THEME;

        const bonusCount = onlyCasPratiques ? numQuestions : BONUS_CAS_PRATIQUES;
        const shuffledCas = [...casPratiquesTheme.questions].sort(() => Math.random() - 0.5);
        shuffledCas.slice(0, bonusCount).forEach(q => bonus.push({ ...q, theme: CAS_PRATIQUE_THEME }));
    }

    // Scored questions first, bonus Cas Pratiques at the end
    return [...scored, ...bonus];
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

    const isCasPratique = q.theme === 'Droit administratif';

    if (isCasPratique) {
        // Cas Pratique: no options, just a "Révéler l'analyse" button
        const hint = document.createElement('p');
        hint.style.cssText = 'color:#7c6fcd;font-style:italic;font-size:0.95em;margin:12px 0;';
        hint.textContent = '⚖️ Cas pratique — Réfléchissez à la solution juridique, puis révélez l\'analyse.';
        container.appendChild(hint);

        const revealBtn = document.createElement('button');
        revealBtn.className = 'option-btn';
        revealBtn.style.cssText = 'background:#7c6fcd;color:#fff;font-weight:bold;margin-top:8px;border:none;';
        revealBtn.textContent = '💡 Révéler l\'analyse juridique';
        revealBtn.addEventListener('click', () => submitAnswer('__cas_pratique__', null));
        container.appendChild(revealBtn);

        skipBtn.style.display = 'none';
    } else {
        q.options.forEach(option => {
            const letter = option.split(')')[0].trim();
            const btn = document.createElement('button');
            btn.className = 'option-btn';
            btn.textContent = option;
            btn.dataset.answer = letter;
            btn.addEventListener('click', () => submitAnswer(letter, btn));
            container.appendChild(btn);
        });
        skipBtn.disabled = false;
        skipBtn.style.display = '';
    }

    document.getElementById('feedback-box').classList.add('hidden');
}

// ===== SUBMIT ANSWER =====
function submitAnswer(answer, clickedBtn) {
    const allBtns = document.querySelectorAll('.option-btn');
    allBtns.forEach(b => b.disabled = true);
    skipBtn.disabled = true;

    const q = questions[currentIndex];
    const isCasPratique = q.theme === 'Droit administratif';
    const skipped = answer === '';
    let isCorrect = null;

    if (isCasPratique) {
        // Bonus question — no score impact
        const feedbackBox = document.getElementById('feedback-box');
        const feedbackContent = document.getElementById('feedback-content');
        feedbackBox.className = 'feedback-box bonus';
        feedbackContent.innerHTML = `
            <div class="feedback-title">⚖️ Analyse juridique</div>
            <div class="feedback-text">💡 <strong>Solution type :</strong> ${q.explanation}</div>`;
        feedbackBox.classList.remove('hidden');

        answersHistory.push({
            question: q.question,
            theme: q.theme,
            user_answer: '(Cas pratique)',
            correct_answer: q.answer,
            is_correct: null,
            skipped: false,
            is_cas_pratique: true
        });

    } else {
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

        feedbackBox.classList.remove('hidden');

        answersHistory.push({
            question: q.question,
            theme: q.theme,
            user_answer: answer || '—',
            correct_answer: q.answer,
            is_correct: isCorrect,
            skipped
        });
    }

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
    // Separate Cas Pratiques (bonus) from scored questions
    const scoredHistory = answersHistory.filter(h => !h.is_cas_pratique);
    const bonusHistory  = answersHistory.filter(h => h.is_cas_pratique);

    const total = scoredHistory.length;
    const pct = total > 0 ? Math.round((score / total) * 100 * 10) / 10 : 0;

    document.getElementById('final-score').textContent = `${score}/${total}`;
    document.getElementById('final-percentage').textContent = `${pct}%`;

    let msg = '';
    if (pct >= 80) msg = '🌟 Excellent ! Vous êtes bien préparé(e) pour le concours ENA !';
    else if (pct >= 60) msg = '👍 Bon travail ! Continuez à vous entraîner pour progresser.';
    else if (pct >= 40) msg = '💪 Pas mal, mais il faut encore réviser certains thèmes.';
    else msg = '📚 Continuez à réviser ! La persévérance est la clé de la réussite.';
    document.getElementById('encouragement-message').textContent = msg;

    // Stats by theme (scored only)
    const themeStats = {};
    scoredHistory.forEach(h => {
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

    // Bonus Cas Pratiques stats
    if (bonusHistory.length > 0) {
        const bonusDiv = document.createElement('div');
        bonusDiv.className = 'theme-stat';
        bonusDiv.style.cssText = 'border-left:4px solid #7c6fcd;background:#f0eeff;';
        bonusDiv.innerHTML = `<span class="theme-name">⚖️ Droit administratif (Bonus)</span><span class="theme-score">${bonusHistory.length} cas pratique(s) — non comptés</span>`;
        statsContainer.appendChild(bonusDiv);
    }

    // Recap — scored questions
    const recapContainer = document.getElementById('answers-recap');
    recapContainer.innerHTML = '';

    scoredHistory.forEach((h, i) => {
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

    // Recap — Cas Pratiques bonus section
    if (bonusHistory.length > 0) {
        const bonusHeader = document.createElement('div');
        bonusHeader.style.cssText = 'margin-top:20px;padding:8px 12px;background:#7c6fcd;color:#fff;border-radius:8px;font-weight:bold;';
        bonusHeader.textContent = `⚖️ Cas Pratiques — ${bonusHistory.length} analysés (non comptés dans le score)`;
        recapContainer.appendChild(bonusHeader);

        bonusHistory.forEach((h, i) => {
            const div = document.createElement('div');
            div.className = 'answer-item neutral';
            div.style.cssText = 'border-left:4px solid #7c6fcd;';
            div.innerHTML = `
                <div class="answer-header">
                    <span class="answer-status">⚖️</span>
                    <small>[${h.theme}]</small>
                </div>
                <div class="answer-question">Cas ${i + 1}: ${h.question}</div>`;
            recapContainer.appendChild(div);
        });
    }

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

