import numpy as np
import pandas as pd
import streamlit as st 
from pages.sector import sectors
import glob
def app():
    # naukri_df =pd.read_csv("csv/naukri_sector_job_infod2021-06-04.csv")
    path = 'csv/' # use your path
    all_files = glob.glob(path + "/*.csv")

    li = []
    data = pd.DataFrame({'Csv_Date':['0'],
            'Count':[0]})
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
        # creating bar chart's data frame
        lenght=len(df.index)
        new_Row={"Csv_Date":str(filename[27:37]),"Count":lenght}
        data=data.append(new_Row, ignore_index=True)

    data=data.drop(labels=0, axis=0)


    naukri_df = pd.concat(li, axis=0, ignore_index=True)

    is_check = st.checkbox("Display Data")
    if is_check:
        st.table(naukri_df)

    columns = st.sidebar.multiselect("Enter the variables", naukri_df.columns)
    # print(type(columns))
    sidebars = {}
    for y in columns:
        ucolumns=list(naukri_df[y].unique())
        sidebars[y]=st.sidebar.multiselect('Filter '+y, ucolumns)   

    if bool(sidebars):
        L = [naukri_df[k].isin(v) if isinstance(v, list) 
            else naukri_df[k].eq(v) 
            for k, v in sidebars.items() if k in naukri_df.columns]
        c=list(sidebars.keys())
        if next(iter(sidebars.items()))[1]:
            f=next(iter(sidebars.items()))[1]
            column=c[0]
            cell_val=f[0]
            sectors(column,cell_val)