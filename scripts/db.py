#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:20:45 2020

@author: Xenia
"""
from sqlalchemy import create_engine
import joblib
import pandas as pd
#from flask import Flask, jsonify
  
# connecting to the database  
engine = create_engine('sqlite:////Users/Xenia/servers/flask app/views.sqlite')
  

# SQL command to create a table in the database 
sql_command = """DROP TABLE IF EXISTS views"""
engine.execute(sql_command)
sql_command = """CREATE TABLE views AS   
SELECT a.session_id, category_A, category_B, category_C, category_D, gender 
FROM 
(SELECT session_id 
,COUNT(distinct category_a) AS category_A 
,COUNT(distinct category_b) AS category_B 
,COUNT(distinct category_c) AS category_C 
,COUNT(distinct category_d) AS category_D 
FROM Product GROUP BY session_id) AS a JOIN Session
ON a.session_id=Session.session_id;"""
  
engine.execute(sql_command)
#t=engine.execute("SELECT * FROM  views WHERE session_id='u30687'").fetchall()
#t1=list(t[0])
#print(t1[0])
filename = '/Users/Xenia/Downloads/ds_project 8.45.56 AM/models/final_model.sav'
loaded_model = joblib.load(filename)

def predict_function(session_id):
    t=engine.execute('''SELECT session_id,sequence_order,category_a,category_b,category_c,category_d  FROM Product
                   WHERE session_id == ( ? )''',(session_id,)).fetchall()
    data = pd.DataFrame(data=t)
    print(data.head())
    ex1=data.iloc[:,2:6]
    ex_size=ex1.shape
    for i in range(0,ex_size[0]):
        for j in range(0,ex_size[1]):
            ex1.values[i][j]= ex1.values[i][j].lstrip('ABCD')

    pred_ex=loaded_model.predict(ex1)
    count_1=0
    count_0=0
    for b in pred_ex:
        if b==0:
            count_0=count_0+1
        else:
            count_1=count_1+1

    if count_0>count_1:
            gender_ex='male'
    else:
            gender_ex='female'
    return gender_ex
