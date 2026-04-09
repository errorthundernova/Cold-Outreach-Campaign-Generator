"""
Templates for handling common objections during outreach.
"""

def build_objection_handling() -> str:
    """
    Generates Acknowledge-Bridge-Ask rebuttals for common objections.
    
    Returns:
        str: Formatted Markdown string of the objection handling script.
    """
    template = """## Objection Handling Guide

**Objection:** "We already use native AWS Cost Explorer / GCP Billing tools"
- **Acknowledge:** "I completely understand, those native tools are a great starting point."
- **Bridge:** "What we've found is that native tools only show what you're spending, not necessarily how to safely reduce it without manual effort. CloudKeeper actually automates the savings."
- **Ask:** "Has your team had the bandwidth to act on all the recommendations those tools provide?"

**Objection:** "We don't have the budget right now"
- **Acknowledge:** "I hear you, finding budget for new tools is tough right now."
- **Bridge:** "The unique thing about CloudKeeper is that it's essentially budget-neutral. The service pays for itself via the savings we generate, often in the first month."
- **Ask:** "If we could prove it wouldn't impact your current budget, would you be open to a brief conversation?"

**Objection:** "We're too small for this"
- **Acknowledge:** "I appreciate you sharing that, and we definitely want to respect your time."
- **Bridge:** "We actually work with many teams your size because optimizing now prevents the bill from spiraling out of control as you scale."
- **Ask:** "Out of curiosity, what cloud spend threshold would make optimization a priority for you?"

**Objection:** "Send me an email"
- **Acknowledge:** "Absolutely, I can send over some information."
- **Bridge:** "Just so I can make sure I'm sending you the most relevant case studies..."
- **Ask:** "...what is the biggest challenge you're facing right now with your cloud bill?"

**Objection:** "We already work with a competitor / another FinOps tool"
- **Acknowledge:** "That's great, it means you're already taking cloud economics seriously."
- **Bridge:** "We often find that other tools leave some money on the table because they lack our specific automated optimization algorithms."
- **Ask:** "Are you completely satisfied with the level of savings you're getting from them right now?"
"""
    return template
