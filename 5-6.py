# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:05:50 2021

@author: yeji
"""

file_dir = "C:/Users/yuyae/Downloads"
#%% 5 Computing GC Content
file = open("C:/Users/yuyae/Downloads/rosalind_gc.txt",'r')
content = file.read()
file.close()

d_content = {}
content = content.split(">")

for i in range(len(content)):
    content[i] = content[i].strip().split('\n')
    if content[i][0] == "":
        continue
    d_content[content[i][0]] = "".join(content[i][1:])

d_GC = {}
for i,j in d_content.items():
    d_GC[i] = (j.count('G')+j.count('C'))/len(j)*100
    
val = 0
for i,j in d_GC.items():
    if val < j:
        val = j
        keys = i
print(keys)
print(val)

#%% 6 Counting Point Mutations
with open("C:/Users/yuyae/Downloads/rosalind_hamm.txt",'r') as f:    
    seq1=f.readline()
    seq2=f.readline()
counts = 0
for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        counts+=1
print(counts)

