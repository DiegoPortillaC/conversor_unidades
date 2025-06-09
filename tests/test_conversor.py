import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import longitud

class TestConversionUnidades(unittest.TestCase):
    def test_inch_cm(self):
        "Test conversion de inches a centimetros"
        self.assertEqual(longitud.Longitud.inch_cm(1), 2.54)
        self.assertEqual(longitud.Longitud.inch_cm(5), 12.7)
        self.assertEqual(longitud.Longitud.inch_cm(10), 25.4)

    def test_cm_inch(self):
        "Test conversion de centimetros a inches"
        self.assertEqual(longitud.Longitud.cm_inch(1), 0.393701)
        self.assertEqual(longitud.Longitud.cm_inch(5), 1.968505)
        self.assertEqual(longitud.Longitud.cm_inch(10), 3.93701)

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

if __name__ == "__main__":
    unittest.main()