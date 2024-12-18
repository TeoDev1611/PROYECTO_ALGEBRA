import tkinter as tk
from tkinter import ttk, messagebox
from interpreter import InterpreteLógico

def analyze_proposition():
    """Función para analizar la proposición ingresada y mostrar resultados."""
    proposition = entry.get()  # Obtener la proposición del cuadro de entrada
    if not proposition:  # Verificar si la proposición está vacía
        messagebox.showwarning("Atención", "Por favor, ingrese una proposición y presione 'Analizar'.\nEjemplo: 'Si llueve, entonces llevaremos paraguas.'")
        reset_display()  # Restablecer la interfaz si no hay entrada
        return

    interpreter = InterpreteLógico()  # Crear una instancia del intérprete lógico
    parsed = interpreter.parse_proposition(proposition)  # Analizar la proposición ingresada

    if parsed['connector']:  # Verificar si se encontró un conector lógico
        prop_original_label.config(text="Proposición original:")  # Configurar la etiqueta de la proposición original
        prop_original_result.config(text=proposition)  # Mostrar la proposición original

        conector_label.config(text="Conector identificado:")  # Configurar la etiqueta del conector
        conector_result.config(text=f"'{parsed['connector']}'")  # Mostrar el conector identificado

        tipo_conector_label.config(text="Tipo de conector:")  # Configurar la etiqueta del tipo de conector
        tipo_conector_result.config(text=parsed['connector_type'])  # Mostrar el tipo de conector

        simbolo_label.config(text="Símbolo lógico:")  # Configurar la etiqueta del símbolo lógico
        simbolo_result.config(text=parsed['symbol'])  # Mostrar el símbolo lógico

        proposiciones_label.config(text="Proposiciones identificadas:")  # Configurar la etiqueta de proposiciones

        proposiciones_result = "\n".join([  # Crear una cadena con las proposiciones identificadas
            f"  P{i}: {prop} ({'negada' if neg else 'no negada'})"
            for i, (prop, neg) in enumerate(zip(parsed['propositions'], parsed['negations']), 1)
        ])
        proposiciones_result_label.config(text=proposiciones_result)  # Mostrar las proposiciones identificadas

        truth_table = interpreter.generate_truth_table(parsed)  # Generar la tabla de verdad
        table.delete(*table.get_children())  # Limpiar la tabla antes de insertar nuevos datos
        if isinstance(truth_table, str):  # Verificar si la tabla de verdad es una cadena
            table.insert("", tk.END, values=(truth_table,))  # Insertar el mensaje de error en la tabla
        else:
            table["columns"] = truth_table[0]  # Configurar las columnas de la tabla
            for col in truth_table[0]:  # Iterar sobre las columnas para configurarlas
                table.heading(col, text=col)  # Configurar el encabezado de la columna
                table.column(col, width=100, anchor=tk.CENTER)  # Configurar el ancho y alineación de la columna

            for row in truth_table[1:]:  # Iterar sobre las filas de la tabla de verdad
                table.insert("", tk.END, values=row)  # Insertar cada fila en la tabla
    else:
        reset_display()  # Restablecer la interfaz si no se encontró un conector lógico
        messagebox.showinfo("Resultado", "No se encontró ningún conector lógico en la proposición.")  # Mostrar mensaje de error

def reset_display():
    """Restablecer la interfaz a su estado inicial."""
    prop_original_label.config(text="")  # Limpiar la etiqueta de la proposición original
    prop_original_result.config(text="")  # Limpiar el resultado de la proposición original

    conector_label.config(text="")  # Limpiar la etiqueta del conector
    conector_result.config(text="")  # Limpiar el resultado del conector

    tipo_conector_label.config(text="")  # Limpiar la etiqueta del tipo de conector
    tipo_conector_result.config(text="")  # Limpiar el resultado del tipo de conector

    simbolo_label.config(text="")  # Limpiar la etiqueta del símbolo lógico
    simbolo_result.config(text="")  # Limpiar el resultado del símbolo lógico

    proposiciones_label.config(text="")  # Limpiar la etiqueta de proposiciones
    proposiciones_result_label.config(text="")  # Limpiar el resultado de las proposiciones

    table.delete(*table.get_children())  # Limpiar la tabla de verdad

