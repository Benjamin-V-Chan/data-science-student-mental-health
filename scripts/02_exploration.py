import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the cleaned dataset
input_path = 'data/processed/cleaned_data.csv'
data = pd.read_csv(input_path)

# Create output directory
os.makedirs('outputs', exist_ok=True)

# Descriptive statistics
print(data.describe())

# Distribution of age
plt.figure()
sns.histplot(data['age'], bins=10, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('outputs/age_distribution.png')

# Proportion of mental health conditions
mental_health_cols = ['do_you_have_depression?_Yes', 'do_you_have_anxiety?_Yes', 'do_you_have_panic_attack?_Yes']
condition_counts = data[mental_health_cols].sum()
condition_counts.plot(kind='bar')
plt.title('Mental Health Conditions')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.savefig('outputs/mental_health_conditions.png')