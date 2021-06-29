import altair as alt
from numpy import printoptions
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import squarify

def Role_Category_Graph(data_frame_selected, df):
    uniqueValues=naukri_df['Role_Category'].unique()
    o=naukri_df['Role_Category'].value_counts()
    df_Role_cat=pd.DataFrame({"Role_Category":[0], "Count":[0]})
    for val in uniqueValues:
        if(str(val)=="nan"):
            pass
        else:
            new_Row={"Employment_Type":str(val),"Count":o[val]}
            df_Role_cat=df_Role_cat.append(new_Row, ignore_index=True)
    df_Role_cat = df_Role_cat.drop(labels=0, axis=0)

    st.write("""
    # Tree graph from Role Category
    """)
    v_R_c=df_Role_cat['Count']
    labels_r_c = df_Role_cat['Employment_Type']

    plt.rc('font', size=5)
    squarify.plot(sizes=v_R_c, label=labels_r_c,
                alpha=0.6)
    plt.axis('off')
    st.pyplot()

