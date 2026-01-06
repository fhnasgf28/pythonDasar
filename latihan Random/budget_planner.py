"""
budget_planner.py

Contoh implementasi OOP: Personal Budget Planner
- Menunjukkan enkapsulasi, pewarisan, polimorfisme, abstraksi, dan komposisi.
- Ditulis dalam bahasa Indonesia (komentar & docstring).
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime, date
from typing import List, Dict, Optional


# -----------------------------
# TRANSACTION (base + subclasses)
# -----------------------------
class Transaction:
    """Representasi umum transaksi (pemasukan atau pengeluaran)."""

    def __init__(self, amount: float, description: str, category: str, when: Optional[date] = None):
        self.amount = float(amount)
        self.description = description
        self.category = category
        self.when = when or date.today()

    def is_income(self) -> bool:
        """Kembalikan True jika ini pemasukan (dipakai oleh subclass)."""
        return False

    def signed_amount(self) -> float:
        """Nilai numerik, positif untuk income, negatif untuk expense (polimorfisme melalui subclass)."""
        return -self.amount

    def summary(self) -> str:
        """Ringkasan singkat transaksi."""
        kind = "Income" if self.is_income() else "Expense"
        return f"[{self.when.isoformat()}] {kind}: {self.category} - {self.description} {self.amount:.2f}"


class Income(Transaction):
    def is_income(self) -> bool:
        return True

    def signed_amount(self) -> float:
        return self.amount


class Expense(Transaction):
    def is_income(self) -> bool:
        return False

    def signed_amount(self) -> float:
        return -self.amount


# -----------------------------
# BUDGET CATEGORY (komposisi)
# -----------------------------
class BudgetCategory:
    """Kategori anggaran. Menampung batas (limit) dan transaksi yang terkait."""

    def __init__(self, name: str, limit: Optional[float] = None):
        self.name = name
        self.limit = None if limit is None else float(limit)
        self._transactions: List[Transaction] = []

    def add_transaction(self, t: Transaction):
        self._transactions.append(t)

    def total(self) -> float:
        """Total (net) transaksi pada kategori ini (income - expense)."""
        return sum(t.signed_amount() for t in self._transactions)

    def total_expenses(self) -> float:
        return sum(-t.signed_amount() for t in self._transactions if not t.is_income())

    def within_limit(self) -> Optional[bool]:
        """Jika limit diset, kembalikan apakah total pengeluaran berada di bawah limit.
        Mengembalikan None jika tidak ada limit."""
        if self.limit is None:
            return None
        return self.total_expenses() <= self.limit

    def __repr__(self):
        return f"BudgetCategory(name={self.name!r}, limit={self.limit})"


# -----------------------------
# ACCOUNT (enkapsulasi)
# -----------------------------
class Account:
    """Sederhana: menyimpan saldo. Menunjukkan enkapsulasi dengan atribut privat."""

    def __init__(self, initial_balance: float = 0.0):
        self._balance = float(initial_balance)

    @property
    def balance(self) -> float:
        """Saldo saat ini (baca saja)."""
        return self._balance

    def apply(self, t: Transaction):
        """Terapkan transaksi ke saldo. Ini memodifikasi state internal privat."""
        self._balance += t.signed_amount()

    def __repr__(self):
        return f"Account(balance={self._balance:.2f})"


# -----------------------------
# GOAL (komposisi / agregasi)
# -----------------------------
class Goal:
    """Tujuan keuangan (mis. menabung untuk sesuatu)."""

    def __init__(self, name: str, target_amount: float, deadline: Optional[date] = None):
        self.name = name
        self.target_amount = float(target_amount)
        self.deadline = deadline
        self._contributed = 0.0  # kontribusi yang dialokasikan ke goal

    def contribute(self, amount: float):
        self._contributed += float(amount)

    def progress(self) -> float:
        """Persentase tercapai (0..100)."""
        if self.target_amount == 0:
            return 100.0
        return min(100.0, (self._contributed / self.target_amount) * 100.0)

    def remaining(self) -> float:
        return max(0.0, self.target_amount - self._contributed)

    def __repr__(self):
        return f"Goal(name={self.name}, target={self.target_amount}, contributed={self._contributed})"


# -----------------------------
# REPORTS (abstraksi + polimorfisme)
# -----------------------------
class ReportGenerator(ABC):
    """Kelas abstrak untuk generator laporan."""

    @abstractmethod
    def generate(self, planner: "BudgetPlanner") -> str:
        pass


class SummaryReport(ReportGenerator):
    def generate(self, planner: "BudgetPlanner") -> str:
        lines = []
        lines.append("=== RINGKASAN ANGGARAN ===")
        lines.append(f"Saldo akun: {planner.account.balance:.2f}")
        lines.append(f"Total transaksi: {len(planner.transactions)}")
        lines.append("Kategori:")
        for name, cat in planner.categories.items():
            tot = cat.total()
            lines.append(f" - {name}: net {tot:.2f} | spent {cat.total_expenses():.2f}" +
                         (f" | limit {cat.limit:.2f}" if cat.limit is not None else ""))
        if planner.goals:
            lines.append("Goals:")
            for g in planner.goals:
                lines.append(f" - {g.name}: {g.progress():.1f}% ({g._contributed:.2f}/{g.target_amount:.2f})" +
                             (f" | deadline {g.deadline.isoformat()}" if g.deadline else ""))
        return "\n".join(lines)


class CategoryReport(ReportGenerator):
    def __init__(self, category_name: str):
        self.category_name = category_name

    def generate(self, planner: "BudgetPlanner") -> str:
        cat = planner.categories.get(self.category_name)
        if not cat:
            return f"Kategori '{self.category_name}' tidak ditemukan."
        lines = [f"=== LAPORAN KATEGORI: {cat.name} ===",
                 f"Limit: {cat.limit if cat.limit is not None else 'tidak ada'}",
                 f"Total pengeluaran: {cat.total_expenses():.2f}",
                 "Transaksi:"]
        for t in cat._transactions:
            lines.append("  " + t.summary())
        return "\n".join(lines)


# -----------------------------
# BUDGET PLANNER (komposisi besar)
# -----------------------------
class BudgetPlanner:
    """Objek pusat yang mengelola akun, kategori, transaksi, dan goals."""

    def __init__(self, account: Optional[Account] = None):
        self.account = account or Account(0.0)
        self.categories: Dict[str, BudgetCategory] = {}
        self.transactions: List[Transaction] = []
        self.goals: List[Goal] = []

    def add_category(self, name: str, limit: Optional[float] = None):
        if name in self.categories:
            raise ValueError(f"Kategori '{name}' sudah ada.")
        self.categories[name] = BudgetCategory(name, limit)

    def add_goal(self, goal: Goal):
        self.goals.append(goal)

    def add_transaction(self, t: Transaction):
        """Tambahkan transaksi: simpan, update kategori, update akun."""
        self.transactions.append(t)
        # Jika kategori belum ada, buat otomatis tanpa limit
        if t.category not in self.categories:
            self.add_category(t.category)
        self.categories[t.category].add_transaction(t)
        self.account.apply(t)

    def allocate_to_goal(self, goal_name: str, amount: float) -> bool:
        """Coba alokasikan sejumlah uang dari saldo ke goal; kembalikan True jika berhasil."""
        g = next((x for x in self.goals if x.name == goal_name), None)
        if g is None:
            raise ValueError("Goal tidak ditemukan.")
        if amount <= 0:
            raise ValueError("Jumlah harus > 0.")
        # simple rule: harus ada saldo yang cukup
        if self.account.balance >= amount:
            g.contribute(amount)
            # secara logika kita bisa menandai pengurangan saldo dengan transaksi khusus
            self.add_transaction(Expense(amount, f"Alokasi ke goal: {g.name}", category="GoalAllocation"))
            return True
        return False

    def get_category_summary(self) -> Dict[str, float]:
        return {name: cat.total_expenses() for name, cat in self.categories.items()}

    def generate_report(self, generator: ReportGenerator) -> str:
        """Polimorfisme: menerima objek yang mengikuti antarmuka ReportGenerator."""
        return generator.generate(self)


# -----------------------------
# Contoh penggunaan
# -----------------------------
if __name__ == "__main__":
    # Inisialisasi planner & akun awal
    planner = BudgetPlanner(Account(initial_balance=500.0))

    # Tambah kategori dengan limit
    planner.add_category("Makanan", limit=300.0)
    planner.add_category("Transport", limit=100.0)
    planner.add_category("Hiburan")

    # Tambah beberapa transaksi (pemasukan & pengeluaran)
    planner.add_transaction(Income(1500.0, "Gaji bulan ini", "Gaji", when=date(2026, 1, 1)))
    planner.add_transaction(Expense(50.0, "Makan siang", "Makanan", when=date(2026, 1, 2)))
    planner.add_transaction(Expense(20.0, "Transport umum", "Transport", when=date(2026, 1, 3)))
    planner.add_transaction(Expense(120.0, "Belanja bahan makanan", "Makanan", when=date(2026, 1, 4)))
    planner.add_transaction(Expense(60.0, "Nonton bioskop", "Hiburan", when=date(2026, 1, 5)))

    # Tambah goal
    vacation = Goal("Liburan Bali", target_amount=1000.0, deadline=date(2026, 6, 1))
    planner.add_goal(vacation)

    # Alokasikan sebagian saldo ke goal (jika saldo cukup)
    # Note: allocate_to_goal akan membuat transaksi Expense (GoalAllocation)
    success = planner.allocate_to_goal("Liburan Bali", 200.0)
    print("Alokasi ke goal berhasil?" , success)

    # Cetak laporan ringkasan
    summary = planner.generate_report(SummaryReport())
    print(summary)
    print()

    # Cetak laporan kategori
    cat_report = planner.generate_report(CategoryReport("Makanan"))
    print(cat_report)

    # Tampilkan saldo akhir dan transaksi lengkap
    print("\nSaldo akhir:", planner.account.balance)
    print("\nSemua transaksi:")
    for t in planner.transactions:
        print(" -", t.summary())
