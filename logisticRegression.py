# Logistic Regression

# Importing the linear model module from Sci-Kit Learn
from sklearn import linear_model

# Splitting the data into the inputs (x) and outputs (y).
x = dataset['question_tokenized'].to_list()
y = dataset['AnswerKey'].to_list()

# Creating an instance of the model
model = linear_model.LogisticRegression()
# Fitting the model to the data
model.fit(x, y)

# Running a model prediction on the third question in the dataset
print(model.predict([x[2]]))
