import math
try:
  num = int(input("Enter number: "))
  result = math.sqrt(num)
  print(result)
except ValueError:
  print("wrong value")

def sqrt(num):
  try:
    result = math.sqrt(num)
    print(result)
  except ValueError:
    print("wrong value")

sqrt(num)

def sqrt1(num):
  result = math.sqrt(num)
  print(result)
  
try:
  sqrt1(num)
except ValueError:
  print("wrong value")