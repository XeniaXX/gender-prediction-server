from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class View(FlaskForm):
    session_id = StringField('session_id', validators=[DataRequired()])
    parameter = StringField('parameter', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Predict(FlaskForm):
    session_id = StringField('session_id', validators=[DataRequired()])
    submit = SubmitField('Predict')
