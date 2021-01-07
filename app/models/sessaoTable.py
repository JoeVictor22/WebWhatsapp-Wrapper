from app import db

class Sessao(db.Model):
    __tablename__= "sessao"

    id = db.Column(db.BigInteger, primary_key=True)

    contato_id = db.Column(db.BigInteger, db.ForeignKey("contato.id"),  nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False)
    finalizada = db.Column(db.Boolean, nullable=False)


    def __init__(self, contato_id, data_criacao):
        self.contato_id = contato_id
        self.data_criacao = data_criacao
        self.finalizada = False


    def __repr__(self):
        return "<Sessao %r %r %r>" % self.id, self.contato_id, str(self.finalizada)