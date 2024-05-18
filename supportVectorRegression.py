# Support Vector Regression model 

# Importing the model from Sci-Kit Learn
from sklearn import svm

# Splitting the data into the inputs (x) and outputs (y).
x = dataset['question_tokenized'].to_list()
y = dataset['AnswerKey'].to_list()

# Creating an instance of the model
model = svm.SVR()
# Fitting the model to the data
model.fit(x,y)

# Running a model prediction on the thrid question in the dataset
print(model.predict([x[2]]))
