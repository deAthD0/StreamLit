import altair as alt
from numpy import printoptions
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import squarify


def Employment_Type_graph(data_frame_selected, df):
    uniqueValues=data_frame_selected['Employment_Type'].unique()
    o=data_frame_selected['Employment_Type'].value_counts()
    df_Emp_type=pd.DataFrame({"Employment_Type":[0], "Count":[0]})
    for val in uniqueValues:
        if(str(val)=="nan"):
            pass
        else:
            new_Row={"Employment_Type":str(val),"Count":o[val]}
            df_Emp_type=df_Emp_type.append(new_Row, ignore_index=True)
    df_Emp_type = df_Emp_type.drop(labels=0, axis=0)

    st.write("""
    # Tree graph from Employemnt Type
    """)
    v_Emp_type=df_Emp_type['Count']
    labels_emp_type = df_Emp_type['Employment_Type']

    plt.rc('font', size=5)
    squarify.plot(sizes=v_Emp_type, label=labels_emp_type,
                alpha=0.6)
    plt.axis('off')
    plt.legend(title='title', bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot()