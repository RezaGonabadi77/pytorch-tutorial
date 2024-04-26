import torch

t1 = torch.arange(20).reshape(4,-1)
print(t1, t1.size())

t1[t1 > 10] = 0
print(t1)