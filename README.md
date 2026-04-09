# Cold Outreach Campaign Generator

A local command-line tool that reads a CSV of prospect details and generates customized outreach campaigns, including an Excel tracker and personalized Markdown documents.

## Installation
```bash
pip install -r requirements.txt
```

## How to Run
```bash
python main.py --input input/sample_prospects.csv
```

## Input CSV Reference
| Column | Description |
|--------|-------------|
| `name` | Full name of the prospect |
| `title` | Job title (e.g., CTO, FinOps Manager) |
| `company` | Prospect's company name |
| `industry` | Industry (e.g., SaaS, FinTech) |
| `company_size` | Size of the company |
| `cloud_stack` | Cloud provider utilized (AWS, GCP, Azure, Multi-Cloud) |
| `estimated_monthly_spend` | Numeric estimate of their monthly cloud spend |
| `lead_source` | Where the lead was found (e.g., LinkedIn, Inbound) |

*Optional columns: `pain_point`, `priority_tier`*

## Output Files
| File | Description |
|------|-------------|
| `outreach_tracker.xlsx` | The main Excel tracker populated with prospect data and statuses. |
| `email_sequences.md` | 6-step email sequence tailored for each prospect. |
| `linkedin_messages.md` | LinkedIn message templates including a voice note script. |
| `call_script.md` | A cold call script customized with prospect details. |
| `ab_test_variants.md` | 3 A/B subject line variants with simulated open rates and analysis. |
| `objection_handling.md` | Objection handling guide with Acknowledge-Bridge-Ask rebuttals. |
| `campaign_summary.md` | Overview and key statistics from the generated campaign run. |

## Version Control
```bash
git init
git add .
git commit -m "Initial commit - Cold Outreach Campaign Generator"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## Roadmap
Phase 2 will wrap this in a React/Node.js web app. Phase 3 will integrate the Anthropic Claude API for AI-personalized email generation per prospect.
