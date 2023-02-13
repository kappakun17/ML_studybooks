import MeCab

tagger = MeCab.Tagger()

result = tagger.parse("メイが恋ダンスを踊っている。")
print(result)