# Crear la ventana principal
root = tk.Tk()
root.title("Intérprete de Lógica Proposicional")  # Configurar el título de la ventana
root.geometry("900x600")  # Configurar el tamaño de la ventana

# Estilo de fuente
font_label_bold = ("Arial", 14, "bold")  # Definir estilo de fuente en negrita
font_label = ("Arial", 12)  # Definir estilo de fuente normal
font_button = ("Arial", 10, "bold")  # Definir estilo de fuente para botones

# Frame para distribución
main_frame = tk.Frame(root)  # Crear el marco principal
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # Empaquetar el marco principal

# Frame izquierdo para resultados
left_frame = tk.Frame(main_frame)  # Crear el marco izquierdo
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)  # Empaquetar el marco izquierdo

# Frame derecho para tabla de verdad
right_frame = tk.Frame(main_frame)  # Crear el marco derecho
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)  # Empaquetar el marco derecho

# Etiqueta de entrada
tk.Label(left_frame, text="Ingrese una proposición:", font=font_label).pack(pady=5)  # Crear etiqueta de entrada

# Cuadro de entrada
entry = tk.Entry(left_frame, width=50, font=font_label)  # Crear cuadro de entrada
entry.pack(pady=5)  # Empaquetar el cuadro de entrada

# Botón de análisis
tk.Button(left_frame, text="Analizar", command=analyze_proposition, font=font_button, bg="blue", fg="white").pack(pady=10)  # Crear botón de análisis

# Sección de resultados
prop_original_label = tk.Label(left_frame, text="", font=font_label_bold, anchor="w")  # Crear etiqueta para la proposición original
prop_original_label.pack(pady=2)  # Empaquetar etiqueta de proposición original
prop_original_result = tk.Label(left_frame, text="", font=font_label, anchor="w")  # Crear etiqueta para el resultado de la proposición original
prop_original_result.pack(pady=2)  # Empaquetar resultado de la proposición original

conector_label = tk.Label(left_frame, text="", font=font_label_bold, anchor="w")  # Crear etiqueta para el conector
conector_label.pack(pady=2)  # Empaquetar etiqueta del conector
conector_result = tk.Label(left_frame, text="", font=font_label, anchor="w")  # Crear etiqueta para el resultado del conector
conector_result.pack(pady=2)  # Empaquetar resultado del conector

tipo_conector_label = tk.Label(left_frame, text="", font=font_label_bold, anchor="w")  # Crear etiqueta para el tipo de conector
tipo_conector_label.pack(pady=2)  # Empaquetar etiqueta del tipo de conector
tipo_conector_result = tk.Label(left_frame, text="", font=font_label, anchor="w")  # Crear etiqueta para el resultado del tipo de conector
tipo_conector_result.pack(pady=2)  # Empaquetar resultado del tipo de conector

simbolo_label = tk.Label(left_frame, text="", font=font_label_bold, anchor="w")  # Crear etiqueta para el símbolo lógico
simbolo_label.pack(pady=2)  # Empaquetar etiqueta del símbolo lógico
simbolo_result = tk.Label(left_frame, text="", font=font_label, anchor="w")  # Crear etiqueta para el resultado del símbolo lógico
simbolo_result.pack(pady=2)  # Empaquetar resultado del símbolo lógico

proposiciones_label = tk.Label(left_frame, text="", font=font_label_bold, anchor="w")  # Crear etiqueta para las proposiciones
proposiciones_label.pack(pady=2)  # Empaquetar etiqueta de proposiciones
proposiciones_result_label = tk.Label(left_frame, text="", font=font_label, anchor="w", justify="left", wraplength=350)  # Crear etiqueta para el resultado de las proposiciones
proposiciones_result_label.pack(pady=2)  # Empaquetar resultado de las proposiciones

# Tabla para mostrar la tabla de verdad
table = ttk.Treeview(right_frame, show="headings")  # Crear tabla para la tabla de verdad
table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # Empaquetar tabla

# Iniciar el bucle principal
root.mainloop()  # Iniciar el bucle de la interfaz gráfica