"""
Intérprete Avanzado de Lógica Proposicional
==========================================

Este módulo implementa un intérprete de lógica proposicional que puede:
- Analizar proposiciones en lenguaje natural
- Identificar diferentes tipos de conectores lógicos
- Manejar negaciones
- Generar tablas de verdad
- Evaluar expresiones lógicas
"""

from typing import Dict, List
from termcolor import colored
from interpreter.parser import InterpreteLógico

def analyze_proposition(text: str) -> str:
    """
    Función principal para analizar una proposición.
    
    Args:
        text (str): Proposición a analizar
        
    Returns:
        str: Resultado del análisis incluyendo la tabla de verdad
    """
    interpreter = InterpreteLógico()
    parsed = interpreter.parse_proposition(text)
    
    print("\nRESULTADO DEL ANÁLISIS:")
    print(f"PROPOSICIÓN ORIGINAL: {colored(text, None, attrs=["underline"])}")
    
    if parsed['connector']:
        print(f"{colored("Conector identificado:", "red", attrs=["underline"] )}'{parsed['connector']}'")
        print(f"{colored("Tipo de conector:", "green", attrs=["underline"])} {parsed['connector_type']}")
        print(f"{colored("Símbolo lógico:", "light_cyan", attrs=["underline"])} {parsed['symbol']}")
        print(f"Proposiciones identificadas:")
        
        for i, (prop, neg) in enumerate(zip(parsed['propositions'], 
                                          parsed['negations']), 1):
            negation_str = "NEGADA" if neg else "NO NEGADA"
            print(f"  P{i}: {colored(prop, attrs=["underline"])} ({negation_str})")
        
        print(f"\n{colored("Tabla de verdad:", "green", attrs=["bold"])}")
        truth_table = interpreter.generate_truth_table(parsed)
        return interpreter.format_truth_table(truth_table)
    else:
        return "No se encontró ningún conector lógico en la proposición."

# Ejemplos de uso con negaciones
if __name__ == "__main__":
    proposiciones_ejemplo = [
        "Si no llueve, entonces el suelo está seco",
        "No hace sol y hace frío",
        "Estudia o no aprueba el examen",
        "No está cansado porque durmió mucho",
        "No fue a clase, por lo tanto no aprobó",
        "No es inteligente, es decir, no aprende rápido",
        "Aunque no hace frío, no iremos al parque",
        "Ya sea no comes o no duermes"
    ]

    for prop in proposiciones_ejemplo:
        print("\n" + "="*50)
        result = analyze_proposition(prop)
        print(result)