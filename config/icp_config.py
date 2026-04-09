"""
Configuration constants for the ICP (Ideal Customer Profile) and rules.
"""

ICP_INDUSTRIES = ["SaaS", "FinTech", "EdTech", "eCommerce", "HealthTech"]

BUYER_PERSONAS = ["CTO", "VP of Engineering", "Head of DevOps", "FinOps Manager",
                  "Engineering Manager", "Cloud Architect", "Director of Infrastructure"]

CLOUD_STACKS = ["AWS", "GCP", "Azure", "Multi-Cloud"]

PAIN_POINTS = {
    "AWS": [
        "Unoptimized EC2 Reserved Instance coverage",
        "Unused Elastic IPs and NAT Gateway charges",
        "S3 storage class mismatches driving up costs",
    ],
    "GCP": [
        "Lack of Committed Use Discount utilization",
        "Idle GKE node pools running 24/7",
        "BigQuery on-demand pricing vs flat-rate analysis",
    ],
    "Azure": [
        "Azure Hybrid Benefit not applied to VMs",
        "Orphaned managed disks accumulating costs",
        "Dev/test environments not using spot pricing",
    ],
    "Multi-Cloud": [
        "No unified visibility across cloud spend",
        "Duplicate services running across AWS and Azure",
        "FinOps practice absent — no cloud tagging strategy",
    ],
}

COMPANY_SIZE_SPEND_RANGE = {
    "Small (10-50)":      (5000, 25000),
    "Mid (51-200)":       (20000, 60000),
    "Large (201-1000)":   (50000, 120000),
    "Enterprise (1000+)": (100000, 300000),
}

PRIORITY_RULES = {
    "High":   {"titles": ["CTO", "VP of Engineering", "Head of DevOps", "Cloud Architect"],
               "min_spend": 40000},
    "Medium": {"titles": ["FinOps Manager", "Engineering Manager", "Director of Infrastructure"],
               "min_spend": 15000},
}
