#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import plotly.express as px


# In[6]:


excel_file = 'vgsales'
sheet_name = 'vgsales'
df = pd.read_excel(excel_file,
                  sheet_name=sheet_name, header=0,usecols='A:K')
df.head()


# In[ ]:





# In[ ]:




