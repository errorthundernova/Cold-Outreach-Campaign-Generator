"""
Templates for generating personalized LinkedIn messages.
"""

def build_linkedin_messages(prospect: dict) -> str:
    """
    Generates a set of LinkedIn messages for a prospect.
    
    Args:
        prospect (dict): Dictionary containing prospect details.
        
    Returns:
        str: Formatted Markdown string of the LinkedIn sequence.
    """
    first_name = prospect.get("first_name", "there")
    title = prospect.get("title", "leader")

    template = f"""## LinkedIn Connection Request
**Note:** Hi {first_name}, keeping my network fresh with {title}s leading cloud initiatives. We help teams control their cloud costs. Would love to connect!

## DM 1 — Post-Connection (Value-First)
Hi {first_name}, thanks for connecting! I usually see leaders in your position dealing with complex visibility issues as their infrastructure scales. I put together a short guide on tackling these common pitfalls — happy to send it your way if you're interested.

## DM 2 — Bump (Day 6)
Hi {first_name}, just bringing this to the top of your inbox. Sent you an email recently but thought I'd touch base here too. No pressure either way.

## Voice Note Template — Record this as a 30-second audio message:
Hey {first_name}, [pause] thanks for the connection. [pause] I know you're busy, so I'll keep this brief. We've been helping similar engineering teams cut their cloud bills by about 30% without changing their architecture. [pause] If you're open to a quick chat next week, let me know. If not, totally fine. Have a great week!
"""
    return template
