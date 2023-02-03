import os

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# config
st.set_page_config(
    page_title="Analyse de Sentiment",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.markdown("## Analyse de Sentiment")
st.sidebar.markdown("---")
st.sidebar.markdown("""Dans cette section, vous pouvez voir les différentes visualisations et statistiques sur
les données""")
st.header("Visualisation des donnees")
# Load the data
# get the path of the train_data.csv file in data folder which is two levels down from the current file using os
# current directory
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(current_dir, "data", "result.csv")

data = pd.read_csv(file_path)

# choose a user and show his sentiment inside a barplot
# choose user
topic = ["SNCF", 'RATP', "NAVIGO"]
user = st.selectbox("Choisissez un topic", topic)
# filter data
# plot
fig, ax = plt.subplots()
ax.bar(data['SENTIMENT'].value_counts().index, data['SENTIMENT'].value_counts())
ax.set_title(f"Sentiment sur le topic {user}")
ax.set_xlabel('Sentiment')
ax.set_ylabel('Nombre')
ax.grid(True)
st.pyplot(fig)