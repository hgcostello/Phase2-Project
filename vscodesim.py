from webbrowser import get
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

df = pd.read_csv('data/kc_house_data.csv')
df.head()