from tkinter import*
import random

BASE = 460
ALTURA = 220


ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.geometry("500x250")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

c = Canvas (ventana_principal , width=BASE, height=ALTURA)
c.config(bg="blue")
c.place(x=10,y=10)

"""color= "#"
for i in range(6):
    clor = color + random.choice("123456789ABCDEF")"""

base_mol=c.create_rectangle(BASE/2-100,ALTURA/2+60,BASE/2+150,ALTURA/2+100,fill="yellow")
trian = c.create_polygon(BASE/2-10,ALTURA/2+60,BASE/2+60,ALTURA/2+60,255,ALTURA/2-20,fill="SteelBlue1")
aspa_1 = c.create_arc(200,ALTURA/2-70,310,ALTURA/2+30,start=60,extent=60, fill="red")
aspa_2=c.create_arc(200,ALTURA/2-70,310,ALTURA/2+30,start=180,extent=60, fill="red")
aspa_3=c.create_arc(200,ALTURA/2-70,310,ALTURA/2+30,start=300,extent=60, fill="red")

ventana_principal.mainloop()