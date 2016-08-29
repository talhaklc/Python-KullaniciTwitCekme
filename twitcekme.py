#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup  #Sayfaya dahil ediyoruz
import requests

http_request = requests.get("https://www.twitter.com/talhaklc")
content = BeautifulSoup(http_request.content,"html.parser")

i=1
for tweets in content.find(id="stream-items-id").find_all("div","js-tweet-text-container"):  #sayfanın kaynak koduna baktığınızda gördüğünüz yapıya göre burayı belirliyoruz
   print("{} ) {}".format(str(i),tweets.get_text().strip().encode("utf-8"))) 
   i+=1