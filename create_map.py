import folium


def create_map(latitude, longitude):
    ido_keido = []
    ido_keido.append(latitude)
    ido_keido.append(longitude)
    
    map = folium.Map(location=ido_keido, zoom_start=15)
    folium.Marker(location=ido_keido).add_to(map)
    map = map._repr_html_()
    
    return map
    
if __name__ == '__main__':
    map = create_map(36.405786242850546, 140.5966370017051)
    print(map)
    
    