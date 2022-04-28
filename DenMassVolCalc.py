import tkinter as tk
from tkinter import ttk

MASS = ("g", "kg", "t")
VOLUME = ("cm³", "m³")
DENSITY = ("g/cm³", "kg/m³", "t/m³")


def density_calculator():

    def density():
        try:
            vol = float(volume_entry.get())
            mas = float(mass_entry.get())
            dens = round(mas / vol, 3)
            calculated_density = ttk.Label(tab1, text=f"{dens} {unit_var2.get()}/{unit_var.get()}",
                                           font=("Helvetica", 20))
            calculated_density.place(x=240, y=320, width=200)

        except:
            error_prompt = tk.Toplevel()
            error_prompt.title("Error")
            error_prompt.geometry("330x70+500+200")
            img = tk.PhotoImage(file="error.png", height=20, width=20)
            label = ttk.Label(error_prompt, image=img)
            label.image = img
            label.place(x=10, y=21)
            ttk.Label(error_prompt, text="Enter numbers using decimal point!").place(x=35, y=23)



    title_label = ttk.Label(tab1, text="Density Calculator", font=("Helvetica", 30))
    volume = ttk.Label(tab1, text="Volume:", font=("Helvetica", 20))
    mass = ttk.Label(tab1, text="Mass:", font=("Helvetica", 20))
    density_label = ttk.Label(tab1, text="Density:", font=("Helvetica", 20))
    volume_entry = ttk.Entry(tab1)
    mass_entry = ttk.Entry(tab1)

    style = ttk.Style()
    style.configure("my.TMenubutton", font=("Helvetica", 18))

    unit_label = ttk.Label(tab1, text="Unit:", font=("Helvetica", 20))
    unit_label.place(x=80, y=180)
    unit_label = ttk.Label(tab1, text="Unit:", font=("Helvetica", 20))
    unit_label.place(x=400, y=180)

    unit_var = tk.StringVar()
    unit_entry = ttk.OptionMenu(tab1, unit_var, VOLUME[0], *VOLUME, style="my.TMenubutton")
    unit_entry.place(x=80, y=230)
    unit_var2 = tk.StringVar()
    unit_entry2 = ttk.OptionMenu(tab1, unit_var2, MASS[0], *MASS, style="my.TMenubutton")
    unit_entry2.place(x=400, y=230)

    ttk.Label(tab1, text="Enter numbers using decimal point!").place(x=30, y=370)

    title_label.place(x=140, y=0)
    volume.place(x=80, y=100)
    mass.place(x=400, y=100)
    density_label.place(x=240, y=280)
    volume_entry.place(x=80, y=150)
    mass_entry.place(x=400, y=150)
    done_button = ttk.Button(tab1, text="Calculate", command=density)
    done_button.place(x=520, y=370)


def mass_calculator():
    def mass():
        try:
            vol = float(volume_entry.get())
            densy = float(dens_entry.get())
            mas = round(densy * vol, 3)
            if unit_var.get() == "cm³" and unit_var2.get() == "g/cm³":
                calculated_mass = ttk.Label(tab2, text=f"{mas} g", font=("Helvetica", 20))
                calculated_mass.place(x=240, y=320)
            elif unit_var.get() == "m³" and unit_var2.get() == "kg/m³":
                calculated_mass = ttk.Label(tab2, text=f"{mas} kg", font=("Helvetica", 20))
                calculated_mass.place(x=240, y=320)
            elif unit_var.get() == "m³" and unit_var2.get() == "t/m³":
                calculated_mass = ttk.Label(tab2, text=f"{mas} t", font=("Helvetica", 20))
                calculated_mass.place(x=240, y=320, width=200)
            else:
                ttk.Label(tab2, text="Choose a valid volume/density unit pair!", foreground="red").place(x=30, y=370)

        except:
            error_prompt = tk.Toplevel()
            error_prompt.title("Error")
            error_prompt.geometry("330x70+500+200")
            img = tk.PhotoImage(file="error.png", height=20, width=20)
            label = ttk.Label(error_prompt, image=img)
            label.image = img
            label.place(x=10, y=21)
            ttk.Label(error_prompt, text="Enter numbers using decimal point!").place(x=35, y=23)



    title_label = ttk.Label(tab2, text="Mass Calculator", font=("Helvetica", 30))
    volume = ttk.Label(tab2, text="Volume:", font=("Helvetica", 20))
    dens = ttk.Label(tab2, text="Density:", font=("Helvetica", 20))
    mass_label = ttk.Label(tab2, text="Mass:", font=("Helvetica", 20))
    volume_entry = ttk.Entry(tab2)
    dens_entry = ttk.Entry(tab2)

    style = ttk.Style()
    style.configure("my.TMenubutton", font=("Helvetica", 18))
    unit_label = ttk.Label(tab2, text="Unit:", font=("Helvetica", 20))
    unit_label.place(x=80, y=180)
    unit_label = ttk.Label(tab2, text="Unit:", font=("Helvetica", 20))
    unit_label.place(x=400, y=180)

    unit_var = tk.StringVar()
    unit_entry = ttk.OptionMenu(tab2, unit_var, VOLUME[0], *VOLUME, style="my.TMenubutton")
    unit_entry.config()
    unit_entry.place(x=80, y=230)
    unit_var2 = tk.StringVar()
    unit_entry2 = ttk.OptionMenu(tab2, unit_var2, DENSITY[0], *DENSITY, style="my.TMenubutton")
    unit_entry2.place(x=400, y=230)

    ttk.Label(tab2, text="Enter numbers using decimal point!").place(x=30, y=370)

    title_label.place(x=160, y=0)
    volume.place(x=80, y=100)
    dens.place(x=400, y=100)
    mass_label.place(x=240, y=280)
    volume_entry.place(x=80, y=150)
    dens_entry.place(x=400, y=150)

    done_button = ttk.Button(tab2, text="Calculate", command=mass)
    done_button.place(x=520, y=370)


