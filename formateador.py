def formateador_aritmético(problemas, respuesta=False):

    # Contamos el numero de elementos en la lista
    if len(problemas) > 5:
        return "Error: Demasiados elementos."
    
    # Identificacion de los elementos de la operación
    OperandoLista1 = []
    OperadorLista = []
    OperandoLista2 = []
    ResultadoLista = []
    
    for problema in problemas:
        componentes = problema.split()
        
        if len(componentes) != 3:
            return "Error: Un problema tiene dos operandos (A y B) y un operador (+ o -), es decir A + B"
        
        Operando1, Operador, Operando2 = componentes
        
        if Operador not in ['+', '-']:
            return "Error: El Operador debe ser suma (+) o resta (-)"
        
        if not Operando1.isdigit() or not Operando2.isdigit():
            return "Error: Deben ser numericos"
        
        if len(Operando1) > 4 or len(Operando2) > 4:
            return "Error: La longitud del numero no debe superara de 4 digitos"
        
        # Calculate result if needed
        if respuesta:
            if Operador == '+':
                Valor = str(int(Operando1) + int(Operando2))
            else:
                Valor = str(int(Operando1) - int(Operando2))
        else:
            Valor = None
        
        # Store components
        OperandoLista1.append(Operando1)
        OperadorLista.append(Operador)
        OperandoLista2.append(Operando2)
        ResultadoLista.append(Valor)
    
    # Prepare lines for output
    Linea1 = []
    Linea2 = []
    TrazoLinea = []
    LineaResultado = []
    
    # Format each problem
    for i in range(len(problemas)):
        # Determine the maximum width needed
        max_width = max(len(OperandoLista1[i]), len(OperandoLista2[i])) + 2
        
        # Format first operand line (right-aligned)
        Linea1.append(OperandoLista1[i].rjust(max_width))
        
        # Format second operand line (operator + space + right-aligned operand)
        Linea2.append(OperadorLista[i] + " " + OperandoLista2[i].rjust(max_width - 2))
        
        # Format dash line
        TrazoLinea.append('-' * max_width)
        
        # Format result line if needed
        if respuesta and ResultadoLista[i] is not None:
            LineaResultado.append(ResultadoLista[i].rjust(max_width))
    
    # Join all lines with 4 spaces between problems
    arranged_problems = "    ".join(Linea1) + "\n"
    arranged_problems += "    ".join(Linea2) + "\n"
    arranged_problems += "    ".join(TrazoLinea)
    
    # Add results if needed
    if respuesta:
        arranged_problems += "\n" + "    ".join(LineaResultado)
    
    return arranged_problems


if __name__ == "__main__":

    problema1 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    problema2 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
    Problema3 = ["1 + 2", "3 + 4", "5 + 6", "7 + 8", "9 + 10", "11 + 12"]
    Problema4 = ["1 * 2", "3 + 4"]
    Problema5 = ["1a + 2", "3 + 4"]
    
    print("Test 1 - Sin Calculo:")
    print(formateador_aritmético(problema1))
    print("\n" + "="*50 + "\n")
    
    print("Test 2 - Con Calculo:")
    print(formateador_aritmético(problema2, True))
    print("\n" + "="*50 + "\n")
    
    # Error test cases
    print("Test 3 - Error: Mas de 5 elementos:")
    print(formateador_aritmético(Problema3))
    print("\n" + "="*50 + "\n")
    
    print("Test 4 - Error: Operador Invalido:")
    print(formateador_aritmético(Problema4))
    print("\n" + "="*50 + "\n")
    
    print("Test 5 - Error: Caracter no numerico:")
    print(formateador_aritmético(Problema5))