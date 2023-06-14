from os import getenv
from dotenv import find_dotenv, load_dotenv
from akeneo.akeneo import Akeneo
load_dotenv(find_dotenv())

AKENEO_HOST = getenv('AKENEO_HOST')
AKENEO_CLIENT_ID = getenv('AKENEO_CLIENT_ID')
AKENEO_CLIENT_SECRET = getenv('AKENEO_CLIENT_SECRET')
AKENEO_USERNAME = getenv('AKENEO_USERNAME')
AKENEO_PASSWORD = getenv('AKENEO_PASSWORD')

AKENEO_SEARCH_QUERY_ENABLED = getenv('AKENEO_SEARCH_QUERY_ENABLED')
AKENEO_SEARCH_QUERY_COMPLETENESS = getenv('AKENEO_SEARCH_QUERY_COMPLETENESS')
AKENEO_SEARCH_QUERY_SCOPE = getenv('AKENEO_SEARCH_QUERY_SCOPE')

def getAkeneoProducts():
  akeneo = Akeneo(
    AKENEO_HOST,
    AKENEO_CLIENT_ID,
    AKENEO_CLIENT_SECRET,
    AKENEO_USERNAME,
    AKENEO_PASSWORD
  )
  searchQuery = '{"enabled":[{"operator":"=","value":'+ AKENEO_SEARCH_QUERY_ENABLED +'}],"completeness":[{"operator":"=","value":' + AKENEO_SEARCH_QUERY_COMPLETENESS +',"scope":"'+AKENEO_SEARCH_QUERY_SCOPE+'"}]}'
  return akeneo.getProducts(limit=100, search=searchQuery, scope=AKENEO_SEARCH_QUERY_SCOPE)

def extract():
  data = getAkeneoProducts()
  return data