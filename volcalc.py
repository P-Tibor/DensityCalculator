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
        if unit_var.get() == "g/cm^3" and unit_var2.get() == "g":
            calculated_volume = ttk.Label(volume_w, text=f"{dens} cm^3", font=("Helvetica", 20))
            calculated_volume.place(x=240, y=320, width=200)
        elif unit_var.get() == "kg/m^3" and unit_var2.get() == "kg":
            calculated_volume = ttk.Label(volume_w, text=f"{dens} m^3", font=("Helvetica", 20))
            calculated_volume.place(x=240, y=320, width=200)
        elif unit_var.get() == "t/m^3" and unit_var2.get() == "t":
            calculated_volume = ttk.Label(volume_w, text=f"{dens} m^3", font=("Helvetica", 20))
            calculated_volume.place(x=240, y=320, width=200)
        else:
            ttk.Label(volume_w, text="Válasszon egy megfelelő sűrűség/térfogat mértékegység párt!").place(x=30, y=370)


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

    style = ttk.Style()
    style.configure("my.TMenubutton", font=("Helvetica", 18))

    unit_label = ttk.Label(volume_w, text="Mértékegység:", font=("Helvetica", 20))
    unit_label.place(x=80, y=180)
    unit_label = ttk.Label(volume_w, text="Mértékegység:", font=("Helvetica", 20))
    unit_label.place(x=400, y=180)

    unit_var = tk.StringVar()
    unit_entry = ttk.OptionMenu(volume_w, unit_var, DENSITY[0], *DENSITY, style="my.TMenubutton")
    unit_entry.place(x=80, y=230)
    unit_var2 = tk.StringVar()
    unit_entry2 = ttk.OptionMenu(volume_w, unit_var2, MASS[0], *MASS, style="my.TMenubutton")
    unit_entry2.place(x=400, y=230)

    ttk.Label(volume_w, text="A számokat tizedespontot használva adja meg!").place(x=30, y=370)

    title_label.place(x=140, y=0)
    density.place(x=80, y=100)
    mass.place(x=400, y=100)
    volume_label.place(x=240, y=280)
    density_entry.place(x=80, y=150)
    mass_entry.place(x=400, y=150)

    done_button = ttk.Button(volume_w, text="Számol", command=volume)
    done_button.place(x=520, y=370)