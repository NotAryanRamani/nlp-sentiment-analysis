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
    preds = ''
    text = ''
    if request.method == 'POST':
        text = request.form.get('user_input')
        predictions = predict_model.get_predictions(text)
        for model, prediction in predictions.items():
            preds += f'{model} : {str(prediction[0])}'
            c = ',  ' if model == 'LogisticRegression' else ' '
            preds += c
    return render_template('index.html', prediction_text=preds, input_text=text)


@app.route('/predict-api', methods=['POST'])
def predict_api():
    data = request.json['data']
    text = data['text']
    predictions = predict_model.get_predictions(text)
    predictions = { model:str(prediction[0]) for model, prediction in predictions.items()}
    return jsonify(predictions)

