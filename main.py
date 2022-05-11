#importacion de libreria api
import requests

#Generacion de condicional
#if __name__ == '__main__':
 #   url = 'https://www.google.com.co/'
    #llamado de metodo get
  #  response = requests.get(url)

    #devolucion del recurso por parte del server
   #if response.status_code == 200:
    #    print(response.content)
    #
    #if response.status_code == 200:
     #   content = response.content
      #  file = open('google.html', 'wb')
       # file.write(content)
        #file.close()

#Generacion de condicional con repositorio github para la peticion
#de parte del usuario el ingreso de su sesion
if __name__ == '__main__':
    url = 'https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%26source%3Dheader-home'

    session = requests.Session()
    #reistro simulacion de base de datos con el usuario y contraseña
    session.auth = ('cramosm@ucompensar.edu.co','SistemasDistribuidos1234')
    #metodo get para llamar el inicio
    response = session.get(url)
    if response.ok:
        print(response.content)
        #creacion de interfaz dentro del server
        content = response.content
        file = open('github_session.html', 'wb')
        file.write(content)
        file.close()

    #Ingreso al repositorio maestro de la sesion de Crisrian Ramos

    response = session.get('https://github.com/CrisRida/SistemaDistribuido')
    if response.ok:
        print(response.cookies)
        #creacion de interfaz del repositorio dentro del server
        content = response.content
        file = open('github_repositorio.html', 'wb')
        file.write(content)
        file.close()

    #en caso de que no responda arrojaria mensaje de que no inicio sesion    
    else:
        print(response.content)
        