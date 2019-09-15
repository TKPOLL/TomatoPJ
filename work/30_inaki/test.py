
import MeCab as mc

t = mc.Tagger('-Ochasen')
sentence = "今日は朝から良い天気ですが、夕方から雨が降りそう。外出時は、傘を忘れないようにね。" #（41文字）
sentence = sentence.replace('\n', ' ')
print(sentence)

# python3 + mecabでnode.surfaceが取得できないバグへの対応
# http://qiita.com/piruty_joy/items/ce218090eae53b775b79
t.parse('')
node = t.parseToNode(sentence)
while(node):
    print('node surface[%s] feature[%s]' %(node.surface, node.feature))
    if node.surface != "":  # ヘッダとフッタを除外
        print(node.surface, '/t', node.feature)
    node = node.next