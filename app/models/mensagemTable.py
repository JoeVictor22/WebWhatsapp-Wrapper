from app import db

class Mensagem(db.Model):
    __tablename__= "mensagem"

    id = db.Column(db.BigInteger, primary_key=True)

    sessao_id = db.Column(db.BigInteger, db.ForeignKey("sessao.id"), primary_key=True)
    data = db.Column(db.DateTime, nullable=False)
    destinatario_eh_sistema = db.Column(db.Boolean, nullable=False)


    def __init__(self, sessao_id, data, destinatario_eh_sistema):
        self.sessao_id = sessao_id
        self.data = data
        self.destinatario_eh_sistema = destinatario_eh_sistema


    def __repr__(self):
        return "<Mensagem %r %r %r>" % self.id, self.sessao_id, str(self.destinatario_eh_sistema)