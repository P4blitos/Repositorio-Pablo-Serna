from tkinter import * 
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image,ImageTk
import random
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np

class trabajo():
    def __init__(self):
        principal = Tk()
        principal.title("Parcial 1")
        principal.geometry("1300x700")
        principal.configure(background="sky blue")

        fuente = font.Font(size=22)
        fuente2 = font.Font(size=12)
        self.fig, self.ax = plt.subplots()

        self.Lbbienvenida = Label(principal,text="Digite la ecuacion", font=fuente,bg="sky blue")
        self.Lbbienvenida.place(x=50, y=50)
        
        #Textbox donde se digita la ecuacion
        self.Entecuacion= Entry(principal,bg='white',font=fuente2, width=25)
        self.Entecuacion.place(x=50, y=100)

        self.SelecMetodo = Label(principal,text="Selecciona el metodo", font=fuente,bg="sky blue")
        self.SelecMetodo.place(x=50, y=160)

        self.Tanteo = IntVar()
        self.Biseccion = IntVar()
        self.Regla = IntVar()

        self.seleccionarTanteo= Checkbutton(principal,text="Tanteo", font=fuente2, bg="white",variable=self.Tanteo)
        

        self.seleccionarBiseccion= Checkbutton(principal,text="Biseccion", font=fuente2, bg="white", variable=self.Biseccion)
        

        self.seleccionarRegla= Checkbutton(principal,text="Regla falsa", font=fuente2, bg="white", variable=self.Regla)
        

        self.btnCalcular= Button(principal, text="Calcular", width=14,height=2, font=fuente, bg="#FF7671", command=self.Calcular)
        self.btnCalcular.place(x=50,y=250)

        self.btnGraficar= Button(principal, text="Graficar", width=14,height=2, font=fuente, bg="#FF7671", command=self.graficar)
        self.btnGraficar.place(x=360,y=250)
        
        self.btnLimpiar= Button(principal, text="Limpiar", width=10,height=2, font=fuente, bg="#FF7671", command=self.limpiar)
        self.btnLimpiar.place(x=400,y=550)


        #Para que no se pueda elegir mas de uno
        self.checkboxes = [self.seleccionarTanteo, self.seleccionarBiseccion, self.seleccionarRegla]
        for checkbox in self.checkboxes:
            checkbox.pack()
            
            # Configura la función "command" de cada checkbox
            checkbox.config(command=lambda c=checkbox: self.deselect_all(c))

        self.seleccionarRegla.place(x=270, y=210)
        self.seleccionarBiseccion.place(x=150, y=210)
        self.seleccionarTanteo.place(x=50, y=210)
        
        #Iteraciones
        self.NITanteo = Label(principal,text="Iteraciones Tanteo", font=fuente2,bg="sky blue")
        self.NITanteo.place(x=50, y=370)

        self.NumTanteo = Label(principal,text="         ", font=fuente2,bg="white")
        self.NumTanteo.place(x=50, y=395)

        self.NIBiseccion = Label(principal,text="Iteraciones Biseccion", font=fuente2,bg="sky blue")
        self.NIBiseccion.place(x=50, y=430)

        self.NumBiseccion = Label(principal,text="         ", font=fuente2,bg="white")
        self.NumBiseccion.place(x=50, y=455)

        self.NIRegla = Label(principal,text="Iteraciones Regla Falsa", font=fuente2,bg="sky blue")
        self.NIRegla.place(x=50, y=490)

        self.NumRegla = Label(principal,text="         ", font=fuente2,bg="white")
        self.NumRegla.place(x=50, y=515)

        self.Raiz = Label(principal,text="Raiz", font=fuente,bg="sky blue")
        self.Raiz.place(x=280, y=430)

        self.NumRaiz = Label(principal,text="                   ", font=fuente2,bg="white")
        self.NumRaiz.place(x=280, y=480)

        Imagen= Image.open("C:/Users/Usuario/Desktop/hola/Juan-Brinez-De-Leon.png")
        photo = ImageTk.PhotoImage(Imagen)
        self.imagen= Label(principal, image=photo, width=400, height=500)
        self.imagen.place(x=660,y=50)

        principal.mainloop()


    def deselect_all(self, current_checkbox):
        # Desmarca todos los checkboxes, excepto el que se acaba de marcar
        for checkbox in self.checkboxes:
            if checkbox is not current_checkbox:
                checkbox.deselect()
    
    def Calcular(self):
        if (self.Tanteo.get()==1):
            ecu = self.Entecuacion.get()
            iterador = 0
            x = random.randint(-20,20)
            while True:
               fx = eval(ecu.format(x))
               if abs(fx) < 0.001:  # La precisión se puede ajustar a la necesidad
                   iterador= iterador+1
                   self.NumRaiz.config(text=x)
                   self.NumTanteo.config(text=iterador)
                   break
               elif fx > 0:
                   x -= 0.01
                   iterador = iterador + 1
               else:
                   x += 0.01
                   iterador = iterador + 1
        
    
        if (self.Biseccion.get()==1):
            ecu = self.Entecuacion.get()
            ecu = ecu.replace("x", "{}")
            a = random.randint(-20, 20)
            b = random.randint(-20, 20)
            iterador_max = 1000000
            iterador = 0
            tolerancia = 0.01
            c = 0

            while True:
                if eval(ecu.format(a)) * eval(ecu.format(b)) < 0:
                    iterador = 0
                    while True:
                        c = (a + b) / 2
                        if abs(eval(ecu.format(a)) * eval(ecu.format(c))) <= tolerancia:
                            iterador=iterador+1
                            self.NumBiseccion.config(text=iterador)
                            self.NumRaiz.config(text=c)
                            break
                        elif eval(ecu.format(a)) * eval(ecu.format(c)) < 0:
                            b = c
                            iterador = iterador + 1
                        else:
                            a = c
                            iterador = iterador + 1
                        if iterador >= iterador_max or abs(b - a) <= tolerancia:
                            break
                    break
                else:
                 a = random.randint(-20, 20)
                 b = random.randint(-20, 20) 

        if(self.Regla.get()==1):
            ecu = self.Entecuacion.get()
            ecu = ecu.replace("x", "{}")
            a = random.randint(-20, 20)
            b = random.randint(-20, 20)
            iterador_max = 1000000
            iterador = 0
            tolerancia = 0.01
            c = 0

            while True:
                if eval(ecu.format(a)) * eval(ecu.format(b)) < 0:
                    iterador = 0
                    while True:
                        c = a- ((eval(ecu.format(a)))*(b-a))/((eval(ecu.format(b)))-(eval(ecu.format(a))))
                        if abs(eval(ecu.format(a)) * eval(ecu.format(c))) <= tolerancia:
                            iterador= iterador+1
                            self.NumRegla.config(text=iterador)
                            self.NumRaiz.config(text=c)
                            break
                        elif eval(ecu.format(a)) * eval(ecu.format(c)) < 0:
                            b = c
                            iterador = iterador + 1
                        else:
                            a = c
                            iterador = iterador + 1
                        if iterador >= iterador_max or abs(b - a) <= tolerancia:
                            break
                    break
                else:
                 a = random.randint(-20, 20)
                 b = random.randint(-20, 20) 
    
    def graficar(self):
        ecuacion = self.Entecuacion.get()
        raiz = float(self.NumRaiz.cget("text"))
        if (self.Regla.get()==1 or self.Biseccion.get()==1):
            ecuacion = ecuacion.replace("{}", "x")
        
        x = np.linspace(-10, 10, 1000)

        y = eval(ecuacion)

        fig, ax = plt.subplots()
        ax.cla()
        ax.plot(x,y)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Gráfica de la ecuación: ' + ecuacion)

        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        ax.plot(raiz, 0, 'ro')
        
        canvas = FigureCanvasTkAgg(fig, master=self.imagen)
        canvas.draw()
        canvas.get_tk_widget().pack() 
    
    def limpiar(self):
        self.Entecuacion.delete(0, tk.END)
        canvas_widget = self.imagen.winfo_children()[0]
        # Destruir el widget
        canvas_widget.destroy()

abrir=trabajo()