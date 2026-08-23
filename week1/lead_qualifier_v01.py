"""Lead Qualifier v0.1
-------------------
This script takes a hardcoded list of potential client companies and filters them
based on Ideal Customer Profile (ICP) rules:
  1. Revenue must be greater than $10 million ($10M).
  2. Employee count must be 50 or more.
"""
#list company records represented as dictionaries
companies = [
    {"name" : "Acne Corp", "revenue" : 15, "employees" : 120},
    {"name" : "StartupX", "revenue" : 3, "employees" : 15},
    {"name" : "Enterprise Solutions", "revenue" : 50, "employees" : 200},
    {"name" : "MidSize Tech", "revenue" : 12, "employees" : 40},
    {"name" : " Global Retail", "revenue" : 80, "employees" : 500}
]
def quality_leads(company_list):
    print(f"--QUALIFIED LEADS (ICP Match)--")
    for company in company_list:
        #filter by two conditions using the logical and operator.
        if company["revenue"] > 10 and company["employees"] >= 50:
            print(f"[QUALIFIED] {company['name']} | Revenue: ${company['revenue']}M | Employees: {company['employees']}")
        else:
            print(f"[REJECTED] {company['name']}")

quality_leads(companies)