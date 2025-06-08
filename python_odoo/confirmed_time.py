if record.pr_request_date and record.confirmed_time:
    delta = record.confirmed_time - record.pr_request_date
    days = delta.days
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    record.approval_gap_time = f"{days} day {hours} hrs {minutes} Minute {seconds} Second"