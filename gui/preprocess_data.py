import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv("deadlock_dataset.csv")

# Handle missing values
df.fillna(df.mean(), inplace=True)

# Normalize numerical columns (if needed)
scaler = StandardScaler()
df.iloc[:, 1:] = scaler.fit_transform(df.iloc[:, 1:])

# Save the cleaned data
df.to_csv("cleaned_deadlock_dataset.csv", index=False)

print("✅ Data preprocessing complete. Saved as cleaned_deadlock_dataset.csv")
