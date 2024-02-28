from pathlib import Path
import csv
import plotly.express as px


path = Path(r'eq_data\world_fires_1_day.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# 0 latitude
# 1 longitude
# 2 brightness
# 3 scan
# 4 track
# 5 acq_date
# 6 acq_time
# 7 satellite
# 8 confidence
# 9 version
# 10 bright_t31
# 11 frp
# 12 daynight

lons, lats, brightness = [], [], []

for row in reader:
        lons.append(float(row[1]))
        lats.append(float(row[0]))
        brightness.append(float(row[2]))





title = 'Worldwide Fires'
fig = px.scatter_geo(lat=lats, lon=lons, size=brightness, title=title,
                    color=brightness,
                    color_continuous_scale='Viridis',
                    labels={'color':'Brightness'},
                    projection='natural earth',
)

fig.write_html('figure.html', auto_open=True)