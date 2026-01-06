import streamlit as st
from streamlit_option_menu import option_menu
import base64
from PIL import Image

# Import pages
from home import home_page
from PROJET_1 import PROJET_1
from PROJET_2 import PROJET_2


# Initialize Streamlit app
st.set_page_config(page_title="WEBSITE RABEB", page_icon='./images/1.png', layout='wide')

image = Image.open('./images/1.png')
with open('./images/1.png', 'rb') as f:
    image_bytes = f.read()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
st.sidebar.markdown(f'<div style="display: flex; justify-content: center; align-items: flex-start;"><img src="data:image/png;base64,{image_base64}" width="200"></div>', unsafe_allow_html=True)

st.sidebar.write(" ")
st.sidebar.write(" ")

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["HOME", "PROJET_1", "PROJET_2","PROJET_3"],
        icons=["house", "chat", "chat","chat"],
        menu_icon="cast",
        default_index=0)
    

# TRAKAH EL TASwIRA MTA3 EL BACKGROUND TRODHA LOCAL MOCH EN LIGNE
# https://w0.peakpx.com/wallpaper/345/456/HD-wallpaper-chatbot-neon-icon-violet-background-neon-symbols-chatbot-neon-icons-chatbot-sign-computer-signs-chatbot-icon-computer-icons.jpg
# https://images.unsplash.com/photo-1542281286-9e0a16bb7366
# url("data:image/jpg;base64,{encoded_image}")

# Set the background image
# background_image = """
# <style>
# [data-testid="stAppViewContainer"] > .main {
#     background-image: url("https://w0.peakpx.com/wallpaper/345/456/HD-wallpaper-chatbot-neon-icon-violet-background-neon-symbols-chatbot-neon-icons-chatbot-sign-computer-signs-chatbot-icon-computer-icons.jpg");
#     background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
#     background-position: center;  
#     background-repeat: no-repeat;
# }
# </style>
# """

# st.markdown(background_image, unsafe_allow_html=True)

# input_style = """
# <style>
# input[type="text"] {
#     background-color: transparent;
#     color: #a19eae;  // This changes the text color inside the input box
# }
# div[data-baseweb="base-input"] {
#     background-color: transparent !important;
# }
# [data-testid="stAppViewContainer"] {
#     background-color: transparent !important;
# }
# </style>
# """

#END BG


# # Page selection
if selected == "HOME":
    home_page()
elif selected == "PROJET_1":
    PROJET_1()
elif selected == "PROJET_2":
    PROJET_2()