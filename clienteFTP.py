'''
Created on 16 de abr. de 2016

@author: aescacena
'''

RUTA_SERVIDOR_FTP = 'ftp.kernel.org'
import ftplib
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
    cliente_ftp_conexion(servidor=RUTA_SERVIDOR_FTP, nombre_usuario='anonymous', correo='nobody@nourl.com')