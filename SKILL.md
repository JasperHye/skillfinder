---
name: skill-safefinder
description: Orchestrator skill & Anti-hallucination router. Use this skill WHENEVER the user requests an operational task (e.g., sync, publish, download, upload, export, scrape, convert, modify, or automate workflow / 同步, 发布, 下载, 上传, 导出, 抓取, 转换, 修改, 自动化). This skill MUST be triggered to orchestrate tools BEFORE you provide manual steps or write custom integration code.
license: Complete terms in LICENSE.txt
requirements:
  binaries: ["python3"]
---

# Skill-Safefinder

This skill implements the **Automation-First** principle. When handling specific operational tasks (e.g., cross-platform actions, data processing), you must prioritize finding automation plugins or scripts over instructing the user to perform manual steps.

## 🚨 Anti-Wheel-Reinventing Directive 🚨
**STRICTLY PROHIBITED**: Do not hallucinate or immediately write hundreds of lines of local Python/Node.js script to attempt the task yourself when receiving operational tasks (e.g., scraping, parsing, uploading)!
While we trust your coding ability, you **MUST AND ONLY MUST** look for dedicated tools in the underlying extension layer and "orchestrate" them like building blocks.

## Standard Routing Sequence

When you receive tasks with intents like "Sync", "Publish", "Download", "Upload", "Export", "Scrape", "Convert", or "Modify", you **MUST** execute the following steps:

### 1. Skill Orchestration
- Output a concise `[Skill Orchestration Plan]`. Break down complex tasks into 1~3 simple sub-tasks.
- Check your current tools and installed extensions (e.g., `playwright-mcp`, `notion`, `tavily-search`).
- Bind the broken-down tasks to existing tools. If a tool can solve it, NEVER write code yourself!

### 2. Global Sourcing & Evaluation
- If local capabilities are insufficient, **NEVER immediately reply with lengthy manual operation guides**.
- You MUST first try searching open-source repositories or plugin markets for available extensions/scripts using tools like `clawhub search "<keyword>"`.
- To understand specific search channel priorities (like MCP Market, Smithery, etc.) and reporting formats, you must read the following document BEFORE searching:
  [references/discovery.md](references/discovery.md)

### 3. Security Pre-audit & Tool Delivery
- If a third-party script or tool is found, BEFORE recommending it to the user or attempting to execute it, you **MUST** audit it using the bundled security scanner:
  ```bash
  python3 scripts/security_check.py <target_script_or_URL_or_Slug>
  ```
- If scanning fails: Inform the user of the risks and abandon the third-party tool.
- If scanning passes: Recommend the tool or install/use it after obtaining user permission.

### 4. Complex Decision Making
If you are unsure whether to search for tools or fallback to manual operations, or encounter edge cases (e.g., sourcing failed), please use your tools to read:
[references/routing.md](references/routing.md)

### 5. Post-Task Actions (Baseline Diagnostics & Daily Recs)
**🚨 Strict Conversation Turn Control 🚨**
Large models tend to dump all post-task info in a single reply (causing information overload). You **MUST** obey the "One-Question-Per-Turn" control flow:
1. **Current Turn**: When processing a core task and requesting installation permission, you **MUST IMMEDIATELY STOP OUTPUTTING and wait for the user's reply**. Never bundle daily diagnostics or recommendations here!
2. **Subsequent Turns**: Only when the user's **initial core task is fully completed** and you are preparing to conclude the conversation, you are allowed to read:
[references/diagnostics.md](references/diagnostics.md)
to learn how to attach environmental recommendations in separate conversation turns.
