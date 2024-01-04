## Importar todas las librerias
from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk, Image
from tkinter import messagebox


import matplotlib

matplotlib.use ("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt

from backend import *


background = "#f0ddd5"
framebg = "#62a7ff"
framefg= "#fefbfb"

root=Tk()
root.title("Sistema de predicción de ataque al corazón")
root.geometry("1366x730+0+20")
root.resizable(False,False)
root.config(bg=background)


######## Analisis ###########################
def analisis():
    name= Name.get()
    D1=Date.get()
    today=datetime.date.today()
    A=today.year-DOB.get()

    try:
        B=selection()
    except:
        messagebox.showerror("Aviso","Por favor selecciona un genero")
        return
    
    try:
        F=selection2()
    except:
        messagebox.showerror("Aviso","Por favor selecciona fbs")
        return
    
    try:
        I=selection3()
    except:
        messagebox.showerror("Aviso","Por favor selecciona exang")
        return
    
    try:
        C=int(selection4())
    except:
        messagebox.showerror("Aviso","Por favor selecciona cp")
        return
    
    try:
        G=int(restecg_combobox.get())
    except:
        messagebox.showerror("Aviso","Por favor selecciona restcg")
        return
    
    try:
        K=int(selection5())
    except:
        messagebox.showerror("Aviso","Por favor selecciona slope")
        return
    
    try:
        L=int(ca_combobox.get())
    except:
        messagebox.showerror("Aviso","Por favor selecciona ca")
        return
    
    try:
        M=int(thal_combobox.get())
    except:
        messagebox.showerror("Aviso","Por favor selecciona thal")
        return
    
    try:
        D=int(trestbps.get())
        E=int(cole.get())
        H=int(thalach.get())
        J=int(oldpeak.get())
    except:
        messagebox.showerror("Aviso no hay datos","No hay datos de entrada")
        return
    
    print ("A es edad", A)
    print ("B es genero", B)
    print ("C es cp", C)
    print ("D es trestbps", D)
    print ("E es colesterol", E)
    print ("F es fbs", F)
    print ("G es restcg", G)
    print ("H es thalach", H)
    print ("I es Exang", I)
    print ("J es oldpeak", J)
    print ("K es slop", K)
    print ("L es ca", L)
    print ("M es thal", M)
    
    
########################## Primera grafica #######################

    f = Figure(figsize=(5,5), dpi=80)
    a= f.add_subplot(111)
    a.plot(["Sexo","fbs","exang"],[B,F,I])
    canvas = FigureCanvasTkAgg(f)
    canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH)
    canvas._tkcanvas.place(width=250,height=250, x=530,y=225)

    ########################## Segunda grafica #######################

    f2 = Figure(figsize=(5,5), dpi=80)
    a2= f2.add_subplot(111)
    a2.plot(["edad","trestbps","colesterol","thalach"],[A,D,E,H])
    canvas2 = FigureCanvasTkAgg(f2)
    canvas2.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas2._tkcanvas.place(width=250,height=250, x=795,y=225)

########################## Tercera grafica #######################

    f3 = Figure(figsize=(5,5), dpi=80)
    a3= f3.add_subplot(111)
    a3.plot(["Oldpeak","resticg","cp"],[J,G,C])
    canvas3 = FigureCanvasTkAgg(f3)
    canvas3.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas3._tkcanvas.place(width=250,height=250, x=530,y=470)

########################## Cuarta grafica #######################

    f4 = Figure(figsize=(5,5), dpi=80)
    a4= f4.add_subplot(111)
    a4.plot(["Slope","ca","thal"],[K,L,M])
    canvas4 = FigureCanvasTkAgg(f4)
    canvas4.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas4._tkcanvas.place(width=250,height=250, x=795,y=470)



####### Input data #######################
    input_data=(A,B,C,D,E,F,G,H,I,J,K,L,M)

    input_data_as_numpy=np.asanyarray(input_data)
    
    input_data_reshape=input_data_as_numpy.reshape(1,-1)

    prediction = model.predict(input_data_reshape)
    print(prediction[0])

    if (prediction[0]==0):
        print("Esta persona no tiene una enfermedad del corazón")
        reporte.config(text=f"Reporte: {0}",fg="#8dc63f")
        reporte1.config(text=f"{name}, no tiene una enfermedad del corazón")
    
    else:
        print("Esta persona tiene enfermedad del corazón")
        reporte.config(text=f"Reporte: {1}",fg="#ed1c24")
        reporte1.config(text=f"{name}, tiene una enfermedad del corazón")



