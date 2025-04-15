def is_palindrome(s):
    """
    Verifica si una cadena es un palíndromo.
    Ignora los espacios,los signos de puntuación y mayúsculas.
    """
   
    limpio = ''.join(c.lower() for c in s if c.isalnum())
    
    
    return limpio == limpio[::-1]
def limpiar_texto(s):
    """
    Convierte el texto a minúsculas y elimina caracteres que no son letras ni números.
    """
    return ''.join(c.lower() for c in s if c.isalnum())
