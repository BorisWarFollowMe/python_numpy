#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Задание 1


# In[2]:


import pandas as pd


# In[3]:


authors = pd.DataFrame({
    "author_id": [1, 2, 3],
    "author_name": ['Тургенев', 'Чехов', 'Островский']
})


# In[4]:


book = pd.DataFrame({
    "author_id": [1, 1, 1, 2, 2, 3, 3],
    "book_title": ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
    "price": [450, 300, 350, 500, 450, 370, 290]
})


# In[5]:


### Задание 2


# In[6]:


authors_price = pd.merge(authors, book, on='author_id', how='inner')
authors_price


# In[7]:


### Задание 3


# In[8]:


top5 = authors_price.nlargest(5, "price")
top5.reset_index(drop=True, inplace=True)
top5


# In[9]:


### Задание 4


# In[10]:


### вариант 1 (merge)

authors_price1 = authors_price.groupby("author_name")
as1 = pd.merge(authors["author_name"], authors_price1["price"].min(), on='author_name', how='inner')
as2 = pd.merge(as1, authors_price1["price"].max(), on='author_name', how='inner')
authors_stat = pd.merge(as2, authors_price1["price"].mean(), on='author_name', how='inner')
authors_stat.rename({"price_x": "min_price", "price_y": "max_price", "price": "mean_price"}, axis='columns')


# In[11]:


### вариант 2 (concat)

apgroup = authors_price.groupby("author_name")
authors_stat = pd.concat([apgroup["price"].min(), apgroup["price"].max(), apgroup["price"].mean()], axis=1, ignore_index=True)
authors_stat.rename(columns={0: "min_price", 1: "max_price", 2: "mean_price"})

