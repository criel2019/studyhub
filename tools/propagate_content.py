import glob, os

content_en = {
    ('math', 'algebra'): (
        'Algebra is the language of mathematics. It lets you solve problems with unknowns. From calculating interest rates to engineering design, algebra is everywhere in modern technology and everyday decisions.',
        'Think of algebra as a <strong>balance scale</strong>. The equals sign (=) means both sides must always balance. Whatever you do to one side, you must do to the other. This is why moving a term across the equals sign changes its sign.',
        'Moving a term across the equals sign just reverses its sign.',
        'This happens because you subtract the same value from both sides to maintain balance. x + 3 = 7 means x = 7 minus 3. <strong>Understanding the reason means you will never forget the rule.</strong>'
    ),
    ('math', 'geometry'): (
        'Geometry is the mathematics of space and shape, used in architecture, GPS navigation, and computer graphics.',
        'Geometry is the <strong>language of space</strong>. Before memorizing formulas, draw the shape and ask: why does this relationship hold? The interior angles of a triangle sum to 180 degrees because sliding the three angles together forms a straight line. Picture first, formula second.',
        None, None
    ),
    ('math', 'statistics'): (
        'Statistics is how we make sense of data in an uncertain world, from medical research to election polling. Understanding statistics helps you critically evaluate claims.',
        'Statistics is the art of <strong>finding truth in data</strong>. But numbers mislead easily: one billionaire joining a group of average workers makes the mean salary enormous, but the median barely changes. <em>The average is easily skewed by outliers.</em>',
        'The mean (average) is always the best measure of center.',
        'When data has outliers, the median is more representative. <strong>Always ask: which measure best represents this data?</strong>'
    ),
    ('science', 'atoms'): (
        None,
        'An atom is like a <strong>miniature solar system</strong> with the nucleus at the center and electrons orbiting around it. Here is the mind-blowing part: 99.9999 percent of an atom is empty space! Matter feels solid because of electromagnetic repulsion between electrons, not because atoms are packed tightly.',
        None, None
    ),
    ('science', 'biology'): (
        None,
        'All life processes are <strong>energy conversion chains</strong>. ATP (adenosine triphosphate) is the cell\'s energy currency. Food (glucose) gets converted to ATP, and when ATP breaks down, that energy powers muscle contraction, protein synthesis, and nerve signals.',
        None, None
    ),
    ('science', 'cells'): (
        None,
        'Think of a cell as a <strong>miniature city</strong>: nucleus = city hall (stores DNA), mitochondria = power plants (produce ATP), ribosomes = factories (build proteins), Golgi apparatus = post office (sorts and ships materials), cell membrane = city walls (controls entry and exit).',
        None, None
    ),
    ('science', 'chemistry'): (
        None,
        'Chemistry is <strong>the game of rearranging atoms</strong>. In any chemical reaction, atoms do not appear or disappear, they just bond differently (conservation of mass). When you read a chemical formula, ask: which atoms, and how many of each, are bonded together?',
        None, None
    ),
    ('science', 'earth'): (
        None,
        'Earth is a <strong>system of four interacting spheres</strong>: geosphere (rocks), hydrosphere (water), atmosphere (air), biosphere (living things). A volcanic eruption triggers a chain: sulfur dioxide enters the atmosphere, causes acid rain, which damages forests. Earth science is about understanding these <em>interaction patterns</em>.',
        None, None
    ),
    ('science', 'ecology'): (
        None,
        'An ecosystem is an <strong>energy flow network</strong>. Solar energy flows: plants (producers) to herbivores to carnivores. But about 90 percent of energy is lost as heat at each step. This is why there must be far more plants than herbivores. <em>The shape of the food pyramid is inevitable, driven by energy loss.</em>',
        None, None
    ),
    ('science', 'energy'): (
        None,
        'Energy <strong>never disappears, it only changes form</strong>. When a ball falls: potential energy becomes kinetic energy, then heat and sound. Saying electricity is consumed is technically wrong; it is converted into light, heat, or motion. The universe total energy stays constant.',
        None, None
    ),
    ('science', 'physics'): (
        None,
        None,
        'Without force, objects stop moving.',
        'Galileo and Newton showed that without force, objects maintain their current state. A stationary object stays still; a moving object keeps moving at constant speed in a straight line (inertia). Objects stop on Earth because <strong>friction is a force acting on them.</strong>'
    ),
    ('english', 'literature'): (
        'Literature is a window into human experience across cultures and time. Analyzing literature sharpens critical thinking, empathy, and communication skills essential in every career.',
        'Reading literature is like <strong>solving a mystery</strong>: the author leaves clues (symbols, word choices, structure) pointing to deeper meanings. Before asking what happened, ask why the author wrote it this way.',
        None, None
    ),
    ('english', 'reading'): (
        None,
        'English reading is the <strong>art of intelligent guessing</strong>. You do not need to know every word. Use context, sentence structure, and word roots to infer meaning. Scan the questions before reading the passage.',
        None, None
    ),
    ('english', 'vocabulary'): (
        None,
        'Vocabulary learning is <strong>not about memorizing isolated words</strong>. Knowing 50 word roots unlocks thousands of words you have never seen. Example: pre + dict + ion means prediction. <em>Pattern recognition scales infinitely better than rote memorization.</em>',
        None, None
    ),
    ('english', 'writing'): (
        None,
        'English and Korean think in opposite orders. Korean puts the verb at the end; English puts the verb right after the subject. When writing in English, <strong>say what you are doing first</strong>, then add where and when. This shift in thinking is the key to natural English writing.',
        'English writing is just translating from Korean.',
        'Direct translation produces awkward English. English centers the verb and keeps sentences concise. <strong>Think in English structure from the start.</strong>'
    ),
    ('english', 'grammar'): (
        None,
        'English grammar is the <strong>traffic rules of the language</strong>. Especially tense and modal verbs (can/could/would/should) are not just rules to memorize but signals about timing, certainty, and relationship that change the meaning entirely.',
        None, None
    ),
}

