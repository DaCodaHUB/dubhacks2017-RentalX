#!flask/bin/python
from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
app = Flask(__name__)

languages = [{'name': 'helloworld'}]

data_file = pd.read_csv('./sheet.csv', header=None)
# print("what is data",np.array(data_file))
data = np.array(data_file);
# print("y", data[1:, 6:].flatten())
# print("X", data[1:, :6])
X, y = data[1:,:6], data[1:, 6:].flatten()
classifier = LogisticRegression()
classifier.fit(X,y)
# classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1)
# classifier.fit(X,y)
# classfier = OneVsRestClassifier(LinearSVC(C=100.))
# classfier.fit(X,y);


# logistic.predict([22,0.95,0,1,0.8,1])
@app.route('/<string:age>/<string:positive>/<string:fuel>/<string:gender>/<string:sport>/<string:travel>', methods=['GET'])
def returnAll(age, positive, fuel, gender, sport, travel):
	return jsonify({'result': classifier.predict([[float(age), float(positive), float(fuel), float(gender), float(sport), float(travel)]])[0]})

if __name__ == '__main__':
	app.run(debug=True, port=3000)