
class Quote:
	def __init__(self, text="", author=""):
		self._text = text
		self._author = author

	@property
	def text(self):
		return self._text

	@property
	def author(self):
		return self._author