import abc

class AbsQuoteTypeFactory(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def create(self):
		pass