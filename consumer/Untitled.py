
# coding: utf-8

# In[1]:


from boto import kinesis
kinesis = kinesis.connect_to_region("us-east-1")


# In[4]:


stream = kinesis.create_stream("BotoDemo", 1)


# In[2]:


kinesis.describe_stream("BotoDemo")


# In[3]:


kinesis.list_streams()

