from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel

app = FastAPI(title = "Finsight")

class DocumentCreate(BaseModel):
    company_name: str
    year: int
class Document(DocumentCreate):
    id: int

documents: dict[int, Document] = {}
next_id = 1


@app.get("/health")
def health_check():
    return{"status":"ok"}

@app.post("/documents",response_model=Document, status_code=status.HTTP_201_CREATED)
def create_document(doc: DocumentCreate):
    global next_id
    new_doc = Document(id=next_id, **doc.model_dump())
    documents[next_id] = new_doc
    next_id += 1
    return new_doc

@app.get("/documents", response_model=list[Document])
def list_documents():
    return list(documents.values())

@app.get("/documents/{document_id}", response_model=Document)
def get_document(document_id: int):
    if document_id not in documents:
        raise HTTPException(status_code=404, detail="Document not found")
    return documents[document_id]

@app.delete("/documents/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_document(document_id: int):
    if document_id not in documents:
        raise HTTPException(status_code=404,detail="Document not found")
    del documents[document_id]

