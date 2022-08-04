from .engine import Engine

class WilloughbyEngine(Engine):
	def __init__(self, last_service_mileage : int, current_mileage : int):
		self.last_service_mileage = last_service_mileage
		self.current_mileage = current_mileage

	def needs_service(self) -> bool:
		# Requires service every 60,000 miles
		return (self.current_mileage - self.last_service_mileage) > 60000