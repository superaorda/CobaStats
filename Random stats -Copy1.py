#!/usr/bin/env python
# coding: utf-8

# In[1]:


#mengimpor library
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
sns.set()


# In[2]:


# menentukan rataan 2 kelompok
rataan1 = 50
rataan2 = 51

# menentukan standar deviasi (variasi) -- sama untuk 2 kelompok
sd = 5

#ukuran sampel dua kelompok
sample1 = 45
sample2 = 40 


# In[3]:


# Generate bilangan random
test = np.random.randn(sample1)
test


# In[4]:


plt.plot(test)


# In[5]:


sns.histplot(test);


# In[6]:


# Generate data 
data1 = np.random.randn(sample1)*sd + rataan1
data2 = np.random.randn(sample2 )*sd + rataan2

# menggabungkan sample size (jumlah data)
kelompok_data = [sample1, sample2]

batas = [np.min(np.hstack((data1, data2))), np.max(np.hstack((data1, data2)))]


# In[7]:


batas


# In[8]:


# plot distribusi kedua kelompok (statistik deskriptif)
plt.figure(figsize=(7,5))

a = sns.distplot(data1, hist=False, label='Data 1')
a = sns.distplot(data2, hist=False, label='Data 2')

a.set(xlabel = 'Data', ylabel='Density')
plt.legend();


# In[9]:


# melakukan uji statistik (statistik inferential)
fig, ax = plt.subplots(1,2,figsize=(8,5), dpi = 200)

ax[0].violinplot(data1)
ax[0].plot(1+np.random.randn(sample1)/10, data1, 'o', color='green')
ax[0].set_ylim(batas)

ax[1].violinplot(data2)
ax[1].plot(1+np.random.randn(sample2)/10, data2, 'o', color='blue')
ax[1].set_ylim(batas)

#melakukan uji t-test
t,p = stats.ttest_ind(data1, data2)

# mencetak hasil t-test di judul
sigtxt = ('', ' TIDAK')
plt.title('Dua kelompok{} berbeda secara signifikan! t({})={}, p={}'.format(sigtxt[int(p>.05)],
                                                                           sum(kelompok_data)-2,
                                                                           np.round(t,2),
                                                                           np.round(p,6)))
plt.show()


# In[10]:


p


# In[ ]:




