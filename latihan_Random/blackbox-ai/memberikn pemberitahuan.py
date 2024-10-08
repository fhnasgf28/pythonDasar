import win10toast

def send_notification(title, message):
    toaster = win10toast.ToastNotifier()
    toaster.show_toast(title, message, duration=10)

# Set the title and message for the notification
title = "Time to Study!"
message = "Don't forget to study for your exam!"

# Send the notification
send_notification(title, message)

from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Study Reminder",
        timeout=10
    )

# Set the title and message for the notification
title = "Time to Study!"
message = "Don't forget to study for your exam!"

# Send the notification
send_notification(title, message)

