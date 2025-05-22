import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# Load your dataset
df = pd.read_excel("Duke/Clinical_and_Other_Features.xlsx")  # Change name if needed

# Show first 5 rows
print(df.head())  # prints first 5 rows of the DataFrame
print(df.info())  # see column names, types, and missing values
print(df.isnull().sum())  # count of NaNs in each column
# Check for duplicates
print(df.duplicated().sum())  # count of duplicates
df = df.iloc[2:].reset_index(drop=True)  # keep rows from 3rd onwards
print("Cleaned shape:", df.shape)
print(df.head(3))