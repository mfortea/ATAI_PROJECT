import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import joblib

# Load the test dataset
test_file_path = 'data/test_diabetes_dataset.csv'
test_data = pd.read_csv(test_file_path)

# Load the trained model
model_file_path = 'models/diabetes_model.pkl'
model = joblib.load(model_file_path)

# Separate features and labels from the test set
X_test = test_data.drop('diabetes', axis=1)
y_test = test_data['diabetes']

# Make predictions
y_pred = model.predict(X_test)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
specificity = conf_matrix[0,0] / (conf_matrix[0,0] + conf_matrix[0,1])

# Print evaluation metrics
print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall (Sensitivity): {recall:.2f}')
print(f'Specificity: {specificity:.2f}')
print(f'F1-Score: {f1:.2f}')
print(f'Confusion Matrix:\n{conf_matrix}')