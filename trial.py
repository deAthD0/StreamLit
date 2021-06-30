# import pandas as pd
# import streamlit as st


# def app():
#     st.markdown("""
#     # Multi-Page App1
#     """)

import numpy as np
import pandas as pd
import streamlit as st 
from pages.sector import sectors
df =pd.read_csv("csv/naukri_sector_job_infod2021-06-04.csv")
is_check = st.checkbox("Display Data")
if is_check:
    st.table(df)

columns = st.sidebar.multiselect("Enter the variables", df.columns)
# print(type(columns))
sidebars = {}
for y in columns:
    ucolumns=list(df[y].unique())
    sidebars[y]=st.sidebar.multiselect('Filter '+y, ucolumns)   

if bool(sidebars):
    L = [df[k].isin(v) if isinstance(v, list) 
         else df[k].eq(v) 
         for k, v in sidebars.items() if k in df.columns]
    
    
    df1 = df[np.logical_and.reduce(L)]
    print(sidebars)
    sectors()