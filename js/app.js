(function () {
  const copy = {
    en: {
      guide: "Three-step path",
      guideText: "Pick a subject, open a topic, then use examples and practice before the exam.",
      chooseLanguageFirst: "Choose your language first to land in the right curriculum.",
      startHere: "Start here",
      freeAccess: "100% free access",
      curriculum: "Curriculum-aligned",
      reviewReady: "Built for fast review",
      sectionCount: "Sections",
      topicCount: "Topics",
      estimatedRead: "Estimated read",
      print: "Print",
      copyLink: "Copy link",
      copied: "Copied",
      share: "Share",
      shareText: "Actually helped with exam prep 📚 Free study guides →",
      backToSection: "Back to section",
      onThisPage: "On this page",
      practiceJump: "Jump to practice",
      continueLearning: "Continue learning",
      previousTopic: "Previous topic",
      nextTopic: "Next topic",
      relatedTopics: "Related topics",
      quickJump: "Quick jump",
      overview: "Overview",
      notFound: "Use one of the sections below to get back on track.",
      backTop: "Back to top"
    },
    ko: {
      guide: "3단계 학습 흐름",
      guideText: "과목을 고르고, 주제를 열고, 예제와 문제로 마무리하세요.",
      chooseLanguageFirst: "내 교육과정에 맞는 언어를 먼저 선택하세요.",
      startHere: "여기서 시작",
      freeAccess: "전부 무료",
      curriculum: "교육과정 기준",
      reviewReady: "시험 직전 복습형",
      sectionCount: "섹션 수",
      topicCount: "주제 수",
      estimatedRead: "예상 학습 시간",
      print: "인쇄",
      copyLink: "링크 복사",
      copied: "복사됨",
      share: "공유하기",
      shareText: "수능·내신 공부할 때 이거 씀 👀 전부 무료임 →",
      backToSection: "과목으로 돌아가기",
      onThisPage: "이 페이지에서",
      practiceJump: "문제 바로가기",
      continueLearning: "이어서 학습하기",
      previousTopic: "이전 주제",
      nextTopic: "다음 주제",
      relatedTopics: "관련 주제",
      quickJump: "빠른 이동",
      overview: "핵심 안내",
      notFound: "아래 경로로 이동하면 원하는 학습 자료를 다시 찾을 수 있습니다.",
      backTop: "위로"
    },
    ja: {
      guide: "3ステップ学習",
      guideText: "教科を選び、単元を開き、例題と練習で仕上げます。",
      chooseLanguageFirst: "先に言語を選ぶと、正しいカリキュラムに入れます。",
      startHere: "ここから",
      freeAccess: "すべて無料",
      curriculum: "学習指導要領対応",
      reviewReady: "試験前の復習向け",
      sectionCount: "セクション数",
      topicCount: "単元数",
      estimatedRead: "学習目安",
      print: "印刷",
      copyLink: "リンクをコピー",
      copied: "コピー済み",
      share: "シェア",
      shareText: "受験対策に使えた 📚 無料でここまで揃ってる →",
      backToSection: "教科へ戻る",
      onThisPage: "このページ",
      practiceJump: "練習へ移動",
      continueLearning: "続けて学ぶ",
      previousTopic: "前の単元",
      nextTopic: "次の単元",
      relatedTopics: "関連単元",
      quickJump: "クイック移動",
      overview: "概要",
      notFound: "下の導線から目的の学習ページに戻れます。",
      backTop: "上へ"
    },
    zh: {
      guide: "三步学习路径",
      guideText: "先选学科，再开主题，最后用例题和练习完成复习。",
      chooseLanguageFirst: "请先选择语言，再进入对应课程体系。",
      startHere: "从这里开始",
      freeAccess: "永久免费",
      curriculum: "贴合课程标准",
      reviewReady: "适合考前速复习",
      sectionCount: "章节数",
      topicCount: "主题数",
      estimatedRead: "预计阅读",
      print: "打印",
      copyLink: "复制链接",
      copied: "已复制",
      share: "分享",
      shareText: "备考神器 📚 这套免费资料真的很全 →",
      backToSection: "返回学科页",
      onThisPage: "本页内容",
      practiceJump: "跳到练习",
      continueLearning: "继续学习",
      previousTopic: "上一主题",
      nextTopic: "下一主题",
      relatedTopics: "相关主题",
      quickJump: "快速跳转",
      overview: "概览",
      notFound: "可通过下方入口回到对应的学习内容。",
      backTop: "返回顶部"
    }
  };

  const page = window.__STUDYHUB_PAGE || {};
  const lang = document.documentElement.lang || page.lang || "en";
  const t = copy[lang] || copy.en;

  function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }

  function formatMinutes(minutes) {
    if (lang === "ko") return `${minutes}분`;
    if (lang === "ja") return `${minutes}分`;
    if (lang === "zh") return `${minutes}分钟`;
    return `${minutes} min`;
  }

  function buildStat(value, label) {
    const card = el("div", "stat-card");
    card.appendChild(el("strong", "stat-value", value));
    card.appendChild(el("span", "stat-label", label));
    return card;
  }

  function addProgressBar() {
    const bar = el("div", "scroll-progress");
    document.body.appendChild(bar);
    const update = () => {
      const height = document.documentElement.scrollHeight - window.innerHeight;
      const progress = height > 0 ? (window.scrollY / height) * 100 : 0;
      bar.style.setProperty("--progress", `${Math.min(progress, 100)}%`);
    };
    update();
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
  }

  function addBackToTop() {
    const button = el("button", "back-to-top", t.backTop);
    button.type = "button";
    button.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
    const update = () => button.classList.toggle("visible", window.scrollY > 520);
    update();
    window.addEventListener("scroll", update, { passive: true });
    document.body.appendChild(button);
  }

  function enhanceHero() {
    const hero = document.querySelector(".hero");
    if (!hero || hero.querySelector(".hero-stats")) return;

    const stats = el("div", "hero-stats");
    if (page.type === "global-home") {
      stats.appendChild(buildStat("4", lang === "ko" ? "언어 버전" : lang === "ja" ? "言語版" : lang === "zh" ? "语言版本" : "Language versions"));
      stats.appendChild(buildStat("3", lang === "ko" ? "핵심 과목" : lang === "ja" ? "主要教科" : lang === "zh" ? "核心学科" : "Core subjects"));
      stats.appendChild(buildStat("Free", t.freeAccess));
    } else if (page.type === "language-home") {
      stats.appendChild(buildStat("3", lang === "ko" ? "과목" : lang === "ja" ? "教科" : lang === "zh" ? "学科" : "Subjects"));
      stats.appendChild(buildStat("100%", t.curriculum));
      stats.appendChild(buildStat("Fast", t.reviewReady));
    }
    hero.appendChild(stats);

    const strip = el("div", "study-path");
    strip.appendChild(el("strong", null, t.guide));
    strip.appendChild(el("p", null, t.guideText));
    hero.appendChild(strip);
  }

  function markFirstCard(selector) {
    const firstCard = document.querySelector(selector);
    if (!firstCard || firstCard.querySelector(".card-badge")) return;
    const badge = el("span", "card-badge", t.startHere);
    firstCard.insertBefore(badge, firstCard.firstChild);
  }

  function enhanceGlobalHome() {
    enhanceHero();
    markFirstCard(".subject-grid .subject-card");
    const hero = document.querySelector(".hero");
    if (hero && !hero.querySelector(".priority-note")) {
      const note = el("div", "priority-note");
      note.appendChild(el("strong", null, t.chooseLanguageFirst));
      hero.appendChild(note);
    }

    const main = document.querySelector("main");
    const headings = main ? Array.from(main.querySelectorAll(":scope > h2")) : [];
    const languageHeading = headings[1];
    if (languageHeading) languageHeading.id = "language-directory";
    document.querySelectorAll(".subject-grid .subject-card").forEach((card) => {
      const href = card.getAttribute("href");
      if (href && href.startsWith("en/")) {
        card.setAttribute("href", "#language-directory");
      }
    });
  }


  /* ---- 첫인상 설득력 강화 (루프36) ---- */
  function initHeroFirstImpression() {
    // 사회적 증명 카운터
    const proofEl = document.querySelector(".hero-social-proof");
    if (proofEl) {
      const seed = Math.floor(Date.now() / 900000); // 15분마다 갱신
      const base = 43;
      const pseudo = ((seed * 1103515245 + 12345) & 0x7fffffff) % 28;
      proofEl.textContent = `지금 ${base + pseudo}명 공부 중`;
    }
    // localStorage 기반 재방문 CTA
    const resumeEl = document.querySelector(".hero-resume-cta");
    if (resumeEl) {
      try {
        const lastPage  = localStorage.getItem("sh_last_page");
        const lastTitle = localStorage.getItem("sh_last_title");
        if (lastPage && lastTitle) {
          resumeEl.href = lastPage;
          const labelEl = resumeEl.querySelector(".resume-label");
          if (labelEl) labelEl.textContent = `"${lastTitle}" 계속하기 →`;
          resumeEl.style.display = "inline-flex";
        }
      } catch(e) {}
    }
  }

  function initTodayConcept() {
    var el2 = document.querySelector(".today-concept-name");
    if (!el2) return;
    var conceptsByLang = {
      ko: [
        { name: "이항정리", url: "math/statistics.html" },
        { name: "함수의 극한", url: "math/calculus.html" },
        { name: "이차방정식 판별식", url: "math/equations.html" },
        { name: "삼각함수 기본", url: "math/trigonometry.html" },
        { name: "적분의 기본정리", url: "math/calculus.html" },
        { name: "지수·로그 법칙", url: "math/functions.html" },
        { name: "확률의 덧셈 법칙", url: "math/statistics.html" },
        { name: "뉴턴의 운동 법칙", url: "science/physics.html" },
        { name: "원자의 전자 배치", url: "science/atoms.html" },
        { name: "에너지 보존 법칙", url: "science/energy.html" },
        { name: "분수의 나눗셈", url: "math/fractions.html" },
        { name: "한국어 시제 표현", url: "korean/grammar.html" },
        { name: "고전 시조의 형식", url: "korean/classical.html" },
        { name: "소설의 서술 시점", url: "korean/modern.html" },
        { name: "영어 가정법", url: "english/grammar.html" },
        { name: "관계대명사 용법", url: "english/grammar.html" },
        { name: "생태계 에너지 흐름", url: "science/ecology.html" },
        { name: "세포의 구조", url: "science/cells.html" },
        { name: "화학 결합의 종류", url: "science/atoms.html" },
        { name: "지구의 층상 구조", url: "science/earth.html" },
        { name: "미분의 정의", url: "math/calculus.html" },
        { name: "영어 어휘 어근법", url: "english/vocabulary.html" },
        { name: "글쓰기 구조화", url: "korean/writing.html" },
        { name: "소수의 성질", url: "math/fractions.html" },
      ],
      en: [
        { name: "Derivative: slope of a curve", url: "math/calculus.html" },
        { name: "Fractions: why flip when dividing?", url: "math/fractions.html" },
        { name: "Equations: the balance scale", url: "math/algebra.html" },
        { name: "Inertia: constant speed without force", url: "science/physics.html" },
        { name: "Atoms: 99.9999% empty space", url: "science/atoms.html" },
        { name: "ATP: the cell energy currency", url: "science/biology.html" },
        { name: "Energy conservation law", url: "science/energy.html" },
        { name: "Tenses: the time map of English", url: "english/grammar.html" },
        { name: "Relative pronouns: who/which/that", url: "english/grammar.html" },
        { name: "Triangle angles: why 180 degrees?", url: "math/geometry.html" },
        { name: "Mean vs median: which is better?", url: "math/statistics.html" },
        { name: "Cell as a mini city", url: "science/cells.html" },
        { name: "Ecosystem energy flow", url: "science/ecology.html" },
        { name: "Vocabulary: roots and affixes", url: "english/vocabulary.html" },
      ],
      ja: [
        { name: "微分 = 曲線の接線の傾き", url: "math/calculus.html" },
        { name: "分数の割り算: なぜ逆数をかける?", url: "math/fractions.html" },
        { name: "方程式 = 天秤", url: "math/equations.html" },
        { name: "慣性: 力がなければ等速運動", url: "science/physics.html" },
        { name: "原子 = 太陽系の縮小版", url: "science/atoms.html" },
        { name: "ATP = エネルギー通貨", url: "science/biology.html" },
        { name: "エネルギー保存の法則", url: "science/energy.html" },
        { name: "時制 = 時間の地図", url: "english/grammar.html" },
        { name: "三角形の内角の和 = 180度", url: "math/geometry.html" },
        { name: "助動詞 = 古文読解の鍵", url: "japanese/classical.html" },
        { name: "平均 vs 中央値", url: "math/statistics.html" },
        { name: "細胞 = ミニチュール都市", url: "science/cells.html" },
        { name: "語根+接辞で単語を推測", url: "english/vocabulary.html" },
      ],
      zh: [
        { name: "导数 = 曲线的瞬间变化率", url: "math/calculus.html" },
        { name: "分数除法: 为什么要乘以倒数?", url: "math/fractions.html" },
        { name: "方程 = 天平秤", url: "math/equations.html" },
        { name: "惯性: 没有力就匀速运动", url: "science/physics.html" },
        { name: "原子 = 辷你太阳系", url: "science/atoms.html" },
        { name: "ATP = 细胞能量货币", url: "science/biology.html" },
        { name: "能量守恒定律", url: "science/energy.html" },
        { name: "时态 = 时间的地図", url: "english/grammar.html" },
        { name: "三角形内角和 = 180度", url: "math/geometry.html" },
        { name: "平均数 vs 中位数", url: "math/statistics.html" },
        { name: "细胞 = 微型城市", url: "science/cells.html" },
        { name: "词根+前后缀推断词义", url: "english/vocabulary.html" },
        { name: "语法 = 语言的设计图", url: "chinese/grammar.html" },
      ],
    };
    var list = conceptsByLang[lang] || conceptsByLang.en;
    var today = new Date();
    var dayOfYear = Math.floor((today - new Date(today.getFullYear(), 0, 0)) / 86400000);
    var concept = list[dayOfYear % list.length];
    el2.textContent = concept.name;

    var linkEl = document.querySelector(".today-concept-link");
    if (linkEl) {
      var path = location.pathname;
      var depth = (path.match(/\/[^\/]+/g) || []).length;
      var prefix = depth > 3 ? "../../" : depth > 2 ? "../" : "./";
      linkEl.href = prefix + concept.url;
    }
    var dateEl = document.querySelector(".today-concept-date");
    if (dateEl) {
      var mo = lang === "ko" ? ["요1월","요2월","요3월","요4월","요5월","요6월","요7월","요8월","요9월","요10월","요11월","요12월"]
              : lang === "ja" ? ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
              : ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
      if (lang === "ko") {
        var kmo = ["1월","2월","3월","4월","5월","6월","7월","8월","9월","10월","11월","12월"];
        dateEl.textContent = kmo[today.getMonth()] + " " + today.getDate() + "일";
      } else if (lang === "ja") {
        dateEl.textContent = (today.getMonth()+1) + "月" + today.getDate() + "日";
      } else if (lang === "zh") {
        dateEl.textContent = (today.getMonth()+1) + "月" + today.getDate() + "日";
      } else {
        var emo = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
        dateEl.textContent = emo[today.getMonth()] + " " + today.getDate();
      }
    }
  }
  function saveLastPage() {
    try {
      const title = document.querySelector("article h1, main h1")?.textContent?.trim();
      if (title && location.pathname) {
        localStorage.setItem("sh_last_page",  location.pathname);
        localStorage.setItem("sh_last_title", title);
      }
    } catch(e) {}
  }

  function enhanceLanguageHome() {
    enhanceHero();
    markFirstCard(".subject-grid .subject-card");
    initHeroFirstImpression();
    initTodayConcept();
  }

  function enhanceSectionIndex() {
    markFirstCard(".topic-grid .topic-card");
    initTodayConcept();

    const main = document.querySelector("main");
    const heroHeading = main ? main.querySelector("h1") : null;
    if (!main || !heroHeading || document.querySelector(".section-overview")) return;

    const intro = heroHeading.nextElementSibling;
    const overview = el("section", "section-overview");
    const heading = el("div", "section-overview-heading");
    heading.appendChild(el("strong", null, t.overview));
    heading.appendChild(el("p", null, page.sectionTitle || heroHeading.textContent.trim()));
    overview.appendChild(heading);

    const grid = el("div", "section-overview-grid");
    const topicCount = Array.isArray(page.links) ? page.links.length : document.querySelectorAll(".topic-card[href$='.html']").length;
    grid.appendChild(buildStat(String(topicCount), t.topicCount));
    grid.appendChild(buildStat(page.firstTopic ? page.firstTopic.title : "Free", t.startHere));
    grid.appendChild(buildStat("1-2", t.estimatedRead));
    overview.appendChild(grid);

    if (intro) {
      intro.insertAdjacentElement("afterend", overview);
    } else {
      heroHeading.insertAdjacentElement("afterend", overview);
    }

    if (Array.isArray(page.links) && page.links.length) {
      const quickJump = el("div", "quick-jump");
      quickJump.appendChild(el("strong", null, t.quickJump));
      page.links.forEach((item) => {
        const link = el("a", "anchor-chip", item.title);
        link.href = item.href;
        quickJump.appendChild(link);
      });
      overview.appendChild(quickJump);
    }
  }

  function copyCurrentUrl(button) {
    const currentUrl = window.location.href;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(currentUrl).then(() => {
        button.textContent = t.copied;
        window.setTimeout(() => {
          button.textContent = t.copyLink;
        }, 1600);
      });
      return;
    }
    window.prompt("Copy this link", currentUrl);
  }

  function shareCurrentPage() {
    const url = window.location.href;
    const title = document.title;
    const shareTextBase = (t.shareText || "Check out this free study guide! 📚");
    const text = `${shareTextBase} ${title}`;
    if (navigator.share) {
      navigator.share({ title, text: shareTextBase, url }).catch(() => {});
      return;
    }
    const twitterUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}`;
    window.open(twitterUrl, "_blank", "noopener,noreferrer,width=600,height=400");
  }

  function enhanceArticle() {
    saveLastPage();
    const main = document.querySelector("main");
    const articleMeta = main ? main.querySelector(".article-meta") : null;
    if (!main || !articleMeta || document.querySelector(".article-shell")) return;

    const rest = [];
    let capture = false;
    Array.from(main.children).forEach((child) => {
      if (capture) rest.push(child);
      if (child === articleMeta) capture = true;
    });
    if (!rest.length) return;

    const articleShell = el("div", "article-shell");
    const articleMain = el("div", "article-main");
    const sidebar = el("aside", "article-sidebar");
    articleShell.append(articleMain, sidebar);
    articleMeta.insertAdjacentElement("afterend", articleShell);
    rest.forEach((node) => articleMain.appendChild(node));

    const headings = Array.from(articleMain.querySelectorAll("h2"));
    headings.forEach((heading, index) => {
      if (!heading.id) heading.id = `section-${index + 1}`;
    });

    const actions = el("div", "page-actions");
    const printButton = el("button", "page-action-button", t.print);
    printButton.type = "button";
    printButton.addEventListener("click", () => window.print());
    const copyButton = el("button", "page-action-button", t.copyLink);
    copyButton.type = "button";
    copyButton.addEventListener("click", () => copyCurrentUrl(copyButton));
    const shareButton = el("button", "page-action-button page-action-share", t.share || "Share");
    shareButton.type = "button";
    shareButton.addEventListener("click", () => shareCurrentPage());
    actions.append(printButton, copyButton, shareButton);
    if (page.sectionHref) {
      const backLink = el("a", "page-action-link", t.backToSection);
      backLink.href = page.sectionHref;
      actions.appendChild(backLink);
    }
    articleMeta.insertAdjacentElement("afterend", actions);

    const words = articleMain.textContent.trim().split(/\s+/).length;
    const minutes = Math.max(4, Math.round(words / 190));
    const practiceHeading = headings.find((heading) => /(practice|문제|연습|練習|练习)/i.test(heading.textContent));

    const summary = el("section", "utility-card");
    summary.appendChild(el("strong", "utility-title", t.overview));
    const summaryList = el("div", "summary-list");
    summaryList.appendChild(buildStat(String(headings.length), t.sectionCount));
    summaryList.appendChild(buildStat(formatMinutes(minutes), t.estimatedRead));
    summaryList.appendChild(buildStat(page.sectionTitle || "", t.backToSection));
    summary.appendChild(summaryList);
    if (practiceHeading) {
      const practiceLink = el("a", "utility-link", t.practiceJump);
      practiceLink.href = `#${practiceHeading.id}`;
      summary.appendChild(practiceLink);
    }
    sidebar.appendChild(summary);

    const toc = el("section", "utility-card");
    toc.appendChild(el("strong", "utility-title", t.onThisPage));
    const tocList = el("div", "toc-list");
    headings.forEach((heading) => {
      const link = el("a", "toc-link", heading.textContent.trim());
      link.href = `#${heading.id}`;
      tocList.appendChild(link);
    });
    toc.appendChild(tocList);
    sidebar.appendChild(toc);

    const relatedItems = [];
    if (page.prev) relatedItems.push({ ...page.prev, label: t.previousTopic });
    if (page.next) relatedItems.push({ ...page.next, label: t.nextTopic });
    (page.related || []).slice(0, 2).forEach((item) => relatedItems.push({ ...item, label: t.relatedTopics }));

    if (relatedItems.length) {
      const section = el("section", "continue-section");
      section.appendChild(el("h2", null, t.continueLearning));
      const grid = el("div", "continue-grid");
      relatedItems.forEach((item) => {
        const card = el("a", "continue-card");
        card.href = item.href;
        card.appendChild(el("span", "continue-label", item.label));
        card.appendChild(el("strong", null, item.title));
        grid.appendChild(card);
      });
      section.appendChild(grid);
      articleMain.appendChild(section);
    }
  }

  // ── 루프65: TOC 활성 섹션 하이라이트 (IntersectionObserver) ──
  function initTocHighlight() {
    const headings = Array.from(document.querySelectorAll("main h2[id]"));
    if (!headings.length) return;

    // page-overview 링크 맵
    const overviewLinks = new Map();
    document.querySelectorAll(".page-overview-list a[href^='#']").forEach(a => {
      overviewLinks.set(a.getAttribute("href").slice(1), a);
    });
    // sidebar toc 링크 맵
    const tocLinks = new Map();
    document.querySelectorAll(".toc-link[href^='#']").forEach(a => {
      tocLinks.set(a.getAttribute("href").slice(1), a);
    });

    if (!overviewLinks.size && !tocLinks.size) return;

    function setActive(id) {
      overviewLinks.forEach((el, key) => el.classList.toggle("active", key === id));
      tocLinks.forEach((el, key) => el.classList.toggle("active", key === id));
    }

    let activeId = headings[0]?.id;
    setActive(activeId);

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          activeId = entry.target.id;
          setActive(activeId);
        }
      });
    }, { rootMargin: "-10% 0px -75% 0px", threshold: 0 });

    headings.forEach(h => observer.observe(h));
  }

  function enhance404() {
    const main = document.querySelector("main");
    if (!main || main.querySelector(".empty-state-note")) return;
    const note = el("p", "empty-state-note", t.notFound);
    main.appendChild(note);
  }

  function injectBreadcrumbJsonLd() {
    const crumbs = document.querySelectorAll("nav.breadcrumb a, nav.breadcrumb span:last-child");
    if (!crumbs.length) return;
    const base = "https://criel2019.github.io/studyhub/";
    const items = [];
    crumbs.forEach((node, i) => {
      const name = node.textContent.trim();
      if (!name) return;
      const entry = { "@type": "ListItem", "position": i + 1, "name": name };
      if (node.tagName === "A") {
        const href = node.getAttribute("href");
        entry["item"] = href && href.startsWith("http") ? href : base;
      }
      items.push(entry);
    });
    if (items.length < 2) return;
    const ld = { "@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items };
    const script = document.createElement("script");
    script.type = "application/ld+json";
    script.textContent = JSON.stringify(ld);
    document.head.appendChild(script);
  }

  function addNavScrolled() {
    const hdr = document.querySelector("header");
    if (!hdr) return;
    const update = () => hdr.classList.toggle("nav-scrolled", window.scrollY > 48);
    update();
    window.addEventListener("scroll", update, { passive: true });
  }

  // ── 루프62: curriculum-badge title 자동 주입 ──
  function initCurriculumBadgeTips() {
    const map = {
      // 수학
      "03수학01-01": "초등 3학년 수학 · 자연수의 덧셈",
      "03수학01-02": "초등 3학년 수학 · 받아올림 덧셈",
      "03수학01-03": "초등 3학년 수학 · 받아올림 연속 덧셈",
      "03수학01-04": "초등 3학년 수학 · 덧셈의 성질",
      "04수학01-01": "초등 4학년 수학 · 세 수의 덧셈",
      "09수02-04": "중학교 수학 · 일차방정식 풀이",
      "09수02-06": "중학교 수학 · 이차방정식",
      "09수학05-01": "중학교 수학 · 기본 도형",
      "09수학05-02": "중학교 수학 · 삼각형의 성질",
      "09수학05-03": "중학교 수학 · 사각형의 성질",
      "09수학05-04": "중학교 수학 · 원의 성질",
      "09수학05-05": "중학교 수학 · 입체도형",
      "10수학01-01": "고등 통합수학 · 수와 연산",
      "12수II01-01": "고등 수학Ⅱ · 극한",
      "12수II01-02": "고등 수학Ⅱ · 미분",
      "12수II01-03": "고등 수학Ⅱ · 적분",
      "12수I01-01": "고등 수학Ⅰ · 삼각함수",
      "12수I02-01": "고등 수학Ⅰ · 수열",
      // 과학
      "10통과01-01": "고등 통합과학 · 물질의 분류",
      "10통과01-02": "고등 통합과학 · 원자 구조",
      "10통과01-03": "고등 통합과학 · 이온",
      "10통과01-04": "고등 통합과학 · 분자와 화학식",
      "10통과2-01": "고등 통합과학 · 뉴턴 운동 법칙",
      "10통과2-03": "고등 통합과학 · 에너지",
      "10통과03-01": "고등 통합과학 · 에너지 전환",
      "10통과03-02": "고등 통합과학 · 신재생에너지",
      "12화학I01-01": "고등 화학Ⅰ · 원소와 주기율표",
      "12화학I01-02": "고등 화학Ⅰ · 화학 결합",
      "12화학I02-01": "고등 화학Ⅰ · 화학 반응식",
      "12화학I03-01": "고등 화학Ⅰ · 산과 염기",
      "12화학I03-02": "고등 화학Ⅰ · 산화·환원",
      "12물리I02-01": "고등 물리학Ⅰ · 에너지 전환과 보존",
      "12물리I02-02": "고등 물리학Ⅰ · 열역학",
      "12생명I01-01": "고등 생명과학Ⅰ · 세포의 구조",
      "12생명I01-02": "고등 생명과학Ⅰ · 세포의 비교",
      "12생명I02-01": "고등 생명과학Ⅰ · 세포 분열",
      // 국어
      "09국02-01": "중학교 국어 · 독서의 방법",
      "09국03-01": "중학교 국어 · 글쓰기의 과정",
      "12국04-01": "고등 국어 · 국어의 역사",
      "12국04-02": "고등 국어 · 언어와 국어",
      // 영어
      "09영01-01": "중학교 영어 · 듣기·말하기 기초",
      "09영03-01": "중학교 영어 · 읽기 이해",
      "12영01-01": "고등 영어 · 말하기·듣기",
      "12영03-01": "고등 영어 · 독해"
    };
    document.querySelectorAll(".curriculum-badge").forEach(el => {
      if (el.hasAttribute("title")) return;
      const code = el.textContent.replace(/[\[\]]/g, "").trim();
      if (map[code]) el.setAttribute("title", map[code]);
    });
  }

  // ── 루프58: 표 접근성 — scope 속성 자동 주입 ──
  function initTableScope() {
    document.querySelectorAll("table").forEach(table => {
      table.querySelectorAll("thead th").forEach(th => {
        if (!th.hasAttribute("scope")) th.setAttribute("scope", "col");
      });
      table.querySelectorAll("tbody tr").forEach(tr => {
        const firstTh = tr.querySelector("th");
        if (firstTh && !firstTh.hasAttribute("scope")) firstTh.setAttribute("scope", "row");
      });
    });
  }

  // ── 루프34: 표 카드 변환 — thead th → td[data-label] 자동 주입 ──
  function initTableCards() {
    document.querySelectorAll(".table-wrap table:not(.times-table):not(.no-card)").forEach(table => {
      const headers = [...table.querySelectorAll("thead th")].map(th => th.textContent.trim());
      if (!headers.length) return;
      table.querySelectorAll("tbody td").forEach((td, i) => {
        const label = headers[i % headers.length];
        if (label) td.setAttribute("data-label", label);
      });
    });
  }

  // ── 루프34: 테이블 스크롤 마스크 (.scrolled-end 토글) + 힌트 주입 ──
  function initTableScrollMask() {
    const wraps = [...document.querySelectorAll(".table-wrap")];
    const checkEnd = w => w.classList.toggle("scrolled-end", w.scrollLeft + w.clientWidth >= w.scrollWidth - 2);
    wraps.forEach(w => {
      checkEnd(w);
      w.addEventListener("scroll", () => checkEnd(w), { passive: true });
      // .times-table / .no-card 앞에 스크롤 힌트 삽입
      const hasBigTable = w.querySelector("table.times-table, table.no-card");
      const alreadyHasHint = w.previousElementSibling?.classList.contains("table-scroll-hint");
      if (hasBigTable && !alreadyHasHint) {
        const hint = document.createElement("span");
        hint.className = "table-scroll-hint";
        hint.textContent = "좌우로 스크롤해 전체 보기";
        w.parentNode.insertBefore(hint, w);
      }
    });
    window.addEventListener("resize", () => wraps.forEach(checkEnd), { passive: true });
  }

  document.addEventListener("DOMContentLoaded", () => {
    addNavScrolled();
    initCurriculumBadgeTips();
    initTocHighlight();
    initTableScope();
    initTableCards();
    initTableScrollMask();
    addProgressBar();
    addBackToTop();
    injectBreadcrumbJsonLd();
    if (page.type === "global-home") enhanceGlobalHome();
    if (page.type === "language-home") enhanceLanguageHome();
    if (page.type === "section-index") enhanceSectionIndex();
    if (page.type === "article") enhanceArticle();
    if (page.type === "404") enhance404();
  });
})();
