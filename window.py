# textBox = tk.Text(Tk, height = 5, width = 52)
# textBox.pack()
import cryptocode
import tkinter as tk
import tkinter.font as tkFont
Tk = tk.Tk()

#setting title
Tk.title("Crypty")
#setting window size
width=618
height=350
screenwidth = Tk.winfo_screenwidth()
screenheight = Tk.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
Tk.geometry(alignstr)
Tk.resizable(width=False, height=False)

GLabel_187=tk.Label(Tk)
ft = tkFont.Font(family='Times',size=10)
GLabel_187["font"] = ft
GLabel_187["fg"] = "#333333"
GLabel_187["justify"] = "center"
GLabel_187["text"] = "Password"
GLabel_187.place(x=0,y=170,width=309,height=30)

encrypt_password=tk.Text(Tk)
ft = tkFont.Font(family='Times',size=10)
encrypt_password["font"] = ft
encrypt_password["fg"] = "#333333"
# encrypt_password["justify"] = "center"
# encrypt_password["text"] = "Password"
encrypt_password.place(x=0,y=200,width=309,height=30)

GLabel_983=tk.Label(Tk)
ft = tkFont.Font(family='Times',size=10)
GLabel_983["font"] = ft
GLabel_983["fg"] = "#333333"
GLabel_983["justify"] = "center"
GLabel_983["text"] = "Password"
GLabel_983.place(x=309,y=170,width=309,height=30)

decrypt_password=tk.Text(Tk)
ft = tkFont.Font(family='Times',size=10)
decrypt_password["font"] = ft
decrypt_password["fg"] = "#333333"
# encrypt_password["justify"] = "center"
# encrypt_password["text"] = "Password"
decrypt_password.place(x=309,y=200,width=309,height=30)

GLabel_40=tk.Label(Tk)
ft = tkFont.Font(family='Times',size=10)
GLabel_40["font"] = ft
GLabel_40["fg"] = "#333333"
GLabel_40["justify"] = "center"
GLabel_40["text"] = "Text"
GLabel_40.place(x=0,y=70,width=309,height=25)

text_to_encrypt=tk.Text(Tk)
ft = tkFont.Font(family='Times',size=10)
text_to_encrypt["font"] = ft
text_to_encrypt["fg"] = "#333333"
# GLabel_40["justify"] = "center"
# GLabel_40["text"] = "Text"
text_to_encrypt.place(x=0,y=100,width=309,height=25)

GLabel_889=tk.Label(Tk)
ft = tkFont.Font(family='Times',size=10)
GLabel_889["font"] = ft
GLabel_889["fg"] = "#333333"
GLabel_889["justify"] = "center"
GLabel_889["text"] = "Encrypted Text"
GLabel_889.place(x=310,y=70,width=309,height=25)

text_to_decrypt=tk.Text(Tk)
ft = tkFont.Font(family='Times',size=10)
text_to_decrypt["font"] = ft
text_to_decrypt["fg"] = "#333333"
# GLabel_40["justify"] = "center"
# GLabel_40["text"] = "Text"
text_to_decrypt.place(x=309,y=100,width=309,height=25)

def decrypt_passwor():
    password = decrypt_password.get("1.0",'end-1c')
    print(password)
    text  = text_to_decrypt.get("1.0",'end-1c')
    print(text)
    decoded = cryptocode.decrypt(text, password)
    print(decoded)
    decrypted_output.insert(tk.END, decoded)


def encrypt_passwor():
    password = encrypt_password.get("1.0",'end-1c')
    print(password)
    text  = text_to_encrypt.get("1.0",'end-1c')
    print(text)
    encoded = cryptocode.encrypt(text, password)
    print(encoded)
    encrypted_output.insert(tk.END, encoded)


GLabel_908=tk.Label(Tk)
ft = tkFont.Font(family='Times',size=30)
GLabel_908["font"] = ft
GLabel_908["fg"] = "#333333"
GLabel_908["justify"] = "center"
GLabel_908["text"] = "Encrypt"
GLabel_908.place(x=0,y=10,width=309,height=36)

GLabel_847=tk.Label(Tk)
ft = tkFont.Font(family='Times',size=30)
GLabel_847["font"] = ft
GLabel_847["fg"] = "#333333"
GLabel_847["justify"] = "center"
GLabel_847["text"] = "Decrypt"
GLabel_847.place(x=310,y=10,width=309,height=36)

encrypt_button=tk.Button(Tk)
encrypt_button["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
encrypt_button["font"] = ft
encrypt_button["fg"] = "#000000"
encrypt_button["justify"] = "center"
encrypt_button["text"] = "Encrypt"
encrypt_button.place(x=120,y=300,width=70,height=25)
encrypt_button["command"] = encrypt_passwor

decrypt_button=tk.Button(Tk)
decrypt_button["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
decrypt_button["font"] = ft
decrypt_button["fg"] = "#000000"
decrypt_button["justify"] = "center"
decrypt_button["text"] = "Decrypt"
decrypt_button.place(x=430,y=300,width=70,height=25)
decrypt_button["command"] = decrypt_passwor

encrypted_output=tk.Text(Tk)
ft = tkFont.Font(family='Times',size=10)
encrypted_output["font"] = ft
encrypted_output["fg"] = "#333333"
# encrypted_output["justify"] = "center"
# encrypted_output["text"] = "output"
encrypted_output.insert(tk.END, "output")
encrypted_output.place(x=0,y=270,width=309,height=30)

decrypted_output=tk.Text(Tk)
ft = tkFont.Font(family='Times',size=10)
decrypted_output["font"] = ft
decrypted_output["fg"] = "#333333"
# decrypted_output["justify"] = "center"
# decrypted_output["insert"] = "output"
decrypted_output.insert(tk.END, "output")
decrypted_output.place(x=310,y=270,width=309,height=30)

Tk.mainloop()

