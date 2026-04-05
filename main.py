from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import FinancialRecord
from schemas import RecordCreate
from services import get_summary

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Basic Finance Tracker API")

def check_admin(role: str):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can modify records")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/records")
def create_record(
    record: RecordCreate,
    role: str = Query(...),
    db: Session = Depends(get_db)
):
    check_admin(role)

    new_record = FinancialRecord(**record.dict())
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@app.get("/records")
def get_records(
    category: str = Query(None),
    record_type: str = Query(None),
    date: str = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(FinancialRecord)

    if category:
        query = query.filter(FinancialRecord.category == category)

    if record_type:
        query = query.filter(FinancialRecord.type == record_type)

    if date:
        query = query.filter(FinancialRecord.date == date)

    return query.all()


@app.put("/records/{record_id}")
def update_record(record_id: int, record: RecordCreate, db: Session = Depends(get_db)):
    existing = db.query(FinancialRecord).filter(FinancialRecord.id == record_id).first()

    if not existing:
        raise HTTPException(status_code=404, detail="Record not found")

    for key, value in record.dict().items():
        setattr(existing, key, value)

    db.commit()
    db.refresh(existing)
    return existing


@app.delete("/records/{record_id}")
def delete_record(record_id: int, db: Session = Depends(get_db)):
    record = db.query(FinancialRecord).filter(FinancialRecord.id == record_id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    db.delete(record)
    db.commit()
    return {"message": "Deleted successfully"}


@app.get("/summary")
def summary(db: Session = Depends(get_db)):
    return get_summary(db)