import urllib.request #handling url
from bs4 import BeautifulSoup #parsing html files
import nltk
from nltk.corpus import stopwords #to remove words like is, was, this, that
#nltk.download("stopwords") #uncomment for 1st time

#to get information from a website
response = urllib.request.urlopen("https://en.wikipedia.org/wiki/Artificial_intelligence")
#to read the contents
html = response.read()

#to remove tags and extra whitespaces
soup = BeautifulSoup(html, 'html5lib')
text = soup.get_text(strip = True)


#store as tokens
tokens =  []
for t in text.split():
    tokens.append(t)

#remove stopwords
sw = stopwords.words('english')
cleaned_tokens = tokens[:]
for token in tokens:
    if token in sw:
        cleaned_tokens.remove(token)

#calculate the frequency of each word
freq = nltk.FreqDist(cleaned_tokens)
#uncomment below 2 lines to print in command line 
#for key, value in freq.items():
    #print(str(key) + ":" + str(value))

#plot a graph for words vs frequency
freq.plot(30)

