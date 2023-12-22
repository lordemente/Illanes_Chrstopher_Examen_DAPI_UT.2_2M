dicconario = {}
while True:
    tiempo = input("Ingresa el hora de la carrera: ")
    km = input("Ingresa el kilometro que se encuentra: ")
    
    dicconario[tiempo] = km
    
    final_carrera = input("Si ya acabo la carrera escriba 'yes o no'").lower()
    
    if final_carrera == "yes":
        for time, distance  in dicconario.items():
            print(f"El corredor a las {time} estaba en el km {distance}")
        break
    else:
        print("Sigue adelante")
        


    
        
        
    
    