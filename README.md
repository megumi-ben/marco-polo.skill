# 马可波罗 Marco Polo

马可波罗是一个中文旅行规划 Codex Skill。它从最小需求收集开始，按阶段完成大交通、住宿区域、景点候选、开放时间/预约核验、坐标与图片、每日动线、预算跟踪、美食路线和高德地图 HTML 手册。

## 适合做什么

- 多日旅行规划、城市串联、行程增删改。
- 人均预算和已定/预估费用管理。
- 住宿区域比较和真实酒店点位更新。
- 景点清单、预约清单、开放时间、门票和闭馆日核验。
- 高德坐标、路线点位、餐饮点、地图 HTML 和旅行手册生成。
- 旅行过程中根据新信息继续更新文件和页面。

## 安装

把本文件夹放到 Codex 的 skills 目录下，例如：

```bash
cp -R marco-polo ~/.codex/skills/marco-polo
```

安装后，在新会话中说“使用马可波罗规划旅行”或直接描述旅行需求即可触发。

## 依赖的其他 Skill

马可波罗是总控工作流，会按阶段调用其他能力。建议一起安装或确保当前环境已有：

- `flyai`：查询大交通、酒店、门票和旅行产品价格。
- `xiaohongshu-skills`：查小红书旅行经验、住宿区域、美食和景点口碑。
- `xhs-auth`：管理小红书登录状态，供小红书检索使用。
- `xhs-explore`：搜索和查看小红书笔记。
- `amap-lbs-skill`：高德 POI、坐标、周边和路线查询。
- `amap-jsapi-skill`：生成高德 JSAPI 地图 HTML。
- `frontend-design`：优化最终旅行手册的前端呈现。

没有全部依赖时也可以使用，但对应阶段会降级：例如没有小红书能力时只走常规搜索和官方核验；没有高德能力时无法稳定生成坐标和地图。

## 外部配置

生成高德地图页面时，需要高德开放平台 Key。模板位于：

```text
assets/amap-html-template/config.local.example.js
```

复制为 `config.local.js` 后填入自己的：

- `AMAP_JSAPI_KEY`
- `AMAP_SECURITY_JS_CODE`
- `AMAP_WEB_SERVICE_KEY`

发布到 GitHub 或公开网页前，不要提交真实 Key。公开展示页建议只保留前端地图所需配置，并在高德控制台限制域名白名单。

## 输出文件

默认会在 `travel_plan/<行程名>/` 下维护：

- `行程需求.json`
- `行程状态.md`
- `费用跟踪.csv`
- `大交通方案.md`
- `住宿区域候选.md`
- `候选景点清单.csv`
- `景点详情清单.csv`
- `景点坐标.csv`
- `景点图片.csv`
- `每日行程.md`
- `市内交通方案.md`
- `美食推荐.md`
- `信息来源.md`
- `index.html`
- `map.html`
- `city-impression.html`
- `food.html`
- `config.local.js`

## 使用示例

```text
$marco-polo 端午去扬州 2 天，2 个成人，人均 1000，想看园林、博物馆和早茶，帮我规划并生成地图手册。
```

```text
使用马可波罗，把住宿酒店换成真实地址，重新更新地图点位和预算。
```

```text
用马可波罗生成详细版 HTML，要求 index 单文件入口能切换路线图、城市印象和美食路线。
```

## 发布说明

本包不包含真实 API Key，也不包含用户具体旅行数据。`assets/amap-html-template/` 只作为生成新行程页面的基础模板。
