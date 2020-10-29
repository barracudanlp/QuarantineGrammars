## Descripción

El objetivo de este repositorio es armar una gramática independiente de contexto aumentada con rasgos (una fcfg) para el español con la mayor cobertura posible, pensada para ser usada con la librería NLTK en Python3. La gramática incluye, a su vez, un rasgo SEM que permite construir, junto con el parseo de la oración, su interpretación semántica usando un sistema de notación neodavidsoniano. 

A la fecha, el script sentence_interpreter.py provee una interfaz para obtener la representación semántica de oraciones.
Al ejecutar sentence_interpreter.py se crea una gramática temporal con las reglas definidas en GramaticaDeRasgosBase.txt más el conjunto de reglas léxicas correspondientes a los tokens de la oración, cuyos rasgos se obtienen del tag de freeling.

## Instalación del entorno

Para instalar el entorno virtual necesario para ejecutar los scripts que se encuentran en este módulo se debe:

    1. Instalar pyenv (seguir instrucciones en [repositorio de pyenv](https://github.com/pyenv/pyenv))
    2. Con pyenv, instalar python 3.7.5 
        pyenv python 3.7.5
    3. Dentro de la carpeta del proyecto, ejecutar: 
        pyenv local 3.7.5
    4. Instalar pipenv utilizando pip 
        pip3 install pipenv
    5. Ejecutar: 
        pipenv --python 3.7.5
    6. Ejecutar
        pipenv install
    7. Dentro de la carpeta delivery ejecutar: 
        ./download_resources.sh
    8. Ejecutar: 
        pipenv run python -m ipykernel install --user --name=`pipenv run basename '$VIRTUAL_ENV'`

## Activación del entorno virtual
    
Para activar el entorno virtual ejecutar:
        pipenv shell

