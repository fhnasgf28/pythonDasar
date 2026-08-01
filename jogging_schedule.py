#!/usr/bin/env python3
"""
Simple Jogging Schedule CLI

Features:
- add a schedule (one-off or repeating daily/weekly)
- list schedules
- remove schedules by id
- run a simple loop that checks schedules and prints a notification when it's time

Storage: schedules.json in the same directory

Usage examples:
  python jogging_schedule.py add --time "2026-08-02 06:30" --duration 30 --note "Jogging pagi" --repeat none
  python jogging_schedule.py add --time "06:30" --duration 30 --note "Jogging pagi" --repeat daily
  python jogging_schedule.py list
  python jogging_schedule.py remove --id <schedule-id>
  python jogging_schedule.py run

"""

import argparse
import json
import os
import uuid
from datetime import datetime, date, time as dtime, timedelta
import time as time_module

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEDULE_FILE = os.path.join(BASE_DIR, "schedules.json")
CHECK_INTERVAL_SECONDS = 20
TRIGGER_WINDOW_SECONDS = 60


def load_schedules():
    if not os.path.exists(SCHEDULE_FILE):
        return []
    with open(SCHEDULE_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_schedules(schedules):
    with open(SCHEDULE_FILE, "w", encoding="utf-8") as f:
        json.dump(schedules, f, indent=2, ensure_ascii=False)


def parse_time_arg(time_str, repeat):
    """
    Accepts either full datetime 'YYYY-MM-DD HH:MM' for one-off events or 'HH:MM' for repeats.
    Returns a dict describing the schedule's time fields.
    """
    if repeat == "none":
        # expect full datetime
        try:
            dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
            return {"datetime": dt.isoformat()}
        except ValueError:
            raise ValueError("For one-off events (repeat none) provide time as 'YYYY-MM-DD HH:MM'")
    else:
        # expects HH:MM
        try:
            t = datetime.strptime(time_str, "%H:%M").time()
            return {"time": t.strftime("%H:%M")}
        except ValueError:
            raise ValueError("For repeating events provide time as 'HH:MM' (24-hour)")


def add_schedule(args):
    schedules = load_schedules()
    time_info = parse_time_arg(args.time, args.repeat)
    item = {
        "id": str(uuid.uuid4()),
        "created_at": datetime.utcnow().isoformat(),
        "duration_min": int(args.duration) if args.duration else None,
        "note": args.note or "",
        "repeat": args.repeat,
        **time_info,
        # last_triggered helps avoid multiple triggers within the same day/minute
        "last_triggered": None
    }
    # optional weekday for weekly repeat (0=Monday ... 6=Sunday)
    if args.repeat == "weekly":
        if args.weekday is None:
            raise ValueError("When repeat is 'weekly' you must provide --weekday (0=Mon .. 6=Sun)")
        item["weekday"] = int(args.weekday)

    schedules.append(item)
    save_schedules(schedules)
    print("Added schedule:")
    print_item(item)


def print_item(item, index=None):
    if index is not None:
        prefix = f"[{index}] "
    else:
        prefix = ""
    print(prefix + f"id: {item['id']}")
    if item.get("datetime"):
        print(prefix + f"  when: {item['datetime']}")
    elif item.get("time"):
        t = item["time"]
        if item.get("repeat") == "daily":
            print(prefix + f"  when (daily at): {t}")
        elif item.get("repeat") == "weekly":
            wd = item.get("weekday")
            wdname = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"][wd] if wd is not None else "?"
            print(prefix + f"  when (weekly {wdname} at): {t}")
        else:
            print(prefix + f"  when: {t}")
    print(prefix + f"  duration_min: {item.get('duration_min')}")
    print(prefix + f"  repeat: {item.get('repeat')}")
    if item.get("note"):
        print(prefix + f"  note: {item.get('note')}")
    if item.get("last_triggered"):
        print(prefix + f"  last_triggered: {item.get('last_triggered')}")


def list_schedules(_args):
    schedules = load_schedules()
    if not schedules:
        print("No schedules found.")
        return
    for i, s in enumerate(schedules, start=1):
        print_item(s, index=i)
        print("")


def remove_schedule(args):
    schedules = load_schedules()
    before = len(schedules)
    schedules = [s for s in schedules if s["id"] != args.id]
    after = len(schedules)
    if before == after:
        print("No schedule found with id:", args.id)
    else:
        save_schedules(schedules)
        print(f"Removed schedule {args.id}")


def next_occurrence_for(item, now=None):
    # returns a datetime for the next occurrence (UTC naive local)
    now = now or datetime.now()
    if item.get("datetime") and item.get("repeat") == "none":
        dt = datetime.fromisoformat(item["datetime"])
        return dt
    if item.get("time"):
        hour, minute = map(int, item["time"].split(":"))
        if item.get("repeat") == "daily":
            candidate = datetime.combine(now.date(), dtime(hour=hour, minute=minute))
            if candidate < now - timedelta(seconds=1):
                candidate = candidate + timedelta(days=1)
            return candidate
        elif item.get("repeat") == "weekly":
            wd = int(item.get("weekday", 0))
            days_ahead = (wd - now.weekday() + 7) % 7
            candidate = datetime.combine((now + timedelta(days=days_ahead)).date(), dtime(hour=hour, minute=minute))
            if candidate < now - timedelta(seconds=1):
                candidate = candidate + timedelta(days=7)
            return candidate
        else:
            # treat as one-off today or tomorrow
            candidate = datetime.combine(now.date(), dtime(hour=hour, minute=minute))
            if candidate < now - timedelta(seconds=1):
                candidate = candidate + timedelta(days=1)
            return candidate
    return None


def run_loop(_args):
    print("Starting schedule runner. Press Ctrl+C to stop.")
    try:
        while True:
            schedules = load_schedules()
            now = datetime.now()
            changed = False
            for item in schedules[:]:
                next_dt = next_occurrence_for(item, now=now)
                if next_dt is None:
                    continue
                diff = (next_dt - now).total_seconds()
                # If within trigger window, and not already triggered for this date, then trigger
                trigger_date_tag = next_dt.strftime("%Y-%m-%d")
                last = item.get("last_triggered")
                if abs(diff) <= TRIGGER_WINDOW_SECONDS and last != trigger_date_tag:
                    # Trigger
                    print("\n=== JOGGING REMINDER ===")
                    print(f"When: {next_dt.strftime('%Y-%m-%d %H:%M')}")
                    print(f"Note: {item.get('note')}")
                    if item.get('duration_min'):
                        print(f"Planned duration: {item.get('duration_min')} minutes")
                    print("========================\n")
                    # mark triggered
                    item['last_triggered'] = trigger_date_tag
                    changed = True
                    # if one-off, remove it
                    if item.get('repeat') == 'none' and item.get('datetime'):
                        schedules = [s for s in schedules if s['id'] != item['id']]
                        changed = True
            if changed:
                save_schedules(schedules)
            time_module.sleep(CHECK_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nRunner stopped by user.")


def build_parser():
    p = argparse.ArgumentParser(description="Jogging schedule manager")
    sub = p.add_subparsers(dest="cmd")

    pa = sub.add_parser("add", help="Add a schedule")
    pa.add_argument("--time", required=True, help="Time for the schedule. For one-off use 'YYYY-MM-DD HH:MM'. For repeats use 'HH:MM'.")
    pa.add_argument("--duration", type=int, default=30, help="Duration in minutes (optional)")
    pa.add_argument("--note", type=str, default="", help="Note for the schedule")
    pa.add_argument("--repeat", choices=["none","daily","weekly"], default="none", help="Repeat type")
    pa.add_argument("--weekday", type=int, choices=list(range(0,7)), help="Weekday for weekly repeat (0=Mon..6=Sun)")

    pl = sub.add_parser("list", help="List schedules")

    pr = sub.add_parser("remove", help="Remove schedule by id")
    pr.add_argument("--id", required=True, help="Schedule id to remove")

    prun = sub.add_parser("run", help="Run schedule checker (prints reminders)")

    return p


def main():
    parser = build_parser()
    args = parser.parse_args()
    if args.cmd == "add":
        try:
            add_schedule(args)
        except Exception as e:
            print("Error adding schedule:", e)
    elif args.cmd == "list":
        list_schedules(args)
    elif args.cmd == "remove":
        remove_schedule(args)
    elif args.cmd == "run":
        run_loop(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
