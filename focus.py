from tkinter import *

root = Tk()
root.title("Pomodoro_focus")

mi_frame = Frame(root)
mi_frame.pack()
mi_frame.config(bg="red")

texto = Label(mi_frame, text="Introduce el tiempo que quieres trabajar", font=("Calibri", 20), bg="grey")
texto.grid(row=0, column=0, columnspan=3, pady=(10,20), padx=20)

pantalla_minutos = Entry(mi_frame, font=("Calibri", 75), width=2)
pantalla_minutos.grid(row=2, column=0, sticky='e')

dos_putos = Label(mi_frame, text=":", font=("Calibri",40), bg="red")
dos_putos.grid(row=2, column=1)

pantalla_segundos = Entry(mi_frame, font=("Calibri", 75), width=2)
pantalla_segundos.grid(row=2, column=2,  sticky='w')
foto1 = PhotoImage(file="arriba.png")
foto1 = foto1.subsample(13)
boton_subir = Button(mi_frame, image=foto1, width=100, height=50,bg="grey")
boton_subir.grid(row=1, column=0, columnspan=1, sticky="e")

foto = PhotoImage(file="abajo.png")
foto = foto.subsample(80)
boton_bajar = Button(mi_frame, image=foto, width=100, height=50,bg="grey")
boton_bajar.grid(row=3, column=0, columnspan=1, sticky="e", pady=(0, 20))


root.mainloop()