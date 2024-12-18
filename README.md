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

## Próximos Pasos

- **Interfaz Gráfica**: Implementar una GUI utilizando herramientas como Tkinter o PyQt para facilitar la interacción con el intérprete.
- **Extensión de Funcionalidades**:
  - Agregar soporte para lógica de predicados.
  - Exportación de resultados en formatos como PDF o Excel.

## Ejemplos de Uso

### Entrada
```plaintext
Si no llueve, entonces el suelo está seco.
