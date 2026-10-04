import csv
import os
import time
from datetime import datetime

LOG_FILE = "/home/joshbruce1107/logger/cpu_temp.csv"
INTERVAL_SECONDS = 60  # change to 60 once it works

def read_cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp") as f:
        return int(f.read()) / 1000

def main():
    new_file = not os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["timestamp", "cpu_temp_c"])
        while True:
            writer.writerow([datetime.now().isoformat(timespec="seconds"),
                             round(read_cpu_temp(), 1)])
            f.flush()
            time.sleep(INTERVAL_SECONDS)

main()
