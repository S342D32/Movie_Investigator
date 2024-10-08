import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.title('🎬🎬Movie Investigator')



with st.expander('About us'):
  st.markdown('**What this app for?**')
  st.info('This is a movie investigator app in which you should find which type of movies are good as per rating and user views.')
  st.warning('Select the genere for the films and start the investigation')

st.subheader('Which movie genre perform ($)best the box office?')

df = pd.read_csv('movies_genres_summary.csv')
df.year = df.year.as_type('int')

genre_list =df.genre.unique()
genres_selection = st.multiselect('Select genres', genres_list, ['Action', 'Adventure', 'Biography', 'Comedy', 'Drama', 'Horror'])




