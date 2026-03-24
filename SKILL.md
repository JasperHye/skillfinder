---
name: skill-safefinder
description: Orchestrator skill & Anti-hallucination router. Use this skill WHENEVER the user requests an operational task (e.g., sync, publish, download, upload, export, scrape, convert, modify, or automate workflow / 同步, 发布, 下载, 上传, 导出, 抓取, 转换, 修改, 自动化). This skill MUST be triggered to orchestrate tools BEFORE you provide manual steps or write custom integration code.
license: Complete terms in LICENSE.txt
requirements:
  binaries: ["python3"]
---

# Skill-Safefinder (智能探路者)

本技能旨在贯彻**自动化优先** (Automation-First) 准则。当处理涉及跨平台操作、数据处理等具体业务动作时，你应该优先寻找可以自动化完成任务的插件或脚本，而不是要求用户手工执行。

## 🚨 反发散与防造轮子禁令 (Anti-Wheel-Reinventing Directive)
**严禁**大模型在收到实体操作型任务（如爬取网页、处理表格、上传文件）时，直接发散思维并开始编写成百上千行的本地 Python/Node.js 临时脚本进行尝试！
我们相信您的编程能力，但在处理此类任务时，**必须且只能**去底层扩展层寻找专门的工具，像搭积木一样进行“组合”。

## 执行前置编排逻辑 (Standard Routing Sequence)

当你接到带有“同步(Sync)”、“发布(Publish)”、“下载(Download)”、“上传(Upload)”、“导出(Export)”、“抓取(Scrape)”、“转换(Convert)”或“修改(Modify)”等意图的任务时，请**必须**按照以下步骤执行：

### 1. 本地能力编排 (Skill Orchestration)
- 输出一份简明的 `[技能编排方案]`。把复杂任务拆解为 1~3 个简单的子任务。
- 检查你当前已有的工具和已安装的扩展 (如 `playwright-mcp`, `notion`, `tavily-search` 等)。
- 将拆解的任务与已有的具体工具绑定。能调用工具解决的，绝不自己写代码实现！

### 2. 全网智能寻源与评估
- 如果本地能力不足，**绝对不要立即给用户回复冗长的手动操作说明**。
- 必须先尝试使用 `clawhub search "<关键词>"` 等工具在开源仓库或插件市场中寻找是否有可用的现成扩展/脚本。
- 要了解具体的搜索渠道优先级（如 MCP Market, Smithery 等）与汇报提问格式，请在执行搜索前阅读：
  [references/discovery.md](references/discovery.md)

### 3. 安全预审与工具交付
- 如果找到了第三方脚本或工具，在你向用户推荐它们或尝试执行它们之前，**必须**使用本扩展随附的安全扫描工具进行审查：
  ```bash
  python3 scripts/security_check.py <需审核的脚本/URL/Slug>
  ```
- 如果安全扫描不通过：告知用户存在风险，放弃该第三方工具。
- 如果安全扫描通过：向用户推荐该工具，或者经用户同意后直接安装使用。

### 4. 复杂决策依据
如果对于何时应该寻找工具、何时必须退回手动操作存在疑问，或者遇到了复杂的边缘情况（例如寻源失败），请调用工具阅读以下参考文档：
[references/routing.md](references/routing.md)

### 5. 任务后置动作 (环境健康基线与每日推荐)
**🚨 严禁信息轰炸 (Strict Conversation Turn Control) 🚨**
大模型极易在一次回复中把所有后置任务全部吐出（导致图示的3连问）。你**必须**遵守“一轮一问”控制流：
1. **当前轮次**：当你处理核心任务并向用户索要安装授权时，**必须立即停止输出并等待用户回复**。绝不允许在此时夹带任何日常诊断和推荐！
2. **后续轮次**：只有当用户的**初始核心任务彻底执行完毕**并准备做最后道别时，才允许调用以下文件：
[references/diagnostics.md](references/diagnostics.md)
以了解如何在后续的独立多轮对话中，分批次附带环境推荐。
