import psutil
from win10toast import ToastNotifier
import time

def monitor_battery():
    toaster = ToastNotifier()
    battery = psutil.sensors_battery()
    
    while True:
        battery = psutil.sensors_battery()
        
        percent = battery.percent
        plugged = battery.power_plugged
        
        if plugged:
            if percent == 100:
                toaster.show_toast("Battery Full", "Your battery is fully charged.", duration=10)
        else:
            if percent < 20:
                toaster.show_toast("Low Battery Warning", f"Your battery is running low: {percent}% remaining.", duration=10)
        
        # Check every 5 minutes
        time.sleep(300)  # 300 seconds = 5 minutes

if __name__ == "__main__":
    monitor_battery()
