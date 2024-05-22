# -*- coding: utf-8 -*-
"""Jebrill D.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RcBkgkPAweJR1WoR9tvvwv1zy3eBW-Lj
"""

#Task 1: Regression Task
# I chosse heart data base for this task.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# loading heart data
data = pd.read_csv("heart.csv")

# Split our data to features and target
X = data.drop('output', axis=1)
y = data['output']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# First algorithm "Linear Regression"
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
y_pred_lr = model_lr.predict(X_test)

# Second algorithm "Random Forest Regression"
model_rf = RandomForestRegressor(random_state=42)
model_rf.fit(X_train, y_train)
y_pred_rf = model_rf.predict(X_test)

# Evaluate Model Performance
def evaluate_model(y_true, y_pred, model_name):
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"{model_name} Mean Squared Error: {mse}")
    print(f"{model_name} R-squared: {r2}")
    return mse, r2

mse_lr, r2_lr = evaluate_model(y_test, y_pred_lr, "Linear Regression")
mse_rf, r2_rf = evaluate_model(y_test, y_pred_rf, "Random Forest Regression")

# Compare model performances
if mse_lr < mse_rf:
    print("Linear Regression performed better.")
else:
    print("Random Forest Regression performed better.")

"""1. Showing accuracies of each model. Which did better?

Linear Regression Mean Squared Error: [MSE_LR]
Linear Regression R-squared: [R2_LR]
Random Forest Regression Mean Squared Error: [MSE_RF]
Random Forest Regression R-squared: [R2_RF]
The model with the lower Mean Squared Error and higher R-squared value is considered better.

2. Explanation of how the two models work (include references). Why did one perform better than the other for your dataset?

Linear Regression: This algorithm builds a correlation between different variables by choosing a linear equation to model the relationship between one dependent variable and several independent variables. A straight line implies a relationship between the two variables that can be described by an equation. The equation selected is one that has the smallest value of the sum of squares when the data is projected on to the straight line. Nonetheless, it is based on a belief that there is a reason – feature relationship which often does not exists in the actual field observations.

Random Forest Regression: The algorithm is an integration of the decision tree learners which creates many trees as weights and outputs the average prediction of the trees during training. Besides complex non-linear feature-target interactions, it is also designed to handle. But for-sale advertisement might be overfitted as its parameters are not tuned properly

It is supposed how the algorithm is going to work - it depends on the data set. Linear Regression could be slightly better fit to the present case of mostly the linear relationship between features and the target variable. Yet, Random Forest Regression is very likely to beat Linear Regression if the case is one of non-linearity or if there are complex interactions between features.


3. Suggest on different methods to improve your models. E.g. Remove/add data? If so, which features would you build on? Think about visualising the data first and seeing which features do not help with the prediction.

To improve model performance, several strategies can be employed:To improve model performance, several strategies can be employed:


Feature Engineering: Develop new attributes, for instance, or transform existing ones to accordingly present the hidden ties between the input data.

Feature Selection: Identify and eliminate features that are not linked to the prediction and are on the contrary, the ones that zero to the prediction. Correlation and other techniques such as feature importance estimation can be employed for this reason.

Hyperparameter Tuning: Optimize the parameters of the models in order to increase their learning abilities. For Random forest, this could include testing the parameter numbers of trees, their tree depth, and other parameters.

Cross-validation: Apply methods of the k-fold cross-validation functionalities to get an estimation of the generalization performance of the models and to mitigate the risk of overfitting.

Ensemble Methods: As such, many combinations of models can be used as long as the specific techniques employed maximizes their capabilities and overall accuracy.

By adopting these strategies in a methodical way and varying their application, we might be able to design more reliable regression models for the data set we are manipulating.

"""

#Task 2: Classification.
#I choose winequality-white data base for this task.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the data
data = pd.read_csv("winequality-white.csv")

# Split data into features, target
X = data.drop('quality', axis=1)
y = data['quality']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Algorithm 1: Logistic Regression
model_lr = LogisticRegression(max_iter=1000)
model_lr.fit(X_train, y_train)
y_pred_lr = model_lr.predict(X_test)

# Algorithm 2: Random Forest Classifier
model_rf = RandomForestClassifier(random_state=42)
model_rf.fit(X_train, y_train)
y_pred_rf = model_rf.predict(X_test)

# Evaluate Model Performance
accuracy_lr = accuracy_score(y_test, y_pred_lr)
accuracy_rf = accuracy_score(y_test, y_pred_rf)

print("Logistic Regression Accuracy:", accuracy_lr)
print("Random Forest Classifier Accuracy:", accuracy_rf)

# Compare model performances
if accuracy_lr > accuracy_rf:
    print("Logistic Regression performed better.")
else:
    print("Random Forest Classifier performed better.")

"""1. Showing the accuracies of each model. Which did better?

Logistic Regression Accuracy: [Accuracy_LR]
Random Forest Classifier Accuracy: [Accuracy_RF]
The model with the higher accuracy is considered better.

2. Explanation of how the two models work (include references). Why did one perform better than the other for your dataset?

Logistic Regression: This algorithm is a linear model that predicts the likelihood that the corresponding class has accidentally been written in the given input. It generates the probability with the help of logist curve. Logistic Regression is the simplest of all, yet it is interpretable; however, it assumes a predetermined linear relationship in between the features and log-odds of the target variable.

Random Forest Classifier: This algorithm is an ensemble learning method exclusively creating multiple decision trees during the process and giving back the class label (classification) which is the most common in the individual trees. Random Forests has this unique ability of depicting the intricate nuances between attributes and a dependent variable which are linear. Still they might experience an underfitting when not properly parameterized or fitted.

The performance of each choice of algorithm seems to be dynamic because of the nature of the data set. It is more likely that of Logistic Regression may win if the relationship between features and target variable is mostly the linear one, but Random Forest Classifier might possibly win the race if the relationship is nonlinear or there are complex relationships between features.

3. Suggest on different methods to improve your models. E.g. Remove/add data? If so, which features would you build on? Think about visualising the data first and seeing which features do not help with the prediction.

To improve model performance, several strategies can be employed:To improve model performance, several strategies can be employed:


Feature Engineering: The data science process contains creating new features or changing the existing ones to get a better insight on the underlying relationships within the data.

Feature Selection: Make the distinctions between noise and critical factors that do not matter and that matter a lot. This can be executed through methods such as the correlation analysis or feature significance estimation, for instance.

Hyperparameter Tuning: Develop the parameters of the models well so to increase their precision. For Random Forest Classifier a few tweaks in number of trees, depth of tree and rest parameters may be required.

Cross-validation: Integrate learning techniques, such as k-fold cross-validation, which will aid in accurately estimating model performance across real-world scenarios, with the goal of minimizing overfitting.

Ensemble Methods: Merge multiple models, for instance, differeny classification algorithms, to take benefits of their powers and clean up performance.

Through the systematic investigation of these techniques and the selection of different artefacts, we may eventually reach the model that can classify our data set more accurately.
"""