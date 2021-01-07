from app import db

class Contato(db.Model):
    __tablename__= "contato"

    id = db.Column(db.BigInteger, primary_key=True)

    chat_id = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.String(50), nullable=False)
    qr_code = db.Column(db.String(255), nullable=False)

    def __init__(self, chat_id, name, numero, qr_code):
        self.chat_id = chat_id
        self.name = name
        self.numero = numero
        self.qr_code = qr_code


    def __repr__(self):
        return "<Contato %r %r %r %r %r>" % self.id, self.chat_id, self.name, self.numero, self.qr_code