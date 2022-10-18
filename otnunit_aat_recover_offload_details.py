import pandas as pd

data = pd.read_csv("otnunit_aat_recover_offload_details_4b23_f002_f89a.csv")

df = data.dropna(axis = 1, how = 'all')

print("Old data frame length: ", len(data.axes[1]), "New data frame length: ", len(df.axes[1]))
df.to_csv('new_otnunit_aat_recover_offload_details.csv')