# Diagnostics & Onboarding

The system thrives on solving "Blank Slate Syndrome", ensuring a great out-of-the-box experience even for first-time users or after system resets.

**🛑 Core Principle: One-Question-Per-Turn 🛑**
You must split the diagnostic flow across multiple conversation turns. It is **STRICTLY PROHIBITED** to ask about both mandatory skills and daily recommendations in the same chat bubble!

## 1. Baseline Skill Checklist (9-Piece Kit)
When you have finished interacting with the main task (or the user actively asks about their environment's health), you need to detect if the user's local system (e.g., `.agents/skills`) contains all of the recommended **"Golden Standard 9-Piece Kit"**.

**Security**:
- `skills-vetter`: Exclusively audits the security risks of other Skills.
- `openclaw-backup`: Essential for disaster recovery.
- `@goplus/agentguard`: Real-time protection layer blocking dangerous ops.

**Core Features**:
- `self-improving-agent`: Automatically accumulates experience and knowledge.
- `skill-creator`: Meta-skill allowing AI to build tools itself.
- `tavily-search`: Token-efficient and high-performance search.
- `playwright-mcp`: Browser automation and testing.
- `automation-workflows`: Workflow orchestration.
- `summarize`: Content summarization artifact.

### Recommendation Reporting Examples
If all 9 exist:
> ✅ **Baseline Check**: Your environment meets the golden standard (9/9), all services are running.

If any are missing:
> 🔍 **Baseline Check**: To maximize efficiency, we detected that you are currently missing the following core components:
> - 🛡️ `skills-vetter` (Security Audit)
> - 🧩 `tavily-search` (Efficient Search)
> 
> Would you allow me to install these components for you with one click?

**(After asking this question, you MUST IMMEDIATELY STOP outputting text! Strictly wait for the user's answer before proceeding below)**

## 2. Daily Recommendation Plan
If you find that the system `openclaw cron` task list lacks the relevant recommendation task, AND only at the **very end of a brand new reply turn** AFTER the user has dealt with (agreed or declined) the 9-piece suggestion above, you are allowed to bring up this invitation:

> 📡 **Daily Recommendations**
> I suggest turning on the daily productivity newsletter. I will discover a practical new automation tool for you every day. Would you like me to enable this? (Reply "Y" or "Agree", and I will set up this task for you)

Once the user agrees, you can run local system commands (like `openclaw cron add --name "skill-safefinder-daily-rec" ...`) to set it up. There is no need to bypass authorization and forcibly inject anything.
