companies = [
                {"name" : "TechCorp", "revenue" : 15},
                {"name" : "DataDynamics", "revenue" : 45},
                {"name" : "LocalBake", "revenue" : 2},
                {"name" : "GreenClean", "revenue" : 8},
                {"name" : "GlobalLogistics", "revenue" : 120},
            ]
print("Companies with revenue above $10M:")

for company in companies:
    if company["revenue"] > 10:
        print(f"- {company ['name']} : ${company ['revenue']}M")