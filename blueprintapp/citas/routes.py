from flask import Blueprint, render_template, request, redirect, url_for
from blueprintapp.app import db
from blueprintapp.citas.models import Cita
from blueprintapp.medicos.models import Medico
from blueprintapp.pacientes.models import Paciente

bp_citas = Blueprint('citas', __name__, template_folder='templates')

@bp_citas.route('/')
def index():
    citas = Cita.query.all()
    return render_template('citas/index.html', citas=citas)

@bp_citas.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        fecha = request.form.get('fecha')
        hora = request.form.get('hora')
        medico_id = request.form.get('medico_id')
        paciente_id = request.form.get('paciente_id')
        
        if fecha and hora and medico_id and paciente_id:
            nueva_cita = Cita(fecha=fecha, hora=hora, medico_id=medico_id, paciente_id=paciente_id)
            db.session.add(nueva_cita)
            db.session.commit()
            return redirect(url_for('citas.index'))
            
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    return render_template('citas/create.html', medicos=medicos, pacientes=pacientes)

@bp_citas.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    cita = Cita.query.get_or_404(id)
    if request.method == 'POST':
        cita.fecha = request.form.get('fecha')
        cita.hora = request.form.get('hora')
        cita.medico_id = request.form.get('medico_id')
        cita.paciente_id = request.form.get('paciente_id')
        db.session.commit()
        return redirect(url_for('citas.index'))
        
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    return render_template('citas/edit.html', cita=cita, medicos=medicos, pacientes=pacientes)

@bp_citas.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    cita = Cita.query.get_or_404(id)
    db.session.delete(cita)
    db.session.commit()
    return redirect(url_for('citas.index'))