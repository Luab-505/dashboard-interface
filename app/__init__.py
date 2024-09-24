from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inicializa o banco de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/nome_do_banco'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializando o banco e as migrações
    db.init_app(app)
    Migrate(app, db)

    # Importando rotas e modelos
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
