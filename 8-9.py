# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:06:33 2021

@author: yeji
"""

file_dir = "C:/Users/yuyae/Downloads"
#%% 8 Translating RNA into Protein
d_codon = {
        'UUU':'F','CUU':'L','AUU':'I','GUU':'V',
        'UUC':'F','CUC':'L','AUC':'I','GUC':'V',
        'UUA':'L','CUA':'L','AUA':'I','GUA':'V',
        'UUG':'L','CUG':'L','AUG':'M','GUG':'V',
        'UCU':'S','CCU':'P','ACU':'T','GCU':'A',
        'UCC':'S','CCC':'P','ACC':'T','GCC':'A',
        'UCA':'S','CCA':'P','ACA':'T','GCA':'A',
        'UCG':'S','CCG':'P','ACG':'T','GCG':'A',
        'UAU':'Y','CAU':'H','AAU':'N','GAU':'D',
        'UAC':'Y','CAC':'H','AAC':'N','GAC':'D',
        'UAA':'Stop','CAA':'Q','AAA':'K','GAA':'E',
        'UAG':'Stop','CAG':'Q','AAG':'K','GAG':'E',
        'UGU':'C','CGU':'R','AGU':'S','GGU':'G',
        'UGC':'C','CGC':'R','AGC':'S','GGC':'G',
        'UGA':'Stop','CGA':'R','AGA':'R','GGA':'G',
        'UGG':'W','CGG':'R','AGG':'R','GGG':'G'
        }
with open("C:/Users/yuyae/Downloads/rosalind_prot.txt",'r') as f:    
    seq=f.read()
print(seq)
protein = ""
for i in range(0,len(seq),3):
    if d_codon[seq[i:i+3]] == "Stop":
        break
    else:
        protein += d_codon[seq[i:i+3]]
print(protein)

#%% 9 Finding a Motif in DNA
with open("%s/rosalind_subs.txt"%file_dir,'r') as f:    
    Seq1=f.readline().strip()
    Seq2=f.readline().strip()
print(Seq1)
print(Seq2)
for i in range(len(Seq1)-len(Seq2)):
    if Seq1[i:i+len(Seq2)] == Seq2:
        print(i+1,end=" ")
        