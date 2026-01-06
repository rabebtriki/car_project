import streamlit as st
from PIL import Image
import pandas as pd
import os
from css import CSS
from vector_DB import get_car

def PROJET_2():

    st.markdown('<h1 class="header">Chat with Your Favorite Car 🚗💬</h1>', unsafe_allow_html=True)
    
    # CSS personnalisé pour le style de l'interface
    st.markdown(CSS, unsafe_allow_html=True)

    # Chargement du CSV avec chemin robuste
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, "all_cars22.csv")

    if not os.path.exists(csv_path):
        st.error(f"❌ Fichier introuvable : {csv_path}")
        return

    df = pd.read_csv(csv_path)
    df['Marque'] = df['Marque'].astype(str)
    cars = df['Marque'].unique().tolist()
    cars.insert(0, "")

    # Initialisation des variables de session
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    if "user_input" not in st.session_state:
        st.session_state["user_input"] = ""

    # Barre de navigation
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        car_marque = st.selectbox("Select a marque", cars, key="marque_select")

    df = df[df['Marque'].str.startswith(car_marque)]
    model = df['Modele'].unique().tolist()
    model.insert(0, "")

    with col2:
        car_model = st.selectbox("Select a model", model, key="model_select")

    with col3:
        chat_with = st.selectbox("Select destinataire", ["👤 Chat with Expert", "🚗 Chat with Car"], key="chat_select")

    df = df[df['Modele'].str.startswith(car_model)]

    # espace
    st.write(" ")
    st.write(" ")

    # Zone d'affichage principale
    col_main, col_side = st.columns([4, 1])

    with col_main:
        if not df.empty and "Image URL" in df.columns:
            car_image = df['Image URL'].iloc[0]
            st.image(car_image, use_container_width=True)
        else:
            st.info("🚗 Veuillez sélectionner une marque et un modèle pour voir l'image.")

    with col_side:
        avatar_name = "👤 Car Expert" if chat_with == '👤 Chat with Expert' else "🚗 AI Car"
        st.markdown(f"""<div class="avatar-container">{avatar_name}</div>""", unsafe_allow_html=True)

    # espace
    st.write(" ")
    st.write(" ")

    def clear_input():
        st.session_state["user_input"] = ""

    # Zone de chat
    chat_container = st.container()
    name_car = car_marque + "_" + car_model

    print("this is the name of the car: ", name_car)

    try:
        retrieval_chain = get_car(name_car)
        print("this is mhamed: ",retrieval_chain)
    except Exception:
        retrieval_chain = None

    # print("this is the retrivel_chain: ",retrieval_chain)


    with chat_container:
        # Affichage de l'historique des messages
        for message in st.session_state['chat_history']:
            message_class = "user-message" if message["role"] == "user" else "assistant-message"
            st.markdown(f"""<div class="message {message_class}">{message["content"]}</div>""", unsafe_allow_html=True)

        # Zone de saisie
        user_input = st.text_input("", placeholder="What do you want to ask your car today ??", key="user_input")

        if st.button("Send", key="send_button"):
            if user_input:
                # Ajouter le message de l'utilisateur à l'historique
                st.session_state['chat_history'].append({
                    "role": "user",
                    "content": user_input
                })

                # Obtenir la réponse
                with st.spinner("Thinking..."):
                    try:
                        if retrieval_chain:
                            answer = retrieval_chain.invoke({"input": user_input})
                            print("this is the answer: ", answer)
                            st.session_state['chat_history'].append({
                                "role": "assistant",
                                "content": answer.get('answer', "⚠️ Pas de réponse disponible.")
                            })
                        else:
                            st.warning("❌ Choisissez une voiture avant de poser une question.")
                    except Exception as e:
                        st.warning(f"Erreur lors de la génération de réponse : {e}")

                # refresh
                st.button("Hidden Clear", on_click=clear_input, key="hidden_clear", disabled=True)
                st.rerun()

            # if st.button("Clear Chat History"):
            #     st.session_state['chat_history'] = []
            #     st.rerun()
