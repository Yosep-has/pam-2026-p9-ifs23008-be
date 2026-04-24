from app import create_app
from app.config import Config
web: gunicorn app:app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=Config.APP_PORT)