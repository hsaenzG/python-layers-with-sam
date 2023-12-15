import json
import calculations
def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))
    numero1 = 1
    numero2 = 45
    resultado = calculations.sumar_numeros(numero1, numero2)
    print(resultado)

    return {}