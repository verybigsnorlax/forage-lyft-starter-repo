from datetime import datetime,
from .battery import Battery

class NubbinBattery(Battery):
	def __init__(self, last_service_date : datetime, current_date : datetime):
		self.last_service_date = last_service_date
		self.current_date = current_date

	def needs_service(self) -> bool:
		# Requires service every 4 years (126,144,000 seconds)
		return (self.current_date - self.last_service_date).total_seconds() > 126144000