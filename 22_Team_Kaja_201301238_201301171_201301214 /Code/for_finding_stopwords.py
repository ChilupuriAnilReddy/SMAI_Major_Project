import json
import pandas as pd
import matplotlib.pyplot as plt
import collections
import nltk
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from nltk.tokenize import word_tokenize
import gensim
import re
import operator


def get_only_required(data):
	new = []
	k1=u'text'
	total_cnt = 0
	correct_cnt =0
	wrong_cnt = 0
	for i in xrange(0,len(data)):
		try:
			dic = collections.OrderedDict()
			dic[k1] = str(data[i][k1])
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



def print_dictionary(dic):
	print
	sorted_dic=sorted(dic.items(), key=lambda x: -x[1])
	#sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
	for i in sorted_dic:
		print i[0] + " " , i[1]
	print
	return


def print_dictionary1(dic):
	print
	
	#sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
	for i in dic:
		print i
		print 
		sorted_dic=sorted(dic[i].items(), key=lambda x: -x[1])
		for j in sorted_dic:
			print j[0] + " " , j[1]
		print
	print
	return



def get_parts_of_speech(data):
	only_tweet = get_only_text(data)	
	tokenizer = RegexpTokenizer(r'\w+')
	p_stemmer = PorterStemmer()

	length = len(only_tweet)
	length = min(length,length)
	total_texts = []

	for i in xrange(0,length): 
		to_lower = only_tweet[i].lower()
		tokens = tokenizer.tokenize(to_lower)
		#texts = [p_stemmer.stem(k) for k in tokens]
		total_texts.append(tokens)

	
	dic_pos = {}
	dic_fre = {}
	
	for i in xrange(0,length):
		for j in xrange(0,len(total_texts[i])):
			text = word_tokenize(str(total_texts[i][j]))
			a = nltk.pos_tag(text)
			try:
				dic_pos[a[0][1]] = dic_pos[a[0][1]] + 1
			except:
				dic_pos[a[0][1]] = 1
			
			try:
				check = dic_fre[a[0][1]]  
			except:
				dic_fre[a[0][1]] = {}

			try:
				dic_fre[a[0][1]][a[0][0]] = dic_fre[a[0][1]][a[0][0]]+1
			except:
				dic_fre[a[0][1]][a[0][0]]  =1 

	
	print_dictionary(dic_pos)
	print_dictionary1(dic_fre)



	return total_texts


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
	pos = get_parts_of_speech(data)
	
	




if __name__ == '__main__':
	file_name = './tofind.txt'
	main(file_name)