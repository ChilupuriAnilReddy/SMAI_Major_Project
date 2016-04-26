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
import re
import operator


def get_only_required(data):
	new = []
	k1=u'text'
	#k2=u'retweeted'
	#k3=u'timestamp_ms'
	#k4=u'entities'
	#k5=u'retweet_count'
	k6=u'created_at'
	total_cnt = 0
	correct_cnt =0
	wrong_cnt = 0
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
			correct_cnt = correct_cnt + 1
		except:
			wrong_cnt = wrong_cnt + 1
		total_cnt = total_cnt + 1
	
	print
	print "Details After Extracing Required Features\n"
	print "Total Tweets = ",total_cnt
	print "Correctly Extracted = ",correct_cnt
	print "Wrong Extracted = ",wrong_cnt
	print
	print
	
	return new



def get_only_text(data):
	new=[]
	k1="text"
	for i in data:
		new.append(i[k1].lower())
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


def get_hashtags(data):
	hashtags = []
	tempdata = get_only_text(data)
	num_of_tweets = len(tempdata)
	for i in xrange(0,num_of_tweets):
		if "#" in tempdata[i]:
			splited = tempdata[i].split()
			new_length  = len(splited)
			temp = []
			for j in xrange(0,new_length):
				if "#"  in splited[j]:
					temp.append(splited[j])
			hashtags.append(temp)
	return hashtags

def print_hashtags(hashtags):
	for i in xrange(0,len(hashtags)):
		print hashtags[i]
	return

def count_hashtags(hashtags):
	dic_hashtags_count = {}
	num_of_tweets = len(hashtags)
	for i in xrange(0,num_of_tweets):
		for j in xrange(0,len(hashtags[i])):
			word = hashtags[i][j][1:]
			temp_word = ''.join(letter for letter in word if letter.isalnum())
			try:
				dic_hashtags_count[temp_word] = dic_hashtags_count[temp_word] + 1
			except:
				dic_hashtags_count[temp_word] = 1
	return dic_hashtags_count

def print_hastags_count(dic):
	sorted_dic=sorted(dic.items(), key=lambda x: -x[1])
	#sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
	for i in sorted_dic:
		print i[0] + " " , i[1]
	return

def main(filename):
	data = []
	fileopen = open(filename, "r")
	total_cnt = 0
	correct_cnt=0
	wrong_cnt = 0

	for line in fileopen:
		try:
			tweet = json.loads(line.strip("\n"))
			data.append(tweet)
			correct_cnt = correct_cnt + 1
		except:
			wrong_cnt = wrong_cnt + 1
		total_cnt = total_cnt + 1

	print
	print "Details After Json Loads\n"
	print "Total Tweets = ",total_cnt
	print "Correctly Jsonified = ",correct_cnt
	print "Wrong Jsonified = ",wrong_cnt
	print
	print
	data = get_only_required(data)
	hashtags = get_hashtags(data)
	counted = count_hashtags(hashtags)
	print_hastags_count(counted)
	
	#lda(data)




if __name__ == '__main__':
	file_name = './pythondata.txt'
	main(file_name)



#Aug 12, 2015 10:36:49 PM
#time.strptime(a, "%b %d, %Y %I:%M:%S %p")
#Aug 12, 2015 10:36:49 PM
#c = datetime.strptime(a, "%b %d, %Y %I:%M:%S %p")
#int(c.strftime("%s"))
#tt = datetime.datetime.timetuple(c)
#import calendar
#sec_epoch_utc = calendar.timegm(tt) * 1000
