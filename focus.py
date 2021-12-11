from tkinter import *
import time
import threading

#PANTALLA--------------------------------------------------------------
root = Tk()
root.title("Pomodoro_focus")

mi_frame = Frame(root)
mi_frame.pack()
mi_frame.config(bg="red")

texto = Label(mi_frame, text="Introduce el tiempo que quieres trabajar", font=("Calibri", 20), bg="grey")
texto.grid(row=0, column=0, columnspan=3, pady=(10,20), padx=20)

numero_pantalla_minutos = StringVar()
numero_pantalla_segundos = StringVar()

#ENTRY----------------------------------------------------------------
pantalla_minutos = Entry(mi_frame, font=("Calibri", 75), width=2, textvariable=numero_pantalla_minutos)
pantalla_minutos.grid(row=2, column=0, sticky='e')
pantalla_minutos.insert(0, "00")
pantalla_minutos.configure({"disabledforeground" : "black"})
pantalla_minutos.config(state="disable")


dos_putos = Label(mi_frame, text=":", font=("Calibri",80), bg="red")
dos_putos.grid(row=2, column=1)

pantalla_segundos = Entry(mi_frame, font=("Calibri", 75), width=2, textvariable=numero_pantalla_segundos)
pantalla_segundos.grid(row=2, column=2,  sticky='w')
pantalla_segundos.insert(0, "00")
pantalla_segundos.configure({"disabledforeground" : "black"})
pantalla_segundos.config(state="disable")


#FUNCIONES-----------------------------------------------------------

def pulsar_arriba(numero):
    global numero_pantalla_minutos
    pantalla_minutos.config(state="normal")
    numero = int(numero)
    numero += 1
    numero_pantalla_minutos.set(str(numero))
    pantalla_minutos.config(state="disabled")

def pulsar_abajo(numero):
    global numero_pantalla_minutos
    if numero == "0" or numero == "00":
        return 
    pantalla_minutos.config(state="normal")
    numero = int(numero)
    numero -= 1
    numero_pantalla_minutos.set(str(numero))
    pantalla_minutos.config(state="disabled")

validator = 0

def empezar():
    global validator
    global numero_pantalla_segundos
    global numero_pantalla_minutos
    while True:

        pantalla_segundos.config(state="normal")
        if validator == 0:    
            numero_pantalla_segundos.set("59")
            validator += 1
        numero = pantalla_segundos.get()
        numero = int(numero) - 1
        numero = str(numero)
        time.sleep(1)
    
        if numero_pantalla_segundos.get() == "0":
            numero2 = int(numero_pantalla_minutos.get())
            numero2 -= 1
            if numero2 == -1:
                break
            pantalla_minutos.config(state="normal")
            numero_pantalla_minutos.set(str(numero2))
            pantalla_minutos.config(state="disabled")
            numero_pantalla_segundos.set("59")
        else:
            numero_pantalla_segundos.set(str(numero))

        pantalla_segundos.config(state="disabled")
        
    
def start1():
    threading.Thread(target=empezar).start()


#BOTONES-------------------------------------------------------------
foto1 = PhotoImage(file="arriba.png")
foto1 = foto1.subsample(13)
boton_subir = Button(mi_frame, image=foto1, width=100, height=50,bg="grey", command=lambda:pulsar_arriba(pantalla_minutos.get()))
boton_subir.grid(row=1, column=0, columnspan=1, sticky="e")

foto = PhotoImage(file="abajo.png")
foto = foto.subsample(80)
boton_bajar = Button(mi_frame, image=foto, width=100, height=50,bg="grey", command=lambda:pulsar_abajo(pantalla_minutos.get()))
boton_bajar.grid(row=3, column=0, columnspan=1, sticky="e", pady=(0, 20))

boton_empezar = Button(mi_frame, text="EMPEZAR", font=("Calibri", 20), bg="grey", command=lambda:start1())
boton_empezar.grid(row=4, column=1, pady=(0, 20))


root.mainloop()