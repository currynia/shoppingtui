import folium
from utils import get_loc
import webbrowser
import os

def open_map():
    loc = get_loc()
    m = folium.Map(location=loc, zoom_start=13)
    folium.Marker(loc, popup="Me").add_to(m)
    file_path = "map.html"
    m.save(file_path)
    webbrowser.open('file://' + os.path.realpath(file_path))
