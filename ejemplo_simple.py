import os

#Crear una carpeta si no existe
carpeta = "NuevaCarpeta"
if not os.path.exists(carpeta):
    os.makedirs(carpeta)
    print(f"Carpeta '{carpeta}' creada.")
else: 
    print(f"La carpeta '{carpeta}' ya existe.") 