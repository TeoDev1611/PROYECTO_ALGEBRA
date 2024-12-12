from itertools import product
from typing import Tuple, Union, Dict, List


class InterpreteLógico:
    """
    Clase principal para el análisis y evaluación de proposiciones lógicas.
    
    Attributes:
        KEY_WORDS (dict): Diccionario de palabras clave y sus tipos de conectores
        LOGICAL_OPERATIONS (dict): Mapeo de tipos de conectores a símbolos lógicos
        NEGATIONS (list): Lista de palabras que indican negación
    """
    
    def __init__(self):
        """Inicializa el intérprete con sus diccionarios y listas de palabras clave."""
        
        # Palabras que indican negación
        self.NEGATIONS = [
            "no", "nunca", "jamás", "tampoco", "ni", "ningún", "ninguno",
            "nadie", "nada", "sin", "ni siquiera"
        ]
        
        # Diccionario de palabras clave y sus tipos
        self.KEY_WORDS = {
            # Conectores condicionales
            "si": "CONDICIONAL",
            "entonces": "CONDICIONAL",
            "siempre que": "CONDICIONAL",
            "a condición de que": "CONDICIONAL",
            
            # Conectores de conjunción
            "y": "CONJUNCIÓN",
            "además": "CONJUNCIÓN",
            "también": "CONJUNCIÓN",
            "ni": "CONJUNCIÓN",
            
            # Conectores de disyunción
            "o": "DISYUNCIÓN",
            "o bien": "DISYUNCIÓN",
            "ya sea": "DISYUNCIÓN",
            
            # Conectores adversativos
            "pero": "ADVERSATIVO",
            "sin embargo": "ADVERSATIVO",
            "no obstante": "ADVERSATIVO",
            "aunque": "ADVERSATIVO",
            
            # Conectores causales
            "porque": "CAUSAL",
            "puesto que": "CAUSAL",
            "ya que": "CAUSAL",
            "dado que": "CAUSAL",
            
            # Conectores consecutivos
            "por lo tanto": "CONSECUTIVO",
            "en consecuencia": "CONSECUTIVO",
            "por consiguiente": "CONSECUTIVO",
            "así que": "CONSECUTIVO",
            
            # Otros conectores
            "es decir": "EXPLICATIVO",
            "o sea": "EXPLICATIVO",
            "por ejemplo": "EJEMPLIFICATIVO"
        }
        
        # Mapeo de conectores a símbolos lógicos
        self.LOGICAL_OPERATIONS = {
            "CONDICIONAL": "→",
            "CONJUNCIÓN": "∧",
            "DISYUNCIÓN": "∨",
            "ADVERSATIVO": "∧",
            "CAUSAL": "→",
            "CONSECUTIVO": "→",
            "EXPLICATIVO": "↔",
            "EJEMPLIFICATIVO": "→"
        }
    
    def check_negation(self, proposition: str) -> Tuple[bool, str]:
        """
        Verifica si una proposición contiene una negación y la procesa.
        
        Args:
            proposition (str): La proposición a analizar
            
        Returns:
            Tuple[bool, str]: (tiene_negación, proposición_sin_negación)
        """
        proposition = proposition.lower().strip()
        is_negated = False
        
        for neg in self.NEGATIONS:
            if proposition.startswith(neg + " "):
                is_negated = True
                proposition = proposition[len(neg):].strip()
            elif f" {neg} " in proposition:
                is_negated = True
                proposition = proposition.replace(f" {neg} ", " ").strip()
        
        return is_negated, proposition

    def find_connector(self, text: str) -> Union[str, None]:
        """
        Encuentra el primer conector lógico en el texto.
        
        Args:
            text (str): El texto a analizar
            
        Returns:
            Union[str, None]: El conector encontrado o None
        """
        text = text.lower()
        sorted_connectors = sorted(self.KEY_WORDS.keys(), key=len, reverse=True)
        
        for connector in sorted_connectors:
            if connector in text:
                return connector
        return None

    def parse_proposition(self, text: str) -> Dict:
        """
        Analiza una proposición y extrae sus componentes.
        
        Args:
            text (str): La proposición a analizar
            
        Returns:
            Dict: Diccionario con los componentes de la proposición
        """
        text = text.lower().strip('.')
        connector = self.find_connector(text)
        
        if not connector:
            is_negated, clean_text = self.check_negation(text)
            return {
                'connector': None,
                'connector_type': None,
                'propositions': [text],
                'symbol': None,
                'negations': [is_negated]
            }
        
        connector_type = self.KEY_WORDS[connector]
        logical_symbol = self.LOGICAL_OPERATIONS[connector_type]
        
        parts = text.split(connector)
        propositions = []
        negations = []
        
        for part in parts:
            is_negated, clean_prop = self.check_negation(part.strip())
            propositions.append(clean_prop)
            negations.append(is_negated)
        
        return {
            'connector': connector,
            'connector_type': connector_type,
            'propositions': propositions,
            'symbol': logical_symbol,
            'negations': negations
        }
    
    def evaluate_expression(self, values: Tuple[bool, bool], 
                          connector_type: str, 
                          negations: List[bool]) -> bool:
        """
        Evalúa una expresión lógica considerando negaciones.
        
        Args:
            values (Tuple[bool, bool]): Valores de verdad de las proposiciones
            connector_type (str): Tipo de conector lógico
            negations (List[bool]): Lista de negaciones para cada proposición
            
        Returns:
            bool: Resultado de la evaluación
        """
        p, q = values
        
        # Aplicar negaciones si existen
        if negations[0]:
            p = not p
        if len(negations) > 1 and negations[1]:
            q = not q
        
        if connector_type in ["CONDICIONAL", "CAUSAL", "CONSECUTIVO"]:
            return not p or q
        elif connector_type in ["CONJUNCIÓN", "ADVERSATIVO"]:
            return p and q
        elif connector_type == "DISYUNCIÓN":
            return p or q
        elif connector_type == "EXPLICATIVO":
            return p == q
        elif connector_type == "EJEMPLIFICATIVO":
            return not p or q
        
        return None

    def generate_truth_table(self, parsed_prop: Dict) -> List[List[str]]:
        """
        Genera una tabla de verdad para la proposición.
        
        Args:
            parsed_prop (Dict): Proposición analizada
            
        Returns:
            List[List[str]]: Tabla de verdad formateada
        """
        if not parsed_prop['connector_type'] or len(parsed_prop['propositions']) != 2:
            return "No se pudo generar la tabla de verdad"
        
        combinations = list(product([True, False], repeat=2))
        
        # Crear encabezados con negaciones si existen
        p_header = "¬p" if parsed_prop['negations'][0] else "p"
        q_header = "¬q" if parsed_prop['negations'][1] else "q"
        
        table = []
        headers = [p_header, q_header, f"{p_header} {parsed_prop['symbol']} {q_header}"]
        table.append(headers)
        
        for values in combinations:
            result = self.evaluate_expression(
                values, 
                parsed_prop['connector_type'],
                parsed_prop['negations']
            )
            row = ["V" if v else "F" for v in [values[0], values[1], result]]
            table.append(row)
            
        return table

    def format_truth_table(self, table: List[List[str]]) -> str:
        """
        Formatea la tabla de verdad para su visualización.
        
        Args:
            table (List[List[str]]): Tabla de verdad sin formato
            
        Returns:
            str: Tabla de verdad formateada
        """
        if not isinstance(table, list):
            return table
            
        widths = [max(len(str(row[i])) for row in table) for i in range(len(table[0]))]
        lines = []
        
        header = "| " + " | ".join(str(cell).center(widths[i]) 
                                  for i, cell in enumerate(table[0])) + " |"
        lines.append("=" * len(header))
        lines.append(header)
        lines.append("=" * len(header))
        
        for row in table[1:]:
            lines.append("| " + " | ".join(str(cell).center(widths[i]) 
                                         for i, cell in enumerate(row)) + " |")
        lines.append("=" * len(header))
        
        return "\n".join(lines)
