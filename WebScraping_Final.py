#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
import requests, bs4
from requests import get
from bs4 import BeautifulSoup
from IPython.core.display import clear_output
from warnings import warn
from time import sleep
from random import randint
from time import time


# In[2]:


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}


# In[3]:


step1=0
step2=50


# In[4]:


pages = [str(i) for i in range(step1,step2,25)]


# In[5]:


pages


# In[6]:


review_titles = []
review_dates = []
user_scores=[]
names = []
positions = []
companys=[]
IndustryTypes=[]
Employees=[]
review_bodys = []
review_pros = []
review_cons = []


# Getting Links of all Cisco Products

# In[7]:


cisco_url = get("https://www.trustradius.com/vendors/cisco", headers = headers)


# In[8]:


cisco_soup_url = BeautifulSoup(cisco_url.text,'html.parser')


# In[9]:


main_table = cisco_soup_url.find_all('a',class_='ProductGridProduct_product__2iNPt')


# In[10]:


urls = [] 
for i in main_table:
    url = i['href']
    if not url.startswith('http'):
        url = "https://www.trustradius.com"+url
    urls.append(url)


# In[11]:


urls


# Creating function for getting data

# In[12]:


def cisco_data(url):
    requests = 0
    start_time = time()
    for page in pages:
        #make a get request
        #cisco = get('https://www.trustradius.com/products/cisco-webex-meetings/reviews?f='+page, headers = headers)
        cisco = get(url+'?f='+page,headers = headers)
        
        
        #pause the loop for 8-20 seconds
        sleep(randint(8,20))
    
        #monitor the requests
        requests += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait = True)
    
        #show a warning if a non 200 status code is returned
        if cisco.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))
        
        
        cisco_soup = BeautifulSoup(cisco.text,'html.parser')
    
        #find the major tag peculiar to each review
        container = cisco_soup.find_all("div", class_ = 'serp-header')
        container2 = cisco_soup.find_all("div", class_ = 'serp-body')
        #iterate through the major tag 
        for con in container:
            
            #scrape the review body
            if not con.find('h3'):
                review_title='-'
            else:
                review_title = con.find('h3').text
            review_titles.append(review_title)
            
            
            #scrape the review dates
            if not con.select('div.review-date'):
                review_date='-'
            else:
                review_date = con.select('div.review-date')[0].text
            review_dates.append(review_date)
    
    
            #scrape the user scores
            if not con.select('div.trust-score__score span'):
                user_score='-'
            else:
                user_score= con.select('div.trust-score__score span')[1].text
            user_scores.append(user_score)
    
            #scrape the user names.
            if not con.select('div.name'):
                name='-'
            else:
                name = con.select('div.name')[0].text
            names.append(name)
        
            #scrape the user positions.
            if not con.select('div.position'):
                position='-'
            else:
                position = con.select('div.position')[0].text
            positions.append(position)
            
            #scrape the company
            if not con.select('span.company'):
                company='-'
            else:
                company=con.select('span.company')[0].text
            companys.append(company)

        
            #scrape the industry tupe.
            if not con.select('span.industry-type'):
                IndustryType='-'
            else:
                IndustryType = con.select('span.industry-type')[0].text
            IndustryTypes.append(IndustryType)
        
            #scrape the employees count
            if not con.select('span.size'):
                Employee='-'
            else:
                Employee = con.select('span.size')[0].text
            Employees.append(Employee)
        
            #scrape the review body
        for con in container2:
            if not con.select('div.question-response-container')[0]:
                review_body = '-'
            else:
                review_body= con.select('div.question-response-container')[0].text
            review_bodys.append(review_body)
        
        
            #scrape the review pros
            if not con.select('ul.pros'):
                review_pro='-'
            else:
                review_pro = con.select('ul.pros')[0].text
            review_pros.append(review_pro)
        
        
            #scrape the review cons
            if not con.select('ul.cons'):
                review_con='-'
            else:
                review_con = con.select('ul.cons')[0].text
            review_cons.append(review_con)
   # return review_titles,review_bodys,review_pros,review_cons,review_dates,user_scores,names,positions,IndustryTypes,Employees
        
        
        


# In[13]:


urls = ['https://www.trustradius.com/products/cisco-webex-meetings/reviews',
 'https://www.trustradius.com/products/cisco-catalyst/reviews']


# In[14]:


#Links pass to function
for url in urls:
    cisco_data(url)


# In[15]:


cisco_df = pd.DataFrame({'Review_Title': review_titles,
                         'Review_body':review_bodys,
                         'Review_pros':review_pros,
                         'Review_cons':review_cons,
'Review_date': review_dates,
'User_Rating': user_scores,
'Customer_Name': names,
'Position':positions,
'Company':companys,
'IndustryType':IndustryTypes,
'Number 0f Employees':Employees})
print(cisco_df.info())


# In[16]:


cisco_df


# In[ ]:




