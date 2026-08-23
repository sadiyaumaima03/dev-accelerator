#List of dictionaries containing company details
companies = [
    {"company" : "Nike", "industry" : "Sports", "employees" : 85000},
    {"company" : "Microsoft", "industry" : "Technology", "employees" : 220000},
    {"company" : "Pfizer", "industry" : "Healthcare", "employees" : 83000},
    {"company" : "JPMorgan", "industry" : "Finance", "employees" : 290000},
    {"company" : "Chevron", "industry" : "Energy", "employees" : 43000}
]
#Loop through and print only company & industry fields
for c in companies:
    print(f"Company : {c['company']} | Industry : {c['industry']}")