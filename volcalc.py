import tkinter as tk
from tkinter import ttk

MASS = ("g", "kg", "t")
VOLUME = ("cm^3", "m^3")
DENSITY = ("g/cm^3", "kg/m^3", "t/m^3")

def volume_calculator():

    def volume():
        dens = float(density_entry.get())
        mas = float(mass_entry.get())
        dens = round(mas / dens, 3)
        calculated_volume = ttk.Label(volume_w, text=f"{dens}", font=("Helvetica", 20))
        calculated_volume.place(x=240, y=320)

    volume_w = tk.Toplevel()
    volume_w.title("Térfogat Kalkulátor")
    volume_w.geometry("600x400")
    volume_w.resizable(False, False)

    title_label = ttk.Label(volume_w, text="Térfogat Kalkulátor", font=("Helvetica", 30))
    density = ttk.Label(volume_w, text="Sűrűség:", font=("Helvetica", 20))
    mass = ttk.Label(volume_w, text="Tömeg:", font=("Helvetica", 20))
    volume_label = ttk.Label(volume_w, text="Térfogat:", font=("Helvetica", 20))
    density_entry = ttk.Entry(volume_w)
    mass_entry = ttk.Entry(volume_w)

    unit_label = ttk.Label(volume_w, text="Mértékegység:", font=("Helvetica", 20))
    unit_label.place(x=80, y=180)
    unit_label = ttk.Label(volume_w, text="Mértékegység:", font=("Helvetica", 20))
    unit_label.place(x=400, y=180)

    unit_var = tk.StringVar()
    unit_entry = ttk.OptionMenu(volume_w, unit_var, DENSITY[0], *DENSITY)
    unit_entry.place(x=80, y=230)
    unit_var2 = tk.StringVar()
    unit_entry2 = ttk.OptionMenu(volume_w, unit_var2, MASS[0], *MASS)
    unit_entry2.place(x=400, y=230)

    title_label.place(x=140, y=0)
    density.place(x=80, y=100)
    mass.place(x=400, y=100)
    volume_label.place(x=240, y=280)
    density_entry.place(x=80, y=150)
    mass_entry.place(x=400, y=150)

    done_button = ttk.Button(volume_w, text="Számol", command=volume)
    done_button.place(x=480, y=350)