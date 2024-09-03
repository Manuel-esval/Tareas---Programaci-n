def precedence(op):
    """Retorna la precedencia de los operadores."""
    precedences = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}
    return precedences.get(op, 0)

def is_operator(c):
    """Verifica si el carácter es un operador."""
    return c in {'+', '-', '*', '/', '**'}

def infix_to_rpn(expression):
    """Convierte una expresión en notación infija a notación polaca inversa (RPN)."""
    output = []
    stack = []
    steps = []

    tokens = expression.split()
    for token in tokens:
        if token.isnumeric():  # Si es un número, lo añade a la salida
            output.append(token)
            steps.append(f"Token '{token}' es un número, se añade a la salida.")
        elif token == '(':  # Si es '(', lo apila
            stack.append(token)
            steps.append(f"Token '{token}' es '(', se apila.")
        elif token == ')':  # Si es ')', desempila hasta '('
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Quita el '(' de la pila
            steps.append(f"Token '{token}' es ')', se desempilan hasta '('.")
        elif is_operator(token):  # Si es un operador, maneja la precedencia
            while (stack and precedence(stack[-1]) >= precedence(token)):
                output.append(stack.pop())
            stack.append(token)
            steps.append(f"Token '{token}' es operador, maneja precedencia y se apila.")
    
    # Vacía los operadores restantes en la pila
    while stack:
        output.append(stack.pop())

    steps.append(f"Operadores restantes en la pila se mueven a la salida: {' '.join(output)}")

    # Genera el reporte
    with open("reporte_rpn.txt", "w") as file:
        file.write("Pasos para la conversión a Notación Polaca Inversa:\n\n")
        file.write("\n".join(steps))
    
    return " ".join(output)

if __name__ == "__main__":
    # Ejemplo de uso:
    expression = input("Ingrese una expresión aritmética en formato infijo: ")
    rpn_expression = infix_to_rpn(expression)
    print("Expresión en Notación Polaca Inversa:", rpn_expression)
