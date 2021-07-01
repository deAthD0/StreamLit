import altair as alt
from numpy import printoptions
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import squarify
   
def BarChart(data):   
    st.subheader('Bar chart')
    p = alt.Chart(data).mark_bar().encode(
        x='Csv_Date',
        y='Count'
    )
    p = p.properties(
        width=alt.Step(80)  # controls width of bar.
    )
    st.write(p)
