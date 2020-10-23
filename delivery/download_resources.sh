#!/bin/bash 


get_dict () {
	if [ -f $1.txt ]; then
		rm $1.txt
	fi
	if [[ $2 == "es" ]]; then
		wget -O $1.txt "https://raw.githubusercontent.com/TALP-UPC/FreeLing/master/data/es/dictionary/entries/$1"
	elif [[ $2 == "es-ar" ]]; then
		wget -O $1.txt "https://raw.githubusercontent.com/TALP-UPC/FreeLing/master/data/es/$2/dictionary/entries/$1"
	fi
}


get_dict MM.adj es
get_dict MM.adv es
get_dict MM.int es
get_dict MM.nom es
get_dict MM.tanc es
get_dict MM.vaux es
get_dict MM.verb es
get_dict AR.verb es-ar


pipenv run python download_resources.py