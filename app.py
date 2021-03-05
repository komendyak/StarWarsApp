import streamlit as st
from PIL import Image
import requests
import io
from result_galaxy import result_galaxy
import time


#Background
st.markdown("""
<style>
.block-container {
    background-color: rgba(0,0,0,0.75);
}
body {
    color: #fff;
    background-image: url("https://github.com/AurelSann/StarWars/blob/master/images/SWwallpaper.png?raw=true");
    background-size: 400px !important;
}
</style>
    """, unsafe_allow_html=True)


#Titre

st.title('**💫 GalaxyFinder 💫**')

st.header("Hi there! Let me show you galaxies. It's very simple 🔭")

#Explanation
st.subheader("You just have to upload a 🌌 **galaxy picture** 🌌 in the file uploader below:")


#File uploader
st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader(' ',type="jpg")

if uploaded_file is not None:

    # uploaded_file.__dict__

    image = Image.open(uploaded_file)
    st.image(image, caption='Beautiful ! Now, let\'s classify it...', use_column_width=True)


    # convert imge to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()




    #API Call, url de prod :
    url = 'https://galaxyfinder-mptzkkztqq-ew.a.run.app/uploadfile'
    #url local pour tester :
    #url = 'http://localhost:8000/uploadfile'
    files = {'file': img_byte_arr}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        resp = response.json()

        value = resp["hubble"]
        result_galaxy(value)


    else:
        "⭐️ Young padawan, a connection issue we seem to have. Retry you must. ⭐️"


#Wait time
# if st.checkbox('Show progress bar'):
#     import time

#     'Starting a long computation...'

#     # Add a placeholder
#     latest_iteration = st.empty()
#     bar = st.progress(0)

#     for i in range(100):
#         # Update the progress bar with each iteration.
#         latest_iteration.text(f'Iteration {i+1}')
#         bar.progress(i + 1)
#         time.sleep(0.1)

#     '...and now we\'re done!'
