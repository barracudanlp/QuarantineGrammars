## Descripción

El objetivo de este repositorio es armar una gramática independiente de contexto aumentada con rasgos (una fcfg) para el español con la mayor cobertura posible, pensada para ser usada con la librería NLTK en Python3. La gramática incluye, a su vez, un rasgo SEM que permite construir, junto con el parseo de la oración, su interpretación semántica usando un sistema de notación neodavidsoniano (i.e., con cuantificación existencial sobre eventos). 

A la fecha, el script sentence_interpreter.py provee una interfaz para obtener la representación semántica o sintáctica (con el parámetro -syn) de oraciones.
Al ejecutar sentence_interpreter.py se crea una gramática temporal con las reglas definidas en GramaticaDeRasgosBase.txt más el conjunto de reglas léxicas correspondientes a los tokens de la oración, cuyos rasgos se obtienen del tag de freeling.

## Instalación del entorno

Para instalar el entorno virtual necesario para ejecutar los scripts que se encuentran en este módulo se debe:

    1. Instalar pyenv (seguir instrucciones en [repositorio de pyenv](https://github.com/pyenv/pyenv))
    2. Con pyenv, instalar python 3.7.5 
        pyenv 3.7.5
    3. Dentro de la carpeta del proyecto, ejecutar: 
        pyenv local 3.7.5
    4. Instalar pipenv utilizando pip (o pip3, según corresponda)
        pip install pipenv
    5. Ejecutar: 
        pipenv --python 3.7.5
    6. Ejecutar
        pipenv install
    7. Dentro de la carpeta delivery ejecutar: 
        ./download_resources.sh
    8. Ejecutar: 
        pipenv run python -m ipykernel install --user --name=`pipenv run basename '$VIRTUAL_ENV'`

Tener en cuenta que si falla la instalación de pipenv, probablemente sea necesario desinstalar pip y volver a instalarlo

## Activación del entorno virtual
    
Para activar el entorno virtual ejecutar:
        pipenv shell


## Para correr el parser con la gramática

Una vez activado el entorno virtual, ejecutar: 

        python3 sentence_intepreter.py 

Esto va a permitir devolver la interpretación semántica de la oración deseada. Si se prefiere el parseo completo, ejecutar

        python3 sentence_interpreter.py -syn



