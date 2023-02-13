from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


learn_data = [[0, 0], [1, 0], [0, 1], [1, 1]]
learn_label = [0, 1, 1, 0]

clf = LinearSVC()
clf.fit(learn_data, learn_label)

clf2 = KNeighborsClassifier(n_neighbors = 1)
clf2.fit(learn_data, learn_label)

test_data = [[0, 0], [1, 0], [0, 1], [1, 1]]
test_label = clf.predict(test_data)
test_label2 = clf2.predict(test_data)

print("{}の予測:{}".format(test_data, test_label))
print("正解率 = {}".format(accuracy_score([0,1,1,0], test_label)))

print("{}の予測:{}".format(test_data, test_label2))
print("正解率 = {}".format(accuracy_score([0,1,1,0], test_label2)))