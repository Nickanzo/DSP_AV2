from flask import render_template

from config import *
from model import *

@app.route("/")
def inicio():
    return '<h2>Sistema de cadastro de Funcionarios. </h2>'+\
            '<br><a href="/listar_funcionarios">Listar Funcionarios</a>'


@app.route("/listar_funcionarios")
def listar_funcionarios():
    # obter os funcionarios do cadastro
    funcionarios = db.session.query(Funcionario).all()
    vendedores = db.session.query(VendedorExterno).all()
    engenheiros = db.session.query(EngenheiroCivil).all()

    return render_template("listar_funcionarios.html", listaFunc=funcionarios, listaVend=vendedores,
                           listaEng=engenheiros)

app.run(debug=True)