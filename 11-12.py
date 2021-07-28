# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:07:03 2021

@author: yeji
"""

file_dir = "C:/Users/yuyae/Downloads"
#%% 11 Finding a Shared Motif
file = open("C:/Users/yuyae/Downloads/rosalind_lcsm (1).txt",'r')
content = file.read()
file.close()

d_gene = {}
content = content.split(">")

for i in range(len(content)):
    content[i] = content[i].strip().split('\n')
    if content[i][0] == "":
        continue
    d_gene[content[i][0]] = "".join(content[i][1:])

key = list(d_gene.keys())[0]
result = {}
for i in range(len(d_gene[key]),1,-1):
    for l in range(0,len(d_gene[key])-i):
        find = d_gene[key][l:l+i]
        result[find] = 0
        for v in d_gene.values():
            if find in v:
                result[find] += 1
        if result[find] != len(d_gene):
            del result[find]
        else:
            break
    if len(result) >= 1:
        break
print(result)

#%% 12 Finding a Protein Motif
### in linux
#for var in $protein; do wget http://www.uniprot.org/uniprot/$var.fasta; done

import re

p = re.compile("N[^P][S][^P]")
p2 = re.compile("N[^P][T][^P]")

with open("rosalind_mprt.txt", "r") as handle:
    protein_name = handle.readlines()
for n in protein_name:
    name = n.strip()
    with open("{}.fasta".format(name), "r") as f:
        content = f.readlines()
    seq = content[1:]
    for s in range(len(seq)):
        seq[s] = seq[s].strip()
    seq = "".join(seq)

    result1 = p.finditer(seq)
    result2 = p2.finditer(seq)

    l_result = [int(r.start()) + 1 for r in result1]
    for r in result2:
        l_result.append(int(r.start()) + 1)
    l_result = list(set(l_result))
    l_result.sort()

    print(name)
    for i in l_result:
        print(i, end=" ")
    print()