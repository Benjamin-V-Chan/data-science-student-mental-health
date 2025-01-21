import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

# Load the cleaned dataset
input_path = 'data/processed/cleaned_data.csv'
data = pd.read_csv(input_path)

# Prepare features and labels
features = data.drop(columns=['do_you_have_depression?_Yes'])
labels = data['do_you_have_depression?_Yes']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred)
print(report)

# Save the model and results
os.makedirs('outputs', exist_ok=True)
joblib.dump(model, 'outputs/depression_model.pkl')
with open('outputs/classification_report.txt', 'w') as f:
    f.write(report)