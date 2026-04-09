"""
Templates for generating cold call scripts.
"""

def build_call_script(prospect: dict) -> str:
    """
    Generates a customized cold call script for a prospect.
    
    Args:
        prospect (dict): Dictionary containing prospect details.
        
    Returns:
        str: Formatted Markdown string of the call script.
    """
    first_name = prospect.get("first_name", "there")
    cloud_stack = prospect.get("cloud_stack", "cloud")
    company = prospect.get("company", "your company")
    title = prospect.get("title", "leader")

    template = f"""## Cold Call Script for {first_name} at {company}

### 1. Introduction
"Hi {first_name}, this is [Your Name] with CloudKeeper. We help companies reduce their cloud spend."

### 2. Permission Opener
"Is this a terrible time to chat for a quick minute?"
*(If yes: "No problem, I'll email you my contact info. Have a great day!")*

### 3. 15-Second Elevator Pitch
"The reason for my call is that many of the {title}s we speak with are struggling to keep their {cloud_stack} costs in check as they scale. We've built a platform that optimizes {cloud_stack} spend behind the scenes, typically saving companies around 30% without requiring any architectural changes."

### 4. Qualifying Question
"How are you currently getting visibility into your cloud spend, and do you have a regular cost review process in place?"

### 5. Bridge to Demo
"It sounds like you might be missing out on some potential savings, especially with the way your {cloud_stack} setup is evolving. At {company}, we can likely find some immediate wins for you."

### 6. Close for Meeting
"Would you be open to a 15-minute introductory call next Tuesday or Wednesday so I can share exactly how we do this?"

### 7. Voicemail Script
"Hi {first_name}, this is [Your Name] from CloudKeeper. I have some ideas on reducing your {cloud_stack} bill. My number is [Callback Number]. Thanks!"
"""
    return template
