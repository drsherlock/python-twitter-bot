import logging
import os
import tweepy

import config

logger = logging.getLogger()

def create_api():
	consumer_key = os.getenv("CONSUMER_KEY") or config.CONSUMER_KEY
	consumer_secret = os.getenv("CONSUMER_SECRET") or config.CONSUMER_SECRET
	access_token = os.getenv("ACCESS_TOKEN") or config.ACCESS_TOKEN
	access_token_secret = os.getenv("ACCESS_TOKEN_SECRET") or config.ACCESS_TOKEN_SECRET

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True,
		wait_on_rate_limit_notify=True)
	try:
		api.verify_credentials()
	except Exception as err:
		logger.error("Error creating API", exc_info=True)

	logger.info("API created")
	return api

def post(quote):
	status = f'"{quote.text}" -{quote.author}'
	api = create_api()
	try:
		response = api.update_status(status)
	except Exception as err:
		logger.error("Error posting tweet", exc_info=True)
