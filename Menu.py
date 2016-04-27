'''
Created on 24 de abr. de 2016

@author: aescacena
'''

#Imports
import os
import sys
import clienteFTP

#Constants
LIMPIAR = "clear" if sys.platform.startswith("linux") else "clear"

class Menu(object):
    '''
    Lista de funciones opcionales, las cuales le permiten al usuario realizar operaciones
    '''

    def __init__(self):
        self.client = clienteFTP.clientFTP()
        self.prompt = "> "
        self.options = [
                        "Listar ficheros", 
                        "Eliminar fichero", 
                        "Subir fichero", 
                        "Editar fichero",
                        "Salir"
                        ]
        self.presentation = "-----------------------------Bienvenido---------------------------------\n"
        
        for number, option in enumerate(self.options, 1) :
            self.presentation += "{0}. {1}\n".format(number, option)
            
    def set_credentials_FTP(self):
        print "Teclea fichero de credenciales \n"
        
        while True:
            if self.client.credentials_FTP(raw_input(my_menu.prompt)):
                break
            else:
                print "Credenciales incorrectas, vuelve a intentarlo\n"
                    
    def ask_operands(self):
        while True:
            print "Ingrese operando"
            
            try:
                op = int(raw_input(self.prompt))
            except ValueError:
                print raw_input("Error: Debes introducir un numero")
            else:
                break
            
        return op
        
    def list_files(self): 
#         raw_input("Funcion lista ficheros")
        self.client.FTP_ListFile()
    
    def delete_file(self): 
        raw_input("Funcion elimina fichero")

    def upload_file(self): 
        raw_input("Funcion subir fichero")
    
    def edit_file(self):
        raw_input("Funcion editar fichero")
        
    def exit(self):
        raw_input("Funcion salir")
        raise KeyboardInterrupt()
        
if __name__== "__main__":
    my_menu = Menu()
    
    my_menu.set_credentials_FTP()
    
    while True:
        print my_menu.presentation
            
        try:
            selection_op = int(raw_input(my_menu.prompt))
             
            if selection_op == 1  :
                my_menu.list_files()
            elif selection_op == 2 :
                my_menu.delete_file()
            elif selection_op == 3 :
                my_menu.upload_file()
            elif selection_op == 4 :
                my_menu.edit_file()
            elif selection_op == 5 :
                my_menu.exit()
            else:
                raw_input("Error: Opcion invalida")
            
        except ValueError:
            raw_input(raw_input("Error: Debes introducir un numero"))
                
        except KeyboardInterrupt:
            break
            
        os.system(LIMPIAR)
        