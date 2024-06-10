import sass

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import Form, FormField, RadioField, SubmitField, FieldList
from wtforms.validators import AnyOf, DataRequired, Length

from pprint import pprint

from models.horse_genes import AgoutiGene

app = Flask(__name__)
app.secret_key = 'temporary' # TODO factor this out to a separate file

app.app_context().push()

# Compile SASS styles
sass.compile(dirname=('static/sass/', 'static/css/'))

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

testGene = AgoutiGene()


class AlleleForm(Form):
    # TODO make gene name/type not hard-coded

    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # self.name = name
    #     # self.options = options

    # name = 'fuck'
    firstAllele = RadioField(
        # 'Agouti Gene:',
        # # Agouti gene is always present, answer may not be None
        # validators = [AnyOf([a.value for a in AgoutiGene.Alleles], message="Must select a value!")],
        # validators = [AnyOf(self.options, message="Must select a value!")],
        choices = [],
        # validators = [AnyOf(choices, message="Must select a value!")],
        # choices    = [a.value for a in AgoutiGene.Alleles]
        label = 'First Allele'
    )
    secondAllele = RadioField(
        # 'Agouti Gene:',
        # # Agouti gene is always present, answer may not be None
        # validators = [AnyOf([a.value for a in AgoutiGene.Alleles], message="Must select a value!")],
        choices = [],
        # validators = [AnyOf(choices, message="Must select a value!")],
        # choices    = [a.value for a in AgoutiGene.Alleles]
        label = 'Second Allele'
    )

    #     self.firstAllele.choices = options
    #     self.secondAllele.choices = options


# class GeneGroupForm(FlaskForm):
#     # TODO Render these using a generated list of genes, not manually

#     def __init__(self, prefix):
#         super()
#         self.prefix = prefix

#         # Each gene requires a pair of alleles
#         self.firstAllele = FormField(AlleleForm, name=("{}-first".format(self.prefix)), label="X_")
#         self.secondAllele = FormField(AlleleForm, name="agoutiSecond", label="_X")


#         self.submit = SubmitField('Submit')

data = [
    {
        'name': 'agouti',
        'options': [
            'A', 'a'
        ]
    },
    {
        'name': 'fakeGene',
        'options': [
            'B', 'b', 'Z'
        ]
    }
]


class GeneForm(FlaskForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.type = 'agouti'

    fields = FieldList(FormField(AlleleForm), min_entries=0)
    submit = SubmitField('Submit')
    
    # for g in groups:
    #     pprint(dir(fields))
        # fields.append_entry([AlleleForm(name=g)])
    # fields = FieldList(AlleleForm('allele'))
    # def __init__(self):
    #     super(GeneForm, self).__init__(self)
    #     for i in self.groups:
    #         a = AlleleForm(name=(str(self.groups[i])))

    # for i in range(len(groups)):
    #     a = AlleleForm(name=(str(groups[i])))
    #     fields.append(a)

        # f = AlleleForm(name=(str(groups[i]) + '-first'), label="X_")
        # fields.append_entry(f)

        # f = FormField(AlleleForm, name=(str(groups[i]) + '-first'), label="X_")
        # fields.append(f)
        # firstAlleles.append(FormField(AlleleForm, name=(str(groups[i])+'-first'), label="X_"))
        # secondAlleles.append(FormField(AlleleForm, name=(str(groups[i])+'-second'), label="_X"))
    






# TODO this is VERY TEMPORARY and should be implemented better later
# agoutiForm = GeneGroupForm('agouti')
geneList = ['agouti']




@app.route("/", methods=['GET', 'POST'])
def hello_world():

    form = GeneForm()
    # for f in form.fields:
    #     print(f)
    # pprint(form.fields)
    if (len(form.fields) == 0):
        for i in range(len(data)):
        # for entry in data:

            form.fields.append_entry(AlleleForm())

            # form.fields[0].name = entry['name']
            form.fields[i].name = data[i]['name']
            # form.fields[0].choices = entry['options']
            form.fields[i].choices = data[i]['options']

            # pprint(vars(form.fields[i]))

            # for f in form.fields:
            #     pprint(vars(f))
            # pprint(vars(form.fields))



            # f = AlleleForm()
            # f.firstAllele.label = entry['name']
            # for option in entry['options']:
            #     # pprint(option)
            #     # pprint(vars(f.firstAllele))
            #     f.firstAllele.choices.append(option)
            # pprint(f.firstAllele.choices)
            # # pprint(vars(f.firstAllele))
            # # f.firstAllele.choices = entry['options']
            # form.fields.append_entry(f)
            # # pprint(form.fields.entries)
            # # pprint(vars(form.fields))



            # pprint(form.fields.entries)
            # # pprint(vars(form.fields))
            # # for field in form.fields:
            # #     pprint(vars(field.form.firstAllele))
            # for entry in form.fields.entries:
            #     pprint(vars(entry.form.firstAllele))
            #     # pprint(vars(field.form))


            # pprint(vars(form.fields[0].firstAllele))
        # for field in data:
        #     # pprint(field['name'])
        #     pprint(form.fields)
        #     f = AlleleForm()
        #     fieldName = field['name']
        #     optionList = field['options']
        #     # pprint(f.firstAllele.choices)
        #     # print(a)
        #     # pprint(vars(f.firstAllele))
        #     form.fields.append_entry(f)
        #     f.firstAllele.name = fieldName
        #     f.secondAllele.name = fieldName
        #     f.firstAllele.choices = optionList
        #     f.secondAllele.choices = optionList
        #     # pprint(vars(form.fields))
        #     for category in form.fields.entries:
        #         pprint(vars(category.form))
        #     # pprint(vars(form.fields))

    
    # pprint(vars(form.fields))

    # groups = ['agouti']
    # for g in groups:
    #     form.fields.append(g)

    # pprint(form.fields.entries)
    # pprint(vars(form.fields))
    # for f in form.fields.entries:
    #     pprint(vars(f)['name'])



    # Generate phenotype value
    phenotype = ''



    if form.validate_on_submit():
        # pprint(dir(form))
        pprint('i got to this point')
        # pprint(vars(form.fields[0]))
        # firstVal = form.fields
        # firstVal = form.firstAlleles[0].alleleField.data
        # secondVal = form.secondAlleles[0].alleleField.data

        # firstVal = form.groups[0].firstAllele.alleleField.data
        # secondVal = form.groups[0].secondAllele.alleleField.data
        # phenotype = firstVal + secondVal

    return render_template('index.html', form=form, phenotype=phenotype)