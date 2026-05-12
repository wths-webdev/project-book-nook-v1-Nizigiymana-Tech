import time

Books = []

print("Welcome to...")
time.sleep(2)

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

def count():
    print(f"There are {len(Books)} in your inventory.")
    Readyup()

def show():
    if len(Books) == 0:
        return
    for i in range(len(Books)):
        print(f"{i + 1}. {Books[i]}")
    Readyup()
    
actions = {"add": add, "remove": remove, "count": count, "show": show}

while True:
    print("""
        Menu: 
        Add book (add)
        Remove book (remove) 
        show inventory (show)
        Show inventory count (count) 
        Quit (q)
        """)
    
    action = input("What would you like to do? ").strip().lower()

    if action == "q":
        break

    try:
        actions[action]()
    except KeyError:
        print("Not a option. Choose again!")
        Readyup()