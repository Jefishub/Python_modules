import pandas as pd
import numpy as np

ser = pd.Series()
print(ser)

data_arr = np.array(['t','a','i','t','o'])
print (data_arr)

data_ser = pd.Series(data_arr)
print("Pandas series:\n", data_ser)