from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def current_user(user_id):
    return cadastros.query.get(user_id)

class usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    os = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    fone = db.Column(db.String(255), nullable=False)
    marca = db.Column(db.String(255), nullable=False)
    modelo = db.Column(db.String(255), nullable=False)
    nserie = db.Column(db.String(255), nullable=False)
    defeito = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    data = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())