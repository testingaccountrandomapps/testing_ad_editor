import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import re
from babel.numbers import parse_decimal
import string 
import locale
locale.setlocale(locale.LC_ALL, 'C')
import csv
import spacy
nlp = spacy.load('en_core_web_sm')
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from bs4 import BeautifulSoup as bs
from csv import DictWriter
import template_retrieval



st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
def main():
    menu =["Template Selection","Gearbox","Tattoo Parlour","Funeral Care"]
    with st.sidebar:
      #  url_search = st.text_input("//TODO Database URL")
        st.subheader("Main Menu")
        choice = st.selectbox("Menu List",menu)
       
    st.header("Ad editor template application 1.0")

    st.write("The current proof of concept demonstrator can be used select csv templates to import into google ads editor" )
    st.write("Use the side bar on the left to select: the desired template" )

    st.title("Template")  
    

    if choice == "Tattoo Parlour":
        
        st.subheader("Tattoo Parlour")
        tattoo_df = pd.read_csv('Inkredible Tattoo test.csv')
        st.dataframe(tattoo_df)
        tattoo_ad_editor_csv = template_retrieval.convert_df(tattoo_df)
        st.download_button("Press to Download",tattoo_ad_editor_csv,"tattooist_template.csv","text/csv",key='download-csv')

    elif choice == "Gearbox":
        st.subheader("Gearbox")
        gearbox_df = pd.read_csv('Halifax Gearbox N Clutch Center Lt Test.csv')
        st.dataframe(gearbox_df)
        gearbox_ad_editor_csv = template_retrieval.convert_df(gearbox_df)
        st.download_button("Press to Download",gearbox_ad_editor_csv,"gearbox_df_template.csv","text/csv",key='download-csv')

    elif choice == "Funeral Care":
        st.subheader("Funeral Care")
        funeral_df = pd.read_csv('Hillier Funeral Care Test.csv')
        st.dataframe(tattoo_df)
        funeral_ad_editor_csv = template_retrieval.convert_df(funeral_df)
        st.download_button("Press to Download",funeral_ad_editor_csv,"funeral_care.csv","text/csv",key='download-csv')

  
  
if __name__ == "__main__":
    main()