### info window#############################################################
def Info():
    Icon_window= Toplevel(root)
    Icon_window.title("Info")
    Icon_window.geometry("700x600+350+100")

    # poner la imagen de icono 
    icon_image=PhotoImage(file ="C:\\Users\\Fernando\\Desktop\\Heart_atack\\Images\\info.png" )
    Icon_window.iconphoto(False,icon_image)

    #Heading
    Label(Icon_window,text="Información relacionada con el dataset", font="robot 20 bold").pack(padx=20, pady=20)


    # Info  (alt+shift+flechaabajo es para copiar todo una linea de codigo)
    Label (Icon_window,text="edad - edad en años",font="arial 11").place(x=20,y=100)
    Label (Icon_window,text="sexo - sexo (1 = Hombre; 0 = Mujer)",font="arial 11").place(x=20,y=130)
    Label (Icon_window,text="cp - Tipo de dolor en el pecho (0 = angina tipica; 1 = angina atipica; 2 = sin dolor angina; 3=asintomatico )",font="arial 11").place(x=20,y=160)
    Label (Icon_window,text="trestbps - presion arterial en reposos (en mm Hg)",font="arial 11").place(x=20,y=190)
    Label (Icon_window,text="cole - colesterol en suero en mg/dl",font="arial 11").place(x=20,y=220)
    Label (Icon_window,text="fbs -  azúcar en sangre > 120mg/dl (1=true;0=false)",font="arial 11").place(x=20,y=250)
    Label (Icon_window,text="restecg - resultados de electrocardigrama en reposo (0 = normal; 1 = Tiene ST-T; 2 = hipertrofia )",font="arial 11").place(x=20,y=280)
    Label (Icon_window,text="thalach - taza maxima del corazón",font="arial 11").place(x=20,y=310)
    Label (Icon_window,text="exang - ejercicios angina inducida (1 = yes;0 = no)",font="arial 11").place(x=20,y=340)
    Label (Icon_window,text="oldpeak - Depresión ST inducida por el segmento ST de ejercicio",font="arial 11").place(x=20,y=370)
    Label (Icon_window,text="slope - la pendiente del pico de ejercico señ segmento ST (0 = upsloping; 1= flat; 2=downsloping)",font="arial 11").place(x=20,y=400)
    Label (Icon_window,text="ca - número de vasos (0-3) coloreado por fluoroscopia",font="arial 11").place(x=20,y=430)
    Label (Icon_window,text="thal  0 = normal; 1 = fixed detect; 2 = reversible defect",font="arial 11").place(x=20,y=460)


    Icon_window.mainloop()

############## Usado para cerrar la ventana##########
def logout():
    root.destroy()

######## limpiar todo las celdas con un solo click
def Clear ():
    Name.get("")
    DOB.get("")
    trestbps.get("")
    cole.get("")
    thalach.set("")
    oldpeak.set("")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#Icon 1
#Ponerle doble slash para que python reconozca el comando
imagen_icon = PhotoImage(file="C:\\Users\\Fernando\\Desktop\\Heart_atack\\Images\\icon.png")
root.iconphoto(False,imagen_icon)

# Titulal de la seccion
logo = PhotoImage (file = "C:\\Users\\Fernando\\Desktop\\Heart_atack\\Images\\header.png")
myimagen= Label(image=logo,bg=background)
myimagen.place(x=0,y=0)


#<<<<<<frame3<<<<<<<<<<<<
heading_entry= Frame(root, width=800, height=190, bg="#df2d4b")
heading_entry.place(x=600, y=20)

Label(heading_entry, text="No. de registro", font= "arial 13", bg= "#df2d4b",fg=framefg).place(x=30,y=0)
Label(heading_entry, text="Fecha", font= "arial 13", bg= "#df2d4b",fg=framefg).place(x=430,y=0)

Label(heading_entry, text="Nombre del paciente", font= "arial 13", bg= "#df2d4b",fg=framefg).place(x=30,y=90)
Label(heading_entry, text="Año de nacimiento", font= "arial 13", bg= "#df2d4b",fg=framefg).place(x=430,y=90)


#<<<<<<<<<<<<<<<<<<<FALTA PONER LAS IMAGENES>>>>>>>>>>>>>>>>>>>>>>>>>>
entry_image=PhotoImage(file="C:\\Users\\Fernando\\Desktop\\Heart_atack\\Images\\Rounded Rectangle 1.png")    
entry_image2=PhotoImage(file="C:\\Users\\Fernando\\Desktop\\Heart_atack\\Images\\Rounded Rectangle 2.png")
Label(heading_entry, image=entry_image, bg="#df2d4b").place(x=20,y=30)
Label(heading_entry, image=entry_image, bg="#df2d4b").place(x=405,y=30)

Label(heading_entry, image=entry_image2, bg="#df2d4b").place(x=20,y=120)
Label(heading_entry, image=entry_image2, bg="#df2d4b").place(x=405,y=120)

