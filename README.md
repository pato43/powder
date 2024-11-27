# powder

Mapa de Incidentes en Tenancingo

Este proyecto utiliza Streamlit para desplegar un mapa interactivo de incidentes en Tenancingo y sus zonas aledañas. Se basa en datos de delitos y un archivo GeoJSON que define el contorno del municipio.
Características

    Mapa interactivo: Los usuarios pueden explorar incidentes marcados en las zonas de Tenancingo.
    Marcadores dinámicos: Cada marcador incluye información detallada, como el delito, la fecha y el número de incidentes.
    Contorno del municipio: Un GeoJSON resalta el área de Tenancingo con un estilo visual atractivo.
    Acceso gratuito: Se despliega en Streamlit Cloud, accesible mediante un enlace compartido.

Archivos del Proyecto

    app.py: Archivo principal que contiene el script para generar el mapa interactivo con Streamlit.
    expanded_csv.csv: Archivo CSV con los datos de los incidentes.
    Tenancingo(1).geojson: Archivo GeoJSON con el contorno del municipio de Tenancingo.

Cómo Ejecutar Localmente

    Clona este repositorio:

git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio

Instala las dependencias necesarias:

pip install -r requirements.txt

Ejecuta la aplicación:

    streamlit run app.py

    Abre el navegador en http://localhost:8501 para ver la aplicación.

Despliegue en Streamlit Cloud

    Sube este repositorio a GitHub.
    Despliega en Streamlit Cloud:
        Inicia sesión en Streamlit Cloud.
        Selecciona este repositorio de GitHub.
        Configura app.py como archivo principal.
    Obtén tu enlace:
        Una vez desplegada, tu aplicación estará disponible en un enlace como:
        https://nombreproyecto.streamlit.app

Estructura del CSV

El archivo CSV debe tener la siguiente estructura:

Fecha,Delito,Zona,Número de Incidentes
2024-12-01,Robo a transeúnte sin violencia,Acatzingo (Acatzingo de la Piedra),20
2024-12-01,Robo a transeúnte con violencia,Acatzingo (Acatzingo de la Piedra),15
...

    Fecha: Fecha del incidente.
    Delito: Tipo de delito registrado.
    Zona: Zona donde ocurrió el incidente.
    Número de Incidentes: Cantidad de incidentes registrados en esa zona.

Requisitos

    Python 3.8+
    Dependencias necesarias:
        streamlit
        pandas
        folium
        streamlit-folium

Licencia

Este proyecto está bajo la licencia MIT. Si utilizas o modificas este trabajo, da el crédito correspondiente.
Créditos

    Desarrollado por [Tu Nombre].
    Contáctame en: [tu.email@correo.com].

Enlace de la Aplicación

Accede al Mapa de Incidentes
