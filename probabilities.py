import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load the cleaned dataset
filepath = 'data/cleaned_diabetes_dataset.csv'
df_cleaned = pd.read_csv(filepath)

# Split data into training and testing sets
X = df_cleaned.drop('diabetes', axis=1)
y = df_cleaned['diabetes']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Calculate probabilities using the dataset
probabilities = {}

# Define intervals for continuous variables
age_bins = pd.cut(df_cleaned['age'], bins=3, labels=['Young', 'Middle-aged', 'Old'])
bmi_bins = pd.cut(df_cleaned['bmi'], bins=3, labels=['Underweight/Normal', 'Overweight', 'Obese'])
glucose_bins = pd.cut(df_cleaned['blood_glucose_level'], bins=3, labels=['Normal', 'Prediabetic', 'Diabetic'])
hba1c_bins = pd.cut(df_cleaned['HbA1c_level'], bins=[0, 5.7, 6.5, np.inf], labels=['Normal', 'Prediabetic', 'Diabetic'])

# Group and calculate probabilities by interval
for column in X.columns:
    prob_values = {}
    if column == 'age':
        values = age_bins.unique()
    elif column == 'bmi':
        values = bmi_bins.unique()
    elif column == 'blood_glucose_level':
        values = glucose_bins.unique()
    elif column == 'HbA1c_level':
        values = hba1c_bins.unique()
    else:
        values = df_cleaned[column].unique()
    
    for value in values:
        if column == 'age':
            count_with_diabetes = np.sum((age_bins == value) & (df_cleaned['diabetes'] == 1))
            count_without_diabetes = np.sum((age_bins == value) & (df_cleaned['diabetes'] == 0))
            total_count = np.sum(age_bins == value)
        elif column == 'bmi':
            count_with_diabetes = np.sum((bmi_bins == value) & (df_cleaned['diabetes'] == 1))
            count_without_diabetes = np.sum((bmi_bins == value) & (df_cleaned['diabetes'] == 0))
            total_count = np.sum(bmi_bins == value)
        elif column == 'blood_glucose_level':
            count_with_diabetes = np.sum((glucose_bins == value) & (df_cleaned['diabetes'] == 1))
            count_without_diabetes = np.sum((glucose_bins == value) & (df_cleaned['diabetes'] == 0))
            total_count = np.sum(glucose_bins == value)
        elif column == 'HbA1c_level':
            count_with_diabetes = np.sum((hba1c_bins == value) & (df_cleaned['diabetes'] == 1))
            count_without_diabetes = np.sum((hba1c_bins == value) & (df_cleaned['diabetes'] == 0))
            total_count = np.sum(hba1c_bins == value)
        else:
            count_with_diabetes = np.sum((df_cleaned[column] == value) & (df_cleaned['diabetes'] == 1))
            count_without_diabetes = np.sum((df_cleaned[column] == value) & (df_cleaned['diabetes'] == 0))
            total_count = np.sum(df_cleaned[column] == value)
        
        if total_count > 0:
            prob_with_diabetes = count_with_diabetes / total_count
            prob_without_diabetes = count_without_diabetes / total_count
        else:
            prob_with_diabetes = 0
            prob_without_diabetes = 0
        
        prob_values[str(value)] = (prob_with_diabetes, prob_without_diabetes)
    
    probabilities[column] = prob_values

# Normalize the probabilities to ensure they sum to 1 within each variable
for column, values in probabilities.items():
    for value in values:
        total_prob = values[value][0] + values[value][1]
        if total_prob > 0:
            values[value] = (values[value][0] / total_prob, values[value][1] / total_prob)

# Save the probabilities to a CSV file
output_file = 'probabilities.csv'
with open(output_file, 'w') as f:
    f.write("Variable,Value,Prob_with_diabetes,Prob_without_diabetes\n")
    for variable, values in probabilities.items():
        for value, probs in values.items():
            f.write(f"{variable},{value},{probs[0]},{probs[1]}\n")

print(f"Probabilities saved to {output_file}")