import altair as alt
from numpy import printoptions
import streamlit as st
import pandas as pd
import csv
import matplotlib.pyplot as plt
import squarify
st.write("""
# Naukri.com job profiles
""")

# naukri_df = pd.read_csv("naukri_sector_job_list2021-06-04.csv")
naukri_df = pd.read_csv("naukri_sector_job_infod2021-06-05.csv")

uniqueValues=naukri_df['Sector'].unique()


o=naukri_df['Sector'].value_counts()


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

# st.set_option('deprecation.showPyplotGlobalUse', False)

st.subheader('Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='Industry',
    y='Count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)

volume = df['Count']
labels = df['Industry']
# color_list = ['#0f7216', '#b2790c', '#ffe9a3',
#              '#f9d4d4', '#d35158', '#ea3033']

plt.rc('font', size=5)
squarify.plot(sizes=volume, label=labels,
              alpha=0.6)
plt.axis('off')
st.pyplot()