import unittest
import conversions
import conversions_refactored


class ConversionFunctions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        celsius = 300
        expected = 573.15
        actual = conversions.convertCelsiusToKelvin(celsius)

        self.assertAlmostEqual(expected, actual, places=2, msg="Celsius to  Kelvin conversion failed")

    def test_convertCelsiusToFahrenheit(self):
        celsius = 300
        expected = 572
        actual = conversions.convertCelsiusToFahrenheit(self)

        self.assertAlmostEqual(expected, actual, places=2, msg="Celsius to Fahrenheit conversion failed")

    def test_convertFahrenheitToCelsius(self):
        fahrenheit = 300
        expected = 148.89
        actual = conversions.convertFahrenheitToCelsius(self)

        self.assertAlmostEqual(expected, actual, places=2, msg="Fahrenheit to Celcius conversion failed")

    def test_convertFahrenheitToKelvin(self):
        fahrenheit = 300
        expected = 422.04
        actual = conversions.convertFahrenheitToKelvin(self)

        self.assertAlmostEqual(expected, actual, places=2, msg="Fahrenheit to Kelvin conversion failed")

    def test_convertKelvinToCelsius(self):
        kelvin = 300
        expected = 26.85
        actual = conversions.convertKelvinToCelsius(self)

        self.assertAlmostEqual(expected, actual, places=2, msg="Kelvin to Celsius conversion failed")

    def test_convertKelvinToFahrenheit(self):
        kelvin = 300
        expected = 80.33
        actual = conversions.convertKelvinToFahrenheit(self)

        self.assertAlmostEqual(expected, actual, places=2, msg="Kelvin to Fahrenheit conversion failed")

    def test_convertCtoK(self):
        fromUnit = 'C'
        toUnit = 'K'
        value = 300
        expected = 573.15
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Celsius to  Kelvin conversion failed")

    def test_convertCtoF(self):
        fromUnit = 'C'
        toUnit = 'F'
        value = 300
        expected = 572
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Celsius to  Fahrenheit conversion failed")

    def test_convertFtoC(self):
        fromUnit = 'F'
        toUnit = 'C'
        value = 300
        expected = 148.89
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Fahrenheit to Celsius conversion failed")

    def test_convertFtoK(self):
        fromUnit = 'F'
        toUnit = 'K'
        value = 300
        expected = 422.04
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Fahrenheit to Kelvin conversion failed")

    def test_convertKtoC(self):
        fromUnit = 'K'
        toUnit = 'C'
        value = 300
        expected = 26.85
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Kelvin to Celsius conversion failed")

    def test_convertKtoF(self):
        fromUnit = 'K'
        toUnit = 'F'
        value = 300
        expected = 80.33
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Kelvin to  Fahrenheit conversion failed")

    def test_convertMtoYr(self):
        fromUnit = 'm'
        toUnit = 'yr'
        value = 100
        expected = 109.36
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Kelvin to  Fahrenheit conversion failed")

    def test_convertMtoMi(self):
        fromUnit = 'm'
        toUnit = 'mi'
        value = 100
        expected = 0.06
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Kelvin to  Fahrenheit conversion failed")

    def test_convertYrtoM(self):
        fromUnit = 'yr'
        toUnit = 'm'
        value = 100
        expected = 91.44
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Kelvin to  Fahrenheit conversion failed")

    def test_convertYrtoMi(self):
        fromUnit = 'yr'
        toUnit = 'mi'
        value = 100
        expected = 0.06
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Yards to Miles conversion failed")

    def test_convertMitoYr(self):
        fromUnit = 'mi'
        toUnit = 'yr'
        value = 100
        expected = 176000
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Miles to Yards conversion failed")

    def test_convertMitoM(self):
        fromUnit = 'mi'
        toUnit = 'm'
        value = 100
        expected = 160934.71
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Miles to Meters conversion failed")

if __name__ == '__main__':
    unittest.main()
