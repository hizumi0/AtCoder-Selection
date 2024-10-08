a, b, c ,x ,y = map(int, input().strip().split())

if x < y: # (※1)　必ずxが大きくなるように、Aピザの必要枚数xとBピザの必要枚数yを比較する。
    a, b = b, a
    x, y = y, x

piza_ab = a * x + b * y # (※2)
piza_c = c * 2 * x # (※3)
piza_cb = a * (x - y) + c * 2 * y # (※4)

price = [piza_ab, piza_c, piza_cb]
new_price= sorted(price)
print(new_price[0])