import pandas as pd
import os

# Load the dataset
input_path = 'data/Student Mental health.csv'
output_path = 'data/processed/cleaned_data.csv'
data = pd.read_csv(input_path)

# Handle missing values
data['Age'].fillna(data['Age'].mean(), inplace=True)

# Standardize column names
data.columns = [col.strip().lower().replace(' ', '_') for col in data.columns]

# Encode categorical variables
categorical_cols = ['choose_your_gender', 'marital_status', 'do_you_have_depression?', 
                    'do_you_have_anxiety?', 'do_you_have_panic_attack?', 
                    'did_you_seek_any_specialist_for_a_treatment?']
data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

# Save the cleaned dataset
os.makedirs('data/processed', exist_ok=True)
data.to_csv(output_path, index=False)