def volume_calculator():

    def volume():
        try:
            dens = float(density_entry.get())
            mas = float(mass_entry.get())
            dens = round(mas / dens, 3)
            if unit_var.get() == "g/cm³" and unit_var2.get() == "g":
                calculated_volume = ttk.Label(tab3, text=f"{dens} cm³", font=("Helvetica", 20))
                calculated_volume.place(x=240, y=320, width=200)
            elif unit_var.get() == "kg/m³" and unit_var2.get() == "kg":
                calculated_volume = ttk.Label(tab3, text=f"{dens} m³", font=("Helvetica", 20))
                calculated_volume.place(x=240, y=320, width=200)
            elif unit_var.get() == "t/m³" and unit_var2.get() == "t":
                calculated_volume = ttk.Label(tab3, text=f"{dens} m³", font=("Helvetica", 20))
                calculated_volume.place(x=240, y=320, width=200)
            else:
                ttk.Label(tab3, text="Choose a valid volume/density unit pair!", foreground="red").place(x=30, y=370)
        except:
            error_prompt = tk.Toplevel()
            error_prompt.title("Error")
            error_prompt.geometry("330x70+500+200")
            img = tk.PhotoImage(file="error.png", height=20, width=20)
            label = ttk.Label(error_prompt, image=img)
            label.image = img
            label.place(x=10, y=21)
            ttk.Label(error_prompt, text="Enter numbers using decimal point!").place(x=35, y=23)



    title_label = ttk.Label(tab3, text="Volume Calculator", font=("Helvetica", 30))
    density = ttk.Label(tab3, text="Density:", font=("Helvetica", 20))
    mass = ttk.Label(tab3, text="Mass:", font=("Helvetica", 20))
    volume_label = ttk.Label(tab3, text="Volume:", font=("Helvetica", 20))
    density_entry = ttk.Entry(tab3)
    mass_entry = ttk.Entry(tab3)

    style = ttk.Style()
    style.configure("my.TMenubutton", font=("Helvetica", 18))

    unit_label = ttk.Label(tab3, text="Unit:", font=("Helvetica", 20))
    unit_label.place(x=80, y=180)
    unit_label = ttk.Label(tab3, text="Unit:", font=("Helvetica", 20))
    unit_label.place(x=400, y=180)

    unit_var = tk.StringVar()
    unit_entry = ttk.OptionMenu(tab3, unit_var, DENSITY[0], *DENSITY, style="my.TMenubutton")
    unit_entry.place(x=80, y=230)
    unit_var2 = tk.StringVar()
    unit_entry2 = ttk.OptionMenu(tab3, unit_var2, MASS[0], *MASS, style="my.TMenubutton")
    unit_entry2.place(x=400, y=230)

    ttk.Label(tab3, text="Enter numbers using decimal point!").place(x=30, y=370)

    title_label.place(x=140, y=0)
    density.place(x=80, y=100)
    mass.place(x=400, y=100)
    volume_label.place(x=240, y=280)
    density_entry.place(x=80, y=150)
    mass_entry.place(x=400, y=150)

    done_button = ttk.Button(tab3, text="Calculate", command=volume)
    done_button.place(x=520, y=370)


root = tk.Tk()
root.title("Density, Mass, Volume Calculator")
root.geometry("630x430")
root.resizable(False, False)
root.iconbitmap("root.ico")


my_notebook = ttk.Notebook(root)
my_notebook.pack(fill=tk.BOTH)
tab1 = ttk.Frame(my_notebook, width=600, height=400)
tab2 = ttk.Frame(my_notebook, width=600, height=400)
tab3 = ttk.Frame(my_notebook, width=600, height=400)
tab1.pack(fill=tk.BOTH, expand=True)
tab2.pack(fill=tk.BOTH)
tab3.pack(fill=tk.BOTH)

density_calculator()
mass_calculator()
volume_calculator()

my_notebook.add(tab1, text="Density Calculator")
my_notebook.add(tab2, text="Mass Calculator")
my_notebook.add(tab3, text="Volume Calculator")


root.mainloop()
