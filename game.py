import random
import msvcrt
list = [["    " for i in range(4)] for i in range(4)]
print(list)
arr = [i for i in range(1,16)]
def getRandomFromList():
  if len(arr) != 0:
    option = random.choice(arr)
    arr.remove(option)
    return option
  else:
    return " "
def mixNumbers():
  for i in range(4):
    for j in range(4):
      num = str(getRandomFromList())
      if len(num) == 2:
        list[i][j] = ' '+num+' '
      else:
        list[i][j] = '  '+num+' '


def showField():
  print()
  print(list[0][0], chr(9474),list[0][1], chr(9474),list[0][2],chr(9474), list[0][3], sep="")
  print(chr(9472)*4, chr(9532),chr(9472)*4,chr(9532),chr(9472)*4, chr(9532), chr(9472)*4, sep="")
  print(list[1][0], chr(9474),list[1][1], chr(9474),list[1][2],chr(9474), list[1][3], sep="")
  print(chr(9472)*4, chr(9532),chr(9472)*4,chr(9532),chr(9472)*4, chr(9532), chr(9472)*4, sep="")
  print(list[2][0], chr(9474),list[2][1], chr(9474),list[2][2],chr(9474), list[2][3], sep="")
  print(chr(9472)*4, chr(9532),chr(9472)*4,chr(9532),chr(9472)*4, chr(9532), chr(9472)*4, sep="")
  print(list[3][0], chr(9474), list[3][1], chr(9474),list[3][2],chr(9474), list[3][3], sep="")
  print()

def changeTemplate(num):
  x = str(num)
  if len(x) == 2:
    line = ' '+x+' '
  else:
    line = '  '+x+' '
  return line

def indexFound(y):
  line = changeTemplate(y)
  for i in range(4):
    if list[i].count(line)>0:
      return [i, list[i].index(line)]
    
def pointOutCell(indexes,num):
  line = str(num)
  if len(line) == 2:
    list[indexes[0]][indexes[1]] = '['+str(line)+']'
  else:
    list[indexes[0]][indexes[1]] = ' ['+str(line)+']'
def isNearbyCellEmpty(i):
  if list[i[0]][i[1]] == "    ":
    return True
  else:
    return False

mixNumbers()
workflow = True
while workflow:
  showField()
  inputNum = input("Enter number which has empty cell nearby if you want to move it or 0 if you want to exit: ")
  if inputNum == 0:
    break
  indexes = indexFound(inputNum)
  pointOutCell(indexes,inputNum)
  showField()
  print("Use w,a,s,d keys on keyboard for moving number to empty cell")
  while True:
    key = msvcrt.getch()
    # w - 119, s - 115, a - 97, d - 100
    match ord(key):
      case 119:
        iOfEmptyCell = [indexes[0]-1,indexes[1]]
        if isNearbyCellEmpty(iOfEmptyCell):
          line = changeTemplate(inputNum)
          list[iOfEmptyCell[0]][iOfEmptyCell[1]] = line
          list[indexes[0]][indexes[1]] = "    "
          showField()
          break
        else:
          showField()
          print("There isn't empty cell")
      case 115:
        iOfEmptyCell = [indexes[0]+1,indexes[1]]
        if isNearbyCellEmpty(iOfEmptyCell):
          line = changeTemplate(inputNum)
          list[iOfEmptyCell[0]][iOfEmptyCell[1]] = line
          list[indexes[0]][indexes[1]] = "    "
          showField()
          break
        else:
          showField()
          print("There isn't empty cell")
      case 97:
        iOfEmptyCell = [indexes[0],indexes[1]-1]
        if isNearbyCellEmpty(iOfEmptyCell):
          line = changeTemplate(inputNum)
          list[iOfEmptyCell[0]][iOfEmptyCell[1]] = line
          list[indexes[0]][indexes[1]] = "    "
          showField()
          break
        else:
          showField()
          print("There isn't empty cell")
      case 100:
        iOfEmptyCell = [indexes[0],indexes[1]+1]
        if isNearbyCellEmpty(iOfEmptyCell):
          line = changeTemplate(inputNum)
          list[iOfEmptyCell[0]][iOfEmptyCell[1]] = line
          list[indexes[0]][indexes[1]] = "    "
          showField()
          break
        else:
          showField()
          print("There isn't empty cell")
      case 27:
        break