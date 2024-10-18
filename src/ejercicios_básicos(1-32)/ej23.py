#
#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
#
correo = input ("Introduce tu correo electrónico:")
partes = correo.split("@")
nombre = partes [0]
dominio = partes [1]
dominio_cambiado = dominio.replace(dominio,"ceu.es")
correo_cambiado = '@'.join([nombre,dominio_cambiado])
print (correo_cambiado)
