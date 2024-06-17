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

% Queries
query(diabetes).