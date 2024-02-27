from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path(r'weather_data\sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# 0 STATION
# 1 NAME
# 2 DATE
# 3 AWND
# 4 PGTM
# 5 PRCP
# 6 TAVG
# 7 TMAX
# 8 TMIN
# 9 WDF2
# 10 WDF5
# 11 WSF2
# 12 WSF5
# 13 WT01
# 14 WT02
# 15 WT04
# 16 WT05
# 17 WT08
# 18 WT09

date, prcp = [], []

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rain = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        date.append(current_date)
        prcp.append(rain)



plt.style.use('ggplot')

fig, ax = plt.subplots()

ax.plot(date, prcp, color='red', alpha=0.5)


ax.set_title("Daily High and Low Temperatures, 2021\nDeath Valley, CA", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()