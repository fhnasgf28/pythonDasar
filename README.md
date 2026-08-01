# Jogging Schedule CLI

Simple Python CLI to manage jogging schedules. It stores schedules in `schedules.json` and can run a background loop that prints reminders when it's time to jog.

Features:
- Add one-off or repeating schedules (daily or weekly)
- List schedules
- Remove schedules
- Run a simple checker that prints reminders

Usage

1. Add a one-off schedule:

  python jogging_schedule.py add --time "2026-08-02 06:30" --duration 30 --note "Jogging pagi" --repeat none

2. Add a daily repeating schedule (time only):

  python jogging_schedule.py add --time "06:30" --duration 30 --note "Jogging pagi" --repeat daily

3. Add a weekly repeating schedule (weekday is 0=Mon .. 6=Sun):

  python jogging_schedule.py add --time "06:30" --duration 30 --note "Weekend jog" --repeat weekly --weekday 6

4. List schedules:

  python jogging_schedule.py list

5. Remove a schedule by id:

  python jogging_schedule.py remove --id <schedule-id>

6. Run the checker (prints reminders):

  python jogging_schedule.py run

Notes

- The script stores data in `schedules.json` in the same directory as the script.
- No external dependencies required. The runner checks schedules every 20 seconds and prints reminders when a schedule is within 60 seconds of the scheduled time. For repeated schedules, it records the last triggered date to avoid duplicate notifications on the same day.

License

MIT
