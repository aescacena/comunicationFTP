'''
Created on 16 de abr. de 2016

@author: aescacena
'''

#librerias propias de python
import ftplib
import os

#librerias propias mias
from readFile import getCredencialesFTP

class clientFTP:
    
    def __init__(self, credentials):
        #Con [:-1] eliminamos el ultimo caracter que es el salto de linea
        self.server_ftp = credentials[0][1][:-1]
        self.user = credentials[1][1][:-1]
        self.password = credentials[2][1][:-1]
        self.file = 'Documento.txt' 
        self.ftp = None;
        
    def upload_ftp(self):
        print "Conectando con servidor..."
        self.ftp = ftplib.FTP(self.server_ftp)
        
        print "Iniciado sesion como usuario: %s" %self.user
        self.ftp.login(self.user, self.password)
        
        extension = os.path.splitext(self.file)[1]
        
        if extension in (".txt", ".htm", ".html"):
            self.ftp.storlines("STOR " + self.file, open(self.file))
        else:
            self.ftp.storbinary("STOR "+ self.file, open(self.file, "rb"), 1024)
        
        print "file %s subido con exito" %self.file
        
    def FTP_ListFile(self):
        #hacemos la apertura de la conexion
        self.ftp = ftplib.FTP(self.server_ftp)
        self.ftp.login(self.user, self.password)
        
        print "Ficheros disponibles en %s:" %self.server_ftp
        files = self.ftp.dir()
        print files
        self.ftp.quit()
        
    def getCommandsFTP(self):
        self.ftp = ftplib.FTP(self.server_ftp)
        self.ftp.login(self.user, self.password)
        return self.ftp.sendcmd('help')
        
if __name__ == '__main__':
    client = clientFTP(getCredencialesFTP('credenciales.txt'))
    client.upload_ftp()
    client.FTP_ListFile()
    print client.getCommandsFTP()
        
        
        