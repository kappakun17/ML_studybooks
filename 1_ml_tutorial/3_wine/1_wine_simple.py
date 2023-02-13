import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# read the data
wine = pd.read_csv("winequality.csv", encoding='utf-8', sep=';')

# split the test data and learning data
y = wine['quality']
x = wine.drop('quality', axis=1)
newlist = []
for v in list(y):
    if v <= 4:
        newlist += [0]
    elif v <= 7:
        newlist += [1]
    else:
        newlist += [2]
y = newlist
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(x_train, y_train)

# accuracy
y_pred = model.predict(x_test)
print(classification_report(y_test, y_pred))
print("正解率 = {}".format(accuracy_score(y_test, y_pred)))

# 正解率 = 0.6959183673469388

# yのグループ分けを修正後
# 正解率 = 0.9459183673469388