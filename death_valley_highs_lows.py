from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# 0 STATION
# 1 NAME
# 2 DATE
# 3 TMAX
# 4 TMIN
# 5 TOBS

date, highs, lows = [], [], []

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        date.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('ggplot')

fig, ax = plt.subplots()

ax.plot(date, highs, color='red', alpha=0.5)
ax.plot(date, lows, color='blue', alpha=0.5)
ax.fill_between(date, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("Daily High and Low Temperatures, 2021\nDeath Valley, CA", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
    
