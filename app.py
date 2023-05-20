from flask import Flask, render_template, request,send_file, url_for
import pickle
import pandas as pd
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

app = Flask(__name__,template_folder='templates')
model=pickle.load(open('dsm.pkl','rb'))




@app.route('/')
def main():
    return render_template('index.html')
# Define route for prediction
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get user input for start and end dates
        name = float(request.form['name'])
        hardness = float(request.form['hardness'])
        solids = float(request.form['solids'])
        chloramines = float(request.form['Chloramines'])
        sulfate = float(request.form['sulfate'])
        conductivity = float(request.form['conductivity'])
        carbon = float(request.form['carbon'])
        trihalomethanes = float(request.form['trihalomethanes'])
        turbidity = float(request.form['turbidity'])
        input=[]
        input_in=[name,hardness,solids,chloramines,sulfate,conductivity,carbon,trihalomethanes,turbidity]
        input.append(input_in)
        
        prediction = model.predict(input)
        predic=""
        if(prediction[0]==1):
            predic="Fit"
        else:
            predic="Unifit"
        return render_template('index.html', prediction=predic)

if __name__ == '__main__':
    app.run(debug=True)