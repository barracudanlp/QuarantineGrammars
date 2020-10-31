from quarentine_grammars.utils import *
import argparse
from quarentine_grammars.paths import tags_mapping_path
import json
from nltk.sem.util import root_semrep

def interpreter_setup():
    """
        Carga el mapeo de tags y los vocabularios.

        Returns
        ----------
        iterable
            tags_mapping: dict
                Mapeo de tags y features
            vocab_df: pandas.DataFrame
                Vocabulario taggeado
    """
    tags_mapping = load_json(tags_mapping_path)
    vocab_df = load_vocabulary()
    return tags_mapping,vocab_df 

def print_parse(interpretation,syn):
    """
        Imprime la interpretación sintáctica
        o semántica de la oración.

        Parámetros
        ----------
        syn: bool
            Si es True, imprime la interpretación sintáctica
            Si es False, imprime la interpretación semántica
    """
    if syn:
        for tree in interpretation:
            tree.pprint()
            #tree.draw()
    else:
        for tree in interpretation:
            print(f"\n\t{root_semrep(tree)}\n")

def print_interpretation(interpretation,syn):
    """
        Chequea si la interpretación obtenida es válida. 
        Si es válida, llama a su impresión.
        Si es inválida, imprime la excepción que ésta devolvió.

        Parámetros
        ----------
        syn: bool
            Si es True, llama a la impresión de la interpretación sintáctica
            Si es False, llama a la impresión de la interpretación semántica
    """
    if isinstance(interpretation, Exception):
        print(f"\n\t{interpretation}\n")
    else:
        print_parse(interpretation,syn)

def interpreter_interface(syn):
    """
        Brinda una interfaz para la obtención
        de la interpreación semántica o sintáctica de oraciones.
        Carga los vocabularios y el mappeo de tags.
        Si en lugar de una oración se provee "q", termina.

        Parámetros
        ----------
        syn: bool
            Si es True, devuelve interpretaciones semánticas
            Si es False, devuelve interpretaciones sintácticas
    """
    tags_mapping,vocab_df = interpreter_setup()
    sentence = input("Oración (type 'q' to quit): ")
    while sentence != "q":
        interpretation = interpret_sentence(sentence,vocab_df,tags_mapping)
        print_interpretation(interpretation,syn)
        sentence = input("Oración (type 'q' to quit): ")


if __name__ == "__main__":
    """
        Inicializa una interfaz para la interpretación de oraciones

        python interpret_sentences.py [-syn]
        
        Parámetros
        ----------
        syn: bool=False
            Si se provee el parámetro, crea una interfaz para obtener interpretaciones semánticas
            Si no se provee el parámetro, crea una interfaz para obtener interpretaciones sintácticas       
    """
    parser = argparse.ArgumentParser(description='Ejecutar rutina de algun/os canal/es')
    parser.add_argument('-syn','--syn',action='store_true', help='Devolver la representación sintáctica')
    args = parser.parse_args()

    interpreter_interface(syn=args.syn)


    
