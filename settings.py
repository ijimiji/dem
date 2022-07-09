from os import environ

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = environ.get("API_TOKEN", "foo")
# Wether temp images should be deleted
DELETE_TEMP = False