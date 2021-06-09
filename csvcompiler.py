import pandas as pd
import glob

path = '/home/astrum/Dev/StreamLit/' # use your path
all_files = glob.glob(path + "/*.csv")

li = []
data = pd.DataFrame({'Csv_Date':['0'],
        'Count':[0]})
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
    # creating bar chart's data frame
    lenght=len(df.index)
    new_Row={"Csv_Date":str(filename[50:60]),"Count":lenght}
    data=data.append(new_Row, ignore_index=True)

data=data.drop(labels=0, axis=0)
print(data)
frame = pd.concat(li, axis=0, ignore_index=True)
# print(frame)