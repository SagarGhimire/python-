# Student Performance in Exams 

## Introduction
    This project will look into the student datasets with gender, race, parental level of education and look into how does student performance is affected by these variables.
    The initial goal is to explore the datasets, predict the student's math's score and classify the data on the given attribute. I guess, Student performance depends on the gender, parental level of education but let's see what the machine learning technique will conculde.

## Technologies Used:
1. Python 3
2. Sypder
3. Pandas
4. skleran modules 
5. Mathplotlib

## Raw Data
For the project the Raw Data has been taken from Kaggle website. The used Datasets is [DataSet](https://www.kaggle.com/spscientist/students-performance-in-exams).
The datasets in the repository can be found at [RepoData](https://github.com/44-599-machine-learning-S19/machine-learning-project-SagarGhimire/blob/master/StudentsPerformance.csv)
Raw data read using Pandas can be found at  [RawData](https://github.com/44-599-machine-learning-S19/machine-learning-project-SagarGhimire/blob/master/initial_exploration.ipynb).

## Data
The notebook that explores the data can be found here:
The value mapping has been done and pandas has been used to read the dataset and some methods are used to map the value from string to numeric.
- [DataExploration](https://github.com/44-599-machine-learning-S19/machine-learning-project-SagarGhimire/blob/master/classification.ipynb)
- [DataExpo](https://github.com/44-599-machine-learning-S19/machine-learning-project-SagarGhimire/blob/master/Classification2.ipynb)

## Analysis
For the Analysis I have used some of the cool Machine Learning techniques. The pandas dataframe read the csv data and value mapping has been done to map the String value to numeric one.
The following Analysis has been done to Datasets.
#### [Linear Regression](https://github.com/44-599-machine-learning-S19/machine-learning-project-SagarGhimire/blob/master/linear_regression.ipynb)
- The first Analysis that has been done to the datasets is Linear Regression. The module is imported using sklearn library. Value mapping for the data has been done and the set has been splitted to train and test sets.
	Parent-level of Education and Math Score has been predicted but can predict 1.5% at a time. The writing score has been added to predict the Math score using Linear Regression.
	The R^2 has been increased to 82% from 1.5%. Also the Root Mean Square Error(RMSE) was 39 from 222, which is awesome. Also the validation in test sets gives 85% of R^2 value.

#### [Decision Tree](https://github.com/44-599-machine-learning-S19/machine-learning-project-SagarGhimire/blob/master/classification.ipynb)
- After Linear Regression, Decision tree method has been applied to dataset to predict the value. First, gender and average score has been visualized to predict the data.
The scatter plot doesn't seems good and that goes same for the parent_level and average score. But when reading and math score has been seen for male and female, the plot seems more better and can be found at above link.
#### [Support Vector Machine](https://github.com/44-599-machine-learning-S19/machine-learning-project-SagarGhimire/blob/master/classification.ipynb)
- The project used another classifier to see if we can do more better. From skleran SVM, rbf kernel is used to predict. The math score has been predicted from reading score and gender.
#### Metrices:
- The random test sets were generated using the method and the model has been cross validated. The metrices from Decision Tree and SVM for test and train set is tabulated below: 

|Methods        | Set   | Accuracy | Precision | Sensitivity| F1-score| 
----------------|-------|----------|-----------|------------|---------|
| Decision Tree | Train | 67.3%    | 69.9%     | 67.3%      | 67.2%   |
| Decision Tree | Test  | 83.86%   | 87%       | 83.86%     | 83.6%   |
| SVM           | Train | 26.8%    | 33.1%     | 26.8%      | 24.32%  | 
| SVM           | Test  | 41.8%    | 43.18%    | 41.8%      | 36.2%   |

Looking at the Analysis, The Decision Tree works great for train set with 67.3% Accuracy and 67.2% F1-score. The test set has high accuracy for 84% and F1 score for 83.6%.
But I guess, Decision tree usually overfit the model, So, SVM has been done. The Accuracy for Train set is 27% and F1 score with 24% whereas the test set has 42% Accuracy and F1-score with 36.2%.
Looking at SVM, the Decision tree has overfitted the model and SVM really performed bad in the model.

#### [PCA](https://github.com/44-599-machine-learning-S19/machine-learning-project-SagarGhimire/blob/master/Classification2.ipynb)
Looking at the decision tree and SVM, performed really bad. So, PCA has been applied to the datasets. This reduces the dimenisons and other related attributes and gives the good classification results. 
For this the knee has been found from the dataset, plotting the values using pyplot. After the knee has been found which is 2, and has been fitted. 
The [graph](https://github.com/44-599-machine-learning-S19/machine-learning-project-SagarGhimire/blob/master/Classification2.ipynb) shows that the two values can be classified with Y=0 line equation.
The graph shows 8 clusters of data classified with different color. I think PCA does really good job on classifying the data.

#### [Random Forest](https://github.com/44-599-machine-learning-S19/machine-learning-project-SagarGhimire/blob/master/Classification2.ipynb)
One more classifier is added, Random Forest Classifier from sklearn. The metrices has been computed and it seems like the score is the lowest of all about 5%.

#### Results:
Looking at all of these various classifier and predicition methods, for the given datasets, the decision tree and PCA works fine for train and test sets.
- The SVM and Random Forest Classifier doesn't work too good for this datasets. The first challenge I have faced for this project is to find the best classification to predict the score.
- The scatter matrix plot has worked fine and helps me easier to classify the data. Most of the data I want to predict is string so I have to map the values to integers to perform any listed method above. 
- Also generating test sets was challenging but the notes from lectures and homework has helped a lot. 
- I was hoping Parent level of Education would work great but the Linear Regression shows it won't work. Also the SVM and Random Forest Classifier didn't give the best result for the classification of the datasets.
- The limitation for my result is it can be overfitted. The Metrices for the validation is quite low, even the Linear Regression gives pretty good results.
- For the improvement, I guess more classifier could be used to train the model. I guess Neural Nets and Tensor Flow may work fine. 

## Conclusion:
- If you are good at Reading and Writing then the score you obtain in Math would be good one. Refer to this [link](https://github.com/44-599-machine-learning-S19/machine-learning-project-SagarGhimire/blob/master/Classification2.ipynb),the correlation score is pretty high for math score.
- Looking at the [Linear Regression](https://github.com/44-599-machine-learning-S19/machine-learning-project-SagarGhimire/blob/master/linear_regression.ipynb), R^2 value is pretty high for writing score to math score which favors the first result.
- In order to predict the score in Math, the decision tree would be good approach but you need to specify gender, parent level of education, ACT/SAT score, Reading score. The predicition can be 83% accurate as your data would be test set. 
- With PCA, the person can be classified in lower y-axis or higher y-axis, depending upon the gender, Reading and math score. 



 






