import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector as mysqlpy
from BreizhibusData import db

cursor=db.cursor()


# Page 2 - Services internes
def page_services_internes():
    st.title("Application Breizhibus")
    st.header("Services internes de Breizhibus")
    
    # Chargement des données de fréquentations par lignes
    cursor.execute("SELECT streamlit_breizhibus_Lignes.nom AS Ligne, SUM(streamlit_breizhibus_Frequentations.nombre_passager) AS Total_Passagers FROM streamlit_breizhibus_Frequentations INNER JOIN streamlit_breizhibus_Horaires ON streamlit_breizhibus_Frequentations.horaires = streamlit_breizhibus_Horaires.id INNER JOIN streamlit_breizhibus_Lignes ON streamlit_breizhibus_Horaires.ligne = streamlit_breizhibus_Lignes.id GROUP BY streamlit_breizhibus_Lignes.nom;")
    frequentations_horaires = cursor.fetchall()
    frequentations_horaires = pd.DataFrame(frequentations_horaires, columns=['horaire', 'frequentations'])
    
    # Afficher le graphique des frequentations par lignes
    st.subheader("frequentations par lignes:")
    plt.bar(frequentations_horaires['horaire'], frequentations_horaires['frequentations'],color='red')
    plt.xlabel("lignes")
    plt.ylabel("frequentations")
    st.pyplot(plt)
    
    
    
    # Chargement des données de fréquentations par heures
    cursor.execute("SELECT streamlit_breizhibus_Horaires.heure AS Horaire, SUM(streamlit_breizhibus_Frequentations.nombre_passager) AS Total_Passagers FROM streamlit_breizhibus_Frequentations INNER JOIN streamlit_breizhibus_Horaires ON streamlit_breizhibus_Frequentations.horaires = streamlit_breizhibus_Horaires.id GROUP BY streamlit_breizhibus_Horaires.heure;")
    frequentations_heures = cursor.fetchall()
    frequentations_heures = pd.DataFrame(frequentations_heures, columns=['horaire', 'frequentations'])
    
    # Afficher le graphique linéaire des fréquentations par heures

    st.subheader("Fréquentations par heure:")
    plt.figure()
    plt.plot(frequentations_heures['horaire'], frequentations_heures['frequentations'],color='green')
    plt.xlabel("Horaire")
    #plt.ylabel("Fréquentations")
    #plt.title("Fréquentations par heure")
    plt.xticks(rotation=45) 
    st.pyplot(plt) 
    # Rotation des étiquettes de l'axe des x pour une meilleure lisibilité
    
    #affichage camembert des frequentations
    st.subheader("Camembert des fréquentations")
    plt.figure(figsize=(8, 8))  # Ajuster la taille du graphique
    plt.pie(frequentations_heures['frequentations'], labels=frequentations_heures['horaire'], autopct='%1.0f%%')
    plt.axis('equal')  # Assurer un cercle parfait
    st.pyplot(plt)
    
    # Récupérer les données de fréquentation par jours
    cursor.execute("SELECT streamlit_breizhibus_Frequentations.jour AS Jour, SUM(streamlit_breizhibus_Frequentations.nombre_passager) AS Total_Passagers FROM streamlit_breizhibus_Frequentations GROUP BY streamlit_breizhibus_Frequentations.jour;")
    frequentations_jours = cursor.fetchall()
    frequentations_jours = pd.DataFrame(frequentations_jours, columns=['Jour', 'frequentations'])
    
    #affichage camembert par jour
    st.subheader("Fréquentations par jours:")
    plt.figure(figsize=(8, 8))  # Ajuster la taille du graphique
    plt.pie(frequentations_jours['frequentations'], labels=frequentations_jours['Jour'], autopct='%1.1f%%')
    plt.axis('equal')  # Assurer un cercle parfait
    st.pyplot(plt)

page_services_internes()