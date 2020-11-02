# MBTI Prediction
:date: Creation date: October 2020

## :dart: Objective

The Myers–Briggs Type Indicator (MBTI) is an introspective self-report questionnaire indicating differing psychological preferences in how people perceive the world and make decisions. The test attempts to assign four categories:

 * introversion or extraversion
 * sensing or intuition
 * thinking or feeling
 * judging or perceiving
 
The goal was to create a web application that could predict the MBTI of a person with a text description.
The model is trained on the following dataset:
<a href="https://www.kaggle.com/datasnaek/mbti-type" target="_blank">https://www.kaggle.com/datasnaek/mbti-type</a>

## :male_detective:	Description

Once the web application is launched, the user should write the largest description of himself. After that, the user clicks on the "Prediction" button and the model returns the user MBTI profile.

## :robot: Installation
 1. Clone the repo
 
```
git clone https://github.com/pmecchia/mbti_prediction.git
```

 2. Download and Install dependencies
 
```
conda install -r requirements.txt
```

 3. Launch the web application
 
```
python app.py
```

 4. Access the application in a web browser

```
http://127.0.0.1:5000/
```
