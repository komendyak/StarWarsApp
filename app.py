import streamlit as st
from PIL import Image
import requests
import io


##Design, couleurs


#Titre
st.title('**GalaxyFinder**')
st.markdown("Hi there ! Let me show you galaxies. It's very simple.")

#Explanation
st.markdown("You just have to upload a galaxy picture on the File uploader below:")


#File uploader
st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Choose a galaxy image", type="jpg")

if uploaded_file is not None:

    # uploaded_file.__dict__

    image = Image.open(uploaded_file)
    st.image(image, caption='Beautiful ! Now, let\'s classify it...', use_column_width=True)

    # image.__dict__

    # convert imge to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    # with open("image.jpg", "wb") as f:
    #     f.write(img_byte_arr)

    #API Call
    url = 'https://hamster-ev6iq3m3na-ew.a.run.app/uploadfile'
    files = {'file': img_byte_arr}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        resp = response.json()
        resp
    else:
        "ça marche pas"





#Wait time
if st.checkbox('Show progress bar'):
    import time

    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'


##Output pour chaque classe

#if Hubble == E0-E2

st.title('Elliptical Galaxies : E0-E2')
st.header('About them')
st.text('Elliptical galaxies have smooth, featureless light distributions and appear as ellipses.\
The ellipticity increases from left to right on the Hubble diagram, with near-circular (E0) galaxies situated on the very left of the diagram to the most flattened elliptical galaxies (E7) with a cigar shape.\
They have very little interstellar matter (neither gas nor dust), which results in low rates of star formation, and few young stars.\
\
Elliptical galaxies vary greatly in both size and mass with diameters ranging from 3000 lightyears to more than 700,000 lightyears, and masses from 105 to nearly 1013 solar masses. This range is much broader for this galaxy type than for any other. The smallest known elliptical galaxy is about one-tenth the size of the Milky Way.')

st.header('A few examples of E0-E2 galaxies')
#import Pil and make an image.open
st.image('...')

#if Hubble == E3-E5

st.title('Elliptical Galaxies : E3-E5')
st.header('About them')
st.text('Elliptical galaxies have smooth, featureless light distributions and appear as ellipses.\
The ellipticity increases from left to right on the Hubble diagram, with near-circular (E0) galaxies situated on the very left of the diagram to the most flattened elliptical galaxies (E7) with a cigar shape.\
They have very little interstellar matter (neither gas nor dust), which results in low rates of star formation, and few young stars.\
\
Elliptical galaxies vary greatly in both size and mass with diameters ranging from 3000 lightyears to more than 700,000 lightyears, and masses from 105 to nearly 1013 solar masses. This range is much broader for this galaxy type than for any other. The smallest known elliptical galaxy is about one-tenth the size of the Milky Way.')

st.header('A few examples of E3-E5 galaxies')
#import Pil and make an image.open
st.image('...')


#if Hubble == E6-E7

st.title('Elliptical Galaxies : E6-E7')
st.header('About them')
st.text('Elliptical galaxies have smooth, featureless light distributions and appear as ellipses.\
The ellipticity increases from left to right on the Hubble diagram, with near-circular (E0) galaxies situated on the very left of the diagram to the most flattened elliptical galaxies (E7) with a cigar shape.\
They have very little interstellar matter (neither gas nor dust), which results in low rates of star formation, and few young stars.\
\
Elliptical galaxies vary greatly in both size and mass with diameters ranging from 3000 lightyears to more than 700,000 lightyears, and masses from 105 to nearly 1013 solar masses. This range is much broader for this galaxy type than for any other. The smallest known elliptical galaxy is about one-tenth the size of the Milky Way.')

st.header('A few examples of E6-E7 galaxies')
#import Pil and make an image.open
st.image('...')

#if Hubble == S0 or Hubble == SB0

st.title('Lenticular Galaxies : S0 and SB0')
st.header('About them')
st.text('A lenticular galaxy  is a type of galaxy intermediate between an elliptical and a spiral galaxy. It contains a large-scale disc but does not have large-scale spiral arms. They have much higher bulge-to-disk ratios than typical spirals.\
    When simply looking at a galaxy\'s image, lenticular galaxies with relatively face-on disks are difficult to distinguish from ellipticals of type E0–E3 (rounded), making the classification of many such galaxies uncertain.\
    When viewed edge-on, the disk becomes more apparent. Lenticular galaxies are disc galaxies that have used or lost most of their interstellar matter and therefore have very little ongoing star formation.\
\
    Like spiral galaxies, lenticular galaxies can possess a central bar structure.')

st.header('A few examples of lenticular galaxies')
#import Pil and make an image.open
st.image('...')

