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

with st.expander("Voir les données"):
    st.write(data)

# diagrammme pie chart
st.subheader("Diagramme pie chart de la distribution des sentiments")
fig1, ax1 = plt.subplots()
ax1.pie(data['SENTIMENT'].value_counts(), labels=data['SENTIMENT'].value_counts().index, autopct='%1.1f%%',
         shadow=True, startangle=90)

st.pyplot(fig1)