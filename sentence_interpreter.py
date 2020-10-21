from utils import *
from rules_builder import MakeRule, NoMapping
import argparse

# Descomentar si no se tiene el recurso
#nltk.download("punkt")

def interpreter_setup():
    tags_mapping = load_json("tags_mapping.json")
    vocab_df = load_freeling_vocabulary()
    return tags_mapping,vocab_df 


def run_interpreter(sentence,tags_mapping,vocab_df):
    interpretation = interpret_sentence(sentence,vocab_df,tags_mapping)
    if not isinstance(interpretation, Exception):
        for results in interpretation:
            for (synrep, semrep) in results:
                print(f"\n{semrep}\n")
    else:
        print(f"\n{interpretation}\n")


def interpreter_interface():
    tags_mapping,vocab_df = interpreter_setup()
    sentence = input("Oración (type 'q' to quit): ")
    while sentence != "q":
        run_interpreter(sentence,tags_mapping,vocab_df)
        sentence = input("Oración (type 'q' to quit): ")


if __name__ == "__main__":
    """
        Interfaz para la interpretación de oraciones
    """
    interpreter_interface()


    
    
