space_delimited_data = """
"""

# Split the data by space and create a list of numbers
numbers = space_delimited_data.split()

# Create a DataFrame with a single column
df = pd.DataFrame({'Numbers': numbers})

# Export the DataFrame to Excel
df.to_excel('/usr/output_aapl_pred4.xlsx', index=False)