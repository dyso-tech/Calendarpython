from tkinter import *

#window
root = Tk() # create a GUI interface
root.geometry("450x250") # width X height
root.title('Account Login')

#headerlabel
Label(text="Log in of registreer een nieuw account", bg="blue", width="300",height="2", font=("Calibri",13)).pack()
Label(text="").pack
                                                                                              

#button login
Button(text="Log in",height="2",width="30").pack()


#button register
Button(text="Registreer uw account",height="2",width="30").pack()


root.mainloop()
