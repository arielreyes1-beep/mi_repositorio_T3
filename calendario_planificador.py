import tkinter as tk
import calendar
from datetime import datetime

#ventana
ventana = tk.Tk()
ventana.title("calendario planificador de turnos")
ventana.config (bg= "lemon chiffon")
ventana.geometry("680x290")

#variables
fecha_actual = datetime.now()
mes = fecha_actual.month 
año = fecha_actual.year
calendario = calendar.Calendar() 
botones_dias = []
dias_seleccionados = []
ciclo_turnos = None
inicio_turno = None

#frames para la interfaz
frame_calendario = tk.Frame (ventana)
frame_calendario.grid (row=0, column= 1)
frame_texto = tk.Frame (ventana, bg= "lemon chiffon")
frame_texto.grid (row= 0, column= 0)
frame_botones = tk.Frame(ventana)
frame_botones.grid(row=1)
frame_leyenda = tk.Frame(frame_texto, bg="lemon chiffon")
frame_leyenda.pack(pady=10)

instrucciones_de_uso = tk.Label(frame_texto,
                                 text="Para definir un turno en este calendario planificador de turnos," \
                                 " basta con presionar el día de inicio del turno y el día en el que" \
                                 " finaliza el mismo. Luego de eso el propio calendario indicara los días" \
                                 " de trabajo y de descanso. ", font= ("arial", 13, "bold"), justify= "left",
                                 wraplength= 250, bg="darkseagreen", fg="snow", borderwidth= 5
                                 , relief="ridge")
instrucciones_de_uso.pack()

tk.Label(frame_leyenda, text="Días de trabajo", bg="khaki1",
         font=("arial", 10, "bold"), width=15, relief="ridge").grid(row=0, column=0, padx=5)
tk.Label(frame_leyenda, text="Días de descanso", bg="lightskyblue",
         font=("arial", 10, "bold"), width=15, relief="ridge").grid(row=0, column=1, padx=5)

#funciones
def mostrar_calendario():
    for widget in frame_calendario.winfo_children():
        widget.destroy()
    botones_dias.clear()

    nombre_mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    meses = tk.Label(frame_calendario, text=f"{nombre_mes[mes-1]} {año}", font=("arial", 15, "bold"),
                    fg="sea green", bg= "lemon chiffon", anchor= "center")
    meses.grid (row= 0, column= 0, columnspan=7, sticky= "ew")

    dias_semana = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
    for i, dia in enumerate(dias_semana):
            tk.Label(frame_calendario, text=dia).grid(row=1, column=i)
             
    dias_mes = calendario.monthdayscalendar(año, mes)
    for fila, semana in enumerate(dias_mes, start=2):
        for col, dia in enumerate(semana):
            if dia == 0:
                texto = ""
            else:
                texto = str(dia)
            boton = tk.Button(frame_calendario, text=texto, width=5, height=2,
                               command=lambda dia=texto: seleccionar_dia(dia))
            boton.grid(row=fila, column=col)
            botones_dias.append(boton)

    aplicar_turnos_mes(año, mes, botones_dias)

def aplicar_turnos_mes(año, mes, botones_mes):
     global ciclo_turnos, inicio_turno
     if not ciclo_turnos or not inicio_turno:
          return
     dias_chamba, dias_descanso = ciclo_turnos
     turno = dias_chamba + dias_descanso
     primer_dia_mes = datetime(año, mes, 1).timetuple().tm_yday

     for b in botones_mes:
        if b["text"] == "":
            continue
        dia_mes = int(b["text"])
        dia_del_año = primer_dia_mes + dia_mes - 1
        posicion = (dia_del_año - inicio_turno) % turno

        if posicion < dias_chamba:
             b.config(bg="khaki1")
        else:
             b.config(bg="lightskyblue") 

def turnos_mensuales(inicio, fin):
     global ciclo_turnos, inicio_turno, año, mes
     if inicio > fin:
          inicio, fin = fin, inicio
     dias_trabajo = fin - inicio +1
     dias_descanso = dias_trabajo
     ciclo_turnos = (dias_trabajo, dias_descanso)

     inicio_turno = datetime(año, mes, inicio).timetuple().tm_yday
     mostrar_calendario()

def seleccionar_dia(dia):
     if dia == "":
          return
     dias_seleccionados.append(int(dia))
     if len(dias_seleccionados) == 2:
          turnos_mensuales(dias_seleccionados[0], dias_seleccionados[1])
          dias_seleccionados.clear()

def mes_anterior():
     global mes, año
     mes -= 1
     if mes < 1:
          mes = 12
          año -= 1
     mostrar_calendario()

def mes_siguiente():
     global mes, año
     mes += 1
     if mes > 12:
          mes = 1
          año += 1
     mostrar_calendario()

def limpiar_calendario():
     global dias_seleccionados, ciclo_turnos, inicio_turno
     ciclo_turnos = None
     inicio_turno = None
     dias_seleccionados.clear()
     mostrar_calendario()

#cambio de meses y limpiar calendario
boton_anterior = tk.Button(frame_botones, text="mes anterior", command=mes_anterior, bg="darkseagreen"
                           , font=("arial", 10, "bold"), fg= "snow")
boton_anterior.grid(row=0, column=0)
boton_siguiente = tk.Button(frame_botones, text="mes siguiente", command=mes_siguiente, bg="darkseagreen"
                            , font=("arial", 10, "bold"), fg= "snow")
boton_siguiente.grid(row=0, column=1)
boton_limpiar_calendario = tk.Button(frame_botones, text="limpiar calendario", command= limpiar_calendario
                                     , bg="darkseagreen", font=("arial", 10, "bold"), fg= "snow") 
boton_limpiar_calendario.grid(row=0, column=2)


mostrar_calendario()
ventana.mainloop()