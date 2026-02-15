#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas  as pd
df=pd.read_csv('customer_shopping_behavior.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[6]:


df.describe(include='all')


# In[ ]:





# In[ ]:





# In[7]:


df.isnull().sum()


# In[8]:


df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))


# In[9]:


df.isnull().sum()


# In[12]:


df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[13]:


df.columns


# In[14]:


#create column age_group
labels=['yound_adult','adult','middle-aged','senior']
df['age_group']=pd.qcut(df['age'], q=4, labels=labels)


# In[ ]:





# In[17]:


df[['age','age_group']].head(10)


# In[21]:


#create column purchase_frequency_days
frequency_mapping={
    'Fortnightly':14,
    'Weekly':7,
    'Monthly':30,
    'Quarterly':90,
    'Bi-Weekly':14,
    'Annually':365,
    'Every3 Months':90,
    
}
df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)


# In[22]:


df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[24]:


(df['discount_applied']==df['promo_code_used']).all()


# In[25]:


df.drop('promo_code_used', axis=1)


# In[40]:


get_ipython().run_line_magic('pip', 'install pymysql')


# In[41]:


from sqlalchemy import create_engine
import pandas as pd

username = "root"
password = "Kowsik111#"   # keep as is
host = "localhost"
port = "3306"             # MySQL default
database = "customer_behaviour"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)



table_name="customer"
df.to_sql(table_name, engine, if_exists="replace", index=False)

