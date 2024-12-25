import pandas as pd

# Load the bank statement CSV file
file_path = 'csvs/Basic_Plus_3489_122424.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Display the first few rows for an initial look
print("Sample Data:")
print(df.head())

# Basic Information
print("\nData Summary:")
print(df.info())

# Example Summary Analysis (Assuming standard columns like 'Date', 'Description', 'Amount', and 'Category')
if 'Amount' in df.columns:
    # Convert 'Amount' to numeric if it's not already
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    
    # Drop rows with invalid or NaN Amount values
    df = df.dropna(subset=['Amount'])
    
    # Calculate totals
    total_income = df[df['Amount'] > 0]['Amount'].sum()
    total_expenses = df[df['Amount'] < 0]['Amount'].sum()
    net_balance = total_income + total_expenses

    # Summary statistics
    print("\nSummary Statistics:")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Balance: ${net_balance:.2f}")
    
    # Largest Transactions
    print("\nLargest Income Transactions:")
    print(df[df['Amount'] > 0].nlargest(5, 'Amount'))
    
    print("\nLargest Expense Transactions:")
    print(df[df['Amount'] < 0].nsmallest(5, 'Amount'))
    
    # Count transactions by category (if a 'Category' column exists)
    if 'Category' in df.columns:
        print("\nTransaction Counts by Category:")
        print(df['Category'].value_counts())
else:
    print("\nColumn 'Amount' not found in the data. Please verify the structure of the CSV file.")
