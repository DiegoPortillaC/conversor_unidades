class Temperatura:

    def celsius_kelvin(number):
        '''
        Funcion que al introducir un numero (celsius) lo
        convierte a kelvin
        '''
        result = number + 273.15
        return result
    
    def kelvin_celsius(number):
        '''
        Funcion que al introducir un numero (kelvin) lo
        convierte a celsius
        '''
        result = number - 273.15
        return result
    
    def celsius_fahren(number):
        '''
        Funcion que al introducir un numero (celsius) lo
        convierte a Fahrenheit
        '''
        result = (number * 9 / 5) + 32
        return result
    
    def fahren_celsius(number):
        '''
        Funcion que al introducir un numero (Fahrenhein) lo
        convierte a celsius
        '''
        result = (number - 32) * 5 / 9
        return result


    
