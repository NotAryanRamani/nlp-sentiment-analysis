from flask import render_template, request, redirect, url_for, flash, session, jsonify
from webapp import app

from src.pipeline.predict_pipeline import PredictPipeline
predict_model = PredictPipeline()
print('done')


@app.route('/')
def home_page():
    return redirect(url_for('predict'))


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        text = request.form.get('user_input')
        predictions = predict_model.get_predictions(text)
    return render_template('index.html', prediction_text=predictions, input_text=text)
