from flask import Flask, render_template

from models.horse_genes import AgoutiGene

app = Flask(__name__)

testGene = AgoutiGene()

@app.route("/")
def hello_world():
    return '<h1>' + testGene.geneString + '</h1>'
    # return render_template('index.html')