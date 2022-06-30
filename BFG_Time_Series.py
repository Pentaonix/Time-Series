import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import time
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import mlxtend as ml
from mlxtend.preprocessing import TransactionEncoder
from datetime import datetime

df = pd.read_csv("repeater_clean.csv", low_memory=False)

basket = (df
          .groupby(['ordered_date'])['quantity']                        # groupby 'invoice_number'
          .sum()                                                        # sum only 'quantity' column
          .reset_index()                                                # set index column to default
          )
df.sort_values(by=['ordered_date'])

for i in range(len(basket)):
    basket['ordered_date'][i] = pd.to_datetime(basket.ordered_date[i])
    basket['ordered_date'][i] = datetime.strftime(basket['ordered_date'][i], "%Y %B")
# print(basket)
to_list_basket = basket['quantity'].values.tolist()
# print(to_list_basket)

def plot_barchart(df, x, y, title="", xlabel='Date', ylabel='Number of products purchased', dpi=100):
    figure, axis = plt.subplots()
    axis.set_ylim(0,400)
    plt.bar(x, y, color='tab:blue')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.xticks(rotation=45)
    #set labels for columns
    rects = axis.patches
    for rect, label in zip(rects, to_list_basket):
        height = rect.get_height()
        axis.text(rect.get_x() + rect.get_width() / 2, height + 1, label,
                ha='center', va='bottom')
    plt.show()

plot_barchart(basket, x=basket.ordered_date, y=basket.quantity, title='Numbers of Orders by Repeater Users')  

def plot_line(df, x, y, title="", xlabel='Date', ylabel='Number of orders', dpi=100):
    plt.figure(figsize=(16,9), dpi=dpi)    
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.xticks(rotation=45)
    plt.show()

# plot_line(basket, x=basket.ordered_date, y=basket.quantity, title='Change of Numbers of Orders in 1 year')   