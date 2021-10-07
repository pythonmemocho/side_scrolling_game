from settings import *
import csv

#csvからデータを呼び出して、リストに格納する。
stage_data = []
#with openでファイルを開き、1行づつ空のリストに格納
with open("stage.csv",newline='') as data:
    reader = csv.reader(data,delimiter=',')
    for row in reader:
        #リストに格納する内容は文字列型(str)になっているので数値型(int)に変換します。
        #map関数はリストの内容1つ毎に関数を実行してくれます。関数実行後rowに再代入します。
        row = list(map(int,(row)))
        #ここでprintを記述すればどのような内容がリストに格納されるか確認できます。
        # print(row)
        stage_data.append(row)