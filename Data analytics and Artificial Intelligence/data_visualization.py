import pandas as pd
import json

# Read the earthquakes.csv file and save its content into a variable. Then use bar chart to visualize magnitude values being 8.2 
#or over so that date values will be presented in x-axle and magnitude in y-axle
mj = pd.read_csv("earthquakes.csv", delimiter=",")
mj[mj.Magnitude >= 8.2].plot.bar(x="Date", y="Magnitude", figsize=(10,5), ylabel="Magnitude", title="Magnitudes over 8.2")

#Filter earthquake data so that all occurrances between time values 10:00 - 12:00 will be visualized with line chart. 
#Group this data so that the average (mean) depth values will be presented for each source
mj[mj.Time.between("10", "12")].plot.line(x="Time", y="Depth", figsize=(10,7), ylim=(100,700))
