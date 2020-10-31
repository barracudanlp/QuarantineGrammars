class LexicalRule():
    
    def build_lexical_rule(self):
        feats = str(getattr(self,f"_{self.category}_feats")()).replace("'","").replace("\\\\","\\")
        lex_rule = f"{self.category}{feats} -> '{self.shape}'"
        return lex_rule

    def _V_feats(self):
        feats = [
            f"SUBCAT={self.subcategoria}",
            f"MODE={self.modo}",
            f"TENSE={self.tiempo}",
            f"PER={self.persona}",
            f"NUM={self.numero}",
            f"SEM=<\e.({self.lemma}(e) & {self.tiempo}(e))>"
        ]
        return feats

    def _N_feats(self):
        feats = [
            f"NUM={self.numero}",
            f"GEN={self.genero}",
            f"SEM=<\\x.({self.lemma}(x))>"
        ]
        return feats

    def _pronoun_feats(self):
        feats = [
            f"NUM={self.numero}",
            f"GEN={self.genero}",
            f"SEM=<\\x.(de-{self.funcion}-persona(x))>"
        ]
        return feats

    def _A_feats(self):
        if subcategoria == "pron":
            feats = self._pronoun_feats(self)
        else:
            feats = [
                f"NUM={self.numero}",
                f"GEN={self.genero}",
                f"FUNCTION={self.funcion}",
                f"SEM=<\\x.({self.lemma}(x))>"
            ]
        return feats

class NoMapping(Exception):
    pass

class MakeRule(LexicalRule):
    
    def __init__(self,word_dict,tags_mapping):
        
        tag = word_dict.get("tag")
        self.lemma = word_dict.get("lema")
        self.shape = word_dict.get("forma")
        self.category = tag[0]
        mapping = tags_mapping.get(self.category)

        if mapping:
            for k in mapping.keys():
                setattr(self,k,self._get_mapped_tag(mapping.get(k),tag))
            self.rule = self._make_rule()            
        else:
            raise NoMapping(f"No mapping for {self.category}")
                
    def _get_mapped_tag(self,rasgo_mapping,tag):
        position_tag = rasgo_mapping.get("posicion")
        return rasgo_mapping.get(tag[position_tag],tag[position_tag])
                
    def _make_rule(self):
        rule = self.build_lexical_rule()
        return rule