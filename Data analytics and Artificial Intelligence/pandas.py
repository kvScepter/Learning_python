import pandas as pd

#Read the data from the csv file and create a DataFrame from it.
mj = pd.read_csv("earthquakes.csv", delimiter=",")

# Remove the following columns from the DataFrame: Magnitude Seismic Stations, Azimuthal Gap, Horizontal Distance and Horizontal Error.
mj.drop(["Magnitude Seismic Stations","Azimuthal Gap","Horizontal Distance","Horizontal Error"],inplace=True,axis=1)

# Filter data from the DataFrame so that only rows matching the following criteria will be shown:
# - Source must be US
# - Magnitude value must be over 7.8
# - ID value must start with the string "USP0007"
mj = mj[(mj["Source"].str.startswith(("US"))) & (mj["Magnitude"] > 7.8) & (mj["ID"].str.match(("USP0007")))]

# Create a new column to the tenth column position called Grade which will have values from the following formula: ("Magnitude" * "Depth") / "Root Mean Square". 
# Results in this column should be presented with three decimals.
mj.insert(loc=10, column="Grade", value=(mj["Magnitude"] * mj["Depth"] / mj["Root Mean Square"]))
mj.round({"Grade" : 3})

# Filter out events that have occurred before the 1st of January in 1996. Then write the resulting DataFrame into csv file called filtered_earthquake_data.csv.
filtered_mj = mj.loc[mj.Date < ("1/1/1996")]
filtered_mj.to_csv("filtered_earthquake_data.csv")
