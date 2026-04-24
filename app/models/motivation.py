from app.extensions import db
from datetime import datetime, timezone

class Motivation(db.Model):
    __tablename__ = "motivations"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    request_id = db.Column(db.Integer, db.ForeignKey("requests.id"))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))