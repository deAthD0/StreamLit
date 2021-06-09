# import os
# import pandas as pd
# path, dirs, files = next(os.walk("./csv/"))
# file_count = len(files)
# # create empty list
# dataframes_list = []
  
# # append datasets to the list 
# for i in range(file_count):
#     temp_df = pd.read_csv("./csv/"+files[i])
#     dataframes_list.append(temp_df)
      
# # display datsets
# for dataset in dataframes_list:
#     display(dataset)

import pandas as pd
import glob

path = '/home/astrum/Dev/StreamLit/' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
    # lines= len(list(df))
    l=len(df.index)
    print(l)
frame = pd.concat(li, axis=0, ignore_index=True)
# print(frame)