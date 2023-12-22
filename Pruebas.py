
'''AQUI ABAJO LO RESOLVI SIN FUNCIONES'''
usuario = "LibroCuentas.txt"
with open(usuario,"r") as file:
        lista = file.readlines()
        
        with open("PAGADO.txt","w") as file:
            for i in lista:
                if "PAGADO" in i:
                    file.write(f"{i}")