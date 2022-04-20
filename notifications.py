from win10toast import ToastNotifier

#Maybe i should schedule a calendar event instead? That way if program stops u dont lose ur notification

def notification_box(userInput):
    toast = ToastNotifier()
    toast.show_toast(
        "Reminder",
        f"{userInput}",
        duration = 10,
        threaded = True
    )