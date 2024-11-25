from flask import Flask, request, render_template
from API import get_prediction

app = Flask(__name__)


model_path = "Malicious_URL_Prediction.h5"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        prediction = get_prediction(url, model_path)
        return render_template('result.html', prediction=prediction, url=url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
