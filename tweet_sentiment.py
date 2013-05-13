import sys
import json

#define global valuable here
scores = {}


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
         # This will store each tweet's json object in response_result in type(<'dict'>)
        response_result = json.loads(response)
        tweet = response_result["text"].encode('utf-8')
        # caculate the sentiment result of a tweet
        words = tweet.split(" ")
        count = 0
        for w in words:
            if scores.has_key(w):
                count += scores[w]
        print('%0.2f' % count)
        
        
    

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiment(sent_file)
    hw(tweet_file)

if __name__ == '__main__':
    main()
