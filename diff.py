def strc(l):
  diffs = []
  for i in range(0,len(l)-1):
    if(l[i+1] >= l[i]):
      diff = l[i+1] - l[i]
    else:
      diff = l[i] - l[i+1]
    diffs.append(diff)
  for i in range(len(diffs)-1):
    if(diffs[i] >= diffs[i+1]):
      return False
  return True
l = list(map(int,input("enter elements: ").split()))
print(strc(l))