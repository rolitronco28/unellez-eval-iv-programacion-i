"""
Librerias en uso:

platform : Para comprobar que SO (Sistema operativo) esta en uso. Se usa en -> _clear()
os :  Para usar comandos que esten presentes en el sistema operativo en el que se ejecute este script. Usado en -> _clear()
time : Integrado en Python. Utilizado para marcar tiempos de espera en algunas funciones.
"""
import os
import platform
import time

# Variables de entorno globales
nombre_de_usuario = ""
id_usuario = ""
saldo_usuario = 0.0
operaciones = []
temp_l_id = [] # Utilizada temporalmente en -> _registro(). Separa lo ingresado por el usuario para comprobar si posee un tipado correcto.

# Clientes. Orden = 0 > Nombre. 1 > CI/ID
cli_edd = ["Edduard Tapia", "32.305.750"]
cli_mary = ["Marysabel Gonzalez", "14.408.200"]

# "Libreta" de contactos
contactos = [cli_edd, cli_mary]

# FUNCIONES VARIAS
def _clear():
  # Para limpiar la pantalla. Comprobamos si el SO donde trabajamos es Windows o, en su defecto, otro.
  if platform == "Windows": 
    os.system("cls")
  else:
    os.system("clear")

def clear_historial():
  # Pregunta si el usuario desea borrar el historial de acciones.
  global operaciones
  
  pregunta = input(f"\nEsta seguro de limpiar el historial? (Esta accion no es reversible).\n(s/n): ")

  if pregunta == "s":
    operaciones = []
    operaciones.append("Limpieza de historial...")
    print("* Se ha limpiado el historial de acciones correctamente.")
  else:
    print("* Se ha cancelado la operacion.")
    
  input(f"\nPresione [ENTER] para continuar.")

def bad_id():
  # Guarda lo que ocurre al ingresar de manera erronea los datos de C.I. en -> _registro()
  global id_usuario
  global temp_l_id
  print(f"\n* C.I. Invalida. Intente usar el patron mas similar al que le pertenece: ")
  print("X.XXX.XXX o XX.XXX.XXX")
  print(f"* Recuerde hacer uso de puntos (.) y respetar el orden.\n")

  id_usuario = input("Ingrese su identificador (C.I.): ")
  temp_l_id = id_usuario.split(".")

def mostrar_contactos():
  # Mostrar contactos. Usado en -> _trans_otro(), menu_cuenta()
  print(f"\n=== Contactos registrados ===\n")
  for i in contactos:
    print(f"* {i[0]} -> {i[1]}")

def _inicio():
  print(f"=== UNELLEZ : Ingenieria Informatica III ===\n=== Algoritmos y programacion I : Evaluacion final, Modulo IV ===\n\nAlumnos:\nYainer Alfonso Ramirez Gonzalez (C.I.: 29.681.766)\nEdduar Orlando Tapia Urbina (C.I.: 32.305.750)\n\n* Descripcion general: El siguiente programa, cuyas instrucciones fueron\notorgadas por el profesor Ing. Dick Diaz, intenta simular de manera sencilla\ny directa un gestor de cuentas bancarias. Cuenta con apartados que van\ndesde gestionar la sesion actual, hasta transferir, guardar contactos\nretirar al saldo actual y elementos esenciales.\n\n* 'Si puedes imaginarlo, puedes programarlo'\n- Alejandro Taboada Sanchez. (2019)\n\nGuasdualito, Edo. Apure, Julio del 2026.")
  print(f"\nNOTA: Programa sujeto a errores. No se hace uso de varias funciones importantes \npara evitarlos. (Requisito impuesto por conocimientos generales)")
  input(f"\nPresione [ENTER] para continuar.")
  _clear()

# Funciones importantes. El programa "Inicia" desde aqui.
def _registro():
  # Funcion de registro. Hace mencion a algunas variables globales.
  global nombre_de_usuario
  global id_usuario
  global temp_l_id

  # Ingreso de nombre de usuario y comprobacion de que la cantidad de caracteres sea mayor a 3.
  nombre_de_usuario = input("Ingrese su nombre: ")
  while len(nombre_de_usuario) < 3:
    print(f"* Nombre de usuario demasiado corto! Se admiten solo nombres con mas de 3 caracteres.\n")
    nombre_de_usuario = input("Ingrese su nombre: ")
    if len(nombre_de_usuario) > 3:
      break
    else:
      pass

  # Ingreso de C.I. y comprobacion de que cuente con un tipado correcto. Codigo reutilizado mas adelante en -> _trans_otro()
  id_usuario = input("Ingrese su identificador (C.I.): ")
  temp_l_id = id_usuario.split(".")
  
  while True:      
    if len(temp_l_id) == 3:
      if (int(temp_l_id[0]) > 0 and int(temp_l_id[0]) <= 37) and len(temp_l_id[1]) == 3 and len(temp_l_id[2]) == 3:
        break
      else:
        bad_id()
    else:
      bad_id()
      
  print(f"\n* Registro completado...")
  time.sleep(3)

