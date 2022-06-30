from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from datetime import datetime


# Import as Dataframe
df = pd.read_csv('new_merries.result.csv')
for i in range(len(df)):
    df['ordered_date'][i] = df['ordered_date'][i].split(" ")[0]
    df['ordered_date'][i] = datetime.strptime(df['ordered_date'][i], "%d-%m-%y")
    df['ordered_date'][i] = datetime.strftime(df['ordered_date'][i], "%Y-%m")
    # df['item_title'][i] = str(df['item_title'][i])[:-4]

df.to_csv("new_clean.csv", sep=',', index=True)



