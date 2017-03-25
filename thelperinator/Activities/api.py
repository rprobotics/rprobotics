import argparse
import json
import pprint
import sys
import urllib
import urllib2

import oauth2



API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 12
#SEARCH_PATH = '/v2/businesses/search/'
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = "X6vW_6VSX2FzT-oy1AZ_Tw"
CONSUMER_SECRET = "m6W3ScxTQFjuFZBX3LZC0HKYZfg"
TOKEN = "pWyYv0ZD4aFIQDXX7RWcMUJRMC7XmJV6"
TOKEN_SECRET ="YmdyaURrewWbRsSxmIbSVOl365s"



def query_api(term, location):
    print "QUERYING YELP! =)"


    """
    auth = Oauth1Authenticator(
        consumer_key="X6vW_6VSX2FzT-oy1AZ_Tw",
        consumer_secret="m6W3ScxTQFjuFZBX3LZC0HKYZfg",
        token="pWyYv0ZD4aFIQDXX7RWcMUJRMC7XmJV6",
        token_secret="YmdyaURrewWbRsSxmIbSVOl365s"
    )

    client = Client(auth)
    """
    params = {
        "term": "food"#,
#        'lang': 'en'
    }
    # read API keys
    with io.open('Activities/yelp_auth.json') as cred:
        creds = json.load(cred)
        auth = Oauth1Authenticator(**creds)
        client = Client(auth)
    
    #terms="term=dinner,location=San+Francisco"
    #results=urlparse("https://{0}{1}?{2}".format(API_HOST,SEARCH_PATH,terms))
    #print results
    #return results
    results=client.search('San Francisco', **params)
    print str(results)
    
    