content_ja = {
    ('math', 'algebra'): (
        '代数は数学の言語です。未知の量で問題を解く力を与えてくれます。金利計算からエンジニアリングまで、代数は現代社会のあらゆる場面で活躍しています。',
        '代数は<strong>天秤ばかり</strong>と同じです。等号(=)の両側は常にバランスが取れていなければなりません。一方の側に操作をしたら、必ず反対側にも同じ操作をします。これが移項すると符号が変わる理由です。',
        '移項すると符号が変わる。これは規則だから覚える。',
        '移項は両辺から同じ値を引くことです。x + 3 = 7で3を移項すると両辺から3を引いてx = 7 - 3になります。<strong>原理を理解すれば絶対に忘れません。</strong>'
    ),
    ('math', 'geometry'): (
        '幾何学は空間と形の数学です。建築、GPS、コンピューターグラフィックスなど多くの分野で使われています。',
        '幾何学は<strong>空間の言語</strong>です。公式を覚える前に図を描き、なぜその関係が成り立つかを確認してください。三角形の内角の和が180度なのは、三つの頂点の角を一直線上に並べると直線になるからです。',
        None, None
    ),
    ('math', 'statistics'): (
        '統計学は不確かな世界でデータから真実を見つける方法です。医学研究や選挙予測など、日常的な意思決定に欠かせません。',
        '統計は<strong>データで真実を探す技術</strong>です。ただし平均は外れ値の影響を強く受けます。中央値の方が実態をより正確に反映することがよくあります。',
        '平均は常に最良の代表値だ。',
        '外れ値があると平均は歪みます。<strong>データに合った代表値を選んでください。</strong>'
    ),
    ('science', 'atoms'): (
        None,
        '原子は<strong>ミニチュア太陽系</strong>のようなものです。原子核が中心に、電子が周りを回っています。原子の99.9999%は空っぽです。物質が固く感じる理由は電子間の電磁気的反発力のためです。',
        None, None
    ),
    ('science', 'biology'): (
        None,
        'すべての生命活動は<strong>エネルギー変換の連続</strong>です。ATP(アデノシン三リン酸)は細胞のエネルギー通貨で、食物がATPに変換され、そのエネルギーで筋肉収縮やタンパク質合成が行われます。',
        None, None
    ),
    ('science', 'cells'): (
        None,
        '細胞は<strong>ミニチュア都市</strong>です。細胞核=市役所(DNA保管)、ミトコンドリア=発電所(ATP生産)、リボソーム=工場(タンパク質合成)、ゴルジ体=物流倉庫、細胞膜=城壁(出入り管理)。',
        None, None
    ),
    ('science', 'chemistry'): (
        None,
        '化学は<strong>原子の組み替えゲーム</strong>です。化学反応で原子は生まれたり消えたりせず、結合の仕方が変わるだけです(質量保存の法則)。',
        None, None
    ),
    ('science', 'earth'): (
        None,
        '地球は<strong>4つの圏域が絶えず相互作用するシステム</strong>です。岩石圏・水圏・大気圏・生物圏が連鎖して影響し合います。地球科学はこの相互作用パターンを理解する学問です。',
        None, None
    ),
    ('science', 'ecology'): (
        None,
        '生態系は<strong>エネルギーが流れる網目</strong>です。太陽エネルギーから植物・草食動物・肉食動物へと伝わりますが、各段階で約90%のエネルギーが熱として失われます。',
        None, None
    ),
    ('science', 'energy'): (
        None,
        'エネルギーは<strong>絶対に消えません</strong>。形が変わるだけです。電気が消費されるという表現は正確ではなく、光・熱・運動エネルギーに変換されています(エネルギー保存の法則)。',
        None, None
    ),
    ('science', 'physics'): (
        None,
        None,
        '力がなければ物体は止まる。',
        'ニュートンの第一法則(慣性の法則)：力がなければ物体は現在の状態を維持します。地球上で物体が止まるのは摩擦力という<strong>力</strong>が作用しているためです。'
    ),
    ('english', 'writing'): (
        None,
        '日本語と英語では語順が逆です。日本語は動詞が最後ですが、英語は動詞が主語の直後に来ます。英語で書くときは<strong>「何をするか」を最初に言い</strong>、時間・場所は後から添えます。',
        None, None
    ),
    ('english', 'grammar'): (
        None,
        '英語の文法は<strong>言語の交通ルール</strong>です。時制と助動詞(can/could/would/should)はニュアンスの違いを理解することが重要です。',
        None, None
    ),
    ('english', 'reading'): (
        None,
        '英語の読解は<strong>推測の技術</strong>です。知らない単語が出てきても、文脈・文構造・語根から意味を推測できます。設問を先に確認する習慣が重要です。',
        None, None
    ),
    ('english', 'vocabulary'): (
        None,
        '英単語の暗記は孤立した単語を覚えることではありません。語根(root)と接辞(prefix・suffix)のパターンを知れば、初めて見る単語の意味を推測できます。<em>パターン認識は丸暗記より何倍も効率的です。</em>',
        None, None
    ),
    ('japanese', 'grammar'): (
        None,
        '日本語文法は<strong>言語の設計図</strong>です。助詞・活用・敬語の仕組みを理解すれば、初めて見る文章でも構造を分析できます。',
        None, None
    ),
    ('japanese', 'reading'): (
        None,
        '読解は<strong>単語から文・文から段落・段落から全体</strong>へと積み上げる階層的な過程です。各段落の要旨を一文で掴む練習が効果的です。',
        None, None
    ),
    ('japanese', 'vocabulary'): (
        None,
        '語彙は<strong>文脈の中で</strong>覚えることが最も効果的です。また、漢字の訓読み・音読みのパターンを知ると語彙が飛躍的に増えます。',
        None, None
    ),
    ('japanese', 'writing'): (
        None,
        '良い文章は<strong>主張1つ+根拠2〜3つ+具体例+結論</strong>の構造から生まれます。一つの段落に一つの考えだけを入れることが読みやすい文章の鉄則です。',
        None, None
    ),
    ('japanese', 'modern'): (
        None,
        '現代文は<strong>筆者の主張と根拠を追跡するゲーム</strong>です。接続詞(しかし・つまり・だから)に注目することで段落の論理構造が見えてきます。',
        None, None
    ),
    ('japanese', 'classical'): (
        None,
        '古典文学の文法は現代語と異なりますが、<strong>助動詞の意味と接続</strong>を理解すれば文章の骨格を掴めます。暗記より構造理解が先です。',
        None, None
    ),
}

