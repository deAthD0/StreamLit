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

frame = pd.concat(li, axis=0, ignore_index=True)
# print(frame)
frame.to_csv('file1.csv')
# print(lin)