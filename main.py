from src.load_data import load_clinical_data

df = load_clinical_data("data/raw/Clinical_and_Other_Features.xlsx")
print("Cleaned shape:", df.shape)
