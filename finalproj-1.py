import tkinter as tk
from tkinter import messagebox

# Create the main window
window1 = tk.Tk()
window1.title("Cooking Measurement Converter")
window1.geometry("600x400")
window1.configure(bg="#FDB4A6")

# Create the 2nd window for calculators

def openWindow2():
    
    """""
        Functions to convert certain measurements
    """""

    ### Functions for Cups to ounces OR ounces to cups
    def CupTOounces():
        # Get the cups from the user
        cup = float(entry.get())
        
        # Convert cups to ounces
        ounces = cup * 8
        result.config(text=str(round(ounces)) + " Ounce(s)")

    def OuncesTOcups():
        # Get the ounces from the user
        ounces = float(entry.get())

        #convert ounces to cups
        cups = ounces / 8
        result.config(text=str(round(cups)) + " Cup(s)")

    ### Functions for tablespoon to grams OR grams to tablespoons
    def TableTOgrams():
        # Get the tablespoon from user
        tablespoon = float(entry.get())

        # Convert tablespoon to grams
        grams = tablespoon * 15
        result.config(text=str(round(grams, 2)) + " Gram(s)")

    def GramsTOtable():
        # Get the grams from user
        grams = float(entry.get())
        
        # Convert grams to tablespoons
        tablespoon = grams / 15
        result.config(text=str(round(tablespoon, 2)) + " Tablespoon(s)")
        
     ### Functions for Cups to milliliters OR milliliters to Cups
    def CupTOml():
        # Get the cups from user
        Cup = float(entry.get())
        
        # Convert cups to milliliters
        milliliters = Cup * 236.6
        result.config(text=str(round(milliliters, 2)) + " milliliter(s)")

    def MlTOcups():
        # Get the milliliters from user
        milliliters = float(entry.get())

        # Convert milliliters to cups
        cups = milliliters / 236.6
        result.config(text=str(round(cups, 2)) + "Cup(s)")

      ### Functions for Teaspoons to Grams OR Teaspoons to Grams
    def TeaTOgrams():
        # Get the teaspoons from user
        teaspoon = float(entry.get())

        # Convert teaspoons to grams
        grams = teaspoon * 4.2
        result.config(text=str(round(grams, 2)) + "gram(s)")

    def GramsTOtea():
        # Get the grams from user
        grams = float(entry.get())

        # Convert grams to teaspoons
        teaspoon = grams / 4.2
        result.config(text=str(round(teaspoon, 2)) + "teaspoon(s)")

    """""
        Functions to convert certain measurements (END)
    """""
    """""
        Down below is the actual work for the 2nd window.
    """""

    window2 = tk.Toplevel(window1)

    # Setting window geometrics, and info
    window2.title("Calculator Menu")
    window2.geometry("600x1000")
    window2.configure(bg="#FDB4A6")

    tk.Label(window2, text = "Enter a value,\n then click on one of the conversions you'd like!",
            fg = "white",
            bg = "#FDB4A6",
            width = "50",
            font = ("Impact", 15)
).pack()

    tk.Label(window2, text ="Entire your desired amount")

    # Entry for the desired number of user
    # Deletes the input to refresh the calculator
    def clearText1():
        entry.delete(0, 'end')

    entry = tk.Entry(window2,
                    fg = "white",
                    bg = "#FDB4A6",
                    width = "30",
                    font = ("Impact", 15) 
    )
    entry.pack()
        
    clearbutton1 = tk.Button(window2, text = "Clear",
                    command = clearText1,
                    fg = "white",
                    bg = "#FF7D75",
                    width = "20",
                    font = ("Impact", 10) 
    )
    clearbutton1.pack(pady = 10)

    # Output:
    # Deletes the output to refresh the calculator
    def removeText():
        result.config(text="")

    result = tk.Label(window2,
                    fg = "white",
                    bg = "#FDB4A6",
                    width = "30",
                    font = ("Impact", 15), 
    text = "")
    result.pack()

    clearbutton2 = tk.Button(window2, text = "Clear",
                    command = removeText,
                    fg = "white",
                    bg = "#FF7D75",
                    width = "20",
                    font = ("Impact", 10) 
    )
    clearbutton2.pack(pady = 10)

    # Creating a way to guide the user to which conversion they would like to use
    # Button for Cups to Ounces
    button1 = tk.Button(window2, text = "Cups to Ounces",
            command = CupTOounces,           
            fg = "white",
            bg = "#FF7D75",
            height = "2",
            width = "20",
            font = ("Impact", 15)   
        )
    button1.pack(pady = 10)

    # Button for Ounces to Cups   
    button2 = tk.Button(window2, text = "Ounces to Cups",
            command = OuncesTOcups,           
            fg = "white",
            bg = "#FF7D75",
            height = "2",
            width = "20",
            font = ("Impact", 15)   
        )
    button2.pack(pady = 10)
    
    # Button for Cups to Milliliters
    button3 = tk.Button(window2, text = "Cups to milliliters",
            command = CupTOml,           
            fg = "white",
            bg = "#FF7D75",
            height = "2",
            width = "20",
            font = ("Impact", 15)   
        )
    button3.pack(pady = 10)

    # Button for Milliliters to Cups
    button4 = tk.Button(window2, text = "Milliliters to Cups",
            command = MlTOcups,           
            fg = "white",
            bg = "#FF7D75",
            height = "2",
            width = "20",
            font = ("Impact", 15)   
        )
    button4.pack(pady = 10)

    # Button for Tablespoon to Grams
    button5 = tk.Button(window2, text = "Tablespoons to Grams",
            command = TableTOgrams,           
            fg = "white",
            bg = "#FF7D75",
            height = "2",
            width = "20",
            font = ("Impact", 15)   
        )
    button5.pack(pady = 10)

    # Button for Grams to Tablespoons
    button6 = tk.Button(window2, text = "Grams to Tablespoons",
            command = GramsTOtable,           
            fg = "white",
            bg = "#FF7D75",
            height = "2",
            width = "20",
            font = ("Impact", 15)   
        )
    button6.pack(pady = 10)

    # Button for Teaspoons to Grams
    button7 = tk.Button(window2, text = "Teaspoons to Grams",
            command = TeaTOgrams,           
            fg = "white",
            bg = "#FF7D75",
            height = "2",
            width = "20",
            font = ("Impact", 15)   
        )
    button7.pack(pady = 10)

    # Button for Grams to Teaspoons
    button8 = tk.Button(window2, text = "Grams to Teaspoons",
            command = GramsTOtea,           
            fg = "white",
            bg = "#FF7D75",
            height = "2",
            width = "20",
            font = ("Impact", 15)   
        )
    button8.pack(pady = 10)

    # Button created to exit the 1st window, or the calculator service
    quit2 = tk.Button(window2, text="Quit",
            command = window2.destroy,           
            fg = "white",
            bg = "#FF7D75",
            width = "20",
            font = ("Impact", 15)                   
    )
    quit2.pack(pady = 10)

