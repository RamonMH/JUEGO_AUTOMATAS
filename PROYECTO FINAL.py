'''
---------------------------------------------------------|
|***************Hernandez Rojas Luis Mario***************|
|****************Mendoza Hernandez Ramon*****************|
|********************************************************|
|*************************4CM25**************************|
|--------------------------------------------------------|
'''

from tkinter import *
from tkinter import messagebox
import sys

jugadas=['Jugada 1', 'Jugada 2']

lengreg1=["acab","acb","bba","cba","bbscba","bbeba","cbcba","cbeba","da",
         "ddea","ddaa","dddab","ddeddab","ddeddb","dddb","ddaddab","ddaddb",
         "ddedb","ddadb","eac","ddeab","ddeb","daeab","daeb","ddcdeab","ddcdeab",        
         "ddcdeb","ddbdeab","ddbdeb","dacaeab","dacaeb","dabaeab","dabaeb","dabdeab"         
         "dabdeb","dacdeab","dacdeb","ddbaeab","ddbaeb","ddcaeab","ddcaeb"]
         
lengreg2=["adaae","adaee","adaabae","adaebae","adaeaae","adaebee","adaaaae","adaabee",
      "adaeaee","adaaaee","aeace","aeacbce","aeacace","aeacbac","aeacbeae","aeacaae",    
      "aeacaee","aeace","aeacbcbae","aeacbcbec","aeacbcaae","aeacbcaee","aeacacbae", 
      "aeacacbee","aeacacaae","aeacacaee","cdb","ca","eb"]

goloc=0 
golvis=0
ganador=0
verif1=0
verif2=0

ventana=Tk()

ju1=PhotoImage(file="J1G.png")
ju2=PhotoImage(file="J2G.png")


def verj1():
    wj1=Toplevel()
    wj1.geometry("600x370")
    lbljug=Label(wj1, image=ju1).pack()

def verj2():    
    wj2=Toplevel()
    wj2.geometry("600x370")
    lbljug=Label(wj2, image=ju2).pack()

cadena1=StringVar()
cadena2=StringVar()

ventana.title("AUTOGOL")
ventana.geometry("600x600+350+20")
ventana.config(bg="light steel blue")

img=PhotoImage(file="LOGO.png")
label=Label(ventana, image=img).place(x=0,y=40)

imgj1=PhotoImage(file="JUGADA1.png")
imgj2=PhotoImage(file="JUGADA2.png")