content_zh = {
    ('math', 'algebra'): (
        '代数是数学的语言，让我们能够处理未知量。从计算利率到工程设计，代数无处不在。',
        '代数就像一杆<strong>天平秤</strong>。等号两边必须始终保持平衡。对一边做任何操作，必须对另一边做相同操作。这就是为什么移项时符号会改变。',
        '移项就是把符号变一下，记住规则就好。',
        '移项是因为两边同时减去同一个数。x + 3 = 7，两边减3得x = 7 - 3。<strong>理解原理，就不会忘记规则。</strong>'
    ),
    ('math', 'geometry'): (
        '几何学是空间和形状的数学，用于建筑、导航、计算机图形学等各个领域。',
        '几何是<strong>空间的语言</strong>。记公式前先画图，问问自己为什么这个关系成立。三角形内角和为180度，是因为三个顶点的角拼在一起恰好形成一条直线。先图形，后公式。',
        None, None
    ),
    ('math', 'statistics'): (
        '统计学帮助我们从数据中找到真相，从医学研究到选举预测都离不开统计。',
        '统计是<strong>从数据中寻找真相的过程</strong>。平均值受极端值影响很大，中位数往往更能反映真实情况。<em>不要只看平均值。</em>',
        '平均值总是最好的代表值。',
        '当数据有极端值时，中位数更具代表性。<strong>根据数据特征选择合适的统计量。</strong>'
    ),
    ('science', 'atoms'): (
        None,
        '原子就像<strong>迷你太阳系</strong>，原子核在中心，电子绕核运动。令人惊讶的是原子99.9999%都是空的。物质感觉坚固是因为电子之间的电磁斥力。',
        None, None
    ),
    ('science', 'biology'): (
        None,
        '所有生命活动都是<strong>能量转换的连续过程</strong>。ATP是细胞的能量货币，食物(葡萄糖)转化为ATP，ATP分解时释放的能量驱动各种生命活动。',
        None, None
    ),
    ('science', 'cells'): (
        None,
        '细胞是一座<strong>微型城市</strong>：细胞核=市政厅(保存DNA)，线粒体=发电厂(产生ATP)，核糖体=工厂(合成蛋白质)，高尔基体=物流中心，细胞膜=城墙(控制进出)。',
        None, None
    ),
    ('science', 'chemistry'): (
        None,
        '化学是<strong>原子重新排列的游戏</strong>。化学反应中原子不会凭空产生或消失，只是结合方式改变(质量守恒定律)。看化学式时先问：哪些原子各有几个是怎么结合的？',
        None, None
    ),
    ('science', 'earth'): (
        None,
        '地球是<strong>四个圈层不断相互作用的系统</strong>：岩石圈、水圈、大气圈、生物圈相互影响。地球科学就是理解这些相互作用模式。',
        None, None
    ),
    ('science', 'ecology'): (
        None,
        '生态系统是一个<strong>能量流动的网络</strong>。每个营养级约90%的能量以热的形式散失，这就是为什么植物数量必须远多于动物。',
        None, None
    ),
    ('science', 'energy'): (
        None,
        '能量<strong>永远不会消失</strong>，只是改变形式(能量守恒定律)。说电能被消耗是不准确的，准确说法是转化为光能、热能或机械能。',
        None, None
    ),
    ('science', 'physics'): (
        None,
        None,
        '没有力，物体就会停止运动。',
        '伽利略和牛顿发现：没有力，物体保持当前状态。地球上物体停下来是因为摩擦力(一种力)在起作用。'
    ),
    ('english', 'writing'): (
        None,
        '中文和英文的思维顺序相反。中文动词在最后，英文动词紧跟主语。用英文写作时<strong>先说做什么，再补充在哪里和什么时候</strong>。',
        None, None
    ),
    ('english', 'grammar'): (
        None,
        '英语语法是<strong>语言的交通规则</strong>。时态和情态动词(can/could/would/should)不是死记硬背的规则，而是表达时间、确定性和关系的信号。',
        None, None
    ),
    ('english', 'reading'): (
        None,
        '英语阅读是<strong>智慧猜测的技艺</strong>。遇到不认识的单词可以通过上下文和词根推断含义。阅读前先看题目，提高阅读效率。',
        None, None
    ),
    ('english', 'vocabulary'): (
        None,
        '学英语词汇不是孤立地死记硬背。掌握词根和词缀规律，就能推断大多数陌生单词的含义。<em>模式识别比死记硬背效率高出几倍。</em>',
        None, None
    ),
    ('chinese', 'grammar'): (
        None,
        '语法是<strong>语言的设计图</strong>。理解词类和句子成分的规律，就能分析任何陌生的句子结构。',
        None, None
    ),
    ('chinese', 'reading'): (
        None,
        '阅读理解是<strong>从词到句、从句到段落、从段落到全文</strong>的层次性理解过程。把握每段的核心句，就能快速理解全文。',
        None, None
    ),
    ('chinese', 'vocabulary'): (
        None,
        '词汇学习<strong>在语境中最有效</strong>。了解汉字偏旁部首的含义，可以推断大量陌生词的意思。',
        None, None
    ),
    ('chinese', 'writing'): (
        None,
        '好文章来自<strong>一个主旨+2-3个论据+具体例子+结论</strong>的清晰结构。每段只表达一个中心思想。',
        None, None
    ),
    ('chinese', 'modern'): (
        None,
        '现代文阅读是<strong>追踪作者观点和论据的过程</strong>。注意接续词(但是、因此、总之)就能看清段落的逻辑结构。',
        None, None
    ),
    ('chinese', 'classical'): (
        None,
        '古汉语文法与现代汉语不同，但理解<strong>虚词用法和句式特点</strong>，就能读懂大多数古文。理解结构比死记硬背重要。',
        None, None
    ),
}

