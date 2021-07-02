import altair as alt
from numpy import printoptions
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import squarify


def sector_graph(data_frame_selected,df):
    uniqueValues_sector=data_frame_selected['Sector'].unique()
    o=data_frame_selected['Sector'].value_counts()
    df_sector=pd.DataFrame({"Sector":[0], "Count":[0]})
    sum=0
    for val in uniqueValues_sector:
        new_Row={"Sector":str(val),"Count":o[val]}
        df_sector=df_sector.append(new_Row, ignore_index=True)
        sum=sum+o[val]
    df_sector = df_sector.drop(labels=0, axis=0)

    st.write("""
    # Tree graph from sectors
    """)
    volume = df_sector['Count']
    labels = df_sector['Sector']
    plt.rc('font', size=5) 
    squarify.plot(sizes=volume, label=labels,
                alpha=0.6)
    plt.axis('off')
    plt.legend(title='title', bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot()

