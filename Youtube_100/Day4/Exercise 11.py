
from plyer import notification
import time

def reminder():
    notification.notify(
        title="Reminder",
        message="Drink Water!!",
        timeout=10,
    )

while True:
    reminder()
    time.sleep(5)

