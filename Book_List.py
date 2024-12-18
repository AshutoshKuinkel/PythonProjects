#A simple program which stores a book read and displays it.

from simple_colors import * # A library which allows text to be Coloured, Bold or Underlined. 

def home_page(): # The homepage, gives a brief introduction on the program and welcomes the user.

    print(green("✨ BookList Maker ✨ ",'underlined')) # This is how this simple_colors is used: print(color(text),'bold' | 'underlined').

    print(yellow("Welcome to the BookList Maker.\n")) # \n creates a new line.

    print(yellow("Here you can make a list of books you have read and view them.\n   ")) 
    print(yellow("Your reading progress can be tracked and to motivate you daily quotes will be displayed!\n "))
    
home_page()
#Do not call function home_page() at all until the end, unless making changes to it, it's not needed.

Books = {
} # Dictonary to store book name, author and amount of pages.
    

def addbook():
    book_name = str(input(green(" 📖 Please enter the title of the book: "))) # Title of Book.
    Books.update({' 📗 BOOK' : book_name}) # Adding the book name to the dictonary.
    book_author = str(input(green(" 🧔 Please enter the Author of the book: "))) # Author of Book.
    Books.update({' 🙍 AUTHOR' : book_author}) # Adding the author to the dictonary
    book_pages = int(input(green(" 📃 Please enter the number of pages: "))) # Amount of pages within book.
    Books.update({' 📄 PAGES' : book_pages}) # Adding the amount of pages within book to dictonary.
    print("\n")
    print(magenta("Thank you, you're selection has been stored within our libraries.")) #Notifying user book has been stored.


def viewbook():
    print(Books) # Spits out the dictonary. 
    if len(Books) == 0:
        print(green("Nothing to be displayed. 😐")) # If the length of the dictonary is 0 then display this message.



def choices_menu(): # The startup menu which allows the user to make a choice of what they would like to do.
    print(blue("If you would like to add a new book to the list please press 1️⃣ \n"))
    print(blue("If you would like to view books read please press 2️⃣ \n"))
    print(blue("To QUIT the program, please press 3️⃣ \n"))
    choice = int(input(cyan("Please enter either 1️⃣, 2️⃣ or 3️⃣ :\n")))

    if choice == 1:
        print("\n")
        addbook() #If the user selects one, call function adbook().
    elif choice == 2:
        print("\n")
        viewbook() #If the user selects two, call function viewbook().
    elif choice == 3:
        quit() #If the user selects three, quit the program.
    

startup = input(magenta("➡️  Please Press [X] to start the program:\n")) # Telling the user they have to press that to start program.
startup = startup.lower() # This avoids the need for the user to type capital x or lower case x, they can type whichever.

if startup == 'x':
    print("\n")
    choices_menu() # This is saying, execute the function choices_menu if the user inputs x.

else:
    raise Exception(red("Please run the program again and if you would like to start the program press [X].")) # Notifies user of error.


while True:
    choices_menu() # Finally found a solution to this problem LOL 😆. Loops through the choices until program is QUIT. 
