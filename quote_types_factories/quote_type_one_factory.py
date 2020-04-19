
import requests
from requests.exceptions import HTTPError

from .abs_quote_type_factory import AbsQuoteTypeFactory
from quote import Quote

class QuoteTypeOneFactory(AbsQuoteTypeFactory):
	"""docstring for QuoteTypeOneFactory"""
	API_URL = 'http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'

	def __init__(self):	
		pass

	def create(self):
		try:
			response = requests.get(self.API_URL)
			response.raise_for_status()
			json_data = response.json()
		except HTTPError as http_err:
			print(f'HTTP error occurred: {http_err}')
		except ValueError as err:
			print(f'JSON decoding error occurred: {err}')
		except Exception as err:
			print(f'Other error occurred: {err}')
		else:
			return Quote(text=json_data['quoteText'], author=json_data['quoteAuthor'])