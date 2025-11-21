import asyncio # Importing the asyncio library for asynchronous programming
from tkinter import * # Importing the tkinter library for GUI applications
from tkinter import ttk #to style tkinter widgets
from googletrans import Translator,LANGUAGES # Importing the Translator class from googletrans for language translation
root=Tk()# Creating the main application window
root.geometry("1100x320") # Setting the dimensions of the window
root.resizable(0,0) # Disabling window resizing
#root.iconbitmap("translate.ico") # Setting the window icon
root ['bg']='violet'# Setting the background color of the window
root.title("Language Translator") # Setting the title of the window
Label(root,text="LANGUAGE TRANSLATOR",font=("Arial",25,"bold"),bg="violet",fg="black").pack() # Adding a title label to the window
Label(root,text="Enter Text",font=("Arial",15,"bold"),bg="white",fg="black").place(x=165,y=90) # Adding a label for input text
Input_text=Entry(root,font=("Arial",15),bd=5,width=40) # Creating an entry widget for user input
Input_text.place(x=30,y=130) # Placing the input text entry widget in the window
Input_text.get()# Getting the text entered by the user
Label(root,text="Translated Text",font=("Arial",15,"bold"),bg="white",fg="black").place(x=788,y=90) # Adding a label for translated text
Output_text=Text(root,font='arial 10',height=5,wrap=WORD,padx=5,pady=5,width=50)# Creating a text widget to display translated text
Output_text.place(x=600,y=130) # Placing the output text widget in the window
language=list(LANGUAGES.values()) # Getting a list of available languages from googletrans
dest_lang=ttk.Combobox(root,values=language,width=22) # Creating a combobox for selecting the destination language
dest_lang.place(x=130,y=180) # Placing the destination language combobox in the window
dest_lang.set("select language") # Setting the default value of the destination language combobox
lang_code = {v: k for k, v in LANGUAGES.items()} # This creates a new dictionary called lang_code that maps language names (like "hindi") to their codes (like "hi"). It reverses the keys and values of the LANGUAGES dictionary since Google Translate needs language codes to translate

def translate_text(): # Defining the function to perform translation
    translator = Translator() # Creates an instance of the Translator class, which provides the method to convert text from one language to another
    dest_language_code = lang_code.get(dest_lang.get(), 'en') # Gets the language name selected by the user in the GUI (dest_lang.get()), finds its language code using the lang_code dictionary. If nothing is selected or the language isn't found, it defaults to 'en' (English).
    async def translate_async(): # Defining an asynchronous function for translation
        return await translator.translate(text=Input_text.get(), dest=dest_language_code) # Performing the translation asynchronously

    translated = asyncio.run(translate_async()) # Running the asynchronous translation function
    Output_text.delete(1.0, END) # Clearing any existing text in the output text widget
    Output_text.insert(END, translated.text) # Inserting the translated text into the output text widget

translate_btn=Button(root,text="Translate",font=("Arial",15,"bold"),bd=5,bg="lightblue",fg="black",command=translate_text) # Creating a button to trigger the translation
translate_btn.place(x=450,y=250) # Placing the translate button in the window
root.mainloop() # Starting the Tkinter event loop to run the application
