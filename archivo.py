def crear_archivo():
    file=open("data.xml","w")
    file.close()
    
def escribir_archivo():
    file=open("data.xml","a")
    file.write("ronal jose\n")    
    file.write("3008934411\n")
    file.write("Santamarta\n")
    
def leer_archivos():
    file=open("data.xml","r")
    linea=file.readline()
    while linea!="":
        print(linea)
        linea=file.readline()
    file.close()
    
def hacerarchivo():
  archi = open("flile.xml","w")
  archi.close()
  
def escribirarchivo():
  archi = open("flile.xml","a")
  archi.write("Hola mundo\n")
  archi.write("aprendiendo \n")
  archi.write("python")
  
def leerarchivo():
    archi = open("flile.xml","r")
    line = archi.readline()
    while line != "":
        print(line)
        line = archi.readline()
    archi.close()       
          
    
    
hacerarchivo()
escribirarchivo()
leerarchivo()        
    
    
crear_archivo()
escribir_archivo()
leer_archivos()    