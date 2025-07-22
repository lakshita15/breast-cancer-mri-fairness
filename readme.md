
# Fairness Evaluation in Breast Cancer Classification Using MRI

This project explores fairness in breast cancer classification using MRI and clinical data. We analyze whether prediction performance varies across subgroups like age and breast density, aiming to identify and reduce potential bias in tumor response prediction models.

## 🗃️ Dataset

- **Source**: Duke Breast Cancer MRI dataset (The Cancer Imaging Archive)
- **Data Includes**:
  - MRI-derived imaging features
  - Clinical features: age, breast density (T1/T2), tumor response, histology, etc.

## 📦 Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/lakshita15/breast-cancer-mri-fairness.git
   cd breast-mri-fairness
   ```

2. **Set up the environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # or use `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

3. **Prepare the data**  
   - Place clinical and imaging CSV files inside the `data/` folder  
   - Ensure columns like `patient_id`, `breastDensity_T1`, `response`, etc., are correctly formatted

## ▶️ How to Run

1. **Run EDA Notebook**  
   Explore patient demographics, tumor response, breast density patterns, correlations:
   ```bash
   jupyter notebook notebooks/1_EDA.ipynb
   ```

2. **Run Preprocessing Notebook**  
   Merge clinical and imaging data, handle missing values, standardize:
   ```bash
   jupyter notebook notebooks/2_Merge_Preprocessing.ipynb
   ```

3. **Run Modeling + Fairness Evaluation**  
   Train a classification model and evaluate subgroup performance:
   ```bash
   jupyter notebook notebooks/3_Modeling_Fairness.ipynb
   ```

## 📂 Output

- `merged_data.csv`: Cleaned dataset combining clinical and imaging data
- Visual outputs in `breast-cancer-mri-fairness/results_lgbm_tuned/`:
  - Boxplots
  - Heatmaps
  - Tumor volume analysis
- Fairness metric tables (planned)

## 🛠️ Dependencies

- Python 3.9+
- pandas, numpy, seaborn, matplotlib
- scikit-learn
- jupyter
- (Coming soon) PyTorch or TensorFlow for deep learning

Install all via:
```bash
pip install -r requirements.txt
```

## ✍️ Author

**Lakshita Mahajan**  
MSc Data Science & Analytics, Toronto Metropolitan University  
Major Research Project – 2025
