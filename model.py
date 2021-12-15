from config import *


class Funcionario(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    cpf = db.Column(db.String(254))

    def __str__(self):
        return str(self.id) + ") " + self.nome + ", " + self.cpf

    def json(self):
        return {
            "id": self.id,
            "Nome": self.nome,
            "Senha": self.cpf
        }

class VendedorExterno(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    cnh = db.Column(db.Integer)
    funcId = db.Column(db.Integer, db.ForeignKey(Funcionario.id), nullable=False)
    funcionario = db.relationship("Funcionario")

    def __str__(self):
        return str(self.id) + ") " + self.cnh + ", " + self.funcId

    def json(self):
        return {
            "id": self.id,
            "CNH": self.cnh,
            "Id Funcionario": self.funcId
        }

class EngenheiroCivil(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    crea = db.Column(db.Integer)
    engId = db.Column(db.Integer, db.ForeignKey(Funcionario.id), nullable=False)
    funcionario = db.relationship("Funcionario")

    def __str__(self):
        return str(self.id) + ") " + self.crea + ", " + self.engId

    def json(self):
        return {
            "id": self.id,
            "CREA": self.cnh,
            "Id Engenheiro": self.engId
        }


if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # criar funcionarios
    f1 = Funcionario(nome="Michele Jones", cpf="43178357033")
    f2 = Funcionario(nome="Leonardo Galhardo", cpf="99429429043")
    db.session.add(f1)
    db.session.add(f2)
    db.session.commit()

    # criar Vendedor Externo
    v1 = VendedorExterno(cnh="62700804600", funcionario=f1)
    db.session.add(v1)
    db.session.commit()

    # criar Engenheiro Civil
    e1 = EngenheiroCivil(crea="2620160010843", funcionario=f2)
    db.session.add(e1)
    db.session.commit()

