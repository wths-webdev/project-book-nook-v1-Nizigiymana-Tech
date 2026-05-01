#  List of books
# print wlecome messages
# open menu
# ask user for input
# ask user for books
# add to list
# success message
# if "show"
#print out list
import climage
import time

Books = []
Options = ["add", "remove", "count", "q"]
image = climage.convert("images/book-nook-logo.png", is_unicode=True, width=80)

# Welcome Message
print("Welcome to...")
time.sleep(2)
print(image)
print("""""
         ______ ______
        _/      Y      \_
       // ~Book | ~~ ~  \
      // ~ ~ ~~ |  Nook~ \      
     //________.|.________\     
    `----------`-'----------'
    """)

def add():
    BookName = input("What's the book's name? ")
    Books.append(BookName)
    print("Added your book!")
    print(f"Books: {Books}")
    return

#Open Menu
while True:
    print("""
        Menu: 
        Add book (add)
        Remove book (remove) 
        Show inventory count (count) 
        Quit (q)
        """)
    
    Action = input("What would you like to do? ")

    try:
        Action()
    except TypeError:
        print("Not a option. Choose again!")
        
