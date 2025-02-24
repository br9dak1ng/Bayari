import streamlit as st

import streamlit as st
from PIL import Image



st.set_page_config(page_title='Cobaye store' , page_icon=':tada:' , layout='wide')

st.subheader('Hi this is cobaye store :wave:')
st.title('here we sell cobayes with a reasonable price')
st.write('this is cobaye store our best cobaye yet is bayari ')

with st.container():
    st.write('---')
    st.header('What we do')
    st.write('we collect the rarest cobayes across the world and sell them for reasonable prices')


with st.container():
    st.write('---')
    st.header('Our rarest cobaye')
    st.subheader('Let us intoduce you our rarest cobaye')
    st.write('This is bayari hes the rarest cobaye in the world he can make anyone laughs but just staring at him and very social')


image = Image.open(r"C:\Users\BR9\Desktop\bayari.png.PNG")
new_size = (300, 300)  # Adjust width & height
resized_image = image.resize(new_size)

# Display in Streamlit
st.image(resized_image, caption="Smaller Image")
