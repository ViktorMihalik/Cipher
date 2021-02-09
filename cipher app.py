# Importing
import random
from tkinter import *

#Tkinter configuration
root = Tk()
root.title("Cipheringo")
root.configure(background ='#0D0D0F')
root.geometry("780x900")


###Defining functions
scrypt = None

#Encrypting the character based on password and key
def password_key ():
    password = str(password_panel_right.get())
    key = int(key_panel_right.get())
    new_password = []
    for i in password:
        
        numbers = "1","2","3","4","5","6","7","8","9"
        char1 ='a', 'b', 'c', 'd', 'e', 'f', 'g' 
        char2 = 'h', 'i', 'j', 'k', 'l', 'm', 'n'
        char3 = 'o', 'p', 'q', 'r', 's', 't' 
        char4 = 'u', 'v', 'w', 'x', 'y', 'z'
        characters = char1, char2, char3, char4, numbers

        if i  in numbers:
            i = 3 ** key
            new_password.extend([i])

        if i  in char1:
            i = 2 ** key
            new_password.extend([i])

        if i  in char2:
            i = 5 ** key
            new_password.extend([i])   

        if i  in char3:
            i = 4 ** key
            new_password.extend([i]) 

        if i  in char4:
            i = 7 ** key
            new_password.extend([i]) 

        if i != characters:
            i = 6 ** key
            new_password.extend([i])
    
    return(sum(new_password))

# random number generator  to create random characters in text
def inputing ():

    # Range of character is from 32 to 126:
    a = 1
    b = random.randrange(1,2)
    c = random.randrange(0,6)
    d = random.randrange(3,9)
    e = random.randrange(2,9)
    three_numbers = f"{a}{b}{c}"
    two_numbers = f"{d}{e}"
    choosing_from = three_numbers,two_numbers
    result = random.choice(choosing_from)

    return result

#Encrypt function    
def encrypt():
    
    data = main_panel.get()
    cipher = ""
    for char in str(data):
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -= 32
            char_ord += password_key()
            char_ord = char_ord % 94
            char_ord += 32
            cipher += str(char_ord) + " " + str(inputing()) + " "

        else:
            cipher += str(char_ord) + " " + str(inputing()) + " "
    
    encryption.insert(END, cipher + '\n'+ '\n')
    main_panel.delete(0,END)

#Decrypt function
def decrypt ():
    
    data = main_panel.get()
    decipher = ""
    data = data.split()
    data = data[::2]
    
    for number in data:
        number= int(number)
        if 32 <= number <= 126:
            number-= 32
            number -= password_key()
            number = number % 94
            number += 32
            letter= chr(number)
            decipher += letter
        else:
            decipher += chr(number)

    decryption.insert(END, decipher + '\n'+ '\n')
    main_panel.delete(0,END)

###user interface
#Password panel
password_panel_right = Entry(root, fg = "White", bg = "#0D0D0F",  insertbackground= "white", 
                             width = 60, relief = "flat", show="*")
password_panel_right.grid(row = 0,  column = 2, columnspan = 2)

password_panel_left = Label(root, fg = "White", bg = "#0D0D0F", text = "Enter Password:", relief = "flat")
password_panel_left.grid(row = 0, column = 0, columnspan = 2, ipadx = 0, sticky = E)

#Key panel
key_panel_right = Entry(root, fg = "White", bg = "#0D0D0F", insertbackground= "white", width = 60, relief = "flat")
key_panel_right.grid(row = 1,  column = 2, columnspan = 2, pady = 4)

key_panel_left = Label(root, fg = "White", bg = "#0D0D0F", text = "Enter Key (number):" , relief = "flat")
key_panel_left.grid(row = 1, column = 0, columnspan = 2, ipadx = 0, sticky = E)

#Main Panel
main_panel = Entry(root, fg = "White", bg = "#144072", width = 122, relief = "flat")
main_panel.grid(row = 2,  column = 0, columnspan = 4, padx = 15, ipady = 21)

#Encryption button
button_encrypt = Button(root, fg = "White", bg = "#556577", text = "Encrypt", height = 1, 
                        width = 45, command = encrypt, relief = "flat")
button_encrypt.grid(row = 3, column = 0, columnspan = 2, pady = 2, padx = 20, sticky = E)

#decryption button
button_decrypt = Button(root, fg = "White", bg = "#556577", text = "Decrypt", height = 1, 
                        width = 45, command = decrypt, relief = "flat")
button_decrypt.grid(row = 3, column = 2,columnspan = 2,pady = 2, sticky = W)

#Scrollbars
scrollbar_encrypt = Scrollbar(root)
scrollbar_encrypt.grid(row = 4, column = 1, ipady = 350,  sticky = E)

scrollbar_decrypt = Scrollbar(root)
scrollbar_decrypt.grid(row = 4, column = 3, ipady = 350,  sticky = W)

#Encryption console
encryption = Text(root, bg = "#0D0D0F", fg = "white", font = "Verdana, 8", bd = 0, 
                  width = 58, height = 30, wrap = WORD, yscrollcommand = scrollbar_encrypt.set)
encryption.config(height= 3)
encryption.grid( row = 4,column = 0, sticky = E, ipady = 350, padx =20)
scrollbar_encrypt.config( command = encryption.yview )

#Decryption console
decryption = Text(root, bg = "#0D0D0F", fg = "white", font = "Verdana, 8", bd = 0, 
                width = 54, height = 30, wrap = WORD, yscrollcommand = scrollbar_decrypt.set)

decryption.config(height= 3)
decryption.grid(row = 4, column = 2, sticky = E, ipady = 350)
scrollbar_decrypt.config(command = decryption.yview )



root.mainloop()