# El siguiente comando sirve para poder introducir datos donnde se especifica
Registration = IntVar()
reg_entry= Entry(heading_entry,textvariable=Registration, width=30, font="arial 15", bg="#0e5363",fg="white", bd=0)
reg_entry.place(x=30,y=45)

Date= StringVar()
today = date.today()
d1=today.strftime("%d/%m/%Y")
date_entry=Entry(heading_entry, textvariable=Date,width=15, font="arial 15", bg="#0e5363", fg="white",bd=0 )
date_entry.place(x=430,y=45)
Date.set(d1)


Name = StringVar()
name_entry= Entry(heading_entry,textvariable=Name, width=20, font="arial 15", bg="#ededed",fg="#222222", bd=0)
name_entry.place(x=30,y=135)

DOB = IntVar()
dob_entry= Entry(heading_entry,textvariable=DOB, width=20, font="arial 15", bg="#ededed",fg="#222222", bd=0)
dob_entry.place(x=430,y=135)


#################################################### Body ################################################ 4 

Detail_entry = Frame(root, width=490, height=260, bg="#dbe0e3")
Detail_entry.place(x=30,y=450)


################################# Radio button ##########################################################3 5
Label (Detail_entry, text= "sexo:", font="arial 13", bg=framebg, fg=framefg).place(x=10,y=10)
Label (Detail_entry, text= "fbs:", font="arial 13", bg=framebg, fg=framefg).place(x=180,y=10)
Label (Detail_entry, text= "exang:", font="arial 13", bg=framebg, fg=framefg).place(x=335,y=10)


def selection():
    if gen.get()==1:
        Gender=1
        return(Gender)
        print(Gender)
    elif gen.get()==2:
        Gender=0
        return(Gender)
        print(Gender)
    else:
        print(Gender)


def selection2():
    if fbs.get()==1:
        Fbs=1
        return(Fbs)
        print(Gender)
    elif fbs.get()==2:
        Fbs=0
        return(Fbs)
        print(Fbs)
    else:
        print(Fbs)

def selection3():
    if exang.get()==1:
        Exang=1
        return(Exang)
        print(Exang)
    elif exang.get()==2:
        Exang=0
        return(Exang)
        print(Exang)
    else:
        print(Exang)

gen = IntVar()
R1= Radiobutton(Detail_entry, text= "Hombre", variable=gen, value=1, command=selection)
R2= Radiobutton(Detail_entry, text= "Mujer", variable=gen, value=2, command=selection)
R1.place(x=53, y=10)
R2.place(x=120,y=10)

fbs = IntVar()
R3= Radiobutton(Detail_entry, text= "Verdad", variable=fbs, value=1, command=selection2)
R4= Radiobutton(Detail_entry, text= "Falso", variable=fbs, value=2, command=selection2)
R3.place(x=213, y=10)
R4.place(x=273,y=10)

exang = IntVar()
R5= Radiobutton(Detail_entry, text= "Si", variable=exang, value=1, command=selection3)
R6= Radiobutton(Detail_entry, text= "No", variable=exang, value=2, command=selection3)
R5.place(x=387, y=10)
R6.place(x=430,y=10)


################################## Combobox ###############################  6
Label(Detail_entry, text="cp", font="arial 13", bg=framebg, fg=framefg).place(x=10,y=50)
Label(Detail_entry, text="restecg", font="arial 13", bg=framebg, fg=framefg).place(x=10,y=90)
Label(Detail_entry, text="slope", font="arial 13", bg=framebg, fg=framefg).place(x=10,y=130)
Label(Detail_entry, text="ca:", font="arial 13", bg=framebg, fg=framefg).place(x=10,y=170)
Label(Detail_entry, text="thal:", font="arial 13", bg=framebg, fg=framefg).place(x=10,y=210)

def selection4():
    input=cp_combobox.get()
    if input=="0 = angina tipica":
        return(0)
    elif input=="1 = angina atipica":
        return(1)
    elif input == "2 = sin dolor angina":
        return(2)
    elif input =="3=asintomatico ":
        return(3)
    else:
        print(Exang)

def selection5():
    input=slope_combobox.get()
    if input=="0 = upsloping":
        return(0)
    elif input=="1= flat":
        return(1)
    elif input == "2=downsloping":
        return(2)
    else:
        print(Exang)



cp_combobox=Combobox(Detail_entry, values=["0 = angina tipica", "1 = angina atipica", "2 = sin dolor angina", "3=asintomatico "],font="arial 12",state="r",width=14)
restecg_combobox=Combobox(Detail_entry, values=["0", "1", "2"],font="arial 12",state="r",width=11)
slope_combobox=Combobox(Detail_entry, values=["0 = upsloping", "1= flat", "2=downsloping"],font="arial 12",state="r",width=12)
ca_combobox=Combobox(Detail_entry, values=["0","1","2","3","4"],font="arial 12",state="r",width=14)
thal_combobox=Combobox(Detail_entry, values=["0 ", "1", "2"],font="arial 12",state="r",width=14)

