import math

def log2(x):
  if x == 0:
    return 0
  return math.log(x,2)

def infoD(vals):
  
  sumVals = 0
  for val in vals:
    sumVals += (((val) * log2(val)))
  print("Info D:")
  return -sumVals

def attributeInfoDHelper(x):
  if x == 0:
    return 0
  return x * log2(x)

def attributeInfoD(vals):
  values = 0
  for val in vals:
    values += val[0] * (-(attributeInfoDHelper(val[1]) + attributeInfoDHelper(val[2])))

  print("Info(Attribute)D")
  return values

def gini(vals):
  sumVals = 0
  for val in vals:
    sumVals += val**2
  print("Gini:")
  return 1 - sumVals

def giniIndex(vals):
  sumVals = 0
  for val in vals:
    sumVals += (val[0] * (gini([val[1],val[2]])))
  print("Gini Index:")
  return sumVals

def splitInfo(vals):
  sumVals = 0
  for val in vals:
    sumVals += ((val) * log2(val))
  print("Split Info:")
  return -sumVals

def gain(infoD, infoA_D):
  print("Gain:")
  return infoD - infoA_D

def gainRatio(gainA, splitInfoA):
  print("Gain Ratio:")
  return gainA/splitInfoA

print(attributeInfoD([[4/14,4/4,0/4],[5/14,3/5,2/5],[5/14,2/5,3/5]]))
#print(infoD([9/14,5/14]))
#print(splitInfo([4/14,6/14,4/14]))
#print(gini([9/14,5/14]))
#print(giniIndex([[10/14,7/10,3/10],[4/14,2/4,2/4]]))