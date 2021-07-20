import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
latitude_list = list(data["LAT"])
longitude_list = list(data["LON"])
elevation_list = list(data["ELEV"])
# Usado para estilizar o POPUP do marcador
HTML = """<h4>Volcano information:</h4>
Height: %s m
"""


def set_marker_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for latitude, longitude, elevation in zip(latitude_list,
                                          longitude_list,
                                          elevation_list):
    iframe = folium.IFrame(html=HTML % str(elevation),
                           width=200,
                           height=100)
    fg.add_child(folium.Marker(location=[latitude, longitude],
                               popup=folium.Popup(iframe),
                               icon=folium.Icon(color=set_marker_color(elevation))))

map.add_child(fg)
map.save("Map1.html")
