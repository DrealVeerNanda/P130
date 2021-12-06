import pandas as pd
import csv
#I wasnt able to complete the last one, so this is all I know although I will update this when I finish it.
df = pd.read_csv("data.csv")

del df["Luminosity"]

df.to_csv('new.csv') 
