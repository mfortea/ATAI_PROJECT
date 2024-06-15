import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset
file_path = 'data/diabetes_dataset.csv'
data = pd.read_csv(file_path)

# Data cleaning
# Replace 'No Info' values with NaN
data.replace('No Info', pd.NA, inplace=True)

# Handle missing values
# One option is to drop rows with missing values
data.dropna(inplace=True)

# Encode categorical variables
label_encoders = {}
for column in ['gender', 'smoking_history']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Save the cleaned dataset
clean_file_path = 'data/cleaned_diabetes_dataset.csv'
data.to_csv(clean_file_path, index=False)
print("Generated " + clean_file_path)