cp_combobox.place(x=50,y=50)
restecg_combobox.place(x=80,y=90)
slope_combobox.place(x=70,y=130)
ca_combobox.place(x=50,y=170)
thal_combobox.place(x=50,y=210)


##################### Data entry box  #########################3 7
Label (Detail_entry, text="Fumador:", font = "arial 13", width=8, bg="#dbe0e3",fg="black").place(x=240,y=50)
Label (Detail_entry, text="trestbps", font = "arial 13", width=8, bg=framebg,fg=framefg).place(x=240,y=90)
Label (Detail_entry, text="colesterol", font = "arial 13", width=8, bg=framebg,fg=framefg).place(x=240,y=130)
Label (Detail_entry, text="thalach", font = "arial 13", width=8, bg=framebg,fg=framefg).place(x=240,y=170)
Label (Detail_entry, text="oldpeak", font = "arial 13", width=8, bg=framebg,fg=framefg).place(x=240,y=210)


trestbps=StringVar()
cole=StringVar()
thalach=StringVar()
oldpeak=StringVar()

trestbps_entry=Entry(Detail_entry,textvariable=trestbps,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
cole_entry=Entry(Detail_entry,textvariable=cole,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
thalach_entry=Entry(Detail_entry,textvariable=thalach,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
oldpeak_entry=Entry(Detail_entry,textvariable=oldpeak,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)

trestbps_entry.place(x=330,y=90)
cole_entry.place(x=330,y=130)
thalach_entry.place(x=330,y=170)
oldpeak_entry.place(x=330,y=210)
#############################################################################################################


############################### Reporte ################################ 8

imagen_reporte=PhotoImage(file="C:\\Users\\Fernando\\Desktop\\Heart_atack\\Images\\Report.png")
reporte_background =Label(image=imagen_reporte,bg=background)
reporte_background.place(x=1070,y=340)

reporte=Label(root,text="holi",font="arial 25 bold",bg="white", fg="#8dc63f")
reporte.place(x=1120,y=520)

reporte1= Label(root,text="holi",font="arial 10 bold",bg="white")
reporte1.place(x=1100,y=570)

#######################################################################################


################################### Grafica ####################################### 9
grafica_imagen=PhotoImage(file="C:\\Users\\Fernando\\Desktop\\Heart_atack\\Images\\graph.png")
Label(image=grafica_imagen).place(x=540,y=270)
Label(image=grafica_imagen).place(x=780,y=270)
Label(image=grafica_imagen).place(x=540,y=500)
Label(image=grafica_imagen).place(x=780,y=500)



########################### Boton ####################  10

boton_analisis= PhotoImage(file="C:\\Users\\Fernando\\Desktop\\Heart_atack\\Images\\Analysis.png")
Button(root,image=boton_analisis, bd=0,bg=background, cursor="hand2",command=analisis).place (x=1085,y=240)

############################# Info button ########################
boton_info= PhotoImage(file="C:\\Users\\Fernando\\Desktop\\Heart_atack\\Images\\info.png")
Button(root,image=boton_info, bd=0,bg=background, cursor="hand2",command= Info).place (x=10,y=240)


############################# Save button ########################
boton_save= PhotoImage(file="C:\\Users\\Fernando\\Desktop\\Heart_atack\\Images\\save.png")
Button(root,image=boton_save, bd=0,bg=background, cursor="hand2").place (x=1300,y=250)

############################# boton de fumador y no fumador ######################## 11
button_mode=True
choice= "Fumador"

def changemode():
    global button_mode
    global choice
    if button_mode:
        choice = "No fumador"
        mode.config(image=no_fumador_icon,activebackground="white")
        button_mode=False
    else:
        choice = "Fumador"
        mode.config(image=fumador_icon,activebackground="white")
        button_mode=True

    print(choice)

fumador_icon=PhotoImage(file="C:\\Users\\Fernando\\Desktop\\Heart_atack\\Images\\smoker.png")
no_fumador_icon=PhotoImage(file="C:\\Users\\Fernando\\Desktop\\Heart_atack\\Images\\non-smoker.png")
mode=Button(root,image=fumador_icon,bg="#dbe0e3",bd=0,cursor="hand2",command=changemode)
mode.place(x=370,y=495)



################################## Logout button ####################################### 12

logout_icon=PhotoImage(file="C:\\Users\\Fernando\\Desktop\\Heart_atack\\Images\\logout.png")
logout_boton= Button(root, image=logout_icon,bg="#df2d4b", cursor="hand2",bd=0,command=logout)
logout_boton.place(x=1300,y=5)


###############################################################################################


root.mainloop()

## info window (boton info)<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



