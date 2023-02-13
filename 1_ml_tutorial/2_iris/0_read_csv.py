import urllib.request as rq
import pandas as pd

url = "https://raw.githubusercontent.com/kujirahand/book-mlearn-gyomu/master/src/ch2/iris/iris.csv"
savefile = "iris.csv"
rq.urlretrieve(url, savefile)

pd.read_csv(savefile, encoding="utf-8")