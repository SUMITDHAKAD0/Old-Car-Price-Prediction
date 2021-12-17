from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model1.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    #Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        #Kilometers_Driven=int(request.form['Kilometers_Driven'])
        Engine=float(request.form['Engine(CC)'])
        #ine(CC)=np.log(Engine(CC))
        Power=float(request.form['Power(bhp)'])	
        Mileage=float(request.form['Mileage(km/kg)'])
        Seats=int(request.form['Seats'])	
        Owner_Type=int(request.form['Owner_Type'])
        Kilometers_Driven=int(request.form['Kilometers_Driven'])
        Fuel_Type_1=request.form['Fuel_Type_1']
        if(Fuel_Type_1=='Petrol'):
            Fuel_Type_1=3
        if(Fuel_Type_1=='Diesel'):
            Fuel_Type_1=1
        if(Fuel_Type_1=='CNG'):
            Fuel_Type_1=0        
        else:
            Fuel_Type_1=2
            
        #Year=2021-Year
        	
        Transmission_1=request.form['Transmission_1']
        if(Transmission_1=='Mannual'):
            Transmission_1=1
        else:
            Transmission_1=0

        Location_1=request.form['Location_1']
        if(Location_1=='Ahmedabad'):
            Location_1=0
        if(Location_1=='Bangalore'):
            Location_1=1
        if(Location_1=='Chennai'):
            Location_1=2      
        if(Location_1=='Coimbatore'):
            Location_1=3
        if(Location_1=='Delhi'):
            Location_1=4
        if(Location_1=='Hyderabad'):
            Location_1=5
        if(Location_1=='Jaipur'):
            Location_1=6
        if(Location_1=='Kochi'):
            Location_1=7
        if(Location_1=='Kolkata'):
            Location_1=8
        if(Location_1=='Mumbai'):
            Location_1=9              
        else:
            Location_1=10

        prediction=model.predict([[Year,Kilometers_Driven,Owner_Type,Seats,Mileage,Engine,Power,Location_1,Fuel_Type_1,Transmission_1]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

