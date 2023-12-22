def leerDocument(Ruta_fichero):
    '''Lee la información de un fichero y lo guarda en una variable del
    tipo lista cada dato de la lista será una línea
            PARAMETRO:
                    RUTA ---> "Acceder con el nombre de la ruta" '''
                    
    with open(Ruta_fichero,"r") as file:
        lista = file.readlines()
        return lista



def IdentificadorPagado(lista):
        ''' Recibe una lista como parámetro de entrada la función 
                crea un fichero llamado "PAGADO.txt" donde se 
                escribiran todas las lineas donde en la lista de 
                entrada aparece la palabra "PAGADO" '''
        
       
        with open("PAGADO.txt","w") as file:
                for i in lista:
                        if "PAGADO" in i:   
                                file.write(f"{i}")
       
       
                                               
ruta = "LibroCuentas.txt"  

lista = leerDocument(ruta)
print(lista)

print(IdentificadorPagado(lista))
                        
                        
                        
                        
                
                
