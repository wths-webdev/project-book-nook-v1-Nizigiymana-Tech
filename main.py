#  List of books
# print wlecome messages
# open menu
# ask user for input
# ask user for books
# add to list
# success message
# if "show"
#print out list
from term_image.image import from_file
import time

Books = []
image = from_file("book-nook-logo.png")

# Welcome Message
print("Welcome to...")
time.sleep(2)
image.draw()