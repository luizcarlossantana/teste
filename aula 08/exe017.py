import math
c1 = int(input('digite o cateto oposto'))
c2 = int(input('digite o cateto adjascente'))
h = math.hypot(c1,c2)
print(f'{h:.1f}')