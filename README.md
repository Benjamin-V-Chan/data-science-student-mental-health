# data-science-student-mental-health

# Project Overview
This project aims to analyze and model factors related to student mental health. Using data on demographics, academic performance, and mental health conditions, the project includes data preprocessing, exploratory analysis, and predictive modeling to uncover insights and support informed decision-making.

---

# Folder Structure
```
project-root/
├── data/
│   ├── Student Mental health.csv       # Raw dataset
│   └── processed/                     # Folder for cleaned data
│       └── cleaned_data.csv           # Preprocessed dataset
├── scripts/
│   ├── 01_preprocessing.py            # Data preprocessing script
│   ├── 02_exploration.py              # Data exploration and visualization script
│   └── 03_modeling.py                 # Modeling script for predictions
├── outputs/
│   ├── age_distribution.png           # Age distribution visualization
│   ├── mental_health_conditions.png   # Mental health conditions visualization
│   ├── classification_report.txt      # Model evaluation report
│   └── depression_model.pkl           # Trained model
├── README.md                          # Project documentation
└── requirements.txt                   # Required Python packages
```

---

# Usage
1. Clone the repository and navigate to the project directory.
2. Place the raw dataset (`Student Mental health.csv`) in the `data/` folder.
3. Install the required Python packages (see Requirements section).
4. Run the scripts in sequence:
   - `python scripts/01_preprocessing.py` to preprocess the data.
   - `python scripts/02_exploration.py` to generate visualizations and insights.
   - `python scripts/03_modeling.py` to train and evaluate the predictive model.
5. Check the `outputs/` folder for results.

---

# Requirements
Install the required Python packages using the command below:
```
pip install -r requirements.txt
```
The `requirements.txt` file includes:
- pandas
- matplotlib
- seaborn
- scikit-learn
- joblib

---

# Acknowledgments
- **Dataset Name:** Student Mental Health
- **Dataset Author:** MD Shariful Islam
- **Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/shariful07/student-mental-health)