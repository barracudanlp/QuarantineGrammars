# Descripción de lo que hay:

El objetivo de este repositorio es armar una gramática independiente de contexto aumentada con rasgos (una fcfg) para el español con la mayor cobertura posible, pensada para ser usada con la librería NLTK en Python3. La gramática incluye, a su vez, un rasgo SEM que permite construir, junto con el parseo de la oración, su interpretación semántica usando un sistema de notación neodavidsoniano. 

Para el armado de la gramática, usamos los diccionarios de freeling MM.verb.txt, MM.adj.txt, MM.adv.txt y MM.nom.txt, que se pueden encontrar en https://github.com/TALP-UPC/FreeLing/tree/master/data/es/dictionary/entries, y AR.verb.txt, que se puede encontrar en de https://github.com/TALP-UPC/FreeLing/tree/master/data/es/es-ar/dictionary/entries. En el repositorio, todos estos diccionarios están reunidos en un solo archivo freeling/all_categories.txt. Para descargarlos por separado, ir al directorio freeling y correr desde la terminal el comando ``sh download-dictionaries.sh''.

Para armar la gramática utilizamos como punto de partida el archivo GramaticaDeRasgosBase.txt, que contiene una gramática reducida. La Jupyter notebook armado_reglas.ipynb posee el script (en construcción) para procesar la información proveniente de los diccionarios de freeling y, en función de eso, concatenar a la gramática en GramaticaDeRasgosBase.txt un conjunto de reglas que introducen nodos no terminales. Esa gramática más robusta se guarda en el archivo integral_grammar.fcfg. 

Los archivos test.ipynb y test.py son meramente scripts para probar la gramática integral_grammar.fcfg en NLTK.