def abrirventanajuego():
    ventana.withdraw()
    winju=Toplevel()
    winju.geometry("800x600+350+20")
    winju.configure(bg="forest green")
    lblcad=Label(winju, text="Selecciona la jugada que vas a usar", font="Arial", bg="forest green", fg="white")
    lblcad.place(x=300, y=40)

    lbljug1=Label(winju, image=imgj1).place(x=15 ,y=133)
    lbljug2=Label(winju, image=imgj2).place(x=420 ,y=130)

    lblcad=Label(winju, text="JUGADA 1", font="Arial", bg="forest green", fg="white").place(x=170,y=100)
    lblcad=Label(winju, text="JUGADA 2", font="Arial", bg="forest green", fg="white").place(x=550,y=100)
    
    jugadasel1=StringVar()
    jugadasel1.set(jugadas[0])
    jugadasel2=StringVar()
    jugadasel2.set(jugadas[0])

    lblp1=Label(winju, text="EQUIPO ROJO", font="Arial", bg="red", fg="white").place(x=145,y=400)
    lblp2=Label(winju, text="EQUIPO AZUL", font="Arial", bg="navy", fg="white").place(x=540,y=400)

    cmbjug1=OptionMenu(winju, jugadasel1, *jugadas).place(x=155,y=450)
    cmbjug2=OptionMenu(winju, jugadasel2, *jugadas).place(x=550,y=450)
    
    def juego():
        winju.withdraw()
        venjuego=Toplevel()
        global goloc
        global golvis

        venjuego.geometry("705x600+350+20")
        lblcad=Label(venjuego, text="Ingresa la cadena: ", font="Arial").place(x=280, y=90)
        lbllocal=Label(venjuego, text="EQUIPO ROJO", font="Arial", bg="red", fg="white").place(x=180, y=30)
        lblvisita=Label(venjuego,text="EQUIPO AZUL", font="Arial", bg="navy", fg="white").place(x=400, y=30)
        txtcadP1=Entry(venjuego, textvariable=cadena1).place(x=175, y=130)
        txtcadP2=Entry(venjuego, textvariable=cadena2).place(x=395, y=130)

        imggol1=PhotoImage(file="GOLROJO.png")
        imggol2=PhotoImage(file="GOLAZUL.png")   
        imgemp=PhotoImage(file="EMPATE.png")  
        imggr=PhotoImage(file="GANADORROJO.png")
        imgga=PhotoImage(file="GANADORAZUL.png")   

        def verificacion():   
            global goloc   
            global golvis
            global ganador
            global verif1
            global verif2
            
            if ganador!=1 and ganador!=2:
                if jugadasel1.get()=="Jugada 1":
                    btnverj1=Button(venjuego, text="VER JUGADA", command=verj1).place(x=90,y=127)
                    print(jugadasel1.get())
                    print(cadena1.get())
                    lpal1=len(cadena1.get())
                    if cadena1.get() in lengreg1:
                        verif1=1
                        print("Cadena valida")
                    else:
                        print("cadena invalida")

                elif jugadasel1.get()=="Jugada 2":
                    btnverj1=Button(venjuego, text="VER JUGADA", command=verj2).place(x=90,y=127)
                    print(jugadasel1.get())
                    print(cadena1.get())
                    lpal1=len(cadena1.get())
                    if cadena1.get() in lengreg2:
                        verif1=1
                        print("Cadena valida")
                    else:
                        print("cadena invalida")

                if jugadasel2.get()=="Jugada 1":
                    btnverj1=Button(venjuego, text="VER JUGADA", command=verj1).place(x=525,y=127)
                    print(jugadasel2.get())
                    print(cadena2.get())
                    lpal2=len(cadena2.get())
                    if cadena2.get() in lengreg1:
                        verif2=1
                        print("Cadena valida")
                    else:
                        print("cadena invalida")

                elif jugadasel2.get()=="Jugada 2":
                    btnverj1=Button(venjuego, text="VER JUGADA", command=verj2).place(x=525,y=127)
                    print(jugadasel2.get())
                    print(cadena2.get())
                    lpal2=len(cadena2.get())
                    if cadena2.get() in lengreg2:
                        verif2=1
                        print("Cadena valida")
                    else:
                        print("cadena invalida")

                if verif1!=0 and verif2!=0:
                    if lpal1<lpal2:
                        goloc+=1
                        
                        mloc=Label(venjuego, text=goloc, font="Arial", bg="red", fg="white").place(x=310, y=30)             
                        lblgol1=Label(venjuego, image=imggol1).place(x=0 ,y=230)
                        if goloc==3:
                            ganador=1

                    elif lpal1>lpal2:        
                        golvis+=1

                        mvis=Label(venjuego, text=golvis ,font="Arial", bg="navy", fg="white").place(x=370, y=30)
                        lblgol2=Label(venjuego, image=imggol2).place(x=0 ,y=230)
                        if golvis==3:
                            ganador=2

                    elif lpal1==lpal2:
                        lblempa=Label(venjuego, image=imgemp).place(x=0, y=230)
                else:
                    messagebox.showwarning("ALERTA", "INGRESEN JUGADAS VALIDAS")        

            else:
                if ganador==1:
                    lblempa=Label(venjuego, image=imggr).place(x=0, y=230)
                    messagebox.showwarning("ALERTA", "EL GANADOR ES EL EQUIPO ROJO")
                if ganador==2:
                    lblempa=Label(venjuego, image=imgga).place(x=0, y=230)
                    messagebox.showwarning("ALERTA", "EL GANADOR ES EL EQUIPO AZUL")


        btncad=Button(venjuego, text="CONFIRMAR JUGADAS", command=verificacion).place(x=280, y=170)

    btnentrada=Button(winju, text="CONFIRMAR JUGADA",command=juego).place(x=300, y=500, width=200, height=30)
    
btnjugar=Button(ventana, text="JUGAR AHORA", command=abrirventanajuego).place(x=145,y=500, width=300, height=30)

ventana.mainloop()