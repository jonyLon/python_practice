num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
try:
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Zero Division Error")

def division(n1,n2):
    result = num1 / num2
    print(result)
try:
    division(num1,num2)
except ZeroDivisionError:
    print("Zero Division Error")

def division2(n1,n2):
    try:
        result = num1 / num2
        print(result)
    except ZeroDivisionError:
        print("Zero Division Error")
division2(num1,num2)

try:
  line = int(input("Enter number: "))
  print(line)
except ValueError:
    print("Can't transform. Wrong value")

def transformToNum():
    line = int(input("Enter number: "))
    print(line)

try:
  transformToNum()
except ValueError:
  print("Can't transform. Wrong value")

def transformToNum1():
  try:
    line = int(input("Enter number: "))
    print(line)
  except ValueError:
      print("Can't transform. Wrong value")
transformToNum1()