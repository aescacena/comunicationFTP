'''
Created on 16 de abr. de 2016

@author: aescacena
'''

#librerias propias de python
import ftplib
import os

#librerias propias mias
from readFile import getCredencialesFTP

class clienteFTP:
    
    def __init__(self, credenciales):
        #Con [:-1] eliminamos el ultimo caracter que es el salto de linea
        self.servidor_ftp = credenciales[0][1][:-1]
        self.usuario = credenciales[1][1][:-1]
        self.contrasena = credenciales[2][1][:-1]
        self.archivo = 'Documento.txt' 
        
        print credenciales
        print self.usuario
        print self.contrasena
        print self.archivo 
    
    def subir_ftp(self):
        print "Conectando con servidor..."
        self.ftp = ftplib.FTP(self.servidor_ftp)
        
        print "Iniciado sesion como usuario: %s" %self.usuario
        self.ftp.login(self.usuario, self.contrasena)
        
        extension = os.path.splitext(self.archivo)[1]
        
        if extension in (".txt", ".htm", ".html"):
            self.ftp.storlines("STOR " + self.archivo, open(self.archivo))
        else:
            self.ftp.storbinary("STOR "+ self.archivo, open(self.archivo, "rb"), 1024)
        
        print "Archivo %s subido con exito" %self.archivo
        
    def cliente_ftp_conexion(self, servidor, nombre_usuario, correo):
        #hacemos la apertura de la conexion
        ftp = ftplib.FTP(servidor, nombre_usuario, correo)
    
        #Listamos los archivos del directorio /pub
        ftp.cwd("/pub")
        print "Archivos disponibles en %s:" %servidor
        archivos = ftp.dir()
        print archivos
        ftp.quit()
    
if __name__ == '__main__':
    cliente = clienteFTP(getCredencialesFTP('credenciales.txt'))
    cliente.subir_ftp()
        
        
        