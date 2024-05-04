import torch

t = torch.empty(2,4)

num_r = t.size(0)
num_c = t.size(1)

for i in range(num_r):
    for j in range(num_c):
        c = i+j
        t[i,j] = c
        

print(t)