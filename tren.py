from tkinter import*
#----------------------------------------
#----------variables globales------------
#----------------------------------------

BASE = 470
ALTURA = 460

#----------------------------------------
#----------VENTANA PRINCIPAL-------------
#----------------------------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.geometry("600x600")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

#----------------------------------------
#----------frame de graficacion----------
#----------------------------------------

#creacion canvas

c = Canvas (ventana_principal , width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=30,y=40)

#dibujar una linea recta

# linea_1 = c.create_line(BASE/2, ALTURA/2, BASE, 0 , fill="red2", width=2)
# linea_2 = c.create_line(BASE, ALTURA, BASE/2, ALTURA/2, fill="yellow2", width=2)
# linea_3 = c.create_line(0,ALTURA,BASE/2,ALTURA/2 ,  fill="blue2", width=2)
# linea_4 = c.create_line(0,0,BASE/2,ALTURA/2 ,  fill="green2", width=2)
# linea_5 = c.create_line(0,ALTURA/2,BASE/2,ALTURA/2 ,  fill="cyan2", width=2)
# linea_6 = c.create_line(BASE/2,0,BASE/2,ALTURA/2 ,  fill="pink2", width=2)
# linea_7 = c.create_line(BASE,ALTURA/2,BASE/2,ALTURA/2 ,  fill="DarkOrange2", width=2)
# linea_8 = c.create_line(BASE/2,ALTURA,BASE/2,ALTURA/2 ,  fill="purple2", width=2)

# #dubujar texto

# texto_1 = c.create_text(BASE/4,ALTURA/2, anchor="center", text="¡Sistemas!" , font=("Arial" , 25 ,"bold"), fill="cyan2",
# activefill="blue2")
# texto_2 = c.create_text(3*BASE/4,ALTURA/2, anchor="center", text="¡Colegi!" , font=("Arial" , 25 ,"bold"), fill="DarkOrange2",
# activefill="red2")
# texto_3 = c.create_text(2*BASE/4,ALTURA/4, anchor="center", text="¡Especialidad!" , font=("Arial" , 25 ,"bold"), fill="pink2",
# activefill="green2")
# texto_4 = c.create_text(2*BASE/4,3*ALTURA/4, anchor="center", text="¡Guanenta!" , font=("Arial" , 25 ,"bold"), fill="purple2",
# activefill="yellow")

# #dibujar rectangulo

rect_1 = c.create_polygon(BASE/2-5,ALTURA-ALTURA,BASE/2-5,ALTURA-ALTURA+25,BASE-45,ALTURA-ALTURA+25,BASE-45,ALTURA-ALTURA,fill="gray35",outline="gray35")

rect_2 = c.create_polygon(BASE/2-25,ALTURA-ALTURA+25,BASE/2-25,ALTURA-ALTURA+70,BASE-25,ALTURA-ALTURA+70,BASE-25,ALTURA-ALTURA+25, fill="gray35", outline="gray35")

rect_2 = c.create_polygon(BASE/2-5,ALTURA-ALTURA+70,BASE-45,ALTURA-ALTURA+70,BASE-45,ALTURA/2-15, BASE/2-5, ALTURA/2-15, fill= "gray50", outline= "gray50")

rect_3 = c.create_rectangle(BASE/2+25,ALTURA-ALTURA+90,BASE-80,ALTURA/2-40,fill=("gray75"), outline=("gray75"))

rect_4 = c.create_rectangle(BASE-25,ALTURA/2-15,BASE-BASE+95,ALTURA-65, fill=("gray70"), outline=("gray70"))

rect_5 = c.create_rectangle(BASE-BASE+115,ALTURA/2-15,BASE/2-65,ALTURA/2-80,fill=("gray50"), outline=("gray50"))


#desplegar ventana
ventana_principal.mainloop()