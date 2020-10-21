from utils import *
from rules_builder import MakeRule, NoMapping
import argparse

# Descomentar si no se tiene el recurso
#nltk.download("punkt")

def run_interpreter(sentence):
    tags_mapping = load_json("tags_mapping.json")
    vocab_df = load_freeling_vocabulary()
    try:
        interpretation = interpret_sentence(sentence,vocab_df,tags_mapping)
        for results in interpretation:
            for (synrep, semrep) in results:
                print(f"\n{semrep}\n")
    except ValueError as exception:
        print(f"\n{exception}\n")
    
"""

    Esto no está andando. Lo dejo para revisar

    sentence = input("Oración: ")

    while sentence != "q":
        print("type 'q' to quit")
        interpretation = interpret_sentence(sentence,vocab_df,tags_mapping)
        for results in interpretation:
            for (synrep, semrep) in results:
                print(semrep)
        sentence = input("Oración: ")

 """   

if __name__ == "__main__":
    """
        Interfaz para la interpretación de una oración
        python sentence_interpreter.py "él canta"
    """
    parser = argparse.ArgumentParser(description='Interpretar una oración')
    parser.add_argument('sentence',metavar='SENTENCE',type=str,help='Oración')
    args = parser.parse_args()

    run_interpreter(args.sentence)

