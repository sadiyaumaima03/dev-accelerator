"""
Lead Qualifier v1
-----------------
Rebuilt using lists and dictionaries to mimic real API JSON payloads.
Safely extracts fields using .get() to prevent KeyErrors on missing data.
"""
#API-like data structure: A list of dictionaries to mimic real API JSON payloads.
leads_payload = [
    {"name" : "Acme Corp", "revenue" : 15, "employees" : 120, "industry" : "SaaS"},
    {"name" : "StartupX", "revenue" : 3, "employees" : 15}, #missing industry
    {"name" : "Enterprise Solutions", "revenue" : 50, "employees" : 200, "industry" : "Finance"},
    {"name" : "Unkown Entity", "revenue" : 20}, #missing employees & industry
    {"name" : "Global Retail", "revenue" : 80, "employees" : 500, "industry" : "Retail"}        
]
def quality_lead(lead):
    #safely get valuess using .get (key, default_value)
    name = lead.get("name", "Unknown Company")
    revenue = lead.get("revenue", 0)
    employees = lead.get("employees", 0)
    industry = lead.get("industry", "Not specified")

#Qualification criteria : revenue > 10M & employees >= 50
    if revenue > 10 and employees >= 50:
        return f"[QUALIFIED] {name} ({industry}) - ${revenue}M Rev, {employees} Employees"

    return f"[REJECTED] {name}"

if __name__ == "__main__":
    for lead in leads_payload:
        print(quality_lead(lead))