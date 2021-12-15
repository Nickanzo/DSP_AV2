from flask import render_template, jsonify, request

from config import *
from model import *

@app.route("/")
def inicio():
    return '<h2>Sistema de cadastro de Funcionarios. </h2>'+\
            '<br><a href="/cadastrar_funcionarios">Cadastra Funcionario</a>' +\
            '<br><a href="/cadastrar_vendedores">Cadastra Vendedor Externo</a>' +\
            '<br><a href="/cadastrar_engenheiros">Cadastra Engenheiro Civil</a>' +\
            '<br><a href="/listar_funcionarios">Listar Funcionarios</a>' +\
            '<br><a href="/listar_vendedores">Listar Vendedores</a>' +\
            '<br><a href="/listar_engenheiros">Listar Engenheiros</a>' +\
            '<br><a href="/listar">Listar Todos</a>'

@app.route("/cadastrar_funcionarios")
def cadastrar_funcionarios():
    return render_template("cadastrar_funcionarios.html")

@app.route("/listar_funcionarios")
def listar_funcionarios():
    # obter os funcionarios do cadastro
    funcionarios = db.session.query(Funcionario).all()
    return render_template("listar_funcionarios.html", listaFunc=funcionarios)

@app.route("/listar_vendedores")
def listar_vendedores():
    # obter os vendedores do cadastro
    vendedores = db.session.query(VendedorExterno).all()
    return render_template("listar_vendedores.html", listaVend=vendedores)

@app.route("/listar_engenheiros")
def listar_engenheiros():
    # obter os engenheiros do cadastro
    engenheiros = db.session.query(EngenheiroCivil).all()
    return render_template("listar_engenheiros.html", listaEng=engenheiros)

@app.route("/listar")
def listar():
    # obter os funcionarios do cadastro
    funcionarios = db.session.query(Funcionario).all()
    vendedores = db.session.query(VendedorExterno).all()
    engenheiros = db.session.query(EngenheiroCivil).all()

    return render_template("listar.html", listaFunc=funcionarios, listaVend=vendedores,
                           listaEng=engenheiros)

@app.route("/incluir_funcionario", methods=['POST'])
def incluir_funcionario():

    resposta = "Funcionario incluído com sucesso!"

    nome = request.form['nome']
    cpf = request.form['cpf']
    if nome != "" and cpf != "":
        try:
            novo = Funcionario(nome=nome,cpf=cpf)
            db.session.add(novo)
            db.session.commit()
        except Exception as e:
            resposta = "Falha ao incluir"
        return resposta
    else:
        resposta = "Falha ao incluir"
        return resposta

@app.route("/incluir_vendedor", methods=['POST'])
def incluir_vendedor():
    resposta = "Funcionario incluído com sucesso!"

    nome = request.form['nome']
    cpf = request.form['cpf']
    if nome != "" and cpf != "":
        try:
            novo = Funcionario(nome=nome, cpf=cpf)
            db.session.add(novo)
            db.session.commit()
        except Exception as e:
            resposta = "Falha ao incluir"
        return resposta
    else:
        resposta = "Falha ao incluir"
        return resposta

@app.route("/incluir_engenheiro", methods=['POST'])
def incluir_engenheiro():
    resposta = "Engenheiro incluído com sucesso!"

    nome = request.form['nome']
    cpf = request.form['cpf']
    if nome != "" and cpf != "":
        try:
            novo = Funcionario(nome=nome, cpf=cpf)
            db.session.add(novo)
            db.session.commit()
        except Exception as e:
            resposta = "Falha ao incluir"
        return resposta
    else:
        resposta = "Falha ao incluir"
        return resposta

app.run(debug=True)