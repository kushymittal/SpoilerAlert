from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn.pipeline import Pipeline

import plotly.plotly as py 
import plotly.graph_objs as go

import json
import numpy as np

import pickle

def load_data(filename):
    """
    read json data from file
    @param filename The file to read from
    """
    json_data = None
    with open(filename, 'r') as data_file:
        json_data = json.loads(data_file.read())
    
    data = np.array([json_data[i]['data'] for i in range(len(json_data))])
    return data

if __name__ == '__main__':
    spoiler_data = load_data('spoilers.json')
    other_data = load_data('not_spoilers.json')

    test_size_x = []
    test_accuracy_y = []

    for i in range(24, 25):
        test_size = float(i) / 100

        # split data into training and testing sets
        spoiler_data_train, spoiler_data_test = train_test_split(spoiler_data, test_size=test_size)
        other_data_train, other_data_test = train_test_split(other_data, test_size=test_size)

        # extract features from training text
        count_vect = CountVectorizer()
        x_train_counts = count_vect.fit_transform(np.append(spoiler_data_train, other_data_train))
        tfidf_transformer = TfidfTransformer()
        x_train_tf = tfidf_transformer.fit_transform(x_train_counts)

        # Naive Bayes classifier
        train_labels = np.array([1]*len(spoiler_data_train) + [0]*len(other_data_train))
        test_labels = np.array([1]*len(spoiler_data_test) + [0]*len(other_data_test))
        nb_clf = MultinomialNB().fit(x_train_tf, train_labels)

        # SVM Classifier
        svm_clf = Pipeline([('vect', CountVectorizer()),
                            ('tfidf', TfidfTransformer()),
                            ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                                    alpha=1e-3, random_state=42,
                                                    max_iter=5, tol=None)),
        ])

        search_params = True

        if search_params:
            # Grid Search for parameter tuning
            parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
                            'tfidf__use_idf': (True, False),
                            'clf__alpha': (1e-2, 1e-3)}

            gs_train = np.append(spoiler_data_train, other_data_train)
            gs_labels = [1]*len(spoiler_data_train) + [0]*len(other_data_train)

            gs_clf = GridSearchCV(svm_clf, parameters, n_jobs=1)
            gs_clf = gs_clf.fit(gs_train, gs_labels)    

            pickle.dump(gs_clf, open('model.sav', 'wb'))

            predicted_spoilers = gs_clf.predict(spoiler_data_test)
            predicted_other = gs_clf.predict(other_data_test)
            predicted_labels = np.append(predicted_spoilers, predicted_other)

            # Result Metrics
            print 'Classification Report\n', metrics.classification_report(test_labels, predicted_labels)
            print 'Confusion Matrix\n', metrics.confusion_matrix(test_labels, predicted_labels)

            accuracy = metrics.accuracy_score(test_labels, predicted_labels)

            test_size_x.append(test_size)
            test_accuracy_y.append(accuracy)

            print test_size, accuracy

    trace = go.Scatter(
        x = test_size_x,
        y = test_accuracy_y
    )
    data = [trace]
    py.plot(data)





