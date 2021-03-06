import altair as alt
from numpy import printoptions
import streamlit as st
import pandas as pd
import csv
import matplotlib.pyplot as plt
import squarify
import glob

from pages.functions.def_sector import sector_graph
from pages.functions.def_Industry_type import Industry_type_graph
from pages.functions.def_role_category import Role_Category_Graph
from pages.functions.def_Employement_type import Employment_Type_graph
from pages.functions.def_functional_area import Functional_area_graph
from pages.functions.def_Bar_Chart import BarChart
def sectors(coulmn, cell_val):
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Compiling all the csv with their total number of enteries
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
    sector_Selected_Data_Frame=naukri_df.loc[naukri_df[str(coulmn)] == str(cell_val)]

    BarChart(data)
    sector_graph(sector_Selected_Data_Frame, df)
    Industry_type_graph(sector_Selected_Data_Frame, df)
    Role_Category_Graph(sector_Selected_Data_Frame,df)
    Employment_Type_graph(sector_Selected_Data_Frame,df)
    Functional_area_graph(sector_Selected_Data_Frame, df)
