# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:31:37 2021

@author: Brij.Singh
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger
from flask import jsonify

app=Flask(__name__)
Swagger(app)
pickle_in=open('random.pkl','rb')
random=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"


@app.route('/predict-cover',methods=["Get"])
def predict_forest_cover_type():
    """Let's find the forest cover from the specifications
    ---
    parameters:
      - in: query
        name: Elevation
        type: number
        required: true
      - in: query
        name: Aspect
        type: number
        required: true
      - in: query
        name: Slope
        type: number
        required: true
      - in: query
        name: Horizontal_Distance_To_Hydrology
        type: number
        required: true
      - in: query
        name: Vertical_Distance_To_Hydrology
        type: number
        required: true
      - in: query
        name: Horizontal_Distance_To_Roadways
        type: number
        required: true
      - in: query
        name: Hillshade_9am
        type: number
        required: true
      - in: query
        name: Hillshade_Noon
        type: number
        required: true
      - in: query
        name: Hillshade_3pm
        type: number
        required: true
      - in: query
        name: Horizontal_Distance_To_Fire_Points
        type: number
        required: true
      - in: query
        name: Wilderness_Area1
        type: number
        required: true
      - in: query
        name: Wilderness_Area2
        type: number
        required: true
      - in: query
        name: Wilderness_Area3
        type: number
        required: true
      - in: query
        name: Wilderness_Area4
        type: number
        required: true
      - in: query
        name: Soil_Type1
        type: number
        required: true
      - in: query
        name: Soil_Type2
        type: number
        required: true
      - in: query
        name: Soil_Type3
        type: number
        required: true
      - in: query
        name: Soil_Type4
        type: number
        required: true
      - in: query
        name: Soil_Type5
        type: number
        required: true
      - in: query
        name: Soil_Type6
        type: number
        required: true
      - in: query
        name: Soil_Type7
        type: number
        required: true
      - in: query
        name: Soil_Type8
        type: number
        required: true
      - in: query
        name: Soil_Type9
        type: number
        required: true
      - in: query
        name: Soil_Type10
        type: number
        required: true
      - in: query
        name: Soil_Type11
        type: number
        required: true
      - in: query
        name: Soil_Type12
        type: number
        required: true
      - in: query
        name: Soil_Type13
        type: number
        required: true
      - in: query
        name: Soil_Type14
        type: number
        required: true
      - in: query
        name: Soil_Type15
        type: number
        required: true
      - in: query
        name: Soil_Type16
        type: number
        required: true
      - in: query
        name: Soil_Type17
        type: number
        required: true
      - in: query
        name: Soil_Type18
        type: number
        required: true
      - in: query
        name: Soil_Type19
        type: number
        required: true
      - in: query
        name: Soil_Type20
        type: number
        required: true
      - in: query
        name: Soil_Type21
        type: number
        required: true
      - in: query
        name: Soil_Type22
        type: number
        required: true
      - in: query
        name: Soil_Type23
        type: number
        required: true
      - in: query
        name: Soil_Type24
        type: number
        required: true
      - in: query
        name: Soil_Type25
        type: number
        required: true
      - in: query
        name: Soil_Type26
        type: number
        required: true
      - in: query
        name: Soil_Type27
        type: number
        required: true
      - in: query
        name: Soil_Type28
        type: number
        required: true
      - in: query
        name: Soil_Type29
        type: number
        required: true
      - in: query
        name: Soil_Type30
        type: number
        required: true
      - in: query
        name: Soil_Type31
        type: number
        required: true
      - in: query
        name: Soil_Type32
        type: number
        required: true
      - in: query
        name: Soil_Type33
        type: number
        required: true
      - in: query
        name: Soil_Type34
        type: number
        required: true
      - in: query
        name: Soil_Type35
        type: number
        required: true
      - in: query
        name: Soil_Type36
        type: number
        required: true
      - in: query
        name: Soil_Type37
        type: number
        required: true
      - in: query
        name: Soil_Type38
        type: number
        required: true
      - in: query
        name: Soil_Type39
        type: number
        required: true
      - in: query
        name: Soil_Type40
        type: number
        required: true
      

        
    responses:
        200:
            description: the output values
              
    """

        

    Elevation=request.args.get('Elevation')
    Aspect=request.args.get('Aspect')
    Slope=request.args.get('Slope')
    Horizontal_Distance_To_Hydrology=request.args.get('Horizontal_Distance_To_Hydrology')
    Vertical_Distance_To_Hydrology=request.args.get('Vertical_Distance_To_Hydrology')
    Horizontal_Distance_To_Roadways=request.args.get('Horizontal_Distance_To_Roadways')
    Hillshade_9am=request.args.get('Hillshade_9am')
    Hillshade_Noon=request.args.get('Hillshade_Noon')
    Hillshade_3pm=request.args.get('Hillshade_3pm')
    Horizontal_Distance_To_Fire_Points=request.args.get('Horizontal_Distance_To_Fire_Points')
    Wilderness_Area1=request.args.get('Wilderness_Area1')
    Wilderness_Area2=request.args.get('Wilderness_Area2')
    Wilderness_Area3=request.args.get('Wilderness_Area3')
    Wilderness_Area4=request.args.get('Wilderness_Area4')
    Soil_Type1=request.args.get('Soil_Type1')
    Soil_Type2=request.args.get('Soil_Type2')
    Soil_Type3=request.args.get('Soil_Type3')
    Soil_Type4=request.args.get('Soil_Type4')
    Soil_Type5=request.args.get('Soil_Type5')
    Soil_Type6=request.args.get('Soil_Type6')
    Soil_Type7=request.args.get('Soil_Type7')
    Soil_Type8=request.args.get('Soil_Type8')
    Soil_Type9=request.args.get('Soil_Type9')
    Soil_Type10=request.args.get('Soil_Type10')
    Soil_Type11=request.args.get('Soil_Type11')
    Soil_Type12=request.args.get('Soil_Type12')
    Soil_Type13=request.args.get('Soil_Type13')
    Soil_Type14=request.args.get('Soil_Type14')
    Soil_Type15=request.args.get('Soil_Type15')
    Soil_Type16=request.args.get('Soil_Type16')
    Soil_Type17=request.args.get('Soil_Type17')
    Soil_Type18=request.args.get('Soil_Type18')
    Soil_Type19=request.args.get('Soil_Type19')
    Soil_Type20=request.args.get('Soil_Type20')
    Soil_Type21=request.args.get('Soil_Type21')
    Soil_Type22=request.args.get('Soil_Type22')
    Soil_Type23=request.args.get('Soil_Type23')
    Soil_Type24=request.args.get('Soil_Type24')
    Soil_Type25=request.args.get('Soil_Type25')
    Soil_Type26=request.args.get('Soil_Type26')
    Soil_Type27=request.args.get('Soil_Type27')
    Soil_Type28=request.args.get('Soil_Type28')
    Soil_Type29=request.args.get('Soil_Type29')
    Soil_Type30=request.args.get('Soil_Type30')
    Soil_Type31=request.args.get('Soil_Type31')
    Soil_Type32=request.args.get('Soil_Type32')
    Soil_Type33=request.args.get('Soil_Type33')
    Soil_Type34=request.args.get('Soil_Type34')
    Soil_Type35=request.args.get('Soil_Type35')
    Soil_Type36=request.args.get('Soil_Type36')
    Soil_Type37=request.args.get('Soil_Type37')
    Soil_Type38=request.args.get('Soil_Type38')
    Soil_Type39=request.args.get('Soil_Type39')
    Soil_Type40=request.args.get('Soil_Type40')
    prediction=random.predict([[Elevation,Aspect,Slope,Horizontal_Distance_To_Hydrology,Vertical_Distance_To_Hydrology,Horizontal_Distance_To_Roadways,Hillshade_9am,Hillshade_Noon,Hillshade_3pm,Horizontal_Distance_To_Fire_Points,Wilderness_Area1,Wilderness_Area2,Wilderness_Area3,Wilderness_Area4,Soil_Type1,Soil_Type2,Soil_Type3,Soil_Type4,Soil_Type5,Soil_Type6,Soil_Type7,Soil_Type8,Soil_Type9,Soil_Type10,Soil_Type11,Soil_Type12,Soil_Type13,Soil_Type14,Soil_Type15,Soil_Type16,Soil_Type17,Soil_Type18,Soil_Type19,Soil_Type20,Soil_Type21,Soil_Type22,Soil_Type23,Soil_Type24,Soil_Type25,Soil_Type26,Soil_Type27,Soil_Type28,Soil_Type29,Soil_Type30,Soil_Type31,Soil_Type32,Soil_Type33,Soil_Type34,Soil_Type35,Soil_Type36,Soil_Type37,Soil_Type38,Soil_Type39,Soil_Type40]])
    return "The predicted value is "+ str(prediction)


@app.route('/predict-cover-file',methods=["POST"])
def predict_forest_cover_type_file():
    """Let's find the forest cover from specifications
    This is using docstrings
    ---
    parameters:
      - in: formdata
        name: file
        type: file
        required: true
        
    responses:
        200:
            description: the output values
              
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=random.predict(df_test)
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000) 
