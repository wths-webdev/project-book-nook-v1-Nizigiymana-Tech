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
image = climage.convert("images/book-nook-logo.png", is_unicode=True, width=80)

# Welcome Message
print("Welcome to...")
time.sleep(2)
# print(image)
print(r"""
         ______ ______
        _/      Y      \_
       // ~Book | ~~ ~  \
      // ~ ~ ~~ |  Nook~ \      
     //________.|.________\     
    `----------`-'----------'
    """)

time.sleep(2)

def Readyup():
    input("Click enter when ready ")
    return

def add():
    BookName = input("What's the book's name? ")
    Books.append(BookName)
    print("Added your book!")
    Readyup()
    return

def remove():
    if len(Books) < 1:
        print("No books to remove.")
        Readyup()
        return
    
    BookName = input("What book do you wanna remove? ")

    try: 
        Books.remove(BookName)
    except ValueError:
        print(f"Error: {BookName} not in inventory.")
        Again = input("Do you wanna try again? (Y/N) ")
        if Again == "Y":
            remove()
            return
        else:
            return

    print("Removed your book!")
    Readyup()
    return

def count():
    print(f"There are {len(Books)} in your inventory.")
    Readyup()
    return

def show():
    print(f"There are {len(Books)} in your inventory.")
    if len(Books) == 0:
        return
    
    for i in range(len(Books)):
        print(f"{i + 1}. {Books[i]}")

    Readyup()
    return

actions = {"add": add, "remove": remove, "count": count, "show": show}

#Open Menu
while True:
    print("""
        Menu: 
        Add book (add)
        Remove book (remove) 
        show inventory (show)
        Show inventory count (count) 
        Quit (q)
        """)
    
    action = input("What would you like to do? ")

    if action == "q":
        break

    try:
        actions[action]()
    except KeyError:
        print("Not a option. Choose again!")
        Readyup()

        
