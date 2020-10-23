import glob
import pandas as pd
import json
import os
import nltk
from shutil import copyfile
from .rules_builder import MakeRule, NoMapping
import random
import string
from .paths import freeling_glob_paths, base_grammar_path, grammars_dir_path

def load_freeling_vocabulary():
    freeling_all = list()
    vocab_df = pd.DataFrame()
    for freeling_file in glob.glob(freeling_glob_paths):
        vocab_df = vocab_df.append(pd.read_csv(freeling_file, sep=" ",names=["forma","lema","tag"]))
    return vocab_df

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def create_tmp_grammar():
    random_str = get_random_string(8)
    tmp_grammar = os.path.join(grammars_dir_path,f"{random_str}.fcfg")
    copyfile(base_grammar_path, tmp_grammar)
    return tmp_grammar
    
def append_rules_to_grammar(rules,grammar):
    with open(grammar,"a+") as current_grammar:
        for rule in rules:
             current_grammar.write(f"{rule}\n")

def get_rules(word,vocab_df,tags_mapping):
    word_rules = list()
    word_in_vocab = json.loads(vocab_df[vocab_df.forma == word].to_json(orient="records"))
    for entry in word_in_vocab:
        word_rules.append(MakeRule(entry,tags_mapping).rule)
    return word_rules

def create_sentence_rules(tokenized_sentence,tags_mapping,vocab_df):
    sentence_rules = list()
    for word in set(tokenized_sentence):
        try:
            rules = get_rules(word,vocab_df,tags_mapping)
            sentence_rules.extend(rules)
        except NoMapping:
            continue
    return sentence_rules

def interpret_sentence(sentence,vocab_df,tags_mapping):
    grammar = create_tmp_grammar()
    tok_sentence = nltk.tokenize.word_tokenize(sentence)
    sentence_rules = create_sentence_rules(tok_sentence,tags_mapping,vocab_df)
    append_rules_to_grammar(sentence_rules,grammar)
    try:
        interpretation = nltk.interpret_sents([sentence], grammar)
    except ValueError as exception:
        interpretation = exception
    os.remove(grammar)
    return interpretation

def load_json(json_file):
    with open(json_file) as file:
        data = json.load(file)
    return data