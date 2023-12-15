import re

def buscar_exacto(cadena, subcadena):
    """
    Busca la subcadena exacta en la cadena dada.
    Devuelve True si se encuentra, False en caso contrario.
    """
    return subcadena in cadena

def buscar_palabras_clave(cadena, palabras_clave):
    """
    Busca la presencia de al menos una palabra clave en la cadena.
    Devuelve True si se encuentra alguna palabra clave, False en caso contrario.
    """
    return any(palabra_clave in cadena for palabra_clave in palabras_clave)

def buscar_expresion_regular(cadena, patron):
    """
    Busca la coincidencia de una expresión regular en la cadena.
    Devuelve True si se encuentra, False en caso contrario.
    """
    return bool(re.search(patron, cadena))

def buscar_prefijo(cadena, prefijo):
    """
    Verifica si la cadena comienza con el prefijo dado.
    Devuelve True si es así, False en caso contrario.
    """
    return cadena.startswith(prefijo)

def buscar_sufijo(cadena, sufijo):
    """
    Verifica si la cadena termina con el sufijo dado.
    Devuelve True si es así, False en caso contrario.
    """
    return cadena.endswith(sufijo)


