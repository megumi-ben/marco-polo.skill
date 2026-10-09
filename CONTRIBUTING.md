# Contributing to Marco Polo

Useful trip reports, clearer setup instructions, and better planning rules are all welcome. You do not need to write code to help.

## Report a problem

Open an issue with the request you gave the agent, the stage that failed, the expected result, and what happened. Include the agent and model you used when relevant. A small, reproducible example is more useful than a complete private trip folder. Remove credentials, names, booking references, and other personal information.

## Propose a change

1. Create a branch and keep the change focused on one problem.
2. Explain the user-visible result in the pull request. For planning rules, include the travel scenario that motivated the change.
3. Keep English and Chinese public documentation consistent.
4. Preserve the workflow's key checks: confirm user choices, verify location and transport, account for reservations and opening hours, and clearly mark unknown information.

Avoid adding a universal rule for a one-off itinerary. A new script or file should solve a recurring problem.

## Preview the website

Python 3.9 or later is enough:

```bash
python3 scripts/build_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory _site
```

Open `http://127.0.0.1:8000/`. Check the landing page and the Nanjing map, food, and city pages on desktop and mobile. Try date filters, place details, and handbook navigation. Stop the server with Ctrl+C when finished.

The build checks local page links and excludes private configuration. Pull requests run the same build; only `main` deploys to GitHub Pages. Deployment needs the repository's **Settings → Pages → Source** set to **GitHub Actions**.

The public demo uses MapLibre and OpenFreeMap without API credentials. The planning skill continues to use Amap. See [demo notes](docs/DEMO-NOTES.md) before updating map data or third-party assets.

## Build the install package

`python3 scripts/package_skill.py` produces `_site/downloads/marco-polo.zip` from the explicit file list in that script. The site build also creates it, so the published download updates with changes to the skill. The package has one `marco-polo/` folder and only the files needed for planning. If the skill gains a required resource, add it to the file list; do not package the whole repository.

## 中文贡献说明

欢迎反馈真实使用问题、完善安装说明、优化规划流程和页面。提 Issue 时说明输入、出错阶段、预期与实际结果，必要时注明所用模型；不要上传密钥、订单和个人信息。

PR 尽量聚焦一个问题，写清改变了什么用户体验。修改规划规则时附具体场景，避免把个别行程的偏好变成所有用户必须遵守的规则。中英文说明同步更新。

网页预览使用上面的两条命令。检查电脑和手机布局、日期筛选、景点详情与手册切换。公开演示不使用私人高德凭据；Skill 的实际规划仍然使用高德。

`python3 scripts/package_skill.py` 可单独生成精简安装包；网站构建也会自动生成。新增必要资源时同步更新打包脚本中的文件清单，网站、宣传资源和本地配置不进入安装包。
