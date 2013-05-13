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
        try:
            response_result = json.loads(response)
            i = 0
            while(len(response_result['entities']['hashtags'][i]['text']) != 0):
                tweet = response_result['entities']['hashtags'][i]['text']
                w = tweet.decode('utf-8')
                # caculate the sentiment result of a tweet
                #for w in hashtag:
                #print(w)
                if not dict_term.has_key(w):
                    dict_term[w] = 1
                else:
                    dict_term[w] += 1            
                total_term += 1
                i += 1
        except Exception:
            pass
            
    # Print frequency of each word
    sort = sorted(dict_term.items(),key=lambda t: t[1], reverse=True)
    #print(str(dict_term.items()))
    sort = list(sort)
    for i in range(10):
        print(sort[i][0] + ' %0.4f' % sort[i][1])
        #print(sort[i][0] + ' %0.4f' % (sort[i][1]/total_term))
        
    

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)


if __name__ == '__main__':
    main()
