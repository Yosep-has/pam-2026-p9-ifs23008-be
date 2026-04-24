from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # CORS config lengkap
    CORS(app,
         origins="*",
         allow_headers=["Content-Type", "Authorization"],
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         supports_credentials=False)

    # Inisialisasi DB dengan App
    db.init_app(app)

    # Import dan register blueprint
    from app.routes.motivation_routes import motivation_bp
    app.register_blueprint(motivation_bp)

    # Buat database jika belum ada
    with app.app_context():
        db.create_all()

    return app