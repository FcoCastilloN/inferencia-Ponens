def inferencia_ponens(premisa_condicional, premisa_verdadera):
    """
    Realiza la inferencia Ponens.

    Args:
    - premisa_condicional: Una tupla que representa una premisa condicional en la forma (p, q), donde p implica q.
    - premisa_verdadera: Un booleano que indica si la premisa p es verdadera.

    Returns:
    - Un booleano que indica si la conclusión q es verdadera según la inferencia Ponens.
    """
    if premisa_verdadera:
        return premisa_condicional[1]  # Retorna la conclusión q si la premisa p es verdadera
    else:
        return False  # Retorna falso si la premisa p es falsa


# Ejemplo de uso:
premisa_condicional = ('Esta lloviendo', 'El suelo esta mojado')
premisa_verdadera = True  # La premisa "Está lloviendo" es verdadera
conclusion = inferencia_ponens(premisa_condicional, premisa_verdadera)
print("Conclusión de la inferencia Ponens:", conclusion)