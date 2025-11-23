import tkinter as tk

ventana = tk.Tk()
ventana.title("calculadora")
ventana.configure(bg="darkgrey")
numero_a = 0
numero_b = 0
operacion = "sumar"
resultado = 0
imagen_tk = None

espacio_util = tk.Frame(ventana, width= 300, height= 100)
espacio_util.grid(row=0, column=0, columnspan=5, pady=10)
espacio_util.grid_propagate(False)

#definir la operacion a realizar
def multiplicar():
    global numero_a, numero_b
    return numero_a * numero_b

def dividir():
    global numero_a, numero_b
    return numero_a / numero_b

def sumar():
    global numero_a, numero_b
    return numero_a + numero_b

def restar():
    global numero_a, numero_b
    return numero_a - numero_b

def borrar():
    pantalla.config(image="", text="")
    pantalla.image = None
    
def mostrar_en_pantalla(valor):
    texto_actual = pantalla.cget("text")
    pantalla.config(text=texto_actual + str(valor))

def seleccionar_operacion(simbolo):
   global numero_a, operacion

   numero_a = float(pantalla.cget("text"))
   print(numero_a)
   pantalla.config(text="")
   operacion = simbolo
   print(operacion)


def resultado_final():
    global operacion, numero_a, numero_b, resultado, imagen_tk
    
    numero_b = float(pantalla.cget("text"))
    print (numero_b)
    pantalla.config(text="")
    if operacion == "+":
        resultado = numero_a + numero_b
    elif operacion == "-":
        resultado = numero_a - numero_b
    elif operacion == "*":
        resultado = numero_a * numero_b
    elif operacion == "/":
        if numero_b == 0:
            pantalla.config(text = "imposible mi loco")  
            return
        resultado = numero_a / numero_b
    else:
        resultado = "Error"

    pantalla.config(text=str(resultado))

    if resultado == 2:
        imagen_tk = tk.PhotoImage(file="jerry.png")
        pantalla.config(image=imagen_tk, text="", compound="center")
        pantalla.image = imagen_tk


#pantalla de la calculadora
pantalla = tk.Label(espacio_util, bg="white", anchor="e", font=("Arial", 20))
pantalla.pack(fill="both", expand=True)

#listas para botones
botones_pf = [7, 8, 9]
botones_sf = [4, 5, 6]
botones_tf = [1, 2, 3]

#botones 
for i, numero in enumerate(botones_pf):
    boton = tk.Button(
        ventana,
        text=str(numero),
        font= ("Arial",12),
        width= 8,
        command=lambda n=numero: mostrar_en_pantalla(n)
    )
    boton.grid(row=1, column=i, padx=10, pady=10)

for i, numero in enumerate(botones_sf):
    boton = tk.Button(
        ventana,
        text=str(numero),
        font= ("Arial",12),
        width= 8,
        command=lambda n=numero: mostrar_en_pantalla(n)
    )
    boton.grid(row=2, column=i, padx=10, pady=10)

for i, numero in enumerate(botones_tf):
    boton = tk.Button(
        ventana,
        text=str(numero),
        font= ("Arial",12),
        width= 8,
        command=lambda n=numero: mostrar_en_pantalla(n)
    )
    boton.grid(row=3, column=i, padx=10, pady=10)

boton_0 = tk.Button(ventana,text="0",font= ("Arial",12), width= 8, command=lambda: mostrar_en_pantalla(0))
boton_0.grid(row=4,column=0, padx=10, pady=10)

boton_decimal = tk.Button(ventana,text=".",font= ("Arial",12,"bold"),bg="red", fg= "white", width= 8, command=lambda: mostrar_en_pantalla("."))
boton_decimal.grid(row=4,column=1, padx=10, pady=10)

boton_igual = tk.Button(ventana,text="=",font= ("Arial",12,"bold"),bg="red", fg= "white", width= 8, command= resultado_final)
boton_igual.grid(row=4,column=2, padx=10, pady=10)

boton_multiplicacion = tk.Button(ventana,text="×",font= ("Arial",12,"bold"), bg="red", fg= "white", width= 5, command=lambda: seleccionar_operacion ("*"))
boton_multiplicacion.grid(row=1,column=i+1, padx=10, pady=10)

boton_division = tk.Button(ventana,text="÷",font= ("Arial",12,"bold"),bg="red", fg= "white", width= 5, command= lambda: seleccionar_operacion ("/"))
boton_division.grid(row=2,column=i+1, padx=10, pady=10)

boton_suma = tk.Button(ventana,text="+",font= ("Arial",12,"bold"),bg="red", fg= "white", width= 5, command= lambda: seleccionar_operacion ("+"))
boton_suma.grid(row=3,column=i+1, padx=10, pady=10)

boton_resta = tk.Button(ventana,text="-",font= ("Arial",12,"bold"),bg="red", fg= "white", width= 5, command= lambda: seleccionar_operacion ("-"))
boton_resta.grid(row=4,column=i+1, padx=10, pady=10)

boton_borrar = tk.Button(ventana,text="⌫",font= ("Arial",12,"bold"),bg="black", fg= "white", width= 4, command=borrar)
boton_borrar.grid(row=1, column=4)


ventana.mainloop()