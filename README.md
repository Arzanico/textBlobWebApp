# textBlobWebApp aproximacion al uso de APIs como solucion al problema de multiplataforma

La idea de este proyecto es usar la libreria TextBLob para analisis de texto a traves de un servidor web y proveer el sevicio de API.

#### Introduccion
Durante mi experiecia como DataScientist he participado activamente desarrolando aplicaciones para facilitar la tarea del analisis de la informacion en el sector de Inteligencia en redes sociales. Unos de los principales inconvenientes que nos encontramos a la hora de la implementacion es la dificultad de cubrir todas las necesidades del proyecto, sus dependencias y versiones durante la puesta en produccion.

Para el despliegue de las herramientas y dependiento del contexto en el cual los analisatas pueden usarlas, se presentaron varias opciones como maquinas virtuales, docker, kubernetes, dashboards, aplicaciones empaquedatas y finalmente webs apis.

#### Hipotesis
Para resolver el problema de multiplataforma y prscindir de una conexion de red, la primera opcion y las mas prometedora fue empaquetar las aplicaciones y generar un ejecutable que instale todo eximiendo al usuario de cualquier intevencion.

#### Desarrollo
1) Empaquetado. 

Armae archivos .bat para windows. Estos archivos instalaron todas las todas la dependencias necesarias para que Python corriera satisfactoriamente, pero se presento un problema. De base necesitaba tener instalado la version correcta de Python y si esta no estaba descargada en la pc de analista no iba a ser facil implementar una descarga automatizada y luego instalar la version correcta de Python, recuerden que no soy desarrollador de software =/. Por lo tanto abandone esta opcion.

2) Otra alternativa de empaquetado fue usar pyinstaller. 

Esta libreria nos permite crear una carpeta con todas las dependencias de nuestro programa de python y genera un archivo ejecutable (.exe). Con esto logre eliminar problemas de dependencias ya que los ejecutables corrian bien en todas las maquinas pero se presentaron de deficiencias. El tamaño del sistema de archivos generados es muy grande ya que tiene todas las librerias que usamos con python anteriormente. En segundo lugar la distribucion del programa no se puede hacer por email dadas las restricciones para enviar archivos ejecutables y esto ultimo trajo el problema que definitivamente me llevo a abandonar la idea de usar pyinstaller en produccion. Luego de comprimir y descomprimir las carpetas de la app, todos los enlaces directos dentro de las carpetas estaban rotos, esto inutilizo la aplicacion

#### Validacion
Como conte antes los caso elegido no me sirvieron para solucionar el problema. Asi que me vi en la necesidad de evaluar las otras opciones. 

#### Opciones alternativas
Maquinas virtuales lo descarte desde el comienzo por la falta de infraestructura. No tenia un servido que pudiese alojar las masquinas ni un sistema de red apropiado para validar las conexiones y establecer requisitos minimos de seguridad.
Docker y kubernetes requerian un desarrollo y conocimientos que no tengo.
Por ultimo montar un servicio con una API. En esta opcion vi, cosa que no habia echo antes, las capacidades y simplesa que necesitaba para mis proyectos. No estaba muy seguro por el echo de que es imprecindible contar con un servidor online 24/7 donde alojar el sevicio y que los analistas tengan una conexion a internet para consumir la API, pero por otro lado esta es una opcion barata, de implementacion relativamente rapida. Por esto me propuse abordar esta solucion y empezar el desarrollo del servicio implementado un simple analiss de texto.




Flask es una alternativa muy buena para empezar a planter esta solucion.

Simple, rapido y liviano.
