#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[8]:


df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')
# To avoid encoding error, use unicode_escape


# In[9]:


df.shape


# In[10]:


df.head()


# In[11]:


df.info()


# In[14]:


#Drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[15]:


df.info()


# In[16]:


#Check for null values
pd.isnull(df).sum()


# In[17]:


df.shape


# In[18]:


#Drop null values
df.dropna(inplace=True)


# In[19]:


df.shape


# In[21]:


#change data type
df['Amount'] = df['Amount'].astype('int')


# In[22]:


df['Amount'].dtypes


# In[23]:


df.columns


# # Exploratory Data Analysis

# ### Gender

# In[24]:


ax = sns.countplot(x ='Gender' ,data = df)
for bars in ax.containers:  #To put labels in bar chart
    ax.bar_label(bars)


# In[25]:


df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount' , ascending=False)


# In[26]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount' , ascending=False)
sns.barplot(x = 'Gender' ,y= 'Amount' , data = sales_gen)


# ##### From above graph we can see that most of the buyers are females and even the purchasing power of female are greater than male

# ### Age

# In[27]:


df.columns


# In[28]:


ax = sns.countplot(data = df, x = 'Age Group' , hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[29]:


#Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index= False)['Amount'].sum().sort_values(by ='Amount', ascending=False)
sns.barplot(x ='Age Group' ,y= 'Amount', data= sales_age)


# ##### From above graphs we can see that most of the buyers are of age group between 26-35 female 

# ### State

# In[31]:


#Total number of orders from Top 10 states
sales_state = df.groupby(['State'], as_index= False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={ 'figure.figsize' : (16,5)})
sns.barplot(data= sales_state, x = 'State', y= 'Orders')


# In[32]:


#Total Amount from Top 10 states
sales_state = df.groupby(['State'], as_index= False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={ 'figure.figsize' : (16,5)})
sns.barplot(data= sales_state, x = 'State', y= 'Amount')


# ##### From above graphs we can see that most of  the orders & Total sales/Amount are from Uttar Pradesh, Maharashtra and Karnataka 

# ### Marital Status

# In[37]:


ax = sns.countplot(data = df, x = 'Marital_Status')
sns.set(rc={ 'figure.figsize' : (7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[52]:


sales_maritalstatus = df.groupby(['Marital_Status','Gender'], as_index= False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={ 'figure.figsize' : (6,5)})
sns.barplot(data = sales_maritalstatus, x = 'Marital_Status',y= 'Amount' , hue = 'Gender')


# #### From above graphs we can see that most of the buyers are married(women) and they havev high purchasing power

# ### Occupation

# In[46]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data= df, x= 'Occupation')
for bars in ax.containers:
    ax.bar_label(bars)


# In[47]:


sales_occupation = df.groupby(['Occupation'], as_index= False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={ 'figure.figsize' : (20,5)})
sns.barplot(data= sales_occupation, x = 'Occupation', y= 'Amount')


# #### From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# ### Product Category

# In[49]:


sns.set(rc={'figure.figsize':(22,5)})
ax = sns.countplot(data= df, x= 'Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)


# In[53]:


sales_pc = df.groupby(['Product_Category'], as_index= False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={ 'figure.figsize' : (22,5)})
sns.barplot(data= sales_pc, x = 'Product_Category', y= 'Amount')


# #### From above graphs we can see that most of the sold products are from Food, Clothing and Electronics & Gadgets category

# ### Product id

# In[54]:


sales_pi = df.groupby(['Product_ID'], as_index= False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={ 'figure.figsize' : (22,5)})
sns.barplot(data= sales_pi, x = 'Product_ID', y= 'Orders')


# In[57]:


#Top 10 most sold products ( same as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending= False).plot(kind='bar')


# ### Conclusion

# #### Married women age group 26-35 years from UP, Maharashtra and Karnataka working in IT, Healthcare and Aviation are more likely buy products from Food, Clothing and Electronics & Gadgets category

# In[ ]:




