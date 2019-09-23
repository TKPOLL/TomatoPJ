import glob
import re
from collections import Counter

import MeCab as mc

# ========= ファイルのinputを行う処理 =====================
# inputPath = 'D:\\PycharmProjects\\TomatoPJ\\work\\10_tabata\\02_data\\10_業種データ01\\*'
# glob.glob(inputPath)
#
# for x in glob.glob(inputPath) :
#     print('"' + x + ':""0"')

# with open('/Users/tabatatoshinori/git/TomatoPJ/work/10_tabata/03_PGM/実験用データ/みずほ情報総研.txt', encoding=UTF-8) as f:
with open('D:\\PycharmProjects\\TomatoPJ\\work\\10_tabata\\03_PGM\\実験用データ\\みずほ情報総研.txt', encoding='utf-8') as f:
    reader = f.read()
    t = mc.Tagger('-Ochasen')
    for data in reader:  # for文を用いて一行ずつ読み込む\n,

        reader = f.read()
        parse = t.parse(reader)
        lines = parse.split('\n')
        print(lines)
        items = (re.split('[\t,]', line) for line in lines)

        # 名詞をリストに格納
        words = [item[0]
                 for item in items
                 if (item[0] not in ('EOS', '', 't', 'ー') and
                     item[1] == '名詞' and item[2] == '一般')]

        # 頻度順に出力
        counter = Counter(words)
        print(counter)
        result_count_dict = {'0050': "0", "1050": "0", "2050": "8", "3050": "0", "3100": "0", "3150": "0", "3200": "0",
                             "3250": "0", "3300": "0", "3350": "0", "3400": "0", "3450": "0", "3500": "0", "3550": "0",
                             "3600": "0", "3650": "0", "3700": "0", "3750": "0", "3800": "5", "4050": "0", "5050": "0",
                             "5100": "0", "5150": "0", "5200": "0", "5250": "4", "6050": "0", "6100": "0", "7050": "0",
                             "7100": "0", "7150": "0", "7200": "0", "8050": "0", "9050": "0"}

    # for word, count in counter:\n,
    #    for dict_goyushu in df_dictionary:\n,
    #        if dict_goyushu[1] == word:\n,
    #          result_count_dict[dict_goyushu[0]] = result_count_dict.get(dict_goyushu[0]) + count
