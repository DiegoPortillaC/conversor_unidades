import unittest
from conversores import longitud, masa, temperatura

class TestConversionUnidades(unittest.TestCase):
    ################################################################
    ################        Test longitud        ###################
    ################################################################

    def test_inch_cm(self):
        "Test conversion de inches a centimetros"
        self.assertEqual(longitud.Longitud.inch_cm(1), 2.54)
        self.assertEqual(longitud.Longitud.inch_cm(5), 12.7)
        self.assertEqual(longitud.Longitud.inch_cm(10), 25.4)

    def test_cm_inch(self):
        "Test conversion de centimetros a inches"
        self.assertAlmostEqual(longitud.Longitud.cm_inch(1), 0.393701)
        self.assertAlmostEqual(longitud.Longitud.cm_inch(5), 1.968505)
        self.assertAlmostEqual(longitud.Longitud.cm_inch(10), 3.93701)

    def test_km_meters(self):
        "Test conversion de kilometros a metros"
        self.assertEqual(longitud.Longitud.km_meters(1), 1000)
        self.assertEqual(longitud.Longitud.km_meters(2.5), 2500)
        self.assertEqual(longitud.Longitud.km_meters(0.5), 500)

    def test_meters_km(self):
        "Test conversion de metros a kilometros"
        self.assertEqual(longitud.Longitud.meters_km(1000), 1)
        self.assertEqual(longitud.Longitud.meters_km(5000), 5)
        self.assertEqual(longitud.Longitud.meters_km(250), 0.25)

    def test_yard_meter(self):
        "Test conversion de yardas a meteros"
        self.assertEqual(longitud.Longitud.yard_meter(1), 0.9144)
        self.assertEqual(longitud.Longitud.yard_meter(2), 1.8288)
        self.assertEqual(longitud.Longitud.yard_meter(5), 4.572)

    def test_meter_yard(self):
        "Test conversion de meteros a yardas"
        self.assertEqual(longitud.Longitud.meter_yard(1), 1.09361)
        self.assertEqual(longitud.Longitud.meter_yard(2), 2.18722)
        self.assertEqual(longitud.Longitud.meter_yard(5), 5.46805)

    ################################################################
    ################        Test masa        #######################
    ################################################################

    def test_gram_kilo(self):
        "Test conversion de gramos a kilos"
        self.assertEqual(masa.Masa.gram_kilo(1000), 1)
        self.assertEqual(masa.Masa.gram_kilo(3750), 3.750)
        self.assertEqual(masa.Masa.gram_kilo(7200), 7.200)

    def test_kilo_gram(self):
        "Test conversion de kilos a gramos"
        self.assertEqual(masa.Masa.kilo_gram(1), 1000)
        self.assertEqual(masa.Masa.kilo_gram(3.75), 3750)
        self.assertEqual(masa.Masa.kilo_gram(7.2), 7200)
    
    def test_lb_kg(self):
        "Test conversion de libras a kilos"
        #Comparacion hasta 4 decimales para evitar errores con decimales
        self.assertAlmostEqual(masa.Masa.lb_kilo(1), 0.453592 ,places = 4)
        self.assertAlmostEqual(masa.Masa.lb_kilo(5), 2.26796 ,places = 4)
        self.assertAlmostEqual(masa.Masa.lb_kilo(10), 4.53592 , places = 4)

    def test_kg_lb(self):
        "Test conversion de kilos a libras"
        self.assertAlmostEqual(masa.Masa.kilo_lb(1), 2.20462 )
        self.assertAlmostEqual(masa.Masa.kilo_lb(5), 11.0231 )
        self.assertAlmostEqual(masa.Masa.kilo_lb(10), 22.0462 )

    def test_ounce_gram (self):
        "Test conversion de onzas a gramos"
        self.assertEqual(masa.Masa.ounce_gram(1), 28.3495 )
        self.assertEqual(masa.Masa.ounce_gram(5), 141.7475 )
        self.assertEqual(masa.Masa.ounce_gram(15), 425.2425 )
    
    def test_gram_ounce (self):
        "Test conversion de gramos a onzas"
        #Comparacion hasta 4 decimales para evitar errores con decimales
        self.assertEqual(masa.Masa.gram_ounce(28.3495), 1)
        self.assertAlmostEqual(masa.Masa.gram_ounce(100), 3.5274 , places = 4 )
        self.assertAlmostEqual(masa.Masa.gram_ounce(250), 8.81849 , places = 4)

    ################################################################
    ################        Test temperatura        ################
    ################################################################

    def test_celsius_kelvin(self):
        "Test conversion de Celsius a Kelvin"
        self.assertAlmostEqual(temperatura.Temperatura.celsius_kelvin(0), 273.15, places=4)
        self.assertAlmostEqual(temperatura.Temperatura.celsius_kelvin(100), 373.15, places=4)
        self.assertAlmostEqual(temperatura.Temperatura.celsius_kelvin(-40), 233.15, places=4)

    def test_kelvin_celsius(self):
        "Test conversion de Kelvin a Celsius"
        self.assertAlmostEqual(temperatura.Temperatura.kelvin_celsius(273.15), 0, places=4)
        self.assertAlmostEqual(temperatura.Temperatura.kelvin_celsius(373.15), 100, places=4)
        self.assertAlmostEqual(temperatura.Temperatura.kelvin_celsius(233.15), -40, places=4)

    def test_celsius_fahrenheit(self):
        "Test conversion de Celsius a Fahrenheit"
        self.assertEqual(temperatura.Temperatura.celsius_fahren(0), 32)
        self.assertEqual(temperatura.Temperatura.celsius_fahren(100), 212)
        self.assertEqual(temperatura.Temperatura.celsius_fahren(-40), -40)

    def test_fahrenheit_celsius(self):
        "Test conversion de Fahrenheit a Celsius"
        self.assertEqual(temperatura.Temperatura.fahren_celsius(32), 0)
        self.assertEqual(temperatura.Temperatura.fahren_celsius(212), 100)
        self.assertEqual(temperatura.Temperatura.fahren_celsius(-40), -40)

if __name__ == "__main__":
    unittest.main()