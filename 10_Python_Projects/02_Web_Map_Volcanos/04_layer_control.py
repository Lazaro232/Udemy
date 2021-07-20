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

fgv = folium.FeatureGroup(name="Volcanoes")

for latitude, longitude, elevation in zip(latitude_list,
                                          longitude_list,
                                          elevation_list):
    iframe = folium.IFrame(html=HTML % str(elevation),
                           width=200,
                           height=100)

    fgv.add_child(folium.CircleMarker(location=[latitude, longitude],
                                      radius=10,
                                      popup=folium.Popup(iframe),
                                      fill_color=set_marker_color(elevation),
                                      color='grey',
                                      fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")


fgp.add_child(folium.GeoJson(
    data=(open('world.json', 'r', encoding='utf-8-sig').read()),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                              else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                              else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("Map1.html")


'''
Anotaçoes

1) Caso NAO tivesse sido criada a feature group (fgv e fgp) apareceriam
62 vulcoes no LayerControl. Usando folium.FeatureGroup, pode-se agrupar
os elementos do tipo .child
'''
