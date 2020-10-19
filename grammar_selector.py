import nltk
from nltk.tokenize import word_tokenize
from nltk import load_parser
import re
import os

#############################
# Chequeo de Léxico
#############################

# Esto es para que al momento de importar este archivo reuna en un solo 
# archivo todo el léxico. 
# Si el archivo ya existe no lo vuelve a armar, trabaja con el que está.
# Estaría bueno repensar esto como una función para poder setear qué archivos
# uno quiere que coleccione, para de esa manera hacerlo más portable por ejemplo
# para otras lenguas.

if not os.path.exists('./reglas_automaticas/integral_lexicon.fcfg'):
    lexicon_files = os.listdir(path='./reglas_automaticas')
    outfile = open('./reglas_automaticas/integral_lexicon.fcfg', 'w')
    for fname in lexicon_files:
        with open(f'./reglas_automaticas/{fname}', 'r') as infile:
            for line in infile:
               outfile.write(line)

#############################
# Grammar selector
#############################

# acá es para pegar la función grammar_selector
