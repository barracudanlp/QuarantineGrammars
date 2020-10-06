#!/bin/bash

if [ -d MM.adj.txt ]; then
	rm MM.adj.txt
fi
if [ -d MM.adv.txt ]; then
	rm MM.adv.txt
fi
if [ -d MM.int.txt ]; then
	rm MM.int.txt
fi
if [ -d MM.nom.txt ]; then
	rm MM.nom.txt
fi
if [ -d MM.tanc.txt ]; then
	rm MM.tanc.txt
fi
if [ -d MM.vaux.txt ]; then
	rm MM.vaux.txt
fi
if [ -d MM.verb.txt ]; then
	rm MM.verb.txt
fi
if [ -d AR.verb.txt ]; then
	rm AR.verb.txt
fi


wget -O MM.adj.txt "https://raw.githubusercontent.com/TALP-UPC/FreeLing/master/data/es/dictionary/entries/MM.adj"
wget -O MM.adv.txt "https://raw.githubusercontent.com/TALP-UPC/FreeLing/master/data/es/dictionary/entries/MM.adv"
wget -O MM.int.txt "https://raw.githubusercontent.com/TALP-UPC/FreeLing/master/data/es/dictionary/entries/MM.int"
wget -O MM.nom.txt "https://raw.githubusercontent.com/TALP-UPC/FreeLing/master/data/es/dictionary/entries/MM.nom"
wget -O MM.tanc.txt "https://raw.githubusercontent.com/TALP-UPC/FreeLing/master/data/es/dictionary/entries/MM.tanc"
wget -O MM.vaux.txt "https://raw.githubusercontent.com/TALP-UPC/FreeLing/master/data/es/dictionary/entries/MM.vaux"
wget -O MM.verb.txt "https://raw.githubusercontent.com/TALP-UPC/FreeLing/master/data/es/dictionary/entries/MM.verb"
wget -O AR.verb.txt "https://raw.githubusercontent.com/TALP-UPC/FreeLing/master/data/es/es-ar/dictionary/entries/AR.verb"


