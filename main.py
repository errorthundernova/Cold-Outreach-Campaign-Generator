"""
Main entry point for the Cold Outreach Campaign Generator.
"""

import argparse
import csv
import sys
from pathlib import Path
from config.icp_config import PAIN_POINTS, PRIORITY_RULES
from generators.excel_generator import generate_excel_tracker
from generators.content_generator import generate_all_content

def main():
    """
    Main execution flow for the tool.
    Parses arguments, processes the CSV, and generates outputs.
    """
    parser = argparse.ArgumentParser(description="Cold Outreach Campaign Generator")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--output", default="output", help="Directory for output files")
    parser.add_argument("--verbose", action="store_true", help="Print detailed prospect info")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_dir = Path(args.output)
    
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' does not exist.")
        sys.exit(1)
        
    output_dir.mkdir(parents=True, exist_ok=True)
    
    required_columns = {"name", "title", "company", "industry", "company_size", "cloud_stack", "estimated_monthly_spend", "lead_source"}
    prospects = []
    
    with open(input_path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        
        if not reader.fieldnames:
            print("Error: CSV file is empty.")
            sys.exit(1)
            
        csv_columns = set(reader.fieldnames)
        missing_columns = required_columns - csv_columns
        
        if missing_columns:
            print(f"Error: Missing required columns in CSV: {', '.join(missing_columns)}")
            sys.exit(1)
            
        for index, row in enumerate(reader):
            prospect = dict(row)
            
            # Derive first_name
            name = prospect.get("name", "").strip()
            prospect["first_name"] = name.split()[0] if name else ""
            
            # Assign Lead_ID
            prospect["lead_id"] = f"L{index+1:03d}"
            
            # Assign Pain_Point if missing
            cloud_stack = prospect.get("cloud_stack", "AWS")
            if "pain_point" not in prospect or not prospect["pain_point"]:
                prospect["pain_point"] = PAIN_POINTS.get(cloud_stack, ["Unoptimized infrastructure costs"])[0]
                
            # Assign Priority_Tier if missing
            if "priority_tier" not in prospect or not prospect["priority_tier"]:
                title = prospect.get("title", "")
                try:
                    spend = float(prospect.get("estimated_monthly_spend", 0))
                except ValueError:
                    spend = 0
                
                tier = "Low"
                for level in ["High", "Medium"]:
                    rules = PRIORITY_RULES.get(level, {})
                    if title in rules.get("titles", []) and spend >= rules.get("min_spend", 0):
                        tier = level
                        break
                prospect["priority_tier"] = tier
                
            prospects.append(prospect)

    if not prospects:
        print("Error: No valid prospect data found in CSV.")
        sys.exit(1)

    # Generate Outputs
    generate_excel_tracker(prospects, str(output_dir / "outreach_tracker.xlsx"))
    generate_all_content(prospects, str(output_dir))
    
    # Terminal summary
    high_count = sum(1 for p in prospects if p.get("priority_tier") == "High")
    med_count = sum(1 for p in prospects if p.get("priority_tier") == "Medium")
    low_count = sum(1 for p in prospects if p.get("priority_tier") == "Low")
    
    print("\n============================================")
    print("Cold Outreach Campaign Generator — Complete")
    print("============================================")
    print(f"Prospects loaded     : {len(prospects)}")
    print(f"High priority        : {high_count}")
    print(f"Medium priority      : {med_count}")
    print(f"Low priority         : {low_count}")
    print("\nOutput files created:")
    print(f"  {output_dir}/outreach_tracker.xlsx")
    print(f"  {output_dir}/email_sequences.md")
    print(f"  {output_dir}/linkedin_messages.md")
    print(f"  {output_dir}/call_script.md")
    print(f"  {output_dir}/ab_test_variants.md")
    print(f"  {output_dir}/objection_handling.md")
    print(f"  {output_dir}/campaign_summary.md")
    print("============================================\n")
    
    if args.verbose:
        for p in prospects:
            print(f"- {p['name']} ({p['company']}) | Tier: {p['priority_tier']} | Pain Point: {p['pain_point']}")

if __name__ == "__main__":
    main()
