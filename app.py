import sass

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import FormField, RadioField, SubmitField
from wtforms.validators import AnyOf, DataRequired, Length

from pprint import pprint

from models.horse_genes import AgoutiGene

app = Flask(__name__)
app.secret_key = 'temporary' # TODO factor this out to a separate file

# Compile SASS styles
sass.compile(dirname=('static/sass/', 'static/css/'))

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

# class GeneGroupForm(FlaskForm):
#     # TODO Render these using a generated list of genes, not manually

#     def __init__(self, prefix):
#         super()
#         self.prefix = prefix

#         # Each gene requires a pair of alleles
#         self.firstAllele = FormField(AlleleForm, name=("{}-first".format(self.prefix)), label="X_")
#         self.secondAllele = FormField(AlleleForm, name="agoutiSecond", label="_X")


#         self.submit = SubmitField('Submit')

class GeneForm(FlaskForm):

    # def __init__(self, groups):
    #     super(GeneForm, self).__init__(self)
    groups = ['agouti']
    firstAlleles = []
    secondAlleles = []
    fields = []

    for i in range(len(groups)):
        fields.append(FormField(AlleleForm, name=(str(groups[i]) + '-first'), extra_classes="testing-class", label="X_"))
        # firstAlleles.append(FormField(AlleleForm, name=(str(groups[i])+'-first'), label="X_"))
        # secondAlleles.append(FormField(AlleleForm, name=(str(groups[i])+'-second'), label="_X"))
    
    submit = SubmitField('Submit')





# TODO this is VERY TEMPORARY and should be implemented better later
# agoutiForm = GeneGroupForm('agouti')
geneList = ['agouti']



@app.route("/", methods=['GET', 'POST'])
def hello_world():

    form = GeneForm()



    # Generate phenotype value
    phenotype = ''



    if form.validate_on_submit():
        # pprint(dir(form))
        pprint(form.fields[0].kwargs)
        # firstVal = form.firstAlleles[0].alleleField.data
        # secondVal = form.secondAlleles[0].alleleField.data

        # firstVal = form.groups[0].firstAllele.alleleField.data
        # secondVal = form.groups[0].secondAllele.alleleField.data
        # phenotype = firstVal + secondVal

    return render_template('index.html', form=form, phenotype=phenotype)