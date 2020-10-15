from flask import Flask, request, render_template
import pandas as pd
import pickle

#create a Flask app
app = Flask(__name__)

#load model
with open('model.p', 'rb') as file:
    model = pickle.load(file)

#create a route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = {'bedrooms':int(request.form.get('bedrooms')),
                'bathrooms':int(request.form.get('bathrooms')), 
                'floorsize':int(request.form.get('floorsize')), 
                'zipcode':int(request.form.get('zipcode'))}
        print(data)
        df = pd.DataFrame(data, index=[0])
        with open('cities.p', 'rb') as file:
            cities = pickle.load(file)
        for city in cities:
            df['city_'+city] = 0 if city==request.form.get('city') else 0
        print(df)
        return render_template('website.html', price="$"+str(model.predict(df)[0]))
    return render_template('website.html', price='')

if __name__ == '__main__':
    app.run(port=2000, debug=True)