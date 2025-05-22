import pandas as pd

def load_clinical_data(filepath):
    df = pd.read_excel(filepath, engine="openpyxl")
    df = df.iloc[2:].reset_index(drop=True)  # remove metadata rows
    return df
