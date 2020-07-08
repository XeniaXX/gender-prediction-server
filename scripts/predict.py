#!flask/bin/python
from flask import Flask, jsonify
import pandas as pd
import joblib


app = Flask(__name__)


filename = '/Users/Xenia/todo-api/final_model.sav'
loaded_model = joblib.load(filename)
data = pd.read_csv("/Users/Xenia/todo-api/product")

from flask import abort
@app.route('/todo/api/v1.0/data/<string:session_id>', methods=['GET'])

def predict_function(session_id):
    ex=data[data.session_id=='u25001']
    ex1=ex.iloc[:,2:6]
    ex_size=ex1.shape
    for i in range(0,ex_size[0]):
        for j in range(0,ex_size[1]):
            ex1.values[i][j]= ex1.values[i][j].lstrip('ABCD')

    pred_ex=loaded_model.predict(ex1)
    count_1=0
    count_0=0
    for b in pred_ex:
        if b==0:
            count_0=count_0+1
        else:
            count_1=count_1+1

    if count_0>count_1:
            gender_ex='male'
    else:
            gender_ex='female'
    return jsonify({'predicted gender is ': gender_ex})





from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
