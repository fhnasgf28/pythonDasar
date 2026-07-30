#!/usr/bin/env python3
"""
motivator.py
A small OOP Python CLI "motivator" app that:
 - stores user data and quotes in a JSON file
 - shows a random motivational quote
 - tracks daily activity streaks
 - lets you set and check simple goals
"""

import json
import random
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta, date
from pathlib import Path
import argparse
import sys

DATA_PATH = Path.home() / ".motivator_data.json"


def today_iso():
    return date.today().isoformat()


@dataclass
class Goal:
    id: int
    title: str
    target_date: str = ""
    done: bool = False

    def to_dict(self):
        return asdict(self)


@dataclass
class UserState:
    name: str = "You"
    quotes: list = field(default_factory=lambda: [
        "Kamu bisa lebih dari yang kamu kira.",
        "Langkah kecil setiap hari membawa perubahan besar.",
        "Fokus pada proses, bukan hasil.",
        "Jatuh tujuh kali, bangkit delapan kali.",
    ])
    streak_last_date: str = ""
    streak_count: int = 0
    goals: list = field(default_factory=list)  # list of Goal dicts
    next_goal_id: int = 1

    def to_dict(self):
        return {
            "name": self.name,
            "quotes": self.quotes,
            "streak_last_date": self.streak_last_date,
            "streak_count": self.streak_count,
            "goals": [g for g in self.goals],
            "next_goal_id": self.next_goal_id,
        }

    @staticmethod
    def from_dict(d):
        state = UserState()
        state.name = d.get("name", state.name)
        state.quotes = d.get("quotes", state.quotes)
        state.streak_last_date = d.get("streak_last_date", state.streak_last_date)
        state.streak_count = d.get("streak_count", state.streak_count)
        state.goals = d.get("goals", [])
        state.next_goal_id = d.get("next_goal_id", state.next_goal_id)
        return state


class Persistence:
    def __init__(self, path: Path = DATA_PATH):
        self.path = path

    def load(self) -> UserState:
        if not self.path.exists():
            return UserState()
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return UserState.from_dict(data)
        except Exception:
            return UserState()

    def save(self, state: UserState):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(state.to_dict(), f, ensure_ascii=False, indent=2)


class Motivator:
    def __init__(self, persistence: Persistence):
        self.persistence = persistence
        self.state = self.persistence.load()

    def greet(self):
        return f"Halo, {self.state.name}! Tetap semangat hari ini 😊"

    def add_quote(self, quote: str):
        if quote and quote not in self.state.quotes:
            self.state.quotes.append(quote)
            self.persistence.save(self.state)
            return True
        return False

    def random_quote(self):
        if not self.state.quotes:
            return "Tetap semangat!"
        return random.choice(self.state.quotes)

    def mark_active_today(self):
        last = self.state.streak_last_date
        today = today_iso()
        if last == today:
            return False  # already marked today
        if last:
            last_date = date.fromisoformat(last)
            if last_date == date.today() - timedelta(days=1):
                self.state.streak_count += 1
            else:
                self.state.streak_count = 1
        else:
            self.state.streak_count = 1
        self.state.streak_last_date = today
        self.persistence.save(self.state)
        return True

    def get_streak(self):
        # If last active was not today or yesterday, streak may be stale
        last = self.state.streak_last_date
        if not last:
            return 0
        last_date = date.fromisoformat(last)
        if last_date == date.today():
            return self.state.streak_count
        if last_date == date.today() - timedelta(days=1):
            return self.state.streak_count
        # streak broken
        return 0

    def add_goal(self, title: str, target_date: str = ""):
        gid = self.state.next_goal_id
        goal = Goal(id=gid, title=title, target_date=target_date, done=False)
        self.state.goals.append(goal.to_dict())
        self.state.next_goal_id += 1
        self.persistence.save(self.state)
        return gid

    def list_goals(self):
        return [Goal(**g) for g in self.state.goals]

    def complete_goal(self, goal_id: int):
        for g in self.state.goals:
            if g.get("id") == goal_id:
                g["done"] = True
                self.persistence.save(self.state)
                return True
        return False

    def set_name(self, name: str):
        self.state.name = name
        self.persistence.save(self.state)

    # small encouraging summary
    def status_card(self):
        streak = self.get_streak()
        pending = [g for g in self.state.goals if not g.get("done", False)]
        return {
            "greeting": self.greet(),
            "quote": self.random_quote(),
            "streak": streak,
            "pending_goals": len(pending),
        }


def build_parser():
    p = argparse.ArgumentParser(description="Motivator CLI (OOP Python)")
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("motivate", help="Show a motivational message and status")
    sub.add_parser("ding", help="Mark you active for today (increase streak)")

    a_addq = sub.add_parser("add-quote", help="Add a new quote")
    a_addq.add_argument("quote", nargs="+", help="Quote text")

    a_listq = sub.add_parser("list-quotes", help="List saved quotes")

    a_setname = sub.add_parser("set-name", help="Set your display name")
    a_setname.add_argument("name", nargs="+", help="Your name")

    a_addgoal = sub.add_parser("add-goal", help="Add a new goal")
    a_addgoal.add_argument("title", nargs="+", help="Goal title")
    a_addgoal.add_argument("--by", dest="by", default="", help="Target date (YYYY-MM-DD)")

    a_listgoals = sub.add_parser("list-goals", help="List goals")
    a_complete = sub.add_parser("done", help="Mark goal done")
    a_complete.add_argument("id", type=int, help="Goal ID")

    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    persistence = Persistence()
    app = Motivator(persistence)

    if args.cmd == "motivate" or args.cmd is None:
        card = app.status_card()
        print(card["greeting"])
        print()
        print("Quote:", card["quote"])
        print()
        print(f"Streak: {card['streak']} hari. Tujuan terpending: {card['pending_goals']}")
        return 0

    if args.cmd == "ding":
        if app.mark_active_today():
            print("Nice! Aktivitas Anda hari ini tercatat. Tetap konsisten!")
        else:
            print("Sudah tercatat hari ini — tetap semangat!")
        return 0

    if args.cmd == "add-quote":
        q = " ".join(args.quote).strip()
        ok = app.add_quote(q)
        print("Added." if ok else "Quote sudah ada atau kosong.")
        return 0

    if args.cmd == "list-quotes":
        for i, q in enumerate(app.state.quotes, 1):
            print(f"{i}. {q}")
        return 0

    if args.cmd == "set-name":
        name = " ".join(args.name).strip()
        app.set_name(name)
        print(f"Name set to {name}")
        return 0

    if args.cmd == "add-goal":
        title = " ".join(args.title).strip()
        gid = app.add_goal(title, target_date=args.by)
        print(f"Goal added with id {gid}")
        return 0

    if args.cmd == "list-goals":
        goals = app.list_goals()
        if not goals:
            print("Tidak ada goals. Tambah satu dengan: add-goal \"Do something\"")
            return 0
        for g in goals:
            status = "✓" if g.done else " "
            td = f" (by {g.target_date})" if g.target_date else ""
            print(f"[{status}] {g.id}. {g.title}{td}")
        return 0

    if args.cmd == "done":
        ok = app.complete_goal(args.id)
        print("Marked done." if ok else "Goal tidak ditemukan.")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
