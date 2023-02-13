from urllib.request import urlretrieve

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
savepath = "winequality.csv"
urlretrieve(url, savepath)