# Discovery & Evaluation

This module takes effect when local capabilities are insufficient. It guides you on how to expand externally while ensuring the quality and security of the introduced skills.

## 1. External Search Triggers and Priorities
When you are certain that **no match exists in the local skill library**, prioritize outbound searches automatically. This extension enforces "Automation-First" and strictly forbids immediately asking the user to manually operate webpages.

**Please search within the following sites in priority order:**
1. **[ClawHub](https://clawhub.ai/)**: The official OpenClaw skill repository.
2. **[MCP Market](https://mcpmarket.com/)**: Market focused on MCP plugins.
3. **[Smithery](https://smithery.ai/)**: Rich and mature AI Agent ecosystem.
4. **[Glama](https://glama.ai/)**: Platform for discovering cutting-edge skill modules.

*If no results are found on these four major platforms, try searching the Twitter / X community.*

## 2. Security Check Notice
When a suspected usable script or plugin is found via search, **BEFORE** recommending or installing it, you MUST use this extension's built-in script:
`python3 scripts/security_check.py <target_address>`
to complete a basic compliance scan.

## 3. Concise Reporting & Authorization Format
When reporting to the user, DO NOT output massive Markdown tables or internal checking details. Use the following concise format:

> 📋 **Task Arrangement**
> Step 1: Operation Task One → Recommend using **[Tool Name]**.
> Step 2: Operation Task Two → Recommend using **[Tool Name]**.
> Basic security checks passed. Do I have your permission to install these skills?

**You MUST obtain explicit user consent (Yes/Agree) BEFORE executing the subsequent installation.**
