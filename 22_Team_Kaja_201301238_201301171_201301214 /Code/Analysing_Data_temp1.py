import json
import pandas as pd
import matplotlib.pyplot as plt
import collections
import nltk
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim


def get_only_required(data):
	new = []
	k1=u'text'
	k2=u'retweeted'
	k3=u'timestamp_ms'
	k4=u'entities'
	k5=u'retweet_count'
	k6=u'created_at'
	cnt = 0
	for i in xrange(0,len(data)):
		try:
			dic = collections.OrderedDict()
			dic[k1] = str(data[i][k1])
			dic[k2] = str(data[i][k2])
			dic[k3] = str(data[i][k3])
			dic[k4] = str(data[i][k4])
			dic[k5] = str(data[i][k5])
			dic[k6] = str(data[i][k6])
			new.append(dic)
		except:
			print data[i]
			print
			print type(data[i])
			print
			print type(data[i][k1])
			print
			print data[i].keys()
			print
			print type(data[i].keys()[0])
			print
			print type(k1)
			print
			print data[i][k1]
			return
			cnt = cnt + 1
	print "get_only_required " , cnt
	return new



def get_only_text(data):
	new=[]
	k1="text"
	for i in data:
		new.append(i[k1])
	return new

def lda(data):
	data = get_only_text(data)
	only_tweet = data
	length = len(only_tweet)
	length = min(20,length)
	for i in xrange(0,length):
		print i
		print only_tweet[i]
	return
	
	tokenizer = RegexpTokenizer(r'\w+')
	en_stop = get_stop_words('en')
	p_stemmer = PorterStemmer()

	length = len(only_tweet)
	length = min(20,length)
	total_texts = []
	for i in xrange(0,length):
		print only_tweet[i]
		print 
		to_lower = only_tweet[i].lower()
		tokens = tokenizer.tokenize(to_lower)
		stopped_tokens = [k for k in tokens if not k in en_stop]
		texts = [p_stemmer.stem(k) for k in stopped_tokens]
		total_texts.append(texts)

	dictionary = corpora.Dictionary(total_texts)
	corpus = [dictionary.doc2bow(text) for text in total_texts]

	ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=20)
	result =  ldamodel.print_topics(num_topics=2, num_words=1)
	for i in result:
		print i

def main(filename):
	data = []
	fileopen = open(filename, "r")
	cnt = 0
	for line in fileopen:
		try:
			tweet = json.loads(line.strip("\n"))
			data.append(tweet)
		except:
			cnt = cnt + 1
			continue
	print "main " ,cnt
	print
	data = get_only_required(data)
	#lda(data)



if __name__ == '__main__':
	file_name = './pythondata.txt'
	main(file_name)