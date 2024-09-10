import datetime
import time
from playsound import playsound
def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Alarm! Wake up!")
            playsound("morningwakealarm.wav") 
            playsound("morningwakealarm.wav")
            playsound("morningwakealarm.wav")
            break
        time.sleep(1)  # Check every 1 second

def main():
    print("Welcome to Alarm Clock")
    print("Enter the time to set the alarm (HH:MM:SS format):")
    alarm_time = input("> ")

    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM:SS format.")
        return

    print(f"Alarm set for {alarm_time}. Waiting for alarm...")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
