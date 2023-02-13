from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("kion10y.csv", encoding='utf-8')

train_year = (df["年"] <= 2015)
test_year = (df["年"] >= 2016)
interval = 6

def make_data(data):
    x = [] # learning data
    y = [] # result data
    temps = list(data["気温"])
    for i in range(len(temps)):
        if i < interval: continue
        y.append(temps[i])
        xa = []
        for p in range(interval):
            d = i + p - interval
            xa.append(temps[d])
        x.append(xa)
    return (x, y)

train_x, train_y = make_data(df[train_year])
test_x, test_y = make_data(df[test_year])

lr = LinearRegression()
lr.fit(train_x, train_y)
pre_y = lr.predict(test_x)

plt.figure(figsize=(10, 6), dpi=100)
plt.plot(test_y, c='r')
plt.plot(pre_y, c='b')
plt.savefig('tenki-kion-lr.png')
plt.show()
