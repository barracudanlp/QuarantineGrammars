class NoMapping(Exception):
    pass


class MakeRule:
    
    def __init__(self,word_dict,tags_mapping):
        
        self.tag = word_dict.get("tag")
        self.lemma = word_dict.get("lema")
        self.shape = word_dict.get("forma")
        self.category = self.tag[0]
        self.mapping = tags_mapping.get(self.category)

        if self.mapping:

            for k in self.mapping.keys():
                setattr(self,k,self._get_mapped_tag(k))

            self.rule = self._make_rule()
            
        else:
            raise NoMapping(f"No mapping for {self.category}")
                
    def _get_mapped_tag(self,rasgo):
        rasgo_mapping = self.mapping.get(rasgo)
        position_tag = rasgo_mapping.get("posicion")
        return rasgo_mapping.get(self.tag[position_tag],self.tag[position_tag])
                
    def _make_rule(self):
        # Habría que agregar un elif por cada categoría a la que le definamos el mapeo de keys.
        # Los atributos son las keys del diccionario. category, shape y lemma siempre se llaman
        # así porque se definen antes (es para todas las clases de palabras igual)
        # Está así cortado para que sea más legible, pero podría estar todo en una línea
        if self.category == "V":
            rule = f"{self.category}[SUBCAT={self.subcategoria},MODE={self.modo},"\
                    f"TENSE={self.tiempo},PER={self.persona},"\
                    f"NUM={self.numero},SEM=<\e.({self.lemma}(e) "\
                    f"& {self.tiempo}(e))>] -> '{self.shape}'"
        if self.category == "N":
            rule = f"{self.category}[NUM={self.numero},GEN={self.genero},"\
                    f"SEM=<\\x.({self.lemma}(x))>] -> '{self.shape}'"
        if self.category == "A":
            if self.subcategoria != "pron":
                rule = f"{self.category}[NUM={self.numero},GEN={self.genero},"\
                    f"SUBCAT={self.subcategoria}, FUNCTION={self.funcion},"\
                    f"SEM=<\\x.({self.lemma}(x))>] -> '{self.shape}'"
            elif self.category == "A" and self.subcategoria == "pron":
                rule = f"{self.category}[NUM={self.numero},GEN={self.genero},"\
                    f"SUBCAT={self.subcategoria},"\
                    f"SEM=<\\x.(de-{self.funcion}-persona(x))>] -> '{self.shape}'"
        return rule