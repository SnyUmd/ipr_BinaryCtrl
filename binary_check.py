#!/usr/bin/env python
# coding: utf-8

# In[117]:


a_data = bytes('あ', 'UTF-8')
print(a_data)

b_data = bytearray('あ', 'shift-jis')
print(b_data)

print('---------------')

b_data = bytes(b'abc')
print(b_data[0])

check = bytes([ord('a'), 99, 100])

if b_data == check:
    print('true')
print(ord('a'))


# In[ ]:





# In[118]:


def BinaryCheck0(bin_target, bin_check_word):
    for i in range(len(bin_target)):
        if bin_target[i] != bin_check_word[i]:
            print(i)
            return False
    return True


# In[119]:


def BinaryCheck1(bin_target, bin_check_word):
    result = list(range(0))


    for i in range(len(bin_target)):
        if bin_target[i] != bin_check_word[i]:
            result.append([i, bin_target[i]])
    return result


# In[122]:


res = BinaryCheck1(bytes(b'abc'), bytes([ord('a'), 99, 100]))
for a in res:
    print(a)


# In[ ]:




