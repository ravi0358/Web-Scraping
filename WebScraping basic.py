#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from requests import get


# In[2]:


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}


# In[3]:


cisco = get("https://www.trustradius.com/products/cisco-webex-meetings/reviews?f=25", headers = headers)


# In[4]:


cisco.status_code


# In[5]:


from bs4 import BeautifulSoup
cisco_soup = BeautifulSoup(cisco.text,'html.parser')


# In[6]:


cisco_soup


# In[7]:


container = cisco_soup.find_all("div", class_ = "serp-header")
print(type(container))


# In[8]:


container


# In[9]:


len(container)


# In[13]:


review_2 = container[24]


# In[14]:


review_2


# In[15]:


#Reviw
review_2.find('h3').text


# In[16]:


#Date
review_2.select('div.review-date')[0].text


# In[17]:


#score
review_2.select('div.trust-score__score span')[1].text


# In[18]:


#Name
review_2.select('div.name')[0].text


# In[19]:


#Position
review_2.select('div.position')[0].text


# In[20]:


#Industry Type
review_2.select('span.industry-type')[0].text


# In[21]:


#Spam company name
review_2.select('span.company')[0].text


# In[ ]:


#Number of Employees
review_2.select('span.size')[0].text


# In[ ]:


if not review_2.select('span.size'):
    print('empty')
else:
    print(review_2.select('span.size')[0].text)


# In[ ]:





# # Body 

# In[ ]:


container2 = cisco_soup.find_all("div", class_ = 'serp-body')
print(type(container2))


# In[ ]:


len(container2)


# In[ ]:


review_body = container2[0]


# In[ ]:


# review_body.select('div.ugc')[0].text


# In[ ]:


review_body.select('div.question-response-container')[0].text


# In[ ]:





# In[ ]:


review_body.select('ul.pros')[0].text


# In[ ]:


review_body.select('ul.cons')[0].text


# In[ ]:


review_body.select('div.ugc')[0].text


# In[ ]:





# # URLS

# In[ ]:


cisco = get("https://www.trustradius.com/vendors/cisco", headers = headers)


# In[ ]:


cisco.status_code


# In[ ]:


from bs4 import BeautifulSoup
cisco_soup = BeautifulSoup(cisco.text,'html.parser')


# In[ ]:


cisco_soup


# In[ ]:


main_table = cisco_soup.find_all('a',class_='ProductGridProduct_product__2iNPt')


# In[ ]:


main_table


# In[ ]:


urls = [] 
for i in main_table:
    url = i['href']
    if not url.startswith('http'):
        url = "https://www.trustradius.com"+url
    urls.append(url)


# In[ ]:


#https://www.trustradius.com
urls


# In[ ]:




