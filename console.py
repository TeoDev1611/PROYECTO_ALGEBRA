## Código Comentado

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

from typing import Dict, List  # Importa tipos de datos para anotaciones
from termcolor import colored  # Importa la función para colorear texto en la consola
from interpreter import InterpreteLógico  # Importa la clase que maneja el análisis lógico

def analyze_proposition(text: str) -> str:
    """
    Función principal para analizar una proposición.
    
    Args:
        text (str): Proposición a analizar
        
    Returns:
        str: Resultado del análisis incluyendo la tabla de verdad
    """
    interpreter = InterpreteLógico()  # Crea una instancia del intérprete lógico
    parsed = interpreter.parse_proposition(text)  # Analiza la proposición dada
    
    print("\nRESULTADO DEL ANÁLISIS:")  # Imprime el encabezado del resultado
    print(f"PROPOSICIÓN ORIGINAL: {colored(text, None, attrs=['underline'])}")  # Muestra la proposición original subrayada
    
    if parsed['connector']:  # Verifica si se identificó un conector lógico
        print(f"{colored('Conector identificado:', 'red', attrs=['underline'])}'{parsed['connector']}'")  # Muestra el conector identificado
        print(f"{colored('Tipo de conector:', 'green', attrs=['underline'])} {parsed['connector_type']}")  # Muestra el tipo de conector
        print(f"{colored('Símbolo lógico:', 'light_cyan', attrs=['underline'])} {parsed['symbol']}")  # Muestra el símbolo lógico correspondiente
        print(f"Proposiciones identificadas:")  # Indica que se listarán las proposiciones identificadas
        
        for i, (prop, neg) in enumerate(zip(parsed['propositions'], parsed['negations']), 1):  # Itera sobre las proposiciones y sus negaciones
            negation_str = "NEGADA" if neg else "NO NEGADA"  # Determina si la proposición está negada
            print(f"  P{i}: {colored(prop, attrs=['underline'])} ({negation_str})")  # Muestra cada proposición con su estado de negación
        
        print(f"\n{colored('Tabla de verdad:', 'green', attrs=['bold'])}")  # Imprime el encabezado de la tabla de verdad
        truth_table = interpreter.generate_truth_table(parsed)  # Genera la tabla de verdad
        return interpreter.format_truth_table(truth_table)  # Formatea y devuelve la tabla de verdad
    else:
        return "No se encontró ningún conector lógico en la proposición."  # Mensaje si no se encuentra un conector

# Ejemplos de uso con negaciones
if __name__ == "__main__":  # Verifica si el script se está ejecutando directamente
    proposiciones_ejemplo = [  # Lista de proposiciones de ejemplo
        "Si no llueve, entonces el suelo está seco",
        "No hace sol y hace frío",
        "Estudia o no aprueba el examen",
        "No está cansado porque durmió mucho",
        "No fue a clase, por lo tanto no aprobó",
        "No es inteligente, es decir, no aprende rápido",
        "Aunque no hace frío, no iremos al parque",
        "Ya sea no comes o no duermes"
    ]

    for prop in proposiciones_ejemplo:  # Itera sobre cada proposición de ejemplo
        print("\n" + "="*50)  # Imprime una línea separadora
        result = analyze_proposition(prop)  # Llama a la función de análisis para cada proposición
        print(result)  # Imprime el resultado del análisis