from flask import Blueprint, render_template, request, redirect, url_for
from blueprintapp.app import db
from blueprintapp.medicos.models import Medico

bp_medicos = Blueprint('medicos', __name__, template_folder='templates')

@bp_medicos.route('/')
def index():
    medicos = Medico.query.all()
    return render_template('medicos/index.html', medicos=medicos)

@bp_medicos.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        especialidad = request.form.get('especialidad')
        if nombre and especialidad:
            nuevo = Medico(nombre=nombre, especialidad=especialidad)
            db.session.add(nuevo)
            db.session.commit()
            return redirect(url_for('medicos.index'))
    return render_template('medicos/create.html')

@bp_medicos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    # 1. Busca al médico en SQLite usando su ID único
    medico = Medico.query.get_or_404(id)
    
    # 2. Si el usuario presiona "Actualizar" (POST), guarda los nuevos datos
    if request.method == 'POST':
        medico.nombre = request.form.get('nombre')
        medico.especialidad = request.form.get('especialidad')
        db.session.commit() # Guarda en la base de datos
        return redirect(url_for('medicos.index'))
        
    # 3. Si solo entra a la página (GET), muestra el formulario con los datos actuales
    return render_template('medicos/edit.html', medico=medico)

@bp_medicos.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    medico = Medico.query.get_or_404(id)
    db.session.delete(medico)
    db.session.commit()
    return redirect(url_for('medicos.index'))