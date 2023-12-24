
from tkinter import *


# UT
FONTH =("Verdana",20 ,"normal")
FONTL =("Verdana",15 ,"normal")
window = Tk() #Tk() yazmadan import * almıyor ?
window.title("SecNot ASC_100 Ver.")
window.config(padx=30, pady=30)

#UI
photo = PhotoImage(file="img.png")
photo_label = Label (image=photo)
photo_label.pack()

# canvas= Canvas (height=170,width=180)
# canvas.create_image(90,95, image=photo)
# canvas.pack()


title_info_label = Label(text="Enter your Title", font=FONTH)
title_info_label.pack()

title_entry= Entry (width=30)
title_entry.pack()


input_info_label = Label(text="Enter your Note wish SecNot Hide",font=FONTL)
input_info_label.pack()

input_text = Text(width=45, height=22)
input_text.pack()

master_secret_label = Label(text="Enter your key master", font=FONTL)
master_secret_label.pack()

master_secret_input = Entry (width=30)
master_secret_input.pack()

save_button = Button(text="Save and Hide in shadow ")
save_button.pack()

decrypt_button =Button(text="Show me hiden")
decrypt_button.pack()



window.mainloop()