#Aula 09 min 56
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Ola mundo'

@app.route('/saudacao')
def saudacao():
    s = render_template("saudacao.html")
    return s

@app.route('/cursos')
def curso():
    return render_template("cursos.html")

if __name__ == '__main__':
    app.run(debug=True)