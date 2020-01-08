# textBlobWebApp
La idea de este proyecto es usar la libreria TextBLob para analisis de texto a traves de un servidor web.

Durante mi experiecia como DataScientist he participado activamente desarrolando aplicaciones para facilitar la tarea de analisis de informacion en el sector de Inteligencia en redes sociales y unos de los principales inconvenientes que nos encontramos a la hora de la implementacion es la dificultad de cubrir todas las necesidades de la applicacion, dependencias y versiones.
Para resolver esto experimente dos caminos.

El primero un poco tedioso, empaquetado. Consistio en armar archivos .bat para windows donde se instalaban todas la dependencias necesarias para que python corriera satisfactoriamente, pero todavia necesitaba tener instalado con anterioridad la version adecuada de Pyhton, por lo tanto no se eliminaron todas las dependencias.
Otra alternativa de empaquetado fue usar pyinstaller, esta libreria nos permite crear una carpeta con todas las dependencias de nuestro programa de python y genera un archivo ejecutable (.exe). Con esto logre eliminar problemas de dependencias ya que los ejecutables corrian bien en todas las maquinas pero se presentaron de deficiencias. El tamaño del sistema de archivos generados es muy grande ya que tiene todas las librerias que usamos con python anteriormente. En segundo lugar la distribucion del programa no se puede hacer por email dadas las restricciones para enviar archivos ejecutables y esto ultimo trajo el problema que definitivamente me llevo a abandonar la idea de usar pyinstaller en produccion. Luego de comprimir y descomprimir las carpetas con el programa de python, todos los enlaces directos dentro de las carpetas estaban inutilizables.

Por lo antes mendionado y muchos motivos mas que otros programadores habran experimentado, la mejor opcion para poner a disposicion un programatipo de python es atraves de una plataforma web accesible desde cualquier lado y sin problemas de dependencia.

Flask es una alternativa muy buena para empezar a planter esta solucion.

Simple, rapido y liviano.
