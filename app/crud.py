from sqlalchemy.orm import Session
from Database.models import Document

def create_document(db: Session, title: str, content: str, file_path: str):
    doc = Document(
        title=title,
        content=content,
        file_path=file_path
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc


def get_documents(db: Session):
    return db.query(Document).all()


def get_document_by_id(db: Session, doc_id: int):
    return db.query(Document).filter(Document.id == doc_id).first()