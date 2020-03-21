## Script para armado de una gramática con su léxico para parsear e interpretar semánticamente oraciones mediante semántica proposicional no eventiva.

# Descripción de los pasos:
# 1) Descargar de https://github.com/TALP-UPC/FreeLing/tree/master/data/es/dictionary/entries MM.verb.txt, MM.adj.txt, MM.adv.txt y MM.nom.txt y de https://github.com/TALP-UPC/FreeLing/tree/master/data/es/es-ar/dictionary/entries AR.verb.txt y colocarlos en una carpeta llamada freeling.
# 2) Correr el script script_para_freeling.sh (bash script_para_freeling.sh en la terminal). Eso va a crear el directorio subclases y un conjunto de archivos con extensión csv 
# 3) Correr este script.
# 4) El script va a tomar los archivos csv que están en subclases y va a recopilar todas las palabras que están en ellos en txt adaptándolas para que la etiqueta de eagles se transforme en rasgos que pueda leer la gramática de nltk. Finalmente, se va a generar en este directorio un archivo llamado gram_para_fcfg.fcfg, que compila todos los léxicos y la gramática y que puede ser utilizado para parsear oraciones con nltk.

import csv
import pandas as pd
import re
import os

# Crea la carpeta donde se guardan todos los archivos intermedios (se puede borrar al final)
if not os.path.exists('freeling/fcfg'):
    os.makedirs('freeling/fcfg')

# En esa carpeta se van a guardar los archivos txt con el léxico por clase de palabra:

##################################
# Armado del léxico de Adjetivos #
##################################

# Adjetivos masculinos singulares
adjs_masc_sing = pd.read_csv('freeling/subclases/adjs-m-s.csv', delimiter=' ')
#print(adjs_masc_sing)

tupla_adjs_masc_sing = [tuple(x) for x in adjs_masc_sing.values]
#print(tupla_adjs_masc_sing)

lista_adjs_m_s = [w[0] for w in tupla_adjs_masc_sing]
#print(lista_adjs_m_s)

#########################################################

# Adjetivos femeninos singulares
adjs_fem_sing = pd.read_csv('freeling/subclases/adjs-f-s.csv', delimiter=' ')
#print(adjs_fem_sing)

tupla_adjs_fem_sing = [tuple(x) for x in adjs_fem_sing.values]
#print(tupla_adjs_fem_sing)

lista_adjs_f_s = [w[0] for w in tupla_adjs_fem_sing]
#print(lista_adjs_f_s)

#########################################################

# Adjetivos comunes singulares
adjs_com_sing = pd.read_csv('freeling/subclases/adjs-c-s.csv', delimiter=' ')
#print(adjs_com_sing)

tupla_adjs_com_sing = [tuple(x) for x in adjs_com_sing.values]
#print(tupla_adjs_com_sing)

lista_adjs_c_s = [w[0] for w in tupla_adjs_com_sing]
#print(lista_adjs_c_s)

#########################################################

# Adjetivos masculinos plurales
adjs_masc_pl = pd.read_csv('freeling/subclases/adjs-m-p.csv', delimiter=' ')
#print(adjs_masc_pl)

tupla_adjs_masc_pl = [tuple(x) for x in adjs_masc_pl.values]
#print(tupla_adjs_masc_pl)

lista_adjs_m_p = [w[0] for w in tupla_adjs_masc_pl]
#print(lista_adjs_m_p)

#########################################################

# Adjetivos femeninos plurales
adjs_fem_pl = pd.read_csv('freeling/subclases/adjs-f-p.csv', delimiter=' ')
#print(adjs_fem_pl)

tupla_adjs_fem_pl = [tuple(x) for x in adjs_fem_pl.values]
#print(tupla_adjs_fem_pl)

lista_adjs_f_p = [w[0] for w in tupla_adjs_fem_pl]
#print(lista_adjs_f_p)

#########################################################
# Adjetivos comunes plurales
adjs_com_pl = pd.read_csv('freeling/subclases/adjs-c-p.csv', delimiter=' ')
#print(adjs_com_pl)

