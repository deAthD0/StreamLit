import altair as alt
from numpy import printoptions
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import squarify


def Functional_area_graph(data_frame_selected, df):
    uniqueValues=data_frame_selected['Functional_Area'].unique()
    o=data_frame_selected['Functional_Area'].value_counts()
    df_func_Area=pd.DataFrame({"Functional_Area":[0], "Count":[0]})
    for val in uniqueValues:
        if(str(val)=="nan"):
            pass
        else:
            new_Row={"Functional_Area":str(val),"Count":o[val]}
            df_func_Area=df_func_Area.append(new_Row, ignore_index=True)

    df_func_Area = df_func_Area.drop(labels=0, axis=0)

    # print(df_func_Area)
            
    st.write("""
    # Tree graph from Functional Area
    """)
    v_Func_Area=df_func_Area['Count']
    labels_Func_Area = df_func_Area['Functional_Area']

    plt.rc('font', size=5)
    squarify.plot(sizes=v_Func_Area, label=labels_Func_Area,
                alpha=0.6)
    plt.axis('off')
    st.pyplot()