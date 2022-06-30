from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from datetime import datetime


# Import as Dataframe
df = pd.read_csv('test_data.csv')
test = df['ordered_date'][0]
test = test.split(" ")[0]
test = datetime.strptime(test, "%d-%m-%y")
test = datetime.strftime(test, "%m-%Y")
print(test)