tupla_adjs_com_pl = [tuple(x) for x in adjs_com_pl.values]
#print(tupla_adjs_com_pl)

lista_adjs_c_p = [w[0] for w in tupla_adjs_com_pl]
#print(lista_adjs_c_p)

#########################################################

# Adjetivos masculinos neutros (no hay)
#adjs_masc_n = pd.read_csv('freeling/subclases/adjs-m-n.csv', delimiter=' ')
#print(adjs_masc_pl)

#tupla_adjs_masc_n = [tuple(x) for x in adjs_masc_n.values]
#print(tupla_adjs_masc_n)

#lista_adjs_m_n = [w[0] for w in tupla_adjs_masc_n]
#print(lista_adjs_m_n)

#########################################################

# Adjetivos femeninos neutros (no hay)
#adjs_fem_n = pd.read_csv('freeling/subclases/adjs-f-n.csv', delimiter=' ')
#print(adjs_fem_n)

#tupla_adjs_fem_n = [tuple(x) for x in adjs_fem_n.values]
#print(tupla_adjs_fem_n)

#lista_adjs_f_p = [w[0] for w in tupla_adjs_fem_n]
#print(lista_adjs_f_n)

#########################################################
# Adjetivos comunes neutros
adjs_com_n = pd.read_csv('freeling/subclases/adjs-c-n.csv', delimiter=' ')
#print(adjs_com_n)

tupla_adjs_com_n = [tuple(x) for x in adjs_com_n.values]
#print(tupla_adjs_com_n)

lista_adjs_c_n = [w[0] for w in tupla_adjs_com_n]
#print(lista_adjs_c_n)

#########################################################

with open('freeling/fcfg/adjs_para_gram.txt', 'w') as f:
    for item in lista_adjs_m_s:
        f.write("A[GEN=masc, Num=sg] -> \'%s\'\n" % item)
    for item in lista_adjs_f_s:
        f.write("A[GEN=fem, Num=sg] -> \'%s\'\n" % item)
    for item in lista_adjs_c_s:
        f.write("A[GEN=?n, Num=sg] -> \'%s\'\n" % item)
    for item in lista_adjs_m_p:
        f.write("A[GEN=masc, Num=pl] -> \'%s\'\n" % item)
    for item in lista_adjs_f_p:
        f.write("A[GEN=fem, Num=pl] -> \'%s\'\n" % item)
    for item in lista_adjs_c_p:
        f.write("A[GEN=?n, Num=pl] -> \'%s\'\n" % item)
#    for item in lista_adjs_m_n:
#        f.write("A[GEN=masc, Num=n?] -> \'%s\'\n" % item)
#    for item in lista_adjs_f_n:
#        f.write("A[GEN=fem, Num=?n] -> \'%s\'\n" % item)
    for item in lista_adjs_c_n:
        f.write("A[GEN=?n, Num=?n] -> \'%s\'\n" % item)
        

####################################
# Armado del léxico de sustantivos #
####################################

# Sustantivos masculinos singulares
sust_masc_sing = pd.read_csv('freeling/subclases/nc-m-s.csv', delimiter=' ')
#print(adjs_masc_sing)

tupla_sust_masc_sing = [tuple(x) for x in sust_masc_sing.values]
#print(tupla_adjs_masc_sing)

lista_sust_m_s = [w[0] for w in tupla_sust_masc_sing]
#print(lista_sust_m_s)

#########################################################

# Sustantivos femeninos singulares
sust_fem_sing = pd.read_csv('freeling/subclases/nc-f-s.csv', delimiter=' ')
#print(sust_fem_sing)

tupla_sust_fem_sing = [tuple(x) for x in sust_fem_sing.values]
#print(tupla_sust_fem_sing)

lista_sust_f_s = [w[0] for w in tupla_sust_fem_sing]
#print(lista_sust_f_s)

#########################################################

# Sustantivos comunes singulares
sust_com_sing = pd.read_csv('freeling/subclases/nc-c-s.csv', delimiter=' ')
#print(sust_com_sing)

tupla_sust_com_sing = [tuple(x) for x in sust_com_sing.values]
#print(tupla_sust_com_sing)

