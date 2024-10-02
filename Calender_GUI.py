# Importing tkinter module
from tkinter import *
# Importing calendar module
import calendar

# Function to show calendar of the given year
def showCalendar():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calendar for the Year")
    gui.geometry("550x600")
    
    # Getting the year from the input field
    year = int(year_field.get())
    
    # Getting the calendar content
    gui_content = calendar.calendar(year)
    
    # Creating a Text widget to display the calendar
    text_area = Text(gui, font="Consolas 10 bold")
    
    # Inserting the calendar content into the Text widget
    text_area.insert(END, gui_content)
    
    # Disabling the Text widget to make it read-only
    text_area.config(state=DISABLED)
    
    # Packing the Text widget to display the content
    text_area.pack(expand=True, fill=BOTH)
    
    # Starting the GUI main loop
    gui.mainloop()

# Main GUI setup
root = Tk()
root.config(background='grey')
root.title("Calendar Generator")
root.geometry("250x150")

# Label for entering the year
cal = Label(root, text="Enter Year", bg='dark grey')
year_field = Entry(root)

# Button to show the calendar
button = Button(root, text='Show Calendar', command=showCalendar)

# Positioning the widgets
cal.grid(row=1, column=1)
year_field.grid(row=2, column=1)
button.grid(row=3, column=1)

# Running the main loop
root.mainloop()
