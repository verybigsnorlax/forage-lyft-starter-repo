import unittest
from datetime import datetime
import sys

sys.path.append("..")
from carfactory import CarFactory as cf

class TestCases(unittest.TestCase):

	# Test Calliope instances
	def test_calliope_battery_should_be_serviced(self):
		# Battery should be serviced test
		today = datetime.today()
		last_service_date = today.replace(year=today.year - 4)
		current_mileage = 0
		last_service_mileage = 0

		car = cf.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
		self.assertTrue(car.needs_service())

	def test_calliope_battery_should_not_be_serviced(self):
		# Battery should not be serviced test
		today = datetime.today()
		last_service_date = today.replace(year=today.year - 2)
		current_mileage = 0
		last_service_mileage = 0

		car = cf.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
		self.assertFalse(car.needs_service())

	def test_calliope_engine_should_be_serviced(self):
		# Engine should be serviced test
		today = datetime.today()
		current_mileage = 30001
		last_service_mileage = 0

		car = cf.create_calliope(today, today, current_mileage, last_service_mileage)
		self.assertTrue(car.needs_service())

	def test_calliope_engine_should_not_be_serviced(self):
		# Engine should not be serviced test
		today = datetime.today()
		current_mileage = 30000
		last_service_mileage = 0

		car = cf.create_calliope(today, today, current_mileage, last_service_mileage)
		self.assertFalse(car.needs_service())

	# Test Glissade instances
	def test_glissade_battery_should_be_serviced(self):
		# Battery should be serviced test
		today = datetime.today()
		last_service_date = today.replace(year=today.year - 4)
		current_mileage = 0
		last_service_mileage = 0

		car = cf.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
		self.assertTrue(car.needs_service())

	def test_glissade_battery_should_not_be_serviced(self):
		# Battery should not be serviced test
		today = datetime.today()
		last_service_date = today.replace(year=today.year - 2)
		current_mileage = 0
		last_service_mileage = 0

		car = cf.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
		self.assertFalse(car.needs_service())

	def test_glissade_engine_should_be_serviced(self):
		# Engine should be serviced test
		today = datetime.today()
		current_mileage = 60001
		last_service_mileage = 0

		car = cf.create_glissade(today, today, current_mileage, last_service_mileage)
		self.assertTrue(car.needs_service())

	def test_glissade_engine_should_not_be_serviced(self):
		# Engine should not be serviced test
		today = datetime.today()
		current_mileage = 60000
		last_service_mileage = 0

		car = cf.create_glissade(today, today, current_mileage, last_service_mileage)
		self.assertFalse(car.needs_service())

	# Test Palindrom instances
	def test_palindrome_battery_should_be_serviced(self):
		# Battery should be serviced test
		today = datetime.today()
		last_service_date = today.replace(year=today.year - 4)
		warning_light_on = False

		car = cf.create_palindrome(today, last_service_date, warning_light_on)
		self.assertTrue(car.needs_service())

	def test_palindrome_battery_should_not_be_serviced(self):
		# Battery should not be serviced test
		today = datetime.today()
		last_service_date = today.replace(year=today.year - 2)
		warning_light_on = False

		car = cf.create_palindrome(today, last_service_date, warning_light_on)
		self.assertFalse(car.needs_service())	

	def test_palindrome_engine_should_be_serviced(self):
		# Engine should be serviced test
		today = datetime.today()
		warning_light_on = True

		car = cf.create_palindrome(today, today, warning_light_on)
		self.assertTrue(car.needs_service())

	def test_palindrome_engine_should_not_be_serviced(self):
		# Engine should not be serviced test
		today = datetime.today()
		warning_light_on = False

		car = cf.create_palindrome(today, today, warning_light_on)
		self.assertFalse(car.needs_service())	

	def test_rorshach_battery_should_be_serviced(self):
		# Battery should be serviced test
		today = datetime.today()
		last_service_date = today.replace(year=today.year - 5)
		current_mileage = 0
		last_service_mileage = 0

		car = cf.create_rorshach(today, last_service_date, current_mileage, last_service_mileage)
		self.assertTrue(car.needs_service())

	def test_rorshach_battery_should_not_be_serviced(self):
		# Battery should not be serviced test
		today = datetime.today()
		last_service_date = today.replace(year=today.year - 3)
		current_mileage = 0
		last_service_mileage = 0

		car = cf.create_rorshach(today, last_service_date, current_mileage, last_service_mileage)
		self.assertFalse(car.needs_service())		

	def test_rorshach_engine_should_be_serviced(self):
		# Engine should be serviced test
		today = datetime.today()
		current_mileage = 60001
		last_service_mileage = 0

		car = cf.create_rorshach(today, today, current_mileage, last_service_mileage)
		self.assertTrue(car.needs_service())

	def test_rorshach_engine_should_not_be_serviced(self):
		# Engine should not be serviced test
		today = datetime.today()
		current_mileage = 60000
		last_service_mileage = 0

		car = cf.create_rorshach(today, today, current_mileage, last_service_mileage)
		self.assertFalse(car.needs_service())

	# Test Thovex instances
	def test_thovex_battery_should_be_serviced(self):
		# Battery should be serviced test
		today = datetime.today()
		last_service_date = today.replace(year=today.year - 5)
		current_mileage = 0
		last_service_mileage = 0

		car = cf.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
		self.assertTrue(car.needs_service())

	def test_thovex_battery_should_not_be_serviced(self):
		# Battery should not be serviced test
		today = datetime.today()
		last_service_date = today.replace(year=today.year - 3)
		current_mileage = 0
		last_service_mileage = 0

		car = cf.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
		self.assertFalse(car.needs_service())	

	def test_thovex_engine_should_be_serviced(self):
		# Engine should be serviced test
		today = datetime.today()
		current_mileage = 30001
		last_service_mileage = 0

		car = cf.create_thovex(today, today, current_mileage, last_service_mileage)
		self.assertTrue(car.needs_service())

	def test_thovex_engine_should_not_be_serviced(self):
		# Engine should not be serviced test
		today = datetime.today()
		current_mileage = 30000
		last_service_mileage = 0

		car = cf.create_thovex(today, today, current_mileage, last_service_mileage)
		self.assertFalse(car.needs_service())	

if __name__ == "__main__":
	unittest.main()