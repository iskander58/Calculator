import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result.set(eval(entry_var.get()))
        except Exception:
            result.set("Ошибка")
    elif text == "C":
        result.set("")
    else:
        result.set(entry_var.get() + text)

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

entry_var = tk.StringVar()
result = tk.StringVar()

entry = tk.Entry(root, textvar=entry_var, font="Arial 20", bd=10, relief=tk.SUNKEN, justify="right")
entry.pack(fill="both", ipadx=8, ipady=8, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(fill="both", expand=True)
    for btn in row:
        button = tk.Button(row_frame, text=btn, font="Arial 20", padx=20, pady=20)
        button.pack(side="left", expand=True, fill="both")
        button.bind("<Button-1>", on_click)

root.mainloop()
