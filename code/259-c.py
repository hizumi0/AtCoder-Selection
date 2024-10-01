s = input()
t = input()

def text_count(iS):
  S = []
  count = 1
  stock = iS[0]
  for s in iS[1:]:
    if stock == s:
      count += 1
    else:
      S.append([stock,count]) #文字と続いた回数をセットで
      stock,count = s,1 #　リセット
  S.append([stock,count])
  return(S)

S,T = text_count(s),text_count(t)

if len(S) != len(T):#そもそも長さが違えばNG
  print("No")
else:
  flag = True
  for sc,tc in zip(S,T):
    if sc[0] == tc[0] and tc[1]>=sc[1]>=2:
      continue
    elif sc[0] == tc[0] and tc[1] == sc[1] ==1:
      continue
    else:
      flag = False
      break
  if flag:
    print("Yes")
  else:
    print("No")