#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import MeCab
import re
from collections import Counter

# ファイルパス
# ---------------------------- 変更値 -----------------------------------------------

#修正イメージ(以下指定じゃ動きませんでした)
#inputDir = r'\\program\\input\\learn'
#outputFile = r"\\program\\myCopus.csv"

#inputファイルが入っているディレクトリのパス
#inputDir = r'C:\\Users\1627538\\Desktop\\ショートカット\\業務\\AIコンテスト\\学習用データ_20190702再配布\\学習用データ_20190702再配布'
#outputファイルのパス：ファイル名まで記載（CSVファイル）
#outputFile = r"C:\\Users\1627538\\Desktop\\ショートカット\\業務\\AIコンテスト\\学習用データ_20190702再配布\\学習用データ_20190702再配布\\myCopus.csv"

#相対パス指定
currentDir = os.getcwd()
strCurrentDir = str(currentDir)
defultInputPath = 'input\\learn'
outputFileName =  'myCopus.csv'

inputDir = currentDir + '\\' + defultInputPath
outputFile = currentDir + '\\' + outputFileName

# -----------------------------------------------------------------------------------

#インプットファイルに入っているファイルの一覧をリストに追加（フルパス）
inputDirs=[]
inputFiles=[]

#結果格納用リスト
counter = []
words = []
dirWords = []
corpusWords = []
compWords = []
uniqWords = []
uniqCounter = []

#インプット元ディレクトリに入ってるディレクトリ一覧を作成
for dir in os.listdir(inputDir):
    if os.path.isdir(inputDir +'\\'+dir):
        inputDirs.append(dir)

#インプットファイルに入っているファイルの一覧をリストに追加（全量フルパス）
for dir in inputDirs:
    for file in os.listdir(inputDir +'\\'+dir):
        #使用する関数の初期化
        data=[]
        #フォルダパスから業種IDを取得
        conpId = dir.split('_')[0]

        #print(conpId)
        print(inputDir +'\\'+dir+'\\'+file)
        inFile = open(inputDir +'\\'+dir+'\\'+file, 'r', encoding='utf-8')
        data = inFile.read()

        # パース
        mecab = MeCab.Tagger()
        parse = mecab.parse(data)
        lines = parse.split('\n')
        items = (re.split('[\t,]', line) for line in lines)

        #名詞をリストに格納
        #words = (['"'+conpId+'","'+str(item[0])+'"'
                #for item in items
                    #if (item[0] not in ('EOS', '', 't', 'ー','\n','\t',' ') and not re.match('[\\sa-zA-Z0-9]{1}$' , str(item[0])) and
                        #(item[1] == '名詞' and item[2] == '一般'))])
		
		#名詞をリストに格納
        words = ([item[0]
                for item in items
                    if (item[0] not in ('EOS', '', 't', 'ー','\n','\t',' ') and not re.match('[\\sa-zA-Z0-9]{1}$' , str(item[0])) and
                        (item[1] == '名詞' and item[2] == '一般'))])
		
        dirWords.extend(words)
        #インプットファイルをクローズ
        inFile.close()
    
    counter.extend(Counter(dirWords).keys())
    uniqCounter = set(counter)
    
    for word in uniqCounter:
    	compWords.append(str('"' + conpId + '","' + str(word) + '"'))
    

# 重複を除いたファイルを出力ファイルへ書き込み
outFile = open(outputFile, 'a', encoding='utf-8',newline='\n')
for word in Counter(compWords).keys():
    if not str(word) == '':
        outFile.write(str(word) + "\n")
outFile.close()
