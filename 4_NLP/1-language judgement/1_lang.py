import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Unicodeのコードポイント頻度測定
def count_codePoint(str):
    # unicodeのポイントがアドレスになっている
    counter = np.zeros(65535)
    
    for i in range(len(str)):
        code_point = ord(str[i])
        if code_point > 65535:
            continue
        counter[code_point] += 1
    
    # 各要素の頻度を正規化 
    counter = counter / len(str)
    return counter

# 学習用データ
ja_str = "これは日本語の文章です。"
en_str = "This is English Sentences."
th_str = 'นี่เป็นประโยคภาษาไทย'

x_train = [count_codePoint(ja_str), count_codePoint(en_str), count_codePoint(th_str)]
y_train = ["ja", "en", "th"]

# 学習
clf = GaussianNB()
clf.fit(x_train, y_train)


# 評価データの準備
ja_test_str = "こんにちは"
en_test_str = "Hello"
th_test_str = "สวัสดี"

x_test = [count_codePoint(ja_test_str), count_codePoint(en_test_str), count_codePoint(th_test_str)]
y_test = ["ja", "en", "th"]

y_pred = clf.predict(x_test)
print(y_pred)
print("正解率: = ", accuracy_score(y_test, y_pred))
        
        
    