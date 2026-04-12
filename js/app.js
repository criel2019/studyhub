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
      shareText: "Check out this free study guide! 📚",
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
      shareText: "무료 학습 자료 발견! 📚",
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
      shareText: "無料学習ノートを見つけました！📚",
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
      shareText: "发现免费学习笔记！📚",
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

  function enhanceLanguageHome() {
    enhanceHero();
    markFirstCard(".subject-grid .subject-card");
  }

  function enhanceSectionIndex() {
    markFirstCard(".topic-grid .topic-card");

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

  function enhance404() {
    const main = document.querySelector("main");
    if (!main || main.querySelector(".empty-state-note")) return;
    const note = el("p", "empty-state-note", t.notFound);
    main.appendChild(note);
  }

  document.addEventListener("DOMContentLoaded", () => {
    addProgressBar();
    addBackToTop();
    if (page.type === "global-home") enhanceGlobalHome();
    if (page.type === "language-home") enhanceLanguageHome();
    if (page.type === "section-index") enhanceSectionIndex();
    if (page.type === "article") enhanceArticle();
    if (page.type === "404") enhance404();
  });
})();
