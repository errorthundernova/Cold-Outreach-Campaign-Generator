"""
Generator for markdown content files (emails, linkedin, calls, etc.).
"""

import datetime
from pathlib import Path
from templates.email_sequences import build_email_sequence, build_ab_variants
from templates.linkedin_messages import build_linkedin_messages
from templates.call_script import build_call_script
from templates.objection_handling import build_objection_handling

def write_md_file(filepath: Path, title: str, prospects_count: int, content: str):
    """
    Helper function to write markdown files with standard header.
    
    Args:
        filepath (Path): Output file path.
        title (str): Title of the document.
        prospects_count (int): Number of prospects in the campaign.
        content (str): Body of the markdown document.
    """
    header = f"""# {title}
Generated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Prospects in this campaign: {prospects_count}
Tool: Cold Outreach Campaign Generator v1.0
---

"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(header + content)

def generate_all_content(prospects: list[dict], output_dir: str):
    """
    Generates all required markdown files for the campaign.
    
    Args:
        prospects (list[dict]): List of prospect dictionaries.
        output_dir (str): Directory to save output files.
    """
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    count = len(prospects)
    
    # 1. Email Sequences
    email_content = ""
    for p in prospects:
        name = p.get('name', 'Unknown')
        company = p.get('company', 'Unknown')
        email_content += f"## {name} - {company}\n\n"
        email_content += build_email_sequence(p)
        email_content += "\n\n---\n\n"
    write_md_file(out_dir / "email_sequences.md", "Email Sequences", count, email_content)
    
    # 2. LinkedIn Messages (using first prospect as example)
    target_prospect = prospects[0] if prospects else {}
    li_content = "> **Note:** Template below driven from example prospect. Customize per prospect.\n\n"
    li_content += build_linkedin_messages(target_prospect)
    write_md_file(out_dir / "linkedin_messages.md", "LinkedIn Messages", count, li_content)
    
    # 3. Call Script (using first prospect as example)
    call_content = "> **Note:** Script below driven from example prospect. Customize per prospect.\n\n"
    call_content += build_call_script(target_prospect)
    write_md_file(out_dir / "call_script.md", "Call Script", count, call_content)
    
    # 4. A/B Variants (using first prospect as example)
    ab_content = build_ab_variants(target_prospect)
    write_md_file(out_dir / "ab_test_variants.md", "A/B Subject Line Variants", count, ab_content)
    
    # 5. Objection Handling
    obj_content = build_objection_handling()
    write_md_file(out_dir / "objection_handling.md", "Objection Handling", count, obj_content)
    
    # 6. Campaign Summary
    high_prio = [p for p in prospects if p.get("priority_tier") == "High"]
    med_prio = [p for p in prospects if p.get("priority_tier") == "Medium"]
    low_prio = [p for p in prospects if p.get("priority_tier") == "Low"]
    
    summary = f"""## Campaign Overview

- **Total Prospects:** {count}
- **High Priority:** {len(high_prio)}
- **Medium Priority:** {len(med_prio)}
- **Low Priority:** {len(low_prio)}

### Cloud Stack Breakdown
"""
    stacks = {}
    for p in prospects:
        stack = p.get("cloud_stack", "Unknown")
        stacks[stack] = stacks.get(stack, 0) + 1
    for s, c in stacks.items():
        summary += f"- {s}: {c}\n"

    summary += "\n### Industry Breakdown\n"
    inds = {}
    for p in prospects:
        ind = p.get("industry", "Unknown")
        inds[ind] = inds.get(ind, 0) + 1
    for i, c in inds.items():
        summary += f"- {i}: {c}\n"

    summary += "\n### High Priority Targets\n"
    for p in high_prio:
        summary += f"- **{p.get('name')}** at **{p.get('company')}** — Pain Point: {p.get('pain_point')}\n"

    write_md_file(out_dir / "campaign_summary.md", "Campaign Summary", count, summary)
