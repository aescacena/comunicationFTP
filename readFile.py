'''
Created on 16 de abr. de 2016

@author: aescacena
'''
def getCredencialesFTP(nombreFichero):
    """ Lee del fichero con nombre pasado por parametros las credenciales para la conexion a servidor FTP """
    
    infile = open(nombreFichero,'r')
    lines = infile.readlines()
    server = lines[0].split(' ', 1)
    usuario = lines[1].split(' ', 1)
    contrasena = lines[2].split(' ', 1)
    infile.close()
    
    return (server, usuario, contrasena)
