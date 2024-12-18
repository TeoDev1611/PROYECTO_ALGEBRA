# Intérprete Avanzado de Lógica Proposicional

## Descripción del Proyecto

El **Intérprete Avanzado de Lógica Proposicional** es una herramienta diseñada para analizar proposiciones escritas en lenguaje natural, identificar conectores lógicos, manejar negaciones y generar tablas de verdad. Este proyecto tiene como objetivo facilitar la enseñanza, aprendizaje y aplicación de la lógica proposicional mediante una solución interactiva y extensible.

El intérprete se desarrolló en Python, utilizando programación orientada a objetos y expresiones regulares para el reconocimiento de patrones. Además, se planea la implementación de una interfaz gráfica (GUI) para mejorar la experiencia del usuario, permitiendo ingresar proposiciones y obtener resultados de forma visual y accesible.

## Características del Intérprete

1. **Análisis de Proposiciones**
   - Reconocimiento de conectores lógicos como "y", "o", "si... entonces", entre otros.
   - División de las proposiciones en componentes fundamentales.

2. **Reconocimiento de Negaciones**
   - Identificación de palabras de negación como "no", "nunca", "jamás".
   - Aplicación lógica de negaciones a proposiciones.

3. **Generación de Tablas de Verdad**
   - Creación automática de tablas de verdad para proposiciones simples y compuestas.
   - Visualización clara de valores de verdad.

4. **Evaluación de Expresiones**
   - Resolución de proposiciones con operadores como conjunción (∧), disyunción (∨), condicional (→) y bicondicional (↔).
   - Manejo de negaciones en proposiciones.

5. **Formato y Visualización**
   - Formateo profesional de tablas de verdad para su lectura y análisis.

6. **Extensibilidad**
   - Diseño modular que permite agregar conectores y funcionalidades adicionales.

## Tecnologías Utilizadas

- **Lenguaje**: Python
- **Principios**: Programación orientada a objetos
- **Librerías y Herramientas**:
  - `re` para manejo de expresiones regulares.
  - `itertools` para generar combinaciones en tablas de verdad.
  - `tkinter` para generar la interfaz gráfica

## Instalación:

Para iniciar con la instalación es necesario conocer que es importante para esto tener instalado python y git.

Como primer paso es necesario descargar el código para eso utilizaremos:
```
git clone https://github.com/TeoDev1611/PROYECTO_ALGEBRA.git
```

### Uso de Interfaz Gráfica

Para la interfaz gráfica solo es necesario llegar a la carpeta donde se encuentra el código y colocar:
```
python ui.py
```
### Uso de la consola

Se tiene un programa en consola con ya proposiciones específicas listas para solo visualizar los datos para eso es necesario colocar:
```
pip install termcolor
python console.py
```

### Uso como librería

#### Intérprete Lógico en Español

Esta librería proporciona un intérprete para analizar proposiciones lógicas en español y generar sus correspondientes tablas de verdad.

#### Características

- Análisis de proposiciones lógicas en lenguaje natural
- Detección de conectores lógicos (y, o, si-entonces, etc.)
- Identificación de negaciones
- Generación de tablas de verdad
- Soporte para múltiples tipos de conectores:
  - Condicionales (→)
  - Conjunciones (∧)
  - Disyunciones (∨)
  - Causales (→)
  - Adversativos (∧)
  - Consecutivos (→)
  - Explicativos (↔)

#### Instalación

```bash
# Asumiendo que tienes el archivo interpreter.py en tu proyecto
from interpreter import InterpreteLógico
```

#### Uso Básico

```python
# Crear una instancia del intérprete
interprete = InterpreteLógico()

# Analizar una proposición
proposicion = "Si llueve entonces me mojo"
resultado = interprete.parse_proposition(proposicion)

# Generar tabla de verdad
tabla = interprete.generate_truth_table(resultado)
tabla_formateada = interprete.format_truth_table(tabla)
print(tabla_formateada)
```

#### Métodos Principales

##### parse_proposition(text: str) -> Dict

Analiza una proposición y devuelve un diccionario con su estructura lógica.

```python
resultado = interprete.parse_proposition("Si llueve entonces me mojo")
# Devuelve:
# {
#     'connector': 'si',
#     'connector_type': 'CONDICIONAL',
#     'propositions': ['llueve', 'me mojo'],
#     'symbol': '→',
#     'negations': [False, False]
# }
```

##### generate_truth_table(parsed_prop: Dict) -> List[List[str]]

Genera una tabla de verdad para la proposición analizada.

```python
tabla = interprete.generate_truth_table(resultado)
tabla_formateada = interprete.format_truth_table(tabla)
```

#### Ejemplos de Uso

##### 1. Análisis Simple

```python
interprete = InterpreteLógico()
proposicion = "El cielo es azul y los pájaros vuelan"
resultado = interprete.parse_proposition(proposicion)
print(f"Conector: {resultado['connector']}")  # 'y'
print(f"Tipo: {resultado['connector_type']}")  # 'CONJUNCIÓN'
```

##### 2. Manejo de Negaciones

```python
proposicion = "No llueve y hace sol"
resultado = interprete.parse_proposition(proposicion)
print(f"Negaciones: {resultado['negations']}")  # [True, False]
```

##### 3. Generación de Tabla de Verdad

```python
proposicion = "Si estudias entonces apruebas"
resultado = interprete.parse_proposition(proposicion)
tabla = interprete.generate_truth_table(resultado)
print(interprete.format_truth_table(tabla))
```

#### Conectores Soportados

La librería soporta varios tipos de conectores en español:

- **Condicionales**: si, entonces, siempre que
- **Conjunciones**: y, además, también
- **Disyunciones**: o, o bien, ya sea
- **Adversativos**: pero, sin embargo, aunque
- **Causales**: porque, puesto que, ya que
- **Consecutivos**: por lo tanto, en consecuencia
- **Explicativos**: es decir, o sea

#### Negaciones Soportadas

La librería reconoce varias formas de negación:

- no
- nunca
- jamás
- tampoco
- ni
- ningún/ninguno
- nadie
- nada
- sin
- ni siquiera

#### Limitaciones

- Solo procesa proposiciones con un conector principal
- Las tablas de verdad se generan para proposiciones con exactamente dos componentes
- No maneja proposiciones complejas con múltiples conectores anidados