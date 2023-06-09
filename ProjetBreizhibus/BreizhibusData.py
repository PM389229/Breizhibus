import mysql.connector
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Connexion à la base de données

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="example",
    port="3307",
    database="Breizhibus"
)

cursor = db.cursor()


