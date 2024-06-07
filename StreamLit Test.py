#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import altair as alt
import pandas as pd

st.title('Hello, Streamlit!')
st.write('Streamlit is installed and working correctly.')

# Sample data for Altair chart
data = pd.DataFrame({
    'a': list(range(10)),
    'b': list(range(10, 20))
})

# Create a simple Altair chart
chart = alt.Chart(data).mark_line().encode(
    x='a',
    y='b'
)

st.altair_chart(chart, use_container_width=True)

