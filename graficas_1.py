from tkinter import*
#----------------------------------------
#----------variables globales------------
#----------------------------------------

BASE = 460
ALTURA = 220

#----------------------------------------
#----------VENTANA PRINCIPAL-------------
#----------------------------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

#----------------------------------------
#----------frame de graficacion----------
#----------------------------------------

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480 , height=240 )
frame_graficacion.place(x=10 , y=10)

#creacion canvas

c = Canvas (frame_graficacion , width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

#dibujar una linea recta

linea_1 = c.create_line(BASE/2, ALTURA/2, BASE, 0 , fill="red2", width=2)
linea_2 = c.create_line(BASE, ALTURA, BASE/2, ALTURA/2, fill="yellow2", width=2)
linea_3 = c.create_line(0,ALTURA,BASE/2,ALTURA/2 ,  fill="blue2", width=2)
linea_4 = c.create_line(0,0,BASE/2,ALTURA/2 ,  fill="green2", width=2)
linea_5 = c.create_line(0,ALTURA/2,BASE/2,ALTURA/2 ,  fill="cyan2", width=2)
linea_6 = c.create_line(BASE/2,0,BASE/2,ALTURA/2 ,  fill="pink2", width=2)
linea_7 = c.create_line(BASE,ALTURA/2,BASE/2,ALTURA/2 ,  fill="DarkOrange2", width=2)
linea_8 = c.create_line(BASE/2,ALTURA,BASE/2,ALTURA/2 ,  fill="purple2", width=2)

#dubujar texto

texto_1 = c.create_text(BASE/4,ALTURA/2, anchor="center", text="¡Sistemas!" , font=("Arial" , 25 ,"bold"), fill="cyan2",
activefill="blue2")
texto_2 = c.create_text(3*BASE/4,ALTURA/2, anchor="center", text="¡Colegi!" , font=("Arial" , 25 ,"bold"), fill="DarkOrange2",
activefill="red2")
texto_3 = c.create_text(2*BASE/4,ALTURA/4, anchor="center", text="¡Especialidad!" , font=("Arial" , 25 ,"bold"), fill="pink2",
activefill="green2")
texto_4 = c.create_text(2*BASE/4,3*ALTURA/4, anchor="center", text="¡Guanenta!" , font=("Arial" , 25 ,"bold"), fill="purple2",
activefill="yellow")

#dibujar rectangulo

rect_1 = c.create_rectangle(BASE,ALTURA,BASE,ALTURA,fill="blue",outline="blue")
rect_2 = c.create_rectangle(0,0,BASE/4,ALTURA/2,fill="orange",outline="blue")
rect_3 = c.create_rectangle(BASE/4,0,BASE/2,ALTURA/2,fill="yellow",outline="blue")
rect_4 = c.create_rectangle(BASE/4,ALTURA,BASE/2,ALTURA/2,fill="yellow",outline="blue")
rect_5 = c.create_rectangle(BASE/4,ALTURA/4,BASE/4,ALTURA/4,fill="red",outline="blue")


#frame de controles

frame_controles=Frame(ventana_principal)
frame_controles.config(bg="green" , width=480 , height=230)
frame_controles.place(x=10 , y=260)

#desplegar ventana
ventana_principal.mainloop()