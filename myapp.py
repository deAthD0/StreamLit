import altair as alt
from numpy import printoptions
import streamlit as st
import pandas as pd
import csv
st.write("""
# Naukri.com job profiles
""")

naukri_df = pd.read_csv("naukri_sector_job_list2021-06-04.csv")

uniqueValues=naukri_df['Industry'].unique()


o=naukri_df['Industry'].value_counts()


df=pd.DataFrame({"Industry":[0], "Count":[0]})

sum=0
for val in uniqueValues:
    new_Row={"Industry":str(val),"Count":o[val]}
    df=df.append(new_Row, ignore_index=True)
    # st.write("There are "+str(o[val])+" : "+str(val)+" postings today")
    sum=sum+o[val]
df = df.drop(labels=0, axis=0)
print(df)

st.write("There are "+ str(sum)+" total postings today")
st.write(df)

st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='Industry',
    y='Count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)