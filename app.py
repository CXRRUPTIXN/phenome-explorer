from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import FormField, RadioField, SubmitField
from wtforms.validators import AnyOf, DataRequired, Length

from models.horse_genes import AgoutiGene

app = Flask(__name__)
app.secret_key = 'temporary' # TODO factor this out to a separate file

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

testGene = AgoutiGene()

class AlleleForm(FlaskForm):
    alleleField = RadioField(
        'Agouti Gene:',
        # Agouti gene is always present, answer may not be None
        validators = [AnyOf([a.value for a in AgoutiGene.Alleles], message="Must select a value!")],
        choices    = [a.value for a in AgoutiGene.Alleles]
    )

class GeneForm(FlaskForm):
    # TODO Render these using a generated list of genes, not manually

    # Each gene requires a pair of alleles
    firstAllele = FormField(AlleleForm, name="firstAllele", label="X_")
    secondAllele = FormField(AlleleForm, name="secondAllele", label="_X")


    submit = SubmitField('Submit')

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    form = GeneForm()

    # Generate phenotype value
    phenotype = ''
    if form.validate_on_submit():
        firstVal = form.firstAllele.alleleField.data
        secondVal = form.secondAllele.alleleField.data
        phenotype = firstVal + secondVal

    return render_template('index.html', form=form, phenotype=phenotype)