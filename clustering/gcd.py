def gcd(x,y):
  remainder = x % y
  division = x // y
  if remainder == 0:
    print(x, "=", y, "x", division)
    return 0
  print(x, "=", y, "x", division, "+", remainder)
  gcd(y, remainder)

gcd(11,7)