from flask import Flask,render_template,request
import joblib
from tools import *


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    text_post = request.form.get('post')

    clean_post = cleanData(text_post)
    clean_post=[clean_post]
    type = type_prediction(clean_post,model_EI,model_NS,model_TF,model_PJ)

    return render_template('index.html', prediction_text='MBTI type: {}'.format(type))

if __name__ == '__main__':
    model_EI=joblib.load('models/model_EI.joblib')
    model_NS=joblib.load('models/model_NS.joblib')
    model_TF=joblib.load('models/model_TF.joblib')
    model_PJ=joblib.load('models/model_PJ.joblib')
    app.run(debug=True)
