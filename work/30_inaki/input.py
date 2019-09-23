
import glob

# ========= ファイルのinputを行う処理 =====================
inputPath = 'D:\\PycharmProjects\\TomatoPJ\\work\\10_tabata\\02_data\\10_業種データ01\\*'
glob.glob(inputPath)

for x in glob.glob(inputPath) :
    print('"' + x + ':""0"')

