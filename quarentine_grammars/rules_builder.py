class LexicalFeatures():
    
    def _V_feats(self):
        """
            Define los features de un verbo
            ...

            Returns
            ----------
            feats: list
                Lista de features
        """
        if self.modo == "PPIO":
            feats = self._participle_feats()
        elif self.subcategoria == "S":
            feats = self._auxiliar_feats()
        elif self.subcategoria == "A":
            feats = self._auxiliar_feats()
        else:
            feats = [
                f"SUBCAT={self.subcategoria}",
                f"LEMA={self.lemma}",
            	f"MODE={self.modo}",
            	f"TENSE={self.tiempo}",
            	f"PER={self.persona}",
            	f"NUM={self.numero}",
            	f"SEM=<\e.({self.lemma}(e) & {self.tiempo}(e))>"
            ]
        return feats

    def _participle_feats(self):
        """
            Define los features de un participio
            ...

            Returns
            ----------
            feats: list
                Lista de features
        """
        feats = [
            f"SUBCAT={self.subcategoria}",
            f"MODE={self.modo}",
            f"PER={self.persona}",
            f"NUM={self.numero}",
            f"SEM=<\e.({self.lemma}(e))>"
        ]
        return feats

    def _auxiliar_feats(self):
        """
            Define los features de un auxiliar
            ...

            Returns
            ----------
            feats: list
                Lista de features
        """
        feats = [
            f"SUBCAT={self.subcategoria}",
            f"LEMA={self.lemma}",
            f"MODE={self.modo}",
            f"TENSE={self.tiempo}",
            f"PER={self.persona}",
            f"NUM={self.numero}",
            f"SEM=<\e.({self.tiempo}(e))>"
        ]
        return feats

    def _N_feats(self):
        """
            Define los features de un sustantivo
            ...

            Returns
            ----------
            feats: list
                Lista de features
        """
        feats = [
            f"NUM={self.numero}",
            f"GEN={self.genero}",
            f"SEM=<\\x.({self.lemma}(x))>"
        ]
        return feats

    def _X_feats(self):
        """
            Define los features de una preposición
            ...

            Returns
            ----------
            feats: list
                Lista de features
        """
        if self.subcategoria == "prep":
            feats = [
                f"LEMA={self.lemma}",
                f"SEM=<\\x.({self.lemma}(x))>"
                ]
            
        return feats

    def _A_feats(self):
        """
            Define los features de un adjetivo o pronombre
            ...

            Returns
            ----------
            feats: list
                Lista de features
        """
        if self.subcategoria == "pron":
            feats = self._pronoun_feats()
        else:
            feats = [
                f"NUM={self.numero}",
                f"GEN={self.genero}",
                f"FUNCTION={self.funcion}",
                f"SEM=<\\x.({self.lemma}(x))>"
            ]
        return feats

    def _pronoun_feats(self):
        """
            Define los features de un pronombre
            ...

            Returns
            ----------
            feats: list
                Lista de features
        """
        feats = [
            f"NUM={self.numero}",
            f"GEN={self.genero}",
            f"SEM=<\\x.(de_{self.funcion}_persona(x))>"
        ]
        return feats
    
    def _D_feats(self):
        """
            Define los features de un determinante.
            ...

            Returns
            ----------
            feats: list
                Lista de features
        """
        if self.subcategoria == 'art':
            feats = self._article_feats()
        else: 
            feats = [
                f"NUM={self.numero}",
                f"GEN={self.genero}",
                f"PER={self.persona}",
                f"SUB={self.subcategoria}",            
                f"SEM=<\\x.({self.lemma}(x))>"
            ]
        return feats

    def _article_feats(self):
        """
            Define los features de un artículo.
            ...

            Returns
            ----------
            feats: list
                Lista de features
        """
        feats = [
            f"NUM={self.numero}",
            f"GEN={self.genero}",
            f"SEM=<\\P Q. (Q(iota x. ({self.numero}(x) & P(x))))>"
        ]
        return feats

    def _P_feats(self):
        """
            Define los features de un pronombre.
            ...

            Returns
            ----------
            feats: list
                Lista de features

        """
        #if self.subcategoria == "pers":
        #    feats = self._personal_feats()
        #elif self.subcategoria == "dem":
        #    feats = self._demonstratives_feats()
        #elif self.subcategoria == "pos":
        #    feats = self._possesives_feats()
        #elif self.subcategoria == "indet":
        #    feats = self._indeterminate_feats()
        #elif self.subcategoria == "inter":
        #    feats = self._interrogative_feats()
        #elif self.subcategoria == "relat":
        #    feats = self._relative_feats()
        #elif self.subcategoria == "exclam":
        #    feats = self._exclamative_feats()
        #else:
        feats = [
            f"NUM={self.numero}",
            f"GEN={self.genero}",
            f"PER={self.persona}",
            f"SEM=<\\P.(P(iota x. ({self.persona}_persona(x))))>"
        ]
        return feats

    def _personal_feats(self):
        """
            Define los features de un pronombre personal.
            ...

            Returns
            ----------
            feats: list
                Lista de features
        """
        feats = [
            f"NUM={self.numero}",
            f"GEN={self.genero}",
            f"PER={self.persona}",
            f"SEM=<\\P. (P(iota x. ({self.persona}_persona(x))))>"
        ]
        return feats

    #def _demonstratives_feats(self):
    #    """
    #        Define los features de un pronombre demostrativo.
    #        ..
    #        Returns
    #        ----------
    #        feats: list
    #            Lista de features
    #    """
    #    feats = [
    #        f"NUM={self.numero}",
    #        f"GEN={self.genero}",
    #        f"SEM=<\\P Q. (Q(iota x. {self.numero}(x) & P(x)))>"
    #    ]
    #    return feat
    #def _possesives_feats(self):
    #    """
    #        Define los features de un pronombre posesivo.
    #        ..
    #        Returns
    #        ----------
    #        feats: list
    #            Lista de features
    #    """
    #    feats = [
    #        f"NUM={self.numero}",
    #        f"PER={self.persona}",
    #        f"GEN={self.genero}",
    #        f"SEM=<\\x.(de-{self.persona}_persona(x))>"
    #    ]
    #    return feat
    #def _interrogative_feats(self):
    #    """
    #        Define los features de un pronombre interrogativos.
    #        ..
    #        Returns
    #        ----------
    #        feats: list
    #            Lista de features
    #    """
    #    feats = [
    #        f"NUM={self.numero}",
    #        f"GEN={self.genero}",
    #        f"SEM=<\\P. (P(x))>"
    #    ]
    #    return feats


