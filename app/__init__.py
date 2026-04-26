from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app,
         resources={r"/*": {"origins": "*"}},
         allow_headers=["Content-Type", "Authorization"],
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         supports_credentials=False)

    db.init_app(app)

    # Register blueprints
    from app.routes.motivation_routes import motivation_bp
    from app.routes.auth_routes import auth_bp

    app.register_blueprint(motivation_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()
        _seed_admin()  # buat akun admin otomatis

    return app

def _seed_admin():
    """Buat akun admin default jika belum ada."""
    from app.models.user import User

    if not User.query.filter_by(username="admin").first():
        admin = User(username="admin")
        admin.set_password("delcomfarm123")
        db.session.add(admin)
        db.session.commit()
        print("✅ Akun admin dibuat: username=admin, password=delcomfarm123")