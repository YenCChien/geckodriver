
# coding: utf-8

# In[87]:


from selenium import webdriver
from PIL import Image


# In[88]:


driver = webdriver.Chrome('C:/Users/nick/Desktop/chromedriver.exe')
#driver = webdriver.Firefox()


# In[89]:


driver.get('http://railway.hinet.net/ctno1.htm') 


# In[90]:


pageSource = driver.page_source


# In[91]:


print(pageSource)


# In[92]:


driver.find_element_by_id("person_id").send_keys('S123456789')
driver.find_element_by_id("from_station").send_keys('115')
driver.find_element_by_id("to_station").send_keys('185')
driver.find_element_by_id("getin_date").send_keys('2017/08/25')
driver.find_element_by_id("train_no").send_keys('121')
driver.find_element_by_id("order_qty_str").send_keys('2')


# In[93]:


driver.find_element_by_xpath("/html/body/form/table/tbody/tr[9]/td[2]/button").click()


# In[106]:


import urllib
path = "//*[@id='idRandomPic']"
img = driver.find_element_by_xpath(path)
#for k in driver.find_elements_by_xpath(path):
#    items = []
#    src = (k.get_attribute('src')).encode('utf8')
#    items.append(src)
#    print items
src = img.get_attribute('src')
urllib.request.urlretrieve(src, "captcha.jpeg")


# In[98]:


#import requests
#with open('kaptcha.jpg', 'wb') as f:
#    res = requests.get(items[0])
#    f.write(res.content)


# In[99]:


#from PIL import Image
#image = Image.open('kaptcha.jpg')
#image


# In[29]:


driver.find_element_by_id("randInput").send_keys('18633')


# In[30]:


driver.find_element_by_xpath("//*[@id='sbutton']").click()


# In[86]:


driver.close()


# In[ ]:




