import pandas as pd
from utils import parse_shoppingmall_data
mall_data = parse_shoppingmall_data()

df = pd.DataFrame(mall_data[1:], columns=["Mall Name", "LATITUDE", "LONGITUDE"], )
# Function to determine region
def get_region(lat, lon):
    lat = float(lat)
    lon = float(lon)
    if lat > 1.42:
        return "North"
    elif lat < 1.30:
        if lon < 103.85:
            return "Southwest"
        else:
            return "South"
    elif 1.30 <= lat <= 1.42:
        if lon < 103.82:
            return "West"
        elif lon > 103.92:
            return "East"
        else:
            return "Central"
    return "Unknown"

# Apply the region assignment
df["Region"] = df[1:].apply(lambda row: get_region(row["LATITUDE"], row["LONGITUDE"]), axis=1)

# Save the updated data
output_path = "data/augmented_singapore_malls.csv"
df.to_csv(output_path, index=False)

