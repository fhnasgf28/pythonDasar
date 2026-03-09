from __future__ import annotations

from dataclasses import dataclass, fields 
from datetime import datetime 
from decimal import Decimal 
from enum import Enum 
from typing import Dict, List, Optional,Protocol
import uud 

class PRStatus(str, Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass(frozen=True)
class Money:
    amount: Decimal 
    currency: str = "IDR"

    def __post_init_(self):
        if self.amount < 0:
            raise ValueError("money cannot be negative")
    
    def _ensure_currency(self, other: "Money") -> None:
        if self.currency != other.currency:
            raise ValueError(f"currency mismatch :{self.currency} != {other.currency}")
    
    def __add__(self, other: "Money") -> "Money":
        self._ensure_currency(other)
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other: "Money") -> "Money":
        self._ensure_currency(other)
        result = self.amount - other.amount 
        return Money(result, self.currency) if result >= 0 else Money(Decimal("0"), self.currency)
    
    def lt(self, other: "Money") -> bool:
        self._ensure_currency(other)
        return self.amount < other.amount 
    
    def gt(self, other: "Money") -> bool:
        self._ensure_currency(other)
        return self.amount > other.amount

@dataclass(frozen=True)
class LineItem:
    sku: str 
    name: str 
    qty: int 
    unit_price: Money

    def __post_init_(self):
        if self.qty <= 0:
            raise ValueError("QTY must be > 0")

@dataclass
class PurchaseRequest:
    requster: str 
    department: str 
    tax_rate: Decimal("0.00")
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    