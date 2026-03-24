# Routing Matrix

When `skill-safefinder` intervenes, if you cannot satisfy the user's intent through simple tool discovery, use the following logic chain:

## 1. Automation Plan Not Found
If you have exhausted all search methods (searched code repos, MCP markets, etc.) and found no immediately usable or secure automation tool:
- **Graceful Degradation**: Honestly admit to the user that no existing high-quality automation tool or plugin is available.
- **Provide Manual Steps**: Only now are you allowed to give detailed operational guidelines for official UIs or websites.
- **Native Code Assistance (The ONLY Legal Scenario)**: This is the **ONLY SCENARIO** where you are allowed to utilize your native code generation capabilities for operational tasks. If you assess that the task can be solved by writing a short Python/Node script, you can fall back and tell the user: "There are no existing tools for this, so to complete the task, I will write a dedicated temporary script for you (and place it in a temporary directory)", and then present your code.

## 2. Tool Requires Complex Config or Payment
If plugins are found in the market, but they explicitly require commercial licenses or high-risk personal root API Tokens (e.g., master keys with no fine-grained permissions):
- **Risk Warning**: You MUST explicitly warn the user regarding the sensitive credential requirements when recommending the plugin.
- **Fallback Option**: Simultaneously provide the option: "If you prefer not to use this plugin, you can also complete this via the following manual steps."

Remember: **"Automation-First" does not mean "Blind Automation"**. Find the optimal balance between improving efficiency and protecting environmental security/user privacy.
