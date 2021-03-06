import altair as alt
from numpy import printoptions
import streamlit as st
import pandas as pd
import csv
import matplotlib.pyplot as plt
import squarify
import glob

def app():
    st.write("""
    # Naukri.com job profiles
    """)
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
        # print(filename[27:37])
        data=data.append(new_Row, ignore_index=True)

    data=data.drop(labels=0, axis=0)


    naukri_df = pd.concat(li, axis=0, ignore_index=True)

    # Defining data frame for sector
    uniqueValues_sector=naukri_df['Sector'].unique()
    o=naukri_df['Sector'].value_counts()
    df_sector=pd.DataFrame({"Industry":[0], "Count":[0]})
    sum=0
    for val in uniqueValues_sector:
        new_Row={"Industry":str(val),"Count":o[val]}
        df_sector=df_sector.append(new_Row, ignore_index=True)
        sum=sum+o[val]
    df_sector = df_sector.drop(labels=0, axis=0)
    #  Data frame for sector generated




    # Data frame for funtional area
    uniqueValues=naukri_df['Functional_Area'].unique()
    o=naukri_df['Functional_Area'].value_counts()
    df_func_Area=pd.DataFrame({"Functional_Area":[0], "Count":[0]})
    for val in uniqueValues:
        if(str(val)=="nan"):
            pass
        else:
            new_Row={"Functional_Area":str(val),"Count":o[val]}
            df_func_Area=df_func_Area.append(new_Row, ignore_index=True)
        
    df_func_Area = df_func_Area.drop(labels=0, axis=0)

    #  Data frame for Functional Area generated

    # Data frame for Employement
    uniqueValues=naukri_df['Employment_Type'].unique()
    o=naukri_df['Employment_Type'].value_counts()
    df_Emp_type=pd.DataFrame({"Employment_Type":[0], "Count":[0]})
    for val in uniqueValues:
        if(str(val)=="nan"):
            pass
        else:
            new_Row={"Employment_Type":str(val),"Count":o[val]}
            df_Emp_type=df_Emp_type.append(new_Row, ignore_index=True)
    df_Emp_type = df_Emp_type.drop(labels=0, axis=0)


    #  Data frame for Employement Type generated


    # Data frame for Role_Category
    uniqueValues=naukri_df['Role_Category'].unique()
    o=naukri_df['Role_Category'].value_counts()
    df_Role_cat=pd.DataFrame({"Role_Category":[0], "Count":[0]})
    for val in uniqueValues:
        if(str(val)=="nan"):
            pass
        else:
            new_Row={"Employment_Type":str(val),"Count":o[val]}
            df_Role_cat=df_Role_cat.append(new_Row, ignore_index=True)
    df_Role_cat = df_Role_cat.drop(labels=0, axis=0)


    #  Data frame for Role_Category generated

    # Data frame for Industry Type
    uniqueValues=naukri_df['Industry_Type'].unique()
    o=naukri_df['Industry_Type'].value_counts()
    df_Industry_t=pd.DataFrame({"Industry_Type":[0], "Count":[0]})
    for val in uniqueValues:
        if(str(val)=="nan"):
            pass
        else:
            new_Row={"Industry_Type":str(val),"Count":o[val]}
            df_Industry_t=df_Industry_t.append(new_Row, ignore_index=True)
    df_Industry_t = df_Industry_t.drop(labels=0, axis=0)


    #  Data frame for Role_Category generated

    st.write("There are "+ str(sum)+" total postings today")
    st.write(df_sector)

    #Bar chart for given data and number of jobs posted
    st.subheader('Bar chart')
    p = alt.Chart(data).mark_bar().encode(
        x='Csv_Date',
        y='Count'
    )
    p = p.properties(
        width=alt.Step(80)  # controls width of bar.
    )
    plt.legend( title='title', bbox_to_anchor=(1.05, 1), loc='upper left')

    st.write(p)

    #tree graph as for sectors in the csv
    st.write("""
    # Tree graph from sectors
    """)
    volume = df_sector['Count']
    labels = df_sector['Industry']
    plt.rc('font', size=5) 
    squarify.plot(sizes=volume, label=labels,
                alpha=0.6)
    plt.axis('off')
    plt.legend(title='title', bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot()

    # tree graph for Functional Area
    st.write("""
    # Tree graph from Functional Area
    """)
    v_Func_Area=df_func_Area['Count']
    labels_Func_Area = df_func_Area['Functional_Area']

    plt.rc('font', size=5)
    squarify.plot(sizes=v_Func_Area, label=labels_Func_Area,
                alpha=0.6)
    plt.axis('off')
    plt.legend(title='title', bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot()



    # tree graph for Employement Type
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



    # tree graph for Role Category
    st.write("""
    # Tree graph from Role Category
    """)
    v_R_c=df_Role_cat['Count']
    labels_r_c = df_Role_cat['Employment_Type']

    plt.rc('font', size=5)
    squarify.plot(sizes=v_R_c, label=labels_r_c,
                alpha=0.6)
    plt.axis('off')
    plt.legend(title='title', bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot()


    # tree graph for Industry Type
    st.write("""
    # Tree graph from Industry Type
    """)
    v_I_t=df_Industry_t['Count']
    labels_I_t = df_Industry_t['Industry_Type']

    plt.rc('font', size=5)
    squarify.plot(sizes=v_I_t, label=labels_I_t,
                alpha=0.6)
    plt.axis('off')
    plt.legend(title='title', bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot()


# altair==4.1.0
# beautifulsoup4==4.9.3
# matplotlib==3.4.2
# matplotlib-inline==0.1.2
# numpy==1.20.3
# pandas==1.2.4
# squarify==0.4.3
# streamlit==0.83.0
# virtualenv==20.4.7