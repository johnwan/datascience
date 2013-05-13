import sys
import json

#define global valuable here
scores = {}
new_scores = {}


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
        words = tweet.split()
        score = 0
        for w in words:
            if scores.has_key(w):
                score += scores[w]
        for w in words:
            if not scores.has_key(w):
                caculate_count(w,score)
        
def caculate_count(word,score):
    global new_scores
    if (not new_scores.has_key(word)):
        new_scores[word] = [1,score]
    else:
        new_scores[word][0] += 1
        new_scores[word][1] += score

def average(dic):
    for k in dic:
        #print(str(dic[k][0]) + ' '+ str(dic[k][1]))
        dic[k][1] = dic[k][1]/dic[k][0]
        print(str(k)+" %0.2f" % dic[k][1])

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiment(sent_file)
    hw(tweet_file)
    #for k in new_scores.keys():
    average(new_scores)
        

if __name__ == '__main__':
    main()
