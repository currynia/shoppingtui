
import math
import geocoder
import pandas

def get_loc():
    g = geocoder.ip('me')
    return g.latlng
    
def parse_shoppingmall_data() -> pandas.DataFrame:
    return pandas.read_csv('./data/merged_output.csv')
   

def distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    
    
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
   
    distance = R * c
    return round(distance,3)