pip install folium
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from folium import GeoJson, GeoJsonTooltip
import json

# Cargar el CSV
csv_path = 'path/to/your/expanded_csv.csv'  # Cambia la ruta al CSV
data = pd.read_csv(csv_path)

# Cargar el GeoJSON (Tenancingo)
geojson_path = 'Tenancingo(1).geojson'  # Ruta al archivo GeoJSON
with open(geojson_path, 'r', encoding='utf-8') as file:
    geojson_data = json.load(file)

# Crear un mapa base centrado en Tenancingo
m = folium.Map(location=[18.923890, -99.588610], zoom_start=12, tiles='cartodbpositron')

# Añadir el contorno del municipio de Tenancingo desde el GeoJSON
GeoJson(
    geojson_data,
    style_function=lambda feature: {
        'fillColor': 'lightblue',
        'color': 'blue',
        'weight': 2,
        'fillOpacity': 0.2,
    },
    tooltip=GeoJsonTooltip(fields=['name'], aliases=['Zona'])
).add_to(m)

# Agrupamiento de marcadores para mayor claridad
marker_cluster = MarkerCluster().add_to(m)

# Diccionario de coordenadas para las zonas
zonas_coords = {
    "Acatzingo (Acatzingo de la Piedra)": [18.923890, -99.588610],
    "Agua Dulce": [18.880300, -99.552590],
    "Barrio Santa Teresa": [18.965850, -99.601490],
    "Chalchihuapan": [18.976940, -99.574720],
    # Agrega el resto de las zonas...
}

# Iterar sobre las filas del CSV y añadir marcadores al mapa
for _, row in data.iterrows():
    zona = row['Zona']
    delito = row['Delito']
    incidentes = row['Número de Incidentes']
    fecha = row['Fecha']
    
    # Obtener coordenadas de la zona
    coords = zonas_coords.get(zona)
    if coords:
        # Crear un marcador para cada incidente
        popup_text = f"""
        <b>Zona:</b> {zona}<br>
        <b>Delito:</b> {delito}<br>
        <b>Fecha:</b> {fecha}<br>
        <b>Número de Incidentes:</b> {incidentes}
        """
        folium.Marker(
            location=coords,
            popup=popup_text,
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(marker_cluster)

# Guardar el mapa en un archivo HTML
m.save('Tenancingo_Expanded_Incidents_Map.html')
print("Mapa guardado como 'Tenancingo_Expanded_Incidents_Map.html'")
