from blueprintapp.app import db

class Medico(db.Model):
    __tablename__ = 'medicos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    
    # Relación uno a muchos
    citas = db.relationship('Cita', backref='medico', lazy=True, cascade="all, delete-orphan")