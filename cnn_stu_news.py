#coding:utf-8
import sys
reload(sys)
#sys.setdefaultencoding('utf-8')
import chardet
import urllib

from pyquery import PyQuery as pq

#
def cnn_dl(mon,day):
    if day==01:
        return 'sorry, I have not say the rule of how to name the first day of the month'
    

    year='13'
    mon=mon
    day=day
    pre_day=str(int(day)-1)
    
    url_n='http://transcripts.cnn.com/TRANSCRIPTS/'+year+mon+'/'+day+'/sn.01.html'
    print url_n
    d=pq(url=(url_n))
    #print d('title')
    #top_headlines_news_module
    #for link in d('#top_headlines_module').children('a'):
    #    print link.text()
    d1=d('.cnnTransSubHead').text()
    d2=d('.cnnBodyText').eq(2).html().replace('<br/>','\n')
    
    filename=year+mon+day+"_"+d1
    try:
        print 'STH wrong with the file name'
        fobj = open(filename+'.txt','w')
    except:
        filename=year+mon+day
        fobj = open(filename+'.txt','w')
    fobj.write(d2)
    fobj.close()
    
    v_name='http://podcasts.cnn.net/cnn/big/podcasts/studentnews/video/2013/'+mon+'/'+pre_day+'/sn-'+mon+day+year+'.cnn.m4v'
    urllib.urlretrieve(v_name,filename+'.m4v')


if __name__ == '__main__':
#    year = open(sys.argv[1])
#    mon = open(sys.argv[1])
#    day = open(sys.argv[2])
#    inputdata = open('matrix.json')
    cnn_dl('05','20')