def menu_main():
  # Menu principal. Guarda el acceso a otros menus.
  _clear()
  print(f"=== Menu Principal ===\n\n1. Cuenta.\n2. Depositar.\n3. Retirar.\n4. Transferencia.\n0. Salir.\n")
  cmd = int(input("Opcion a realizar: "))
  if cmd == 0:
    exit()
  elif cmd == 1:
    menu_cuenta()
  elif cmd == 2:
    _depositar()
  elif cmd == 4:
    _transferencia()
  elif cmd == 3:
    _retiro()

def menu_cuenta():
  # Menu en el que se pueden acceder a diferentes propiedades de la sesion actual.
  global operaciones
  global contactos

  _clear()
  
  print(f"=== Cuenta ===\n\n1. Ver datos.\n2. Re-Registro.\n3. Limpiar historial de acciones.\n4. Ver contactos.\n5. Ir atras.\n")
  cmd = int(input("Opcion a realizar: "))
  
  if cmd == 5:
    menu_main()
  elif cmd == 1:
    print('=' * 32)

    if saldo_usuario < 0:
      print(f"* Deuda pendiente.\n")
    
    print(f"Nombre: {nombre_de_usuario}\nID: {id_usuario}\nSaldo: {saldo_usuario:.2f}\n")
    q = input("Mostrar operaciones realizadas? (s/n): ")
    if q == "s":
      print('=' * 32)
      if len(operaciones) >= 1:
        for i in operaciones:
          print("*",i)
      else:
        print("* No se han realizado operaciones.")
    else:
      pass

    print('=' * 32)
    input("Presione [ENTER] para continuar.")
  elif cmd == 2:
    _registro()
  elif cmd == 3:
    if len(operaciones) >= 1:
      clear_historial()
    else:
      print(f"* ERROR: No hay operaciones por limpiar.\n")
      input("Presione [ENTER] para continuar.")
  elif cmd == 4:
    mostrar_contactos()
    
    input(f"\nPresione [ENTER] para continuar.")
    menu_cuenta()

def _depositar():
  # Menu de deposito...
  global saldo_usuario
  global operaciones
  
  _clear()
  print(f"=== Deposito ===")
  print(f"\nIngrese un valor numerico.\n")
  deposito = float(input("Deposito de: "))
  if deposito < 0:
    print(f"* Valor invalido... Ingrese un valor mayor a 0.")
    input("Presione [ENTER] para continuar.")
  else:
    operacion = f"Deposito -> +{deposito}"
    operaciones.append(operacion)
    saldo_usuario += deposito
    print(f"* Deposito completado...")
    time.sleep(3)
    return

def _trans_otro():
  # 2da opcion en -> _transferencia()
  global saldo_usuario
  global contactos
  global operaciones

  todo_bien: False # Variable local para comprobar si el proceso va por orden.

  print(f"\n* Saldo actual: {saldo_usuario}\n")
  transferir_a = input("Ingrese el C.I. al que va a transferir: ")
  temp = transferir_a.split(".")

  # Comprobacion de tipado de C.I. Mencionado en _registro()
  while True:      
    if len(temp) == 3:
      if (int(temp[0]) > 0 and int(temp[0]) <= 37) and len(temp[1]) == 3 and len(temp[2]) == 3:
        todo_bien = True
        break
      else:
        todo_bien = False
        break
    else:
      todo_bien = False
      break

  if todo_bien:
    alias_1 = input(f"\nLe gustaria guardar este contacto? (s/n): ")
    if alias_1 == "s":
      alias_2 = input("Alias del nuevo contacto: ")
      if len(alias_2) > 3:
        contactos.append([alias_2, transferir_a])
        operaciones.append(f"Contacto guardado -> '{alias_2}'")
        print(f"* Contacto guardado correctamente!\n")
      else:
        print(f"* ERROR: El alias indicado debe ser mayor a 3 caracteres.")
    else:
      print(f"* Si la transferencia es exitosa, el C.I. indicado quedara guardado en el historial de acciones.\n")

    monto = float(input("Monto a transferir: "))
    if monto > saldo_usuario:
      print("* ERROR: El monto indicado es mayor a su saldo actual!")
    elif monto <= 0:
      print("* ERROR: Monto menor o igual a 0.")
    else:
      # Comprobacion de porcentaje de comision. Reutilizado en _trans_otro()
      comision = 0.0
      
      if monto > 200:
        comision = 30
      elif monto > 100:
        comision = 15
      elif monto > 50:
        comision = 10
      else:
        comision = 0

      if comision > 0:
        saldo_usuario -= monto + (monto * comision/100)
        operaciones.append(f"Transferencia a {transferir_a} -> -{monto} + {comision}% por comison. (-{(monto + (monto * comision/100)):.2f} En total.)")
      else:
        saldo_usuario -= monto
        operaciones.append(f"Transferencia a {transferir_a} -> -{monto}")
      
      print(f"* Transferencia realizada correctamente.")
  else:
    print(f"* ERROR: Indicaste un C.I. valido?")

  input(f"\nPresione [ENTER] para continuar.")
  _transferencia()

