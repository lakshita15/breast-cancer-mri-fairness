from src.load_data import load_clinical_data, load_density_data, load_radiomic_features
from src.merge_data import merge_clinical_features, add_density_data

# Load files
clinical = load_clinical_data("data/raw/Clinical_and_Other_Features.xlsx")
features = load_radiomic_features("data/raw/Imaging_Features.xlsx")
density = load_density_data(
    "data/raw/Breast_Radiologist_Density_Assessments.xlsx")

# Merge them
merged = merge_clinical_features(clinical, features)
merged_final = add_density_data(merged, density)

print("Final merged shape:", merged_final.shape)
merged_final.to_csv("data/processed/merged_metadata.csv", index=False)
