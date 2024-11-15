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

@app.route('/cursos/<nome>')
def curso_com_nome(nome):
    if nome == 'devweb':
        return render_template("curso_devweb.html")
    elif nome == 'poo':
        return render_template("curso_poo.html")
    else:
        return "Curso não existe "

if __name__ == '__main__':
    app.run(debug=True)