def _trans_contacto():
  # 1ra opcion en -> _transferencia()
  global saldo_usuario
  global contactos
  global operaciones

  coincidencia: bool # Variable que comprueba si hay coincidencias entre el C.I. tipado por el usuario y los contactos registrados. 
  
  print(f"\n* Saldo actual: {saldo_usuario}")
  mostrar_contactos()

  _ta = input(f"\nIngrese el C.I. del contacto a transferir: ")
  _match = ""

  # Buscar coincidencias. Realizar la transferencia si existe. No realizar si no la hay.
  for i in contactos:
    if _ta == i[1]:
      coincidencia = True
      break
    else:
      coincidencia = False
      
  if coincidencia:
    print(f"* Contacto registrado!\n")
    monto = float(input("Ingrese el monto a transferir: "))
    
    if monto > saldo_usuario:
      print(f"* ERROR: El monto que ha indicado supera su saldo actual!\n")
      input("Presione [ENTER] para continuar.")
    elif monto <= 0:
      print(f"ERROR: Monto menor o igual a 0.\n")
      input("Presione [ENTER] para continuar.")
    else:
      # Comprobacion de porcentaje de comision. Reutilizado en _trans_otro()
      comision = 0.0
      
      if monto > 200:
        comision = 30
      elif monto > 100:
        comision = 15
      elif monto > 50:
        comision = 10
      else:
        comision = 0
        
      if comision > 0:  
        saldo_usuario -= monto + (monto * comision/100)
        operaciones.append(f"Transferencia a {_ta} -> -{monto} + {comision}% por comision (-{(monto + (monto * comision/100)):.2f} En total)")
      else:
        saldo_usuario -= monto
        operaciones.append(f"Transferencia a {_ta} -> -{monto}")
        
      print(f"* Transferencia realizada correctamente!\n")
      input("Presione [ENTER] para continuar.")
      
  else:
    print(f"* Contacto no registrado. Indico su C.I correctamente?\n")
    input("Presione [ENTER] para continuar.")
    _transferencia()
      
  # Volver al menu inicial < Este parte de _transferencia()
  _transferencia()

def _transferencia():
  # Menu de transferencias... Muestra 2 opciones.
  global saldo_usuario
  _clear()
  print(f"=== Transferecia ===")
  
  if saldo_usuario <= 0:
    print(f"\nSu saldo actual es menor o igual a 0, por lo que no puede realizar una transferencia.")
    input(f"\nPresione [ENTER] para regresar.")
    return
  else:  
    print(f"\n1. Transferir a un contacto.\n2. Transferir a otro.\n3. Ir atras.\n")
    cmd = int(input("Opcion a realizar: "))
  
  if cmd == 3:
    menu_main()
  elif cmd == 1:
    _trans_contacto()
  elif cmd == 2:
    _trans_otro()

def _retiro():
  # Menu de retiros...
  global saldo_usuario
  global operaciones
  
  _clear()
  print(f"=== Retirar ===\n")
  monto = float(input("Ingrese el monto a retirar: "))

  if monto > saldo_usuario:
    print(f"* ERROR: El monto ingresado es mayor a su saldo actual.\n")
  elif monto <= 0:
    print(f"* ERROR: El monto ingresado es menor o igual a 0.\n")
  else:
    saldo_usuario -= monto
    operaciones.append(f"Retiro -> -{monto}")
    print(f"* Retiro realizado con exito!\n")

  input("Presione [ENTER] para continuar")

# Inicio del programa.
_inicio()
_registro()

while True:
  menu_main()

