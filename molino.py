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

def modificar_arco(angulo):
    c.itemconfig(arco,extent=angulo)

"""color= "#"
for i in range(6):
    color = color + random.choice("123456789ABCDEF")"""
"""base_mol=c.create_rectangle(BASE/2-100,ALTURA/2+60,BASE/2+150,ALTURA/2+10,fill=color)
trian = c.create_polygon(BASE/2-10,ALTURA/2+60,BASE/2+60,ALTURA/2+60,255,ALTURA/2-20,fill="SteelBlue1")
aspa_1 = c.create_arc(200,ALTURA/2-70,310,ALTURA/2+30,start=60,extent=60, fill="red")
aspa_2=c.create_arc(200,ALTURA/2-70,310,ALTURA/2+30,start=180,extent=60, fill="red")
aspa_3=c.create_arc(200,ALTURA/2-70,310,ALTURA/2+30,start=300,extent=60, fill="red")"""

#general 100 circulos de color de 20 de radio y sin salir del canva
"""for i in range(100):
    color= "#"
    for i in range(6):
        color = color + random.choice("123456789ABCDEF")
    # general aleatoriamente X y Y
    radio=random.randint(5,25)
    X=random.randint(0,BASE-2*radio)
    Y=random.randint(0,ALTURA-2*radio)
    circulo=c.create_oval(X,Y,X+2*radio,Y+2*radio,fill=color)
    hola = c.create_arc(200,ALTURA/2-70,310,ALTURA/2+30,start=45,extent=280, fill="yellow")
    ojo = c.create_oval(240,ALTURA/2-60,260,ALTURA/2-40, fill="black")"""

arco=c.create_arc(BASE/2-RADIO,ALTURA/2-RADIO,BASE/2+RADIO,ALTURA/2+RADIO, start=0,extent=0, fill="blue")

"""# agregar imagen al canva
img_nave=PhotoImage(file="img/nave2.png")
nave= c.create_image(BASE/2,ALTURA/2,image=img_nave)"""

frame_controles=Frame(ventana_principal)
frame_controles.config(bg="green" , width=480 , height=230)
frame_controles.place(x=10 , y=260)

#barra de deslisamiento 
barra_deslizamiento=Scale(frame_controles, label="Angulo", from_=0, to=360, orient="horizontal",length=460, tickinterval=45,command=modificar_arco)
barra_deslizamiento.place(x=10,y=10)

ventana_principal.mainloop()


