import urllib
import json
import sys

def fil(tweet_file):
    context = tweet_file.readlines()
    for response in context:
        try:
            response_result = json.loads(response)        
            country = response_result["place"]["country_code"].encode('utf-8')
            if (country == 'US'):
                print response
        except Exception,e:
            a = 0
                
def main():
    tweet_file = open(sys.argv[1])
    fil(tweet_file)


if __name__ == '__main__':
    main()
