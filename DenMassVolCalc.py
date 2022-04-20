from masscalc import *
from denscalc import *
from volcalc import *


root = tk.Tk()
root.title("Sűrűség, Térfogat, Tömeg Kalkulátor")
root.geometry("270x170")
root.resizable(False, False)


var_choice = tk.IntVar()
density_choice = tk.Button(
    root,
    text="Sűrűség Számolás",
    command=density_calculator,
    font=("Helvetica", 20),
    fg="Blue"
)
volume_choice = tk.Button(
    root,
    text="Térfogat Számolás",
    command=volume_calculator,
    font=("Helvetica", 20),
    fg="Blue"
)
mass_choice = tk.Button(
    root,
    text="Tömeg Számolás",
    command=mass_calculator,
    font=("Helvetica", 20),
    fg="Blue"
)
density_choice.pack(side=tk.TOP, fill=tk.X)
volume_choice.pack(side=tk.TOP, fill=tk.X)
mass_choice.pack(side=tk.TOP, fill=tk.X)

root.mainloop()
