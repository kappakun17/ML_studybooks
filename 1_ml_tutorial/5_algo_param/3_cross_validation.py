import pandas as pd
from sklearn.utils import all_estimators
from sklearn.model_selection import KFold, cross_val_score
import warnings

iris_data = pd.read_csv("iris.csv", encoding='utf-8')

y = iris_data.loc[:, "Name"]
x = iris_data.loc[:, ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]

allAlgorithms = all_estimators(type_filter = "classifier")

kfold_csv = KFold(n_splits=5, shuffle=True)
warnings.filterwarnings("ignore")

for(name, algorithm) in allAlgorithms:
  try:
    if(name == "LinearCSV"):
      clf = algorithm(max_iter=10000)
    else:
      clf = algorithm()
      
    if hasattr(clf, "score"):
      scores = cross_val_score(clf, x, y, cv=kfold_csv)
      print("{}の正解率 =".format(name))
      print(scores)
  
  except Exception as e:
    pass  
    
  