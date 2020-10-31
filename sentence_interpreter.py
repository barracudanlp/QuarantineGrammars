from quarentine_grammars.utils import *
import argparse
from quarentine_grammars.paths import tags_mapping_path
import json
from nltk.sem.util import root_semrep

def interpreter_setup():
    tags_mapping = load_json(tags_mapping_path)
    vocab_df = load_vocabulary()
    return tags_mapping,vocab_df 

def print_parse(interpretation,syn):
    if syn:
        for tree in interpretation:
            tree.pprint()
            #tree.draw()
    else:
        for tree in interpretation:
            print(f"\n\t{root_semrep(tree)}\n")

def print_interpretation(interpretation,syn):
    if isinstance(interpretation, Exception):
        print(f"\n\t{interpretation}\n")
    else:
        print_parse(interpretation,syn)

def interpreter_interface(syn):
    tags_mapping,vocab_df = interpreter_setup()
    sentence = input("Oración (type 'q' to quit): ")
    while sentence != "q":
        interpretation = interpret_sentence(sentence,vocab_df,tags_mapping)
        print_interpretation(interpretation,syn)
        sentence = input("Oración (type 'q' to quit): ")


if __name__ == "__main__":
    """
        Interfaz para la interpretación de oraciones
        python interpret_sentences.py [-syn]
    """

    parser = argparse.ArgumentParser(description='Ejecutar rutina de algun/os canal/es')
    parser.add_argument('-syn','--syn',action='store_true', help='Devolver la representación sintáctica')
    args = parser.parse_args()

    interpreter_interface(syn=args.syn)


    
