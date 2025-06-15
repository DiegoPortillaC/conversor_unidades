"""
Módulo para realizar conversiones entre diferentes unidades de longitud.
Incluye conversiones entre sistemas métricos e imperiales.

Conversiones disponibles:
- Pulgadas ↔ Centímetros
- Kilómetros ↔ Metros
- Yardas ↔ Metros
"""

class Longitud:

    def inch_cm (number):
        '''
        Funcion que al introducir un numero (inches) lo
        convierte a centrimetros
        '''
        result = number * 2.54
        return result

    def cm_inch (number):
        '''
        Funcion que al introducir un numero (centimetros) lo
        convierte a inches
        '''
        result = number * 0.393701
        return result

    def km_meters (number):
        '''
        Funcion que al introducir un numero (Km) lo
        convierte a metros
        '''
        result = number * 1000
        return result

    def meters_km (number):
        '''
        Funcion que al introducir un numero (metros) lo
        convierte a km
        '''
        result = number / 1000
        return result

    def yard_meter (number):
        '''
        Funcion que al introducir un numero (yards) lo
        convierte a metros
        '''
        result = number * 0.9144
        return result

    def meter_yard (number):
        '''
        Funcion que al introducir un numero (metros) lo
        convierte a yardas
        '''
        result = number * 1.09361
        return result