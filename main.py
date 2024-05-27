import string
from collections import Counter
from nltk.tokenize import  word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()
cleaned_text =  lower_case.translate(str.maketrans('','',string.punctuation))

tokenized_words = word_tokenize(cleaned_text,"english")
print(tokenized_words)




final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

print(final_words)

emotion_list = []
with open('emotion.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')
        print("Word :" + word + " " + "Emotion :" + emotion)

        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)
w = Counter(emotion_list)
print(w)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral")
sentiment_analyse(cleaned_text)

fig , axl = plt.subplots()
plt.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()