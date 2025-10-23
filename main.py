import pywhatkit
import tkinter as tk
root = tk.Tk()
root.title("WhatsApp Massege")
root.geometry("600x600")
def massege():
    pywhatkit.sendwhatmsg(str(number.get()),"Hi",12,4)
lab1 =tk.Label(root,text="Enter Your Number",font=("Arial",15))
lab1.pack(pady=10)
number = tk.Entry(root);
number.pack(pady=10)
submit = tk.Button(root,text=("Submit"))
submit.pack(pady=10)
root.mainloop()