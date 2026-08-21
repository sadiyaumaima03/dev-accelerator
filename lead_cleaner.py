"""
Lead Cleaner v1
---------------
Loads a messy CSV of leads, drops exact duplicates, fills missing phone numbers,
and exports a cleaned Excel file split into sheets by industry.
"""
import pandas as pd

def clean_leads(input_csv, output_excel):
    #1. load the raw dataset
    df = pd.read_csv(input_csv)
    print(f"Original row count: {len(df)}")

    #2 Drop duplicate rows(without altering raw file)
    df_cleaned = df.drop_duplicates()
    print(f"Row count after removing duplicates: {len(df_cleaned)}")

    #3 Handle missing values: Fill missing phone numbers with 'Unknown'
    df_cleaned['phone'] = df_cleaned['phone'].fillna('Unknown')

    #4 Save cleaned output to excel split into per-industry sheets
    with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
        #Sheet 1: Master cleaned list
        df_cleaned.to_excel(writer, sheet_name='All Cleaned leads', index=False)

        #Separate sheets per industry
        industries = df_cleaned['industry'].dropna().unique()
        for ind in industries:
            industry_df = df_cleaned[df_cleaned['industry'] == ind]
            sheet_name = str(ind)[:30] #Excel sheet names max 31 characters
            industry_df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Cleaned leads successfully written to: {output_excel}")

if __name__ == "__main__":
    clean_leads("messy_leads.csv", "cleaned_leads.xlsx")