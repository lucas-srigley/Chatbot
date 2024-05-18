# Bayesian Ridge Regression model 

# Importing the model from Sci-Kit Learn
from sklearn import linear_model

# Splitting the data into the inputs (x) and outputs (y).
x = dataset['question_tokenized'].to_list()
y = dataset['AnswerKey'].to_list()

# Creating an instance of the model
model = linear_model.BayesianRidge()
# Fitting the model to the data
model.fit(x,y)

# Running a model prediction on the thrid question in the dataset
print(model.predict([x[2]]))
