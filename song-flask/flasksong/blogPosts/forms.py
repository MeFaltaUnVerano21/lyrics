from flask_wtf import FlaskForm
from sqlalchemy.sql.elements import RollbackToSavepointClause
from wtforms import StringField , SubmitField , TextAreaField
from wtforms.validators import DataRequired

class BlogPostInfo(FlaskForm):
        title = StringField( 'Song title' , validators=[DataRequired()])
        text = TextAreaField( 'Lyrics' , validators=[DataRequired()])
        submit = SubmitField( ' post')

class Search(FlaskForm):
        text = TextAreaField( 'text' , validators=[DataRequired()])
        submit = SubmitField( 'Search')
        