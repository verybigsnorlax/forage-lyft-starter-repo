from tire import Tire

class CarriganTire(Tire):
	def __init__(self, tires : list):
		self.tires = tires

	def needs_service(self) -> bool:
		return any(map(lambda wear: wear >= 0.9, self.tires))