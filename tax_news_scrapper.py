#coding:utf-8
import sys
reload(sys)
#sys.setdefaultencoding('utf-8')
import chardet
__author__ = 'Sizuo'
from pyquery import PyQuery as pq
fobj = open('tax.txt','w')
for i in range(1,5):
    d=pq(url=('http://shiju.tax861.gov.cn/bjds/nsfw/wyzx/jrrx_more.asp?aa='+str(i)))
    #print d('title')
    #top_headlines_news_module
    #for link in d('#top_headlines_module').children('a'):
    #    print link.text()
    d1=d('.xubiandi table tr td a')
    d2=d('.xubiandi table tr td font')
    #d2=d('.xubiandi table tr td font')
    s1=u"下一页"
    s2=u"首页"
    #fobj.writelines([‘%s%s’ %(x, ls) for x in all])
    for i in range(0,d1.size()-1):
        if unicode(d1.eq(i).text())==s1 or unicode(d1.eq(i).text())==s2:
            break
        temp_str=d1.eq(i).text() + " " +d2.eq(i).text()
        detail_page=pq(url=d1.eq(i).make_links_absolute().attr('href'))
        content=detail_page('#div_zhengwen').text()
        fobj.write(temp_str)
        fobj.write('\n')
        fobj.write(content)
        fobj.write('\n')
        fobj.write('\n')
        fobj.write('\n')
fobj.close()
#d.make_links_absolute()
#for i in range(1,d.size()):
    #print d.children('a').attr('href')
   # psg=pq(url=d.children('a').attr('href'))
   # content=psg('#story_display').children()
