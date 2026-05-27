from flask import Blueprint, render_template, request, redirect, url_for
from blueprintapp.app import db
from blueprintapp.pacientes.models import Paciente

bp_pacientes = Blueprint('pacientes', __name__, template_folder='templates')

@bp_pacientes.route('/')
def index():
    pacientes = Paciente.query.all()
    return render_template('pacientes/index.html', pacientes=pacientes)

@bp_pacientes.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        telefono = request.form.get('telefono')
        if nombre and telefono:
            nuevo = Paciente(nombre=nombre, telefono=telefono)
            db.session.add(nuevo)
            db.session.commit()
            return redirect(url_for('pacientes.index'))
    return render_template('pacientes/create.html')

@bp_pacientes.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    paciente = Paciente.query.get_or_404(id)
    if request.method == 'POST':
        paciente.nombre = request.form.get('nombre')
        paciente.telefono = request.form.get('telefono')
        db.session.commit()
        return redirect(url_for('pacientes.index'))
    return render_template('pacientes/edit.html', paciente=paciente)

@bp_pacientes.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    return redirect(url_for('pacientes.index'))