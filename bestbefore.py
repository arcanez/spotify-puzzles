from datetime import date
from itertools import permutations

dates = []
date_input = raw_input()

for [a, b, c] in permutations(map(int, date_input.split('/', 3))):
  if a < 2000:
    a += 2000
  try:
    dates.append(date(a, b, c))
  except:
    continue

try:
  print min(dates).isoformat()
except:
  print "%s is illegal" % date_input
