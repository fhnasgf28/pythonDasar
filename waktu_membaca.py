"""
waktu_membaca.py

Simple OOP module untuk melacak waktu membaca buku.

Kelas:
- Book: metadata buku (judul, pengarang, total halaman)
- ReadingSession: satu sesi membaca (waktu mulai, waktu selesai, halaman dibaca)
- ReadingTracker: kumpulan sesi untuk sebuah buku, dengan metode untuk menghitung total waktu,
  kecepatan membaca rata-rata, dan estimasi sisa waktu.

Contoh penggunaan ada di bawah pada blok __main__.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional


@dataclass
class Book:
    title: str
    author: Optional[str] = None
    total_pages: Optional[int] = None


@dataclass
class ReadingSession:
    start: datetime
    end: datetime
    pages_read: int

    def duration(self) -> timedelta:
        """Durasi sesi sebagai timedelta."""
        return self.end - self.start

    def duration_minutes(self) -> float:
        """Durasi dalam menit (float)."""
        return self.duration().total_seconds() / 60.0


@dataclass
class ReadingTracker:
    book: Book
    sessions: List[ReadingSession] = field(default_factory=list)

    def add_session(self, start: datetime, end: datetime, pages_read: int) -> None:
        if end <= start:
            raise ValueError("waktu selesai harus setelah waktu mulai")
        if pages_read < 0:
            raise ValueError("pages_read tidak boleh negatif")
        self.sessions.append(ReadingSession(start=start, end=end, pages_read=pages_read))

    def add_session_minutes(self, duration_minutes: float, pages_read: int, end: Optional[datetime] = None) -> None:
        """Tambahkan sesi dengan durasi dalam menit. Jika end tidak diberikan, gunakan sekarang sebagai akhir."""
        if duration_minutes <= 0:
            raise ValueError("duration_minutes harus > 0")
        if pages_read < 0:
            raise ValueError("pages_read tidak boleh negatif")
        if end is None:
            end = datetime.now()
        start = end - timedelta(minutes=duration_minutes)
        self.add_session(start, end, pages_read)

    def total_time_minutes(self) -> float:
        return sum(s.duration_minutes() for s in self.sessions)

    def total_pages_read(self) -> int:
        return sum(s.pages_read for s in self.sessions)

    def average_speed_ppm(self) -> Optional[float]:
        """Rata-rata kecepatan membaca: pages per minute. None jika tidak ada sesi atau pages_read=0."""
        total_minutes = self.total_time_minutes()
        total_pages = self.total_pages_read()
        if total_minutes <= 0 or total_pages == 0:
            return None
        return total_pages / total_minutes

    def estimated_minutes_remaining(self) -> Optional[float]:
        """Estimasi menit tersisa untuk menyelesaikan buku berdasarkan kecepatan rata-rata.
        Mengembalikan None jika total_pages tidak diketahui atau kecepatan tidak dapat dihitung.
        """
        if self.book.total_pages is None:
            return None
        remaining_pages = max(0, self.book.total_pages - self.total_pages_read())
        speed = self.average_speed_ppm()
        if speed is None or speed == 0:
            return None
        return remaining_pages / speed

    def summary(self) -> str:
        total_minutes = self.total_time_minutes()
        total_pages = self.total_pages_read()
        avg_speed = self.average_speed_ppm()
        est_minutes = self.estimated_minutes_remaining()

        parts = [f"Buku: {self.book.title}"]
        if self.book.author:
            parts.append(f"Penulis: {self.book.author}")
        if self.book.total_pages is not None:
            parts.append(f"Total halaman: {self.book.total_pages}")
        parts.append(f"Total sesi: {len(self.sessions)}")
        parts.append(f"Halaman dibaca: {total_pages}")
        parts.append(f"Total waktu: {total_minutes:.1f} menit")
        parts.append(f"Kecepatan rata-rata: {avg_speed:.3f} halaman/menit" if avg_speed else "Kecepatan rata-rata: -")
        if est_minutes is not None:
            parts.append(f"Estimasi sisa waktu: {est_minutes:.1f} menit")
        else:
            parts.append("Estimasi sisa waktu: -")

        return "\n".join(parts)


if __name__ == "__main__":
    # Contoh penggunaan sederhana
    buku = Book(title="Belajar Python", author="Penulis Contoh", total_pages=300)
    tracker = ReadingTracker(book=buku)

    # tambahkan beberapa sesi (misal 30 menit baca 15 halaman)
    now = datetime.now()
    tracker.add_session(start=now - timedelta(minutes=60), end=now - timedelta(minutes=30), pages_read=20)
    tracker.add_session(start=now - timedelta(minutes=20), end=now, pages_read=15)

    print(tracker.summary())
