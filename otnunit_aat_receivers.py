import pandas as pd

data = pd.read_csv("otnunit_aat_receivers_c595_05f4_68b2.csv")

df = data.dropna(axis = 1, how = 'all')

print("Old data frame length: ", len(data.axes[1]), "New data frame length: ", len(df.axes[1]))
df.to_csv('new_otnunit_aat_receivers.csv')