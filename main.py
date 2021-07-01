import streamlit as st
from multiapp import MultiApp
import csv
# from apps import home, data, model # import your app modules here
import myapp2, myapp, graphs
app = MultiApp()

st.markdown("""
# Multi-Page App
""")


# Add all your application here
app.add_app("Home", myapp2.app)
# app.add_app("Data", myapp.app)
app.add_app("Graph-Data", graphs.app)
# The main app
app.run()