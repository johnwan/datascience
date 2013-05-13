from __future__ import division
import sys
import json

#define global valuable here
total_term = 0
dict_term = {}


def hw(tweet_file):
    global total_term,dict_term
    context = tweet_file.readlines()
    for response in context:
         # This will store each tweet's json object in response_result in type(<'dict'>)
        response_result = json.loads(response)
        tweet = response_result["text"].encode('utf-8')
        # caculate the sentiment result of a tweet
        words = tweet.split()
        for w in words:
            if not dict_term.has_key(w):
                dict_term[w] = 1
            else:
                dict_term[w] += 1            
            total_term += 1
            
    # Print frequency of each word    
    for k in dict_term.iterkeys():        
        frq = dict_term[k] / total_term
        print(k + ' %0.4f' % frq)

        
        
    

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)


if __name__ == '__main__':
    main()
