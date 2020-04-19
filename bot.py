import os
from glob import glob
import sys, inspect
import random

import quote_types_factories

def main():
	quote_types_classes = inspect.getmembers(sys.modules['quote_types_factories'], inspect.isclass)
	cls_quote_type_factory = random.choice(quote_types_classes)

	quote_factory = cls_quote_type_factory[1]()
	quote = quote_factory.create()
	quote_text = quote.text
	quote_author = quote.author
	
	print(quote_text)
	print(quote_author)

if __name__ == "__main__":
	main()