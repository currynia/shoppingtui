import folium
from utils import get_loc
from options.num import OptionsNum
import webbrowser
import os

def text():
    return f'{OptionsNum.MAP.value}. Open map.'

def execute():
    loc = get_loc()
    if loc is None:
        print("Unable to get location.\n")
    else:
        
        m = folium.Map(location=loc, zoom_start=13)
        folium.Marker(loc, popup="Me").add_to(m)
        file_path = "map.html"
        m.save(file_path)
        webbrowser.open('file://' + os.path.realpath(file_path))
