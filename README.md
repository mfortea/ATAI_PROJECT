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
%%% ATAI - DIABETES PROBLOG MODEL %%%
% Variables definition / Possible values
0.5::gender(0); 0.5::gender(1).
0.33::age(old); 0.33::age(middle_aged); 0.34::age(young).
0.5::hypertension(0); 0.5::hypertension(1).
0.5::heart_disease(0); 0.5::heart_disease(1).
0.2::smoking_history(0); 0.2::smoking_history(1); 0.2::smoking_history(2); 0.2::smoking_history(3); 0.2::smoking_history(4).
0.33::bmi(underweight_normal); 0.33::bmi(overweight); 0.34::bmi(obese).
0.33::hba1c_level(diabetic); 0.33::hba1c_level(normal); 0.34::hba1c_level(prediabetic).
0.33::blood_glucose_level(normal); 0.33::blood_glucose_level(prediabetic); 0.34::blood_glucose_level(diabetic).

% Conditional probabilities
0.09541336353340883::diabetes :- gender(0).
0.13187203791469193::diabetes :- gender(1).

0.2084520804494748::diabetes :- age(old).
0.06491215437788019::diabetes :- age(middle_aged).
0.010383251730541955::diabetes :- age(young).

0.089981174763821::diabetes :- hypertension(0).
0.29221709374502625::diabetes :- hypertension(1).

0.3484597548857237::diabetes :- heart_disease(1).
0.0979972206327148::diabetes :- heart_disease(0).

0.09534121669753526::diabetes :- smoking_history(3).
0.10208916648718501::diabetes :- smoking_history(0).
0.17001710863986313::diabetes :- smoking_history(2).
0.11788211788211789::diabetes :- smoking_history(1).
0.10702652396463472::diabetes :- smoking_history(4).

0.09482876947361196::diabetes :- bmi(underweight_normal).
0.2566552901023891::diabetes :- bmi(overweight).
0.375::diabetes :- bmi(obese).

0.43722543352601156::diabetes :- hba1c_level(diabetic).
0.019734123157459704::diabetes :- hba1c_level(normal).
0.10155483432711902::diabetes :- hba1c_level(prediabetic).

0.058578865453764825::diabetes :- blood_glucose_level(normal).
0.10809608540925267::diabetes :- blood_glucose_level(prediabetic).
1.0::diabetes :- blood_glucose_level(diabetic).

%%% Evidences for Profile 1 %%%
evidence(gender(1)).  % Male
evidence(age(young)).  % Young
evidence(hypertension(0)).  % No hypertension
evidence(heart_disease(0)).  % No heart disease
evidence(smoking_history(1)).  % Light smoking history
evidence(bmi(overweight)).  % Overweight
evidence(hba1c_level(normal)).  % Normal HbA1c level
evidence(blood_glucose_level(diabetic)).  % Diabetic blood glucose level

%%% Query %%%
query(diabetes).


%%% Evidences for Profile 2 %%%
evidence(gender(0)).  % Female
evidence(age(old)).  % Old
evidence(hypertension(1)).  % Hypertension
evidence(heart_disease(1)).  % Heart disease
evidence(smoking_history(3)).  % Moderate smoking history
evidence(bmi(obese)).  % Obese
evidence(hba1c_level(diabetic)).  % Diabetic HbA1c level
evidence(blood_glucose_level(normal)).  % Normal blood glucose level

%%% Query %%%
query(diabetes).

%%% Evidences for Profile 3 %%%
evidence(gender(1)).  % Male
evidence(age(middle_aged)).  % Middle-aged
evidence(hypertension(0)).  % No hypertension
evidence(heart_disease(0)).  % No heart disease
evidence(smoking_history(0)).  % Non-smoker
evidence(bmi(underweight_normal)).  % Normal or underweight
evidence(hba1c_level(prediabetic)).  % Prediabetic HbA1c level
evidence(blood_glucose_level(normal)).  % Normal blood glucose level

%%% Query %%%
query(diabetes).
```

