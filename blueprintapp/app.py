from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='templates')
    
    # Configuración de SQLite
    app.config['SECRET_KEY'] = 'control_medico_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medicontrol.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensiones con el contexto de la app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 1. Importación de los Blueprints desde blueprintapp
    from blueprintapp.core.routes import bp_core
    from blueprintapp.medicos.routes import bp_medicos
    from blueprintapp.pacientes.routes import bp_pacientes
    from blueprintapp.citas.routes import bp_citas
    
    # 2. Registro de Blueprints con sus prefijos reglamentarios
    app.register_blueprint(bp_core, url_prefix="/")
    app.register_blueprint(bp_medicos, url_prefix="/medicos")
    app.register_blueprint(bp_pacientes, url_prefix="/pacientes")
    app.register_blueprint(bp_citas, url_prefix="/citas")
    
    return app