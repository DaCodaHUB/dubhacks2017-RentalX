#!flask/bin/python
from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
app = Flask(__name__)

languages = [{'name': 'helloworld'}]

data_file = pd.read_csv('/Users/ktran035/Google Drive/dubhack2017/server/sheet.csv', header=None)
# print("what is data",np.array(data_file))
data = np.array(data_file);
# print("y", data[1:, 6:].flatten())
# print("X", data[1:, :6])
X, y = data[1:,:6], data[1:, 6:].flatten()
print(OneVsRestClassifier(LinearSVC(C=100.)).fit(X, y).predict([[22,0.95,0,1,0.8,1],[25,0.8,0,1,0.8,1]]))
# logistic.predict([22,0.95,0,1,0.8,1])
@app.route('/<string:age>/<string:positive>', methods=['GET'])
def returnAll(age, positive):
	# print("data", data_file["travel"])
	return jsonify({'age': age, 'positive': positive})

if __name__ == '__main__':
	app.run(debug=True, port=3000)