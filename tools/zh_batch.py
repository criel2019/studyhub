import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

zh_pages = [
    {
        'path': 'zh/science/atoms.html',
        'old_bc': '<span>原子与分子</span>',
        'new_bc': '<span class="breadcrumb-current">原子与分子</span>',
        'meta_end': '      <span>🎯 核心概念：原子结构·元素符号·离子·化学式</span>\n    </div>',
        'first_h2': '    <h2>1. 原子的结构</h2>',
        'new_first_h2': '    <h2 id="s1">1. 原子的结构</h2>',
        'insert': """
    <div class="learning-goal">
      <span class="learning-goal-label">📌 学完本单元，你将能够</span>
      <ul>
        <li>用质子·中子·电子的位置和作用说明原子结构</li>
        <li>看到10个以上的元素符号，说出元素名称和原子序数</li>
        <li>用电子转移解释离子的形成，并写出离子式</li>
        <li>读懂化学式，判断元素的种类和数目</li>
      </ul>
    </div>

    <div class="why-box">
      <div class="why-label">🌱 为什么要学原子与分子？</div>
      <p>原子是<strong>构成物质的最小单位</strong>。食盐为何有咸味、水为何是H₂O、电池如何储电——所有化学现象的解释都从原子、离子和分子层面开始。半导体、新药、电池、合成材料等现代产业都建立在对原子级物质的理解之上。</p>
    </div>

    <div class="tldr">
      <div class="tldr-label">⚡ 30秒核心摘要</div>
      <ul>
        <li><strong>原子结构</strong>：核（质子+中子）+电子。原子序数＝质子数＝电子数</li>
        <li><strong>质量数</strong>＝质子数+中子数。同位素：质量数不同，原子序数相同</li>
        <li><strong>离子</strong>：失去电子→阳离子(+)，得到电子→阴离子(−)</li>
        <li><strong>分子</strong>：通过共价键形成的中性粒子，用化学式表示</li>
        <li><strong>元素周期表</strong>：按原子序数排列，同族元素化学性质相似</li>
      </ul>
    </div>
""",
        'h2_map': [
            ('<h2>2. 元素符号与元素周期表</h2>', '<h2 id="s2">2. 元素符号与元素周期表</h2>'),
            ('<h2>3. 离子(Ion)</h2>', '<h2 id="s3">3. 离子(Ion)</h2>'),
            ('<h2>4. 分子与化学式</h2>', '<h2 id="s4">4. 分子与化学式</h2>'),
            ('<h2>练习题</h2>', '<h2 id="s5">练习题</h2>'),
        ]
    },
    {
        'path': 'zh/science/cells.html',
        'old_bc': '<span>细胞</span>',
        'new_bc': '<span class="breadcrumb-current">细胞</span>',
        'meta_end': '      <span>🎯 核心概念：细胞结构·细胞器·有丝分裂·减数分裂</span>\n    </div>',
        'first_h2': '    <h2>1. 细胞的基本结构</h2>',
        'new_first_h2': '    <h2 id="s1">1. 细胞的基本结构</h2>',
        'insert': """
    <div class="learning-goal">
      <span class="learning-goal-label">📌 学完本单元，你将能够</span>
      <ul>
        <li>说明7种主要细胞器的名称和功能</li>
        <li>用表格比较动物细胞和植物细胞的区别</li>
        <li>按顺序说明有丝分裂的前中后末期</li>
        <li>比较有丝分裂与减数分裂的目的和结果</li>
      </ul>
    </div>

    <div class="why-box">
      <div class="why-label">🌱 为什么要学细胞？</div>
      <p>细胞是<strong>生命的基本单位</strong>。人体约有37万亿个细胞，癌症就是细胞分裂失控的结果。了解细胞，就是了解疾病的成因和治疗原理。生物学·医学·药学的所有领域都从细胞层面出发。</p>
    </div>

    <div class="tldr">
      <div class="tldr-label">⚡ 30秒核心摘要</div>
      <ul>
        <li><strong>细胞膜</strong>：选择透过性。<strong>细胞核</strong>：DNA储存·调控。<strong>线粒体</strong>：ATP产生</li>
        <li><strong>核糖体</strong>：蛋白质合成。<strong>高尔基体</strong>：加工·分泌。<strong>内质网</strong>：物质运输</li>
        <li><strong>植物专有</strong>：细胞壁（纤维素）+ 叶绿体（光合作用）+ 大液泡</li>
        <li><strong>动物专有</strong>：溶酶体（消化）+ 中心体（分裂方向）</li>
        <li><strong>有丝分裂</strong>：1→2个（相同）。<strong>减数分裂</strong>：1→4个（染色体减半）</li>
      </ul>
    </div>
""",
        'h2_map': [
            ('<h2>2. 动物细胞 vs 植物细胞</h2>', '<h2 id="s2">2. 动物细胞 vs 植物细胞</h2>'),
            ('<h2>3. 细胞分裂</h2>', '<h2 id="s3">3. 细胞分裂</h2>'),
            ('<h2>练习题</h2>', '<h2 id="s4">练习题</h2>'),
        ]
    },
    {
        'path': 'zh/science/ecology.html',
        'old_bc': '<span>生态系统</span>',
        'new_bc': '<span class="breadcrumb-current">生态系统</span>',
        'meta_end': '      <span>🎯 核心概念：食物链·能量流动·物质循环·生物多样性</span>\n    </div>',
        'first_h2': '    <h2>1. 生态系统的组成</h2>',
        'new_first_h2': '    <h2 id="s1">1. 生态系统的组成</h2>',
        'insert': """
    <div class="learning-goal">
      <span class="learning-goal-label">📌 学完本单元，你将能够</span>
      <ul>
        <li>说明生产者·消费者·分解者的作用和相互关系</li>
        <li>预测食物网中某生物消失后的连锁影响</li>
        <li>用能量效率（10%法则）解释越往高营养级能量越少的原因</li>
        <li>将碳循环·氮循环过程与生态系统组成要素联系起来说明</li>
      </ul>
    </div>

    <div class="why-box">
      <div class="why-label">🌱 为什么要学生态系统？</div>
      <p>生态系统是<strong>生物与环境相互作用的巨大系统</strong>。蜜蜂消失为何会引发粮食危机？森林砍伐为何会改变气候？这都是因为生态系统中的一切都相互关联。气候变化·生物多样性危机·可持续发展——当今最重要的环境问题都从生态系统理解出发。</p>
    </div>

    <div class="tldr">
      <div class="tldr-label">⚡ 30秒核心摘要</div>
      <ul>
        <li><strong>生态系统组成</strong>：生产者（植物）→ 初级消费者 → 次级消费者 → 分解者</li>
        <li><strong>能量流动</strong>：单向流动。向上一营养级只传递约10%的能量</li>
        <li><strong>碳循环</strong>：CO₂ ↔ 光合作用·呼吸 ↔ 有机物 ↔ 燃烧·分解</li>
        <li><strong>氮循环</strong>：N₂ → 固氮 → 铵盐 → 亚硝酸盐 → 硝酸盐 → 生物体</li>
        <li><strong>生物多样性</strong>：遗传·物种·生态系统多样性。减少原因：栖息地破坏·入侵物种·污染</li>
      </ul>
    </div>
""",
        'h2_map': [
            ('<h2>2. 食物链与食物网</h2>', '<h2 id="s2">2. 食物链与食物网</h2>'),
            ('<h2>3. 能量流动</h2>', '<h2 id="s3">3. 能量流动</h2>'),
            ('<h2>4. 物质循环</h2>', '<h2 id="s4">4. 物质循环</h2>'),
            ('<h2>5. 生物多样性</h2>', '<h2 id="s5">5. 生物多样性</h2>'),
            ('<h2>练习题</h2>', '<h2 id="s6">练习题</h2>'),
        ]
    },
    {
        'path': 'zh/science/energy.html',
        'old_bc': '<span>能量</span>',
        'new_bc': '<span class="breadcrumb-current">能量</span>',
        'meta_end': '      <span>🎯 核心概念：动能·势能·守恒定律·热力学</span>\n    </div>',
        'first_h2': '    <h2>1. 什么是能量</h2>',
        'new_first_h2': '    <h2 id="s1">1. 什么是能量</h2>',
        'insert': """
    <div class="learning-goal">
      <span class="learning-goal-label">📌 学完本单元，你将能够</span>
      <ul>
        <li>区分5种以上的能量形式并举出实生活例子</li>
        <li>用过山车或摆为例说明能量守恒定律</li>
        <li>用自然语言描述热力学第一和第二定律，理解效率极限</li>
        <li>简要说明太阳能·风能·氢能的工作原理</li>
      </ul>
    </div>

    <div class="why-box">
      <div class="why-label">🌱 为什么要学能量？</div>
      <p>能量是<strong>引发所有变化的能力</strong>。我们吃的食物、行驶的汽车、点亮的灯泡——都是能量的形式转换。能量守恒定律是贯穿物理·化学·生物的最根本法则之一，在气候变化时代，理解可再生能源已成为必备素养。</p>
    </div>

    <div class="tldr">
      <div class="tldr-label">⚡ 30秒核心摘要</div>
      <ul>
        <li><strong>能量形式</strong>：动能·势能·热能·化学能·电能·光能·核能</li>
        <li><strong>能量守恒</strong>：形式改变但总量不变（热力学第一定律）</li>
        <li><strong>第二定律</strong>：能量总从有用→较无用（热量）方向流动，100%效率不可能</li>
        <li><strong>功＝力×距离</strong>（J）。<strong>功率＝功÷时间</strong>（W）</li>
        <li><strong>可再生能源</strong>：太阳能（光电效应）、风能（动能→电能）、氢能（燃料电池）</li>
      </ul>
    </div>
""",
        'h2_map': [
            ('<h2>2. 能量的转化</h2>', '<h2 id="s2">2. 能量的转化</h2>'),
            ('<h2>3. 能量守恒定律</h2>', '<h2 id="s3">3. 能量守恒定律</h2>'),
            ('<h2>4. 热力学定律</h2>', '<h2 id="s4">4. 热力学定律</h2>'),
            ('<h2>5. 可再生能源与不可再生能源</h2>', '<h2 id="s5">5. 可再生能源与不可再生能源</h2>'),
            ('<h2>练习题</h2>', '<h2 id="s6">练习题</h2>'),
        ]
    },
    {
        'path': 'zh/science/earth.html',
        'old_bc': '<span>地球科学</span>',
        'new_bc': '<span class="breadcrumb-current">地球科学</span>',
        'meta_end': '      <span>🎯 核心概念：地球结构·板块构造·岩石循环·大气·太阳系</span>\n    </div>',
        'first_h2': '    <h2>1. 地球内部结构</h2>',
        'new_first_h2': '    <h2 id="s1">1. 地球内部结构</h2>',
        'insert': """
    <div class="learning-goal">
      <span class="learning-goal-label">📌 学完本单元，你将能够</span>
      <ul>
        <li>说明地球内部4层结构（地壳·地幔·外核·内核）的特性</li>
        <li>用板块构造理论解释地震·火山·山脉的分布</li>
        <li>用图示说明岩石的3种类型及循环过程</li>
        <li>说明气压·锋面·天气变化的相互关系</li>
      </ul>
    </div>

    <div class="why-box">
      <div class="why-label">🌱 为什么要学地球科学？</div>
      <p>地球科学是<strong>理解我们所居住星球的学科</strong>。地震为何发生、如何防灾？气候变化为何严峻？板块构造理论是20世纪最重大的科学革命之一，气象学是现代气候变化政策的基础。学习地球科学，能让你看懂自然灾害·气候·宇宙相互连接的地球系统。</p>
    </div>

    <div class="tldr">
      <div class="tldr-label">⚡ 30秒核心摘要</div>
      <ul>
        <li><strong>地球内部</strong>：地壳（最薄）→ 地幔（最厚）→ 外核（液态·磁场来源）→ 内核（固态）</li>
        <li><strong>板块构造</strong>：地壳分为多个板块，边界处发生地震·火山·造山运动</li>
        <li><strong>岩石循环</strong>：火成岩（岩浆冷却）→ 沉积岩（压实）→ 变质岩（热·压）</li>
        <li><strong>天气</strong>：高气压＝晴天，低气压＝阴天。锋面过境时天气骤变</li>
        <li><strong>太阳系</strong>：水金地火木土天海，小行星带在火星与木星之间</li>
      </ul>
    </div>
""",
        'h2_map': [
            ('<h2>2. 板块构造理论</h2>', '<h2 id="s2">2. 板块构造理论</h2>'),
            ('<h2>3. 岩石的种类与循环</h2>', '<h2 id="s3">3. 岩石的种类与循环</h2>'),
            ('<h2>4. 大气层结构</h2>', '<h2 id="s4">4. 大气层结构</h2>'),
            ('<h2>5. 太阳系</h2>', '<h2 id="s5">5. 太阳系</h2>'),
            ('<h2>练习题</h2>', '<h2 id="s6">练习题</h2>'),
        ]
    },
    {
        'path': 'zh/science/biology.html',
        'old_bc': '<span>生物</span>',
        'new_bc': '<span class="breadcrumb-current">生物</span>',
        'meta_end': '      <span>🎯 重要概念：细胞、光合作用、遗传、进化</span>\n    </div>',
        'first_h2': '    <h2>1. 细胞生物学</h2>',
        'new_first_h2': '    <h2 id="s1">1. 细胞生物学</h2>',
        'insert': """
    <div class="learning-goal">
      <span class="learning-goal-label">📌 学完本单元，你将能够</span>
      <ul>
        <li>用具体例子说明生命体的7个共同特性</li>
        <li>写出光合作用和细胞呼吸的反应式并进行比较</li>
        <li>用孟德尔定律计算遗传性状的遗传比例</li>
        <li>基于自然选择说解释进化过程</li>
      </ul>
    </div>

    <div class="why-box">
      <div class="why-label">🌱 为什么要学生物？</div>
      <p>生物学是<strong>理解生命运作原理的学科</strong>。为什么人必须睡觉？癌细胞如何增殖？了解光合作用，就能看懂粮食问题与碳中和。现代医学·农业·环境科学的核心都是生物学。</p>
    </div>

    <div class="tldr">
      <div class="tldr-label">⚡ 30秒核心摘要</div>
      <ul>
        <li><strong>生命特性</strong>：细胞构成·物质代谢·刺激反应·生长·生殖·遗传·进化</li>
        <li><strong>光合作用</strong>：6CO₂ + 6H₂O + 光能 → C₆H₁₂O₆ + 6O₂（叶绿体）</li>
        <li><strong>细胞呼吸</strong>：C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP（线粒体）</li>
        <li><strong>孟德尔定律</strong>：显隐性·分离定律·自由组合定律。Rr × Rr ＝ 3:1</li>
        <li><strong>进化</strong>：变异 + 自然选择 → 适应 → 物种形成（达尔文自然选择说）</li>
      </ul>
    </div>
""",
        'h2_map': [
            ('<h2>2. 光合作用与细胞呼吸</h2>', '<h2 id="s2">2. 光合作用与细胞呼吸</h2>'),
            ('<h2>3. DNA、基因与蛋白质合成</h2>', '<h2 id="s3">3. DNA、基因与蛋白质合成</h2>'),
            ('<h2>4. 孟德尔遗传定律</h2>', '<h2 id="s4">4. 孟德尔遗传定律</h2>'),
            ('<h2>5. 进化与自然选择</h2>', '<h2 id="s5">5. 进化与自然选择</h2>'),
        ]
    },
    {
        'path': 'zh/science/chemistry.html',
        'old_bc': '<span>化学</span>',
        'new_bc': '<span class="breadcrumb-current">化学</span>',
        'meta_end': '      <span>🎯 重要概念：原子结构、周期表、化学反应、酸碱盐</span>\n    </div>',
        'first_h2': '    <h2>1. 原子结构</h2>',
        'new_first_h2': '    <h2 id="s1">1. 原子结构</h2>',
        'insert': """
    <div class="learning-goal">
      <span class="learning-goal-label">📌 学完本单元，你将能够</span>
      <ul>
        <li>区分纯净物·混合物·单质·化合物，并举出实例</li>
        <li>解释共价键和离子键的形成原理与区别</li>
        <li>说明酸碱的定义和pH的概念</li>
        <li>用化合价的概念判断氧化还原反应</li>
      </ul>
    </div>

    <div class="why-box">
      <div class="why-label">🌱 为什么要学化学？</div>
      <p>化学是<strong>解释物质是什么、如何变化</strong>的科学。药物如何治病？铁为何生锈而金不生锈？电池如何储电？这些都有化学解答。酸碱概念与血液pH调节直接相关，氧化还原是电池和燃料电池的工作原理。</p>
    </div>

    <div class="tldr">
      <div class="tldr-label">⚡ 30秒核心摘要</div>
      <ul>
        <li><strong>物质分类</strong>：纯净物（单质·化合物）vs 混合物（均匀·非均匀）</li>
        <li><strong>化学键</strong>：离子键（金属+非金属，电子转移），共价键（非金属+非金属，电子共用）</li>
        <li><strong>化学方程式</strong>：反应物 → 生成物。原子数守恒（配平系数）</li>
        <li><strong>酸碱</strong>：酸（释放H⁺），碱（释放OH⁻）。中和：酸+碱→水+盐</li>
        <li><strong>氧化还原</strong>：氧化（失去电子），还原（获得电子）</li>
      </ul>
    </div>
""",
        'h2_map': [
            ('<h2>2. 元素周期律</h2>', '<h2 id="s2">2. 元素周期律</h2>'),
            ('<h2>3. 化学键</h2>', '<h2 id="s3">3. 化学键</h2>'),
            ('<h2>4. 化学反应类型</h2>', '<h2 id="s4">4. 化学反应类型</h2>'),
            ('<h2>5. 酸碱盐与pH</h2>', '<h2 id="s5">5. 酸碱盐与pH</h2>'),
            ('<h2>6. 练习题</h2>', '<h2 id="s6">6. 练习题</h2>'),
        ]
    },
]

for cfg in zh_pages:
    content = open(cfg['path'], encoding='utf-8').read()
    content = content.replace(cfg['old_bc'], cfg['new_bc'])

    # Use meta_end as anchor, then find next h2
    old_marker = cfg['meta_end'] + '\n\n' + cfg['first_h2']
    new_marker = cfg['meta_end'] + '\n' + cfg['insert'] + '\n' + cfg['new_first_h2']

    if old_marker in content:
        content = content.replace(old_marker, new_marker)
        print(f"  OK: {cfg['path']}")
    else:
        # Try single newline
        old_marker2 = cfg['meta_end'] + '\n' + cfg['first_h2']
        if old_marker2 in content:
            content = content.replace(old_marker2, cfg['meta_end'] + '\n' + cfg['insert'] + '\n' + cfg['new_first_h2'])
            print(f"  OK (1nl): {cfg['path']}")
        else:
            print(f"  WARN NOT FOUND: {cfg['path']}")

    for old_h2, new_h2 in cfg['h2_map']:
        content = content.replace(old_h2, new_h2)

    open(cfg['path'], 'w', encoding='utf-8').write(content)
    print(f"  written: {cfg['path']}")
