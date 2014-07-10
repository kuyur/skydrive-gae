# -*- coding: utf-8 -*-
import webapp2
import urllib2, httplib
import re

def getcid(link):
    pos = link.find('.office.live.com')
    return link[4:pos]

def to_new_type_link(link):
    pos = link.find('.office.live.com')
    cid = link[4:pos]
    uri = link[pos+len('.office.live.com'):]
    return 'skydrive.live.com' + uri + '?cid=' + cid# + '&sc=documents'

def get_real_link(static_url):
    curl = "https://" + static_url
    response = urllib2.urlopen(curl)
    return response.geturl()

def get_dynamic_download_link(real_url, cid):
    pos = real_url.find(cid) + len(cid) + len('&id=')
    resid = real_url[pos:]
    real_url2 = 'https://skydrive.live.com/download.aspx?cid=' + cid.upper() + '&resid=' + resid + '&canary='
    response = urllib2.urlopen(real_url2)
    return response.geturl()

def replace_html_code(old_link):
    return old_link.replace('\\/','/')

class MainPage(webapp2.RequestHandler):
    def get(self):
        old_type_link = self.request.path[1:]
        cid = getcid(old_type_link)
        new_type_link = to_new_type_link(old_type_link)
        real_link = get_real_link(new_type_link)
        self.redirect(replace_html_code(get_dynamic_download_link(real_link, cid)))
        
class IndexPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('''<html>
<head>
<title>
skydrie-gae
</title>
<meta content="A Google App Engine application for redirect the skydrive link" name="description">
<meta content="skydrive, skydirve-gae, gae, google app engin," name="keywords">
<meta name="google-site-verification" content="MRuE10bVaHltuPvjYFH0PGfvJAuCZ2FScfAviXiKDFE" />
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-4981483-8']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
</head>
<body>
This another Google App Engine application!<br>
You can use it redirect the skydrive link.<br>
It's very simple:copy your skydrive link after the HOST,Then it's work.<br>
<br>
For Example:<br>
your skydrive link is <br>
http://cid-7978ee0a34b7f662.office.live.com/self.aspx/Public/EMS/2010/0627.mp3<br>
Then the static access link should be <br>
http://skydrive-gae.appspot.com/cid-7978ee0a34b7f662.office.live.com/self.aspx/Public/EMS/2010/0627.mp3<br>

remember remove the skydrive "http://"<br>

<br>
Thanks to <img src="http://msl.appspot.com/static/images/gmail.png"><br>
<br>
Modified by <a href="http://kuyur.info/blog" target="_blank"><img src="http://kuyur.info/blog/uploads/2010/03/mail.png"></a><br>
</body>
</html>''')
     
app = webapp2.WSGIApplication(
                                     [('/', IndexPage),
                                     ('/index.html', IndexPage),
                                     ('/index.htm', IndexPage),
                                     ('/cid.*', MainPage),
                                     #(r'/http\*',MainPage),
                                     ],
                                     debug=True)
