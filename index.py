from tkinter import *
from datetime import date
from datetime import datetime



raiz = Tk()
raiz.geometry("500x500")
raiz.title("Examen final by Osman Cordero")
miFrame= Frame()
miFrame.pack()
bienvenido = Label(miFrame, text="BIENVENIDO A MI PROGRAMA")
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('Arial', 16))

#Funciones


nombre = StringVar()
apellido = StringVar()
dia = IntVar()
mes = IntVar()
anio = IntVar()

#binario(en desarrollo)
def binario ():
    uno=int(dia.get())
    dos=int(mes.get())
    tres=int(anio.get())
    bindia=format(uno, '0b' )
    binmes=format(dos, '0b')
    binanio=format(tres, '0b')

    lblResp['text'] = "La fecha es: {}/{}/{} y  en binario es:{}/{}/{}".format(uno,dos,tres,bindia,binmes,binanio)
#dias vividos
def conteoDias():
    fechaString = f"{anio.get()}-{mes.get()}-{dia.get()}"
    date_object = datetime.strptime(fechaString, '%Y-%m-%d')

    today= datetime.today()
    
    d1 = today
    d2 = date_object
    result1 = abs(d1-d2).days 

    respuesta = f"Usted nacio el {date_object} y ha vivido {result1} días."

    lblResp.configure(text = respuesta)

#par e impar de nombre y apellido
def conteoLetras():
    sNombre = f"{nombre.get()}"
    sApellido = f"{apellido.get()}"

    conteoN = len(sNombre)
    conteoA = len(sApellido)
  

    if conteoN % 2 == 0:
        r1 = f"{sNombre} su Nombre es de número Par"
    else:
        r1 = f"{sNombre} su Nombre es de número Impar"

    if conteoA % 2 == 0:
        r2 = f"{sApellido} su Apellido es de número Par."
    else:
        r2 = f"{sApellido} su Apellido es de número Impar."

    respuesta = f"{r1} y  {r2} "

    lblResp.configure(text =respuesta )


#vocalConsonante
def vocalConsonante():
    sNombre = f"{nombre.get()}"
    sApellido = f"{apellido.get()}"
    cuenta = 0
    for carac in sNombre:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
    for carac in sApellido:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
    cajita=len(sNombre)
    cajita1=len(sApellido)
    consonante=cajita+cajita1-cuenta

    lblResp['text'] = 'Su nombre y apellido tienen {} vocales y {} consonantes'.format(cuenta,consonante)

#Nombre al alReves
def ALREVES():
    cajita = nombre.get()+" "+apellido.get()
    cajita = cajita[::-1]
    lblResp["text"] = nombre.get() + " " + apellido.get() + " al revés es: " + cajita
#Nombre
lblnombre= Label(miFrame, text="Nombre:")
lblnombre.grid(row=1, column=0)
lblnombre.config(padx=10, pady=10)
txtNombre=Entry(miFrame, textvariable =nombre)
txtNombre.grid(row=1, column=1)

#Apellido
lblapellido=Label(miFrame, text="Apellido:")
lblapellido.grid(row=2, column=0)
lblapellido.config(padx=10, pady=10)
txtApellido=Entry(miFrame, textvariable =apellido)
txtApellido.grid(row=2, column=1)

#Día
lbldia=Label(miFrame, text="Día: ")
lbldia.grid(row=3, column=0)
lbldia.config(padx=10, pady=10)
txtDia=Entry(miFrame, textvariable =dia)
txtDia.grid(row=3, column=1)

#Mes
lblmes=Label(miFrame, text="Mes: ")
lblmes.grid(row=4, column=0)
lblmes.config(padx=10, pady=10)
txtMes=Entry(miFrame, textvariable =mes)
txtMes.grid(row=4, column=1)

#Año
lblanio=Label(miFrame, text="Año: ")
lblanio.grid(row=5, column=0)
lblanio.config(padx=10, pady=10)
txtanio=Entry(miFrame, textvariable =anio)
txtanio.grid(row=5, column=1)

#Botones
btnFuncion1 = Button(miFrame, text="Función 1", command=binario)
btnFuncion1.grid(row=6, column=0)
btnFuncion1.config(padx=10, pady=10)
btnFuncion2 = Button(miFrame, text = "Función 2", command=conteoDias)
btnFuncion2.grid(row=6, column=1)
btnFuncion2.config(padx=10, pady=10)
btnFuncion3 = Button(miFrame, text = "Función 3", command=conteoLetras)
btnFuncion3.grid(row=7, column=0)
btnFuncion3.config(padx=10, pady=10)
btnFuncion4 = Button(miFrame, text = "Función 4", command=vocalConsonante)
btnFuncion4.grid(row=7, column=1)
btnFuncion4.config(padx=10, pady=10)
btnFuncion5 = Button(miFrame, text = "Función 5", command=ALREVES)
btnFuncion5.grid(row=8, column=0)
btnFuncion5.config(padx=10, pady=10)
#Respuesta
lblResp=Label(miFrame, text="Respuesta:")
lblResp.grid(row=9, column=0)
lblResp.config(padx=10, pady=10)
lblR=Label(miFrame)
lblR.grid(row=10, column=0)
lblR.config(padx=10, pady=10)

raiz.mainloop()

