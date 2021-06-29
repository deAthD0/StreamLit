import altair as alt
from numpy import printoptions
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import squarify


def Industry_type_graph(data_frame_selected, df):
    uniqueValues=data_frame_selected['Industry_Type'].unique()
    o=data_frame_selected['Industry_Type'].value_counts()
    df_Industry_t=pd.DataFrame({"Industry_Type":[0], "Count":[0]})
    for val in uniqueValues:
        if(str(val)=="nan"):
            pass
        else:
            new_Row={"Industry_Type":str(val),"Count":o[val]}
            df_Industry_t=df_Industry_t.append(new_Row, ignore_index=True)
    df_Industry_t = df_Industry_t.drop(labels=0, axis=0)
    
    
    st.write("""
    # Tree graph from Industry Type
    """)
    v_I_t=df_Industry_t['Count']
    labels_I_t = df_Industry_t['Industry_Type']

    plt.rc('font', size=5)
    squarify.plot(sizes=v_I_t, label=labels_I_t,
                alpha=0.6)
    plt.axis('off')
    st.pyplot()

