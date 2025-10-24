import pywhatkit
import tkinter as tk
root = tk.Tk()
root.title("WhatsApp Massege")
root.geometry("600x600")
def massege():
    pywhatkit.sendwhatmsg(str(number.get()),str(text.get()),int(hr.get()),int(miniute.get()))
lab1 =tk.Label(root,text="Enter Your Number",font=("Arial",15))
lab1.pack(pady=10)
number = tk.Entry(root);
number.pack(pady=10)
lab2 =tk.Label(root,text="Enter your massage",font=("Arial",15))
lab2.pack(pady=10)
text = tk.Text(root,height=10,width=30)
text.pack(pady=10)
lab3 =tk.Label(root,text=("Enter sending time"),font=("Arial",15))
lab3.pack(pady=10)
hr = tk.Entry(root)
hr.pack(pady=10)
miniute = tk.Entry(root)
miniute.pack(pady=10)
submit = tk.Button(root,text=("Submit"),command=massege)
submit.pack(pady=10)
root.mainloop()