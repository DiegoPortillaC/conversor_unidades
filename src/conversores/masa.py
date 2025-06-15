"""
Módulo para realizar conversiones entre diferentes unidades de masa.
Incluye conversiones entre sistemas métricos e imperiales.

Conversiones disponibles:
- Gramos ↔ Kilogramos
- Libras ↔ Kilogramos
- Onzas ↔ Gramos
"""

class  Masa:

    def gram_kilo(number):
        '''
        Funcion que al introcir una numero (gramos) lo
        convierte a kilos
        '''
        result = number / 1000
        return result
    
    def kilo_gram(number):
        '''
        Funcion que al introcir una numero (kilos) lo
        convierte a gramos
        '''
        result = number * 1000
        return result
    
    def lb_kilo(number):
        '''
        Funcion que al introcir una numero (libras) lo
        convierte a kilos
        '''
        result = number / 2.20462
        return result
    
    def kilo_lb(number):
        '''
        Funcion que al introcir una numero (kilos) lo
        convierte a libras
        '''        
        result = number * 2.20462
        return result
    
    def ounce_gram(number):
        '''
        Funcion que al introcir una numero (onzas) lo
        convierte a gramos
        '''   
        result = number * 28.3495
        return result   
    
    def gram_ounce(number):
        '''
        Funcion que al introcir una numero (kilos) lo
        convierte a libras
        '''   
        result = number / 28.3495
        return result  