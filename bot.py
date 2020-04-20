import os
from glob import glob
import sys, inspect
import random

import quote_types_factories
import twitter

def main():
	quote_types_classes = inspect.getmembers(sys.modules['quote_types_factories'], inspect.isclass)
	cls_quote_type_factory = random.choice(quote_types_classes)

	quote_factory = cls_quote_type_factory[1]()
	quote = quote_factory.create()

	twitter.post(quote)

if __name__ == "__main__":
	main()