import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("cpu_temp.csv", parse_dates=["timestamp"])

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df["timestamp"], df["cpu_temp_c"], linewidth=1)
for t, label in [("2026-10-04 09:50:45", "reboot 1"), ("2026-10-04 10:04:10", "reboot 2")]:
    ax.axvline(pd.Timestamp(t), color="red", linestyle="--", linewidth=1)
    ax.text(pd.Timestamp(t), ax.get_ylim()[1], label, color="red", ha="right", va="top")
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
ax.set_xlabel("Time (BST, 4 Oct 2026)")
ax.set_ylabel("CPU temperature (°C)")
ax.set_title("Pi Zero 2 W idle CPU temperature, ~9 hours")
fig.tight_layout()
fig.savefig("cpu_temp.png", dpi=150)
plt.show()