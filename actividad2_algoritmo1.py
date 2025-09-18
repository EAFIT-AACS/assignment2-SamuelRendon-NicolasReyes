from typing import List, Tuple, Union


def generate_grammar_strings(max_n: int) -> List[str]:
(max_n: int) -> List[str]:
    """Genera cadenas del lenguaje a^n b^n para valores de n de 0 a max_n.

    La gramática G produce cadenas formadas por n símbolos 'a'
    seguidos de n símbolos 'b'.  Para n = 0 la producción S -> ε
    devuelve la cadena vacía.  Este generador recorre n desde 0 hasta
    max_n y concatena 'a' repetido n veces con 'b' repetido n veces.

    Args:
        max_n (int): El valor máximo de n a generar.  Si max_n es 0
            únicamente se obtendrá la cadena vacía.  Debe ser un
            entero no negativo.

    Returns:
        List[str]: Una lista de cadenas aceptadas por la gramática.
    """
    # Creamos una lista vacía donde se almacenarán las cadenas generadas.
    strings: List[str] = []
    # Iteramos n desde 0 hasta max_n, inclusive.  Cada n representa la
    # cantidad de 'a' y 'b' en la cadena resultante.
    for n in range(max_n + 1):
        # Construimos la cadena para el valor actual de n.  Utilizamos
        # multiplicación de cadenas para repetir 'a' n veces y 'b' n
        # veces.  Para n=0, tanto 'a'*0 como 'b'*0 devuelven la
        # cadena vacía, resultando en ''.
        s = ('a' * n) + ('b' * n)
        # Añadimos la cadena generada a la lista de resultados.
        strings.append(s)
    # Retornamos la lista completa de cadenas válidas.
    return strings


def generate_non_grammar_strings() -> List[str]:
    """Genera cadenas que utilizan sólo los símbolos 'a' y 'b' pero no
    pertenecen al lenguaje a^n b^n.

    Estas cadenas se construyen de manera explícita para violar las
    reglas de la gramática: algunas tienen distinto número de 'a' y
    'b'; otras comienzan con 'b' o intercalan los caracteres.  Es
    importante que la función siempre devuelva al menos dos cadenas.

    Returns:
        List[str]: Una lista de cadenas que no pertenecen al lenguaje.
    """
    # Definimos manualmente algunas cadenas que NO cumplen la forma a^n b^n.
    # 1. 'aab' tiene dos 'a' y una 'b' (números diferentes).
    # 2. 'aabbbb' tiene dos 'a' y cuatro 'b'.
    # 3. 'ba' tiene un 'b' antes de un 'a', invirtiendo el orden.
    # 4. 'abab' alterna los símbolos.
    # 5. 'bbbaaaa' comienza con 'b's y luego 'a's.
    # Se pueden agregar más ejemplos para enriquecer las pruebas.
    non_strings: List[str] = [
        'aab',       # número de 'a' y 'b' distinto
        'aabbbb',    # más 'b' que 'a'
        'ba',        # 'b' aparece antes que 'a'
        'abab',      # alternancia de símbolos
        'bbbaaaa',   # todos los 'b' antes de los 'a'
    ]
    # Retornamos la lista de cadenas no válidas.
    return non_strings


def algorithm_1() -> Tuple[List[str], List[str]]:
    """Ejecuta el Algoritmo 1: genera cadenas válidas e inválidas.

    Esta función llama a `generate_grammar_strings` para obtener una
    colección de cadenas aceptadas por la gramática y a
    `generate_non_grammar_strings` para obtener cadenas que utilizan
    el mismo alfabeto pero son rechazadas.  Imprime las cadenas
    resultantes conforme al ejemplo de la guía y devuelve ambas
    listas.

    Returns:
        Tuple[List[str], List[str]]: Una tupla donde el primer
            elemento es la lista de cadenas válidas y el segundo la
            lista de cadenas no válidas.
    """
    # Elegimos un valor de n máximo para generar cadenas válidas.  Aquí
    # usamos 5 para incluir ejemplos hasta 'aaaaabbbbb'.  Se puede
    # modificar para obtener más o menos cadenas según se necesite.
    max_n = 5
    # Obtenemos las cadenas aceptadas.  Este generador incluye la
    # cadena vacía cuando n = 0.
    valid_strings = generate_grammar_strings(max_n)
    # Obtenemos las cadenas que no cumplen la forma a^n b^n.
    invalid_strings = generate_non_grammar_strings()
    # Imprimimos las cadenas generadas al estilo del ejemplo del
    # enunciado.  En el ejemplo, cada línea tiene el prefijo "String: '".
    # Iteramos primero sobre las cadenas válidas y luego sobre las no
    # válidas.
    print("Example Output_Algorithm_1:")
    for s in valid_strings + invalid_strings:
        # Usamos comillas simples en la impresión para imitar el ejemplo.
        print(f"String: '{s}'")
    # Devolvemos las listas para ser usadas por el Algoritmo 2.
    return valid_strings, invalid_strings



def main():
    valid, invalid = algorithm_1()
    print("\nValid strings:", valid)
    print("Invalid strings:", invalid)

if __name__ == "__main__":
    main()
