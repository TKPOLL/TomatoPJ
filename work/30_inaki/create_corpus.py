#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import MeCab
import sys
import re
from collections import Counter

# ファイルパス
inputDir = r'C:\\Users\1627538\\Desktop\\ショートカット\\業務\\AIコンテスト\\学習用データ_20190702再配布\\学習用データ_20190702再配布'
outputFile = r"C:\\Users\1627538\\Desktop\\ショートカット\\業務\\AIコンテスト\\学習用データ_20190702再配布\\学習用データ_20190702再配布\\countResult.csv"

#インプットファイルに入っているファイルの一覧をリストに追加（フルパス）
inputDirs=[]
inputFiles=[]

#結果格納用リスト
counter=[]

#インプット元ディレクトリに入ってるディレクトリ一覧を作成
for dir in os.listdir(inputDir):
    if os.path.isdir(inputDir +'\\'+dir):
        inputDirs.append(inputDir +'\\'+dir)
        print(dir)
#print(inputDirs)

#インプットファイルに入っているファイルの一覧をリストに追加（全量フルパス）
for dir in inputDirs:
    for file in os.listdir(dir):
        #inputDir以下に格納されているものがファイルだった場合、フルパスを作成
        if not os.path.isdir(dir + '\\' + file):
            inputFiles.append(dir + '\\' + file)

#print(inputFiles)

for inputFile in inputFiles:
    
    #使用する関数の初期化
    data=[]
    words=[]
    conpCode=''
    stripStr=inputDir+'\\'
    
    #フォルダパスから業種IDを取得
    conpCode = os.path.dirname(str(inputFile)).lstrip(stripStr)
    
    #print(conpCode)
    
    inFile = open(inputFile, 'r', encoding='utf-8')
    data = inFile.read()
    
    # パース
    mecab = MeCab.Tagger()
    parse = mecab.parse(data)
    lines = parse.split('\n')
    items = (re.split('[\t,]', line) for line in lines)

    #名詞をリストに格納
    words = ['"'+conpCode+'","'+str(item[0])+'"'
            for item in items
                if (item[0] not in ('EOS', '', 't', 'ー','\n') and not re.match('[a-zA-Z0-9]{1}$' , str(item[0])) and
                     item[1] == '名詞' and item[2] == '一般') and words not in item]

    #辞書の中をリスト化
    if not os.path.exists(outputFile):
        outFile = open(outputFile, 'a', encoding='utf-8',newline='\n')
        outFile.close()
    #outFile = open(outputFile, 'r', encoding='utf-8',newline='\n')
    #corpusDatas=[]
    #for corpus in outFile.readlines():
        #corpusDatas = corpus.rstrip('\n')
        
    #リストを結合
    #words.extend(corpusDatas)
    
    # リストの重複をcounterリストへ格納
    counter = Counter(words)
    
    #インプットファイルをクローズ
    inFile.close()

    
# 重複を除いたファイルを出力ファイルへ書き込み
outFile = open(outputFile, 'a', encoding='utf-8',newline='\n')
for word, count in counter.most_common():
    if not str(word) == '':
        outFile.write(str(word) + "\n")
outFile.close()
