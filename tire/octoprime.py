from tire import Tire

class OctoprimeTire(Tire):
	def __init__(self, tires : list):
		self.tires = tires

	def needs_service(self):
		return sum(self.tires) >= 3