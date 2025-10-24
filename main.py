import pywhatkit
import tkinter as tk

root = tk.Tk()
root.title("WhatsApp Message")
root.geometry("600x600")

def massege():
    try:
        pywhatkit.sendwhatmsg(
            str(number.get()),
            str(text.get("1.0", "end-1c")),
            int(hr.get()),
            int(minute.get())
        )
        lab4.config(text="Message has been sent successfully", font=("Arial", 12, "bold"), fg="green")
    except Exception as e:
        lab4.config(text=f"Error: {e}", font=("Arial", 12, "bold"), fg="red")

# --- Number section ---
lab1 = tk.Label(root, text="Enter Your Number", font=("Arial", 15))
lab1.pack(pady=10)

number = tk.Entry(root)
number.pack(pady=10)

# --- Message section ---
lab2 = tk.Label(root, text="Enter your message", font=("Arial", 15))
lab2.pack(pady=10)

text = tk.Text(root, height=10, width=30)
text.pack(pady=10)

# --- Time section ---
lab3 = tk.Label(root, text="Enter sending time", font=("Arial", 15))
lab3.pack(pady=10)

time_frame = tk.Frame(root)   
time_frame.pack(pady=5)

hr = tk.Entry(time_frame, width=5)
hr.pack(side=tk.LEFT, padx=5)
tk.Label(time_frame, text="Hour").pack(side=tk.LEFT, padx=5)

minute = tk.Entry(time_frame, width=5)
minute.pack(side=tk.LEFT, padx=5)
tk.Label(time_frame, text="Minute").pack(side=tk.LEFT, padx=5)

# --- Submit section ---
lab4 = tk.Label(root, text="Click the Submit button to send the message.")
lab4.pack(pady=10)

submit = tk.Button(root, text="Submit", command=massege)
submit.pack(pady=10)

root.mainloop()
