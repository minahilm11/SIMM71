import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('israel.csv')

# Read the second CSV file
df2 = pd.read_csv('palestine.csv')

# Combine the two dataframes
combined_df = pd.concat([df1, df2])

# Remove duplicates
combined_df = combined_df.drop_duplicates()

# Save the combined dataframe to a new CSV file
combined_df.to_csv('economist_dataset.csv', index=False)
