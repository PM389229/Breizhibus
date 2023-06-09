import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from BreizhibusData import db

cursor=db.cursor()

    # Page 1 - Horaires par lignes
def page_horaires_par_lignes():
    st.title("Application Breizhibus")
    st.header("Horaires par lignes")
    st.image('/home/pm3829/iadev-python/ProjetBreizhibus/reseau_bus.jpg', use_column_width=True)

    # Récupérer la liste des lignes

    cursor.execute("SELECT DISTINCT ligne FROM streamlit_breizhibus_Horaires")
    lignes = cursor.fetchall()
    lignes = [ligne[0] for ligne in lignes]

    # Sélection de la ligne par l'utilisateur
    selected_ligne = st.selectbox("Sélectionnez une ligne :", lignes)

    # Récupérer les horaires pour la ligne sélectionnée
    cursor.execute("SELECT * FROM streamlit_breizhibus_Horaires WHERE ligne = %s", (selected_ligne,))
    horaires = cursor.fetchall()

    # Afficher les horaires
    st.subheader(f"Horaires pour la ligne {selected_ligne}:")
    for horaire in horaires:
        st.write(horaire[1])
    
# Appel de la fonction pour afficher la page des horaires par lignes
page_horaires_par_lignes()