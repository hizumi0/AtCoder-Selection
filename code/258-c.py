N,Q = map(int,input().split())
S = list(input())
index = 0
for _ in range(Q):
  q,x = map(int,input().split())
  if q == 1:
    index = (index-x)%N
    #`q` が `1` の場合、文字列の開始位置を `x` だけ左にシフトします。
    # シフト後のインデックスは `(index-x)%N` で計算されます。
  else:
    print(S[(index+x-1)%N])