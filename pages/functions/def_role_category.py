import altair as alt
from numpy import printoptions
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import squarify

def Role_Category_Graph(data_frame_selected, df):
    uniqueValues=data_frame_selected['Role_Category'].unique()
    o=data_frame_selected['Role_Category'].value_counts()
    df_Role_cat=pd.DataFrame({"Role_Category":[0], "Count":[0]})
    for val in uniqueValues:
        if(str(val)=="nan"):
            pass
        else:
            new_Row={"Role_Category":str(val),"Count":o[val]}
            df_Role_cat=df_Role_cat.append(new_Row, ignore_index=True)
    df_Role_cat = df_Role_cat.drop(labels=0, axis=0)

    st.write("""
    # Tree graph from Role Category
    """)
    v_R_c=df_Role_cat['Count']
    labels_r_c = df_Role_cat['Role_Category']

    plt.rc('font', size=5)
    squarify.plot(sizes=v_R_c, label=labels_r_c,
                alpha=0.6)
    plt.axis('off')
    plt.legend(title='title', bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot()

