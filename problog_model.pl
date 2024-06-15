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
