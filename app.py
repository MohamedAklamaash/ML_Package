from flask import Flask,render_template,request
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import CustomDataClass,PredictPipeline

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
    if request.method == "GET":
        return render_template(
            "home.html"
        )
    else:
        data = CustomDataClass(
            gender = request.form.get("gender"),
            lunch=request.form.get("lunch"),
            race_ethinicity=request.form.get("ethnicity"),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            reading_score=float(request.form.get("reading_score")),
            test_preparation_course= request.form.get("test_preparation_course"),
            writing_score= request.form.get("writing_score")
        )

        pred_df = data.get_data_as_frame()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        res = predict_pipeline.predict(pred_df)
        return render_template("home.html",results=res[0])
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)