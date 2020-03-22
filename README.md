# Descripción de lo que hay:

1) Descargar de https://github.com/TALP-UPC/FreeLing/tree/master/data/es/dictionary/entries MM.verb.txt, MM.adj.txt, MM.adv.txt y MM.nom.txt y de https://github.com/TALP-UPC/FreeLing/tree/master/data/es/es-ar/dictionary/entries AR.verb.txt y colocarlos en una carpeta llamada freeling (Eso ya está hecho en este repositorio).

2) Correr el script script_para_freeling.sh (bash script_para_freeling.sh en la terminal). Eso va a crear el directorio subclases y un conjunto de archivos con extensión csv que compilan por separado palabras con propiedades morfológicas iguales (e.g. todos los nombres masculinos singulares en un csv, todos los femeninos plurales en otro, etc.)
 
3) Correr el script script_armado_gram_cfg.py. El script va a tomar los archivos csv que están en subclases y va a recopilar todas las palabras que están en ellos en txt adaptándolas para que la etiqueta de eagles se transforme en rasgos que pueda leer la gramática de nltk. Finalmente, se va a generar en este directorio un archivo llamado gram_para_fcfg.fcfg, que compila todos los léxicos y la gramática y que puede ser utilizado para parsear oraciones con nltk.

Pasos a hacer a futuro:

- Revisar gramática
- Revisar subclases morfológicas en función de los rasgos que vaya a tener la gramática
- Revisar el script en función de eso
- Todo lo que hay subido ahora es para una gramática no eventiva, si vamos a asumir una eventiva, hay que adaptar todo eso a una semántica de ese tipo.


