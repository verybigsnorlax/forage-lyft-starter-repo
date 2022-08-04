from datetime import datetime, date, timedelta
from car import Car
from engine.capulet import CapuletEngine
from engine.willoughby import WilloughbyEngine
from engine.sternman import SternmanEngine
from battery.spindler import SpindlerBattery
from battery.nubbin import NubbinBattery

def create_calliope(current_date : datetime, last_service_date : datetime, current_mileage : int, last_service_mileage : int) -> Car:
	engine = CapuletEngine(last_service_mileage, current_mileage)
	battery = SpindlerBattery(last_service_date, current_date)
	car = Car(engine=engine, battery=battery)

	return car

def create_glissade(current_date : datetime, last_service_date : datetime, current_mileage : int, last_service_mileage : int) -> Car:
	engine = WilloughbyEngine(last_service_mileage, current_mileage)
	battery = SpindlerBattery(last_service_date, current_date)
	car = Car(engine=engine, battery=battery)

	return car

def create_palindrome(current_date : datetime, last_service_date : datetime, warning_light_on : bool) -> Car:
	engine = SternmanEngine(warning_light_on)
	battery = SpindlerBattery(last_service_date, current_date)
	car = Car(engine=engine, battery=battery)

	return car

def create rorshach(current_date : datetime, last_service_date : datetime, current_mileage : int, last_service_mileage : int) -> Car:
	engine = WilloughbyEngine(last_service_mileage, current_mileage)
	battery = NubbinBattery(last_service_date, current_date)
	car = Car(engine=engine, battery=battery)

	return car

def create_thovex(current_date : datetime, last_service_date : datetime, current_mileage : int, last_service_mileage : int) -> Car:
	engine = CapuletEngine(last_service_mileage, current_mileage)
	battery = NubbinBattery(last_service_date, current_date)
	car = Car(engine=engine, battery=battery)

	return car