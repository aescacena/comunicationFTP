'''
Created on 16 de abr. de 2016

@author: aescacena
'''
#librerias propias de python
import ftplib
import os
import argparse
import getpass

#librerias propias mias
from readFile import getCredencialesFTP
from ast import parse

credenciales = getCredencialesFTP('credenciales.txt')
SERVIDOR_FTP = credenciales[0][1]
USUARIO = credenciales[1][1]
CONTRASENA = credenciales[2][1]
ARCHIVO = 'Documento.txt' 

def subir_ftp(servidor, usuario, contrasena, archivo):
    print "Conectando con servidor..."
    ftp = ftplib.FTP(str(servidor))
    
    print "Iniciado sesion como usuario: %s" %usuario
    ftp.login(str(usuario), str(contrasena))
    
    extension = os.path.splitext(archivo)[1]
    
    if extension in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + archivo, open(archivo))
    else:
        ftp.storbinary("STOR "+ archivo, open(archivo, "rb"), 1024)
    
    print "Archivo %s subido con exito" %archivo
    
def cliente_ftp_conexion(servidor, nombre_usuario, correo):
    #hacemos la apertura de la conexion
    ftp = ftplib.FTP(servidor, nombre_usuario, correo)

    #Listamos los archivos del directorio /pub
    ftp.cwd("/pub")
    print "Archivos disponibles en %s:" %servidor
    archivos = ftp.dir()
    print archivos
    ftp.quit()

if __name__ == '__main__':
    subir_ftp(SERVIDOR_FTP, USUARIO, CONTRASENA, ARCHIVO)
    
    
    