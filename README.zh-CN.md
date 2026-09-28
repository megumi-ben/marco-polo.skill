<div align="center">

# 🧭 Marco Polo · 马可波罗

[English](README.md) | **简体中文**

### 把旅行灵感，变成走得通的行程。

**一个和你一起做选择、查路线、安排每一天的 AI 旅行规划 Skill。**

高德定位有依据 · 每天安排有细节 · 交互地图看得见

![Agent Skill](https://img.shields.io/badge/Agent-Skill-263F3A?style=flat-square)
![高德地图](https://img.shields.io/badge/地图与路线-高德-397D68?style=flat-square)
![小红书](https://img.shields.io/badge/旅行经验-小红书-C76565?style=flat-square)
[![GitHub Stars](https://img.shields.io/github/stars/megumi-ben/marco-polo.skill?style=flat-square&color=C18A53)](https://github.com/megumi-ben/marco-polo.skill/stargazers)

[为什么选择它](#为什么选择马可波罗) · [快速上手](#快速上手) · [看一趟旅行怎样生成](#从一句话到一趟旅行) · [工作流](#工作流) · [参与改进](#一起让旅行规划更好用)

</div>

收藏了很多攻略，真正出发前，还是要把问题一个个串起来：**住哪里方便？哪些地方值得去？一天怎么走？预约来得及吗？**

马可波罗结合小红书经验、官方信息与高德地图，先帮你选住宿和景点，再围绕**住宿位置、景点分布与适合游玩的时间**，把交通、吃饭、预约和休息一起排进每天。最后交付一份能继续修改的旅行计划，以及一张可以点击、筛选和查看路线的地图网页。

**你决定旅行的样子，马可波罗帮你理清实现它的细节。** 当前聚焦中文、单城市旅行，也支持近郊安排。

![南京旅行地图：分日路线、行程时间轴与景点详情](assets/demo-map.png)

<p align="center"><sub>南京行程展示：分日配色、游览时间轴与景点详情。此示例中的连线表示游览顺序；规划时会另行查询实际交通路线。</sub></p>

## 为什么选择马可波罗

马可波罗把 **位置准确、时间合适、体验完整、地图清楚** 放进同一套工作流。每个推荐都要回答：它为什么适合你，又怎样融入这一天？

### 📍 更有依据的路线：从你住的地方开始规划

用高德查询景点、住宿与必要交通节点的 **POI、坐标和入口**，核对同名地点与景区内部点，再根据空间位置分组。每天从哪里出发、哪些景点适合放在一起、晚上如何回住处，都围绕你选定的住宿来考虑。

相邻地点之间继续查询实际步行、公交或驾车路线，校正道路距离与预计耗时，把绕路、入口位置和换乘成本纳入安排。**空间上顺路，交通上有依据。**

### 🕒 更细致的一天：景点、小吃、预约和休息一起安排

白天适合参观的场馆、饭点顺路的小吃街、适合晚上的夜景，会结合开放时间、停留时长、预约场次和交通耗时共同排程。午餐、休息、排队、取行李与赶车也有时间预算，让一天的安排有余量。

另有一份独立的 **景点预约清单**：记录预约入口、放票规则、目标时段、当前状态和失败后的备选。你能提前准备，也能在每日行程里看到当天的预约摘要。

### 🗺️ 更美观、更直观的交付：一张可以操作的旅行地图

最终生成清爽的 **`map.html` 地图网页**：每天用不同颜色展示，路线带顺序与方向箭头；可以按日期筛选、从行程列表定位景点，点击查看停留时间、预约和交通信息，并检查手机上的可读性。

住宿、景点、餐饮和交通节点在地图上有各自的标识。出发前看全局，旅行时查下一站，文字行程和空间位置可以一起看。

**还有这些贯穿全程的细节：**

| 优势 | 对你的实际帮助 |
|---|---|
| 🧭 **选择权在你手里** | 候选覆盖不同类型与片区，说明推荐理由、优先级和取舍。先给足选择空间，再由你筛选；已有车票、酒店和必去项目会被尊重。 |
| 🔎 **信息有来源，未知有标记** | 小红书提供经验与口碑，官方来源核验开放、票务和预约。保留查询时间与依据；尚未核验、尚未预约的事项明确可见，便于出发前复查。 |
| 💰 **人均费用算得清楚** | 酒店、打车等共享费用按人数分摊，门票等单人费用分别记录；区分已定、预估与未知项，避免联票、景区内部项目重复计费。 |
| 🔄 **改计划时保持一致** | 换住宿、增减景点或调整日期后，更新受影响的日程、路段、预约目标、费用与地图。已有预订保留实际状态，需变更时说明影响。 |

行程、预约清单、预算和地图都会保存为本地文件，并保留结构化数据。你可以带走成果，继续讨论和修改。

适合准备周末游、和朋友商量去哪里，或者已经订好车票酒店、只想把市内几天安排明白的人。已有大交通可以跳过比较，已有酒店可以直接进入景点选择。

## 快速上手

### 1. 安装马可波罗

在目标项目目录运行：

```bash
mkdir -p .agents/skills
git clone https://github.com/megumi-ben/marco-polo.skill.git .agents/skills/marco-polo
```

也可以[下载 ZIP](https://github.com/megumi-ben/marco-polo.skill/archive/refs/heads/main.zip)，解压后将文件夹重命名为 `marco-polo`，放入 `.agents/skills/`。安装后应能找到 `.agents/skills/marco-polo/SKILL.md`。

### 2. 接上旅行研究和地图能力

安装 **小红书、两个高德 Skill**，配置自己的高德 Key 和小红书登录状态；需要查询大交通或具体酒店时，再安装 **FlyAI**。各依赖与 `marco-polo/` 并列放置，下载入口和配置方式见[依赖安装](#依赖安装)。

依赖尚未齐全时，可以先整理需求；相关研究和地图能力会说明缺口，不冒充已经验证。

### 3. 说说你想怎么旅行

```text
$marco-polo 想去北京玩两天，喜欢人文建筑和公园，节奏松一点。
大交通自己安排，住宿区域还没选。帮我一起规划一下。
```

从你已知的信息开始即可。马可波罗会补问当前阶段需要的日期、人数、预算等信息，再和你一起推进。后续只需继续说：

> 酒店换到这个地址，帮我调整每天的首尾交通和费用。

<details>
<summary>其他安装位置、更新与成果目录</summary>

- 也可安装到个人目录 `~/.agents/skills/marco-polo/`，参见 [Codex 官方安装位置](https://learn.chatgpt.com/docs/build-skills)。未发现新 Skill 时，可重新开启会话或重启 Codex。
- 安装新版时更新已有的马可波罗文件夹，先保留自己添加的本地配置。
- 成果按阶段保存在工作目录的 `travel_plan/<城市-行程标识>/`；继续修改时沿用同一份数据，无需重新开始。

</details>

## 从一句话到一趟旅行

下面用一次简化的虚构对话，展示完整过程。省略日期、人数等补充问答；示例不对应真实出行，具体开放、票务、预约与路线仍需针对出行日期核验。

**你：** 想去北京玩两天，喜欢人文建筑和公园，节奏松一点。大交通自己安排，住宿区域还没选。

**马可波罗：** 先比较 1—3 个住宿区域，解释交通、氛围与取舍；同时给出有比较空间的景点候选，附推荐理由、优先级、建议时长和初步预约信息。

**你：** 住宿选王府井一带。想去故宫、景山、北海和天坛，其他先不排。

**马可波罗：** 核验开放与预约，查询坐标、入口和交通，把相邻项目归在一起，并给用餐、休息与返程留出时间。先与你确认这样的分配：

| 日期 | 简化输出示例 |
|---|---|
| 第 1 天 | 上午故宫 → 午餐与休息 → 景山 → 北海 |
| 第 2 天 | 上午天坛 → 午餐 → 自由活动，按车次预留返程时间 |

**你：** 这个分配可以，进入地图阶段。

**马可波罗：** 按确认的安排生成交互地图，检查底图、日期筛选、点位定位和手机显示，同步行程、预约与费用文件。尚未办理的预约，仍标注未预约。

你会拿到 **每天怎么走、预约怎么办、费用怎么算、地点在哪里** 这几类成果。选择、依据和待落实事项都有记录，方便出发前准备，也方便途中调整。

<details>
<summary>展开查看交付文件与用途</summary>

| 交付 | 用来做什么 |
|---|---|
| `住宿区域候选.md`、`景点清单.md` | 比较选择，保留推荐理由与最终名单 |
| `景点预约.md` | 出发前知道何时、去哪里、预约哪一场 |
| `每日行程.md` | 查看每天的景点、交通、餐饮、休息与备选 |
| `费用跟踪.csv` | 区分已定、预估和未知费用，按人均计算 |
| `map.html` | 查看位置、顺序、方向和点位详情 |
| `行程数据.json`、`行程状态.md` | 保存事实、决定和进度，便于继续修改 |

按需生成，不预先堆空文件；大交通比较只有需要时才增加。详细约定见 [输出规范](references/outputs.md)。

</details>

## 工作流

五个阶段，逐步收敛：先理解需求，再研究住宿和景点，选好后安排路线，确认后生成地图。

```mermaid
flowchart TD
    A[① 收集需求与已有安排] --> B{需要辅助规划大交通？}
    B -->|需要| C[比较方案，记录采用结果]
    B -->|已有或自理| D[记录到离时间边界]
    C --> E[② 推荐住宿区域]
    D --> E
    C --> F[③ 推荐景点候选]
    D --> F
    E --> G[用户选住宿与景点]
    F --> G
    G --> H[④ 核验开放、门票与预约]
    H --> I[高德 POI 与入口坐标 → 空间分组]
    I --> J[查询真实交通 → 加入餐饮、休息与预算]
    J --> K{用户确认路线}
    K -->|调整| I
    K -->|确认| L[⑤ 生成交互地图并在浏览器验收]
    L --> M[交付行程、预约清单、预算与地图]
```

②③可以并行研究；已有酒店直接采用。紧迫的预约事项提前提醒，不必等候选全部筛完。用户确认的是方案，不代表已经下单或预约成功。

## 依赖安装

外部依赖共 **4 个 Skill 包**，本包不附带它们的源码或小红书操作指南。入口于 2026-09-27 核对，上游变化时以所下载版本的说明为准。

| Skill | 作用 | 下载来源 |
|---|---|---|
| `amap-lbs-skill` | POI、坐标、入口、实际交通 | [高德官方说明](https://lbs.amap.com/api/skill/ready-to-use/summary) · [官方 ZIP](https://a.amap.com/jsapi/static/openClaw/amap-lbs-skill.zip) |
| `amap-jsapi-skill` | 高德交互地图 | [高德官方说明](https://lbs.amap.com/api/skill/ready-to-use/summary) · [官方 ZIP](https://a.amap.com/jsapi/static/openClaw/amap-jsapi-skill.zip) |
| `xiaohongshu-skills` | 住宿、景点、美食经验 | [XHS Bridge 版本源码](https://github.com/autoclaw-cc/xiaohongshu-skills)，Code → Download ZIP，保留整个仓库结构 |
| `flyai` | 大交通、具体酒店和旅行产品 | [官方安装说明](https://open.fly.ai/docs/quickstart) · [源码](https://github.com/alibaba-flyai/flyai-skill)，下载后取 `skills/flyai/` |

**高德：** 将两个 ZIP 解压到 Skill 目录，在 [高德控制台](https://console.amap.com/dev/key/app)申请自己的 Web 服务 Key 和 Web 端 JSAPI Key。LBS 按其说明安装运行依赖（带 `package.json` 的版本可运行 `npm install`），配置 `AMAP_WEBSERVICE_KEY`。JSAPI 需要自己的 Key 及对应安全配置。[Web 服务配置说明](https://lbs.amap.com/api/webservice/create-project-and-key)

生成地图时，把本包 `assets/amap-html-template/config.local.example.js` 复制到**行程目录**并改名 `config.local.js`，填入自己的 `jsapiKey`，以及 `securityJsCode` 或已部署的 `serviceHost`。不在浏览器配置里放 Web 服务 Key；公开部署按[高德安全配置](https://lbs.amap.com/api/javascript-api-v2/guide/abc/prepare)使用适当的代理和域名限制。

生成后，在行程目录运行 `python3 -m http.server 8000 --bind 127.0.0.1`，打开 `http://127.0.0.1:8000/map.html` 预览地图。底图需要联网；结束后在终端按 Ctrl+C。

**小红书：** 需要 Python 3.11+、uv 和 Chrome。在依赖目录运行 `uv sync`；按[上游 README](https://github.com/autoclaw-cc/xiaohongshu-skills#安装)将其 `extension/` 加载为 Chrome 已解压扩展，启用 XHS Bridge，再运行 `uv run python scripts/cli.py check-login`。登录和搜索子技能已在集合内，无需另外下载；登录态由使用者建立。本工作流不需要发布、评论或点赞。

**FlyAI（按需）：** 安装 `skills/flyai/` 后运行 `npm i -g @fly-ai/flyai-cli`，再用 `flyai --help` 确认当前命令。查询命令和可选 API Key 按[上游说明](https://github.com/alibaba-flyai/flyai-skill#quick-start)配置，使用自己的凭据。

安装后先验证一次 POI 与路段查询、小红书搜索与正文读取。只有登录成功或文件存在，还不足以确认对应能力可用。依赖缺失时工作流会说明缺口，不冒充完成研究或验证。

<details>
<summary>包内结构与地图模板</summary>

## 包内结构

```text
marco-polo/
├── SKILL.md                         五阶段工作流
├── README.md                        英文介绍、示例与安装
├── README.zh-CN.md                  中文介绍、示例与安装
├── agents/openai.yaml               名称与调用提示
├── references/outputs.md            输入输出与文件规范
└── assets/
    ├── demo-map.png                 南京地图展示
    └── amap-html-template/
        ├── map.html                不含行程数据的地图骨架
        └── config.local.example.js 凭据占位符
```

</details>


## 一起让旅行规划更好用

马可波罗来自真实规划过程中的反复调整：候选太少、相邻景点被拆开、别名重复、预约遗漏……这些具体问题，是继续改进它的起点。

如果这个项目能帮到你的下一次出行，欢迎点一个 **[⭐ Star](https://github.com/megumi-ben/marco-polo.skill)**，让更多旅行者发现它。

也欢迎[提交反馈](https://github.com/megumi-ben/marco-polo.skill/issues)或贡献改进：分享哪个环节好用、哪里安排不合理，或者你希望怎样调整。反馈时请去掉 API Key、登录信息、订单和个人行程中的敏感内容。

从 [SKILL.md](SKILL.md) 可以了解规划规则，从 [输出规范](references/outputs.md) 可以了解各阶段如何交接。一起把每一次实际使用，变成下一次更好的出发。
