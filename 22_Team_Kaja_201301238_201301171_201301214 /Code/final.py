import json
import datetime
import collections
import matplotlib.pyplot as plt




def print_details(func, total_cnt, correct_cnt, wrong_cnt):
    print "Details " + func
    print "Total Tweets = ", total_cnt
    print "Correctly Extracted = ", correct_cnt
    print "Wrong Extracted = ", wrong_cnt
    print
    return


def extract_tweets_fromfile(filename):
    new = []
    fileopen = open(filename, "r")
    total_cnt = 0
    correct_cnt = 0
    wrong_cnt = 0

    for line in fileopen:
        try:
            tweet = json.loads(line.strip("\n"))
            new.append(tweet)
            correct_cnt = correct_cnt + 1
        except Exception, exception:
            #print str(exception)
            wrong_cnt = wrong_cnt + 1
        total_cnt = total_cnt + 1

    print_details("After Extracting Tweets", total_cnt, correct_cnt, wrong_cnt)
    return new


def extract_features_from_tweet(data):
    new = []
    k1 = u'text'
    #k6 = u'created_at'
    k6 = "createdAt"
    total_cnt = 0
    correct_cnt = 0
    wrong_cnt = 0
    length = len(data)
    length = min(100000, length)
    for i in xrange(0, length):
        try:
            dic = collections.OrderedDict()
            dic[k1] = str(data[i][k1])
            time = datetime.datetime.strptime(((data[i][k6])), "%b %d, %Y %I:%M:%S %p")
            dic[k6] = (int(time.strftime("%s"))/1)
            new.append(dic)
            correct_cnt = correct_cnt + 1
        except Exception, exception:
            #print str(exception)
            #print data[i][k6]
            #print
            wrong_cnt = wrong_cnt + 1
        total_cnt = total_cnt + 1

    print_details("After Extracting Features", total_cnt, correct_cnt, wrong_cnt)
    return new


def get_hashtags(data):
    hashtags = []
    k1 = u'text'
    #k6 = u'created_at'
    k6 = "createdAt"
    k7 = "tweet"
    k8 = "time"
    num_of_tweets = len(data)
    for i in xrange(0, num_of_tweets):
        if "#" in data[i][k1]:
            splited = data[i][k1].split()
            new_length = len(splited)
            temp = []
            for j in xrange(0, new_length):
                if "#"  in splited[j]:
                    det = {}
                    temp_word = ''.join(letter for letter in splited[j] if letter.isalnum())
                    if temp_word != '':
                        det[k7] = temp_word.lower()
                        det[k8] = data[i][k6]
                        hashtags.append(det)
    return hashtags



def count_hashtags(hashtags):
    dic_hashtags_count = {}
    dic_time_count = {}
    length = len(hashtags)
    k7 = "tweet"
    k8 = "time"
    for i in xrange(0, length):
        word = hashtags[i][k7]
        time = hashtags[i][k8]
        try:
            dic_hashtags_count[word].append(time)
        except Exception, exception:
            #print str(e)
            dic_hashtags_count[word] = []
            dic_hashtags_count[word].append(time)


        try:
            dic_time_count[time].append(word)
        except Exception, exception:
            #print str(e)
            dic_time_count[time] = []
            dic_time_count[time].append(word)
    return dic_hashtags_count, dic_time_count


def print_hastags_count(dic):
    sorted_dic = sorted(dic.items(), key=lambda x: -len(x[1]))
    for i in sorted_dic:
        print i[0] + " ", i[1]
    return


def get_timewise_hashtags(data):
    start = min(data.keys())
    end = max(data.keys())
    print "start = ", start
    print "end   = ", end
    #print sorted(data.keys())
    s = start
    e = s + 3600
    while 1:
        dic = {}
        print
        for i in xrange(s, e+1):
            try:
                for j in xrange(0, len(data[i])):
                    try:
                        dic[data[i][j]] = dic[data[i][j]] + 1
                    except Exception, exception:
                        dic[data[i][j]] = 1
            except Exception, exception:
                z = 1
        sorted_dic = sorted(dic.items(), key=lambda x: -(x[1]))
        #print sorted_dic
        length = min(10, len(sorted_dic))
        print s, " ", e
        for n in xrange(0, length):
            print sorted_dic[n][0] + " ", sorted_dic[n][1]
        print
        s = e + 1
        e = s + 3600
        if s >= end:
            break
    return


def print_result(tweet, mini, maxi, result, interval):
    print "Tweet = " + tweet
    print "mini = ", mini
    print "maxi = ", maxi
    for i in xrange(0, len(result)):
        print result[i]
    print
    print
    result.insert(0, 0)
    result.insert(0, 0)
    result.insert(0, 0)
    result.insert(0, 0)
    result.append(0)
    result.append(0)
    result.append(0)
    result.append(0)
    result.append(0)
    #plt.xticks(range(len(dic)), dic.keys())
    start=mini
    #for i in xrange(0, len(result)):
    #    c = datetime.datetime.fromtimestamp(start)
    #    result.append(c.hour)
    
    c = datetime.datetime.fromtimestamp(start)
    hr = c.hour
    xlab=[]
    xlab.insert(0,(hr-1+24)%24)
    xlab.insert(0,(hr-2+24)%24)
    xlab.insert(0,(hr-3+24)%24)
    xlab.insert(0,(hr-4+24)%24)
    for i in xrange(0, len(result)):
        xlab.append(hr)
        hr = (hr+1) % 24



    plt.plot(result)
    plt.ylabel('Frequency')
    plt.xlabel('Time ' + str(c.date()))
    plt.ylim(-2, max(result))
    plt.xlim(-2, len(result))
    plt.xticks(range(len(xlab)), xlab)
    plt.savefig(tweet + ".png")
    plt.clf()

    return


def get_wordwise_hastags(data):
    sorted_dic = sorted(data.items(), key=lambda x: -len(x[1]))
    length = len(sorted_dic)
    length = min(5, length)
    print
    for i in xrange(0, length):
        print sorted_dic[i][0]
        mini = min(sorted_dic[i][1])
        maxi = max(sorted_dic[i][1])
        result = []
        st = mini
        interval = 3600
        while 1:
            cnt = 0
            for k in xrange(0, interval):
                try:
                    cnt = cnt + sorted_dic[i][1].count(st+k)
                except Exception, exception:
                    print str(exception)
                    z = 1
            result.append(cnt)
            if st >= maxi:
                break
            st = st + interval
        print_result(sorted_dic[i][0], mini, maxi, result, interval)
    return




def main(filename):
    data = extract_tweets_fromfile(filename)
    data = extract_features_from_tweet(data)
    hashtags = get_hashtags(data)
    word_counted, time_counted = count_hashtags(hashtags)
    #print_hastags_count(word_counted)
    get_timewise_hashtags(time_counted)
    get_wordwise_hastags(word_counted)
    return




if __name__ == '__main__':
    file_name = './tofind1.txt'
    main(file_name)



#Aug 12, 2015 10:36:49 PM
#time.strptime(a, "%b %d, %Y %I:%M:%S %p")
#Aug 12, 2015 10:36:49 PM
#c = datetime.strptime(a, "%b %d, %Y %I:%M:%S %p")
#int(c.strftime("%s"))
#tt = datetime.datetime.timetuple(c)
#import calendar
#sec_epoch_utc = calendar.timegm(tt) * 1000
