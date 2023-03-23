import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json
import requests
from PIL import Image
import os.path
import numpy as np
from zipfile import ZipFile
import base64
import io
import streamlit as st
from streamlit.elements.image import image_to_url, MAXIMUM_CONTENT_WIDTH
from PIL import Image
import pandas as pd
#import plotly.express as px
import plotly.graph_objects as go


@st.cache_data
def load_data():
    data = pd.read_csv('sammelstellen.csv', sep= ";")
    return data

samstelstellen = load_data()


# st.title("Wilkommen bei der Sperrgutentsorgung St. Gallen")

# location = get_geolocation()
# print(location)
# latitudes = []
# longitudes = []
# names = []

# for i in range(0, len(samstelstellen)):
#     newStrings = samstelstellen["Geo Point"][i].split(",")
    
#     latitudes.append(newStrings[0])
#     longitudes.append(newStrings[1])
#     names.append(samstelstellen["Standort"][i])



# if not location:

#     st.header("Bitte geben Sie uns folgende Angaben:")
#     strasse = st.text_input("Strasse")
#     nummer = st.text_input("Nummer")
#     plz = st.text_input("Postleitzahl")

#     location_input = strasse + nummer + plz 
#st.header("Ihre Adresse lautet: {}".format(location))

tab1, tab2, tab3= st.tabs(["Trash collector", "Recycling near you", "Too good to Throw"])

with tab1:
    
#st.header("Laden Sie Bitte ein Foto des Sperrguts hoch:")
#picture = st.camera_input("Take a picture")

#if picture:
#    test = Image.open(picture)
#    width, height = test.size  # width is needed for image_to_url()
#    if width > MAXIMUM_CONTENT_WIDTH:
#        width = MAXIMUM_CONTENT_WIDTH  # width is capped at 2*730 https://github.com/streamlit/streamlit/blob/949d97f37bde0948b57a0f4cab7644b61166f98d/lib/streamlit/elements/image.py#L39
#    #st.image(picture)

#st.write(
#        image_to_url(
#            image=picture,
#            width=width,
#            clamp=False,
#            channels="RGB",
#            output_format=picture.type,
#            image_id=picture.id,  # each uploaded file has a file.id
#        )
#    ) # each uploaded file has a file.id)

# part_url = image_to_url(
#             image=picture,
#             width=width,
#             clamp=False,
#             channels="RGB",
#             output_format=picture.type,
#             image_id=picture.id,)  # each uploaded file has a file.id)

# leading_url = "https://dave-spontani-start-hack-23-test-file-nk8fhe.streamlit.app/~/+/"

#     #full_url = str(leading_url) + str(part_url)

# st.write(part_url)
# st.write(leading_url)

# api_key = "acc_816120464915b83"
# api_secret = "d82827db621dc470e5f03c08bc55abad"
# image_path = '/path/to/your/image.jpg'

# response = requests.post(
#     'https://api.imagga.com/v2/tags',
#     auth=(api_key, api_secret),
#     files={'image': open(image_path, 'rb')})
# print(response.json())
    location = get_geolocation()

    st.header("Bitte geben Sie uns noch zusätzliche Angaben zu dem Sperrgut:")

    gewicht = st.radio(
        "Ist das Objekt schwerer als 30kg?",
        ('Ja', "Nein"))

    if gewicht == "Ja":
        gewicht = 1
    else: 
        gewicht = 1

    länge = st.radio(
        "Ist das mehr als zwei Meter lang?",
        ('Ja', "Nein"))

    if länge == "Ja":
        länge = 1
    else:
        länge = 0

    breite = st.radio(
        "Ist das mehr als 90 cm Breit?",
        ('Ja', "Nein"))

    if breite == "Ja":
        breite = 1
    else: 
        breite = 0

    höhe = st.radio(
        "Ist das mehr als 40 cm Hoch?",
        ('Ja', "Nein"))

    if höhe == "Ja":
        höhe = 1
    else: 
        höhe = 0


    submit_button = st.button("Absenden")




    if submit_button:

        total = gewicht + länge + breite + höhe

        kostenvorschlag = 20

        st.write("Der Kostenvorschlag für dieses Objekt ist {}".format(kostenvorschlag))


# Returns user's location after asking for permission when the user clicks the generated link with the given text

# The URL parts of the page
#location_json = get_page_location()

with tab2:
    # location values hardcoded lat = 47.4335382954281
    # lon = 9.383928186686626
    # recycling center = 47.41847764687886, 9.36442953556214


    st.header("Here you can find the nearest recycling center to you")
    
    st.write(type(location))

    if location:
        lon = location['coords']['longitude']
        lat = location['coords']['latitude']

        st.header(f"Your location is: {lon}, {lat}")





        fig = go.Figure(go.Scattermapbox(
            lat=[47.4335382954281, 47.41847764687886],
            lon=[9.383928186686626, 9.36442953556214],
            mode='markers',
            marker=go.scattermapbox.Marker(
            size=13, color=["red", "green"], 
            ),
            text=["You", "Recycling center"],
        ))


        fig.update_layout(
            autosize=True,
            hovermode='closest',
            mapbox_style="open-street-map",
            mapbox=dict(
            center=go.layout.mapbox.Center(lat = location['coords']['latitude'],
            lon = location['coords']['longitude']),
            zoom=14
        ))
            
        st.plotly_chart(fig, use_container_width=True)





