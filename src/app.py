
from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
def index():
    titulo='IEVN'
    list=['Pedro','Mario','Dario']
    return render_template('index.html',titulo=titulo,list=list)

@app.route('/hola')
def hola():
    return 'Hola :D'

@app.route("/user/<string:user>")
def user(user):
    return "Hola como estás: "+user+" :D"

@app.route("/numero/<int:n>")
def numero(n):
    return "Número: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID: {} Nombre: {} ".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma es: {}".format(n1+n2)

@app.route("/default")
@app.route("/default/<string:n>")
def default(n='Leo xd'):
    return "El valor de n es: "+n

if __name__=="__main__":
    app.run(debug=True)