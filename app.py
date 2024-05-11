from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

from models.horse_genes import AgoutiGene

app = Flask(__name__)
app.secret_key = 'temporary' # TODO factor this out to a separate file

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

testGene = AgoutiGene()

class GeneForm(FlaskForm):
    name = StringField('Which actor is your favorite?', validators=[DataRequired(), Length(10, 40)])
    submit = SubmitField('Submit')

@app.route("/")
def hello_world():
    form = GeneForm()
    # return '<h1>' + testGene.geneString + '</h1>'
    return render_template('index.html', form=form)