from quarentine_grammars.utils import *
import argparse
from quarentine_grammars.paths import tags_mapping_path
import json
from nltk.sem.util import root_semrep

def interpreter_setup():
    tags_mapping = load_json(tags_mapping_path)
    vocab_df = load_freeling_vocabulary()
    return tags_mapping,vocab_df 

def print_parse(interpretation,parse):
    if parse == "syn":
        for tree in interpretation:
            print(f"\n\t{tree}\n")
    elif parse == "sem":
        for tree in interpretation:
            print(f"\n\t{root_semrep(tree)}\n")

def print_interpretation(interpretation,parse):
    if isinstance(interpretation, Exception):
        print(f"\n\t{interpretation}\n")
    else:
        print_parse(interpretation,parse)

def interpreter_interface(parse="sem"):
    tags_mapping,vocab_df = interpreter_setup()
    sentence = input("Oración (type 'q' to quit): ")
    while sentence != "q":
        interpretation = interpret_sentence(sentence,vocab_df,tags_mapping)
        print_interpretation(interpretation,parse)
        sentence = input("Oración (type 'q' to quit): ")


if __name__ == "__main__":
    """
        Interfaz para la interpretación de oraciones
    """
    interpreter_interface()


    
