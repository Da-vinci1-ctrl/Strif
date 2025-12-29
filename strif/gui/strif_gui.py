import tkinter as tk
from tkinter import filedialog
import subprocess

def run_strif():
    file = filedialog.askopenfilename(filetypes=[("Strif Files", "*.strf")])
    if file:
        output.delete("1.0", tk.END)
        result = subprocess.run(
            ["python3", "../engine/strif_engine_v02.py", file],
            capture_output=True, text=True
        )
        output.insert(tk.END, result.stdout)

app = tk.Tk()
app.title("STRIF Runtime")

tk.Button(app, text="Run STRIF", command=run_strif).pack()
output = tk.Text(app, height=25, width=80)
output.pack()

app.mainloop()
