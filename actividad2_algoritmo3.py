from typing import List, Tuple, Union


def build_derivation_tree(n: int) -> Union[str, List]:
(n: int) -> Union[str, List]:
    """Construye recursivamente un árbol de derivación izquierda para a^n b^n.

    Este árbol se basa en la regla de producción S -> a S b.  Para n > 0,
    el árbol tiene una raíz etiquetada como 'S' con tres hijos: el
    primer hijo es el terminal 'a', el segundo es el árbol
    recursivo para n - 1 (correspondiente al subárbol S), y el tercer
    hijo es el terminal 'b'.  Para n = 0, la producción S -> ε se
    representa con el nodo 'ε'.

    Args:
        n (int): Número de pares a/b en la cadena aceptada.

    Returns:
        Union[str, List]: Una estructura de árbol anidada.  Para n = 0
            devolvemos la cadena 'ε'.  Para n > 0 devolvemos una
            lista con la forma ['S', 'a', subárbol, 'b'].
    """
    # Si n es cero, retornamos la producción S -> ε como el símbolo 'ε'.
    if n == 0:
        return 'ε'
    # En caso contrario, construimos el árbol anidado para n > 0.  La
    # primera posición de la lista es la etiqueta del nodo (S), la
    # segunda el terminal 'a', la tercera el subárbol recursivo y la
    # cuarta el terminal 'b'.
    return ['S', 'a', build_derivation_tree(n - 1), 'b']


def print_tree(tree: Union[str, List], indent: str = "") -> None:
    """Imprime de forma legible un árbol de derivación generado por build_derivation_tree.

    Esta función recorre la estructura de árbol en preorden e
    imprime cada nodo con indentación para reflejar la jerarquía.  Si
    el nodo es una cadena (terminal o 'ε'), se imprime en una
    línea.  Si el nodo es una lista, asumimos que tiene la forma
    ['S', 'a', subárbol, 'b'] y primero imprimimos la etiqueta del
    nodo 'S' y luego los hijos 'a', subárbol y 'b' con mayor
    indentación.

    Args:
        tree (Union[str, List]): El árbol a imprimir, tal como lo
            devuelve build_derivation_tree.
        indent (str, optional): Cadena utilizada para la indentación
            actual.  Se incrementa al descender en el árbol.
    """
    # Si el árbol es una cadena, significa que estamos en un nodo hoja.
    # Simplemente imprimimos el valor con la indentación actual.
    if isinstance(tree, str):
        print(f"{indent}{tree}")
        return
    # De lo contrario, asumimos que es una lista de longitud 4:
    # [etiqueta, terminal_izq, subárbol, terminal_der].  Extraemos
    # sus componentes para mayor claridad.
    label, left_terminal, subtree, right_terminal = tree
    # Imprimimos la etiqueta del nodo (en este caso siempre 'S').
    print(f"{indent}{label}")
    # Incrementamos la indentación para los hijos.  Añadimos dos
    # espacios para que cada nivel sea visible.
    child_indent = indent + "  "
    # Imprimimos el terminal izquierdo 'a'.
    print(f"{child_indent}{left_terminal}")
    # Imprimimos recursivamente el subárbol correspondiente a S.
    print_tree(subtree, child_indent)
    # Imprimimos el terminal derecho 'b'.
    print(f"{child_indent}{right_terminal}")


def algorithm_3(accepted_strings: List[str]) -> None:
    """Ejecuta el Algoritmo 3: construye y muestra árboles de derivación.

    Para cada cadena aceptada proporcionada en la lista, se calcula el
    número de pares (n) contando cuántos símbolos 'a' aparecen al
    principio, puesto que en las cadenas válidas la cantidad de 'a'
    siempre coincide con la cantidad de 'b'.  A continuación se
    construye el árbol de derivación izquierda mediante
    build_derivation_tree(n) y se imprime con print_tree().  En el
    caso de la cadena vacía, se muestra simplemente la producción
    S -> ε.

    Args:
        accepted_strings (List[str]): Cadenas que el PDA aceptó.
    """
    # Imprimimos un encabezado para diferenciar la salida de este
    # algoritmo.
    print("\nExample Output_Algorithm_3:")
    # Recorremos cada cadena aceptada.
    for s in accepted_strings:
        # Para cada cadena obtenemos la longitud de la secuencia de 'a'.
        # Dado que las cadenas aceptadas son de la forma a^n b^n, basta
        # contar el número de 'a' al comienzo.  Esto se puede hacer
        # recorriendo la cadena hasta encontrar el primer 'b'.
        n = 0
        for char in s:
            if char == 'a':
                n += 1
            else:
                # Al encontrar el primer 'b' terminamos el conteo.
                break
        # Construimos el árbol de derivación con el número n obtenido.
        tree = build_derivation_tree(n)
        # Imprimimos un título para la cadena actual.
        print(f"\nDerivation tree for string '{s}':")
        # Utilizamos print_tree para mostrar el árbol de forma jerárquica.
        print_tree(tree)



def main():
    # Ejemplo: construir árbol para 'aabb' y cadena vacía
    accepted_strings = ['','ab','aabb']
    algorithm_3(accepted_strings)

if __name__ == "__main__":
    main()
