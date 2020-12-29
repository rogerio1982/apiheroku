import os
from flask import Flask, jsonify, request, render_template
#import joblib
import pickle

import numpy as np


app = Flask(__name__)
#model = joblib.load(open('iris_trained_model.pkl', 'rb'))
model = pickle.load(open('iris_trained_model2.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features).astype(int)]
    prediction = model.predict(final_features)

    output = prediction[0]

    return render_template('index.html', prediction_text=' Iris Flower category is {}'.format(output))

@app.route('/api',methods=['POST'])
def api():
        posted_data = request.get_json()
        sepal_length = posted_data['sepal_length']
        sepal_width = posted_data['sepal_width']
        petal_length = posted_data['petal_length']
        petal_width = posted_data['petal_width']

        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
        if prediction == 0:
            predicted_class = 'Iris-setosa'
        elif prediction == 1:
            predicted_class = 'Iris-versicolor'
        else:
            predicted_class = 'Iris-virginica'

        return jsonify({
            'Prediction': predicted_class
        })

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(port = 5000, debug=True)

