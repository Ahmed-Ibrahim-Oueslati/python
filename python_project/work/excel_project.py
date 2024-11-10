import pandas as pd

# Load the Excel file
df = pd.read_excel('alllabPCAccounts2.xlsx')
df2 = pd.read_excel('Helix_data.xlsx')

# Print the 44th row (index 43, as pandas is 0-indexed)
print(df.iloc[43])
