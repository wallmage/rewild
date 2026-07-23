# Rewild

[![GitHub stars](https://img.shields.io/github/stars/wallmage/rewild?style=flat-square)](https://github.com/wallmage/rewild/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/wallmage/rewild?style=flat-square)](https://github.com/wallmage/rewild/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/wallmage/rewild?style=flat-square)](https://github.com/wallmage/rewild/watchers)
[![GitHub last commit](https://img.shields.io/github/last-commit/wallmage/rewild?style=flat-square)](https://github.com/wallmage/rewild/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/wallmage/rewild?style=flat-square)](https://github.com/wallmage/rewild)
[![Top language](https://img.shields.io/github/languages/top/wallmage/rewild?style=flat-square)](https://github.com/wallmage/rewild)
[![Focus](https://img.shields.io/badge/focus-human%20writing-111827?style=flat-square)](https://github.com/wallmage/rewild)
[![Removes](https://img.shields.io/badge/removes-AI%20writing%20patterns-0f766e?style=flat-square)](https://github.com/wallmage/rewild)
[![Keeps](https://img.shields.io/badge/keeps-your%20voice-4f46e5?style=flat-square)](https://github.com/wallmage/rewild)
[![Languages](https://img.shields.io/badge/languages-English%20%7C%20%E4%B8%AD%E6%96%87%20%7C%20Deutsch-b45309?style=flat-square)](https://github.com/wallmage/rewild)
[![Benchmark](https://img.shields.io/badge/benchmark-30%2F30-2563eb?style=flat-square)](https://github.com/wallmage/rewild)

[English](README.md) | [中文](README.zh-CN.md) | [Deutsch](README.de.md)

AI 写的东西有一种味道，你肯定闻到过：动不动就"随着……的不断发展"，四字成语一串一串，结尾永远是"未来将会更加美好"。大多数"去 AI 化"工具呢，就是把这些套话擦掉，留下一段干净但没灵魂的文字。Rewild 不一样——它去掉 AI 痕迹的同时，把你的声音还给你。观点还在，节奏还在，棱角也还在。不编造事实，不硬塞人设。就是你本来想写的那段话。

**中文基准测试 30/30。41 个中文专属模式。三种语言。**

## 基准测试：Rewild 中文 vs. 典型去 AI 工具

相同 AI 文本，相同模型，盲测对比。每篇输出 10 项评分标准，3 个测试文本。

| | Rewild-ZH | 典型 24 模式工具 |
|---|---|---|
| **得分** | **30 / 30 (100%)** | 20 / 30 (67%) |
| 无 AI 词汇 / 翻译腔 | 6/6 | 6/6 |
| 无公式化结构 | 6/6 | 6/6 |
| 无四字套语 / 假引用 | 6/6 | 5/6 |
| 句式变化 + 具体细节 | 6/6 | 0/6 |
| 语气词 + 观点/情感 | 6/6 | 3/6 |

前三行基本打平——去掉表面的 AI 套话，大多数工具都能做到。差距在后面两行：句式变化、具体细节、语气词、有没有自己的观点。典型工具的得分是 0/6 和 3/6，加起来才 3 分。Rewild 拿了 12 分满分。为什么？因为"不像 AI"只是底线，不是终点。光把套话删掉，剩下的东西照样没人味。得把节奏调回来，把原文里已有的细节往前推，让文字敢有态度——Rewild 干的是这件事。

100% vs. 67%，差了整整 10 分。中文上的差距比英文还大，原因不复杂：通用工具压根没有中文专属的检测模式。语气词缺失、四字成语堆砌、翻译腔——这仨是中文 AI 写作最明显的痕迹，通用工具一个都不认。

> **输入（AI 套话）：** 随着人工智能技术的不断发展，我司始终秉持创新驱动、砥砺前行的理念……据统计显示，超过 87% 的用户……不忘初心、开拓创新、赋能增效……未来将会更加美好。
>
> **典型工具输出：** 我们做了一个智能平台，帮用户少做重复的事。上线后收到的反馈还不错——内部调研里大概 87% 的用户说体验比之前好。接下来会继续根据实际使用情况做调整。
>
> **Rewild 输出：** AI 写作工具确实提高了内容生产效率，也让更多人更容易把初稿写出来。但问题也很明显：很多稿子虽然通顺，读起来却像一个模子里刻出来的。与其说未来一定更美好，不如先把质量这件事讲明白。

典型工具把套话换了个说法，87% 这个没来源的数字照抄不误。Rewild 把虚的部分指出来，把话说实在。

## 为什么 Rewild 管用

大多数去 AI 工具就二十来条通用规则：删掉"此外"，变变句子长度，完事。表面问题是处理了，往深了就不行了。Rewild 多走了四步：

**41 个中文专属模式，不是 20 条通用规则。** 每种语言的 AI 痕迹不一样啊。英文 AI 爱说"testament""landscape"，动不动来个破折号。中文 AI 毛病是另一套：语气词不用，四字成语一串一串，"的"字连环套，开头永远"随着……的不断发展"。Rewild 给每种语言做了专门的模式库，来源是学术研究和真实检测数据。

**两层架构。** `SKILL.md`（操作手册）精简，启动快，规则一目了然。`references/patterns.md`（诊断目录）详尽，按需加载——词汇表、改写前后对比、学术引用，用到哪块读哪块。精度够了，上下文窗口也没浪费。

**反编造是核心规则。** 很多工具"人性化"的办法是编故事、造数据、加一段第一人称经历。Rewild 不干这事。输出里每一个细节都必须在原文里找得到——人味靠的是节奏和观点，不是靠编。

**防矫枉过正。** 每篇都用同样三招"加人味"——短句连发、假装自我纠正、每段一个反问——只会造出另一种同样好认的模板。Rewild 限制单篇的改动数量并轮换手法，改十篇不会是同一种腔调。

## 改写流程

Rewild 不是逐句改——逐句改只是把 AI 的骨架擦亮，架子还立在那儿。它先给每一段分类：

- **本来就像人写的？** 不动。改过头是这类工具最常见的翻车方式，干净的段落顶多修一小处。
- **有零星痕迹？** 对照模式库，原地改掉。
- **通篇 AI 味？** 别补，重说一遍。记下事实，把原文放到一边，按同样的语域重新写，再逐条核对每个细节都来自原文。

书面文体是例外。公告、公文、营销稿只删和压，不整段重说——书面骨架本身就是语域，重说容易滑进聊天腔。整段重说只留给随笔、博客这种靠个人声音撑起来的文字。

交付前跑两道检查。一个干净上下文的审稿人盲看改写稿，把还像 AI 的地方标出来；然后自带的脚本量一遍模型自己看不见的统计痕迹，改到报告干净为止。这套流程做过盲测：让评审在不知道谁是谁的情况下，拿旧版的输出和现在这版对比打分，现在这版每一项都赢了。

## 中文专属模式

Rewild-ZH 检测 10 种中文特有的 AI 痕迹，每种都不难认：

- **语气词缺失** — 呢/啊/吧/嘛/哦 都不见了，这是最强的中文 AI 信号，一条就能揪出大部分 AI 文本
- **"首先…其次…最后" 僵化骨架** — AI 不会起承转合，只会排列编号
- **翻译腔/欧化句式** — "的"字串过长，被动句滥用，一看就不是母语写法
- **对偶句过密** — 虎嗅数据：AI 每篇 4 个 vs 人类 0.67 个
- **过度连接词** — 中文是意合语言，不需要标记每个逻辑关系嘛
- **四字成语堆砌** — 一段 3 个以上成语？大概率 AI
- **公式化开头** — "随着……的不断发展"——一眼就知道了吧
- **假引用和虚构统计** — 没来源的"78% 的用户"，编的
- **标点符号异常** — 分号过多，顿号逗号混着用
- **术语混搭失败** — 跨领域术语强行拼凑，读着别扭

## 技能

| 技能 | 模式数 | 特色 |
|------|--------|------|
| [English](rewild-en/SKILL.md) | 42 | 精简 `SKILL.md` + 详细 [pattern catalog](rewild-en/references/patterns.md) |
| [中文](rewild-zh/SKILL.md) | 41 | 中文特有模式：语气词缺失、翻译腔、四字套语、公式化开头 |
| [Deutsch](rewild-de/SKILL.md) | 42 | 德语特有模式：Modalpartikeln、Komposita、Gedankenstrich、Konnektoren-Flut |

## 如何使用

1. 把你需要的语言的技能文件夹（`rewild-en/` 或 `rewild-zh/`）整个复制到技能目录——Claude Code 是 `~/.claude/skills/`。文件夹别拆散：`references/` 模式库和 `scripts/` 检测脚本要跟着一起走。
2. 或者，在别的 LLM 里把 `SKILL.md` 当系统提示词粘进去，`references/patterns.md` 放在旁边供模型按需读取。
3. 说"rewild 一下"，然后粘贴你的文本。

## 自动量化检测

每个技能文件夹都自带 [`scripts/naturalness-check.py`](rewild-zh/scripts/naturalness-check.py)（Python 3，零依赖）。它对文本做统计筛查：句长是否均匀、句子开头是否重复、段落长短是否雷同、AI 高频词、标点问题（中文里的半角标点、分号滥用、引号风格混用等）。

跑这个脚本是工作流里的必做步骤：模型每次改写都会自动检测，修到零警告才交付。你也可以随时手动跑：

```
python3 rewild-zh/scripts/naturalness-check.py draft.txt --lang zh
```

## 结构设计

每种语言拆成两个文件，有讲究的。

`SKILL.md` 是操作手册。定义什么时候触发、什么东西不能动、不同场景怎么校准、好的声音长什么样。快速检查清单、完整改写示例、评分标准都在里面。每次都加载到上下文。

`references/patterns.md` 是诊断目录。装着完整的语言专属 AI 模式库——词汇表、改写前后对比、严重程度排序、学术引用来源。模型按需读取，用到哪块读哪块。

拆开的好处：启动快，诊断够深，上下文也不浪费。

## 改写前 / 改写后

**AI 生成：**
> 近年来，随着人工智能技术的快速发展，内容创作领域经历了深刻的变革。首先，AI 写作工具的普及显著提高了内容生产效率。此外，值得注意的是，AI 生成的内容在质量方面仍然面临着不可忽视的挑战。总的来说，未来将会更加美好。

**Rewild 之后：**
> AI 写作工具确实提高了内容生产效率，也让更多人更容易把初稿写出来。但问题也很明显：很多稿子虽然通顺，读起来却像一个模子里刻出来的。与其说未来一定更美好，不如先把质量这件事讲明白。

## 来源

- [维基百科：AI 写作特征](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Tercon & Dobrovoljc (2025) — 44 项研究综合
- 虎嗅——修辞手法频率量化分析
- PaperBert——AI 论文常用词解析
- AIGCleaner——检测权重分析
- LLM-Detector (arXiv: 2402.01158)

## 设计原则

- 只在你明确说"有 AI 味"时才触发
- 不编造数字、案例、经历、引语
- 正式文本保持正式，不会硬塞语气词
- 人味靠的是提取原文已有的细节，不靠编
- 默认两遍：交付前由一个干净上下文的子代理盲审成品

---

## 作者

[Wallny](https://github.com/wallmage)
