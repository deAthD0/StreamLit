import altair as alt
from numpy import printoptions
import streamlit as st
import pandas as pd
import csv
import matplotlib.pyplot as plt
import squarify
import glob


# def app():
st.set_option('deprecation.showPyplotGlobalUse', False)

# Compiling all the csv with their total number of enteries
path = '/home/astrum/Dev/StreamLit/csv' # use your path
all_files = glob.glob(path + "/*.csv")

li = []
data = pd.DataFrame({'Csv_Date':['0'],
        'Count':[0]})
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
    # creating bar chart's data frame
    lenght=len(df.index)
    new_Row={"Csv_Date":str(filename[54:64]),"Count":lenght}
    data=data.append(new_Row, ignore_index=True)

data=data.drop(labels=0, axis=0)

print(data)

#     # Defining data frame for sector
# uniqueValues_sector=naukri_df['Sector'].unique()
# o=naukri_df['Sector'].value_counts()
# df_sector=pd.DataFrame({"Industry":[0], "Count":[0]})
# sum=0
# for val in uniqueValues_sector:
#     new_Row={"Industry":str(val),"Count":o[val]}
#     df_sector=df_sector.append(new_Row, ignore_index=True)
#     sum=sum+o[val]
# df_sector = df_sector.drop(labels=0, axis=0)
#     #  Data frame for sector generated



#   uniqueValues_sector=naukri_df['Sector'].unique()
#     o=naukri_df['Sector'].value_counts()
#     df_sector=pd.DataFrame({"Industry":[0], "Count":[0]})
#     sum=0
#     for val in uniqueValues_sector:
#         new_Row={"Industry":str(val),"Count":o[val]}
#         df_sector=df_sector.append(new_Row, ignore_index=True)
#         sum=sum+o[val]
#     df_sector = df_sector.drop(labels=0, axis=0)
# # st.subheader('Bar chart')

# p = alt.Chart(data).mark_bar().encode(
#     x='Csv_Date',
#     y='Count'
# )
# p = p.properties(
#     width=alt.Step(80)  # controls width of bar.
# )
# st.write(p)

