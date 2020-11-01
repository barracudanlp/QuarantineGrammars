import glob
import pandas as pd
import json
import os
import nltk
from shutil import copyfile
from .rules_builder import MakeRule, NoMapping
import random
import string
from nltk.parse.featurechart import InstantiateVarsChart


class NoVocabFiles(Exception):
    """
        No hay archivos que coincidan con los paths solicitados
    """
    pass

def vocabulary_to_df(vocabulary_paths):
    """
        Crea un dataframe con las palabras taggeadas
        en los archivos indicados en una lista.
        ...

        Parámetros
        ----------
        vocabulary_paths: list
            Paths a los archivos de vocabulario

        Returns
        ----------
        vocab_df: pandas.DataFrame
            Dataframe con las columnas "forma","lema" y "tag"
    """
    vocab_df = pd.DataFrame()
    for vocabulary_file in vocabulary_paths:
        vocab_df = vocab_df.append(pd.read_csv(vocabulary_file, sep=" ",names=["forma","lema","tag"]))
    return vocab_df

def load_vocabulary(glob_paths):
    """
        Arma una lista con los paths de los diccionario a partir de un 
        patrón en formato glob.
        Si no encuentra ninguno, levanta una excepción.
        Si encuentra, llama al armado de un DataFrame.
        ...

        Parámetros
        ----------
        glob_paths: str
            Patrón en formato glob para ubicar los archivos de diccionarios

        Returns
        ----------
        vocab_df: pandas.DataFrame
            Dataframe con las columnas "forma","lema" y "tag"
    """
    vocabulary_paths = glob.glob(glob_paths)
    if len(vocabulary_paths) > 0:
        vocab_df = vocabulary_to_df(vocabulary_paths)
    else:
        raise NoVocabFiles("No vocabulary available. Please read README file for instructions")
    return vocab_df

def get_random_string(length):
    """
        Crea una cadena de letras aleatorias
        ...

        Parámetros
        ----------
        length: str
            Largo de la cadena a devolver

        Returns
        ----------
        random_str: str
            Cadena de letras aleatorias
    """
    letters = string.ascii_lowercase
    random_str = ''.join(random.choice(letters) for i in range(length))
    return random_str

def create_tmp_grammar(base_grammar_path):
    """
        Copia el archivo de reglas gramaticales.
        Le asigna a la copia un nombre aleatorio de 8 letras 
        y la guarda en la misma ubicación que la otra. 
        Devuelve el path a la gramática creada.
        ...

        Parámetros
        ----------
        base_grammar_path: str
            Path a la gramática con reglas gramaticales

        Returns
        ----------
        tmp_grammar_path: str
            Path la gramática temporal
    """
    random_str = get_random_string(8)
    grammars_dir_path = os.path.dirname(base_grammar_path)
    tmp_grammar_path = os.path.join(grammars_dir_path,f"{random_str}.fcfg")
    copyfile(base_grammar_path, tmp_grammar_path)
    return tmp_grammar_path
    
def append_rules_to_grammar(rules,grammar):
    """
        Agrega reglas al archivo de una gramática.
        ...

        Parámetros
        ----------
        rules: str
            Reglas
        grammar: str
            Path a la gramática
    """
    with open(grammar,"a+") as current_grammar:
        for rule in rules:
             current_grammar.write(f"\n{rule}")

def get_rules(word,vocab_df,tags_mapping):
    """
        Selecciona las filas para una forma léxica del dataframe con el vocabulario,
        convierte el dataframe resultante en una lista de diccionarios y llama al armado
        de las reglas para cada elemento.
        ...

        Parámetros
        ----------
        word: str
            Palabra cuyas reglas se quiere obtener
        vocab_df: DataFrame
            DataFrame con el vocabulario taggeado
        tags_mapping: dict
            Mapeo tags-features

        Returns
        ----------
        word_rules: list
            Lista de reglas correspondientes a word
    """
    word_rules = list()
    word_in_vocab = json.loads(vocab_df[vocab_df.forma == word].to_json(orient="records"))
    for entry in word_in_vocab:
        word_rules.append(MakeRule(entry,tags_mapping).rule)
    return word_rules

def create_sentence_rules(words_list,vocab_df,tags_mapping):
    """
        Llama al armado de reglas para todas las palabras de una lista
        y devuelve una lista no anidada.
        Si alguna palabra no tiene mapeo tags-features, continúa con la
        siguiente
        ...

        Parámetros
        ----------
        words_list: list
            Lista de palabras
        vocab_df: DataFrame
            DataFrame con el vocabulario taggeado
        tags_mapping: dict
            Mapeo tags-features

        Returns
        ----------
        sentence_rules: list
            Lista de reglas correspondientes a todas las palabras de words_list
    """
    sentence_rules = list()
    for word in set(words_list):
        try:
            rules = get_rules(word,vocab_df,tags_mapping)
            sentence_rules.extend(rules)
        except NoMapping:
            continue
    return sentence_rules

def interpret_sentence(sentence,vocab_df,tags_mapping,base_grammar_path):
    """
        Crea una gramática temporal, tokeniza una oración, obtiene su
        interpretación y elimina la gramática temporal.
        Si algún item léxico no es interpreable, en lugar de la interpretación
        devuelve la excepción.
        ...

        Parámetros
        ----------
        sentence: str
            Oración
        vocab_df: DataFrame
            DataFrame con el vocabulario taggeado
        tags_mapping: dict
            Mapeo tags-features
        base_grammar_path: str
            Path a la gramática con reglas gramaticales

        Returns
        ----------
        interpretation: nltk.Tree or Exception
            Interpretación de nltk de sentence o la excepción que levanta nltk
    """
    grammar = create_tmp_grammar(base_grammar_path)
    tok_sentence = nltk.tokenize.word_tokenize(sentence)
    sentence_rules = create_sentence_rules(tok_sentence,vocab_df,tags_mapping)
    append_rules_to_grammar(sentence_rules,grammar)
    try:
        cp = nltk.parse.load_parser(grammar)
        interpretation = cp.parse(tok_sentence)
    except ValueError as exception:
        interpretation = exception
    os.remove(grammar)
    return interpretation

def load_json(json_file):
    """
        Carga un archivo json
        ...

        Parámetros
        ----------
        json_file: str
            Path al archivo json

        Returns
        ----------
        data: dict
            Diccionario con la data en json_file
    """
    with open(json_file) as file:
        data = json.load(file)
    return data