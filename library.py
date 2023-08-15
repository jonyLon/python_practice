library = [
    [
        "The Master and Margarita",
        "Mikhail Bulgakov",
        "XYZ Publishers",
        "Fantasy",
        250,
        4.7
    ],
    [
        "1984",
        "George Orwell",
        "ABC Literary Agency",
        "Dystopia",
        180,
        4.5
    ],
    [
        "Game of Thrones",
        "George R. R. Martin",
        "QWE Publishers",
        "Fantasy",
        320,
        4.8
    ],
    [
        "The Shadow of the Wind",
        "Carlos Ruiz Zafón",
        "ZXC Publishers",
        "Mystery",
        210,
        4.6
    ],
    [
        "Harry Potter and the Philosopher's Stone",
        "J. K. Rowling",
        "ASD Publishers",
        "Fantasy",
        280,
        4.9
    ],
    [
        "War and Peace",
        "Leo Tolstoy",
        "QAZ Publishers",
        "Novel",
        350,
        4.7
    ],
        [
        "To Kill a Mockingbird",
        "Harper Lee",
        "LMN Publishers",
        "Classic",
        220,
        4.9
    ],
    [
        "Pride and Prejudice",
        "Jane Austen",
        "OPQ Publishers",
        "Romance",
        200,
        4.8
    ],
    [
        "The Great Gatsby",
        "F. Scott Fitzgerald",
        "RST Publishers",
        "Classic",
        270,
        4.7
    ],
    [
        "Brave New World",
        "Aldous Huxley",
        "UVW Publishers",
        "Science Fiction",
        230,
        4.6
    ]
]

def editBook():
    try:
      bookIndex = int(input("Enter number of the book you want to edit: "))
      print(library[bookIndex])
      keysIndex = int(input("Enter index of characteristic(0-Title,1-Author,2-Publisher,3-Genre,4-Price,5-Rating): "))
      print(library[bookIndex][keysIndex])
      if keysIndex == 4:
          newNumValue = int(input("Enter new price value: "))
          if newNumValue == 0:
            raise ValueError("Wrong prise")
      elif keysIndex == 5:
          newNumValue = float(input("Enter new rating value: "))
          if newNumValue > 5:
            raise ValueError("Rating value can't be more then 5")
      else:
          newNumValue = str(input("Enter new value: "))
      library[bookIndex][keysIndex] = newNumValue
      print(library[bookIndex][keysIndex])
    except ValueError as ex:
        print(ex)
    except IndexError:
        print("You entered wrong index")
# editBook()

def printAllBooks():
  print("\t\tName\t\t\t\t\tAutor\t\tRublisher\t\tGenre\t\t\tPrice\tRating")
  for i in library:
    spaces = 45 - len(i[0])
    spaces1 = 25 - len(i[1])
    spaces2 = 25 - len(i[2])
    spaces3 = 20 - len(i[3])
    print("{}".format(i[0])+" "*spaces,end="")
    print("{}".format(i[1])+" "*spaces1,end="")
    print("{}".format(i[2])+" "*spaces2,end="")
    print("{}".format(i[3])+" "*spaces3,end="")
    print("\t{}\t{}".format(i[4],i[5]))
  print()
# printAllBooks()

def addBook():
  try:
    name = input("Enter name of a book: ")
    autor = input("Enter autor of a book: ")
    publisher = input("Enter publisher of a book: ")
    genre = input("Enter genre of a book: ")
    price = int(input("Enter price of a book: "))
    if price == 0:
      raise ValueError("Wrong prise")
    rating = float(input("Enter rating of a book: "))
    if rating > 10:
      raise ValueError("Rating value can't be more then 10")
    library.append([name,autor,publisher,genre,price,rating])
    printAllBooks()
  except ValueError as ex:
    print(ex)
# addBook()

def deleteBook():
  try:
    index = int(input("Enter index of the book you want to delete: "))
    library.pop(index)
    printAllBooks()
  except IndexError:
    print("You entered wrong index of the book")
# deleteBook()

def searchBookByTitle(title):
  found = False
  for i in library:
    if i.count(title)>0:
      found = True
      print(i)
  if not found:
    print("Book with such a title wasn't found")

# searchBookByTitle("Brave New World")

def searchBookByAuthor(author):
  found = False
  for i in library:
    if i.count(author)>0:
      found = True
      print(i)
  if not found:
    print("Book with such an author wasn't found")
# searchBookByAuthor("Leo Tolstoy")

def sortByTitle():
  def byTitle(i):
    return i[0]
  library.sort(key=byTitle)
  printAllBooks()
# sortByTitle()

def sortByAuthor():
  def byAuthor(i):
    return i[1]
  library.sort(key=byAuthor)
  printAllBooks()
# sortByAuthor()

def sortByPablisher():
  def byPablisher(i):
    return i[2]
  library.sort(key=byPablisher)
  printAllBooks()
# sortByPablisher()

def sortByPrice():
  def byPrice(i):
    return i[4]
  library.sort(key=byPrice)
  printAllBooks()
# sortByPrice()

def sortByRating():
  def byRating(i):
    return i[5]
  library.sort(key=byRating)
  printAllBooks()
# sortByRating()

while True:
  option = int(input("\n1 - edit book \n2 - print all books \n3 - add book \n4 - delete book \n5 - search book by author \n6 - search book by title \n7 - sort books by title \n8 - sort books by author \n9 - sort books by pablisher \n10 - sort books by price \n11 - sort books by rating \n0 - exit \nChoose action you want to preform: "))
  match option:
    case 0:
      break
    case 1:
      editBook()
    case 2:
      printAllBooks()
    case 3:
      addBook()
    case 4:
      deleteBook()
    case 5:
      author = input("Enter author of the desired book: ")
      searchBookByAuthor(author)
    case 6:
      title = input("Enter title of the desired book: ")
      searchBookByTitle(title)
    case 7:
      sortByTitle()
    case 8:
      sortByAuthor()
    case 9:
      sortByPablisher()
    case 10:
      sortByPrice()
    case 11:
      sortByRating()
    case _:
      print("You entered wrong number of option. Try again.")
    