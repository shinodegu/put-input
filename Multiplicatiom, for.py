
s=0

n=int(input())
for x in range(n+1):
    if x%3 != 0:
      s = x ** 3 + s
print(s)