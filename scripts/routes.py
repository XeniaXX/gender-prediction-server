from app import app
from flask import render_template, url_for, flash, get_flashed_messages, redirect, request
from datetime import datetime
from db import *
import forms
import re


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/view', methods=['GET', 'POST'])
def view():
    form = forms.View()
    session_id = form.session_id.data
    if form.validate_on_submit():
        p = int(form.parameter.data)
        task = engine.execute('''SELECT * FROM views WHERE session_id=(?)''',(session_id,)).fetchall()
        if len(task) == 0:
              flash('no such session_id ')
        if p==1:
            return render_template('answer_view.html',result=task[0],parameter=p)
        elif p==2:
            t1=list(task[0])
            temp=t1[1:5]
            s=sum(temp)
            t2=[t1[0]]
            for i in range(0,4):
                t2.append(temp[i]/s*100)
            return render_template('answer_view.html', result=t2, parameter=p)
        else:
            flash('no such parameter ')
            #return redirect(url_for('index'))
    return render_template('view.html', form=form)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = forms.Predict()
    session_id = form.session_id.data
    if form.validate_on_submit():
        try:
            res=predict_function(session_id)
            return render_template('answer_predict.html',result=res)
        except:
            flash('There is no such session_id')                   
    return render_template('predict.html', form=form)


