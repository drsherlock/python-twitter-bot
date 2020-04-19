
import requests
from requests.exceptions import HTTPError

from .abs_quote_type_factory import AbsQuoteTypeFactory
from quote import Quote

class QuoteTypeTwoFactory(AbsQuoteTypeFactory):
	"""docstring for QuoteTypeTwoFactory"""
	API_URL = 'https://programming-quotes-api.herokuapp.com/quotes/random'

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
			return Quote(text=json_data['en'], author=json_data['author'])