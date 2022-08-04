import unittest
import sys

sys.path.append('..')
from tire.carrigan import CarriganTire
from tire.octoprime import OctoprimeTire

class TestCases(unittest.TestCase):

	# Test Carrigan tires
	def test_carrigan_should_be_serviced(self):
		# Carrigan tires should be serviced
		tires = [0.1, 0.9, 0.2, 0.5]

		carrigan = CarriganTire(tires)
		self.assertTrue(carrigan.needs_service())

	def test_carrigan_should_not_be_serviced(self):
		# Carrigan tires should not be serviced
		tires = [0.1, 0.8, 0.2, 0.5]

		carrigan = CarriganTire(tires)
		self.assertFalse(carrigan.needs_service())

	# Test Octoprime tires
	def test_octoprime_should_be_serviced(self):
		# Octoprime tires should be serviced
		tires = [0.9, 0.9, 0.8, 0.5]

		octoprime = OctoprimeTire(tires)
		self.assertTrue(octoprime.needs_service())

	def test_octoprime_should_not_be_serviced(self):
		# Octoprime tires should not be serviced
		tires = [0.2, 0.3, 0.1, 0.9]

		octoprime = OctoprimeTire(tires)
		self.assertFalse(octoprime.needs_service())

if __name__ == "__main__":
	unittest.main()