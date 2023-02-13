from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# 学習用のデータと結果の準備
# X ,Y
learn_data = [[0,0], [1,0],[0,1],[1,1]]

# X and Y
learn_label = [0, 0, 0, 1]

# algorithmの指定 / LinearSVC
clf = LinearSVC()

# 学習用データと結果の学習
clf.fit(learn_data, learn_label)

# テストデータによる予測
test_data = [[0,0], [1,0], [0,1],[1,1]]
test_label = clf.predict(test_data)

# 予測の結果
print("{}の予測:{}".format(test_data, test_label))
print("正解率 = {}".format(accuracy_score([0,0,0,1], test_label)))