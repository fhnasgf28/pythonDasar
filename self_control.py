"""
self_control.py

A simple CLI tool to help manage impulses and build self-control habits.
Features:
- Prompted breathing exercise (box breathing)
- Delay-and-decide timer (gives a cooling-off period before acting)
- Quick journaling/logging of urges and triggers
- Habit tracker (simple streaks stored in a local JSON in the repo)
- Motivational quotes and tips

Usage:
    python self_control.py --help

This is intentionally simple and meant as an accompaniment to real-world
strategies: therapy, coaching, and medical advice when needed.

"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = Path(".self_control_data.json")

DEFAULT_QUOTES = [
    "Sabar itu bukan menunggu — tapi bagaimana kita bersikap saat menunggu.",
    "Jeda 5 menit dapat menyelamatkan keputusan yang buruk.",
    "Kontrol diri adalah otot, latih perlahan tapi konsisten.",
]


def load_data():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text())
        except Exception:
            return {"logs": [], "habits": {}}
    return {"logs": [], "habits": {}}


def save_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False))


def breathe(box_seconds=4, rounds=4):
    print("Mulai latihan pernapasan box breathing")
    print("Tarik napas — tahan — buang — tahan")
    for r in range(rounds):
        for phase in ("Tarik", "Tahan", "Buang", "Tahan"):
            print(f"{phase}... ({box_seconds}s)")
            time.sleep(box_seconds)
        print(f"-- Selesai ronde {r+1}/{rounds} --")
    print("Selesai. Ambil napas dalam-dalam dan amati perasaanmu.")


def delay_and_decide(minutes=5):
    seconds = int(minutes * 60)
    end = datetime.now() + timedelta(seconds=seconds)
    print(f"Berikan jeda {minutes} menit. Waktu selesai: {end.strftime('%H:%M:%S')}")
    try:
        while datetime.now() < end:
            remaining = (end - datetime.now()).seconds
            mins, sec = divmod(remaining, 60)
            print(f"Sisa waktu: {mins:02d}:{sec:02d}", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nJeda dibatalkan oleh pengguna.")
        return False
    print("\nWaktu jeda selesai. Sekarang buat keputusan dengan kepala dingin.")
    return True


def log_urge(description, intensity=5):
    data = load_data()
    entry = {
        "time": datetime.now().isoformat(),
        "description": description,
        "intensity": int(intensity),
    }
    data.setdefault("logs", []).append(entry)
    save_data(data)
    print("Tercatat: ", entry)


def add_habit(name):
    data = load_data()
    habits = data.setdefault("habits", {})
    if name in habits:
        print("Habit sudah terdaftar.")
        return
    habits[name] = {"streak": 0, "last_done": None}
    save_data(data)
    print(f"Habit '{name}' ditambahkan.")


def mark_habit_done(name):
    data = load_data()
    habits = data.setdefault("habits", {})
    if name not in habits:
        print("Habit belum terdaftar. Gunakan --add-habit untuk menambahkan.")
        return
    today = datetime.now().date().isoformat()
    h = habits[name]
    if h.get("last_done") == today:
        print("Sudah dicatat untuk hari ini.")
        return
    # if last done was yesterday, increment streak
    last = h.get("last_done")
    if last:
        last_date = datetime.fromisoformat(last).date()
        if last_date == (datetime.now().date() - timedelta(days=1)):
            h["streak"] = h.get("streak", 0) + 1
        else:
            h["streak"] = 1
    else:
        h["streak"] = 1
    h["last_done"] = datetime.now().isoformat()
    save_data(data)
    print(f"Dicatat: {name}. Streak sekarang: {h['streak']}")


def show_stats():
    data = load_data()
    logs = data.get("logs", [])
    habits = data.get("habits", {})
    print("\n=== Statistik Singkat ===")
    print(f"Total catatan keinginan: {len(logs)}")
    if logs:
        recent = logs[-5:]
        print("5 catatan terakhir:")
        for l in recent:
            t = l.get("time")
            desc = l.get("description")
            intensity = l.get("intensity")
            print(f"- [{t}] (intensitas {intensity}) {desc}")
    print("\nHabit:")
    if not habits:
        print("  - Belum ada habit terdaftar.")
    else:
        for name, info in habits.items():
            streak = info.get("streak", 0)
            last = info.get("last_done")
            print(f"  - {name}: streak {streak}, terakhir {last}")


def quote():
    import random

    print(random.choice(DEFAULT_QUOTES))


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Tools sederhana untuk mengatur hawa nafsu / impuls")
    p.add_argument("--breathe", action="store_true", help="Lakukan sesi pernapasan singkat")
    p.add_argument("--delay", type=float, nargs="?", const=5, help="Jeda dalam menit sebelum mengambil keputusan (default 5)")
    p.add_argument("--log", nargs="+", help="Catat keinginan/hasrat. Gunakan tanda kutip untuk deskripsi multi-kata")
    p.add_argument("--intensity", type=int, default=5, help="Intensitas hasrat (1-10)")
    p.add_argument("--add-habit", help="Tambahkan habit untuk dilacak")
    p.add_argument("--done", help="Tandai habit sebagai selesai hari ini")
    p.add_argument("--stats", action="store_true", help="Tampilkan statistik dan log singkat")
    p.add_argument("--quote", action="store_true", help="Tampilkan kutipan motivasi singkat")
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if args.breathe:
        breathe()
    if args.delay is not None:
        delay_and_decide(args.delay)
    if args.log:
        desc = " ".join(args.log)
        log_urge(desc, args.intensity)
    if args.add_habit:
        add_habit(args.add_habit)
    if args.done:
        mark_habit_done(args.done)
    if args.stats:
        show_stats()
    if args.quote:
        quote()
    if not any([args.breathe, args.delay is not None, args.log, args.add_habit, args.done, args.stats, args.quote]):
        print("Tidak ada opsi diberikan. Jalankan dengan --help untuk melihat perintah yang tersedia.")


if __name__ == "__main__":
    main()
