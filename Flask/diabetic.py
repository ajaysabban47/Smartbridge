from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__) #your application
ran=pickle.load(open('diabetic.pkl','rb'))


@app.route('/') # default route
def home():
    return render_template("diabetic.html")


@app.route('/predict',methods=['post'])
def predict():
    Pregnancies=float(request.form['Pregnancies'])
    Glucose=float(request.form['Glucose'])
    BloodPressure=float(request.form['BloodPressure'])
    SkinThickness=float(request.form['SkinThickness'])
    Insulin=float(request.form['Insulin'])
    BMI=float(request.form['BMI'])
    DiabetesPedigreeFunction=float(request.form['DiabetesPedigreeFunction'])
    Age=float(request.form['Age'])
    
    print(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    a=np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
    result=ran.predict(a)
    if(result == 1):
        output = "Tested positive"
        print("Tested Positive")
    else:
        output = "Tested negative"
        print("Tested Negative")
    
    return render_template('diabetic.html',prediction_text= output)

if __name__ == '__main__':
    app.run(port=8000) # you are running your app