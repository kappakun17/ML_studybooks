import MeCab

tagger = MeCab.Tagger()
tagger.parse("")

node = tagger.parseToNode("メイが恋ダンスを踊っている。")

result = []

while node is not None:
    print(node.feature.split(","))
    hinshi = node.feature.split(",")[0]
    if hinshi in ["名詞"]:
        result.append(node.surface)
    elif hinshi in ["動詞", "形容詞"]:
        result.append(node.feature.split(",")[7])
    node = node.next
    
print(result)