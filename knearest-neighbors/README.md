# Knearest Neighbors

## Background

The k-Nearest Neighbors classification algorithm is a non-parametric machine learning algorithm that classifies new data based by finding its k nearest neighbors in the data set, and choosing the classification that is represented the most.

## Task

Create a program that will classify a series of information a person is diabetic or not.

## Input

The program must read the data from the data folder named diabetes.csv. Diabetes.csv contains the training data for knearest neighbor. It has columns of no. of pregnancies, Glucose value, Blood Pressure, Skin Thickness, Insulin value, BMI, Diabetes Pedigree Function, Age, and Outcome (Class Variable). It is a labelled dataset the last column (output/class variable) signifies if the patient has diabetes with 1 while does who are not are is given a label 0. The program must read input.in. Input.in contains unlabelled data points.

The dataset is taken from this site: https://www.kaggle.com/mathchi/diabetes-data-set
You are NOT ALLOWED to use built in knearest neighbor algorithms. You must implement them all by scratch.

## Required Output

The output of the program is a text file named output.txt which contains the values from input.in and their corresponding output/class variables/labels

Example Output (output.txt):

3.0,70.0,34.0,31.0,77.0,31.0,0.59,24.0,Diabetic

4.0,135.0,91.0,0.0,33.0,34.6,0.19,25.0,Non-Diabetic

8.0,140.0,80.0,0.0,0.0,23.1,1.85,49.0,Non-Diabetic
