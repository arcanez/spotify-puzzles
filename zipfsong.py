(n, m) = raw_input().split()

r = dict()

for i in range(0, int(n)):
  (f, s) = raw_input().split()
  z = 1/float(i+1)
  q = int(f)/z
  r[str(q)] = s

_s = sorted(r, key=float, reverse=True)
for x, y in enumerate(_s[:int(m)]):
  print r[y]
