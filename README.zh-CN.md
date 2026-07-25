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
[![Blind A/B](https://img.shields.io/badge/blind%20A%2FB-83%25%20EN%20%C2%B7%2075%25%20ZH-2563eb?style=flat-square)](benchmarks/)

[English](README.md) | [中文](README.zh-CN.md) | [Deutsch](README.de.md)

AI 写的东西有一股固定的味道，你肯定读到过。硬拔高的意义、三个形容词一串、结尾一段听着圆满其实什么也没说。市面上的"去 AI 化"工具多半是把这层味道刮掉，交还给你一段干净但没人味的文字。Rewild 做的是另一件事：把 AI 模式去掉，把你自己的声音放回去——观点、节奏、不那么齐整的地方。它不会替你编事实，也不会给你安一个原本没有的人设。

**139 条分语言的模式。三种语言。一个会读你原文、而不只是读你改稿的检测脚本。**

## 到底管不管用

有两件事在被量化，回答的是不同的问题。

**这一版比上一版好吗？** 评审同时看到同一篇原文的两个改写版本，必须二选一，不许打平——这样测试就不会像打勾清单那样很快见顶。五篇输入，三位互不通气的评审，谁都不知道哪个版本出自哪套系统。

| | English | 中文 |
|---|---|---|
| 被判定优于上一版 | **10 / 12（83%）** | **9 / 12（75%）** |
| 读起来更不像机器写的 | 是 | 是 |

中文这个结果是跑了三轮才拿到的：6/12，7/12，最后 9/12。每一轮都修掉了一个真问题。举一个：中文技能里有四处把句末语气词当成必须凑够的指标，模型于是在一封内部邮件里硬贴了个"啊"——"辛苦了啊"。三位评审全都点了这一句。现在语气词是用来诊断的，不是用来达标的。

**比通用去 AI 工具好吗？** 早先一次跑分是 30/30 对典型 24 条规则工具的 24/30，中文是 30/30 对 20/30。这个数字请当成未经确认：原始输出没留下来，而且那次跑分早于下面这些检测脚本的修复。跑分的东西都在 [`benchmarks/`](benchmarks/) 里——测试输入、评分标准、对照组提示词、盲评流程——你可以自己跑一遍，然后告诉我这数字不对。

> **输入：** 随着人工智能技术的不断发展，我司始终秉持创新驱动、砥砺前行的理念……据统计显示，超过 87% 的用户……不忘初心、开拓创新、赋能增效……未来将会更加美好。
>
> **典型工具输出：** 我们做了一个智能平台，帮用户少做重复的事。上线后收到的反馈还不错——内部调研里大概 87% 的用户说体验比之前好。接下来会继续根据实际使用情况做调整。
>
> **Rewild 输出：** AI 写作工具确实提高了效率，也让更多人能把初稿写出来。但问题也明显：很多稿子读着通顺，像一个模子刻出来的。与其说未来更美好，不如先把质量讲清楚。

典型工具把套话换了个说法，87% 这个没来源的数字照抄不误。Rewild 把虚的地方点出来。

## 为什么管用

大多数去 AI 工具就二十来条通用规则。删掉"此外"，把句子长短调一调，完事。表面问题是处理了，再往下就没有了。Rewild 多做的事集中在四处。

**每种语言一套模式，不是一套规则通吃。** 英文 AI 爱用 testament、landscape，破折号一个接一个。中文 AI 不用语气词，四字成语一串一串。德文 AI 回避 Modalpartikeln，还会把复合词拆开写。每种语言有自己的模式库，来源是学术研究和真实检测数据。

**防止矫枉过正。** 每篇都用同样三招去 AI 味——短句连发、刻意的自我纠正、每段一个反问——你只是造出了另一套同样好认的模板。Rewild 限制单篇的改动数量，并且换着用。

**忠实度，不只是文风。** 这是大部分工具完全跳过的一块。一篇改写可以一个人名一个数字都没编，照样说出原文没说过的话。有四种走法：

- 原文把判断挂在别人名下，改写把出处删了，判断留下了
- 原文只是在陈述，改写变成了承诺
- 原文说"受到影响"，改写说"全都不能用了"
- 原文交代了一个原因，改写顺手排除掉几个别的

前三种，自带脚本拿你的改稿和原文一比就能查出来。第四种查不了，只能靠写的人，模式库里写明了这一点。

**不编造，包括那些听着谦虚的话。** 输出里的每一个细节都必须原文已经有。这条规则以前有个漏洞：旧版本告诉模型，删掉无来源的吹捧之后可以补一句诚实克制的自评——模型照做了。一篇营销稿长出了原文没有的免责声明，一份发布公告让公司认了一个自己从没提过的短板。谦虚版的编造，还是编造。

## 怎么改

每一段在动手之前先分类。重度 AI 味的文字逐句修，只是把骨架擦亮，架子还立在那儿，所以工作分三条路：

- **本来就像人写的？** 不动。改过头是这类工具最常见的翻车方式，干净的段落顶多修一小处。
- **有零星痕迹？** 对照模式库原地改掉。
- **通篇 AI 味？** 重说一遍。记下事实，把原文放到一边，按同样的语域重新写，写完再逐条核对每个细节都来自原文。

重说改的是措辞，不是顺序。把随笔里那句"最重要的一课"挪到末尾，前面的铺垫就落空了。

书面文体完全不走重说这条路。公告、公文、营销稿只删和压——书面骨架本身就是语域，重说容易滑进聊天腔。

交付前跑两道检查。一个不记得原文的审稿人盲看改写稿，把还像 AI 的地方标出来。然后脚本量一遍模型自己看不见的统计痕迹，并把改稿和原文做比对。风格类警告是建议，忠实度类警告是硬伤。

## 技能

| 技能 | 模式数 | 特色 |
|------|--------|------|
| [English](rewild/SKILL.md) | 46 | 精简 `SKILL.md` + 详细 [pattern catalog](rewild/references/patterns.md) |
| [中文](rewild-zh/SKILL.md) | 45 | 中文特有模式：语气词缺失、翻译腔、四字套语、公式化开头 |
| [Deutsch](rewild-de/SKILL.md) | 48 | 德语特有模式：Modalpartikeln、Komposita、Gedankenstrich、Konnektoren-Flut |

## 如何使用

1. 把你需要的语言的技能文件夹（`rewild/`、`rewild-zh/` 或 `rewild-de/`）整个复制到技能目录，Claude Code 是 `~/.claude/skills/`。文件夹名和内容都别改：文件夹名和技能自己的 `name:` 字段是对应的，`references/` 模式库和 `scripts/` 检测脚本也要跟着走。
2. 在别的 LLM 里，把 `SKILL.md` 当系统提示词贴进去，`references/patterns.md` 放在旁边供模型按需读取。
3. 说"rewild 一下"，然后粘贴你的文本。

## 自带的检测脚本

每个技能文件夹都带一个 [`scripts/naturalness-check.py`](rewild-zh/scripts/naturalness-check.py)，Python 3，零依赖。跑它是工作流里的必做步骤，不是可选项。

把原文和改稿一起传进去，两半的活它都干：

```bash
python3 rewild-zh/scripts/naturalness-check.py 改稿.txt --source 原文.txt --lang zh
```

风格那一半量的是模式库里描述的东西：句长是否均匀、句子开头是否重复、段落长短是否雷同、AI 高频词、标点问题。忠实度那一半把两个文本对比，查出改稿里多出来的人名和数字、替原文做的承诺、被抢过来的判断、被抬高的严重程度。有警告时退出码是 1，干净时是 0，所以它也能直接当门禁用。

有几处是随手实现容易做错的。markdown 按正文读，不按骨架读——标题、代码块、表格行会跳过，列表项各算一句。匹配不受排版影响，弯引号直引号一视同仁。中文句长同时计入汉字和中间夹的英文词，所以"我们用 Kubernetes 做容器编排"这类中英混排的技术文不会被少算。

改完模式库跑一次 `--audit`，它会拿脚本里的词表和旁边的模式库对一遍，把模式库写了、脚本却看不见的词列出来：

```bash
python3 rewild-zh/scripts/naturalness-check.py --audit --lang zh
```

脚本本身有三十条回归测试，覆盖它历史上出过的每一个 bug：

```bash
python3 tests/test_checker.py
```

## 结构设计

每种语言拆成两个文件，这个拆法是有讲究的。

`SKILL.md` 是操作手册：什么时候触发、什么不能动、不同场景怎么校准、好的声音长什么样。它每次都加载进上下文，所以要精简。

`references/patterns.md` 是诊断目录，模式的完整清单，带词表、改写前后对比和引用。模型按需读取其中的章节，不用一上来全部加载。

测试里还有一个结果，说实话有点出乎意料：一条规则放在哪里，和它怎么写同样重要。忠实度那几条一开始放在讲"声音"那一节的末尾，于是模型动笔前读到的最后一段全是禁令。它写得畏手畏脚，盲测输在 5/12。原文一个字没改，只是挪进"写完之后核对"那一节，结果就变成了 10/12。

## 改写前 / 改写后

**AI 味道：**
> 近年来，随着人工智能技术的快速发展，内容创作领域经历了深刻的变革。首先，AI 写作工具的普及显著提高了内容生产效率。其次，这些工具在一定程度上降低了创作门槛。此外，值得注意的是，AI 生成的内容在质量和创意方面仍然面临着不可忽视的挑战。

**Rewild 之后：**
> AI 写作工具确实提高了内容生产效率，也让更多人更容易把初稿写出来。但问题也很明显：很多稿子虽然通顺，读起来却像一个模子里刻出来的。

## 来源

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Tercon & Dobrovoljc (2025)——44 项研究综合
- KONVENS 2024——德语 AI 文本检测
- De Gruyter 2025——德语语言复杂度分析
- 虎嗅量化分析——中文修辞手法频率
- AIGCleaner——中文检测权重

## 交付说明

- 只有你明确说"这段有 AI 味"才会触发
- 不会加进原文没有的数据、案例或经历
- 正式文体改完仍然正式
- 声音来自原文已有的细节
- 每篇改写交付前都会被盲审一次，并和原文逐条比对

---

## 作者

[Wallny](https://github.com/wallmage)
