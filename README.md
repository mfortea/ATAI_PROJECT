# Diabetes Prediction Project


## ⚙️ Setting up the enviroment

This project has been created over a Python3 virtual enviroment.

Create a virtual environment:
```bash
python3 -m venv atai_project
```

Activate the enviroment
```bash
source atai_project/bin/activate
```

## 📄 Dependencies
This project uses the followig Python3 dependencies:
```bash
pip3 install pandas scikit-learn matplotlib
```

## 🚀 Running the code
The original dataset is located in ```data/diabetes_dataset```

The dataset came from this Kagggle repository: https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset/data

### Cleaning the dataset
First of all for we need to clean the dataset, to do this we have to run:
```bash
python3 preprocess_data.py
```
This will generate ```cleaned_diabetes_dataset.csv``` on the data folder.

### Spliting the data
In order to separate the dataset for training and test, we are going to split it in 90% of the dataset for training and the rest 10% for test. We need to run this:
```bash
python3 split_data.py
```
This will generate ```train_diabetes_dataset.csv``` & ```test_diabetes_dataset.csv```  in the data folder .for the training and test respectivel

### Training the model
Using the Scikit-learn library we are going to train the model. For run it:
```bash
python3 train_model.py
```
This will generate ```diabetes_model.pkl``` in the models folder.

### Evaluating the model
Finally, using the Sklearn-metrics library we are going to evaluate the model and get some metrics. For run it:
```bash
python3 evaluate_model.py
```
This will output something similar to the following:
```bash
Accuracy: 0.94
Precision: 0.73
Recall (Sensitivity): 0.75
Specificity: 0.96
F1-Score: 0.74
Confusion Matrix:
[[5474  203]
 [ 186  556]]
```

## Problog model
To help to generate the Problog model, we can run the following for generate the probabilities of the model that we can use it later for make the Problog model.
```bash
python3 probabilities.py
```
This will generate a ```probabilities.csv``` file with all the probabilities normalized.

After this, this is the Problog model generated (it is also in the ```problog_model.pl``` file):
```problog
% Diabetes probabilities

% Gender
0.05610121996093861::diabetes :- gender(female).
0.08430883112411774::diabetes :- gender(male).

% Age
0.1349698892106836::diabetes :- age(old).
0.036570036923560374::diabetes :- age(middle_aged).
0.006517526862779637::diabetes :- age(young).

% Hypertension
0.05481606290367874::diabetes :- hypertension(no).
0.1966990291262136::diabetes :- hypertension(yes).

% Heart Disease
0.23887775551102206::diabetes :- heart_disease(yes).
0.05965757089352595::diabetes :- heart_disease(no).

% Smoking History
0.05822258104583282::diabetes :- smoking_history(never).
0.060602508498417536::diabetes :- smoking_history(current).
0.10961214165261383::diabetes :- smoking_history(former).
0.0747945205479452::diabetes :- smoking_history(ever).
0.06226607689690371::diabetes :- smoking_history(not_current).

% BMI
0.06362144420131291::diabetes :- bmi(overweight).
0.025024374390640234::diabetes :- bmi(underweight_normal).
0.13478395380014438::diabetes :- bmi(obese).

% HbA1c Level
0.2773122284295469::diabetes :- hba1c_level(diabetic).
0.013710057669290196::diabetes :- hba1c_level(normal).
0.07234215885947047::diabetes :- hba1c_level(prediabetic).

% Blood Glucose Level
0.07250987275120667::diabetes :- blood_glucose_level(prediabetic).
0.030506641952425084::diabetes :- blood_glucose_level(normal).
0.21950761135124977::diabetes :- blood_glucose_level(diabetic).

% Facts for a sample patient
gender(male).
age(middle_aged).
hypertension(yes).
heart_disease(no).
smoking_history(former).
bmi(overweight).
hba1c_level(prediabetic).
blood_glucose_level(normal).

```

