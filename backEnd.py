import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer


dataset = pd.read_csv('twitter_training.csv', nrows = 10000)

def model(dataset, input):
    
    parsedDb = dataset
        
    if input in list(dataset.iloc[:, 1]):
        Answerkey = dataset.iloc[:, 0].unique() # Extract unique values from column 0
        Column = dataset.iloc[:, 1] # Extract unique values from column 1
    else:
        Answerkey = dataset.iloc[:, 0].unique() # Extract unique values from column 0
        Column = dataset.iloc[:, 1] # Extract unique values from column 1

    vectorizer = CountVectorizer()
    tokenized_posts = vectorizer.fit_transform(Column.astype('U'))
    tokenized_posts = tokenized_posts.toarray()

    # Appending the vectorized questions to the dataset
    tokenized_questions_df = pd.DataFrame(tokenized_posts, columns=vectorizer.get_feature_names_out())

    parsedDb['QuestionTokenized'] = tokenized_questions_df.values.tolist()

    keyCol = []
    for i in range(len(dataset.iloc[:,0])):
        ans = dataset.iloc[:,0][i]

        for j in range(len(Answerkey)):
            if ans == Answerkey[j]:
                index = j

        keyCol.append(index)

    parsedDb['AnswerTokenized'] = keyCol

    y_train = parsedDb['AnswerTokenized'].to_list()

    x_train_vec = parsedDb['QuestionTokenized'].to_list()

    # Import and train a Multinomial Naive Bayes classifier
    model = MultinomialNB()
    model.fit(x_train_vec, y_train)

    input =  vectorizer.transform([input])
    prediction = model.predict(input)

    # Make predictions on the test set
    return(Answerkey[prediction])

#Test function
#print(model(dataset, "Rock-Hard La Varlope, RARE & POWERFUL, HANDSOME JACKPOT, Borderlands 3 (Xbox) dlvr.it/RMTrgF  "))