lista_sust_c_s = [w[0] for w in tupla_sust_com_sing]
#print(lista_sust_c_s)

#########################################################

# Sustantivos masculinos plurales
sust_masc_pl = pd.read_csv('freeling/subclases/nc-m-p.csv', delimiter=' ')
#print(sust_masc_pl)

tupla_sust_masc_pl = [tuple(x) for x in sust_masc_pl.values]
#print(tupla_sust_masc_pl)

lista_sust_m_p = [w[0] for w in tupla_sust_masc_pl]
#print(lista_sust_m_p)

#########################################################

# Sustantivos femeninos plurales
sust_fem_pl = pd.read_csv('freeling/subclases/nc-f-p.csv', delimiter=' ')
#print(sust_fem_pl)

tupla_sust_fem_pl = [tuple(x) for x in sust_fem_pl.values]
#print(tupla_sust_fem_pl)

lista_sust_f_p = [w[0] for w in tupla_sust_fem_pl]
#print(lista_sust_f_p)

#########################################################
# Sustantivos comunes plurales
sust_com_pl = pd.read_csv('freeling/subclases/nc-c-p.csv', delimiter=' ')
#print(sust_com_pl)

tupla_sust_com_pl = [tuple(x) for x in sust_com_pl.values]
#print(tupla_sust_com_pl)

lista_sust_c_p = [w[0] for w in tupla_sust_com_pl]
#print(lista_sust_c_p)

#########################################################

# Sustantivos masculinos neutros (no hay)
#sust_masc_n = pd.read_csv('freeling/subclases/nc-m-n.csv', delimiter=' ')
#print(sust_masc_pl)

#tupla_sust_masc_n = [tuple(x) for x in sust_masc_n.values]
#print(tupla_sust_masc_n)

#lista_sust_m_n = [w[0] for w in tupla_sust_masc_n]
#print(lista_sust_m_n)

#########################################################

# Sustantivos femeninos neutros (no hay)
#sust_fem_n = pd.read_csv('freeling/subclases/nc-f-n.csv', delimiter=' ')
#print(sust_fem_n)

#tupla_sust_fem_n = [tuple(x) for x in sust_fem_n.values]
#print(tupla_sust_fem_n)

#lista_sust_f_p = [w[0] for w in tupla_sust_fem_n]
#print(lista_sust_f_n)

#########################################################
# Sustantivos comunes neutros
sust_com_n = pd.read_csv('freeling/subclases/nc-c-n.csv', delimiter=' ')
#print(sust_com_n)

tupla_sust_com_n = [tuple(x) for x in sust_com_n.values]
#print(tupla_sust_com_n)

lista_sust_c_n = [w[0] for w in tupla_sust_com_n]
#print(lista_sust_c_n)

#########################################################

with open('freeling/fcfg/sust_para_gram.txt', 'w') as f:
    for item in lista_sust_m_s:
        f.write("N[GEN=masc, Num=sg] -> \'%s\'\n" % item)
    for item in lista_sust_f_s:
        f.write("N[GEN=fem, Num=sg] -> \'%s\'\n" % item)
    for item in lista_sust_c_s:
        f.write("N[GEN=?n, Num=sg] -> \'%s\'\n" % item)
    for item in lista_sust_m_p:
        f.write("N[GEN=masc, Num=pl] -> \'%s\'\n" % item)
    for item in lista_sust_f_p:
        f.write("N[GEN=fem, Num=pl] -> \'%s\'\n" % item)
    for item in lista_sust_c_p:
        f.write("N[GEN=?n, Num=pl] -> \'%s\'\n" % item)
#    for item in lista_sust_m_n:
#        f.write("N[GEN=masc, Num=n?] -> \'%s\'\n" % item)
#    for item in lista_sust_f_n:
#        f.write("N[GEN=fem, Num=?n] -> \'%s\'\n" % item)
    for item in lista_sust_c_n:
        f.write("N[GEN=?n, Num=?n] -> \'%s\'\n" % item)

##################################
# Armado del léxico de adverbios #
##################################

