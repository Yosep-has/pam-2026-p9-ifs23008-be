from app.extensions import db
from app.models.motivation import Motivation
from app.models.request_log import RequestLog
from app.services.llm_service import generate_from_llm
from app.utils.parser import parse_llm_response

def create_motivations(theme: str, total: int):
    """Fungsi untuk membuat tips peternakan baru menggunakan AI dan menyimpannya ke DB."""
    try:
        prompt = f"""
        Kamu adalah seorang ahli peternakan berpengalaman dari Delcom Farm.
        Dalam format JSON, berikan {total} tips, saran, atau informasi seputar peternakan dengan topik "{theme}".

        Setiap tips harus informatif, praktis, dan berguna bagi peternak.
        Gunakan bahasa Indonesia yang mudah dipahami.

        WAJIB gunakan struktur JSON murni seperti di bawah ini:
        {{
            "motivations": [
                {{"text": "tips peternakan 1 yang informatif dan praktis"}},
                {{"text": "tips peternakan 2 yang informatif dan praktis"}}
            ]
        }}
        """

        # Ambil hasil dari Gemini
        result = generate_from_llm(prompt)

        # Pastikan ambil string dari dictionary
        if isinstance(result, dict):
            raw_response = result.get("response", "")
        else:
            raw_response = result

        # Ubah teks string menjadi list Python menggunakan parser
        motivations = parse_llm_response(raw_response)

        # Simpan log permintaan ke database
        req_log = RequestLog(theme=theme)
        db.session.add(req_log)
        db.session.flush()

        saved_texts = []
        for item in motivations:
            text = item.get("text")
            new_m = Motivation(text=text, request_id=req_log.id)
            db.session.add(new_m)
            saved_texts.append(text)

        db.session.commit()
        return saved_texts

    except Exception as e:
        db.session.rollback()
        print(f"Error di create_motivations: {e}")
        raise e

def get_all_motivations(page: int = 1, per_page: int = 10):
    """Fungsi untuk mengambil daftar tips peternakan yang sudah ada di DB."""
    try:
        query = Motivation.query
        total = query.count()
        data = (
            query
            .order_by(Motivation.id.desc())
            .offset((page - 1) * per_page)
            .limit(per_page)
            .all()
        )

        result = [
            {
                "id": m.id,
                "text": m.text,
                "created_at": m.created_at.isoformat() if m.created_at else None
            } for m in data
        ]

        return {
            "total": total,
            "page": page,
            "per_page": per_page,
            "data": result
        }
    except Exception as e:
        print(f"Error di get_all_motivations: {e}")
        raise e