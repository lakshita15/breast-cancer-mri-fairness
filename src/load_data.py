import pandas as pd

def load_clinical_data(filepath):
    df = pd.read_excel(filepath, engine="openpyxl")
    df = df.iloc[2:].reset_index(drop=True) 
    return df

def load_density_data(filepath):
    df = pd.read_excel(filepath, engine="openpyxl")
    df.columns = df.columns.str.strip()
    return df

def load_radiomic_features(filepath):
    df = pd.read_excel(filepath, engine="openpyxl")
    df.columns = df.columns.str.strip()
    return df