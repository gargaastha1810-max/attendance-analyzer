import tkinter as tk
def calculate():
    try:
        t = int(total.get())
        a = int(attended.get())
        target = int(target_entry.get())
        attendance = (a/t)*100
        x = 0
        while ((a+x)/(t+x))*100 < target:
            x += 1
        bunk = 0
        while ((a)/(t+bunk+1))*100 >= target:
            bunk += 1
        result.config(
            text=f"Current Attendance: {attendance:.2f}%\n"
                 f"Attend next {x} lectures to reach {target}%\n"
                 f"You can bunk {bunk} lectures safely",
            fg="green"
        )
    except:
        result.config(text="Please enter valid numbers!", fg="red")
root = tk.Tk()
root.title("Attendance Analyzer")
root.geometry("400x350")
root.configure(bg="#fde3e3")
tk.Label(root,text="Attendance Analyzer",font=("Arial",18,"bold"),bg="#e3f2fd",fg="#0d47a1").pack(pady=15)
tk.Label(root,text="Total Lectures Conducted",bg="#e3f2fd").pack()
total = tk.Entry(root)
total.pack()
tk.Label(root,text="Lectures Attended",bg="#e3f2fd").pack()
attended = tk.Entry(root)
attended.pack()
tk.Label(root,text="Target Attendance %",bg="#e3f2fd").pack()
target_entry = tk.Entry(root)
target_entry.pack()
tk.Button(root,text="Analyze Attendance",bg="#1976d2",fg="white",command=calculate).pack(pady=15)
result = tk.Label(root,text="",bg="#e3f2fd",font=("Arial",11))
result.pack()
root.mainloop()