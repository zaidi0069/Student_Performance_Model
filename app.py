import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) if i != 2 else x for i, x in enumerate(request.form.values())]
    features[2] = 1 if features[2].lower() == 'yes' else 0
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return render_template("index.html", prediction_text="Student Performance Index is: {}".format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)