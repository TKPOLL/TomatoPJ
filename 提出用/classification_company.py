#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:50:09 2019

@author: tabatatoshinori
"""
#import
#import
import pandas as pd
import MeCab
import re
from collections import Counter

#自身のPCのgitHub親パス(次は田端の場合。動かす場合は、各自のパスに差し替えること)
root_git_path = "/Users/tabatatoshinori/git"
df_dictionary1 = pd.read_csv(root_git_path + '/TomatoPJ/work/10_tabata/03_PGM/実験用データ/csv/加工前csv/data1/result.csv')
df_dictionary = df_dictionary1.values.tolist()

#cohodが50のものを0050に変換しておく
for record in df_dictionary:
    if record[0] == 50:
        record[0] = '0050'


tagger = MeCab.Tagger()

#本番用にループ処理に書き換えること
with open('/Users/tabatatoshinori/git/TomatoPJ/work/10_tabata/03_PGM/実験用データ/フジフィルム.txt', "r", encoding="UTF-8") as f:
    reader = f.read()
    parse = tagger.parse(reader)
    lines = parse.split('\n')
    items = (re.split('[\t,]', line) for line in lines)

    # 名詞をリストに格納
    words = [item[0]
        for item in items
            if (item[0] not in ('EOS', '', 't', 'ー') and
                 item[1] == '名詞' and item[2] == '一般')]
        
    # 頻度順に出力
    counter = Counter(words)
    result_count_dict = {'0050' : '0','1050' : '0', '2050' : '0', '3050' : '0', '3100' : '0', '3150' : '0', 
                        '3200' : '0', '3250' : '0', '3300' : '0', '3350' : '0', '3400' : '0', '3450' : '0', 
                        '3500' : '0', '3550' : '0', '3600' : '0', '3650' : '0', '3700' : '0', '3750' : '0', 
                        '3800' : '0', '4050' : '0', '5050' : '0', '5100' : '0', '5150' : '0', '5200' : '0', 
                         '5250' : '0', '6050' : '0', '6100' : '0', '7050' : '0', '7100' : '0', '7150' : '0', 
                        '7200' : '0', '8050' : '0', '9050' : '0'}  #集計結果リストの初期化
    #print(result_count_dict)
    #print(type(result_count_dict))
    for word, count in counter.most_common():
        for dict_gyoushu in df_dictionary:
            
            if dict_gyoushu[1] == word:
                #print("合致!!") 
                #print(result_count_dict[str(dict_gyoushu[0])])
                #print(count)
                result_count_dict[str(dict_gyoushu[0])] = str(int(result_count_dict.get(str(dict_gyoushu[0]))) + int(count)  ) 
    
    resultDict = result_count_dict
    # 結果ファイルのパス(ファイル名は仮置き)
    outputFile = '/Users/tabatatoshinori/git/TomatoPJ/work/10_tabata/03_PGM/ver1.0/output/submission.csv'
    file = open(outputFile, 'w', encoding='utf-8')
    #　上位３位の業種にソート ⇒　sortResultの辞書へ
    sortResult = sorted(resultDict.items(), key=lambda x: x[1], reverse=True)[:10]

    #ファイル名取得はinput時にファイル名から取得して、以下へ入れ込む
    writeStr = 'ファイル名,'

    for k, v in sortResult:
        writeStr += str(k)+','

    file.write(writeStr)
    file.close()