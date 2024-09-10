'''
from plyer import notification
#import time
#time.sleep(5)
notification.notify
{
    "Title" : "Namaste",
    "Text"  : "This is a sample notification for testing purpose"
}'''
from win10toast import ToastNotifier

toaster = ToastNotifier()
#toaster.show_toast("Namaste", "Hi Ramana adhi na pilla ra adhi na pilla", duration=10)
Notifications={"Hello":"This is my first remainder","Hi":"This is my second remainder","Namaste":"This is my third remainder"}
for msg,title in Notifications.items():
    toaster.show_toast(msg,title)