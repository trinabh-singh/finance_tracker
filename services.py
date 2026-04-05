from sqlalchemy.orm import Session
from sqlalchemy import func
from models import FinancialRecord


def get_summary(db: Session):
    total_income = db.query(func.sum(FinancialRecord.amount)).filter(
        FinancialRecord.type == "income"
    ).scalar() or 0

    total_expense = db.query(func.sum(FinancialRecord.amount)).filter(
        FinancialRecord.type == "expense"
    ).scalar() or 0

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "current_balance": total_income - total_expense
    }