import tkinter as tk
from tkinter import ttk

MASS = ("g", "kg", "t")
VOLUME = ("cm^3", "m^3")
DENSITY = ("g/cm^3", "kg/m^3", "t/m^3")

def density_calculator():

    def density():
        vol = float(volume_entry.get())
        mas = float(mass_entry.get())
        dens = round(mas / vol, 3)
        calculated_density = ttk.Label(density_w, text=f"{dens} {unit_var2.get()}/{unit_var.get()}", font=("Helvetica", 20))
        calculated_density.place(x=240, y=320, width=200)

    density_w = tk.Toplevel()
    density_w.title("Sűrűség Kalkulátor")
    density_w.geometry("600x400")
    density_w.resizable(False, False)

    title_label = ttk.Label(density_w, text="Sűrűség Kalkulátor", font=("Helvetica", 30))
    volume = ttk.Label(density_w, text="Térfogat:", font=("Helvetica", 20))
    mass = ttk.Label(density_w, text="Tömeg:", font=("Helvetica", 20))
    density_label = ttk.Label(density_w, text="Sűrűség:", font=("Helvetica", 20))
    volume_entry = ttk.Entry(density_w)
    mass_entry = ttk.Entry(density_w)

    style = ttk.Style()
    style.configure("my.TMenubutton", font=("Helvetica", 18))

    unit_label = ttk.Label(density_w, text="Mértékegység:", font=("Helvetica", 20))
    unit_label.place(x=80, y=180)
    unit_label = ttk.Label(density_w, text="Mértékegység:", font=("Helvetica", 20))
    unit_label.place(x=400, y=180)

    unit_var = tk.StringVar()
    unit_entry = ttk.OptionMenu(density_w, unit_var, VOLUME[0], *VOLUME, style="my.TMenubutton")
    unit_entry.place(x=80, y=230)
    unit_var2 = tk.StringVar()
    unit_entry2 = ttk.OptionMenu(density_w, unit_var2, MASS[0], *MASS, style="my.TMenubutton")
    unit_entry2.place(x=400, y=230)

    ttk.Label(density_w, text="A számokat tizedespontot használva adja meg!").place(x=30, y=370)

    title_label.place(x=140, y=0)
    volume.place(x=80, y=100)
    mass.place(x=400, y=100)
    density_label.place(x=240, y=280)
    volume_entry.place(x=80, y=150)
    mass_entry.place(x=400, y=150)
    done_button = ttk.Button(density_w, text="Számol", command=density)
    done_button.place(x=520, y=370)