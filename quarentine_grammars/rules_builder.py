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
            f"SEM=<\\x.(de-{self.funcion}-persona(x))>"
        ]
        return feats

# Habría que agregar las preposiciones en el json, pero no sé muy bien cómo 
# hacer porque estaría bueno que le quede de categoría Prep en lugar de S, ya que
# S lo tenemos reservado para la raíz, entonces hay que revisar para que ante S
# en la posición cero redefina el self.category como Prep. 
#
    def _Prep_feats(self):
        """
            Define los features de una preposición
            ...

            Returns
            ----------
            feats: list
                Lista de features
        """
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



#    def _P_feats(self):
#        """
#            Define subtipos de pronombre.
#        """
#        if self.subcategoria == "pers":
#            feats = self._personal_feats()
#        if self.subcategoria == "dem":
#            feats = self._demonstratives_feats()
#        if self.subcategoria == "pos":
#            feats = self._possesives_feats()
#        if self.subcategoria == "indet":
#            feats = self._indeterminate_feats()
#        if self.subcategoria == "inter":
#            feats = self._interrogative_feats()
#        if self.subcategoria == "relat":
#            feats = self._relative_feats()
#        if self.subcategoria == "exclam":
#            feats = self._exclamative_feats()
#
#    def _personal_feats(self):
#        """
#            Define los features de un pronombre personal.
#            ...
#
#            Returns
#            ----------
#            feats: list
#                Lista de features
#        """
#        feats = [
#            f"NUM={self.numero}",
#            f"GEN={self.genero}",
#            f"PER={self.persona}",
#            f"SEM=<\\P. (P(iota x. ({self.persona}-persona(x))))>"
#        ]
#        return feats
#
#    def _demonstratives_feats(self):
#        """
#            Define los features de un pronombre demostrativo.
#            ...
#
#            Returns
#            ----------
#            feats: list
#                Lista de features
#        """
#        feats = [
#            f"NUM={self.numero}",
#            f"GEN={self.genero}",
#            f"SEM=<\\P Q. (Q(iota x. {self.numero}(x) & P(x)))>"
#        ]
#        return feats
#
#    def _possesives_feats(self):
#        """
#            Define los features de un pronombre posesivo.
#            ...
#
#            Returns
#            ----------
#            feats: list
#                Lista de features
#        """
#        feats = [
#            f"NUM={self.numero}",
#            f"PER={self.persona}",
#            f"GEN={self.genero}",
#            f"SEM=<\\x.(de-{self.persona}-persona(x))>"
#        ]
#        return feats
#
#    def _interrogative_feats(self):
#        """
#            Define los features de un pronombre interrogativos.
#            ...
#
#            Returns
#            ----------
#            feats: list
#                Lista de features
#        """
#        feats = [
#            f"NUM={self.numero}",
#            f"GEN={self.genero}",
#            f"SEM=<\\P. (P(x))>"
#        ]
#        return feats


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
        self.lemma = word_dict.get("lema")
        self.shape = word_dict.get("forma")
        if tag[0] == "S":
            self.category = "Prep"
        else:
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
