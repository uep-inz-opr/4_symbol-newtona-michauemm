import math
n, k = input().split()
n = int(n)
k = int(k)
nsil = math.factorial(n)
ksil = math.factorial(k)
nsilOdksil = math.factorial(n-k)
wzor = nsil/(ksil*nsilOdksil)
print(wzor)
