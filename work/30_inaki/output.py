# ===================== 結果書き込み用のプログラム（仮）！！！ ==========================


# 一旦仮置きで、評価用のディクショナリを！
templeteDict = {"0050": "0", "1050": "0", "2050": "8", "3050": "0", "3100": "0", "3150": "0", "3200": "0", "3250": "0",
                "3300": "0", "3350": "0", "3400": "0", "3450": "0", "3500": "0", "3550": "0", "3600": "0", "3650": "0",
                "3700": "0", "3750": "0", "3800": "5", "4050": "0", "5050": "0", "5100": "0", "5150": "0", "5200": "0",
                "5250": "4", "6050": "0", "6100": "0", "7050": "0", "7100": "0", "7150": "0", "7200": "0", "8050": "0",
                "9050": "0"}
resultDict = templeteDict
# 結果ファイルのパス(ファイル名は仮置き)
outputFile = 'D:\\PycharmProjects\\TomatoPJ\\work\\30_inaki\\output\\submission.csv'
file = open(outputFile, 'w', encoding='utf-8')
#　上位３位の業種にソート ⇒　sortResultの辞書へ
sortResult = sorted(resultDict.items(), key=lambda x: x[1], reverse=True)[:3]

#ファイル名取得はinput時にファイル名から取得して、以下へ入れ込む

writeStr = 'ファイル名,'

for k, v in sortResult:
    writeStr += str(k)+','

file.write(writeStr)
file.close()
