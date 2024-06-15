import pandas as pd
from sklearn.model_selection import train_test_split

# Load the cleaned dataset
clean_file_path = 'data/cleaned_diabetes_dataset.csv'
data = pd.read_csv(clean_file_path)

# Split the dataset
train_data, test_data = train_test_split(data, test_size=0.1, random_state=42)

# Save the split datasets
train_file_path = 'data/train_diabetes_dataset.csv'
test_file_path = 'data/test_diabetes_dataset.csv'
train_data.to_csv(train_file_path, index=False)
test_data.to_csv(test_file_path, index=False)
print("Generated " + train_file_path)
print("Generated " + test_file_path)