import numpy as np
from flask import Flask,render_template,request
import joblib


app = Flask(__name__)

pred_EI=joblib.load('models/model_EI.joblib')
pred_NS=joblib.load('models/model_NS.joblib')
pred_TF=joblib.load('models/model_TF.joblib')
pred_PJ=joblib.load('models/model_PJ.joblib')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text_post = request.get_json()
    print(text_post)

    result_IE = pred_EI.predict(text_post)
    result_NS = pred_NS.predict(text_post)
    result_TF = pred_TF.predict(text_post)
    result_PJ = pred_PJ.predict(text_post)

    type = result_IE[0]+result_NS[0]+result_TF[0]+result_PJ[0]
    return render_template('index.html', prediction_text='MBTY type: $ {}'.format(type))
