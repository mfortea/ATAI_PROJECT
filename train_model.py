import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the training dataset
train_file_path = 'data/train_dataset.csv'
train_data = pd.read_csv(train_file_path)

# Separate features and labels
X_train = train_data.drop('diabetes', axis=1)
y_train = train_data['diabetes']

# Train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the trained model
model_file_path = 'models/diabetes_model.pkl'
joblib.dump(model, model_file_path)
print("Generated model in " + model_file_path)
