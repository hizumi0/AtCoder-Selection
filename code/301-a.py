from collections import Counter
n = input()
S = input()
Awin = S.count('A')  # 文字列S中の 'A' の数をカウント
Twin = S.count('T')  # 文字列S中の 'T' の数をカウント
if Awin == Twin:  # 'A' と 'T' の数が同じ場合
  for s in S:
    if s == "A":
      Awin -= 1
      if Awin == 0:
        print("A")  # 'A' の数が0になった時点で 'A' を出力し、プログラムを終了
        exit()
    else:
      Twin -= 1
      if Twin == 0:
        print("T")  # 'T' の数が0になった時点で 'T' を出力し、プログラムを終了
        exit()
elif Awin > Twin:
  print("A")  # 'A' の数が 'T' より多い場合、 'A' を出力
else:
  print("T")  # それ以外の場合（'T' の数が 'A' より多い場合）、 'T' を出力