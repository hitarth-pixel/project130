

import pandas as pd
df=pd.read_csv("bright_stars.csv")
del df["Luminosity"]
del df["Unnamed: 0"]

df.to_csv("class130-1.csv")
df2=pd.read_csv("dwarf_stars.csv")
del df2["Mass"]
del df2["Radius"]
df2.to_csv("class131-2.csv")