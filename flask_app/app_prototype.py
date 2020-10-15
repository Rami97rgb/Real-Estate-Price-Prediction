from flask import Flask, request, jsonify
import pandas as pd
import pickle

#create a Flask app
app = Flask(__name__)

#load model
with open('model.p', 'rb') as file:
    model = pickle.load(file)

#create predict url
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data, index=[0])
    print(df)
    return jsonify(df.to_json())

if __name__ == '__main__':
    app.run(port=3000, debug=True)