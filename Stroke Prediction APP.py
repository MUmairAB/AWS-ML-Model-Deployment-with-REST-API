"""
This deploys a ML model in AWS Cloud for production.
It creates a FastAPI that accepts 7 features about the patient and 
predicts whether the patient is vulnerable to stroke of not.

"""
#Import necessary libraries
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field
from typing import Literal
import numpy as np
import pickle

#Load the pre-trained model
model = pickle.load(open('trained_model.sav','rb'))

#Define a function to make prediction using the model
def stroke_classifier(user_input):
    # Convert 1D array to 2D features matrix
    X = np.array(user_input).reshape(1,-1)
    pred = model.predict(X)[0]
    if pred == 0:
        return("Congratulation! your brain stroke test result is negative")
    else:
        return("Unfortunately! your brain stroke test result is positive. Kindly consult a doctor!")

#Instantiate the app
app = FastAPI()

#Define the home function
@app.get("/")
async def home():
     return {"message": "Welcome to my AWS server for Stroke Prediction"}

#Define a class to get the patient data
class PatientData(BaseModel):
    #Gender vaues can be from the list only
    gender : Literal["Male","Female","Other"]

    #Age must be in the range [1,100]
    age : int = Field(ge=1, le=100)

    #Hypertension is a Boolean number
    hypertension : bool

    #Heart disease is also a Boolean
    heart : bool

    #Work type values can also be from the list
    work : Literal['Private Job', 'Self Employed','Govt. Job','Never Worked','You are a Child']

    #Average Glucose can be in the range [40, 400]
    glucose : float = Field(ge=40.0, le=400.0)

    #BMI 
    bmi : float = Field(ge=10.0, le=100.0)

@app.post("/predict")
async def str_pred(pdata: PatientData):
   
   #Convert the class object to a dictionary
   data_dict = pdata.dict()

   #Decode the Categorical Features into Numberical Values
   # This coding is defined while model training

   #                          Gender                    #
   if pdata.gender == 'Male':
        data_dict["gender"] = 0
   elif pdata.gender == 'Female':
        data_dict["gender"] = 1
   else:
        data_dict["gender"] = -1

   #                       Hypertension                #
   if pdata.hypertension == 'Yes':
        data_dict["hypertension"] = 1
   else:
        data_dict["hypertension"] = 0

   #                       Heart Disease               #
   if pdata.heart == 'Yes':
        data_dict["heart"] = 1
   else:
        data_dict["heart"] = 0
   
   #                         Work Type                 #
   if pdata.work == 'Private Job':
        data_dict["work"] = 0
   elif pdata.work == 'Self Employed':
        data_dict["work"] = 1
   elif pdata.work == 'Govt. Job':
        data_dict["work"] = 2
   elif pdata.work == 'Never Worked':
        data_dict["work"] = -2
   elif pdata.work == 'You are a Child':
        data_dict["work"] = -1


    ########   Converting the user input to an array   ############
   
   arr = [data_dict["gender"],data_dict["age"],data_dict["hypertension"],data_dict["heart"],data_dict["work"],data_dict["glucose"],data_dict["bmi"]]
   
   return {"message":stroke_classifier(arr)}

#Define the main function
if __name__ == "__main__":
    uvicorn.run(app="Stroke Prediction APP:app",
                host="0.0.0.0",
                port=8080,
                reload=True)