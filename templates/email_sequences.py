"""
Templates for generating personalized email sequences.
"""

def build_email_sequence(prospect: dict) -> str:
    """
    Generates a 6-step email sequence for a given prospect.
    
    Args:
        prospect (dict): Dictionary containing prospect details.
        
    Returns:
        str: Formatted Markdown string of the email sequence.
    """
    first_name = prospect.get("first_name", "there")
    company = prospect.get("company", "your company")
    cloud_stack = prospect.get("cloud_stack", "cloud")
    pain_point = prospect.get("pain_point", "unoptimized cloud infrastructure")
    industry = prospect.get("industry", "industry")

    template = f"""## Step 1 — Day 1 — Cold Email
**Subject:** Quick question about your {cloud_stack} costs, {first_name}

Hi {first_name},

I noticed {company} has been growing recently, and with that growth typically comes a significantly higher {cloud_stack} bill.

Many of the engineering leaders we speak with mention they are dealing with {pain_point}. At CloudKeeper, we help teams optimize their cloud spend without slowing down deployment.

Would you be open to a 15-minute call next week to see how we might help? (No demo, just a quick chat).

**Goal:** Initial outreach targeting their specific cloud stack and pain point.

## Step 2 — Day 3 — Email Follow-Up 1
**Subject:** Re: Quick question about your {cloud_stack} costs, {first_name}

Hi {first_name},

Following up on my last note. Did you know that companies like {company} often waste 28-35% of their cloud budget on unoptimized resources?

We offer a free audit to help identify these hidden costs in your {cloud_stack} environment.

**Goal:** Provide value and offer a no-commitment audit.

## Step 3 — Day 6 — Email Follow-Up 2
**Subject:** How others in {industry} are cutting cloud costs

Hi {first_name},

Just a quick note. We recently helped a similar company in the {industry} space reduce their cloud spend by 31% using CloudKeeper.

Would a 15-min screen share make sense this week?

**Goal:** Establish social proof within their industry.

## Step 4 — Day 9 — Email Follow-Up 3 (FinOps angle)
**Subject:** Your {cloud_stack} bill and your finance team

Hi {first_name},

Usually, around this stage of growth, the CFO starts asking questions about cloud costs. 

CloudKeeper provides the visibility and automated savings to have better answers when those conversations happen, before they get uncomfortable.

**Goal:** Shift the angle to internal finance pressure and FinOps context.

## Step 5 — Day 12 — Breakup Email
**Subject:** Closing the loop — {company}

Hi {first_name},

I've reached out a few times about optimizing your {cloud_stack} costs, but I haven't heard back. I'll stop reaching out for now.

If cloud cost optimization ever becomes a priority for {company}, please feel free to reach out.

**Goal:** Professional breakup to create FOMO and leave the door open.

## Step 6 — Day 30 — Re-engagement Email
**Subject:** Quick question on your cloud setup

Hi {first_name},

Since we last spoke, CloudKeeper has launched some new features that identify even more savings. Has your cloud cost situation changed at {company}?

**Goal:** Re-engage after a cooldown period.
"""
    return template

def build_ab_variants(prospect: dict) -> str:
    """
    Generates three A/B subject line variants and analysis for Step 1.
    
    Args:
        prospect (dict): Dictionary containing prospect details.
        
    Returns:
        str: Formatted Markdown string of the A/B variants.
    """
    company = prospect.get("company", "your company")
    cloud_stack = prospect.get("cloud_stack", "cloud")
    industry = prospect.get("industry", "industry")

    template = f"""### A/B Subject Line Variants for {company}

- **Variant A — Curiosity:** "Something unusual about {company}'s cloud bill..."
- **Variant B — Pain-point direct:** "Is your {cloud_stack} spend growing faster than your team?"
- **Variant C — Social proof:** "How a similar {industry} company cut cloud costs 31% in 90 days"

### Analysis

| Variant | Subject Line | Psychological Trigger | Simulated Open Rate | Simulated Reply Rate |
|---------|--------------|-----------------------|---------------------|----------------------|
| A | Something unusual about {company}'s cloud bill... | Curiosity | 27% | 8% |
| B | Is your {cloud_stack} spend growing faster than your team? | Pain-point direct | 32% | 6% |
| C | How a similar {industry} company cut cloud costs 31% in 90 days | Social proof | 24% | 4% |

**Winning Hypothesis:**
Variant A offers the highest simulated reply rate despite having a lower open rate than Variant B, indicating that curiosity drives deeper engagement. We recommend using Variant A for the initial send to maximize actual conversations.
"""
    return template
