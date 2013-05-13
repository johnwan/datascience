from __future__ import division
import sys
import json
from collections import OrderedDict

#define global valuable here
scores = {}
state_hap = {}



def sentiment(sent_file):
    global scores
    afinnfile = sent_file
     # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    
def hw(tweet_file):
    global scores
    context = tweet_file.readlines()
    for response in context:
        try:
             # This will store each tweet's json object in response_result in type(<'dict'>)
            response_result = json.loads(response)
            tweet = response_result["text"].encode('utf-8')
            # get the state of the tweet
            location = response_result["place"]["full_name"].encode('utf-8')
            state = location[-2:]
            #print(state)
            # caculate the sentiment result of a tweet
            words = tweet.split(" ")
            count = 0
            for w in words:
                if scores.has_key(w):
                    count += scores[w]
            hap_state(state,count)
        except Exception,e:
             a = 0

def hap_state(state,score):
    global state_hap
    short_state=["CO","SC","ND","SD","DE","FL",
                 "GA","HI","ID","IL","IN","IA",
                 "KS","KY","LA","ME","MD","MA",
                 "MI","MN","MS","MO","MT","NE",
                 "NV","NH","NJ","NY","NM","OH",
                 "OK","OR","PA","RI","TN","TX",
                 "UT","VT","VA","WA","WV","WI",
                 "WY","AK","AZ","AR","CA","NC","CT"]
    if (state in short_state):
        if (state_hap.has_key(state)):
            state_hap[state][0] += 1
            state_hap[state][1] += score
        else:
            state_hap[state] = [1,score]
        
def sort(d):
    result = list(OrderedDict(sorted(d.items(), key=lambda t: t[1][1]/t[1][0])))
    print(result[-1])
    #for k in result:
    #    print (k + ' ' + str(d[k][1]/d[k][0]))
    
        
    

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiment(sent_file)
    hw(tweet_file)
    sort(state_hap)
    
        

if __name__ == '__main__':
    main()
