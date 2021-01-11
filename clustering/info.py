import math

def infoDInner(x):
  if x == 0:
    return 0
  return x * math.log(x, 2)

def attributeInfoD(vals):
  values = 0
  for val in vals:
    values += val[0] * (-(infoDInner(val[1]) + infoDInner(val[2])))

  return values

x = [[8/26,1/8,7/8],[18/26,5/18,13/18]]
print(attributeInfoD(x))