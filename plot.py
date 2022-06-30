# Time series data source: fpp pacakge in R.
import matplotlib.pyplot as plt
from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv',parse_dates = ['date'], index_col = ['date'])

print(df)
# Draw Plot
def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
    plt.figure(figsize=(16,5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

plot_df(df, x=df.index, y=df.value, title='Monthly anti-diabetic drug sales in Australia from 1992 to 2008.')    

# # Import data
# df = pd.read_csv('datasets/AirPassengers.csv', parse_dates=['date'])
# x = df['date'].values
# y1 = df['value'].values

# # Plot
# fig, ax = plt.subplots(1, 1, figsize=(16,5), dpi= 120)
# plt.fill_between(x, y1=y1, y2=-y1, alpha=0.5, linewidth=2, color='seagreen')
# plt.ylim(-800, 800)
# plt.title('Air Passengers (Two Side View)', fontsize=16)
# plt.hlines(y=0, xmin=np.min(df.date), xmax=np.max(df.date), linewidth=.5)
# plt.show()