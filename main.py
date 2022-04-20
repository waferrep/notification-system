import time
from notifications import notification_box

#time is taken in seconds so need to multiply by 60 
def sleep_minutes(minutes):
    time.sleep(minutes * 60)
def sleep_hours(minutes):
    time.sleep(minutes * 3600)
def sleep_days(minutes):
    time.sleep(minutes * 86400)
    
reminder = input("Please enter a reminder: ")
minutes_or_hours = input("Enter D for days, H for hours, or M for minutes: ").lower()

while minutes_or_hours != 'm' and minutes_or_hours != 'h' and minutes_or_hours and minutes_or_hours != 'd': #if input isnt one of these ask again for input
    print("Invalid input, try again")
    minutes_or_hours = input("Enter D for days, H for hours, or M for minutes: ").lower()

while True: #checks if user input is an int (any exception thrown makes user ask again,  could just do ValueError but i think catching all exceptions is fine)
    try:
        timeamt = int(input(f"In how many minutes, days, or hours do you want to be reminded? "))
        break
    except:
        print("Invalid input, try again")

if minutes_or_hours == 'm':
    sleep_minutes(timeamt)
    print("Notification queued.")
elif minutes_or_hours == 'h':
    sleep_hours(timeamt)
    print("Notification queued.")
elif minutes_or_hours == 'd':
    sleep_days(timeamt)
    print("Notification queued.")

notification_box(reminder)

