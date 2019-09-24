#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 15:53:43 2019

@author: tabatatoshinori
"""
import os

import MeCab
import sys
import re
from collections import Counter

# ファイルパス
inputDir = 'D:\\PycharmProjects\\TomatoPJ\\work\\30_inaki\\input'
#infile = "D:\\PycharmProjects\\TomatoPJ\\work\\30_inaki\\input\\パルプ・紙_522894.xml"
outputFile = "D:\\PycharmProjects\\TomatoPJ\\work\\30_inaki\\output\\countResult.txt"

#インプットファイルに入っているファイルの一覧をリストに追加（フルパス）
inputDirs=[]
inputFiles=[]

#インプット元ディレクトリに入ってるディレクトリ一覧を作成
for dir in os.listdir(inputDir):
    if os.path.isdir(inputDir +'\\'+dir):
        inputDirs.append(inputDir +'\\'+dir)
print(inputDirs)

#インプットファイルに入っているファイルの一覧をリストに追加（全量フルパス）
for dir in inputDirs:
    for file in os.listdir(dir):
        #inputDir以下に格納されているものがファイルだった場合、フルパスを作成
        if not os.path.isdir(dir + '\\' + file):
            inputFiles.append(dir + '\\' + file)

print(inputFiles)

for inputFile in inputFiles:
    print(inputFile)

    inFile = open(inputFile, 'r', encoding='utf-8')
    data = inFile.read()
    # パース
    mecab = MeCab.Tagger()
    parse = mecab.parse(data)
    lines = parse.split('\n')
    items = (re.split('[\t,]', line) for line in lines)

    # 名詞をリストに格納
    words = [str(item[0])
            for item in items
                if (item[0] not in ('EOS', '', 't', 'ー') and
                     item[1] == '名詞' and item[2] == '一般')]

    #辞書の中をリスト化
    if not os.path.exists(outputFile):
        outFile = open(outputFile, 'w', encoding='utf-8',newline='\n')
        outFile.close()
    outFile = open(outputFile, 'r', encoding='utf-8',newline='\n')
    corpusDatas=[]
    for corpus in outFile.readlines():
        corpusDatas = corpus

    print(corpusDatas)
    #リストを結合
    words.extend(corpusDatas)

    # リストの重複をcounterリストへ格納
    counter = Counter(words)
    # 重複を除いたファイルを出力ファイルへ書き込み
    outFile = open(outputFile, 'w', encoding='utf-8',newline='\n')
    for word, count in counter.most_common():
        outFile.write(word + "\n")
    outFile.close()

    #インプットファイルをクローズ
    inFile.close()