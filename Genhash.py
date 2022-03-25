""" Este código representa el funcionamiento del encriptado en mensajes que se envían a traves de la redes
de telecomunicaciones. Los códigos de encriptación utilizados en este algoritmo son SHA256 y SHA512. Ademas, 
se realiza un código que permite almacenar los datos enviados en un HMAC permitiendo una mayor integridad en 
los datos. También se simula qué sucedería cuando se modifican los datos enviados, comprobando así la efectividad 
de la integridad mencionada anteriormente mediante HMAC. """

import hashlib   # biblioteca de generacion de hash
import hmac      # biblioteca de hmac
import os        # modulo para limpiar la consola

# declaramos la función que realizará los cálculos de HMAC
def keycod(clave,msj):
    encodedkey=str.encode(clave)
    #print("Clave codificada: \n", encodedkey)
    hmac1=hmac.new(encodedkey,msj.encode('utf-8'),hash)
    valor_hmac=hmac1.digest()
    #print('Valor HMAC: \n', valor_hmac)
    valor_hex=hmac1.hexdigest()
    print('Valor HMAC en Hexadecimal: \n', valor_hex)
    print('Tamaño del valor HMAC en bits: ', 8*hmac1.digest_size)

# declaramos la función que calcule el hash de 256 y 512 bits
def fun_sha(q,msj):
    # si q=1 calculamos el SHA256 y si q=2 entonces calculamos el SHA512
    if q == 1:
        msj_cif=hashlib.sha256(msj.encode('utf-8'))
        print('Hash del mensaje: \n', msj_cif.hexdigest())
    else:
        msj_cif=hashlib.sha512(msj.encode('utf-8'))
        print('Hash del mensaje: \n', msj_cif.hexdigest())

# función que llama a las funciones fun_sha y keycod
def opcion(q,clave,msj):
    global hash # declaramos la variable hash como global para ser utilizada en otras funciones
    if q == 1:
        hash=hashlib.sha256
        a = fun_sha(q,msj)     # llamamos a la función que genera SHA256
        b = keycod(clave,msj)  # llamamos a la función que calcula el HMAC
        return a, b
    elif q == 2:
        hash=hashlib.sha512
        a = fun_sha(q,msj)     # llamamos a la función que genera SHA512
        b = keycod(clave,msj)  # llamamos a la función que calcula el HMAC
        return a, b

# función que imprime los datos ingresados por el emisor
def impresiones():
    print("\n Introducir mensaje: \n")
    mensaje2 = input()
    print("\n Introducir clave: \n")
    key2 = input()
    opcion(n,key2,mensaje2)
    input()

# Programa principal
z=0
while z<1:    # mensaje de bienvenida para el usuario
    print("\n Bienvenidos a la demo de Criptografía Simétrica")
    print("\n Por favor elige una opción:")
    print("1- Emisor")
    print("2- Receptor")
    print("3- Hackear")
    print("4- Terminar Programa")
    m = int(input())

    if m == 1:         # operaciones realizadas para el Emisor 
        x=0
        while x<1:
            print("\n Elegir el tipo de hash a utilizar")
            print("1- SHA256")
            print("2- SHA512")
            print("3- Regresar")
            print("")
            n = int(input())  

            if n != 3:
                print("\n Introducir mensaje: \n")
                mensaje = input()
                print("Introducir clave: \n")
                key = input()
                print('\n Mensaje ingresado:', mensaje)
                opcion(n,key,mensaje)
                x = 1
                # si el mensaje original no es modificado se mantendrá lo siguiente:
                mensaje3 = mensaje 
                input()
                os.system("cls")
            else:
                x = 1
                input()

    elif m == 2:         # operaciones realizadas para el Receptor 
        if mensaje3 == mensaje: # si el mensaje original no se modificó
            print('\n Mensaje recibido: \n', mensaje)
            opcion(n,key,mensaje)
            impresiones()
        else: # si el mensaje original fue cambiado se realizan distintas opciones
            print('\n Mensaje recibido: \n', mensaje3)
            fun_sha(n,mensaje3)
            keycod(key,mensaje)
            impresiones()

    elif m == 3:         # operaciones realizadas para el Hackeo
        print('\n Mensaje recibido: \n', mensaje)
        opcion(n,key,mensaje)
        print("\n Ingresar mensaje modificado:")
        mensaje3 = input()
        input()
        os.system("cls")
    else:         # si no se desea ninguna opción se termina el programa
        z=1
        print("\n Programa terminado")
        os.system("cls")