class NoMapping(Exception):
    """
        No hay mapeo tag-feature para la clase de palabra
    """
    pass

class MakeRule(LexicalFeatures):
    
    def __init__(self,word_dict,tags_mapping):
        """
            Setea como atributos los features de una palabra
            obtenidos del cruce entre el diccionario taggeado
            y el mapeo tag-features.
            Guarda en el atributo "rule" la regla léxica correspondiente.
            Si no hay mapeo tag-feature para una clase de palabra,
            devuelve la excepción NoMapping.
            ...
            
            Parámetros
            ----------
            word_dict: dict
                Información de una acepción de la palabra en el vocabulario taggeado.
                forma: str
                    forma léxica
                lema: str
                    lema
                tag: str
                    tag asociado
            tags_mapping: dict
                Mapeo de los tags a los rasgos de la gramática con la estructura:
                [categoría]: dict
                    [rasgo]: dict
                        "posicion": int
                            Posición del rasgo en el tag del diccionario
                        [valor_posible_en_el_tag]: str
                            Nombre del valor del rasgo en la gramática
        """
        tag = word_dict.get("tag")
        lema = word_dict.get("lema")
        self.lemma = lema if len(lema) > 1 else f"_{lema}"
        self.shape = word_dict.get("forma")
        self.category = tag[0]
        mapping = tags_mapping.get(self.category)
        if mapping:
            for k in mapping.keys():
                setattr(self,k,self._get_mapped_tag(mapping.get(k),tag))
            self.rule = self._build_lexical_rule()
        else:
            raise NoMapping(f"No mapping for {self.category}")
                
    def _get_mapped_tag(self,rasgo_mapping,tag):
        """
            Obtiene el valor para un rasgo del tag y devuelve
            el nombre del rasgo en la gramática.
            Si el valor encontrado en el tag no está
            mapeado, devuelve el valor del tag.
            ...

            Parámetros
            ----------
            rasgo_mapping: dict
                Mapeo para un rasgo de la clase de palabra en cuestión
            tag:
                Tag del diccionario

            Returns
            ----------
            feature_value: str
                Valor del rasgo tal como lo interpreta la gramática
        """
        position_tag = rasgo_mapping.get("posicion")
        feature_value = rasgo_mapping.get(tag[position_tag],tag[position_tag])
        return feature_value

    def _build_lexical_rule(self):
        """
            Construye una regla léxica.
            Toma los features del método self._[categoría]_feats() correspondiente.
            ...

            Returns
            ----------
            lex_rule: str
                Regla con el formato: categoría[features] -> 'forma_léxica'
        """
        feats = str(getattr(self,f"_{self.category}_feats")()).replace("'","").replace("\\\\","\\")
        lex_rule = f"{self.category}{feats} -> '{self.shape}'"
        return lex_rule