# Adverbios
advs = pd.read_csv('freeling/MM.adv.csv', delimiter=' ')
#print(advs)

tupla_advs = [tuple(x) for x in advs.values]
#print(tupla_advs)

lista_advs = [w[0] for w in tupla_advs]
#print(lista_advs)

with open('freeling/fcfg/advs_para_gram.txt', 'w') as f:
    for item in lista_advs:
        f.write("ADV -> \'%s\'\n" % item)


###########################################
# Armado del léxico de verbos principales #
###########################################


# Verbos 1era persona singular
verbs1s = pd.read_csv('freeling/subclases/v-1-s.csv', delimiter=' ')
#print(verbs1s)

tupla_verbs1s = [tuple(x) for x in verbs1s.values]
#print(tupla_verbs1s)

lista_verbs1s = [w[0] for w in tupla_verbs1s]
#print(lista_verbs1s)

##########################################

# Verbos 1era persona plural
verbs1p = pd.read_csv('freeling/subclases/v-1-p.csv', delimiter=' ')
#print(verbs1p)

tupla_verbs1p = [tuple(x) for x in verbs1p.values]
#print(tupla_verbs1p)

lista_verbs1p = [w[0] for w in tupla_verbs1p]
#print(lista_verbs1p)

#######################################################

# Verbos 2nda persona singular
verbs2s = pd.read_csv('freeling/subclases/v-2-s.csv', delimiter=' ')
#print(verbs2s)

tupla_verbs2s = [tuple(x) for x in verbs2s.values]
#print(tupla_verbs2s)

lista_verbs2s = [w[0] for w in tupla_verbs2s]
#print(lista_verbs2s)

#######################################################

# Verbos 2nda persona plural
verbs2p = pd.read_csv('freeling/subclases/v-2-p.csv', delimiter=' ')
#print(verbs2p)

tupla_verbs2p = [tuple(x) for x in verbs2p.values]
#print(tupla_verbs2p)

lista_verbs2p = [w[0] for w in tupla_verbs2p]
#print(lista_verbs2p)

#######################################################

# Verbos 3era persona singular
verbs3s = pd.read_csv('freeling/subclases/v-3-s.csv', delimiter=' ')
#print(verbs3s)

tupla_verbs3s = [tuple(x) for x in verbs3s.values]
#print(tupla_verbs3s)

lista_verbs3s = [w[0] for w in tupla_verbs3s]
#print(lista_verbs3s)

#######################################################

# Verbos 3era persona plural
verbs3p = pd.read_csv('freeling/subclases/v-3-p.csv', delimiter=' ')
#print(verbs3p)

tupla_verbs3p = [tuple(x) for x in verbs3p.values]
#print(tupla_verbs3p)

lista_verbs3p = [w[0] for w in tupla_verbs3p]
#print(lista_verbs3p)

#######################################################


with open('freeling/fcfg/verbs_para_gram.txt', 'w') as f:
    for item in lista_verbs1s:
        f.write("V[Num=sg, Per=1] -> \'%s\'\n" % item)
    for item in lista_verbs1p:
        f.write("V[Num=pl, Per=1] -> \'%s\'\n" % item)
    for item in lista_verbs2s:
        f.write("V[Num=sg, Per=2] -> \'%s\'\n" % item)
    for item in lista_verbs2p:
        f.write("V[Num=pl, Per=2] -> \'%s\'\n" % item)
    for item in lista_verbs3s:
        f.write("V[Num=sg, Per=3] -> \'%s\'\n" % item)
    for item in lista_verbs3p:
        f.write("V[Num=pl, Per=3] -> \'%s\'\n" % item)

# Finalmente se compilan los léxicos de cada clase de palabra con la gramática GramaticaDeRasgos.txt

###########################################
# Compilación de todos los léxicos en uno #
###########################################

filenames = ['GramaticaDeRasgos.txt', 'freeling/fcfg/verbs_para_gram.txt', 'freeling/fcfg/advs_para_gram.txt', 'freeling/fcfg/sust_para_gram.txt', 'freeling/fcfg/adjs_para_gram.txt']
with open('gram_para_fcfg.fcfg', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)




