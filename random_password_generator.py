import random #importing random module
import tkinter as tk #importing tkinter this as tk is important
from tkinter import messagebox #useful when trying to display an error.

def programfunc(length):
    special = ['!','@','#','$','%','&','*']
    #List for special characters

    numbers = ['0','1','2','3','4','5','6','7','8','9']
    #List for numbers 0-9

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #List for lowercase letters a-z.

    cap_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    #List for capital letters A-Z.

    list2 = special + numbers + letters + cap_letters 
    # Combining lists together so that the computer can easily pool all the items from every list into one list.

    '''Looping through every element from 1 to the length user picks. Length is simply just a number.
    This can be thought of for e.g, like for x in range(5) which would print (,1,2,3,4,5)'''
    password = ''.join(random.choice(list2) for x in range(length))
    return password
        #For each number in the list we go through the combined list and pick a random item from it and print it.
        #Therefore, we are able to generate a random password which looks crazy, and is hard to guess. 


def GUI(): #GUI function
    def showscreen2(): #function which hides screen 2 until some condition is met in screen 1.
        '''the pack() method on the next line just organises the widgets in horizontal and vertical boxes that are limited to left, right, top, bottom positions. 
        Essientially it's used for positioning. The forget() makes tkinter forgets where the widget was. This piece of code is just used to hide screen 1 when the button is clicked'''
        screen1.pack_forget() 
        screen2.pack(fill="both",expand=True) #This is what actually displays the second screen once the button is clicked on screen 1.
        enter_characters.focus_set() #.focus_set() method just focuses on that specific widget, this only happens if and only if the master window is focused.

    def showscreen3(event=None): #same as before, function hides screen until some condition happens. (In this case until user enters the amount of characters.)
        global user_input #setting user_input as a global variable so it can be used anywhere within this project.
        user_input = input_var.get().strip() #get() Returns the entry’s current text as a string. strip() removes any leading, and trailing whitespaces.

        if user_input.isdigit(): #Checks if user_input is a digit.
            user_input = int(user_input) #If the user_input is a digit, then it converts the user_input into an integer.
            generated_password = programfunc(user_input) #Set generated_password variable to the random generated password.
            label_password.config(text=f"Generated Password:\n {generated_password}") #This line displays the random generated password to the user. The .config() allows attributes to be modified within widget.
            screen2.pack_forget() #Hides, the second screen.
            screen3.pack(fill="both",expand=True) #This is what actually displays the third screen once the number of characters is entered on screen 2.

        else:
            messagebox.showerror("Invalid Input","Please enter a valid integer.") #If the user does not enter an integer, then an error will be displayed in a textbook format. 

        
    #SCREEN 1 (MAIN MENU)
    random_pass = tk.Tk() #Used to boot up the main window.
    random_pass.title("Random Password Generator") #Sets the title of the window
    random_pass.geometry("700x700") #Dimensions of window
    random_pass.configure(bg='black') #Sets background colour of black.
    random_pass.resizable(False,False) #Doesn't allow for the window to be resized.

    screen1 = tk.Frame(random_pass, width = 700, height = 700, bg = "black") #Sets the dimensions of screen1, Frame method important for the process of grouping and organizing other widgets. Notice, this is linked to main window.
    screen1.pack(fill="both", expand=True) #This is what actually displays screen 1.

    startbutton = tk.Button(screen1, text="START", bg= "#FF99FF", fg= "Black", font=("Helvetica",50), command=showscreen2) #Displays a start button on screen 1. Command means, what'll happen when the button is hit, in this case it'll show screen 2.
    startbutton.pack(side="bottom",pady=150) #Used for the positioning of the button 

    canvas1 = tk.Canvas(screen1, width=700, height=700, bg="black", highlightthickness=0) #Creates a canvas for the first screen.
    canvas1.pack()
    canvas1.create_text(25, 100, text="RANDOM PASSWORD GENERATOR", fill="yellow", anchor="nw",font=("Helvetica", 28)) #Creates text.
    canvas1.create_text(80,200,text="CHOOSE AMOUNT OF CHARACTERS \nTO RECEIVE A STRONG PASSWORD!", fill="light blue", anchor="nw", font=("Helvetica",22)) #Creates text.

    #SCREEN 2 (SECOND PAGE)
    screen2 = tk.Frame(random_pass,width = 700, height = 700, bg = "black") #Sets dimensions of screen 2.
    screen2.pack_propagate(False) # Prevents the frame from resizing to fit its children
    input_var = tk.StringVar() #used to edit a widget's text.

  # Prompt text label at the top
    label_prompt = tk.Label(screen2, text="INPUT NO. OF CHARACTERS:", bg="black", fg="white", font=("Helvetica", 28))
    label_prompt.pack(pady=(100, 20))  # Top padding to push the label down from the top

    enter_characters = tk.Entry(screen2, textvariable=input_var,bg= "grey", fg= "Black", font=("Helvetica",25), cursor="circle") #User enters the amount of characters within the input box.
    enter_characters.pack(pady=(0, 20)) #Used for positioning.

    submit_button = tk.Button(screen2, text="Submit", command=showscreen3) #Submit button, once clicked shows screen 3.  
    submit_button.pack() #Positioning of submit button.


    #SCREEN 3 (THIRD PAGE)
    screen3 = tk.Frame(random_pass, width= 700, height = 700, bg = "black") #Create third screen.
    label_password = tk.Label(screen3, text="", font=("Helvetica", 28), bg="black", fg="yellow") #Used for styling/positioning of text on screen 3.
    label_password.pack(pady=100) #Positioning of text.
    


    random_pass.mainloop() #Execution of Python commands halts there.


GUI()
