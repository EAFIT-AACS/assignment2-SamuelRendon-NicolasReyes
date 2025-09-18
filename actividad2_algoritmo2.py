from typing import List, Tuple, Union


def pda_accepts(input_string: str) -> bool:
(input_string: str) -> bool:
    """Determina si una cadena es aceptada por un PDA que reconoce a^n b^n.

    Este autómata de pila empuja un símbolo por cada 'a' leída y
    desapila por cada 'b'.  Si al terminar de leer la cadena la
    pila está vacía y nunca se intentó desapilar de una pila vacía,
    entonces la cadena pertenece al lenguaje.

    Args:
        input_string (str): La cadena sobre el alfabeto {'a','b'} a analizar.

    Returns:
        bool: True si la cadena es aceptada, False en caso contrario.
    """
    # Declaramos una lista que servirá como la pila del autómata.  Cada
    # 'a' provocará que añadamos un marcador (por ejemplo 'A') a la pila.
    stack: List[str] = []
    # Además de la pila, llevamos un indicador que nos dice si ya
    # comenzamos a leer 'b'.  En el lenguaje a^n b^n todos los 'a' deben
    # aparecer antes de cualquier 'b'.  Si encontramos un 'a' después de
    # haber leído un 'b', la cadena se rechaza.
    in_b_phase = False
    # Recorremos cada símbolo de la cadena en orden.
    for char in input_string:
        # Si el símbolo es 'a', aún estamos en la fase de contar 'a'.
        if char == 'a':
            # Si ya hemos visto un 'b' previamente, encontrar un 'a'
            # intercalado viola el orden requerido y se rechaza.
            if in_b_phase:
                return False
            # Apilamos un marcador por cada 'a'.  Usamos el carácter
            # 'A' como marcador arbitrario; cualquier símbolo distinto
            # funcionaría como indicador en la pila.
            stack.append('A')
        # Si encontramos un 'b', pasamos a la fase de desapilar.
        elif char == 'b':
            # Marcamos que estamos en la fase de lectura de 'b'.  A
            # partir de este momento no se permitirán más 'a'.
            in_b_phase = True
            if stack:
                # Desapilamos el último marcador.  No almacenamos el
                # valor devuelto porque sólo nos importa reducir el
                # tamaño de la pila.
                stack.pop()
            else:
                # Si no hay nada en la pila para desapilar, la cadena no
                # puede ser de la forma a^n b^n (hay más 'b' que 'a').
                # Retornamos False inmediatamente.
                return False
        else:
            # Si aparece un símbolo diferente de 'a' o 'b', la cadena no
            # pertenece al alfabeto de la gramática y se rechaza.
            return False
    # Al terminar de procesar todos los símbolos, la cadena será
    # aceptada únicamente si la pila está vacía (igual número de 'a' y
    # 'b').  Si queda algún marcador, significa que hay más 'a' que
    # 'b' y se rechaza.
    return len(stack) == 0


def algorithm_2(valid_strings: List[str], invalid_strings: List[str]) -> List[str]:
    """Ejecuta el Algoritmo 2: evalúa con el PDA cada cadena y reporta.

    Esta función toma las cadenas generadas en el Algoritmo 1 y,
    utilizando la función `pda_accepts`, determina cuáles son
    aceptadas y cuáles rechazadas.  Imprime mensajes detallados
    indicando el resultado y devuelve una lista con las cadenas
    aceptadas, que servirán de entrada al Algoritmo 3.

    Args:
        valid_strings (List[str]): Cadenas que deberían ser aceptadas.
        invalid_strings (List[str]): Cadenas que deberían ser rechazadas.

    Returns:
        List[str]: Una lista con todas las cadenas que el PDA acepta.
    """
    # Combinamos las listas para procesar todas las cadenas una tras
    # otra.  El segundo elemento de la tupla indica si esperamos que
    # la cadena sea aceptada (True) o rechazada (False).  Este dato
    # puede ser útil para comparar el comportamiento del PDA con lo
    # esperado.
    all_strings = [(s, True) for s in valid_strings] + [(s, False) for s in invalid_strings]
    # Lista donde almacenaremos únicamente las cadenas que el PDA
    # acepta realmente.
    accepted: List[str] = []
    # Imprimimos encabezado acorde al ejemplo.
    print("\nExample Output_Algorithm_2:")
    # Recorremos cada cadena junto con el valor booleano esperado.
    for s, expected in all_strings:
        # Evaluamos la cadena usando el autómata de pila.
        result = pda_accepts(s)
        # Construimos un mensaje indicando si la cadena es aceptada o
        # rechazada.  Notar que usamos la misma redacción que el
        # ejemplo del PDF: “The string 'cadena' is accepted/rejected by
        # the PDA.”
        if result:
            message = f"The string '{s}' is accepted by the PDA."
            # Añadimos la cadena aceptada a la lista de aceptadas.
            accepted.append(s)
        else:
            message = f"The string '{s}' is rejected by the PDA."
        # Imprimimos el mensaje.
        print(message)
    # Retornamos la lista de cadenas que el PDA aceptó, sin importar
    # si venían de valid_strings o invalid_strings (aunque en teoría
    # sólo deberían provenir de valid_strings).
    return accepted



def main():
    # Ejemplo de entrada para algoritmo 2 (puede cambiarse si se quiere usar directamente con Algoritmo 1)
    valid_strings = ['','ab','aabb']
    invalid_strings = ['aab','abab']
    accepted = algorithm_2(valid_strings, invalid_strings)
    print("\nStrings accepted by PDA:", accepted)

if __name__ == "__main__":
    main()
