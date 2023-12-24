
from tkinter import *
from tkinter import messagebox
import base64

def encode(key,clear):
    enc=[]
    for i in range(len(clear)):
        key_c =key[i % len(key)]
        enc_c =chr((ord(clear[i])+ord(key_c)) %256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
def decode(key,enc):
    dec =[]
    enc= base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c =key[i % len (key)]
        dec_c = chr((256+ord(enc[i])-ord(key_c))%256)
        dec.append(dec_c)
    return "".join(dec)


def save_and_encrypt_notes():
    title= title_entry.get()
    message= input_text.get("1.0",END)
    master_secret = master_secret_input.get()
    if len(title) == 0 or len (message) == 0 or len(master_secret) == 0 :
        messagebox.showwarning(title="Error!!!", message="Please give me all key of Secret.")
    else:
        #encryption
        message_encrypted =encode(master_secret, message)
        try:
            with open ("HidenForest.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("HidenForest.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        finally:
            title_entry.delete(0,END)
            master_secret_input.delete(0,END)
            input_text.delete("1.0",END)






#UI
FONTH =("Verdana",20 ,"normal")
FONTL =("Verdana",15 ,"normal")
window = Tk() #Tk() yazmadan import * almıyor ?
window.title("SecNot ASC_100 Ver.")
window.config(padx=30, pady=30)
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

save_button = Button(text="Save and Hide in shadow ",command=save_and_encrypt_notes)
save_button.pack()

decrypt_button =Button(text="Show me hiden")
decrypt_button.pack()



window.mainloop()