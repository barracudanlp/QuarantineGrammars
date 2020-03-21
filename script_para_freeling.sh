mkdir -p freeling/subclases

cat freeling/MM.adj.txt| grep 'FS' > freeling/subclases/adjs-f-s.csv
cat freeling/MM.adj.txt| grep 'CP' > freeling/subclases/adjs-c-p.csv
cat freeling/MM.adj.txt| grep 'CS' > freeling/subclases/adjs-c-s.csv
cat freeling/MM.adj.txt| grep 'MS' > freeling/subclases/adjs-m-s.csv
cat freeling/MM.adj.txt| grep 'MP' > freeling/subclases/adjs-m-p.csv
cat freeling/MM.adj.txt| grep 'FP' > freeling/subclases/adjs-f-p.csv
cat freeling/MM.adj.txt| grep 'CN' > freeling/subclases/adjs-c-n.csv
cat freeling/MM.adj.txt| grep 'FN' > freeling/subclases/adjs-f-n.csv
cat freeling/MM.adj.txt| grep 'MN' > freeling/subclases/adjs-m-n.csv

cat freeling/MM.nom.txt| grep 'NCMS' > freeling/subclases/nc-m-s.csv
cat freeling/MM.nom.txt| grep 'NCFS' > freeling/subclases/nc-f-s.csv
cat freeling/MM.nom.txt| grep 'NCCS' > freeling/subclases/nc-c-s.csv
cat freeling/MM.nom.txt| grep 'NCMP' > freeling/subclases/nc-m-p.csv
cat freeling/MM.nom.txt| grep 'NCFP' > freeling/subclases/nc-f-p.csv
cat freeling/MM.nom.txt| grep 'NCCP' > freeling/subclases/nc-c-p.csv
cat freeling/MM.nom.txt| grep 'NCMN' > freeling/subclases/nc-m-n.csv
cat freeling/MM.nom.txt| grep 'NCFN' > freeling/subclases/nc-f-n.csv
cat freeling/MM.nom.txt| grep 'NCCN' > freeling/subclases/nc-c-n.csv

cat freeling/MM.verb.txt| grep 'VM..3S' > freeling/subclases/v-3-s.csv
cat freeling/MM.verb.txt| grep 'VM..3P' > freeling/subclases/v-3-p.csv
cat freeling/MM.verb.txt| grep 'VM..1S' > freeling/subclases/v-1-s.csv
cat freeling/MM.verb.txt| grep 'VM..1P' > freeling/subclases/v-1-p.csv
cat freeling/AR.verb.txt| grep 'VM..2S' > freeling/subclases/v-2-s.csv
cat freeling/MM.verb.txt| grep 'VM..3P' > freeling/subclases/v-2-p.csv

