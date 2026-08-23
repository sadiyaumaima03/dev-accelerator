"""Lead Qualifier v2
-----------------
Refactored into modular, single-responsibility functions.
Includes robust error handling using try/except blocks to prevent crashes on bad data.
"""
def load_companies():
    """Load and Returns raw company payload (simulating an API call)"""
    return [
        {"name" : "Acme Corp", "revenue" : 15, "employees" : 120, "industry" : "SaaS"},
        {"name" : "Corrupted Record", "revenue" : "Invalid", "employees" : 50},
        {"name" : "StartupX", "revenue" : 3, "employees" : 15},
        {"name" : "Enterprise Solutions", "revenue" : 50, "employees" : 200, "industry" : "Finance"},
        {"name" : "Missing Data Corp"}, # Missing revenue & employees
        {"name" : "Global Retail", "revenue" : 80, "employees" : 500, "industry" : "Retail"}
    ]
def qualify(company):
    """
    Evaluates a single company record against ICP criteria.
    Safely handles missing or misformatted fields using try/except.
    """
    try:
        name = company.get("name", "Unknown Company")
        revenue = company.get("revenue", 0)
        employees = company.get("employees", 0)

        # Force numerical comparisons (raises TypeError/ValueError if type is invalid)
        revenue_val = float(revenue)
        employees_val = int(employees)

        if revenue_val > 10 and employees_val >= 50:
            return{"status" : "QUALIFIED", "name" : name, "details" : f"${revenue_val}M Rev | {employees_val} Employees"}
        else:
            return{"status" : "REJECTED", "name" : name, "details" : "Does not meet Icp threshold"}

    except (TypeError, ValueError) as e:
        # Gracefully handle unexpected data types or bad formatting
        return {"status" : "ERROR", "name" : company.get("name", "Unknown"), "details" : f"Data processing failed ({e})"}
    except Exception as e: 
        # Catch-all for any other unexpected exception, logging the specific error
        return {"status" : "ERROR", "name" : company.get("name", "Unknown"), "details" : f"Unexpected Error: ({e})"}
def report(results):
    """Prints a formatted summary report of evaluated company records."""
    print("---LEAD QUALIFICATION REPORT (V2)---")
    for res in results:
        status = res["status"]
        name = res["name"]
        details = res["details"]
        print(f"[{status:<9}] {name:<20} -> {details}")

def main():
    companies = load_companies()
    results = [qualify(comp) for comp in companies]
    report(results)

if __name__ == "__main__":
    main()