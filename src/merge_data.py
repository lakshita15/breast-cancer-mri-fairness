import pandas as pd

def merge_clinical_features(clinical_df, features_df):
    clinical_df = clinical_df.rename(columns={"Patient Information": "Patient ID"})
    merged_df = pd.merge(clinical_df, features_df, on="Patient ID", how="inner")
    return merged_df

def add_density_data(merged_df, density_df):
    density_df = density_df.rename(columns={"Subject_ID": "Patient ID"})
    merged = pd.merge(merged_df, density_df, on="Patient ID", how="left")
    return merged