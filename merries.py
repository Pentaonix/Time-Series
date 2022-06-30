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

df = pd.read_csv("BFG_clean_final.csv", low_memory=False)

df = df[df.item_title.str.contains("Merries")]

df.to_csv("no_merries.csv", sep=',', index=True)

