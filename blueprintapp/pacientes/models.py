from blueprintapp.app import db

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    
    # Relación uno a muchos
    citas = db.relationship('Cita', backref='paciente', lazy=True, cascade="all, delete-orphan")