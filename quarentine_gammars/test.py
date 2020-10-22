
import nltk

#print('escribí una oración')
#sents1 = input()
#sents = list(string(sents1))
sents = ['Cata aba'.decode('utf-8')]
grammar = 'integral_grammar.fcfg'
for results in nltk.interpret_sents(sents, grammar):
    for (synrep, semrep) in results:
             print(synrep)