all_content = {'en': content_en, 'ja': content_ja, 'zh': content_zh}
base = 'F:/work/studyhub/'
total_updated = 0

for lang, content_db in all_content.items():
    files = glob.glob(base + lang + '/**/*.html', recursive=True)
    for f in sorted(files):
        if 'index' in f:
            continue
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()

        why = c.count('why-box')
        intuit = c.count('intuition-box')
        misc = c.count('misconception')

        if why > 0 and intuit > 0:
            continue

        subdir = os.path.basename(os.path.dirname(f))
        fname_stem = os.path.splitext(os.path.basename(f))[0]
        key = (subdir, fname_stem)

        if key not in content_db:
            continue

        data = content_db[key]
        why_text, intuit_text, misc_ohaeseo, misc_jinsil = data

        if why > 0:
            why_idx = c.find('class="why-box"')
            insert_pos = c.find('</div>', why_idx) + 6
        else:
            meta_idx = c.find('article-meta')
            if meta_idx != -1:
                insert_pos = c.find('</div>', meta_idx) + 6
            else:
                insert_pos = c.find('<h2')

        inserts = ''

        if why == 0 and why_text:
            if lang == 'en':
                label = 'Why study this?'
            elif lang == 'ja':
                label = 'なぜ学ぶの？'
            else:
                label = '为什么要学？'
            inserts += (
                '\n\n    <div class="why-box">'
                '<div class="why-label">' + label + '</div>'
                '<p>' + why_text + '</p></div>'
            )

        if intuit == 0 and intuit_text:
            if lang == 'en':
                label = 'Think of it intuitively'
            elif lang == 'ja':
                label = '直感的に理解しよう'
            else:
                label = '直觉理解'
            inserts += (
                '\n\n    <div class="intuition-box">'
                '<span class="intuition-box-label">' + label + '</span>'
                '<p>' + intuit_text + '</p></div>'
            )

        if misc == 0 and misc_ohaeseo and misc_jinsil:
            if lang == 'en':
                misc_label = 'Common Misconception'
                m_prefix = 'Common mistake:'
                t_prefix = 'Reality:'
            elif lang == 'ja':
                misc_label = 'よくある誤解'
                m_prefix = 'よくある誤解：'
                t_prefix = '真実：'
            else:
                misc_label = '常见误解'
                m_prefix = '误解：'
                t_prefix = '事实：'
            inserts += (
                '\n\n    <div class="misconception">'
                '<div class="misconception-label">' + misc_label + '</div>'
                '<p><strong>' + m_prefix + '</strong> ' + misc_ohaeseo + '</p>'
                '<p><strong>' + t_prefix + '</strong> ' + misc_jinsil + '</p></div>'
            )

        if inserts:
            c = c[:insert_pos] + inserts + c[insert_pos:]
            with open(f, 'w', encoding='utf-8') as fp:
                fp.write(c)
            total_updated += 1

print('Total files updated:', total_updated)
