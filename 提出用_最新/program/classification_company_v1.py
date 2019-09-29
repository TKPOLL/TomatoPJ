#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:50:09 2019

@author: tabatatoshinori
"""

import os
import pandas as pd
import MeCab
import re
from collections import Counter

#相対パス指定
currentDir = os.getcwd()
defultInputPath = 'input/question'
outputFileName =  'AIコンテスト予測結果_チーム名.csv'
inputDir = currentDir + '/' + defultInputPath
outputFile = currentDir + '/' + outputFileName


#学習結果の読み込み処理
df_dictionary1 = pd.read_csv(currentDir + '/myCopus.csv')
df_dictionary = df_dictionary1.values.tolist()

tagger = MeCab.Tagger()

#結果書き込みリストの初期化
answerList = []

#読み込み＆集計処理
for file in os.listdir(inputDir):
    #print(file)
    with open(inputDir +'/'+file, "r", encoding="UTF-8") as f:
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
        result_count_dict = {'1' : '0', '2' : '0', '3' : '0', '4' : '0', '5' : '0', '6' : '0', 
                             '7' : '0', '8' : '0', '9' : '0', '10' : '0', '11' : '0', '12' : '0', 
                             '13' : '0', '14' : '0', '15' : '0', '16' : '0', '17' : '0', '18' : '0', 
                             '19' : '0', '20' : '0', '21' : '0', '22' : '0', '23' : '0', '24' : '0', 
                             '25' : '0', '26' : '0', '27' : '0', '28' : '0', '29' : '0', '30' : '0', 
                             '31' : '0', '32' : '0', '33' : '0'}  #集計結果リストの初期化(出力時に、左0埋めを行う)

        for word, count in counter.most_common():
            for dict_gyoushu in df_dictionary:
            
                if dict_gyoushu[1] == word:

                    result_count_dict[str(dict_gyoushu[0])] = str(int(result_count_dict.get(str(dict_gyoushu[0]))) + int(count)  ) 
        #print(result_count_dict)           
        resultDict = result_count_dict

    #　上位３位の業種にソート ⇒　sortResultの辞書へ
    sortResult = sorted(resultDict.items(), key=lambda x: x[1], reverse=True)[:3]
    #ファイル名取得はinput時にファイル名から取得して、以下へ入れ込む
    writeStr =  str(file).rstrip(".txt")
    for k, v in sortResult:
        writeStr += ',' + str(k).zfill(2)
    answerList.append(writeStr + '\n')
    
#評価結果書き出し
outputFileInstance = open(outputFile, 'w', encoding='utf-8')
for answer in answerList:
    outputFileInstance.write(answer)
outputFileInstance.close()