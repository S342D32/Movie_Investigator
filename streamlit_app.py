import streamlit as st
import numpy as np
import pandas as pd
import altier as alt

st.title('🎬🎬Movie Investigator')



with st.expander('About us'):
st.markdown('**What this app for?**')
st.info('This is a movie investigator app in which you should find which type of movies are good as per rating and user views.')
st.warning('Select the genere for the films and start the investigation')

st.subheader('Which movie genre perform ($)best the box office?')

