import tkinter as tk
from tkinter import ttk

MASS = ("g", "kg", "t")
VOLUME = ("cm^3", "m^3")
DENSITY = ("g/cm^3", "kg/m^3", "t/m^3")

def mass_calculator():
    def mass():
        vol = float(volume_entry.get())
        densy = float(dens_entry.get())
        mas = round(densy * vol, 3)
        calculated_mass = ttk.Label(mass_w, text=f"{mas}", font=("Helvetica", 20))
        calculated_mass.place(x=240, y=320)

    mass_w = tk.Toplevel()
    mass_w.title("Tömeg Kalkulátor")
    mass_w.geometry("600x400")
    mass_w.resizable(False, False)

    title_label = ttk.Label(mass_w, text="Tömeg kalkulátor", font=("Helvetica", 30))
    volume = ttk.Label(mass_w, text="Térfogat:", font=("Helvetica", 20))
    dens = ttk.Label(mass_w, text="Sűrűség:", font=("Helvetica", 20))
    mass_label = ttk.Label(mass_w, text="Tömeg:", font=("Helvetica", 20))
    volume_entry = ttk.Entry(mass_w)
    dens_entry = ttk.Entry(mass_w)

    unit_label = ttk.Label(mass_w, text="Mértékegység:", font=("Helvetica", 20))
    unit_label.place(x=80, y=180)
    unit_label = ttk.Label(mass_w, text="Mértékegység:", font=("Helvetica", 20))
    unit_label.place(x=400, y=180)

    unit_var = tk.StringVar()
    unit_entry = ttk.OptionMenu(mass_w, unit_var, VOLUME[0], *VOLUME)
    unit_entry.place(x=80, y=230)
    unit_var2 = tk.StringVar()
    unit_entry2 = ttk.OptionMenu(mass_w, unit_var2, DENSITY[0], *DENSITY)
    unit_entry2.place(x=400, y=230)

    title_label.place(x=170, y=0)
    volume.place(x=80, y=100)
    dens.place(x=400, y=100)
    mass_label.place(x=240, y=280)
    volume_entry.place(x=80, y=150)
    dens_entry.place(x=400, y=150)

    done_button = ttk.Button(mass_w, text="Számol", command=mass)
    done_button.place(x=480, y=350)

