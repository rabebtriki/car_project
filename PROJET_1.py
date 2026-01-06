import streamlit as st
from PIL import Image
import pandas as pd

def PROJET_1():

    # Page title
    st.title("ANALYSE DES VEHICULE NEUF")
    st.write("## Entrez la marque du véhicule")

    # get_data
    df = pd.read_csv("all_cars22.csv")

    df['Marque'] = df['Marque'].astype(str)
    cars= df['Marque'].unique().tolist()
    cars.insert(0, "")
    

    df['Nombre de places'] = df['Nombre de places'].astype(str)
    df['Nombre de portes'] = df['Nombre de portes'].astype(str)  
    df['Energie'] = df['Energie'].astype(str)
    df['Puissance fiscale'] = df['Puissance fiscale'].astype(str) 
    df['Boîte'] = df['Boîte'].astype(str)
    df['Modele'] = df['Modele'].astype(str)
    df['Image URL'] = df['Image URL'].astype(str)


    # Search box for car brand
    car_brand = st.selectbox("Entrez la marque", cars)
    df = df[df['Marque'].str.startswith(car_brand)]

 
    # change to list all 
    nb_place= df['Nombre de places'].unique().tolist()
    nb_porte= df['Nombre de portes'].unique().tolist()
    Energie= df['Energie'].unique().tolist()
    puiss= df['Puissance fiscale'].unique().tolist()
    gear= df['Boîte'].unique().tolist()
    modl= df['Modele'].unique().tolist()
    
    nb_place.insert(0, "0")
    nb_porte.insert(0, "0")
    Energie.insert(0, "")
    puiss.insert(0, "")
    gear.insert(0, "")
    modl.insert(0, "")

    # Columns to hold car attributes
    col1, col2, col3 = st.columns(3)

    with col1:
        seats = st.selectbox("Nombre de places", nb_place)
        power = st.selectbox("Puissance fiscale", puiss)

    with col2:
        doors = st.selectbox("Nombre de portes", nb_porte)
        gearbox = st.selectbox("Boite", gear)

    with col3:
        model = st.selectbox("Nombre de model", modl)
        energy = st.selectbox("Energie", Energie)

    # Display the car images
    st.write("### Comparaison des véhicules")

    if seats!= "0":
        df = df[df['Nombre de places'].str.startswith(str(seats))]

    if doors!= "0":
        df = df[df['Nombre de portes'].str.startswith(str(doors))]

    df = df[df['Energie'].str.startswith(energy)]
    df = df[df['Puissance fiscale'].str.startswith(power)]  
    df = df[df['Boîte'].str.startswith(gearbox)]  
    df = df[df['Modele'].str.startswith(model)] 


    num_results = len(df)
    st.write(f"Number of results: {num_results}")

    num_columns = 3

    for i in range(0, num_results, num_columns):
        cols = st.columns(num_columns)

        for j, col in enumerate(cols):
            if i + j < num_results:
                car = df.iloc[i + j]
                car_brand = car['Marque']
                car_model = car['Modele']
                car_image = car['Image URL']
                car_price = car['Prix']

                with col:
                    st.image(car_image, caption=f"{car_brand} - {car_model} - {car_price}", use_column_width=True)