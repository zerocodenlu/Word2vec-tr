#!/usr/bin/env python
# coding: utf-8

# In[54]:


#turkish word to vectors
from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('tr-word2veq-20190320', binary=True)


# In[55]:


model.most_similar(positive=["hayvancılık","çiftçi"],negative=["tarım"])


# In[56]:


model.most_similar('çiftçi')


# In[57]:


def analogy(x1, x2, y1):
    result = model.most_similar(positive=[y1, x2], negative=[x1])
    return result[0][0]


# In[58]:


model.most_similar('gübre')


# In[59]:


analogy('gübreler','yağlar','ilaç')

