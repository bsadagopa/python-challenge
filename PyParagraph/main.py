
# coding: utf-8

# In[70]:


# Option4 : PyParagraph.py

import re
import os
import csv

input_data_1_txt = os.path.join("./", "paragraph_1.txt")
input_data_2_txt = os.path.join("./", "paragraph_2.txt")

files = [input_data_1_txt, input_data_2_txt]
#files = [input_data_1_txt]


# In[71]:


for file in files:
    print("--- Processing file: " + file + "---")
    
    words = re.findall(r'\w+', open(file).read())
    sentences = re.findall(r'\.', open(file).read())
    letters = re.findall(r'\S', open(file).read())
    
    #print("Number of words = " + str(len(words)))
    #print("Number of Sentences = " + str(len(sentences)))
    #print("Average sentence Length = " + str(len(words) / len(sentences)))  
    #print("Average letter count PER word = " + str(len(letters)/len(words)))
            
    output = (
        f"\nParagraph Analysis\n"
        f"----------------------------\n"
        f"Approximate Word Count: {len(words)}\n"
        f"Approximate Sentence Count: {len(sentences)}\n"
        f"Average Letter Count: {len(letters)/len(words)}\n"
        f"Average Sentence Length: {len(words) / len(sentences)}\n"
    )   
    
    print(output)

