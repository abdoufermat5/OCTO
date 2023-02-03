import os
import re
import spacy

import streamlit as st
from PIL import Image


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


def show_sidebar_footer():
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

    st.sidebar.markdown("<br/>"*6, unsafe_allow_html=True)
    st.sidebar.markdown("""<i>Université Paris-Saclay - Master 2 Data Scale</i>""", unsafe_allow_html=True)
    paris_saclay = Image.open(os.path.join(data_path, "assets", "uvsq.png"))
    st.sidebar.image(paris_saclay, use_column_width=True)


stopwords = ['yourself', 'yourselves', 'herself', 'themselves',
             'himself', 'ourselves',
             'myself', 'between', 'whom', 'is', "she", 'here', 'your', 'each', 'we', 'he',
             'my', 'you', 'are', 'them', 'other', 'and', 'an', 'their', 'can', 'she', 'these',
             'ours', 'while', 'have', 'when', 'were', 'who', 'they', 'has', 'before', 'yours',
             "it", 'on', 'now', 'her', 'an', 'from', "would", 'how', 'the', 'or', 'doing',
             'his', 'was', 'through', 'own', 'theirs', 'me', 'him', 'be', 'same', 'it', 'its',
             'which', 'there', 'our', 'this', 'hers', 'being', 'did', 'those', 'i', 'does', 'will',
             'shall', 's', 't', 'n', 'd', 'e', 'u', 'x', 'am', 'get', 've']