"""""
    This part of the program below will be any necessary coding done
    for the main window, which will display 1 button, as well as what the program
    actually does for the user that decides to use it.
"""""
    

# Creating a introduction/greeting
greeting1 = tk.Label(window1, text = "Hello!\nWelcome to the measurement converter!",
    fg = "white",
    bg = "#FDB4A6",
    width = "50",
    font = ("Impact", 20),
    borderwidth = 4,
    relief = "ridge",
)
greeting1.pack(fill=tk.BOTH, side=tk.TOP, expand=True, pady = 10, padx = 10)

# Creating a label widget to explain what this program does

introduction = tk.Label(window1, text = "This program is created to simplify anyones life when it comes\n to converting measurements to other measurements while cooking, \nThis program will convert it to its most accurate conversion.",
    fg = "white",
    bg = "#FDB4A6",
    width = "50",
    font = ("Impact", 15)
)
introduction.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# Creating a second label widget to guide the user to the actual calculator portion

calculator = tk.Label(window1, text = "Click down below to calculate your measurements!",
    fg = "white",
    bg = "#FDB4A6",
    width = "50",
    font = ("Impact", 13)
)
calculator.pack(fill=tk.BOTH, side=tk.TOP, expand=True, pady = 10)

calcButton = tk.Button(window1, text = "Calculators!",
                       command = openWindow2,
                       fg = "white",
                       bg = "#FF7D75",
                       width = "20",
                       font = ("Impact", 20)
    )
calcButton.pack(pady = 30)

# Button created to exit the 1st window
quit1 = tk.Button(window1, text="Quit",
            command = window1.quit,           
            fg = "white",
            bg = "#FF7D75",
            width = "20",
            font = ("Impact", 15)                   
)
quit1.pack(pady = 10)

# Run the main loop
window1.mainloop()