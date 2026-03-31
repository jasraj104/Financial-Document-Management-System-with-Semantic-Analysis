from db import SessionLocal
from crud import create_document, get_documents

db = SessionLocal()

create_document(db, "Test Doc", "This is content", "/files/doc1.txt")

docs = get_documents(db)

for d in docs:
    print(d.title, d.content)

db.close()