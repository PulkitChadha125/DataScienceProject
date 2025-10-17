from flask import Flask,request,jsonify,render_template
import os
import numpy as np
import pandas as pd
from src.datascienceproject.pipeline.prediction_pipeline import PredictionPipeline

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/train',methods=['GET'])
def training():
    os.system("python main.py")
    return 'Training completed successfully'


@app.route('/predict',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            fixed_acidity=float(request.form['fixed_acidity'])
            volatile_acidity=float(request.form['volatile_acidity'])
            citric_acid=float(request.form['citric_acid'])
            residual_sugar=float(request.form['residual_sugar'])
            chlorides=float(request.form['chlorides'])
            free_sulfur_dioxide=float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide=float(request.form['total_sulfur_dioxide'])
            density=float(request.form['density'])
            pH=float(request.form['pH'])
            sulphates=float(request.form['sulphates'])
            alcohol=float(request.form['alcohol'])
            data=[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            final_data=np.array(data).reshape(1,11)
            object=PredictionPipeline()
            prediction=object.predict(final_data)
            return render_template('results.html',prediction=f"The predicted quality of the wine is {str(prediction)}")
        except Exception as e:
            return "Something went wrong"
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
