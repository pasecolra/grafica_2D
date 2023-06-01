from tkinter import*
import random

BASE = 460
ALTURA = 220
RADIO= 50

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480 , height=240 )
frame_graficacion.place(x=10 , y=10)

c = Canvas (ventana_principal , width=BASE, height=ALTURA)
c.config(bg="white")
c.place(x=20,y=20)


ventana_principal.mainloop()